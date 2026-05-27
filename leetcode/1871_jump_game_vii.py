from collections import deque


class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        # if the last character isn't a '0', we can never reach it
        if s[n - 1] != "0":
            return False

        queue = deque([0])
        far_reached = 0  # To avoid re-checking indices we've already looked at

        while queue:
            curr = queue.popleft()

            # if we reached the end, we're done
            if curr == n - 1:
                return True

            # The window of indices we can legally jump to
            start = max(curr + minJump, far_reached + 1)
            end = min(curr + maxJump, n - 1)

            for j in range(start, end + 1):
                if s[j] == "0":
                    queue.append(j)
            # ensure we don't scan the indices again from a future 'curr'
            far_reached = max(far_reached, end)

        return False


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
    assert not sol.canReach(s, minJump, maxJump)
    print("TESTS Passed")
