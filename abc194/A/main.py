import bisect,collections,copy,heapq,itertools,math,numpy,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())



def main():
	a, b = LI()
	if a + b >= 15 and b >= 8:
		print("1")
	elif a + b >= 10 and b >= 3:
		print("2")
	elif a + b >= 3:
		print("3")
	else:
		print("4")

if __name__ == "__main__":
	main()