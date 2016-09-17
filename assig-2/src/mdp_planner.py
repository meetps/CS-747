"""
MDP Planner
"""

import numpy as np
import sys

def readMDP(file_path=None):
    pass

def planMDP(nstates=0, nactions=0, rewards=[], transistion_p=[]):
    pass

def printOptimalPolicy(policy):
    pass

if __name__ == '__main__':
    mdp_file_path = sys.argv[1]

    # Read MDP file
    mdp_data = readMDP(mdp_file_path)

    # Obtain optimal policy
    opt_policy = planMDP(mdp_data)

    # Print Optimal policy into file & CLI
    printOptimalPolicy(opt_policy)
