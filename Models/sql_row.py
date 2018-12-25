
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
            value = sheet.cell(index, col).value
            value = str(value).replace("'", "''")
            try:
                value = str(int(value)).strip()
            except ValueError:
                pass
            finally:
                self.values_arr.append(value)

    def get_values(self):   #: -> List[str]
        #: Returns the list of values for the row item
        return self.values_arr
