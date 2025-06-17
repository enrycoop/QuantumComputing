import numpy as np

# usiamo la libreria numpy per rappresentare i vettori
ket0 = np.array([[1], [0]])
ket1 = np.array([[0], [1]])

# numpy rappresenta i vettori 2x1 come colonne
print(f'|0> = {ket0}\n')

#costruiamo altri stati come |+> il quale è una combinazione lineare di |0> e |1>
ket_plus = (ket0 + ket1) / np.sqrt(2)
print(f'|+> = {ket_plus}')

# l'operazione di Hadamard trasforma
# |0> in |+>
# |1> in |->
H = np.array([[1, 1], [1, -1]]) / np.sqrt(2)

print(f"H|0> = {H @ ket0}\n")
print(f"H|1> = {H @ ket1}\n")


# il NOT può essere espresso come la trasformazione X
X = np.array([[0, 1], [1, 0]])
print(f"X|0> = {X @ ket0}\n")
print(f"X|1> = {X @ ket1}\n")

print(f'(X @ ket0 == ket1).all() = {(X @ ket0 == ket1).all()}')
print(f'X @ H @ ket0 = {X @ H @ ket0}')






