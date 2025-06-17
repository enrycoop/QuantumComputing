from interface import QuantumDevice

def qrng(device: QuantumDevice):
    with device.allocate_qubit() as q:
        q.h()
    return q.measure()