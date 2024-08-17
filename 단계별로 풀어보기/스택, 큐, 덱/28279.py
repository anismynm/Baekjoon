from collections import deque
import sys
input = sys.stdin.readline

deck = deque([])
N = int(input())

for i in range(N):
    command = list(map(int, input().split()))
    match command[0]:
        case 1:
            deck.insert(0, command[1])
        case 2:
            deck.append(command[1])
        case 3:
            if (not(deck)):
                print(-1)
            else:
                print(deck.popleft())
        case 4:
            if (not(deck)):
                print(-1)
            else:
                print(deck.pop())
        case 5:
            print(len(deck))
        case 6:
            if (not(deck)):
                print(1)
            else:
                print(0)
        case 7:
            if (not(deck)):
                print(-1)
            else:
                print(deck[0])
        case 8:
            if (not(deck)):
                print(-1)
            else:
                print(deck[-1])