primeiraLinha = input("").split(" ")
total = 0

for c in range(len(primeiraLinha)):
    primeiraLinha[c] = int(primeiraLinha[c])

sequencia = input("").split(" ")

for i in range(primeiraLinha[0]):
    sequencia[i] = int(sequencia[i])

subSequencia = input("").split(" ")

for t in range(primeiraLinha[1]):
    subSequencia[t] = int(subSequencia[t])

seq_index = 0
subseq_index = 0

while seq_index < len(sequencia) and subseq_index < len(subSequencia):
    if sequencia[seq_index] == subSequencia[subseq_index]:
        seq_index += 1
        subseq_index += 1
    else:
        seq_index += 1

if subseq_index == len(subSequencia):
    print("S")
else:
    print("N")
