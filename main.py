import numpy as np
import networkx as nx
from time import time
import matplotlib.pyplot as plt
from scipy import sparse

plt.figure(figsize=(18, 18))
G = nx.Graph()

#nodes_txt = {'1', '2', '3', '4', '5', '6', '7'}
expid = "ermodel30k"
uniform = False
no_weight = True
edges = list()
nodes = set()
color_map = dict()

start = time()

with open('/Users/BleuDChan/ReposUPC/spectralgraph/data/graph_' + expid + '.txt', 'r') as the_file:
    f1 = the_file.readlines()
    for x in f1:
        first = int(x.split(" ")[0].replace('\n', ''))
        second = int(x.split(" ")[1][:].replace('\n', ''))
        if no_weight == True:
            weight = 1
        else:
            weight = int(x.split(" ")[2][:].replace('\n', ''))
        nodes.add(first)
        nodes.add(second)
        if first not in color_map.keys():
            color_map[first] = "red" if weight == 1 else "blue"
        else:
            if color_map[first] != "blue":
                color_map[first] = "red" if weight == 1 else "blue"
        if second not in color_map.keys():
            color_map[second] = "red" if weight == 1 else "blue"
            if color_map[second] != "blue":
                color_map[second] = "red" if weight == 1 else "blue"
        edges.append((first, second, weight))

print("Start Graph build")
G.add_nodes_from(nodes)
for item in edges:
    u, v, w = item
    w = 1 if uniform == True else w
    w = w if w == 10 else 3
    G.add_edge(u, v, weight=w)

print("Graph completed")

degree_dict = nx.degree(G)
degree_list = [x[1] for x in degree_dict]


lap_matrix = nx.normalized_laplacian_matrix(G)
print("Finished Normalized Laplacian")
eigval, eigvec = sparse.linalg.eigsh(lap_matrix, k=4, which="SM")

# print(G.nodes)
print("Eigenvalues")
print(eigval)
# print(eigvec)
print("Finished Eigen")
x_coords = eigvec[:, 1]*100
y_coords = eigvec[:, 2]*100

print((x_coords))
print((y_coords))
node_to_xy = dict()


with open('/Users/BleuDChan/ReposUPC/spectralgraph/data/graph1-test.txt', 'w') as the_file:
    for i in range(len(x_coords)):
        node_to_xy[i] = (x_coords[i], y_coords[i])
        the_file.write(
            str(i) + " " + str(x_coords[i]) + " " + str((y_coords[i])) + "\n")

colors_list = list()
for node in G:
    colors_list.append(color_map[node])

# print(colors_list)
# pos = nx.spectral_layout(G, weight=2)
finish = time() - start
print("Seconds " + str(finish))
print("About to draw")

nx.draw(G, pos=node_to_xy, node_color=colors_list, with_labels=False,
        node_size=1, font_size=8, font_family='sans-serif')
plt.savefig("mygraph_" + expid + "" +
            ("_nw" if uniform == True else "") + ".png", dpi=200)
