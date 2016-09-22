"""
File : MDP Planner | Policy Iteration
Author : Meet Pragnesh Shah
Roll : 13D070003
"""

import sys
import numpy as np

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

def getActionValue(i):
    V_a = [sum(map(mul,map(add,[df * value for value in V],reward),T[i][action])) for action,reward in enumerate(R[i])]
    max_a = max(V_a)
    index = V_a.index(max_a)
    return {'V':max_a, 'a':index}

def solveLP():
    rhs = np.zeros((S, 1), dtype=d_type)
    lhs = np.zeros((S, S), dtype=d_type)
    for i in range(S):
        lhs_s = np.zeros((S,1), dtype=d_type).flatten()
        sum_a = 0.0
        for j in range(S):
            sum_a += T[i][pi[i]][j] * R[i][pi[i]][j]
            if j == i:
                lhs_s[j] = -df*T[i][pi[i]][j] + 1.0
            else:
                lhs_s[j] = -df*T[i][pi[i]][j]
        lhs[i] = lhs_s
        rhs[i] = sum_a
    return np.linalg.solve(lhs, rhs)

def planMDP():
    global V
    has_converged = False
    while not has_converged:
        has_converged = True
        V = solveLP()
        D = map(getActionValue,range(S))
        action_val, index = [d['V'] for d in D], [d['a'] for d in D]

        for i in range(S):
            if(action_val[i] > V[i]):
                is_optimal = pi[i] == index[i]
                has_converged = has_converged and is_optimal
                pi[i] = index[i]
    return V.flatten(), pi

def printOptimalPolicy(v, pi):
    for i in range(len(v)):
        print str(format(v[i],'0.6f')) + '\t' + str(pi[i])

if __name__ == '__main__':
    mdp_file_path = sys.argv[1]

    # Read MDP file
    R,T,S,A,df = readMDP(mdp_file_path)

    pi = np.random.randint(0,A-1,size=S).flatten()
    V = np.zeros((S,1),dtype=d_type)

   # Obtain optimal policy
    v_star, pi_star = planMDP()

    # Print Optimal policy into file & CLI
    printOptimalPolicy(v_star, pi_star) 