# 5 5
# 1 4 7 11 15
# 2 5 8 12 19
# 3 6 9 16 22
# 10 13 14 17 24
# 18 21 23 26 30
# 5

def main():
    n,m = map(int, input().split())
    matrix = [list(map(int,input().split()) for _ in range(m))]
