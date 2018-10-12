Add your answers to the questions below.

1. What is the runtime complexity of your `depth_first_for_each` method?
O(n) since it simply traverses all the nodes in the structure
2. What is the space complexity of your `depth_first_for_each` function?
O(n) as well since we are storing
3. What is the runtime complexity of your `breadth_first_for_each` method?
O(n) only one loop
4. What is the space complexity of your `breadth_first_for_each` method?
O(n) because of the stack
5. What is the runtime complexity of your `heapsort` function?
O(log n) heap is contructed linearly and then it performs a logaritmic operation n-1 times
6. What is the space complexity of the `heapsort` function? Recall that your implementation should return a new array with the sorted data. What would be the space complexity if your function instead altered the input array?
Because we iterate over the array to add to heap it's O(n) but if we could sort the array in place we can reduce the space complexity to O(1).
