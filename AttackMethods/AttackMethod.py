import thread
import threading
import abc
from time import sleep


class AttackMethod:
    """
        The AttackMethod class represents a DOS attack. The AttackMethod class is an abstract class and needs to be
        extended by other classes. An AttackMethod runs in its own thread. The thread loop starts when the
        start_attack() function is called and stops when the stop_attack() function is called.
    """
    __metaclass__ = abc.ABCMeta

    def __init__(self, proxy, target):
        """
            Constructor. Creates a new AttackMethod instance.

            :type target: Destination
            :type proxy: Proxy
        """
        self._proxy = proxy
        self._attack_is_active = False
        self._innerThread = None
        self._attack_lock = threading.Lock()
        self._attack_target = target
        self._loop_delay = 0.050
        self.exception = None

    def start_attack(self):
        """
            Starts the DOS attack.
        """
        self._attack_lock.acquire()
        if not self._attack_is_active:
            self._attack_is_active = True
            self._attack_lock.release()
            self._innerThread = thread.start_new_thread(self._thread_loop, ())
        else:
            self._attack_lock.release()

    def stop_attack(self):
        """
            Stops the attack loop.
        """
        self._set_attack_active(False)

    def has_exception(self):
        if not self.is_active():
            return self.exception is not None
        else:
            return False

    def get_exception(self):
        return self.exception

    def _thread_loop(self):
        """
            The main loop of the attack thread. This function is called by the attack thread and could not be called
            directly.
        """
        while self.is_active():
            try:
                self._attack_loop()
                sleep(self._loop_delay)
            except Exception as ex:
                self.exception = ex
                self.stop_attack()

    def is_active(self):
        """
            Checks the value of the _attack_is_active value in a thread safe was.
            Use this function to get the value of _attack_is_active instead of checking the value directly.

            :return: True if the attack is active and False otherwise
        """
        self._attack_lock.acquire()
        attack_active = self._attack_is_active
        self._attack_lock.release()
        return attack_active

    def _set_attack_active(self, value):
        """
            Thread-safe setter for the _attack_is_active value. This function is only for internal use.

            :param value: New value of the _attack_is_value value (True or False)
        """
        if not isinstance(value, bool):
            raise ValueError('set_attack_active value has to be a boolean and not a ' + type(value))

        self._attack_lock.acquire()
        self._attack_is_active = value
        self._attack_lock.release()

    @abc.abstractmethod
    def _attack_loop(self):
        """
            Part of the _thread_loop. This function has to be implemented by the class which extends from the
            AttackMethod class. The function gets called repeatedly until the stop_attack function gets called.
            The class which extends from this class has to implement it's attack logic in this function.
        """
        return
