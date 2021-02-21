from collections import deque

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity= capacity
        self.l_map= dict()
        self.que= deque()

    def get(self, key: int) -> int:
        if key not in self.l_map:
            return -1
        self.que.remove(key)
        self.que.append(key)
        return self.l_map[key]

    def put(self, key, value):
        if key not in self.l_map:
            if len(self.que==self.capacity):
                oldest= self.que.popleft()
                del self.l_map[oldest]
        else:
            self.que.remove(key)
        self.que.append(key)
        self.l_map[key]= value


lru= LRUCache(2)
