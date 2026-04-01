n = int(input())
ans_s = n

root = int(n**0.5)

start = root - 1000000
if start < 1:
    start = 1

end = root + 1000000
if end > n:
    end = n

for rad in range(start, end + 1):
    k = n // rad
    rad_count = n % rad

    count_base = rad-rad_count
    count_plus_one = rad_count

    is_ok = False
    count_max = 0

    if rad_count == 0:
        is_ok = True
        count_max = k
    else:
        diff_counts = count_base - count_plus_one
        if diff_counts < 0:
            diff_counts = -diff_counts
        if diff_counts <= 1:
            is_ok = True
            count_max = k + 1

    if is_ok:
        ans = rad - count_max
        if ans < 0:
            ans = -ans
        if ans < ans_s:
            ans_s = ans

print(ans_s)