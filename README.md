# Q-learning
Implementation of Q-learning

For this project, I implemented a Q-learning strategy for model-free reinforcement learning. 
 I’ll explain some key parts of my implementation here:
1.	looping through our data, we get each line’s s, a, r, and sp information.
2.	 The Q-values were stored in a nested dictionary that had state values as keys on the outer dictionary, actions as keys on the inner dictionary, and Q-values as the value for a particular (state, action) pair. 
3.	We can retrieve the maximum Q-value for sp from this Q dictionary, or it’s 0.
4.	Update the value of Q[s][a].

I had slightly different strategies for extracting the policies for different data files.
For small, I used the most straightforward approach – taking the action that would maximize the Q-value given a state.
For medium, many  states did not get observed. I looked at the data and observed that rewards were gotten on actions 5, 6, and 7. Because of the nature of the states (positions and velocities) I assumed that for unobserved values, we could try to get arg max action for Q-values of nearby states, or just choose randomly from the actions we know will garner reward. For observed states, I chose the the action that would maximize the Q-value for that state, like in small.
For large, we know that many states did not get observed. Since we don’t know the nature of the problem, I didn’t make the same assumptions as with medium. For unobserved states, I recommend a random action. For observed, take the same approach as in small.

Here are the execution times for each data file:
small 		5.96002411842 seconds
medium 	12.9156279564 seconds
large 		13.0601329803 seconds
