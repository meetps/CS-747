#!/bin/sh

PWD=`pwd`
numArms=$1
horizon=$2
explorationHorizon=$3
hostname=$4
port=$5
randomSeed=$6

#echo "Inside Client"

cmd="./bandit-agent --numArms $numArms --randomSeed $randomSeed --horizon $horizon --explorationHorizon $explorationHorizon --hostname $hostname --port $port"
#echo $cmd
$cmd
