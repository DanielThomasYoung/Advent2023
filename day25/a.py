from collections import defaultdict
import random

def main():
    with open("sample.txt", "r") as file:
        file_lines = file.readlines()
    
    connections = defaultdict(list)
    
    for line in file_lines:
        chars = line.strip().split(":")
        component = chars[0].strip()
        connected_components = [conn.strip() for conn in chars[1].split()]
        
        for connected_component in connected_components:
            connections[component].append(connected_component)
            connections[connected_component].append(component)
    
    for key, value in connections.items():
        print(key)
        print(value)
    
    # Find a partition using the heuristic approach
    group_a, group_b, cut_size = find_partition(connections)
    
    print(f"Group A: {group_a}")
    print(f"Group B: {group_b}")
    print(f"Cut size: {cut_size}")
    print(f"The product of the sizes of the two groups is: {len(group_a) * len(group_b)}")

def find_partition(connections):
    all_nodes = set(connections.keys())

    start_node = random.choice(list(all_nodes))
    group_a = {start_node}
    all_nodes.remove(start_node)
    
    while True:
        cut_size = 0
        min_external_connections = float('inf')
        node_to_add = None
        
        for node in group_a:
            for neighbor in connections[node]:
                if neighbor in all_nodes:
                    external_connections = sum(1 for n in connections[neighbor] if n not in group_a)
                    cut_size += 1
                    if external_connections < min_external_connections:
                        min_external_connections = external_connections
                        node_to_add = neighbor
        
        if node_to_add is None:
            break
        
        if cut_size == 3:
            break
        
        group_a.add(node_to_add)
        all_nodes.remove(node_to_add)
    
    group_b = all_nodes
    
    return group_a, group_b, cut_size

if __name__ == "__main__":
    main()