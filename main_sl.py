# import numpy as np
# from scipy.sparse import csgraph
# G = np.arange(5) * np.arange(5)[:, np.newaxis]
# # print(G)
# G2 = csgraph.laplacian(G, normed=False)
# # print(G2)
# w, v = np.linalg.eig(G2)
# print(w)
# print(v[:1])
# print(v[1:2])
# print(v[2:3])
# print(v[3:4])
# print(v[4:5])
# print("Total")
# print(v)

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from scipy import sparse

plt.figure(figsize=(18,18))
G = nx.Graph()

#nodes_txt = {'1', '2', '3', '4', '5', '6', '7'}
expid = "a2fg"
uniform = False
edges = list()
nodes = set()
color_map = dict()

with open('/home/Earth/wuruchi/Documents/Personal/spectralgraph/data/graph_' + expid + '.txt', 'r') as the_file:
    f1 = the_file.readlines()
    for x in f1:
        first = int(x.split(" ")[0].replace('\n',''))
        second = int(x.split(" ")[1][:].replace('\n',''))
        weight = int(x.split(" ")[2][:].replace('\n',''))
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

spring = nx.kamada_kawai_layout(G)
print(spring)

colors_list = list()
for node in G:
    colors_list.append(color_map[node])

#return
# G.add_edges_from(edges)
print("Graph completed")
print("About to draw")
nx.draw(G, pos=spring, node_color = colors_list, with_labels=False, node_size=1, font_size=8, font_family='sans-serif')
plt.savefig("mygraph_spring_" + expid + "" + ("_nw" if uniform == True else "") + ".png", dpi=200)

# # Testing degree
# # nodelist = G.nodes()
# # A = nx.to_scipy_sparse_matrix(G, nodelist=nodelist,
# #                                   format='csr')
# # diags = A.sum(axis=1).flatten()
# # print(diags)
# # End Testing degree


# #print(nodes)
# #print(edges)
# degree_dict = nx.degree(G)
# degree_list = [x[1] for x in degree_dict]
# # A = nx.adjacency_matrix(G)
# # for i in A:
# #     print(i.toarray())
# # print("### degree list ###")
# # print(degree_list)
# # print("#########")






# lap_matrix = nx.normalized_laplacian_matrix(G)
# print("Finished Normalized Laplacian")
# eigval, eigvec = sparse.linalg.eigsh(lap_matrix, k=4, which="SM")

# # print(G.nodes)
# print("Eigenvalues")
# print(eigval)
# # print(eigvec)
# print("Finished Eigen")
# x_coords = eigvec[:, 1]*100
# y_coords = eigvec[:, 2]*100

# print((x_coords))
# print((y_coords))
# node_to_xy = dict()


# with open('/home/Earth/wuruchi/Documents/Personal/spectralgraph/data/graph1-test.txt', 'w') as the_file:
#     for i in range(len(x_coords)):
#         node_to_xy[i] = (x_coords[i], y_coords[i])
#         the_file.write(str(i) + " " + str(x_coords[i]) + " " + str((y_coords[i])) + "\n")

# colors_list = list()
# for node in G:
#     colors_list.append(color_map[node])

# # print(colors_list)
# # pos = nx.spectral_layout(G, weight=2)

# print("About to draw")
# nx.draw(G, pos=node_to_xy, node_color = colors_list, with_labels=False, node_size=1, font_size=8, font_family='sans-serif')
# plt.savefig("mygraph_" + expid + "" + ("_nw" if uniform == True else "") + ".png", dpi=200)
