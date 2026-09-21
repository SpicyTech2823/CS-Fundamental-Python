# CS Fundamentals --- Python

This repository is organized around core **Data Structures, Algorithms,
Networking, Operating Systems, Processes/Threads, and Synchronization**
concepts.

The goal of each topic is to understand **how the idea works, why it is
useful, and what problem it solves** rather than focusing on
implementation details.

------------------------------------------------------------------------

## 01 --- Data Structures

Data structures are ways of organizing and storing data so that
operations such as accessing, inserting, deleting, and searching can be
performed efficiently.

### `arrays.py` --- Arrays

An array stores a collection of elements in an ordered sequence.

**Core concept:** - Elements are stored at positions called indexes. -
An index provides direct access to an element. - Arrays are useful when
we need fast access to elements by position. - Inserting or removing
elements in the middle can require shifting other elements.

**Key idea:**\
Arrays are good for **ordered data with frequent index-based access**.

------------------------------------------------------------------------

### `linked_lists.py` --- Linked Lists

A linked list stores data in separate nodes. Each node contains data and
a reference to another node.

**Core concept:** - A node points to the next node in the sequence. -
The list does not require elements to be stored next to each other in
memory. - Moving through the list normally starts from the first node
and follows links. - Inserting or deleting a node can be efficient when
the correct position/node is already known.

**Key idea:**\
Linked lists are useful when **connections between elements are more
important than direct index access**.

------------------------------------------------------------------------

### `stack.py` --- Stack

A stack follows the **LIFO (Last In, First Out)** principle.

**Core concept:** - The most recently added item is removed first. -
Adding an item is called a push. - Removing the top item is called a
pop. - The top of the stack is the main point of interaction.

**Real-world examples:** - Undo operations - Browser history - Function
call management - Expression evaluation

**Key idea:**\
A stack behaves like a **pile of plates**: the last plate placed on top
is the first one removed.

------------------------------------------------------------------------

### `queue.py` --- Queue

A queue follows the **FIFO (First In, First Out)** principle.

**Core concept:** - The first item added is the first item removed. -
New items enter at the back. - Items leave from the front.

**Real-world examples:** - Print queues - Task scheduling - Customer
waiting lines - Network packet processing

**Key idea:**\
A queue behaves like a **line of people waiting for service**.

------------------------------------------------------------------------

### `tree.py` --- Trees

A tree represents hierarchical relationships between data.

**Core concept:** - A tree starts with a root. - Nodes can have
children. - Nodes can have parent-child relationships. - A tree does not
normally contain cycles. - Different tree structures are useful for
different operations.

**Real-world examples:** - File systems - Organization structures - HTML
document structure - Search trees

**Key idea:**\
Trees are useful for representing **hierarchical data**.

------------------------------------------------------------------------

### `graph.py` --- Graphs

A graph represents relationships between objects.

**Core concept:** - Objects are represented as vertices/nodes. -
Relationships are represented as edges. - Edges can be directed or
undirected. - Edges can also have weights, such as distance or cost.

**Real-world examples:** - Social networks - Road networks - Computer
networks - Dependency relationships

**Key idea:**\
Graphs are useful when data is connected through **general
relationships**, rather than a simple hierarchy.

------------------------------------------------------------------------

### `hash_table.py` --- Hash Tables

A hash table stores data using **key-value relationships**.

**Core concept:** - A key is processed by a hash function. - The hash
function determines where the associated value should be stored. -
Searching can be very fast when the hash function distributes keys
well. - Different keys can sometimes produce the same storage location.
This is called a collision. - Collision-handling strategies are needed
to store and retrieve data correctly.

**Real-world examples:** - Dictionaries/maps - Caches - Fast lookup
tables - Symbol tables

**Key idea:**\
Hash tables are designed for **fast lookup using keys**.

------------------------------------------------------------------------

## 02 --- Algorithms

Algorithms are step-by-step procedures for solving problems.

### `searching/linear_search.py` --- Linear Search

Linear search checks elements one by one until the target is found or
all elements have been checked.

**Core concept:** 1. Start from the first element. 2. Compare it with
the target. 3. If it matches, stop. 4. Otherwise, move to the next
element. 5. Continue until the target is found or the collection ends.

**Key idea:**\
Simple and works even when the data is **not sorted**, but it may need
to inspect many elements.

------------------------------------------------------------------------

### `searching/binary_search.py` --- Binary Search

Binary search repeatedly divides a **sorted** collection into smaller
sections.

