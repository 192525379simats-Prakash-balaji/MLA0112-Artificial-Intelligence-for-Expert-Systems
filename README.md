**Breadth First Search** 

BFS(Graph, Start)

1. Create an empty queue Q
2. Create an empty set Visited

3. Mark Start as visited
4. Enqueue(Start) into Q

5. While Q is not empty
      a. Node ← Dequeue(Q)
      b. Print Node

      c. For each Neighbor of Node
            If Neighbor is not visited
                  Mark Neighbor as visited
                  Enqueue(Neighbor)

End BFS

**Depth First Search**

DFS(Node)

1. Mark Node as visited
2. Print Node

3. For each Neighbor of Node
      If Neighbor is not visited
            DFS(Neighbor)

End DFS


