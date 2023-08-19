컴퓨터 = int(input())
컴퓨터쌍 = int(input())

graph = [[] for i in range(컴퓨터 + 1)]
visited = [False] * (컴퓨터 + 1)

for i in range(컴퓨터쌍):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(node):
    visited[node] = True
    count = 1

    for i in graph[node]:
        if not visited[i]:
            count += dfs(i)

    return count

result = dfs(1) - 1
print(result)
