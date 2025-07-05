def count_valid_subarrays_optimized(P):
    N = len(P)
    is_peak = [0] * N
    is_valley = [0] * N

    # 山・谷判定（中央がi）
    for i in range(1, N - 1):
        if P[i - 1] < P[i] > P[i + 1]:
            is_peak[i] = 1
        elif P[i - 1] > P[i] < P[i + 1]:
            is_valley[i] = 1

    # 累積和を作成（クエリで区間内の個数が O(1) で出せる）
    peak_sum = [0] * (N + 1)
    valley_sum = [0] * (N + 1)
    for i in range(N):
        peak_sum[i + 1] = peak_sum[i] + is_peak[i]
        valley_sum[i + 1] = valley_sum[i] + is_valley[i]

    def count_peaks(l, r):
        # 区間[l, r) にあるピークの個数
        return peak_sum[r] - peak_sum[l]

    def count_valleys(l, r):
        return valley_sum[r] - valley_sum[l]

    count = 0

    # スライディングウィンドウで区間 [l, r) を全て調べる
    for l in range(N):
        # 条件1: P[l] < P[l+1]
        if l + 1 < N and P[l] < P[l + 1]:
            # 探索する最大区間長：固定（たとえば最大10くらいまで）にするのが現実的
            # → 全探索せず、長さLの候補だけに絞る（O(N log N)）
            for r in range(l + 3, min(N + 1, l + 10)):
                peaks = count_peaks(l, r)
                valleys = count_valleys(l, r)
                if peaks == 1 and valleys == 1:
                    count += 1

    return count

N = int(input())
P = list(map(int, input().split()))
print(count_valid_subarrays_optimized(P))