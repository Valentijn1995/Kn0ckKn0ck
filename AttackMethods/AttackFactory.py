from Proxies.Destination import Destination
from Proxies.NoProxy import NoProxy
from HttpAttack import HTTPAttack
from TCPAttack import TCPAttack


def create_attack(target_address, target_port, proxy=NoProxy(), attack_type="tcp"):
    """
        The AttackFactory is responsible for creating AttackMethods.

        :param attack_type: The type of attack you want to launch against your target (default= tcp).
        :param proxy: The proxy that the attack method will use to send data through (default= NoProxy).
        :param target_port: The port of the DOS target
        :param target_address: The address of the DOS target
        :raises ValueError: when attack_type is not recognised as a valid attacktype
    """
    target_dest = Destination(target_address, target_port)

    if attack_type == "tcp":
        return TCPAttack(proxy, target_dest)
    elif attack_type == "http":
        return HTTPAttack(proxy, target_dest)
    else:
        raise ValueError(attack_type.__str__() + " is not recognised as a valid attacktype")
