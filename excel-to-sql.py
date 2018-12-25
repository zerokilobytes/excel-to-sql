#!/usr/bin/python3
from xlrd import open_workbook
import time
from Models.sql_sheet import SQLSheet
import glob
import os

"""
Excel to SQL tool
Generates SQL statements for an Excel workbook
"""

os.chdir(".")
for filename in glob.glob("*.xls*"):
    wb = open_workbook(filename)

    #: Set directory and file names
    file_base_name = filename.rsplit('.', 1)[0]
    base_directory = os.path.dirname(__file__)
    directory = os.path.join(base_directory, file_base_name)

    for sheet in wb.sheets():
        sql_sheet = SQLSheet(sheet)
        sql_sheet.create(directory)
    #: Move excel sheet to new directory
    os.rename(base_directory + "/" + filename, base_directory + "/" + file_base_name + "/" + filename)
    print('SQL Generated Successfully in ' + base_directory + "/" + file_base_name)

print('Tasks Completed Successfully.')
time.sleep(1)
