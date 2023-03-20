"""
This program find the pair of node with the largest preferential_attachment score
and add this pair of node as edge to the network
Input how many iterations you want
One edge is added in one iteration
"""
import pandas as pd
import networkx as nx
import csv
file = input("Please input the edge file name: ")
iteration = int(input("How many iterations?\n"))
ite_round = 0
print("Edges:")

while ite_round < iteration:
    # build a graph from new_edge.csv file
    df = pd.read_csv(file)
    G = nx.from_pandas_edgelist(df, source = 'Source', target = 'Target', create_using = nx.Graph())
    # compute preferential_attachment score of every pair of node
    # type(nx.preferential_attachment(G)) = tuple
    score = list(nx.preferential_attachment(G))

    # convert tuple to list
    # so that we can store it into csv file
    i = 0
    while i < len(score):
        score[i] = list(score[i])
        i += 1
    # Write score into score.csv file
    with open('score.csv', 'w') as f:
        # Using csv.writer method from CSV package
        write = csv.writer(f, lineterminator = '\n')
        write.writerow(["node_1", "node_2", "score"])
        write.writerows(score)
   
    # Sort in descending order
    data = pd.read_csv("score.csv")
    data.sort_values(["score"], axis=0, ascending=[False], inplace=True)
    data.to_csv('score.csv')

    # Get the pair of node with the largest score
    # store in big_score
    data = pd.read_csv("score.csv")
    index = 0
    link = data.iloc[index]
    big_score = link.tolist()

    sc = big_score[3]
    big_score = [big_score[1], big_score[2]]

    while G.has_edge(big_score[0], big_score[1]):
        index += 1
        link = data.iloc[index]
        big_score = link.tolist()
        big_score = [big_score[1], big_score[2]]
    
    print(f"Iteration: {ite_round}: New edge: {big_score[0]} - {big_score[1]}\t(score:{sc}) is added!")
    # add this pair of node as edge to new_edge.csv
    with open(file, 'a+') as f:
        # using csv.writer method from CSV package
        write = csv.writer(f, lineterminator = '\n')
        write.writerows([big_score])

    ite_round += 1
print("are added to the graph successfully!")
