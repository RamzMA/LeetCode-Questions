from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        """
        Asteroid Collision - #735

        Positive asteroids get pushed, negative ones may collide with the top of the stack.
        If the top is smaller pop and continue, if equal pop and break (both destroyed), if larger just break (new one destroyed).
        The while/else means the asteroid only gets added if it survived all collisions.

        Time complexity: O(n)
        Space complexity: O(n)
        """
        stack = []

        for ast in asteroids:
            while stack and ast < 0 and stack[-1] > 0:
                if stack[-1] < abs(ast):
                    stack.pop()
                    continue
                elif stack[-1] == abs(ast):
                    stack.pop()
                break
            else:
                stack.append(ast)
        return stack


# test cases
solution = Solution()
print(solution.asteroidCollision([5, 10, -5]))  # [5, 10]
print(solution.asteroidCollision([8, -8]))  # []
print(solution.asteroidCollision([10, 2, -5]))  # [10]
print(solution.asteroidCollision([-2, -1, 1, 2]))  # [-2, -1, 1, 2]
print(solution.asteroidCollision([1, -2, -2, -2]))  # [-2, -2, -2]
