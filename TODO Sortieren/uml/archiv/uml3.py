import json
import argparse
from anytree import Node, RenderTree

def json_to_tree(json_obj, parent=None):
    if isinstance(json_obj, dict):
        for k, v in json_obj.items():
            if isinstance(v, (dict, list)):
                node = Node(k, parent=parent)
                json_to_tree(v, node)
            else:
                Node(f"{k}: {v}", parent=parent)
    elif isinstance(json_obj, list):
        for index, item in enumerate(json_obj):
            if isinstance(item, (dict, list)):
                node = Node(f"item_{index}", parent=parent)
                json_to_tree(item, node)
            else:
                Node(f"item_{index}: {item}", parent=parent)

def main(json_file):
    with open(json_file, 'r') as f:
        json_obj = json.load(f)

    root = Node("root")
    json_to_tree(json_obj, root)

    # Baum ausgeben
    for pre, fill, node in RenderTree(root):
        print(f"{pre}{node.name}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("json_file", help="The JSON file to convert to a tree.")
    args = parser.parse_args()

    main(args.json_file)
