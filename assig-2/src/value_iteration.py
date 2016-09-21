"""
File : MDP Planner | Value Iteration
Author : Meet Pragnesh Shah
Roll : 13D070003
"""

import sys
import numpy as np

from multiprocessing import Pool
from operator import add, mul

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
    V_a = [sum(map(mul,map(add,[df * value for value in V],reward),T[i][action])) for action,reward in enumerate(R[i])]
    max_a = max(V_a)
    index = V_a.index(max_a)
    return {'V':max_a, 'T':index}

def planMDP():
    global V
    global V_prev
    eps = 0.000001
    count = 0
    while True:
        V_prev = np.copy(V)
        d = map(getValueIndex, range(S))
        V, P = np.asarray([v['V'] for v in d]), [p['T'] for p in d]
        if abs(V_prev - V).all() < eps:
            return V.flatten(), P

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
    v_star, pi_star = planMDP()

    # Print Optimal policy into file & CLI
    printOptimalPolicy(v_star, pi_star)
