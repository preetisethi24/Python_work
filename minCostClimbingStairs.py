def minCostClimbingStairs(cost):
    n = len(cost)
    if n == 0 or n == 1:
        return 0
    min_cost0, min_cost1 = cost[0], cost[1]
    for i in range(2, n):
        min_cost0, min_cost1 = min_cost1, min(min_cost0, min_cost1) + cost[i]
        print min_cost0,min_cost1

    return min(min_cost0, min_cost1)

print(minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
