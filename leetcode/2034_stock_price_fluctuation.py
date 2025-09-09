import heapq


class StockPrice:

    def __init__(self):
        self.data: dict[int, int] = {}
        self.newest = 0
        self.min_heap = []
        self.max_heap = []

    def update(self, timestamp: int, price: int) -> None:
        self.data[timestamp] = price
        self.newest = max(self.newest, timestamp)

        heapq.heappush(self.min_heap, (price, timestamp))
        heapq.heappush(self.max_heap, (-price, timestamp))

    def current(self) -> int:
        return self.data[self.newest]

    def maximum(self) -> int:
        return 0

    def minimum(self) -> int:
        return 0


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()
