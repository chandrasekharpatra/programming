
MOD = 1000000007
dp = [[-1 for i in range(2)] for j in range(101)]


def k_tree(n, k, d, least_d_selected):
    if least_d_selected:
        selected_index = 1
    else:
        selected_index = 0
    if n < 0:
        return 0
    if n == 0 and least_d_selected:
        return 1
    if n == 0 and not least_d_selected:
        return 0
    temp = 0
    if dp[n][selected_index] != -1:
        return dp[n][selected_index]
    for i in range(k):
        if not least_d_selected and (i+1) >= d:
            temp += k_tree(n-(i+1), k, d, True)
            temp %= MOD
        else:
            temp += k_tree(n-(i+1), k, d, least_d_selected)
            temp %= MOD
    dp[n][selected_index] = temp
    return dp[n][selected_index]


def k_tree_runner():
    line = input()
    sn, sk, sd = line.split(' ')
    n = int(sn)
    k = int(sk)
    d = int(sd)
    print(k_tree(n, k, d, False))


k_tree_runner()
