# BFS - Breadeth First Search

[Link to reference](https://favtutor.com/blogs/breadth-first-search-python)

Breadth-First Search (BFS) is an algorithm used for traversing graphs or trees. Traversing means visiting each node of the graph.

Breadth-First Search in tree and graph is almost the same. The only difference is that the graph may contain cycles, so we may traverse to the same node again.

 
BFS uses a queue.


The steps of the algorithm work as follow:

 - Start by putting any one of the graph’s vertices at the back of the queue.
 - Now take the front item of the queue and add it to the visited list.
 - Create a list of that vertex's adjacent nodes. Add those which are not within the visited list to the rear of the queue.
 - Keep continuing steps two and three till the queue is empty.


