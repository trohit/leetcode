# https://leetcode.com/problems/lru-cache/
# when importing OrderedDict from collections is not possible
# since py 3.6 the built-in dict class also keeps its items ordered as well.
# But since dict() does not support move_to_end() and popitem() with args 
# we create our own move_to_end() and popitem(last) implementation
class LRUCache(dict):
    def __init__(self, capacity: int):
        self.cap = capacity
        
    def move_to_end(self, k):
        v = self[k]
        self.pop(k)
        self[k] = v
        
    def popitem(self, last:bool):
        if last == False:
            k = list(self.keys())[0]
            self.pop(k)
    
    def get(self, key: int) -> int:
        if key not in self:
            return -1
        self.move_to_end(key)
        return self[key]

    def put(self, key: int, value: int) -> None:
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.cap:
            self.popitem(last=False)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
