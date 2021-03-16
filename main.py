import bisect,collections,copy,heapq,itertools,math,numpy,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr

def sosuu(i):
	if i == 2 or i == 3 or i == 5 or i == 7 or i == 11 or i == 13 or i == 17 or i == 19 or i == 23 or i == 29 or i == 31 or i == 37 or i == 41 or i == 43 or i == 47:
		return 1
	else:
		return 0

def main():
	n = I()
	x = LI()
	li = []
	ans = 1
	for i in x:
		ans *= i
	li2 = []
	tmp = factorization(ans)
	for j in range(len(tmp)):
		if tmp[j][0] in li2:
			continue
		else:
			li2.append(tmp[j][0])
	ans2 = 1
	for i in li2:
		ans2 *= i
	print(ans2)

if __name__ == "__main__":
	main()