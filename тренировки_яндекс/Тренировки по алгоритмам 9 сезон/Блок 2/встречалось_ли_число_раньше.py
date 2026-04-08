nums = list(map(int, input().split()))
set_nums = set()

for num in nums:
    if num in set_nums:
        print("YES")
    else:
        print("NO")
        set_nums.add(num)