import json
import pygraphviz as pgv

def analyse_json(json_file):
    with open(json_file, 'r') as file:
        data = json.load(file)
    
    # Check if data is a list
    if isinstance(data, list):
        data = data[0]

    G = pgv.AGraph(directed=True)
    
    for key, value in data.items():
        G.add_node(key, color='red')

        if isinstance(value, dict):
            for subkey in value:
                G.add_node(subkey, color='blue')
                G.add_edge(key, subkey, color='black')

        elif isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    for subkey in item:
                        G.add_node(subkey, color='green')
                        G.add_edge(key, subkey, color='black')

    G.layout(prog='dot')
    G.draw('output.pdf')

# usage
analyse_json('output.json')
