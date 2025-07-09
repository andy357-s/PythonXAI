print([])  # 這是一個空的list
print([1, 2, 3])  # 這是一個有三個元素的list
print([1, 2, 3, "a,b,c"])  # 這是一個有六個元素的list
print([1, 2, 3, ["a,b,c"]])  # 這是一個有四個元素的list

L = [1, 2, 3, "a", "b", "c"]
print(L[0])
print(L[1])
print(L[2])
print(L[3])

# list的走訪元素
L = [1, 2, 3, "a", "b", "c"]
for i in range(0, len(L), 2):
    print(L[i])
for i in L:
    print(i)

# list 修改元素
# 可透過index來修改list中的元素
L = [1, 2, 3, "a", "b", "c"]
L[0] = 2  # 把index 0的元素改成2
print(L)

# call by value
a = 1
b = a  # 把a跟b指向同一記憶體位置，所以改變b的職，a也會改變
b = 2
print(a, b)

# call by reference
a = [1, 2, 3]
b = a
b[0] = 2
print(a, b)

a = [1, 2, 3]
b = a
b[0] = 2
print(a, b)

# list的append,也就是在list的最後面加上新的元素
L = [
    1,
    2,
    3,
]
L.append(4)
print(L)

L = [a, b, c, d, a]
L.remove(a)
print(L)

for i in L:
    if i == a:
        L.remove(i)

L = [a, b, c, d, a]
L.pop(0)
L.pop(0)
print(L)

# sort:排序
L = [1, 3, 2, 4, 5]
L.sort()
print(L)

# open:打開檔案
# read:讀取檔案
# write:寫入檔案
# append:在檔案最後面加上新的元素

# 開啟檔案
# 絕對路徑:C:\Users\user\Desktop\PythonXAI\pages\class1-1.py
# 相對路徑:pages\class1-1.py
with open("pages\class1-1.py", "r") as f:
    content = f.read()
    print(content)

# 字串小工具:用來檢查字串是否包含某個字
filename = "class1.md"
print(filename.endswith(".md"))
