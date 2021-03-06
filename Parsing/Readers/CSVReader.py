from Reader import Reader
from Table import Table


class CSVReader(Reader):
    """
        The CSVReader is used to read CSV files.
    """

    def __init__(self, file_path, row_separator='\n', column_separator=','):
        """
            Creates a new instance of the CSVReader.

            :param file_path: The file_path to the csv file
            :param row_separator: The separator used for separating the rows (',' by default)
            :param column_separator: The separator used for separating the columns ('\n' by default)
        """
        Reader.__init__(self)
        self._row_separator = row_separator
        self._column_separator = column_separator
        self._init_data(file_path)

    def _init_data(self, file_path):
        """
            Initializes the CSV data. Uses the read_file method to read the data from the file and uses the
            parse_file_content and extract_header methods to process the data.

            :param file_path: File path to the CSV file.
        """
        # TODO Use standard csv python module to read the csv file instead of using own parser.
        try:
            file_content = self._read_file(file_path)
            table_with_header = self._parse_file_content(file_content)
            table_header, table_body = self._extract_header(table_with_header)
            self._table = Table(table_header, table_body)
        except ValueError as error:
            raise ValueError("Failed to parse the CSV file at '" + file_path + "'. " + error.message)
        except IOError:
            raise ValueError("Could not read the proxy file. Check if the file path is correct and if the file is "
                             "readable")

    @staticmethod
    def _read_file(file_path):
        """
            Read a file and return its contents.

            :param file_path: Path to the file
            :return: The file content (as string)
        """
        file_to_read = open(file_path, 'r')
        file_content = file_to_read.read()
        file_to_read.close()
        if not file_content:
            raise ValueError("File is empty")
        else:
            return file_content

    def _parse_file_content(self, content):
        """
            Convert the content of the CSV file to table like structure ([[row],[row]])

            :param content: The content of the CSV file (in string form)
            :return: list with innerlists as rows (table header included)
        """
        rows = content.split(self._row_separator)
        if len(rows) > 0:
            table = []
            for row in rows:
                cells = row.split(self._column_separator)
                table.append(cells)
            return table
        else:
            raise ValueError("Could not parse the rows. Make sure you use the '" + self._row_separator +
                             "' to separate the rows")

    @staticmethod
    def _extract_header(table):
        """
            Extracts the header from the table data generated by the parse_file_content method.

            :param table: The table structure genarated by the parse_file_content method
            :return: Header and table as separate objects
        """
        header_index = 0
        header = table[header_index]
        del table[header_index]
        return header, table

    def get_value(self, value_name, index):
        value = self._table.get_cell(value_name, index)
        return value

    def value_exists(self, value_name):
        return value_name in self._table.header

    def get_item(self, index):
        row = self._table.get_row(index)
        header = self._table.header
        item_dict = {}
        for index, header_name in enumerate(header):
            item_dict[header_name] = row[index]
        return item_dict

    def get_count(self):
        return self._table.get_row_count()
