import bisect,collections,copy,heapq,itertools,math,numpy,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())



def main():
	h,w,a,b = LI()
	pattern = 0
	if h == 1 or w == 1:
		pattern = h*w-1
	else:
		pattern = (h-1) * w + (w-1) * h
	

if __name__ == "__main__":
	main()