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

**8-Queen Problem**

NQueens(row)

1. If row = 8
      Print the solution
      Return True

2. For each column from 0 to 7

      If placing a queen at (row, column) is safe

            Place Queen at (row, column)

            NQueens(row + 1)

            Remove Queen from (row, column)
            // Backtrack

End NQueens


