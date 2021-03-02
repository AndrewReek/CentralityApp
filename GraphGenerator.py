import pandas as pd
import networkx as nx

def read_file(file_path, investor_name, company_id, investment_amount):
    df = pd.read_csv(filepath_or_buffer = file_path, usecols = [investor_name, company_id, investment_amount])
    df = df.dropna()
    df = df[df[investment_amount] > 0]
    df = df.rename(columns = {investor_name: 'Investor Name',
                              company_id: 'Company ID',
                              investment_amount: 'Investment Amount'})
    return df

def generate_edgelist(dataframe):
    df = dataframe
    
    firms = df['Company ID'].unique()

    investor_combinations = []
    for firm in firms:
        df_firm = df[df['Company ID'] == firm]
        firm_investors = df_firm['Investor Name'].unique()

        for investor in firm_investors:
            for i in range(len(firm_investors)):
                if investor != firm_investors[i]:
                    investor_combinations.append([investor, firm_investors[i]])

    investor_combinations = [list(x) for x in set(tuple(x) for x in investor_combinations)]

    edgelist = pd.DataFrame(investor_combinations, columns = ['Investor 1', 'Investor 2'])
        
    return edgelist

def generate_graph(edgelist):
    df = edgelist
    G = nx.from_pandas_edgelist(df, source = 'Investor 1', target = 'Investor 2')
    return G

def generate_matrix(graph):
    adjacencymatrix = nx.to_pandas_adjacency(graph)
    return adjacencymatrix

def export_graph(df, file_path):
    df.to_csv(file_path)


######Test Code
# df = read_file('2005_test.csv', 'Investor Full Name', 'ISIN', 'Holdings Value Held')
# edgelist = generate_edgelist(df)
# adjacency = generate_matrix(edgelist)

# export_graph(adjacency, 'adjacencymatrix2.csv')