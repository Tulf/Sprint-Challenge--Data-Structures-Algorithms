def heapsort(arr):
    # use Heap class to initialize heap and create a list for the sorted heap
    # array representation used for heaps beacuse it's space efficient and you can calculate the children easily
    # eg if index I, left child = 2I + 1 (odd) right child even: 2I + 2.
    heap = Heap()
    list = []
    #loop over array that's passed in and insert values into heap, so it is sorted by the below methods
    for i in arr:
        heap.insert(i)
    #loop over array  again and insert heap elements into list while deleting from heap (need to run seperately or heap won't be full)
    for i in arr:
        list.insert(0, heap.delete())
        # unforutnaley we have to use the stupid insert method here and can't just append
    # return the list as that we just sorted
    return list

class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        self.storage.append(value)
        self._bubble_up(len(self.storage) - 1)

    def delete(self):
        retval = self.storage[0]
        self.storage[0] = self.storage[len(self.storage) - 1]
        self.storage.pop()
        self._sift_down(0)
        return retval

    def get_max(self):
        return self.storage[0]

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        while (index - 1) // 2 >= 0:
            if self.storage[(index - 1) // 2] < self.storage[index]:
                self.storage[index], self.storage[(index - 1) // 2] = self.storage[(index - 1) // 2], self.storage[index]
            index = (index - 1) // 2

    def _sift_down(self, index):
        while index * 2 + 1 <= len(self.storage) - 1:
            mc = self._max_child(index)
            if self.storage[index] < self.storage[mc]:
                self.storage[index], self.storage[mc] = self.storage[mc], self.storage[index]
            index = mc

    def _max_child(self, index):
        if index * 2 + 2 > len(self.storage) - 1:
            return index * 2 + 1
        else:
            return index * 2 + 1 if self.storage[index * 2 + 1] > self.storage[index * 2 + 2] else index * 2 + 2
