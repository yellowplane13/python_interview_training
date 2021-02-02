#Implement BFS with queue from Queue
# follow this guy: https://www.youtube.com/watch?v=PQhMkmhYZjQ&t=344s&ab_channel=PyTechVision
from queue import Queue
vertices = {
    'A':['B','D'],
    'B':['C','A'],
    'C':['B'],
    'D':['A','E','F'],
    'E':['D','F','G'],
    'F':['D','E','H'], 
    'G':['E','H'],
    'H':['G','F']
}
# initialize all the required dictionaries and variables
s = 'A' # source node
print(s,": Source Node")

visited = {}
distance = {} # distance from the source to every node
path = []
parent = {} # parent of every node is stored here
queue = Queue() # contains all the children of the current element that will be looped over for the next round

# set them to default values
for node in vertices.keys():
    parent[node] = None
    distance[node] = float("-inf") 

# initialize source values
visited[s] = True
distance[s] = 0
queue.put(s)

while not queue.empty():
    s = queue.get()
    path.append(s)
    for v in vertices[s]:
        if v not in visited:
            visited[v] = True
            distance[v] = distance[s]+1
            parent[v] = s
            queue.put(v)
            #print(visited)
            #print(path)

print(path,":total path")
#print(distance)

# CODE TO GET THE SHORTEST PATH FROM SOURCE NODE
d = 'C'
shortestPath = []
while parent[d] is not None:
    shortestPath.append(d)
    d = parent[d]
shortestPath.append(d)
shortestPath.reverse()
print(shortestPath,":shortest path")

