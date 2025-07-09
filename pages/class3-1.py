# 連續使用if跟使用if elif else的差別
# elif可以排除前面有判斷過的條件，所以縮短條件的複雜度。


for i in range(100000):
    print(i)
    print("hello")

for i in range(1, 10):
    print(i)

for i in range(1, 10, 2):
    print(i)
