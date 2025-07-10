# 算術指定運算子
a = 1
a += 1
print(a)
a -= 1
print(a)
a *= 2
print(a)
a /= 2
print(a)
a **= 2
print(a)
a %= 2
print(a)
a //= 2
print(a)

# 優先順序
# 1.()
# 2.**'次方
# 3.* / // % '乘法 除 取商 取於數
# 4.+ - '加減
# 字串運算
# not
# and
# or

# while迴圈
# while會搭配一個條件是來使用
# 條件式是True會執行，False會不執行
i = 0
while i < 5:
    print(i)
    i += 1
    for j in range(5):
        print(j)
    if i == 3:
        break
    i += 1


for i in range(5):
    print(i)
    if i == 3:
        break

import random  # 匯入random模組

# random.randange()設定範圍的方式和range一樣
print(random.randrange(7))
print(random.randrange(1, 7))
print(random.randrange(1, 7, 2))

random.seed(1)  # 設定隨機數產生器的種子
print(random.randint(1, 6))

ans = random.randint(1, 6)
while True:
    num = int(input(f"請輸入1~100的整數"))

    if num < 0 or num > 100:
        print("請輸入1~100的整數")
    elif num < ans:
        print("太小了")
    elif num > ans:
        print("太大了")
    else:
        print("正確")

# 建立字典:使用{},key和value之間用冒號
d = {"蘋果": 20, "香蕉": 30, "梨": 40}
print(d)

# 從字典中取得特定key對應的value
d = {"蘋果": 20, "香蕉": 30, "梨": 40}
print(d["蘋果"])

d = {"蘋果": 20, "香蕉": 30, "梨": 40}
print(d["蘋果"])
# print(d.梨子)會錯誤

d = {"蘋果": 20, "香蕉": 30, "梨": 40}


for key in d:
    print(key)
    print(d[key])

for k in d.keys():
    print(k)
    print(d[k])


for v in d.values():
    print(v)

# 方式4
for k, v in d.items():
    print(f"{k}:{v}")

# 修改內容
d = {"蘋果": 20, "香蕉": 30, "梨": 40}
d["蘋果"] = 10
print(d)
d["蓮霧"] = 35
print(d)

# 刪除內容
d = {"蘋果": 20, "香蕉": 30, "梨": 40}
d.pop("蘋果")
# 沒有這個東西就會錯誤
popitem = d.pop("蓮霧", "不存在資料")
print(d)
print(popitem)
