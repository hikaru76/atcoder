import bisect,collections,copy,heapq,itertools,math,numpy,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())



def main():
	n = I()
	li = [LI() for _ in range(n)]
	ans = li[0][1] if li[0][2] - li[0][0] > 0 else 1000000000
	for i in range(1, n):
		if (li[i][1] < ans and li[i][2] - li[i][0] > 0):
			ans = li[i][1]
	print(ans if ans != 1000000000 else -1)
	

if __name__ == "__main__":
	main()