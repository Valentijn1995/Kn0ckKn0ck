from unittest import TestLoader, TextTestRunner, TestSuite
from UnitTests.TableTest import TestTable
from UnitTests.DestinationTest import TestDestination
from UnitTests.CSVReaderTest import TestCSVReader
from UnitTests.ProxyExtractorTest import TestProxyExtractor
from UnitTests.NoProtocolTest import TestNoProtocol
from UnitTests.HttpProtocolTest import TestHttpProtocol
from UnitTests.ProxyTest import TestProxy


def run_tests():
    suite_list = []

    suite_list.append(TestLoader().loadTestsFromTestCase(TestTable))
    suite_list.append(TestLoader().loadTestsFromTestCase(TestDestination))
    suite_list.append(TestLoader().loadTestsFromTestCase(TestCSVReader))
    suite_list.append(TestLoader().loadTestsFromTestCase(TestProxyExtractor))
    suite_list.append(TestLoader().loadTestsFromTestCase(TestNoProtocol))
    suite_list.append(TestLoader().loadTestsFromTestCase(TestHttpProtocol))
    suite_list.append(TestLoader().loadTestsFromTestCase(TestProxy))

    suite = TestSuite(suite_list)

    TextTestRunner(verbosity=2).run(suite)

if __name__ == "__main__":
    run_tests()
