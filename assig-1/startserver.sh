#!/bin/bash

server/bandit-environment --numArms 5 --randomSeed 0 --horizon 20 --explorationHorizon 0 --banditFile ../data/instance-01.txt --port 5001
