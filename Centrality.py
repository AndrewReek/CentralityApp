import pandas as pd
import networkx as nx

def get_degree(graph, run):
    if run:
        centrality = nx.degree_centrality(graph)
        df = pd.DataFrame(centrality, index = ['Degree Centrality'])
        return df
    else:
        pass

def get_eigenvector(graph, run):
    if run:
        centrality = nx.eigenvector_centrality(graph)
        df = pd.DataFrame(centrality, index = ['Eigenvector Centrality'])
        return df
    else:
        pass

def get_closeness(graph, run):
    if run:
        centrality = nx.closeness_centrality(graph)
        df = pd.DataFrame(centrality, index = ['Closeness Centrality'])
        return df

def get_betweenness(graph, run):
    if run:
        centrality = nx.betweenness_centrality(graph)
        df = pd.DataFrame(centrality, index = ['Betweenness Centrality'])
        return df

def get_load(graph, run):
    if run:
        centrality = nx.load_centrality(graph)
        df = pd.DataFrame(centrality, index = ['Load Centrality'])
        return df

def get_subgraph(graph, run):
    if run:
        centrality = nx.subgraph_centrality(graph)
        df = pd.DataFrame(centrality, index = ['Subgraph Centrality'])
        return df

def get_harmonic(graph, run):
    if run:
        centrality = nx.harmonic_centrality(graph)
        df = pd.DataFrame(centrality, index = ['Harmonic Centrality'])
        return df


######Test Code
# df = pd.read_csv('edgelist.csv')
# graph = nx.from_pandas_edgelist(df, source = 'Investor 1', target = 'Investor 2')

# df = get_betweenness(graph)
# df.to_csv('test.csv')

# print(df.head)