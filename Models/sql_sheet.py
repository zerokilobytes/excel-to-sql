import re
import os
import errno

from Models.sql_row import SQLRow
from Models.sql_header import SQLHeader
from Models.sql_table import SQLTable
from Models.constants import Constants


"""
SQLSheet
Generates the sql table for the Excel spreadsheet
"""


class SQLSheet:
    def __init__(self, sheet):
        #: self.wb = wb
        self.sql_rows_arr = []
        self.sheet = sheet
        self.directory = ''
        self.header = None
        self.table_name = None

    def create(self, directory):   #: -> Void
        #: Created the sql table for the spreadsheet

        self.directory = directory
        self.table_name = re.sub('[^0-9a-zA-Z]+', '_', self.sheet.name).upper()
		#: Replace SQL keywords
        if self.table_name in Constants.key_words:
            self.table_name = self.table_name + '_'

        number_of_rows = self.sheet.nrows

        header = SQLHeader(self.sheet)
        header.get_headers()

        for row_index in range(1, number_of_rows):
            sql_row = SQLRow(header, self.table_name)
            sql_row.set_values(self.sheet, row_index)
            self.sql_rows_arr.append(sql_row)

        self.write(header)

    def write(self, header):   #: -> Void
        sql_inserts = ""
        filename = os.path.join(self.directory, self.sheet.name + ".sql")

        #: Creates the directory if it does not exist
        if not os.path.exists(os.path.dirname(filename)):
            try:
                os.makedirs(os.path.dirname(filename))
            except OSError as exc:  # Guard against race condition
                if exc.errno != errno.EEXIST:
                    raise

        #: Builds the insert statements
        for row in self.sql_rows_arr:
            sql_inserts += str(row) + "\n"

        #: Opens file for writing
        text_file = open(filename, "w")

        #: Sets sql statements for creating table and inserting rows
        sql_create_table = SQLTable(header, self.sql_rows_arr, self.table_name)
        sql_select_table = "\n\n--SELECT * FROM {0}; \n\n".format(self.table_name)

        #: Writes file and then close it
        text_file.write(str(sql_create_table))
        text_file.write(str(sql_inserts))
        text_file.write(str(sql_select_table))
        text_file.close()
