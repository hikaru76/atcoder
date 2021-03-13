import bisect,collections,copy,heapq,itertools,math,numpy,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())



def main():
	n = I()
	ans = 0
	if n < 1000:
		print(0)
	elif n < 1000000:
		print(n-1000+1)
	elif n < 1000000000:
		print((n-1000000+1)*2+999999-1000+1)
	elif n < 1000000000000:
		print((n-1000000000+1)*3+(999999999-1000000+1)*2+999999-1000+1)
	elif n < 1000000000000000:
		print((n-1000000000000+1)*4+(999999999999-1000000000+1)*3+(999999999-1000000+1)*2+999999-1000+1)
	else:
		print(5+(999999999999999-1000000000000+1)*4+(999999999999-1000000000+1)*3+(999999999-1000000+1)*2+999999-1000+1)


if __name__ == "__main__":
	main()