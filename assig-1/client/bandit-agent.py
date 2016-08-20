import sys
import socket
import time

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

        for i in range(h):
            print s.send(bytes(2))
            time.sleep(2)

        s.close
