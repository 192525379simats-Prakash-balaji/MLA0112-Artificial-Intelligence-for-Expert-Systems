**Breadth First Search** 

BFS(Graph, Start)

1. Create an empty queue Q
2. Create an empty set Visited

3. Mark Start as visited
4. Enqueue(Start) into Q

5. While Q is not empty
      Node ← Dequeue(Q)
      Print Node

      For each Neighbor of Node
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


8-Queen Problem
NQueens(Row)

If Row = 8

    Print Solution
    Return

For each Column from 0 to 7

    If Position(Row, Column) is Safe

        Place Queen

        NQueens(Row + 1)

        Remove Queen

End NQueens
8-Puzzle Problem (BFS)
EightPuzzle(Start, Goal)

Create Queue

Enqueue(Start)

Mark Start as Visited

While Queue is not empty

    State ← Dequeue

    If State = Goal

        Print Solution
        Stop

    Generate all Valid Moves

    For each New State

        If Not Visited

            Mark Visited
            Enqueue(New State)

End
Water Jug Problem (4L, 3L)
WaterJug(Start, Goal)

Create Queue

Enqueue(Start)

Mark Start as Visited

While Queue is not empty

    State ← Dequeue

    If Goal Reached

        Print Solution
        Stop

    Generate States by

        Fill Jug
        Empty Jug
        Transfer Water

    Add New States to Queue

End
Missionaries and Cannibals
MissionariesCannibals(Start, Goal)

Create Queue

Enqueue(Start)

Mark Start as Visited

While Queue is not empty

    State ← Dequeue

    If State = Goal

        Print Solution
        Stop

    Generate Valid Boat Moves

        1 Missionary
        2 Missionaries
        1 Cannibal
        2 Cannibals
        1 Missionary and 1 Cannibal

    Check Safety Condition

        Cannibals ≤ Missionaries

    Enqueue Valid States

End
Tic-Tac-Toe (Minimax)
Minimax(Board, IsMax)

If X Wins

    Return +1

If O Wins

    Return -1

If Board Full

    Return 0

If IsMax

    Best ← -∞

    For each Empty Cell

        Place X

        Best ← Max(Best, Minimax)

        Undo Move

    Return Best

Else

    Best ← +∞

    For each Empty Cell

        Place O

        Best ← Min(Best, Minimax)

        Undo Move

    Return Best
A* Search
AStar(Start, Goal)

Open ← Start

While Open is not empty

    Select Node with Lowest f(n)

    If Node = Goal

        Return Solution

    For each Neighbor

        g(n) = Cost from Start

        h(n) = Heuristic Value

        f(n) = g(n) + h(n)

        Add Neighbor to Open

End
Uniform Cost Search (UCS)
UCS(Start, Goal)

Create Priority Queue

Insert Start with Cost 0

While Queue is not empty

    Remove Lowest Cost Node

    If Node = Goal

        Return Cost

    For each Neighbor

        NewCost ← CurrentCost + EdgeCost

        Insert Neighbor with NewCost

End
Map Coloring
MapColoring(Region)

If All Regions Colored

    Print Solution
    Return

Select Uncolored Region

For each Color

    If Color is Safe

        Assign Color

        MapColoring(Next Region)

        Remove Color

End
Minimax Algorithm
Minimax(Node, Depth, IsMax)

If Leaf Node

    Return Value

If IsMax

    Return Maximum of Children

Else

    Return Minimum of Children

End
Alpha-Beta Pruning
AlphaBeta(Node, Depth, Alpha, Beta, IsMax)

If Leaf Node

    Return Value

If IsMax

    For each Child

        Alpha ← Max(Alpha, AlphaBeta)

        If Alpha ≥ Beta

            Stop

    Return Alpha

Else

    For each Child

        Beta ← Min(Beta, AlphaBeta)

        If Beta ≤ Alpha

            Stop

    Return Beta
Tower of Hanoi
Hanoi(N, Source, Destination, Auxiliary)

If N = 1

    Move Disk from Source to Destination

Else

    Hanoi(N-1, Source, Auxiliary, Destination)

    Move Disk N from Source to Destination

    Hanoi(N-1, Auxiliary, Destination, Source)

End
Bird Can Fly or Not
CanFly(Bird)

If Bird is Penguin or Ostrich

    Return False

Else

    Return True
First Order Logic
Human(X)

Mortal(X)

If Human(X)

    Then Mortal(X)

Example:

Human(Socrates)

Therefore Mortal(Socrates)
Universal Quantifier (∀)
For Every Element X

    Check Condition(X)

If All Conditions True

    Return True

Else

    Return False
Existential Quantifier (∃)
For Every Element X

    Check Condition(X)

If Any Condition True

    Return True

Else

    Return False
Prolog Sum of Integers (1 to N)
Sum(N)

If N = 0

    Return 0

Else

    Return N + Sum(N-1)
Three Jug Problem (Transfer Only)
ThreeJug(Start, Goal)

Create Queue

Enqueue(Start)

Mark Start as Visited

While Queue is not empty

    State ← Dequeue

    If State = Goal

        Print Solution
        Stop

    Transfer Water

        Jug1 → Jug2
        Jug1 → Jug3
        Jug2 → Jug1
        Jug2 → Jug3
        Jug3 → Jug1
        Jug3 → Jug2

    Enqueue New States

End

