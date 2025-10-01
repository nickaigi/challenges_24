class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total, empty_count = numBottles, numBottles
        while empty_count >= numExchange:
            drunk = empty_count // numExchange
            bal = empty_count % numExchange
            empty_count = drunk + bal
            total += drunk
        return total


if __name__ == '__main__':
    numBottles = 9
    numExchange = 3
    print(Solution().numWaterBottles(numBottles, numExchange))
