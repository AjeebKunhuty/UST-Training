import threading
import requests
from bs4 import BeautifulSoup

class WikiWorkerMasterScheduler(threading.Thread):
    def __init__(self, output_queue, **kwargs):
        if 'input_queue' in kwargs:
            kwargs.pop('input_queue')

        self.input_values = kwargs.pop('input_values')
       
        temp_queue = output_queue
        if type(temp_queue) is not list:
            temp_queue = [temp_queue]
        self._output_queues = temp_queue
        super(WikiWorkerMasterScheduler, self).__init__(**kwargs)
        self.start()

    def run(self):
        for entry in self.input_values:
            wikiWorker = WikiWorker(entry)
            symbols = list(wikiWorker.get_sp_500_companies())
            # print(symbols[:10])  # Print first 10 symbols for verification
            symbol_counter = 0
            for symbol in symbols[:]:
                for output_queue in self._output_queues:
                    output_queue.put(symbol)
                symbol_counter += 1
                if symbol_counter >= 5:
                    break
        
        # for output_queue in self._output_queues:
        #     for i in range(len(self._output_queues) * 20):  # Assuming 20 YahooFinance workers
        #         output_queue.put('DONE')

class WikiWorker():
    def __init__(self, url):
        self._url = url
        self._headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Accept": "text/html,application/json",
}

    @staticmethod
    def _extract_company_symbols(page_html):
        soup = BeautifulSoup(page_html, 'lxml')
        table = soup.find(id='constituents')
        table_rows = table.find_all('tr')
        for table_row in table_rows[1:]:
            symbol = table_row.find_all('td')[0].text.strip()
            yield symbol

    def get_sp_500_companies(self):
        response = requests.get(self._url, headers=self._headers)
        if response.status_code != 200:
            print("Failed to retrieve data from Wikipedia")
            return []
        
        yield from self._extract_company_symbols(response.text)
        