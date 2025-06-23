import numpy as np

from src.quantum.interface import Qubit
from src.quantum.interface import QuantumDevice

KET_0 = np.array([
    [1],
    [0]
], dtype=complex)

H = np.array([
    [1, 1],
    [1, -1]
], dtype=complex) / np.sqrt(2)

X = np.array([
    [0, 1],
    [1, 0]
], dtype=complex) / np.sqrt(2)

class SimulatedQubit(Qubit):
    def __init__(self):
        self.reset()

    def h(self):
        self.state = H @ self.state

    def measure(self):
        """Pr(misurazione|stato)= |<misurazione|stato>|^2"""
        pr0 = np.abs(self.state[0,0]) ** 2 # P(0|KET_0) = |<0|0>|^2
        sample = np.random.random() <= pr0 # generiamo numero random tra 0 e 1 e controlliamo se <= alla probabilità
        return bool(0 if sample else 1)

    def reset(self):
        self.state = KET_0.copy()

    def x(self):
        self.state = X @ self.state

class SingleQubitSimulator(QuantumDevice):
    available_qubits = [SimulatedQubit()]

    def allocate_qubit(self) -> SimulatedQubit:
        if self.available_qubits:
            return self.available_qubits.pop()

    def deallocate_qubit(self, qubit: SimulatedQubit):
        self.available_qubits.append(qubit)

