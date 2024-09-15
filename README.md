# Overview
This project implements and analyzes heap data structures, specifically focusing on their applications in sorting (Heapsort) and priority queue operations. We also compare Heapsort to other sorting algorithms such as Quicksort and Merge Sort and evaluate the performance of a priority queue in task scheduling scenarios.


# How to Run the Code:
1. Ensure Python is Installed on your system.
2. Clone the repository from GitHub: : https://github.com/Tushar-4747/MSCS532_Assignment4.git
3. Navigate to the project directory: cd MSCS532_Assignment4

# Summary of Findings

1. Heapsort Efficiency:

- Heapsort has a consistent time complexity of O(n log n) in all cases (worst, average, best).
- Compared to Quicksort and Merge Sort, Heapsort is slightly slower on average due to constant factors but has better worst-case performance.

2. Priority Queue Analysis:

- The priority queue efficiently handles task scheduling using a binary heap.
- Key operations like insert, extract_max/min, and increase_key maintain the heap property in O(log n) time.
- The priority queue demonstrated significant efficiency when simulating task scheduling with varying priorities.

3. Real-World Applications:

- The priority queue can be applied in operating system scheduling, where tasks must be processed based on their importance (priority).
- Heapsort is valuable in applications requiring stable performance guarantees, such as in embedded systems with limited resources.
