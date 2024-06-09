import networkx as nx
import matplotlib.pyplot as plt
import random

from itertools import combinations

def all_simple_graphs(n):
    nodes = list(range(n))
    all_edges = list(combinations(nodes, 2))
    graphs = []
    for i in range(2**len(all_edges)):
        edges = [all_edges[j] for j in range(len(all_edges)) if i & (1 << j)]
        G = nx.Graph()
        G.add_nodes_from(nodes)
        G.add_edges_from(edges)
        graphs.append(G)
    return graphs

def random_graph(n):
    G = nx.Graph()
    G.add_nodes_from(range(n))
    for u in range(n):
        for v in range(u + 1, n):
            if random.random() < 0.5:
                G.add_edge(u, v)
    return G

def gray_code(n):
    if n == 0:
        return [0]
    else:
        lower_bits = gray_code(n-1)
        return lower_bits + [x | (1 << (n-1)) for x in reversed(lower_bits)]

def format_gray_code(code, n):
    return [format(x, f'0{n}b') for x in code]

def main_menu():
    print("Escolha uma questão para resolver:")
    print("1. Exibir todos os grafos simples com quatro vértices")
    print("2. Gerar aleatoriamente 10 grafos simples diferentes, cada um com até 20 vértices")
    print("3. Construir um código de Gray no qual as palavras do código sejam cadeias de bit de comprimento seis")
    print("4. Sair")

    choice = int(input("Digite o número da questão: "))
    return choice

def execute_choice(choice):
    if choice == 1:
        graphs = all_simple_graphs(4)
        for i, G in enumerate(graphs):
            plt.figure(figsize=(2, 2))
            nx.draw(G, with_labels=True)
            plt.title(f"Grafo {i+1}")
            plt.show()
    elif choice == 2:
        global random_graphs
        random_graphs = [random_graph(random.randint(1, 20)) for _ in range(10)]
        for i, G in enumerate(random_graphs):
            plt.figure(figsize=(4, 4))
            nx.draw(G, with_labels=True)
            plt.title(f"Random Grafo {i+1}")
            plt.show()
    elif choice == 3:
        gray_code_6 = format_gray_code(gray_code(4), 6)
        for i, code in enumerate(gray_code_6):
            print(f"Código Gray {i+1}: {code}")
    elif choice == 4:
        print("Saindo...")
    else:
        print("Escolha inválida. Tente novamente.")

if __name__ == "__main__":
    while True:
        choice = main_menu()
        if choice == 4:
            break
        execute_choice(choice)
