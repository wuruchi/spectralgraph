import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from scipy import sparse

plt.figure(figsize=(18, 18))
G = nx.Graph()

# Implementation for spring layout. Not included in the presentation.
expid = "a247"
uniform = False
edges = list()
nodes = set()
color_map = dict()

with open('/home/Earth/wuruchi/Documents/Personal/spectralgraph/data/graph_' + expid + '.txt', 'r') as the_file:
    f1 = the_file.readlines()
    for x in f1:
        first = int(x.split(" ")[0].replace('\n', ''))
        second = int(x.split(" ")[1][:].replace('\n', ''))
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

spring = nx.spring_layout(G)
print(spring)

colors_list = list()
for node in G:
    colors_list.append(color_map[node])

# return
# G.add_edges_from(edges)
print("Graph completed")
print("About to draw")
nx.draw(G, pos=spring, node_color=colors_list, with_labels=False,
        node_size=1, font_size=8, font_family='sans-serif')
plt.savefig("mygraph_spring_" + expid + "" +
            ("_nw" if uniform == True else "") + ".png", dpi=200)
