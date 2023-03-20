import pandas as pd
import numpy as np
import networkx as nx
from node2vec import Node2Vec
from sklearn.model_selection import train_test_split
import lightgbm

nodeFile = input("Please input node file: ")
edgeFile = input("Please input edge file: ")
print("Please wait a second!")
with open(nodeFile, 'r', encoding = 'UTF-8') as f:
    node = f.read().splitlines()
with open(edgeFile, 'r', encoding = 'UTF-8') as f:
    edge = f.read().splitlines()

node_1 = list()
node_2 = list()

for i in edge:
    node_1.append(i.split(',')[0])
    node_2.append(i.split(',')[1])

dataFrame = pd.DataFrame({'node_1': node_1, 'node_2': node_2})

G = nx.from_pandas_edgelist(dataFrame, "node_1", "node_2", create_using = nx.Graph())

allNode = node_1 + node_2
allNode = list(dict.fromkeys(allNode))

Matrix = nx.to_numpy_matrix(G, nodelist = allNode)
unconnected = list()
flag = 0
for i in range(Matrix.shape[0]):
    for j in range(flag, Matrix.shape[1]):
        if i != j:
            if nx.has_path(G, str(i), str(j)) and nx.shortest_path_length(G, str(i), str(j)) <= 2:
                if Matrix[i, j] == 0:
                    unconnected.append([allNode[i], allNode[j]])
    flag = flag + 1
unconnectedN_1 = [i[0] for i in unconnected]
unconnectedN_2 = [i[1] for i in unconnected]

data = pd.DataFrame({'node_1': unconnectedN_1,
                     'node_2': unconnectedN_2})

data['link'] = 0
fb_df_temp = dataFrame.copy()
positiveIndex = list()

for i in dataFrame.index.values:
    G_temp = nx.from_pandas_edgelist(fb_df_temp.drop(index = i), "node_1", "node_2", create_using = nx.Graph())
    if (nx.number_connected_components(G_temp) == 1) and (len(G_temp.nodes) == len(G.nodes)):
        positiveIndex.append(i)
        fb_df_temp = fb_df_temp.drop(index = i)

if len(positiveIndex) == 0:
    i = 0
    while i < 5:
        positiveIndex.append(i)
        i += 1
    
    i = 20
    while i < 24:
        positiveIndex.append(i)
        i += 1
    i = 100
    while i < 105:
        positiveIndex.append(i)
        i += 1
    i = 700
    while i < 705:
        positiveIndex.append(i)
        i += 1
    positiveIndex.append(962)
    positiveIndex.append(931)
    positiveIndex.append(921)
    positiveIndex.append(911)
target = dataFrame.loc[positiveIndex]
target['link'] = 1
data = data.append(target[['node_1', 'node_2', 'link']], ignore_index = True)
part = dataFrame.drop(index = target.index.values)
newGraph = nx.from_pandas_edgelist(part, "node_1", "node_2", create_using = nx.Graph())
node2vec = Node2Vec(newGraph, dimensions = 100, walk_length = 16, num_walks = 50)

n2w_model = node2vec.fit(window = 7, min_count = 1)
x = [(n2w_model.wv[str(i)] + n2w_model.wv[str(j)]) for i, j in zip(data['node_1'], data['node_2'])]

xtrain, xtest, ytrain, ytest = train_test_split(np.array(x), data['link'],
                                                test_size = 0.33,
                                                random_state = 35)

train = lightgbm.Dataset(xtrain, ytrain)
testData = lightgbm.Dataset(xtest, ytest)

parameters = {
    'metric': 'auc',
    'is_unbalance': 'true',
    'objective': 'binary',
    'bagging_freq': 20,
    'num_threads': 20,
    'feature_fraction': 0.8,
    'bagging_fraction': 0.8,
}
model = lightgbm.train(parameters,
                       train,
                       valid_sets = testData,
                       num_boost_round = 500,
                       early_stopping_rounds = 20)
model.save_model('mode.txt')

