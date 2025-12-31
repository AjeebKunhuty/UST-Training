import datetime
import threading
import requests
import time
import random
from bs4 import BeautifulSoup
from queue import Empty
from lxml import html

class YahooFinancePriceScheduler(threading.Thread):
    def __init__(self, input_queue, output_queue, **kwargs):
        super(YahooFinancePriceScheduler, self).__init__(**kwargs)
        self._input_queue = input_queue
        temp_queue = output_queue
        if type(temp_queue) is not list:
            temp_queue = [temp_queue]
        self._output_queue = temp_queue
        self.start()

    def run(self):
        while True:
            try:
                val = self._input_queue.get()
            except Empty:
                print("Yahoo scheduler queue is empty, exiting.")
            if val == 'DONE':
                for q in self._output_queue:
                    q.put('DONE')
                break
            yahooFinanaceWorker = YahooFinanceWorker(symbol=val)
            price = yahooFinanaceWorker.get_price()
            for q in self._output_queue:
                q.put((val, price, datetime.datetime.utcnow()))
            # print(f"Price for {val} is {price}")
            time.sleep(random.random())  # Stagger requests to avoid being blocked

        # for q in self._output_queue:
        #     for i in range(20):  # Assuming 1 Postgres worker
        #         q.put('DONE')

class YahooFinanceWorker():
    def __init__(self, symbol, **kwargs):
        super(YahooFinanceWorker, self).__init__(**kwargs)
        self._symbol = symbol
        base_url = "https://finance.yahoo.com/quote/"
        self._url = f"{base_url}{self._symbol}"
        self._headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
                "Accept": "text/html,application/json",
                }
        # self.start()

    def get_price(self):
        time.sleep(30*random.random())  # Stagger requests to avoid being blocked
        response = requests.get(self._url, headers=self._headers)
        if response.status_code != 200:
            print(f"Failed to retrieve data for {self._symbol}\n")
            return
        
        page_contents = html.fromstring(response.text)
        price_xpath = '//*[@id="main-content-wrapper"]/section[1]/div[2]/div[1]/section/div/section/div[1]/div[1]/span'
        try:
            price = float(page_contents.xpath(price_xpath)[0].text.replace(',', ''))
            return price
        except ValueError:
            print(f"Could not convert price to float for {self._symbol}")
            return


# //*[@id="main-content-wrapper"]/section[1]/div[2]/div[1]/section/div/section/div[1]/div[1]/span

# <span class="yf-ipw1h0 base" data-testid="qsp-price">
# ::before
# "273.40"
# ::after
# </span>