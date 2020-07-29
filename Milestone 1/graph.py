import queue as Q
import numpy as np

# Pembacaan node dari dataset
def read_nodes(file):
    dataset = open("../dataset/"+file+".txt",'r')
    nodes = dataset.readlines()
    locations = {}
    dataset.close()

    for node in nodes:
        place = []
        place = node.split(" ")
        if(node[2][-1] == '\n'):
            place[2] = place[2][:-1]
        # loc = Node(place[0],place[1],place[2])
        locations.update({place[0] : (float(place[1]),float(place[2]))})
        # locations[int(place[0])] = (float(place[1]),float(place[2]))
    return locations

# Pembacaan edge dari dataset
def read_edges(file):
    dataset = open("../dataset/"+file+".txt",'r')
    edges = dataset.readlines()
    street = {}
    dataset.close()

    for edge in edges :
        edge = edge.split(" ")
        if edge[3][-1] == '\n' : 
            edge[3] = edge[3][:-1]
        if int(edge[2]) not in street :
            street.update({int(edge[2]) : []})
        if int(edge[1]) not in street : 
            street.update({int(edge[1]) : []})
        connect(street,edge)

    return street

# Untuk menghubungkan edge antar node
def connect(street,edge):
    street[int(edge[2])].append((int(edge[1]), float(edge[3])))
    street[int(edge[1])].append((int(edge[2]), float(edge[3])))

# Fungsi heuristik menggunakan numpy (Euclidean Distance)
def heuristic(init,finish):
    return(np.linalg.norm(finish-init))

# Tetangga dari sebuah node
def neighbors(node,edge_data):
    # print(node)
    list_neighbor = edge_data[node]
    neighbors = []

    for neighbor in list_neighbor:
        neighbors.append(neighbor)
        
    return neighbors

# Menyimpan path yang ditempuh untuk mencapai sebuah node
def reconstruct_path(node, start):
    path = []
    path.append(node)
    while node != start:
        node = node.parent
        path.append(node)
    return path

# Algoritma A* untuk mencari shortest path antar node
def a_star(start,finish,node_data,edge_data):
    frontier = Q.PriorityQueue()
    frontier.put(start, 0)
    parent = {start: None}
    total_cost = {start: 0}

    while frontier:
        current = frontier.get()

        if current == finish:
            break

        for visit,cost in neighbors(current,edge_data):
            new_cost = total_cost[current] + cost
            if visit not in total_cost or new_cost < total_cost[visit]:
                total_cost[visit] = new_cost
                priority = new_cost + heuristic(finish, visit)
                frontier.put(visit, priority)
                parent[visit] = current

    return total_cost[current]

# Membentuk matriks subgraph dari list node dan edge yang telah dibuat
def subgraph_matrix(node_data, edge_data, unvalued_node) :
    index = {}
    for i in range(len(unvalued_node)) :
        index[unvalued_node[i]] = i
    subgraph = [[0 for i in range(len(unvalued_node))] for j in range(len(unvalued_node))]

    for i in range(len(unvalued_node)) :
        for j in range(len(unvalued_node)) :
            if i > j : 
                subgraph[i][j] = subgraph[j][i]
                # print(i,j,subgraph[i][j])
            elif i < j :
                subgraph[i][j] = a_star(unvalued_node[i], unvalued_node[j], node_data, edge_data)
    
    return index,subgraph


# Main function
city = input("Masukkan wilayah yang ingin dianalisis : ")
if(city == "OL"):
    edge_data = read_edges("OLcedge")
    node_data = read_nodes("OLcnode")
elif(city == "SF"):
    edge_data = read_edges("SFcedge")
    node_data = read_nodes("SFcnode")
else:
    edge_data = read_edges("exedge")
    node_data = read_nodes("exnode")

node1 = int(input("Masukkan node 1 : "))
node2 = int(input("Masukkan node 2 : "))
print()
print("Rute terpendek dari " + str(node1) + " ke " + str(node2) + " adalah :")
print(a_star(node1,node2,node_data,edge_data))
print()
dest = [i for i in range(6)]
idx,sg = subgraph_matrix(node_data, edge_data, dest)

print("Matriks rute terpendek hasil algoritma A* :")
for row in sg:
    print(row)