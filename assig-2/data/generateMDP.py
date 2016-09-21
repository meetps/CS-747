"""To execute, run:
python3 generateMDP.py > mdp.txt
"""
import random, sys

random.seed(sys.argv[1])

S = 100
A = 100

print(S)
print(A)

R = [[[random.uniform(-1, 1) for s_ in range(S)] for a in range(A)] for s in range(S)]

for s in range(0, S):
    for a in range(0, A):
        for sPrime in range(0, S):
            print(str(R[s][a][sPrime]) + "\t", end="")
        print()

T = [[[random.uniform(0, 1) for s_ in range(S)] for a in range(A)] for s in range(S)]

# normalize so that probabilities add to one.
for s in range(0,S):
	for a in range(0, A):
		total = sum(T[s][a])
		T[s][a] = [val / total for val in T[s][a]]

for s in range(0, S):
    for a in range(0, A):
        for sPrime in range(0, S):
            print(str(T[s][a][sPrime]) + "\t", end="")
        print()

gamma = random.random() # 0 <= gamma  < 1
print(gamma)
