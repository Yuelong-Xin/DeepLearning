import torch

X = torch.tensor([1, 3, 5, 2])
Y = torch.tensor([2, 4, 6, 7])
Z = torch.zeros_like(Y)
print(Z)
before = id(Z)
Z[:] = Y + X
after = id(Z)
print(Z)
print(before)
print(after)
print(after==before)