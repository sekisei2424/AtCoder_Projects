import collections
import bisect

def solve():
    N = int(input())
    S_values = list(map(int, input().split()))

    domino_info = []
    for i in range(N):
        domino_info.append((S_values[i], i))

    domino_info_sorted = sorted(domino_info)

    original_idx_to_sorted_idx = [0] * N
    for i, (s_val, original_idx) in enumerate(domino_info_sorted):
        original_idx_to_sorted_idx[original_idx] = i

    start_sorted_idx = original_idx_to_sorted_idx[0]
    queue = collections.deque([(start_sorted_idx, 1)])

    sorted_visited = [False] * N
    sorted_visited[start_sorted_idx] = True

    end_original_idx = N - 1

    search_ptr = 0 

    while queue:
        current_sorted_idx, current_count = queue.popleft()
        
        current_s_val, current_original_idx = domino_info_sorted[current_sorted_idx]

        if current_original_idx == end_original_idx:
            print(current_count)
            return

        reach_limit = 2 * current_s_val
        
        # search_ptr が現在の current_s_val から到達可能な範囲内にあるドミノを指すように更新
        # このwhileループとsearch_ptrの更新により、各ドミノは最大でも1回しか処理されない
        while search_ptr < N and domino_info_sorted[search_ptr][0] <= reach_limit:
            if not sorted_visited[search_ptr]:
                sorted_visited[search_ptr] = True
                queue.append((search_ptr, current_count + 1))
            search_ptr += 1
            
        # 注意: キューから取り出したノードが、以前のノードの search_ptr で既に処理されていて
        # 訪問済みになっている可能性があるため、search_ptr の更新と visited のチェックの順序が重要。
        # 上記のコードでは、search_ptr を常に進めることで、すでに訪問済みのドミノをスキップし、
        # 未訪問のドミノだけをキューに追加している。

    print(-1)


T = int(input())
for _ in range(T):
    solve()