n, m = map(int, input().split())
grid = [list(input()) for _ in range(n)]

count = 0

for i in range(n):
    for j in range(m):
        if grid[i][j] == "#":
            count += 1
            queue = [(i, j)]
            grid[i][j] = "."
            
            head = 0
            while head < len(queue):
                r, c = queue[head]
                head += 1
                
                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nr, nc = r + dr, c + dc
                    
                    if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == "#":
                        grid[nr][nc] = "."
                        queue.append((nr, nc))

print(count) 