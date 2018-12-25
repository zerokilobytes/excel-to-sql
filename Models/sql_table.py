

"""
SQLTable
Generates the sql table for creating the sql table command
"""


class SQLTable:

    def __init__(self, header, sql_rows_arr, table_name):
        self.header = header
        self.sql_rows_arr = sql_rows_arr
        self.table_name = table_name

    def __str__(self):   #: -> Array
        column_sizes = {}

        #: Set the sql column and find the maximum size for each column
        for row in self.sql_rows_arr:
            row_values = row.get_values()
            for col_index in range(0, len(row_values)):
                col_name = self.header.get_headers()[col_index]
                if column_sizes.get(col_name):
                    column_sizes[col_name] = max(column_sizes[col_name], len(row_values[col_index]))
                else:
                    column_sizes[col_name] = max(len(row_values[col_index]), 0)

        #: Formats each column for table create
        fields_str = ",".join(
            "\n   {0} VARCHAR({1})".format(key, str(value))
            for key, value in column_sizes.items()
        )

        return (
                "CREATE TABLE {0} \n({1}\n);\n\n".format(self.table_name, fields_str)
        )
