## heapq Module
import heapq
import sys
input = sys.stdin.readline

T = int(input())

maxHeap = []
minHeap = []

for _ in range(T):
    k = int(input())
    visited = [False] * k

    for i in range(k):
        op, num = input().split()
        if op == 'I':
            heapq.heappush(maxHeap, (-int(num), i))
            heapq.heappush(minHeap, (int(num), i))
        elif num == '1':
            if maxHeap:
                visited[heapq.heappop(maxHeap)[1]] = True
        else:
            if minHeap:
                visited[heapq.heappop(minHeap)[1]] = True
        
        ## 각 힙의 최상위 노드만 동기화되면 상관 없음 ?
        while minHeap and visited[minHeap[0][1]]:
            heapq.heappop(minHeap)
        while maxHeap and visited[maxHeap[0][1]]:
            heapq.heappop(maxHeap)
    
    if len(minHeap) != 0:
        print(-maxHeap[0][0], minHeap[0][0])
    else:
        print("EMPTY")
    
    minHeap.clear()
    maxHeap.clear()
        
