from copy import copy


class Table:
    """
        Simple implementation of a table. The Table class helps with accessing table structured data.
    """
    def __init__(self, header, body):
        """
            Initiates a new table.

            :param header: Table headers in the form of a list. Example: ['Name', 'Surname', 'Age']
            :param body: Table body. Example: [['Jon', 'Doe', 25], ['Jane', 'Doe', 24]]
        """
        header_length = len(header)
        self._check_body_length(body, header_length)
        self._header = header
        self._body = body

    @property
    def header(self):
        # I make a copy because the header can be changed externally. These changes could reflect back at the table
        return copy(self._header)

    @property
    def body(self):
        return copy(self._body)

    @staticmethod
    def _check_body_length(body, header_length):
        """
            Checks if the length of each row is the same as the table header length.

            :param body: The table body
            :param header_length: The length of the table header
            :raises ValueError: when the rows do not check up
        """
        for index, row in enumerate(body):
            if len(row) is not header_length:
                raise ValueError('Row at index ' + str(index) + " is not of the same length as the table header")

    def _get_column_index(self, column_name):
        """
            Gets the index of a given column_name.

            :param column_name: Name of the column. Example: 'Surname'
            :return: The index of the column (1 in the case of the example).
        """
        return self._header.index(column_name)

    def _parse_column(self, column):
        """
            Check if the given column is an index or name.

            :param column: The column to parse
            :return: The index of the column
        """
        if isinstance(column, str):
            index = self._get_column_index(column)
        elif isinstance(column, int):
            index = column
        else:
            raise TypeError('Column has to be a string or an integer value')
        return index

    def get_row(self, index):
        """
            Gets the row at the given index. The first row has an index of zero.

            :param index: The index of the row (int)
            :return: The row at the given index. Example get_row(1) -> ['Jane', 'Doe', 24]
        """
        return self._body[index]

    def get_column(self, column):
        """
            Get a specific column.

            :param column: The name (str) or index (int) of the column
            :return: The requested column. Example: get_column('Name') -> ['John', 'Jane']
        """
        column_index = self._parse_column(column)
        column_array = []
        for row in self._body:
            column_array.append(row[column_index])
        return column_array

    def get_cell(self, column, row_index):
        """
            Get the value of a specific call in the table

            :param column: The name (str) or index (int) of the column
            :param row_index: The index of the table row
            :return: The value of the cell at the given column and row.
        """
        column_index = self._parse_column(column)
        cell = self._body[row_index][column_index]
        return cell

    def get_row_count(self):
        """
            Gets the amount of rows in the table

            :return: The amount of rows (as int)
        """
        table_length = len(self._body)
        return table_length

    # TODO implement __str__() method so you can print the contents of the table
