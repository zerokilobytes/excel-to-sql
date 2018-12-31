import re
from Models.constants import Constants

"""
SQLHeader
Get the list of headers in the sheet
"""


class SQLHeader(object):
    def __init__(self, sheet):
        self.number_of_columns = sheet.ncols
        self.headers = []

        #: Find each header in the first row only
        for row in range(0, 1):
            for col in range(self.number_of_columns):
                #: Get the value for the cell and remove spaces, none-numeric and none alpha characters
                key = sheet.cell(row, col).value
                key = key.strip()
                key = re.sub('[^0-9a-zA-Z]+', '_', key)

                #: Replace SQL keywords
                if key in Constants.key_words:
                    key = key + '_'

                #: Add the key to the list of keys
                self.headers.append(key)

    def get_headers(self):  #: -> List[str]
        #: Return the list of headers
        return self.headers

    def get_number_of_columns(self):  #: -> List[str]
        #: Returns list of columns
        return self.number_of_columns


