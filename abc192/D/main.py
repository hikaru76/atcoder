import bisect,collections,copy,heapq,itertools,math,numpy,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

def base10int(value, base):
    if (int(value / base)):
        return base10int(int(value / base), base) + str(value % base)
    return str(value % base)

def main():
	x = S()
	m = S()
	for i in range(2, 10):
		print(base10int(int(x), i))

sys.setrecursionlimit(10000)
if __name__ == "__main__":
	main()