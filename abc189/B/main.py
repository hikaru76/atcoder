import bisect,collections,copy,heapq,itertools,math,numpy,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())



def main():
	n,x = LI()
	li = [LI() for _ in range(n)]
	total = 0
	for i in range(n):
		total += li[i][0] * li[i][1] * 0.01
		if total > x:
			print(i+1)
			exit()
	print(-1)

if __name__ == "__main__":
	main()