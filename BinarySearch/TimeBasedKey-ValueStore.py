class TimeMap:
    """
    Time Based Key Value Store - #981

    Store values in a hashmap where each key maps to a list of [value, timestamp] pairs.
    Since timestamps are inserted in increasing order the list is always sorted, allowing binary search on get().
    Find the largest timestamp <= the given timestamp and return its value.

    Time complexity: O(1) set, O(log n) get
    Space complexity: O(n)
    """

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.store.get(key, [])
        l, r = 0, len(values) - 1

        while l <= r:
            m = (l + r) // 2
            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1
        return res


# test cases
obj = TimeMap()
obj.set("foo", "bar", 1)
print(obj.get("foo", 1))  # "bar"
print(obj.get("foo", 3))  # "bar"
obj.set("foo", "bar2", 4)
print(obj.get("foo", 4))  # "bar2"
print(obj.get("foo", 5))  # "bar2"
print(obj.get("foo", 0))  # ""
