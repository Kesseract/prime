import math
import sys
import time

print("素数チェックしたい数値を入力してください")

#入力
input = input()

# 開始
start_time = time.perf_counter()

#数値化
inputint = int(input)

#1以上sqrt(input)以下の素数を調べる。
i = 2

#素数を入れる配列
list = []

while True:
    flg = False
    for n in list:
        if i % n == 0:
            flg = True
    if flg == False:
        list.append(i)
    if i * i > inputint:
        break
    i = i + 1

for n in range(len(list)):
    if inputint%list[(len(list) - 1) - n] == 0:
        print(input+"は、"+str(list[(len(list) - 1) - n])+"×"+str(int(inputint/list[(len(list) - 1) - n]))+"です")
        # 修了
        end_time = time.perf_counter()
        # 経過時間を出力(秒)
        elapsed_time = end_time - start_time
        print(elapsed_time)
        sys.exit()

print(input+"は素数です")
# 修了
end_time = time.perf_counter()
# 経過時間を出力(秒)
elapsed_time = end_time - start_time
print(elapsed_time)
