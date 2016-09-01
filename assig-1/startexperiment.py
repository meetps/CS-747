import os
import sys
import time
import subprocess

pwd = os.getcwd()

horizon=50
explorationHorizon=0
port=5001
nRuns=100
hostname="localhost"
banditFile= pwd + "/data/instance-01.txt"
numArms = 0

with open(banditFile) as f:
   numArms = len(list(f))

SERVERDIR='/server/'
CLIENTDIR='/client/'
OUTPUTFILE=pwd + '/serverlog.txt'
randomSeed=0

os.chdir( pwd + SERVERDIR)
p = subprocess.Popen(['./startserver.sh', str(numArms), str(horizon), str(explorationHorizon), str(port), banditFile, str(randomSeed), OUTPUTFILE])
os.chdir(pwd)

time.sleep(1)

os.chdir( pwd + '/client/')
commandString = ['./startclient.sh', str(numArms) , str(horizon), str(explorationHorizon) ,'localhost' ,str(port) ,str(randomSeed)]
print " ".join(commandString)
c = subprocess.Popen(commandString)

time.sleep(5)

p.terminate()
c.kill()