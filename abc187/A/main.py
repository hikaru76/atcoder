import bisect,collections,copy,heapq,itertools,math,numpy,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())



def main():
	a, b = LS()
	ansa = 0
	ansb = 0
	for i, j in zip(a,b):
		ansa += int(i)
		ansb += int(j)
	print(max(ansa, ansb))

if __name__ == "__main__":
	main()