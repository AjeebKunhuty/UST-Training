from queue import Empty
import threading
from sqlalchemy import create_engine 
from sqlalchemy.sql import text
import os


class PostgresMasterScheduler(threading.Thread):
    def __init__(self, input_queue, **kwargs):
        if 'output_queue' in kwargs:
            kwargs.pop('output_queue')
        super(PostgresMasterScheduler, self).__init__(**kwargs)
        self._input_queue = input_queue
        self.start()
    
    def run(self):
        while True:
            try:
                val = self._input_queue.get(timeout = 60)
            except Empty:
                print("Timeout reached in Postgres scheduler, exiting.")
                break
            if val == 'DONE':
                break

            symbol, price, extracted_time = val
            postgresWorker = PostgresWorker(symbol, price, extracted_time)
            postgresWorker.insert_into_db()



PG_USER = os.environ.get('PG_USER') or ''
PG_PASSWORD = os.environ.get('PG_PW') or ''
PG_HOST = os.environ.get('PG_HOST') or 'localhost'
PG_DB = os.environ.get('PG_DB') or 'postgres'
PG_PORT = os.environ.get('PG_PORT') or '5433'

engine = create_engine(f"postgresql://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{PG_DB}",
                       pool_size=5,
                       max_overflow=10)


class PostgresWorker():
    def __init__(self, symbol, price, extracted_time):
        self._symbol = symbol
        self._price = price
        self._extracted_time = extracted_time
        

    def create_insert_query(self):
        # Code to create SQL insert query
        SQL = """INSERT INTO prices (symbol, price, extracted_time) VALUES 
        (:symbol, :price, :extracted_time)"""
        return SQL

    def insert_into_db(self):
        # Code to insert data into PostgreSQL database
        insert_query = self.create_insert_query()
        with engine.begin() as connection:
            connection.execute(text(insert_query),{'symbol': self._symbol,
                                                    'price': self._price,
                                                    'extracted_time': self._extracted_time})
            print(f"Inserted {self._symbol}, {self._price}, {self._extracted_time} into DB")
            