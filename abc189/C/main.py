import bisect,collections,copy,heapq,itertools,math,numpy,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())



def main():
	n = I()
	a = LI()
	ans = 0
	for i in range(n):
		x = a[i]
		for j in range(i, n):
			x = min(x, a[j])
			ans=max(ans, x*(j-i+1))
	print(ans)

if __name__ == "__main__":
	main()