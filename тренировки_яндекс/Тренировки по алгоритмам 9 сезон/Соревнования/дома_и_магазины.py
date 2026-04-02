lst = list(map(int, input().split()))
rasts = []
stores = [index for index, elem in enumerate(lst) if elem == 2]
houses = [index for index, elem in enumerate(lst) if elem == 1]

for house in houses:
    min_rast = min([abs(magaz - house) for magaz in stores])
    rasts.append(min_rast)

print(max(rasts))