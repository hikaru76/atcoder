import bisect,collections,copy,heapq,itertools,math,numpy,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())



def main():
	li = []
	for _ in range(4):
		li.append(S())
	if ("3B" in li) and ("HR" in li) and ("2B" in li) and ("H" in li):
		print("Yes")
	else:
		print("No")

if __name__ == "__main__":
	main()