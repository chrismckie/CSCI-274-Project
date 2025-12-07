def create_interval_schedule(job_interval, start_time, finish_time, priority):
    n = len(start_time)

    # Step 1: Sort jobs by finish time and renumber so f1 <= f2 <= ... <= fn -> O(n log n)
    jobs = []
    for i in range(n):
        jobs.append((job_interval[i], start_time[i], finish_time[i], priority[i], i))

    jobs.sort(key=lambda f: f[2])
    
    # Set up DP table
    start = [jobs[i][1] for i in range(n)]
    finish = [jobs[i][2] for i in range(n)]
    weight = [jobs[i][3] for i in range(n)]
    original_indices = [jobs[i][4] for i in range(n)]

    # Step 2: Compute p[1], p[2], ..., p[n], Latest job that DOESN'T overlap with job j -> O(log n)
    p = []
    for j in range(n):
        # Using binary search keeps this at O(log n)
        p.append(binary_search(finish, start[j], j))

    # Step 3: Populate DP array -> O(n)
    M = [0] * (n + 1)
    for j in range(1, n + 1):
        i = j - 1   # weight and p are 0 indexed, so they use i, while M uses j

        if p[i] != -1:
            M[j] = max(M[j - 1], weight[i] + M[p[i] + 1])
        else:
            # p[i] = -1 means no predecessor, so p[i] = 0
            M[j] = max(M[j - 1], weight[i])

    # Step 4: Return results
    selected_jobs = construct_solution(n, weight, p, M, original_indices)
    return M[n], selected_jobs

def binary_search(finish_times, start, curr):
    low, high = 0, curr - 1

    # Stores the latest time that doesn't overlap
    result = -1

    while low <= high:
        mid = (low + high) // 2

        if finish_times[mid] <= start:
            # Finish time doesn't overlap -> update result and search later times
            result = mid
            low = mid + 1
        else:
            # Finish time overlaps -> search earlier times
            high = mid - 1

    return result

def construct_solution(n, weight, p, M, original_indices):
    selected_jobs = []
    j = n

    # Reconstruct solution by backtracking through M
    while j > 0:
        i = j - 1
        # Check if job was included in M
        if weight[i] + M[p[i] + 1] >= M[j - 1]:
            # Job included, move to p[j] predecessor
            selected_jobs.append(original_indices[i])
            j = p[i] + 1 if p[i] != -1 else 0
        else:
            # Job is not included, move to j-1 prev job
            j -= 1

    # Reverse the array to get the correct order
    selected_jobs.reverse()

    return selected_jobs