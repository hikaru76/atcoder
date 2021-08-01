import bisect,collections,copy,heapq,itertools,math,numpy,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

def main():
	n, m = LI()
	g = [[] for _ in range(n)]
	for i in range(m):
		a, b = LI()
		a -= 1
		b -= 1
		g[a].append(b)
		g[b].append(a)
	
	que=[0]
	dist=[None]*n
	cnt=[0]*n
	dist[0]=0
	cnt[0]=1

	for v in que:
		for vv in g[v]:
			if dist[vv] is None:
				dist[vv] = dist[v]+1
				que.append(vv)
				cnt[vv] = cnt[v]
			elif dist[vv] == dist[v]+1:
				cnt[vv] += cnt[v]
				cnt[vv] %= 10**9+7
	print(cnt[n-1])

if __name__ == "__main__":
	main()