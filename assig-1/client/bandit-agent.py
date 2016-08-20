import sys
import socket
import time
import random


error_str = """
    Usage :
    python bandit-agent.py
    [--numArms numArms]
    [--randomSeed randomSeed]
    [--horizon horizon]
    [--explorationHorizon explorationHorizon]
    [--banditFile banditFile]
    [--port port]
    """


def get_arg(arguments):
    numArms = int(arguments[2])
    randomSeed = int(arguments[4])
    horizon = int(arguments[6])
    explorationHorizon = int(arguments[8])
    banditFile = str(arguments[10])
    port = int(arguments[12])
    return numArms, randomSeed, horizon, explorationHorizon, banditFile, port

if __name__ == '__main__':
    n_args = 6

    if len(sys.argv) != n_args * 2 + 1:
        sys.exit(error_str)
    else:
        n, s, h, eh, file_path, port = get_arg(sys.argv)

        s = socket.socket(socket.AF_INET)
        host = socket.gethostname()
        port = port
        s.connect((host, port))

        arm_to_pull = 0
        for i in range(h):
            try:
                s.send(bytes(random.randint(0, 4)))
                print 'Sent arm to pull : ' + str(arm_to_pull)
            except:
                print 'Send Connection Error'

            time.sleep(0.5)

            try:
                raw_message = s.recv(256).rstrip('\0')
                receive_list = raw_message.replace(' ', '').split(',')
                print 'Received Message : ' + raw_message
            except:
                print 'Receive Connection Error'
            reward, n_pulls = int(receive_list[0]), int(receive_list[1])

        s.close
