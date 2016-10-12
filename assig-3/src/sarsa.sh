echo "This may take a while | Grab some coffee"

python sarsa.py 5 0.9
echo "Done for states = 5"
python sarsa.py 8 0.9
echo "Done for states = 8"
python sarsa.py 10 0.9
echo "Done for states = 10"
python sarsa.py 20 0.9
echo "Done for states = 20"

python sarsa.py 5 0.6
echo "Done for states = 5 and gamma = 0.6"
python sarsa.py 5 0.7
echo "Done for states = 5 and gamma = 0.7"
python sarsa.py 5 0.8
echo "Done for states = 5 and gamma = 0.8"
python sarsa.py 5 0.9
echo "Done for states = 5 and gamma = 0.9"
