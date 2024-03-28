import pytest
import os
from zipfile import ZipFile

current_file = os.path.abspath(__file__)
current_dir = os.path.dirname(current_file)
PROJECT = os.path.dirname(current_dir)
resource_dir = os.path.join(PROJECT, 'resource')
temp_dir = os.path.join(PROJECT, 'temp')
book_pdf_dir = os.path.join(temp_dir, 'book.pdf')
table_csv_dir = os.path.join(temp_dir, 'table.csv')
table_xlsx_dir = os.path.join(temp_dir, 'table.xlsx')
zip_dir = os.path.join(resource_dir, 'newzipfile.zip')

@pytest.fixture(scope='session', autouse=True)
def create_archive():
    if os.path.exists(zip_dir):
        pass
    else:
        with ZipFile(zip_dir, "a") as myzip:
            myzip.write(book_pdf_dir, 'book.pdf')
            myzip.write(table_xlsx_dir, 'table.xlsx')
            myzip.write(table_csv_dir, 'table.csv')
            print(myzip.namelist())