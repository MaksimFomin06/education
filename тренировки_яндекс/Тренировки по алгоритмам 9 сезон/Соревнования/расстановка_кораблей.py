field = [input().strip() for _ in range(10)]
used = [[False] * 10 for _ in range(10)]
sizes = []
is_correct = True

for r in range(10):
    for c in range(10):
        if field[r][c] == '#' and not used[r][c]:
            ship_cells = []
            stack = [(r, c)]
            used[r][c] = True

            while stack:
                curr_r, curr_c = stack.pop()
                ship_cells.append((curr_r, curr_c))
                for dr in range(-1, 2):
                    for dc in range(-1, 2):
                        nr, nc = curr_r + dr, curr_c + dc
                        if 0 <= nr < 10 and 0 <= nc < 10:
                            if field[nr][nc] == '#' and not used[nr][nc]:
                                used[nr][nc] = True
                                stack.append((nr, nc))

            rows = [p[0] for p in ship_cells]
            cols = [p[1] for p in ship_cells]
            h = max(rows) - min(rows) + 1
            w = max(cols) - min(cols) + 1

            if len(ship_cells) != h * w or (h > 1 and w > 1):
                is_correct = False

            sizes.append(len(ship_cells))

if is_correct and sorted(sizes) == [1, 1, 1, 1, 2, 2, 2, 3, 3, 4]:
    print("YES") 
else:   
    print("NO") 