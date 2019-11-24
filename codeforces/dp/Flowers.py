# https://codeforces.com/problemset/problem/474/D
#
# f(n) = f(n-k) + f(n-1)
#

MOD = 1000000007
SIZE = 100010
dp = [-1 for i in range(SIZE)]


def flowers(n, k):
    if n == 0:
        return 1
    if dp[n] != -1:
        return dp[n]
    temp = 0
    if n >= k:
        temp = (flowers(n-k, k) % MOD)
    temp += (flowers(n-1, k) % MOD)
    temp %= MOD
    dp[n] = temp
    return dp[n]


def flowers_runner():
    dp[0] = 0
    line = input()
    sn, sk = line.split(' ')
    n = int(sn)
    k = int(sk)
    for i in range(SIZE-1):
        flowers(i+1, k)
    for i in range(SIZE-1):
        dp[i+1] += dp[i]
        dp[i+1] %= MOD
    while n != 0:
        line = input()
        sa, sb = line.split(' ')
        a = int(sa)
        b = int(sb)
        print((MOD + dp[b] - dp[a-1]) % MOD)
        n -= 1


flowers_runner()
