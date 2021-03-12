import bisect,collections,copy,heapq,itertools,math,numpy,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())



def main():
	n = I()
	a, b = [], []
	for _ in range(n):
		c, d = LI()
		a.append(c)
		b.append(d)
	i = a.index(min(a))
	ans = 1000000000
	for i in range(n):
		for j in range(n):
			ans = min(ans, a[i]+b[j] if i == j else max(a[i], b[j]))
	print(ans)

if __name__ == "__main__":
	main()