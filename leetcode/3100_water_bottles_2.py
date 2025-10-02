class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        drunk, empty = numBottles, numBottles
        while empty >= numExchange:
            drunk += 1
            empty -= numExchange - 1
            numExchange += 1
        return drunk


if __name__ == '__main__':
    numBottles = 13
    numExchange = 6
    sol = Solution()
    print(sol.maxBottlesDrunk(numBottles, numExchange))

    numBottles = 10
    numExchange = 3
    print(sol.maxBottlesDrunk(numBottles, numExchange))
