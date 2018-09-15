# https://www.hackerrank.com/contests/codeagon/challenges/is-it-t-shaped
t = int(input().strip())
def checksame3(cor):
    for i in range(len(cor)):
        c = 0
        for j in range(len(cor)):
            if (cor[j] == cor[i]):
                c+=1
        if (c == 3):
            return True, cor[i]
    return False, 1

def check_is_consecutive(l):
    a = sorted(l)
    if ((a[1] - a[0] == 1) and (a[2] - a[1] == 1) and (a[2] - a[0] == 2)):
        return True

for t_itr in range(t):
    p = []
    for _ in range(5):
        points = list ((map(int, input().strip().split())))
        p.append(points)
    x_cor = []
    y_cor = []
    for i in range(len(p)):
        x_cor.append(p[i][0])
        y_cor.append(p[i][1])

    x_bool , x_val = checksame3(x_cor)
    y_bool , y_val = checksame3(y_cor)
    x = []
    y = []
    if (x_bool and y_bool):
        for i in range(len(x_cor)):
            if (x_cor[i] == x_val):
                x.append(y_cor[i])
        for j in range(len(y_cor)):
            if (y_cor[j] == y_val):
                y.append(x_cor[j])
        if (check_is_consecutive(x) and check_is_consecutive(y)):
            print("Yes")
        else:
            print("No")
    else:
        print("No")
