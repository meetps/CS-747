#!/bin/bash

PWD=`pwd`

horizon=50
explorationHorizon=0
port=5001
nRuns=100
hostname="localhost"
banditFile="$PWD/data/instance-01.txt"

numArms=$(wc -l $banditFile | cut -d" " -f1 | xargs)

SERVERDIR=./server
CLIENTDIR=./client

OUTPUTFILE=$PWD/serverlog.txt

randomSeed=0

# sudo kill -9 `sudo netstat -plten | awk '{print $9}' | sed "s/\// /g" | grep bandit | awk '{print $1}'`

pushd $SERVERDIR
cmd="./startserver.sh $numArms $horizon $explorationHorizon $port $banditFile $randomSeed $OUTPUTFILE &"
#echo $cmd
$cmd 
popd

sleep 1

pushd $CLIENTDIR
cmd="./startclient.sh $numArms $horizon $explorationHorizon $hostname $port $randomSeed &"
#echo $cmd
$cmd > /dev/null 
popd