**Core concept:** 1. Look at the middle element. 2. Compare it with the
target. 3. If it matches, the search is complete. 4. If the target is
smaller, continue in the left half. 5. If the target is larger, continue
in the right half. 6. Repeat until the target is found or no elements
remain.

**Key idea:**\
Binary search is efficient because each step eliminates roughly half of
the remaining search space.

**Important requirement:**\
The data must be ordered appropriately before binary search can be used.

------------------------------------------------------------------------

### `bfs.py` --- Breadth-First Search

BFS explores a graph **level by level**.

**Core concept:** - Start from a selected node. - Visit its immediate
neighbors first. - Then visit the neighbors of those nodes. - Continue
outward layer by layer. - A queue is commonly used to remember which
nodes should be explored next. - A visited record prevents repeatedly
processing the same node.

**Real-world examples:** - Finding the minimum number of connections in
an unweighted graph - Exploring a network by distance from a starting
point

**Key idea:**\
BFS explores **nearby nodes before farther nodes**.

------------------------------------------------------------------------

### `dfs.py` --- Depth-First Search

DFS explores as far as possible along one path before going back and
trying another path.

**Core concept:** - Start from a selected node. - Follow one neighbor
deeply. - Continue until there is nowhere new to go. - Backtrack to an
earlier point. - Explore another available path. - A visited record
prevents cycles from causing endless exploration.

DFS can be understood using: - A stack, or - Recursion, which naturally
uses the program's call stack.

**Key idea:**\
DFS explores **deep into a path before exploring alternatives**.

------------------------------------------------------------------------

### `bubble_sort.py` --- Bubble Sort

Bubble sort repeatedly compares neighboring elements and swaps them when
they are in the wrong order.

**Core concept:** - Compare adjacent elements. - Swap them if their
order is incorrect. - Continue through the collection. - After one
complete pass, an element is moved toward its correct position. - Repeat
until the collection is sorted.

**Key idea:**\
Bubble sort is easy to understand and demonstrates the idea of
**repeated local comparisons and swaps**, but it is generally
inefficient for large datasets.

------------------------------------------------------------------------

## 03 --- Networking

The networking section contains practical labs organized by week.

### `Labs/Week1`

Introduces fundamental networking concepts and provides the foundation
for understanding how devices communicate.

**Core ideas may include:** - Basic network communication - Hosts and
network devices - Addresses - Packets - Basic network architecture

**Key idea:**\
Understand the basic components involved when **one device communicates
with another**.

------------------------------------------------------------------------

### `Labs/Week2`

Builds on the networking foundation by exploring how communication is
organized and managed.

**Core ideas may include:** - Communication between devices - Network
addressing - Protocol concepts - How information moves through a network

**Key idea:**\
Understand how devices **identify each other and exchange information**.

------------------------------------------------------------------------

### `Labs/Week4`

Focuses on more detailed networking behavior and practical network
concepts.

**Key idea:**\
Move from basic networking concepts toward understanding **how networks
operate in practice**.

------------------------------------------------------------------------

### `Labs/Week5`

Continues practical networking work with more advanced network concepts
and lab exercises.

**Key idea:**\
Connect individual networking concepts together to understand **larger
communication processes**.

------------------------------------------------------------------------

### `Labs/Week6`

Further develops networking knowledge through practical exercises.

**Key idea:**\
Use the concepts learned in earlier weeks to reason about **real network
behavior and communication**.

> The exact topics inside each weekly lab depend on the exercises
> contained in those folders. The folders are kept separate so each
> stage of the networking material can be studied independently.

------------------------------------------------------------------------

## 04 --- Operating Systems

Operating systems manage computer resources and coordinate programs,
processes, memory, files, and hardware.

### `CPU-Scheduling/fcfs.py` --- First-Come, First-Served

FCFS is a CPU scheduling strategy where processes are handled according
to their arrival order.

**Core concept:** - The process that arrives first gets the CPU first. -
A process normally keeps the CPU until it finishes or otherwise gives it
up. - Later processes wait behind earlier processes.

**Important scheduling concepts:** - Arrival time: when a process
becomes ready. - Burst time: how long the process needs the CPU. -
Waiting time: how long a process waits before execution. - Turnaround
time: total time from arrival until completion.

**Key idea:**\
FCFS is simple because scheduling follows **arrival order**.

------------------------------------------------------------------------

## Processes and Threads

### `processes_thread/process.py` --- Processes

A process is a running instance of a program.

