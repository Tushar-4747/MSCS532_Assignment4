class Task:

    def __init__(self, task_id, priority, arrival_time, deadline):
        self.task_id = task_id
        self.priority = priority# Priority level 
        self.arrival_time = arrival_time
        self.deadline = deadline

    def __repr__(self):
        return f"Task(ID: {self.task_id}, Priority: {self.priority}, Arrival: {self.arrival_time}, Deadline: {self.deadline})"


class PriorityQueue:
    def __init__(self, max_heap=True):
        self.heap = []
        self.max_heap = max_heap 

    def insert_task(self, task):
        
        self.heap.append(task)
        self._heapify_up(len(self.heap) - 1)

    def max_or_min_task(self):
        if self.is_empty():
            return None
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        max_or_min_task = self.heap.pop()
        self._heapify_down(0)
        return max_or_min_task

    def increase_or_decrease_key(self, task_id, new_priority):
        # Find the task 
        for idx, task in enumerate(self.heap):
            if task.task_id == task_id:
                old_priority = task.priority
                task.priority = new_priority

                if (self.max_heap and new_priority > old_priority) or (not self.max_heap and new_priority < old_priority):
                    self._heapify_up(idx)
                else:
                    self._heapify_down(idx)
                return task
        return None

    def _heapify_up(self, idx):
        parent_idx = (idx - 1) // 2
        while idx > 0 and self.compare_task(self.heap[idx], self.heap[parent_idx]):
            self.heap[idx], self.heap[parent_idx] = self.heap[parent_idx], self.heap[idx]
            idx = parent_idx
            parent_idx = (idx - 1) // 2

    def _heapify_down(self, idx):
        size = len(self.heap)
        while idx < size:
            left_child = 2 * idx + 1
            right_child = 2 * idx + 2
            if left_child >= size:
                break
            if right_child < size and self.compare_task(self.heap[right_child], self.heap[left_child]):
                child_idx = right_child
            else:
                child_idx = left_child
            if self.compare_task(self.heap[child_idx], self.heap[idx]):
                self.heap[idx], self.heap[child_idx] = self.heap[child_idx], self.heap[idx]
                idx = child_idx
            else:
                break

    def compare_task(self, task1, task2):
        if self.max_heap:
            return task1.priority > task2.priority#Max heap comparison
        else:
            return task1.priority < task2.priority# min heap comparison

    def is_empty(self):
        return len(self.heap) == 0

pq = PriorityQueue(max_heap=True)#max-heap priority 
pq.insert_task(Task(101, 10, 0, 20))
pq.insert_task(Task(102, 15, 4, 25))
pq.insert_task(Task(103, 5, 7, 30))

print("Heap_after_insertions:", pq.heap)
print("Maximum priority task:", pq.max_or_min_task())
print("Heap after extraction:", pq.heap)

pq.increase_or_decrease_key(103, 20)#Increase priority
print("Heap after increasing task 103 priority:", pq.heap) #print in
print("Is heap empty?", pq.is_empty())
