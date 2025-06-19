from interface import QuantumDevice
from src.qnrg.simulator import SingleQubitSimulator


def qrng(device: QuantumDevice):
    with device.using_qubit() as q:
        q.h()
        return q.measure()


if __name__ == "__main__":
    qsim = SingleQubitSimulator()
    for idx_sample in range(10):
        random_sample = qrng(qsim)
        print(f"Our QNRG returned {random_sample}.")