#!/bin/sh

numArms=$1
horizon=$2
explorationHorizon=$3
port=$4
banditFile=$5
randomSeed=$6
outputFile=$7

#echo "Inside Server"

cmd="./bandit-environment --numArms $numArms --randomSeed $randomSeed --horizon $horizon --explorationHorizon $explorationHorizon --banditFile $banditFile --port $port"
#echo $cmd
$cmd > $outputFile &
 
