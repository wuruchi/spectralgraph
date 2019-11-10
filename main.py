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
G.add_nodes_from([1, 2, 3, 4, 5, 6, 7, 8, 9])
G.add_edges_from([(1, 2), (2, 1), (1, 3), (3, 1), (2, 4), (4, 2), (2, 5), (5, 2),
                  (3, 6), (6, 3), (3, 7), (7, 3), (4, 8), (8, 4), (6, 7), (7, 6), (5, 6), (6, 5), (8, 9), (9, 8)])

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
    node_to_xy[i+1] = (x_coords[i], y_coords[i])

# pos = nx.spectral_layout(G, weight=2)


nx.draw(G, pos=node_to_xy, with_labels=True)
plt.show()
