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
	tmp = 0
	for i in a:
		ans += i * i * (n - 1)
	for i in range(n - 1):
		tmp = tmp + a[n - i - 1]
		ans -= 2 * tmp * a[n - i - 2]
	print(ans)

if __name__ == "__main__":
	main()