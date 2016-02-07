import abc


class Reader:
    """
        Abstract class which defines the minimal functionality of Readers. You will need to extend from tis class
        if you want to create your own reader.
    """
    def __init__(self):
        pass

    @abc.abstractmethod
    def get_count(self):
        """
            Gets the amount of items in this Reader.

            :return: amount of items (int)
        """
        return

    @abc.abstractmethod
    def get_value(self, value_name, index):
        """
            Get a value from the reader.

            :param value_name: The name of the value
            :param index: The index of the value
            :return: The value with the given value name at the given index. Example get_value('Age', 0) -> 25
        """
        return

    @abc.abstractmethod
    def value_exists(self, value_name):
        """
            Checks if the given value name exists.

            :param value_name: The value name to check
            :return: True if the given value name exists in the Reader and False otherwise
        """
        return

    @abc.abstractmethod
    def get_item(self, index):
        """
            Get a dictionary with values and their names at a given index.

            :param index: Index of the values you want
            :return: A list with values. Example: ['Name': 'John', 'Surname': 'Doe', 'Age': 25]
        """
        return


