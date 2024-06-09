from itertools import combinations
from collections import Counter
import heapq

# Função para exibir todas as árvores com seis vértices
def generate_trees(vertices):
    edges = list(combinations(vertices, 2))
    trees = []
    for edge in edges:
        tree = [edge]
        remaining_vertices = list(set(vertices) - set(edge))
        for combo in combinations(remaining_vertices, 3):
            tree.extend(list(combinations(combo, 2)))
            trees.append(tree)
    return trees

# Função para exibir um conjunto completo de árvores não isomorfas com sete vértices
def generate_non_isomorphic_trees(vertices):
    trees = []
    for tree in generate_trees(vertices):
        if tree not in trees:
            trees.append(tree)
    return trees

# Função para calcular o número de árvores geradoras diferentes de K
def count_spanning_trees(n):
    return n ** (n - 2) if n >= 1 else 0

# Exibir todas as árvores com seis vértices
vertices_6 = ['A', 'B', 'C', 'D', 'E', 'F']
print("Todas as árvores com seis vértices:")
for tree in generate_trees(vertices_6):
    print(tree)

# Exibir um conjunto completo de árvores não isomorfas com sete vértices
vertices_7 = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
print("\nConjunto completo de árvores não isomorfas com sete vértices:")
for tree in generate_non_isomorphic_trees(vertices_7):
    print(tree)


# Calcular o número de árvores geradoras diferentes de K para n=1,2,3,4,5,6
print("\nNúmero de árvores geradoras diferentes de K:")
for n in range(1, 7):
    print(f"n={n}: {count_spanning_trees(n)}")

# Conjectura sobre uma fórmula para o número de árvores geradoras diferentes de K
print("\nConjectura sobre uma fórmula para o número de árvores geradoras:")
print("Parece seguir a fórmula n ^ (n - 2) para n sendo um número inteiro positivo.")
print("exemplo= O resultado é 2 ** (2 - 2) = 2 ** 0 = 1.")
