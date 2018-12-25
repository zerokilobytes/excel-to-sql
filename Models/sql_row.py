import xlrd
import datetime

from Models.constants import Constants
from Models.utililty import Utility

"""
SQLRow
Generates the sql statement for list of values
"""


class SQLRow(object):

    def __init__(self, header, table_name):
        self.table_name = table_name
        self.header = header
        self.values_arr = []

    def __str__(self):   #: -> str
        #: Returns the SQL insert statement
        header_str = ", ".join(str(x) for x in self.header.get_headers())
        values_str = ", ".join(str("'" + x + "'") for x in self.values_arr)

        return (
            "INSERT INTO {0} ({1}) VALUES ({2});"  .format(self.table_name, header_str, values_str)
        )

    def set_values(self, sheet, index):   #: -> void
        #: Sets the list of values for the row item
        number_of_columns = sheet.ncols

        for col in range(number_of_columns):
            cell = sheet.cell(index, col)
            value = cell.value

            #: Check the cell type and convert to date if necessary
            if cell.ctype == xlrd.XL_CELL_DATE:
                data_int = Utility.int_try_parse(value)
                date_tuple = xlrd.xldate_as_tuple(data_int, Constants.WB_DATE_MODE)
                date = datetime.date(date_tuple[0], date_tuple[1], date_tuple[2])
                # required format for xsd:Date type, for web service call
                value = date.isoformat()
            else:
                value = str(value).replace("'", "''").strip()

            try:
                value = str(int(value)).strip()
            except ValueError:
                pass
            finally:
                self.values_arr.append(value)

    def get_values(self):   #: -> List[str]
        #: Returns the list of values for the row item
        return self.values_arr
