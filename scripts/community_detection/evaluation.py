"""""""""""""""""""""""""""""""""""""""""""""""
|    SMM638: Network Analytics - Group 7      |
|---------------------------------------------|
| This python script contains functions       |
| to evalue communities detection algorithms  |
|                                             |
"""""""""""""""""""""""""""""""""""""""""""""""

import pandas as pd
import networkx.algorithms.community as nx_comm

def evaluate_modularity(G, commu_list):
    
    # initiate a dictionary to store modularity
    modularities = {}
    
    # loop over all community structure
    for c in commu_list:
        communities = c['communities']
        # prepare element for modularity calculation
        commu = []
        # loop over communities in an algorithm
        for i in sorted(pd.Series(communities.values()).unique()):
            store_list = []
            # loop over all nodes
            for node in G.nodes:
                if communities[node] == i:
                    store_list.append(node)
            commu.append(store_list)
        # calculate modularity
        modularity = nx_comm.modularity(G, commu)
        # store value in `modularities`
        modularities[c['algo']] = modularity
    
    return modularities
        
        
        

    
    