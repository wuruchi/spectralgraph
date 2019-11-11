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

G = nx.Graph()

#nodes_txt = {'1', '2', '3', '4', '5', '6', '7'}
G.add_nodes_from([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])
G.add_edges_from([(0, 1), (0, 15), (0, 20), (0, 26), (1, 2), (1, 10), (2, 3), (2, 9), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (9, 4), (10, 11), (10, 14), (11, 12), (12, 13), (12, 9), (13, 6), (14, 12), (15, 16), (15, 18), (16, 17), (17, 4), (18, 19), (19, 12), (20, 21), (21, 22), (22, 23), (23, 24), (24, 25), (25, 10), (25, 18), (25, 2), (25, 16), (26, 27), (26, 28), (27, 19), (28, 17), (29, 22), (30, 14)])

degree_dict = nx.degree(G)
degree_list = [x[1] for x in degree_dict]
# A = nx.adjacency_matrix(G)
# for i in A:
#     print(i.toarray())
# print("### degree list ###")
# print(degree_list)
# print("#########")
lap_matrix = nx.normalized_laplacian_matrix(G)
print(lap_matrix)
eigval, eigvec = sparse.linalg.eigsh(lap_matrix, k=7, which="SM")

# print(G.nodes)
# print(eigval)
# print(eigvec)

x_coords = eigvec[:, 2]*100
y_coords = eigvec[:, 3]*100

node_to_xy = dict()
for i in range(len(eigvec[:, 1])):
    node_to_xy[i] = (x_coords[i], y_coords[i])

# pos = nx.spectral_layout(G, weight=2)


nx.draw(G, pos=node_to_xy, with_labels=True)
plt.show()
