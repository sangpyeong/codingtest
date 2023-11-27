from collections import defaultdict


def init(links):
    edge_dict = defaultdict(list)

    for a, b in links:
        edge_dict[a].append(b)

    return edge_dict


def dfs(node, edge_dict, dp):
    if not edge_dict[node]:
        return

    min_val, min_diff = 0, float('inf')
    for leaf in edge_dict[node]:
        dfs(leaf, edge_dict, dp)
        min_val += min(dp[leaf])
        min_diff = min(min_diff, dp[leaf][1] - dp[leaf][0])
    dp[node][0] += min_val + min_diff if min_diff >= 0 else min_val
    dp[node][1] += min_val


def solution(sales, links):
    dp = [[0, 0]] + [[0, sale] for sale in sales]

    edge_dict = init(links)
    dfs(1, edge_dict, dp)
    return min(dp[1])
