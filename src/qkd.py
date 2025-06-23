from src.interface import Qubit, QuantumDevice
from src.qnrg.qnrg import qrng
from src.simulator import SingleQubitSimulator


def prepare_classical_message(bit: bool, q: Qubit) -> None:
    """Se vero lo stato di q viene negato"""
    if bit:
        q.x()

def eve_measure(q: Qubit) -> bool:
    return q.measure()

def send_classical_bit(device: QuantumDevice, bit: bool) -> None:
    with device.using_qubit() as q:
        prepare_classical_message(bit, q)
        result = eve_measure(q)
        q.reset()
    assert result == bit

### NOI
qrng_simulator = SingleQubitSimulator()

key_bit = int(qrng(qrng_simulator))


qkd_simulator = SingleQubitSimulator()

with qkd_simulator.using_qubit() as q:
    prepare_classical_message(key_bit, q)
    print(f"You prepared the classical key bit: {key_bit}")
    ### EVE
    eve_measurement = int(eve_measure(q))
    print(f"Eve measured the classical key bit: {eve_measurement}")