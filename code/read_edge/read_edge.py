import pandas as pd
import csv

fileName = input("File name: ")
source = pd.read_csv(fileName, usecols = ['Source'])
target = pd.read_csv(fileName, usecols = ['Target'])

source_list = source.values.tolist()
target_list = target.values.tolist()

source_list = [item for sublist in source_list for item in sublist]
target_list = [item for sublist in target_list for item in sublist]

i = 0
node_dic = {}
for item in target_list:
    if not node_dic.__contains__(item):
        node_dic[item] = i
        i += 1

for item in source_list:
    if not node_dic.__contains__(item):
        node_dic[item] = i
        i += 1

i = 0
while i < len(target_list):
    target_list[i] = node_dic[target_list[i]]
    i += 1
i = 0
while i < len(source_list):
    source_list[i] = node_dic[source_list[i]]
    i += 1

edge_list = []
i = 0
while i < len(source_list):
    edge_list.append([source_list[i], target_list[i]])
    i += 1
print(edge_list)

with open('new_edge.csv', 'w') as f:
    # using csv.writer method from CSV package
    write = csv.writer(f, lineterminator = '\n')
    write.writerows(edge_list)

node_list = set()

for item in source_list:
    node_list.add(item)

for item in target_list:
    node_list.add(item)

node_list = list(node_list)
node = [[el] for el in node_list]
field = ['id']
with open('node.csv', 'w') as f:
    # using csv.writer method from CSV package
    write = csv.writer(f, lineterminator = '\n')
    write.writerow(field)
    write.writerows(node)

