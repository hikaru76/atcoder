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
	j = b.index(min(b))

	if i == j:
		c, d = a[i], b[i]
		del a[i]
		del b[i]
		ans = min(c + d, max(min(a), d), max(c, min(b)))
	else:
		ans = max(a[i], b[i])
	print(ans)

if __name__ == "__main__":
	main()