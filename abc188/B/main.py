import bisect,collections,copy,heapq,itertools,math,numpy,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())



def main():
	n = I()
	a = LI()
	b = LI()
	ans = 0
	for x,y in zip(a,b):
		ans += x*y
	if ans == 0:
		print('Yes')
	else:
		print('No')

if __name__ == "__main__":
	main()