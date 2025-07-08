print(len("apple"))  # len()是一個函式，可以計算字串長度
# type()可查看型態
print(type(1))
print(type(1.0))
print(type(True))
# 型態轉換
print(int(1.0))
print(float(1))
print(bool(1))
print(bool(0))
print(int)
# input()函示使用
print("輸入開始")
a = input("請輸入你的名字：")
print("輸入結束")
# input()輸入的都是字串
pi = 3.14
r = float(input("輸入圓的半徑："))
Area = pi * r * r
print(f"圓的面積為{Area}")
