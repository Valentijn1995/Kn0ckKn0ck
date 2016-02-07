import sys
import argparse
from AttackMethods import AttackFactory
from Proxies import ProxyFactory
from Proxies.MultiProxy import MultiProxy
from Parsing.ProxyExtractor import ProxyExtractor
from Parsing.Readers.CSVReader import CSVReader
from time import sleep

__author__ = 'Valentijn Harmers'
__description__ = 'Kn0ckKn0ck - Stress Testing tool'
__version__ = 0.1


def main(argv):
    """
        This is the main routine of Kn0ckKn0ck. The main routine parses the input of the user and
        launches the DOS attack by using the create_attack en start_attack_loop methods.

        :param argv: user arguments
    """

    # Parse the arguments of the user
    parser = argparse.ArgumentParser(description=__description__, version=str(__version__))
    parser.add_argument("address", help="Address of the DOS target", type=str, nargs='?', default="127.0.0.1" )
    parser.add_argument("port", help="Port of the DS target", type=int, nargs='?', default=80)
    parser.add_argument("-a", "--attack_type", help="Attacktype of the DOS attack [tcp|http]", type=str, default="tcp")
    parser.add_argument("-f", '--proxy_file', help="The file which contains proxy information [*.csv]", default=None)
    parser.add_argument("--no_warning", help="Do not show the attack warning",
                        action="store_true", default=False)
    parser.add_argument("--license", help="Show the program license and exit", action="store_true", default=False)
    parser_args = parser.parse_args(args=argv)

    if parser_args.license:
        print_license()
        sys.exit()

    # Create the attack
    try:
        proxy = create_proxy(parser_args.proxy_file)
        attack = create_attack(proxy, parser_args.address, parser_args.port, parser_args.attack_type)
    except ValueError as error:
        print "A value error has occurred while initiating the attack. Please check your input."
        print "Error message: " + error.message
        sys.exit(2)
    except NotImplementedError as error:
        print "You are tying to use functionality which is not implemented yet. Are you using the newest " \
              "version of Kn0ckKn0ck?"
        print "Error message:" + error.message
        sys.exit(2)

    if not parser_args.no_warning:
        start_attack = show_attack_warning(parser_args.address)
        if not start_attack:
            print "aborting the attack"
            sys.exit()

    print "Starting " + parser_args.attack_type + " attack against " + parser_args.address + ":" + str(parser_args.port)
    # Time to start the attack. The attack will stop when a KeyboardInterrupt is registered.
    start_attack_loop(attack)
    print "The attack has been stopped"
    sys.exit()


def create_attack(proxy, target_address, target_port, attack_type):
    """
        Create an AttackMethod object with the given parameters.

        :param proxy: Proxy object to use for this attack.
        :param target_address: The IP/Domain address of the DOS target
        :param target_port: The port of the DOS target
        :param attack_type: The attack type (tcp, http)
        :return: A new AttackMethod object with the given configurations
    """

    attack = AttackFactory.create_attack(target_address, target_port, proxy, attack_type)
    return attack


def create_proxy(proxy_file_path):
    """
        Creates a Proxy object.

        :param proxy_file_path: The path to the proxy file (can be None if you don't want to use a proxy)
        :return: This function can return different Proxies. The method will return a NoProxy object if the proxy_file
          _path is None, a MultiProxy object when the proxy file contain multiple proxy entries or a specific proxy
          object if here is only one proxy entry declared in the proxy file
        :raises ValueError: when the proxy file does not contain any proxy entries
    """
    if proxy_file_path is not None:
        proxy_list = read_proxy_file(proxy_file_path)
        proxy_list_len = len(proxy_list)

        if proxy_list_len > 1:
            proxy = MultiProxy(proxy_list)
        elif proxy_list_len is 1:
            proxy = proxy_list[0]
        else:
            raise ValueError("No proxy's found in proxy file")
    else:
        proxy = ProxyFactory.create_proxy(proxy_name='no-proxy')
    return proxy


def read_proxy_file(file_path):
    """
        Method used by the create_proxy method. Reads the file at the given file path and uses the CSVReader and
        ProxyExtractor classes from the Parsing module to convert the contents of the file to usable Proxy objects.

        :param file_path: Path to the proxy file
        :return: List with extracted Proxies. List will be empty if no proxies where found.
    """
    reader = CSVReader(file_path)
    extractor = ProxyExtractor(reader)
    proxy_list = extractor.get_all_proxies()
    return proxy_list


def show_attack_warning(address):
    """
        Shows a attack warning. The message warns the user about the dangers of DOS attacks.

        :param address: The address of the DOS target
        :return: True if the user wants to proceed with the attack and False if the user want to abort the attack
    """
    warning = """
You are about to launch a DOS attack against {addr}.

Always acquire permission from the owner of the targeted machine before launching an attack.
Launching a DOS attack against a machine without permission of the owner can be punishable by law.

The author of this program is not responsible for any damages.

    """.format(addr=address)

    print warning

    while True:
        answer = raw_input("Do you want to proceed with the attack? (yes/no)")
        if answer == "yes":
            return True
        elif answer == "no":
            return False
        else:
            print "please answer with yes or no."


def print_license():
    try:
        license_text = open('./LICENSE', 'r').read()
        print license_text
    except IOError:
        print "Could not read the LICENSE file. Make sure it's present!"
        sys.exit(2)


def start_attack_loop(attack):
    """
        This method contains the main attack loop. It will start the attack and stops the attack again where a
        KeyboardInterrupt is triggered. This is a blocking method. Call the start_attack and stop_attack methods of the
        AttackMethod object your self if you want to do stuff during the attack.

        :param attack: The AttackMethod object (created by the create_attack method)
    """
    try:
        attack.start_attack()
        # The attack sequence will run in a separate thread which leaves this thread with nothing to do.
        # Maybe in future releases this thread can be used to show something like a spinner or information about the
        # progress of the attack to the user.
        while True:
            sleep(1)
            if attack.has_exception():
                print "Attack stopped with an error. " + str(attack.get_exception())
                sys.exit(2)
    except KeyboardInterrupt:
        # stop the attack when the user presses Ctrl + c
        attack.stop_attack()


if __name__ == "__main__":
    main(sys.argv[1:])
