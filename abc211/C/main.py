import bisect,collections,copy,heapq,itertools,math,numpy,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())



def main():
	s = S()
	n = len(s)
	dp = numpy.zeros((n+1, 9))
	for i in range(n+1):
		dp[i][0] = 1
	mod = 10**9+7
	t = "chokudai"
	for i in range(n):
		for j in range(8):
			if s[i] != t[j]:
				dp[i+1][j+1] = dp[i][j+1]
			else:
				dp[i+1][j+1] = (dp[i][j+1] + dp[i][j]) % mod
	print(int(dp[n][8]))


if __name__ == "__main__":
	main()