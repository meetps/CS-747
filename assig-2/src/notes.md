## ALGORITHMS

I have implemented value iteration and policy iteration. But as it turns out the latter outperforms the former in our testcases. Thus I use it by default in `planner.sh`. 

### Policy Iteration
	
The policy iteration algorithm implemented has the following algorithm:

```
Procedure Policy_Iteration(S,A,T,R) 
   set π arbitrarily 
   repeat
         noChange ←true 
         Solve V[s] = ∑s'∈S T(s'|s,π[s])(R(s,a,s')+γ * V[s']) 
         for each s∈S do 
           Let QBest=V[s] 
           for each a ∈A do 
           		Let Qsa = ∑s'∈S T(s'|s,a)(R(s,a,s')+γ * V[s']) 
                 	if (Qsa > QBest) then 
                       π[s]←a 
                       QBest ←Qsa 
                       noChange ←false 
   until noChange 
   return π
```

### Value Iteration

The value iteration algorithm implemented has the following algorithm:

```
Value_Iteration(S,A,T,R,eps):
  assign V_0[S] arbitrarily 
   k ←0 
   repeat
        k ←k+1 
         for each state s do 
               Vk[s] = maxa ∑s' T(s'|s,a) (R(s,a,s')+ γ * Vk-1[s']) 
   until ∀s |Vk[s]-Vk-1[s]| < eps 
   for each state s do 
             π[s] = argmaxa ∑s' P(s'|s,a) (R(s,a,s')+ γVk[s']) 
   return Vk,π
```

### Reason for choosing policy iteration: 
* Faster convergence in given test cases (such |S| = 100 and |A| = 100).
* LP can be solved much faster than iteratively searching for best values.

## REFERENCES

* http://artint.info/html/ArtInt_227.html (psuedo code credits for value iteration)
* http://artint.info/html/ArtInt_228.html (best pseudo code for Policy iteration)
* http://docs.scipy.org/doc/numpy/reference/generated/numpy.linalg.solve.html (for solving LP in policy iteration)
* https://people.eecs.berkeley.edu/~pabbeel/cs287-fa12/slides/mdps-exact-methods.pdf (psuedo code for value iteration)

## Running code 

As suggested in the instructions.txt my code can be run using : 

* `./planners.sh <file_path>`

If you want to run value iteration (slower in such cases) / policy iteration explicitly :

* `python value_iteration.py <filePath>`
* `python policy_iteration.py <filePath>`

### Additional Notes
 It takes about **24s** on an average find the optimal policy for a MDP with |S|=100 and |A|=100.
