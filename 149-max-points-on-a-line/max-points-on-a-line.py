class Solution(object):
    def maxPoints(self, points):
        from collections import defaultdict

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return abs(a)

        n = len(points)
        if n <= 2:
            return n

        ans = 0

        for i in range(n):
            slopes = defaultdict(int)

            for j in range(i + 1, n):
                dx = points[j][0] - points[i][0]
                dy = points[j][1] - points[i][1]

                g = gcd(dx, dy)
                dx //= g
                dy //= g

                if dx < 0:
                    dx = -dx
                    dy = -dy
                elif dx == 0:
                    dy = 1
                elif dy == 0:
                    dx = 1

                slopes[(dy, dx)] += 1

            max_line = 0
            for count in slopes.values():
                max_line = max(max_line, count)

            ans = max(ans, max_line + 1)

        return ans