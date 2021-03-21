import bisect,collections,copy,heapq,itertools,math,numpy,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())



def main():
	n = I()
	li = [LI() for _ in range(n)]
	ans = 0
	for i in range(n-1):
		for j in range(i+1,n):
			if -1 <= (li[i][1] - li[j][1]) / (li[i][0] - li[j][0]) <= 1:
				ans += 1
	print(ans)

if __name__ == "__main__":
	main()