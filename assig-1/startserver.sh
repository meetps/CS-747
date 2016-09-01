#!/bin/bash

server/bandit-environment --numArms 7 --randomSeed 0 --horizon 5000 --explorationHorizon 0 --banditFile ../data/instance-01.txt --port 5001