**Core concept:** - A process has its own execution context and
resources. - Separate processes are generally isolated from one
another. - Communication between processes requires mechanisms that
allow them to exchange information. - Multiple processes can execute
concurrently.

**Key idea:**\
A process represents an **independent running program/environment**.

------------------------------------------------------------------------

### `processes_thread/threads.py` --- Threads

A thread is a unit of execution inside a process.

**Core concept:** - A process can contain multiple threads. - Threads
within the same process share many resources. - Each thread has its own
execution flow. - Multiple threads can work on different tasks within
the same program.

**Key idea:**\
Threads allow a program to have **multiple execution paths within one
process**.

------------------------------------------------------------------------

## Synchronization

### `Synchronization/`

Synchronization deals with coordinating multiple processes or threads
that operate on shared resources.

**Why synchronization is needed:**

When multiple execution flows access shared data at the same time, their
operations can interfere with each other.

For example, imagine two threads both trying to update the same counter:

1.  Thread A reads the current value.
2.  Thread B reads the same value.
3.  Thread A calculates a new value.
4.  Thread B calculates a new value.
5.  One update may overwrite the other.

This type of problem is commonly called a **race condition**.

### Core synchronization concepts

#### Critical Section

A critical section is the part of a program where shared data or a
shared resource is accessed.

The goal is to ensure that conflicting operations do not happen at the
same time.

#### Mutual Exclusion

Mutual exclusion means that only one execution flow can enter a
protected critical section at a time.

#### Lock

A lock provides a mechanism for controlling access to shared resources.

A thread obtains the lock before entering a protected section and
releases it when finished.

#### Race Condition

A race condition occurs when the result depends on the timing or
ordering of concurrent operations.

**Key idea:**\
Synchronization makes concurrent programs **predictable and safe when
sharing resources**.

------------------------------------------------------------------------

# How the Topics Connect

These topics are not isolated. They build a foundation for understanding
how software works.

``` text
Data Structures
      │
      ├── Arrays
      ├── Linked Lists
      ├── Stacks
      ├── Queues
      ├── Trees
      ├── Graphs
      └── Hash Tables
             │
             ▼
Algorithms
      │
      ├── Searching
      │     ├── Linear Search
      │     └── Binary Search
      │
      ├── Graph Traversal
      │     ├── BFS
      │     └── DFS
      │
      └── Sorting
            └── Bubble Sort
             │
             ▼
Networking
             │
             ▼
Operating Systems
      │
      ├── CPU Scheduling
      ├── Processes
      ├── Threads
      └── Synchronization
```

## Quick Mental Model

  -----------------------------------------------------------------------
  Topic                               Main Question
  ----------------------------------- -----------------------------------
  Array                               How can I store ordered data and
                                      access it by position?

  Linked List                         How can elements be connected
                                      without requiring contiguous
                                      storage?

  Stack                               How can I process the newest item
                                      first?

  Queue                               How can I process the oldest item
                                      first?

  Tree                                How can I represent hierarchy?

  Graph                               How can I represent general
                                      relationships?

  Hash Table                          How can I find data quickly using a
                                      key?

  Linear Search                       How can I find an item by checking
                                      elements one by one?

  Binary Search                       How can I repeatedly eliminate half
                                      of a sorted search space?

  BFS                                 How can I explore a graph level by
                                      level?

  DFS                                 How can I explore deeply before
                                      backtracking?

  Bubble Sort                         How can repeated neighbor
                                      comparisons produce sorted data?

  Networking                          How do computers communicate?

  CPU Scheduling                      How does an operating system decide
                                      which process uses the CPU?

  Process                             How does the OS manage an
                                      independent running program?

  Thread                              How can one process have multiple
                                      execution paths?

  Synchronization                     How can concurrent execution safely
                                      share resources?
  -----------------------------------------------------------------------

## Suggested Learning Order

A useful way to study this repository is:

1.  **Arrays**
2.  **Linked Lists**
3.  **Stacks and Queues**
4.  **Trees**
5.  **Graphs**
6.  **Hash Tables**
7.  **Linear Search**
8.  **Binary Search**
9.  **Bubble Sort**
10. **BFS and DFS**
11. **Networking fundamentals**
12. **CPU Scheduling**
13. **Processes**
14. **Threads**
15. **Synchronization**

The main goal is not just to memorize definitions. Try to understand the
**problem each structure or algorithm solves, how information flows
through it, and what trade-offs it introduces**.
