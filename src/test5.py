import math
import sys
import time

print("素数チェックしたい数値を入力してください")

# 入力
input = input()

# 開始
start_time = time.perf_counter()

# 数値化(以下n)
inputint = int(input)

if inputint % 2 == 0:
    print(input+"は、"+str(int(inputint/2))+"×2です")
    sys.exit()

# 求めたい数値の平方根の小数点以下切り捨て
p = math.floor(math.sqrt(inputint))

# math.floor(math.sqrt(n))とinputintの差分をmと置く。
# math.floor(math.sqrt(inputint))*(y-x)-xy でも出せる。
# ただしx, yはそれぞれp, qに足した回数。(x,p)、(y,q)
m = inputint - p * p

if m == 1:
    print(str(i)+"は素数です")
    sys.exit()

# pと別で扱える変数を持っておく
q = p

count = 0
countp = 0
countq = 0

# p(n) = n - (floor(sqrt(n)))^2
#
# n = (p-x)(p+y)
# x > 0, y > 0
# x < y
# n > p^2 => m > 0
#
# 命題
# x(n) = ?
# y(n) = ?
#
# 177773
#
# p = 421
#
# m = n - p^2 = 532
#
# x = 32
# y = 36
#
# x = 32
# y = 32 -> 34 -> 36
#
# -xy = -1024(x=32, y=32)
#
# 421-32の倍数＝389*?
#
# ? = 4 => 1556
#
# m = p(y-x)-xy
#
# 532+1024 = (p-x)dy
# 1556 = 389の倍数
#
# xとかyは自然数 2刻み。
# y = x のとき、-xyしか変化しない -x^2、-y^2
#
# 偏微分すると、
# dx = p-y
# dy = p-x

# 素数判定
# n=p*qになるまで周る
while inputint != p * q:
    # n>p*qなら
    if inputint > p * q:
        # qに1足す。掛け算ではp分だけ足されている。
        count = count + 1
        countq = countq + 1
        q = q + 2
    # n<p*qなら
    elif inputint < p * q:
        # pから1引く。掛け算ではq分だけ引かれている。
        count = count + 1
        countp = countp + 1
        p = p - 2
    # 繰り返されてpが2になってもp*q!=nならそれはもう素数
    elif p <= 2 or p == 0:
        break


# 一応2以下は絶対素数だよと明言する
if p <= 2 or p == 0:
    print(count)
    print(countp)
    print(countq)
    print(m)
    print(input+"は素数です")
# ここに回答を載せる。目下の問題は素因数分解したやつが素数じゃないことがある。
else:
    print(count)
    print(countp)
    print(countq)
    print(m)
    print(input+"は、"+str(p)+"×"+str(q)+"です")

# 終了
end_time = time.perf_counter()

# 経過時間を出力(秒)
elapsed_time = end_time - start_time
print(elapsed_time)
