from collections import defaultdict

class Dijkstra:
    
    def Initialization(self, n , mat, s):
         # Function to initialize all required variables.
         # graph: storing weight for edges
         # adj: dictionary to store adjacent vertices
         # distFromSrc: List of distances of all vertices from start vertex
         # usp: List to store binary variable for to each vertex
         # shortPath: Stores visited vertices
         self.distFromSrc, self.shortPath, self.usp = [float('inf') for _ in range(n+1)], [], [1 for _ in range(n+1)]
         self.distFromSrc[s] = 0
         self.adj = defaultdict(list)
         self.queue = []
         self.graph = [[0 for _ in range(n+1)] for _ in range(n+1)]
         
         # Create the adjacency list and graph
         for r in range(len(mat)):
             self.adj[mat[r][0]].append(mat[r][1])
             self.adj[mat[r][1]].append(mat[r][0])
             self.graph[mat[r][0]][mat[r][1]] = self.graph[mat[r][1]][mat[r][0]] = mat[r][2]
             
         for i in range(n+1):
             self.queue.append([i, self.distFromSrc[i]])
             
    def Build_heap(self, n):
        # Function to build a min heap initially
        for i in range(n//2,-1,-1):
            self.Heapify(n, i)
        
    def Heapify(self, n, i):
        # Helper function to build min heap and to maintain heap property during extract min and update operations
        size = n
        left = 2*i + 1
        right = 2*i + 2
        smallest = i
    
        if left < size and self.queue[left][1] < self.queue[i][1]:
            smallest = left
    
        if right < size and self.queue[right][1] < self.queue[smallest][1]:
            smallest = right
    
        if smallest != i:
            self.queue[i], self.queue[smallest] = self.queue[smallest], self.queue[i]
            self.Heapify(n, smallest)
    
    def Extract_min(self):
        # Function to return vertex with minimum distance from source
        vertex = self.queue.pop(0)
        self.Heapify(len(self.queue), 0)
        return vertex
    
    def Update_dist(self, vertex, oldDistance, newDistance):
        # Helper function to update  distance from source for a vertex, called from RELAX
        idx = self.queue.index([vertex, oldDistance])
        self.queue[idx][1] = newDistance
        self.Heapify(len(self.queue), 0)
    
    def Relax(self, u, v, w):
        # Function required up update distance of vertex from source and the usp values
        if self.distFromSrc[u] + w < self.distFromSrc[v]:
            self.Update_dist(v, self.distFromSrc[v], self.distFromSrc[u] + w)
            self.distFromSrc[v] = self.distFromSrc[u] + w
            self.usp[v] = self.usp[u]
        elif self.distFromSrc[u] + w == self.distFromSrc[v]:
            self.usp[v] = 0       

    def Dijkstra_alg(self, n, e, mat, s):
         # Function to run the algorithm and send out results
         self.Initialization(n, mat, s)
         self.Build_heap(n)

         res = []
         
         while len(self.queue) > 0:
             u = self.Extract_min()
             ver, dist = u[0], u[1]
             self.shortPath.append(ver)
             for v in self.adj[ver]:
                 if v not in self.shortPath:
                     self.Relax(ver, v, self.graph[ver][v])
                     
         for i in range(1, n+1):
            res.append([self.distFromSrc[i], self.usp[i]])
            
         print ("Unique Shortest Path: ")
         for i in range(len(res)):
             if res[i][1] == 0: 
                 res[i][1] = 'N'
             else:
                 res[i][1] = 'Y'
             print ("Vertex: " + str(i+1) + " ,Distance from Source: " + str(res[i][0]) + " ,USP: " + str(res[i][1]))
         
     

# Input format:
# N = Number of nodes
# E = Number of edges
# Mat = A matrix of dimension Ex3
# Each row of Mat consist of 3 integers. The first 2 integers denote the 2 nodes between which the
# undirected edge exists. The third integer denotes the weight of edge between these corresponding nodes
# S = source vertex to start Dijkstra Algorithm

N = 5
E = 5
Mat = [[1, 3, 2], [1, 5, 3], [2, 5, 3], [4, 1, 1], [4, 2, 1]]
S = 4
D = Dijkstra()
D.Dijkstra_alg(N, E, Mat, S)
