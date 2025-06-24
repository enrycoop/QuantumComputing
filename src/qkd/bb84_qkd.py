from src.quantum.interface import QuantumDevice, Qubit


def sample_random_bit(device: QuantumDevice) -> bool:
    with device.using_qubit() as q:
        q.h()
        result = q.measure()
        q.reset()
    return result

def prepare_message_qubit(message: bool, basis: bool, q: Qubit) -> None:
    if message:
        q.x()
    if basis:
        q.h()

def measure_message_qubit(basis: bool, q: Qubit) -> bool:
    if basis:
        q.h()
    result = q.measure()
    q.reset()
    return result

def convert_to_hex(bits: list[bool]) -> str:
    return hex(int("".join(["1" if bit else "0" for bit in bits]),2))

def send_single_bit_with_bb84(your_device: QuantumDevice, eve_device: QuantumDevice) -> tuple:
    [your_message, your_basis] = [sample_random_bit(your_device) for _ in range(2)]

    eve_basis = sample_random_bit(eve_device)

    with your_device.using_qubit() as q:
        prepare_message_qubit(your_message, your_basis, q)

        # QUBIT SENDING...
        eve_result = measure_message_qubit(eve_basis, q)

    return ((your_message, your_basis), (eve_result, eve_basis))