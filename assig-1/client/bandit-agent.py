import sys
import socket
import time

from numpy import *

error_str = """
    Usage :
    python bandit-agent.py
    [--numArms numArms]
    [--randomSeed randomSeed]
    [--horizon horizon]
    [--explorationHorizon explorationHorizon]
    [--hostname hostname]
    [--port port]
    """

def update(trial_id, rewards, success):
    """
    Updates the state space based on received reward
    """
    trials[trial_id] = trials[trial_id] + 1
    # Since rewards are bernoulli, its just 0 or 1
    if (success):
        rewards[trial_id] = rewards[trial_id] + 1

def select_arm(n_arms, prior_params, rewards, trials):
    """
    Contructs beta distribution from the present state and
    takes random sample from it returns the arm index with
    the largest value.
    """
    sampled_theta = []
    for i in range(n_arms):
        sampled_theta.append(random.beta(prior_params[0]+rewards[i], prior_params[1]+trials[i]-rewards[i]))
    return sampled_theta.index(max(sampled_theta))

def get_arg(arguments):
    numArms = int(arguments[2])
    randomSeed = int(arguments[4])
    horizon = int(arguments[6])
    explorationHorizon = int(arguments[8])
    hostname = str(arguments[10])
    port = int(arguments[12])
    return numArms, randomSeed, horizon, explorationHorizon, hostname, port

if __name__ == '__main__':
    n_args = 6

    if len(sys.argv) != n_args * 2 + 1:
        sys.exit(error_str)
    else:
        n, s, h, eh, host, port = get_arg(sys.argv)

        s = socket.socket(socket.AF_INET)
        host = socket.gethostname()
        port = port
        s.connect((host, port))

        trials = zeros(shape=(n,), dtype=int)
        rewards = zeros(shape=(n,), dtype=int)
        prior_params = (1.0, 1.0)

        for i in range(h):
            arm_to_pull = select_arm(n, prior_params, rewards, trials)
            try:
                s.send(str(arm_to_pull) + '\n')
                print 'Sent arm to pull : ' + str(arm_to_pull)
            except:
                print 'Send Connection Error'

            time.sleep(0.005)

            try:
                raw_message = s.recv(512).rstrip('\0')
                receive_list = raw_message.replace(' ', '').split(',')
                print 'Received Message : ' + raw_message
            except:
                print 'Receive Connection Error'
            reward, n_pulls = int(receive_list[0]), int(receive_list[1])
            update(arm_to_pull, rewards, reward)
        s.close
