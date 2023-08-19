import json
import networkx as nx
import matplotlib.pyplot as plt

def analyse_json(json_file):
    with open(json_file, 'r') as file:
        data = json.load(file)
    
    # Check if data is a list
    if isinstance(data, list):
        data = data[0]

    G = nx.DiGraph()
    
    for key, value in data.items():
        G.add_node(key)

        if isinstance(value, dict):
            for subkey in value:
                G.add_node(subkey)
                G.add_edge(key, subkey)

        elif isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    for subkey in item:
                        G.add_node(subkey)
                        G.add_edge(key, subkey)

    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos)
    nx.draw_networkx_labels(G, pos)
    nx.draw_networkx_edges(G, pos, edge_color='black')

    plt.show()

# usage
analyse_json('output.json')
