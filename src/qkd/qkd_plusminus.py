from src.quantum.interface import Qubit, QuantumDevice


def prepare_classical_message_plusminus(bit: bool, q: Qubit) -> None:
    """Se vero lo stato di q viene negato"""
    if bit:
        q.x()
    q.h()

def eve_measure(q: Qubit) -> bool:
    q.h()
    return q.measure()

def send_classical_bit(device: QuantumDevice, bit: bool) -> None:
    with device.using_qubit() as q:
        prepare_classical_message_plusminus(bit, q)
        result = eve_measure(q)
        q.reset()
    assert result == bit