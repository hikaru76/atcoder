import bisect,collections,copy,heapq,itertools,math,numpy,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())



def main():
	a,b,w=LI()
	big=int(math.floor(1000*w/a))
	small=int(math.ceil(1000*w/b))
	if small>big:
		print("UNSATISFIABLE")
	else:
		print(small, big)

if __name__ == "__main__":
	main()