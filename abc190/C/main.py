import bisect,collections,copy,heapq,itertools,math,numpy,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())



def main():
	n, m = LI()
	dishlis = [0] * n
	li = [LI() for _ in range(m)]
	k = I()
	lis = [LI() for _ in range(k)]
	ans = 0
	for balls in itertools.product(*lis):
		balls = set(balls)
		cnt = sum(A in balls and B in balls for A, B in li)
		if ans < cnt:
			ans = cnt
	print(ans)

if __name__ == "__main__":
	main()