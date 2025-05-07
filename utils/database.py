# utils/database.py
import sqlite3
import pandas as pd
from sqlalchemy import create_engine

class DatabaseManager:
    def __init__(self, db_path=':memory:'): # Mặc định database sẽ được lưu trong bộ nhớ
        self.db_path = db_path
        self.engine = create_engine(f'sqlite:///{db_path}')

    def create_table(self, table_name, columns):
        """Tạo bảng mới với các cột được chỉ định."""
        columns_str = ', '.join([f'{col} TEXT' for col in columns])
        with sqlite3.connect(self.db_path) as conn:
            conn.execute(f'CREATE TABLE IF NOT EXISTS {table_name} ({columns_str})')

    def insert_data_from_csv(self, csv_file, table_name):
        """Đọc dữ liệu từ file CSV và chèn vào bảng."""
        df = pd.read_csv(csv_file)
        df.to_sql(table_name, self.engine, if_exists='replace', index=False)

    def select_data(self, table_name, limit=1):
        """Lấy dữ liệu từ bảng."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(f'SELECT * FROM {table_name} LIMIT {limit} OFFSET 2')
            return cursor.fetchone()

    def select_all_data(self, table_name):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(f'SELECT * FROM {table_name}')
            return cursor.fetchall()