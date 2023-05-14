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

flg = False
for i in range(2, int(inputint**0.5)+1):
    if inputint % i == 0:
        break
else:
    flg = True

if flg == True:
    print(input+"は、素数ではないです")
else:
    print(input+"は、素数です")

# 終了
end_time = time.perf_counter()

# 経過時間を出力(秒)
elapsed_time = end_time - start_time
print(elapsed_time)
