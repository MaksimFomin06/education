nums1 = list(map(int, input().split()))
nums2 = list(map(int, input().split()))
set1 = set(nums1)
set2 = set(nums2)

out = []

for num in set1:
    if num in set2:
        out.append(num)

out.sort()

print(*out)