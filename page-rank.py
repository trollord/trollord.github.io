import numpy as np
print("Enter the edges in format 'u v', enter 'a' if you want to end:")
nodes = []
while (_in:=input()) != "a":
  nodes.append(list(map(int, _in.split(" "))))
nodes = np.array(nodes)
adjacency_matrix = np.zeros((np.max(nodes)+1, np.max(nodes)+1))
for s, e in nodes:
  adjacency_matrix[s, e] = 1
hits = np.ones((np.max(nodes)+1,))
authorities = np.ones((np.max(nodes)+1,))
print(f"The adjacency matrix is:\n{adjacency_matrix}\n")
max_itr = 10
for _ in range(max_itr):
  hits = adjacency_matrix @ authorities
  authorities = adjacency_matrix.T @ hits
# normalize
  hits = hits / np.linalg.norm(hits)
  authorities = authorities / np.linalg.norm(authorities)
print("Hits: ", dict(enumerate(hits)))
print()
print("Authorities: ", dict(enumerate(authorities)))
print()
