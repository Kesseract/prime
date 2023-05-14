import math
import sys
import time
import openpyxl

print("1から順にいくつ素数チェックしたいかを入力してください")

# 入力
input = input()

# 開始
start_time = time.perf_counter()

# 数値化(以下n)
inputint = int(input)

for i in range(inputint):

    if i % 2 == 0:
        print(str(i)+"は、"+str(int(i/2))+"×2です")
        continue

    # 求めたい数値の平方根の小数点以下切り捨て
    p = math.floor(math.sqrt(i))

    # math.floor(math.sqrt(n))とinputintの差分をmと置く。
    # math.floor(math.sqrt(i))*(y-x)-xy でも出せる。
    # ただしx, yはそれぞれp, qに足した回数。(x,p)、(y,q)
    m = i - p * p

    if m == 1:
        print(str(i)+"は素数です")
        continue
    # pと別で扱える変数を持っておく
    q = p

    count = 0
    countp = 0
    countq = 0

    # 素数判定
    # n=p*qになるまで周る
    while i != p * q:
        # n>p*qなら
        if i > p * q:
            # qに1足す。掛け算ではp分だけ足されている。
            count = count + 1
            countq = countq + 1
            q = q + 2
        # n<p*qなら
        elif i < p * q:
            # pから1引く。掛け算ではq分だけ引かれている。
            count = count + 1
            countp = countp + 1
            p = p - 2
        # 繰り返されてpが2になってもp*q!=nならそれはもう素数
        if p <= 2 or p == 0:
            break


    # 一応2以下は絶対素数だよと明言する
    if p <= 2 or p == 0:
        print(count)
        print(countp)
        print(countq)
        print(m)
        print(str(i)+"は素数です")
    # ここに回答を載せる。目下の問題は素因数分解したやつが素数じゃないことがある。
    else:
        print(count)
        print(countp)
        print(countq)
        print(m)
        print(str(i)+"は、"+str(p)+"×"+str(q)+"です")


# 終了
end_time = time.perf_counter()

# 経過時間を出力(秒)
elapsed_time = end_time - start_time
print(elapsed_time)
