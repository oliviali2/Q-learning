import sys
import networkx as nx
import pandas as pd
import numpy as np
import collections
import math
import time
import operator
import random

def get_policy_sm(Q, s, a, out):
    with open(out, 'w') as f:
        for i in range(1, s+1):
            policy = max(Q[i].iteritems(), key=operator.itemgetter(1))[0]
            f.write( str(policy) + '\n' )

def get_policy_med(Q, s, a, out):
    with open(out, 'w') as f:
        for i in range(1, s+1):
            if i not in Q:
                if i+1 in Q:
                    policy = max(Q[i+1].iteritems(), key=operator.itemgetter(1))[0]
                elif i-1 in Q:
                    policy = max(Q[i-1].iteritems(), key=operator.itemgetter(1))[0]
                else: policy = random.randint(5,7)
            else:
                policy = max(Q[i].iteritems(), key=operator.itemgetter(1))[0]
            f.write( str(policy) + '\n' )

def get_policy_lg(Q, s, a, out):
    with open(out, 'w') as f:
        for i in range(1, s+1):
            if i not in Q:
                policy = random.randint(1,4)
            else:
                policy = max(Q[i].iteritems(), key=operator.itemgetter(1))[0]
            f.write( str(policy) + '\n' )

def q_learning(data, g):
    # Q = initialize_Q(num_states, num_actions)
    Q = {}
    for index, row in data.iterrows():
        s, a, r, sp = row['s'], row['a'], row['r'], row['sp']
        if sp in Q:
            max_Qsp = max( Q[sp][a_sp] for a_sp in Q[sp].keys())
        else: max_Qsp = 0

        if s not in Q:
            Q[s] = {}
            Q[s][a] = r + g*max_Qsp
        else:
            if a not in Q[s]:
                Q[s][a] = r + g*max_Qsp
            else:
                Q[s][a] += r + g * (max_Qsp - Q[s][a])
    print('Q: \n' + str(Q))
    return Q

def rl(infile, outfile, discount):
    info = {'small.csv' : (100, 4),
            'medium.csv' : (50000, 7),
            'large.csv' : (312020, 9)}
    n_states, n_actions = info[infile]
    data =  pd.read_csv(infile)
    Q = q_learning(data, discount)
    # get_policy_sm(Q, n_states, n_actions, outfile)
    # get_policy_med(Q, n_states, n_actions, outfile)
    # get_policy_lg(Q, n_states, n_actions, outfile)

def main():
    start_time = time.time()
    rl('small.csv', 'small.policy', 0.95)
    # rl('medium.csv', 'medium.policy', .805)
    # rl('large.csv', 'large.policy', 0.95)
    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == '__main__':
    main()
