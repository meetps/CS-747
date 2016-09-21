"""
MDP Planner
"""

import sys
import numpy as np

from multiprocessing import Pool

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
    return rewards, transistion_p, nstates, nactions, gamma

def getValueIndex(i):
    index = 0
    max_a = 0.0
    for j in range(A):
        sum_a = 0.0
        for k in range(S):
            sum_a += T[i][j][k] * (R[i][j][k] + df * V_prev[k])
        if max_a < sum_a:
            max_a = sum_a
            index = j
    return {'V':max_a, 'T':index}

def planMDP(V_prev,V):
    eps = 0.000001
    count = 0
    while True:
        # print count, np.mean(abs(V_prev - V))
        count += 1
    # for n in range(10):
        V_prev = np.copy(V)
        p = Pool(10)
        d = p.map(getValueIndex, range(S))
        V = [l['V'] for l in d]
        print V
        P = [l['T'] for l in d]
        # V = d['V']
        # P = d['P']
        # for i in range(S):
        #     index = 0
        #     max_a = 0.0
        #     for j in range(A):
        #         sum_a = 0.0
        #         for k in range(S):
        #             sum_a += T[i][j][k] * (R[i][j][k] + df * V_prev[k])
        #         if max_a < sum_a:
        #             max_a = sum_a
        #             index = j
        #     V[i], p[i] = max_a
            # P[i] = index
        if abs(V_prev - V).all() < eps:
            return V, P

def printOptimalPolicy(v, pi):
    for i in range(len(v)):
        print str(v[i]) + '\t' + str(pi[i])

if __name__ == '__main__':
    mdp_file_path = sys.argv[1]

    # Read MDP file
    R,T,S,A,df = readMDP(mdp_file_path)

    V = np.zeros((S,1), dtype=d_type)
    P = np.zeros((S,1),dtype='int')
    V_prev = np.zeros((S,1), dtype=d_type)

    # Obtain optimal policy
    v_star, pi_star = planMDP(V_prev,V)

    # Print Optimal policy into file & CLI
    printOptimalPolicy(v_star, pi_star)
