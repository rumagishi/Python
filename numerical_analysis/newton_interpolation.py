from sympy import *
x = symbols("x")
y = symbols("y")

bk_div_times = 0 #除算回数
bk_sub_times = 0 #減算回数
yk_mul_times = 0 #乗算回数
yk_add_times = 0 #加算回数

# 初期化
xk = [1.5, 1.6, 1.7]
fk = [0.40547, 0.47000, 0.53063]
number_of_points = len(xk)
n = number_of_points - 1
bk = [fk[0]] #0次のニュートン補間係数b0はf0なのでアペンドする
differences = fk
term = []

# 係数を求めるときに必要な差分を求めるメソッド
def take_a_difference(denomi1, denomi2, numer1, numer2):
    global bk_div_times
    global bk_sub_times
    bk_div_times += 1
    bk_sub_times += 2
    return (denomi1 - denomi2) / (numer1 - numer2)

# ニュートン補間係数を計算するメソッド
def calculate_coefficient(diff, h):
    diff_len = len(diff)
    differences_temp = []
    offset = number_of_points+1 - diff_len
    if diff_len < 1:
        return 0
    for i in range(0, diff_len-1):
        d = take_a_difference(diff[i+1], diff[i], xk[i+1+h], xk[i+1+h-offset])
        differences_temp.append(d)
        if i == 0:
            bk.append(d)
    diff = differences_temp
    calculate_coefficient(diff,h+1)

# m次までの補間多項式の項を求めるメソッド
def calculate_term(m):
    if m > n:
        return 0
    else:
        term.append("{0} + (x - {1})".format(bk[m],xk[m]))
        calculate_term(m+1)

# 項から補間多項式を求めるメソッド
def calculate_polynomial():
    global yk_mul_times
    global yk_add_times
    for i in range(1, len(term)):
        yk_mul_times += 1
        yk_add_times += 2
        term[0] = term[0] + " * (" + term[i]
    polynomial = term[0]
    for j in range(0, n):
        polynomial = polynomial + ")"
    eliminate = "+ (x - {0})".format(xk[-1])
    return polynomial.replace(eliminate,"")

if __name__ == "__main__":
    # ニュートン補間係数bkを求める
    calculate_coefficient(differences, 0)
    print("ニュートン補間係数は...")
    for i in range(0,len(bk)):
        print("b{0} = {1}".format(i,bk[i]))

    # ニュートン補間多項式を求める
    calculate_term(0)
    y_str = calculate_polynomial()
    y = sympify(y_str)
    print("よってニュートン補間多項式は...")
    print("f(x) = {0}".format(y_str))
    print("     = {0}".format(expand(y)))
    print("それぞれの関数値は...")
    print("f({0}) = {1}".format(xk[0],y.subs([(x,xk[0])])))
    print("f({0}) = {1}".format(xk[1],y.subs([(x,xk[1])])))
    print("f({0}) = {1}".format(xk[2],y.subs([(x,xk[2])])))
    print("f({0}) = {1}".format(1.65,y.subs([(x,1.65)])))
    print("")
    print("ニュートン補間係数の演算総数:除算は{0}回".format(bk_div_times))
    print("ニュートン補間係数の演算総数:減算は{0}回".format(bk_sub_times))
    print("ニュートン補間多項式の演算総数:乗算は{0}回".format(yk_mul_times))
    print("ニュートン補間多項式の演算総数:加算は{0}回".format(yk_add_times))
