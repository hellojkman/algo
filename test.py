import sys
A, B = map(int,sys.stdin.readline().split())
C = list(map(int,sys.stdin.readline().split()))

def bigger(x):
    return x < B

D=list(filter(bigger,C))

print(' '.join(str(_) for _ in D))