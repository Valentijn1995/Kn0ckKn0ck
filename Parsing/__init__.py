"""
    The Parsing package contains classes which can be used to read the proxy file. The proxy file contains information
    about the proxies that will be used during de DOS attack. The proxy file is supplied be the user in a supported
    format.

    This package contains the ProxyExtractor and the Readers sub-package. The classes in the Readers package are
    responsible for reading the proxy file but are not aware of de meaning of the data which whey are reading. Readers
    supply a generic interface to the Extractors. An Extractor class readers the data supplied by the Readers and gives
    meaning to it but does not know the format of the data (CSV, JSON, XML, FLAT file, ...).

    So the difference between Readers and Extractors is short:

    - Readers know format of the data but do not know what the data means.
    - Extractors do not know the format of the data but do know what the data means.

    How to create a proxy file:

    - At first you will need to choose a supported format to write you proxy file in. The CSV format is the only
        supported format at the moment so you don't really has van choice.
    - You can create a CSV file with a text editor like notepad or a spreadsheet program like Libre Office Calc.
    - You will need to write the header of the CSV file. The Header has to contain the following columns:
        - Address
        - Port
        - Type
        - Auth method
        - Username
        - Password

        You can add extra headers like Comment or Proxy name to the header. Kn0ckKn0ck will just ignore them.
        The order of the headers is also no problem. You can begin with Type and end with Address if this is more
        convenient for you.
    - The last step is to fill the CSV file with proxy information. cells are separated by a comma and rows are
        separated by a newline.

    Example:

        Address,Port,Type,Auth method,Username,Password
        127.0.0.1,8080,http,none,,
        example.com,8000,http,basic,Admin,Welcome1
"""