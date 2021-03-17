import bisect,collections,copy,heapq,itertools,math,numpy,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())



def main():
	n, s, d = LI()
	dmg = 0
	for _ in range(n):
		x, y = LI()
		if not (x >= s or y <= d):
			dmg = 1
	if dmg:
		print("Yes")
	else:
		print("No")


if __name__ == "__main__":
	main()