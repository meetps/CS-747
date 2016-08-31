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


class ThompsonSampling(object):
    def __init__(self, n_arms=2, prior_params=(1.0, 1.0)):
        self.trials = zeros(shape=(n_arms,), dtype=int)
        self.rewards = zeros(shape=(n_arms,), dtype=int)
        self.n_arms = n_arms
        self.prior_params = prior_params

    def update(self, trial_id, success):
        """
        Updates the state space based on received reward
        """
        self.trials[trial_id] = self.trials[trial_id] + 1
        # Since rewards are bernoulli, its just 0 or 1
        if (success):
            self.rewards[trial_id] = self.rewards[trial_id] + 1

    def select_arm(self):
        """
        Contructs beta distribution from the present state and
        takes random sample from it returns the arm index with
        the largest value.
        """
        sampled_theta = []
        for i in range(self.n_arms):
            sampled_theta.append(random.beta(self.prior_params[0]+self.rewards[i], self.prior_params[1]+self.trials[i]-self.rewards[i]))
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

        algorithm = ThompsonSampling(n_arms=n)

        for i in range(h):
            arm_to_pull = algorithm.select_arm()
            try:
                s.send(str(arm_to_pull) + '\n')
                print 'Sent arm to pull : ' + str(arm_to_pull)
            except:
                print 'Send Connection Error'

            time.sleep(0.05)

            try:
                raw_message = s.recv(512).rstrip('\0')
                receive_list = raw_message.replace(' ', '').split(',')
                print 'Received Message : ' + raw_message
            except:
                print 'Receive Connection Error'
            reward, n_pulls = int(receive_list[0]), int(receive_list[1])
            algorithm.update(arm_to_pull, reward)
        s.close
