v = int(input(""))
a = int(input(""))
f = int(input(""))
p = int(input(""))


contasPagas = 0

if v >= a + f + p:
    contasPagas = 3

elif v >= a + f:
    contasPagas = 2

elif v >= a + p:
    contasPagas = 2

elif v >= f + p:
    contasPagas = 2

elif v >= a:
    contasPagas = 1

elif v >= f:
    contasPagas = 1

elif v >= p:
    contasPagas = 1

else:
    contasPagas = 0



print(contasPagas)