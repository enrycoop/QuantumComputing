from abc import ABCMeta, abstractmethod
from contextlib import contextmanager

class Qubit(metaclass=ABCMeta):
    @abstractmethod
    def h(self):
        pass

    @abstractmethod
    def measure(self) -> bool:
        pass

    @abstractmethod
    def reset(self):
        pass


class QuantumDevice(metaclass=ABCMeta):
    # Metodo che consente agli utenti di ottenere Qubit
    @abstractmethod
    def allocate_qubit(self) -> Qubit:
        pass

    @abstractmethod
    def deallocate_qubit(self, qubit: Qubit):
        pass

    # Possiamo fornire un gestore del contesto Python per semplificare l'allocazione
    # e la deallocazione dei qubit in modo sicuro
    @contextmanager
    def using_qubit(self):
        qubit = self.allocate_qubit()
        try:
            yield qubit
        finally:
            qubit.reset()
            self.deallocate_qubit(qubit)

