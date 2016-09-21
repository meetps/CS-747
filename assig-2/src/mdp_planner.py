"""
MDP Planner
"""

import numpy as np
import sys

d_type = 'double'

def readMDP(file_path=None):
    f = open(file_path, 'r')
    nstates = int(f.readline())
    nactions = int(f.readline())
    rewards = np.zeros((nstates, nactions, nstates), dtype = d_type)
    transistion_p = np.zeros((nstates, nactions, nstates), dtype= d_type)

    results = []
    input_line = ''

    for i in range(nstates):
        for j in range(nactions):
            input_line = f.readline().split('\t')[:-1]
            results = [float(k) for k in input_line]
            rewards[i][j] = np.asarray(results, dtype=d_type)

    for i in range(nstates):
        for j in range(nactions):
            input_line = f.readline().split('\t')[:-1]
            results = [float(k) for k in input_line]
            transistion_p[i][j] = np.asarray(results, dtype='double')
    
    gamma = float(f.readline())
    return {'R': rewards, 'T': transistion_p, 'S':nstates, 'A':nactions, 'Y':gamma}

def planMDP(mdp=None):
    R, T = mdp['R'], mdp_data['T']
    V = np.zeros((mdp['S'],1), dtype=d_type)
    P = np.zeros((mdp['S'],1),dtype='int')
    V_prev = np.zeros((mdp['S'],1), dtype=d_type)
    df = mdp['Y']
    eps = 0.000001
    count = 0
    while True:
        print count
        count += 1
    # for n in range(10):
        V_prev = np.copy(V)
        for i in range(mdp['S']):
            index = 0
            max_a = 0.0
            for j in range(mdp['A']):
                sum_a = 0.0
                for k in range(mdp['S']):
                    sum_a += T[i][j][k] * (R[i][j][k] + df * V_prev[k])
                if max_a < sum_a:
                    max_a = sum_a
                    index = j
            V[i] = max_a
            P[i] = index
        if abs(V_prev - V).all() < eps:
            return V, P

def printOptimalPolicy(v, pi):
    for i in range(len(v)):
        print v[i], pi[i]

if __name__ == '__main__':
    mdp_file_path = sys.argv[1]

    # Read MDP file
    mdp_data = readMDP(mdp_file_path)

    # Obtain optimal policy
    v_star, pi_star = planMDP(mdp_data)

    # Print Optimal policy into file & CLI
    printOptimalPolicy(v_star, pi_star)
