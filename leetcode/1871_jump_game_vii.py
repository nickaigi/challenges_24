class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        i, j = 0, 0

        while i < n:
            j = i + minJump
            print(f"{j=}, {i=}")

            if j < n and s[j] == "0":
                i = j
                continue

            j = min((i + maxJump), (n - 1))
            if j < n and s[j] == "0":
                i = j
            else:
                return False
            print(f"New i: {i}")
        return True


if __name__ == "__main__":
    sol = Solution()

    s = "011010"
    minJump = 2
    maxJump = 3
    assert sol.canReach(s, minJump, maxJump)

    s = "00111010"
    minJump = 3
    maxJump = 5
    sol.canReach(s, minJump, maxJump)
    # assert not sol.canReach(s, minJump, maxJump)
    # print("TESTS Passed")
