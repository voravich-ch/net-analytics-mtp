import collections
import numpy as np
import matplotlib.pyplot as plt
import pathlib
import networkx as nx
import itertools
from networkx.algorithms.community import girvan_newman, modularity
from networkx import edge_betweenness_centrality as betweenness
import infomap

def girvan_newman_detection(G):
    
    # define a function to compute weighted centrality betweenness
    def most_central_edge(G):
        centrality = betweenness(G, weight = 'weight')
        return max(centrality, key = centrality.get)

    # fit the model
    if nx.is_weighted(G):
        solutions = girvan_newman(G, most_valuable_edge = most_central_edge)
    else:
        solutions = girvan_newman(G)
    
    # assign the number of times partitioning
    k = 30
    
    # register modularity scores
    modularity_scores = dict()

    # initiate a maximum modularity score
    max_score = 0

    # iterate over solutions
    for community in itertools.islice(solutions, k):
        solution = list(sorted(c) for c in community)
        score = modularity(G, solution)
        # store modularity score
        modularity_scores[len(solution)] = score
        if score > max_score:
            # save the community structure with highest modularity score
            community_structure = list(solution)
            max_score = score
    
    # get the number of isolated nodes
    num_isolated_nodes = [len(i) for i in community_structure].count(1)
    
    # report the result
    print("Weighted Girvan-Newman Community Detection")
    print("------------------------------------------")
    if num_isolated_nodes == 0:
        print("Number of communities detected: {}".format(len(community_structure)))
    else:
        print("Number of communities detected: {}".format(len(community_structure) - num_isolated_nodes))
        print("Number of nodes not in any community: {}".format(num_isolated_nodes))
        
    # plot modularity data
    fig = plt.figure(figsize = (8, 4))
    pos = list(modularity_scores.keys())
    values = list(modularity_scores.values())
    ax = fig.add_subplot(1, 1, 1)
    ax.stem(pos, values)
    ax.set_xticks(pos)
    ax.set_xlabel(r'Number of communities detected')
    ax.set_ylabel(r'Modularity score')
    
    # save plot
    pathlib.Path("output").mkdir(exist_ok=True)
    plt.savefig("output/modularity_plot_{}.png".format(G.name))
    
    plt.show()
    print("The image was saved to: `output/modularity_plot_{}.png`".format(G.name))
    
    # process data for analysis
    communities = {}
    for node in G.nodes():
        for index, commu in enumerate(community_structure):
            if node in commu:
                communities[node] = index
                
    return communities


def infomap_community_detection(G):
    
    # initiate an infomap object
    im = infomap.Infomap()
    
    # add nodes
    im.add_nodes(G.nodes)
    
    # add edges and weights
    # transpose a numpy array to get arrays of first and second elements in edges
    sources = np.array(G.edges).T[0]
    targets = np.array(G.edges).T[1]
    weights = nx.get_edge_attributes(G, 'weight').values()
    if nx.is_weighted(G):
        edges = zip(sources, targets, weights)
    else:
        edges = zip(sources, targets)
    im.add_links(edges)
    
    # run the model
    im.run()
    
    # get a dictionary with node id as key and respective community as value
    communities = im.get_modules()
    
    # get the number of isolated nodes
    freq_dict = collections.Counter(communities.values())
    num_isolated_nodes = list(freq_dict.values()).count(1)
    
    # report the result
    print("Infomap Community Detection")
    print("---------------------------")
    if num_isolated_nodes == 0:
        print("Number of communities detected: {}".format(im.num_top_modules))
    else:
        print("Number of communities detected: {}".format(im.num_top_modules - num_isolated_nodes))
        print("Number of nodes not in any community: {}".format(num_isolated_nodes))
                
    return communities