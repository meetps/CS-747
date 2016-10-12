"""
File : Sarsa with Eligibility Traces | Accumulation vs Replacement
Author : Meet Pragnesh Shah
Roll : 13D070003
"""

import sys
import random
import numpy as np
from itertools import product
from matplotlib import pyplot as plt

n_states       = int(sys.argv[1])
gamma          = float(sys.argv[2])
term_state     = n_states
n_actions      = 2
state          = 0

def apply_action(action):
    global state
    if action == 1:
        state += 1
    if state == term_state:
        return 1
    return 0


def eps_greedy_action(epsilon, p):
    if random.random() <= epsilon:
        return random.randint(0, len(p) - 1)
    else:
        return np.random.choice(np.where(p == np.amax(p))[0])


def sarsa(n_episodes=50, Lambda=0.9, epsilon=0.05, alpha=0.1, accumulate_trace=False):
    global state
    global gamma

    state_actions = list(product(range(n_states+1), range(n_actions)))
    Q_val         = np.random.random([n_states+1, n_actions])
    trace         = np.zeros([n_states+1, n_actions])
    steps_to_term = []

    for n in range(n_episodes):
        n_steps = 0
        trace = trace * 0
        state = 0
        s = state
        a = random.randint(0, Q_val.shape[1] - 1)
        while not state == term_state:
            r = apply_action(a)
            n_steps += 1
            s_prime = state
            a_prime = eps_greedy_action(epsilon, Q_val[s_prime, :])
            delta = r + gamma * Q_val[s_prime, a_prime] - Q_val[s, a]

            if accumulate_trace:
                trace[s, a] = trace[s, a] + 1
            else:
                trace[s, a] = 1
                
            for s, a in state_actions:
                Q_val[s, a] = Q_val[s, a] + alpha * delta * trace[s, a]
                trace[s, a] = gamma * Lambda * trace[s, a]
                
            s = s_prime
            a = a_prime
            
        steps_to_term.append(n_steps)
    return steps_to_term

def exp_instance(n_trials, n_episodes, accumulate_trace):
    alphas = np.linspace(0.1, 1, 10)
    results = np.array([])
    for alpha in alphas:
        res = []
        for i in range(n_trials):
            t = sarsa(n_episodes=n_episodes, alpha=alpha, accumulate_trace=accumulate_trace, epsilon=0.05, Lambda=0.9)
            res.append(np.mean(t))
        if results.shape[0] == 0:
            results = np.array([alpha, np.mean(res)])
        else:
            results = np.vstack([results, [alpha, np.mean(res)]])
    return results

def run_sarsa_exp(n_trials=100, n_episodes=50):
    trace_replaced    = exp_instance(n_trials, n_episodes, accumulate_trace=False)
    trace_accumulated = exp_instance(n_trials, n_episodes, accumulate_trace=True)

    plt.plot(trace_replaced[:, 0], trace_replaced[:, 1], label='Replaced Traces', c='b')
    plt.plot(trace_accumulated[:, 0], trace_accumulated[:, 1], label='Accumulated Traces', c='r')

    plt.legend()
    plt.title('n_states = ' + str(n_states) + " gamma = " + str(gamma) + " | " + str(n_episodes) + ' episodes stochastically averaged ' + str(n_trials) + ' times.')
    plt.xlabel('alpha')
    plt.ylabel('n_Steps to terminal state')
    # plt.show()
    # plt.savefig('../imgs/'  + str(term_state) + ".jpg")
    plt.savefig('../imgs/'  + str(gamma) + ".jpg")

if __name__ == '__main__':
    run_sarsa_exp(100,50)