import streamlit as st

with st.expander("class1的筆記"):
    st.write(
        '''

# 🐍 Python 程式筆記

## ✏️ 註解是什麼？

程式裡的「註解」就是給自己或別人看的說明文字，電腦不會執行它們喔！

- **單行註解**：只註解一行，用 `#` 開頭

  ```python
  # 這是註解，不會被執行
  ```

- **多行註解**：註解很多行，用三個雙引號 `"""` 包起來

  ```python
 \ "\"\"
  這裡有
  很多行
  註解
  \"\"\"
  ```

👉 小技巧：可以按 `Ctrl + ?` 快速註解或取消註解喔！

---

## 📦 變數是什麼？

變數就像是一個「裝東西的盒子」，你可以把數字、文字放進去！

```python
a = 10      # 把 10 放進 a
print(a)    # 顯示 a 裡的東西（是 10）

a = "apple" # 把字 "apple" 放進 a
print(a)    # 顯示 a（現在是 apple）
```

---

## ➕ 運算是什麼？

就像數學一樣，電腦也會加減乘除！

```python
print(1 + 1)  # 加法
print(2 - 1)  # 減法
print(3 * 2)  # 乘法
print(6 / 2)  # 除法
print(2 ** 3) # 次方（2 的 3 次方 = 8）
print(5 % 2)  # 取餘數（5 ÷ 2 剩下 1）
print(5 // 2) # 取整數（5 ÷ 2 = 2.5，只取 2）
```

---

## 🧠 比較特別的運算（可以跳過但也可以試試）

```python
print(1 & 1)  # AND 位元運算
print(1 | 1)  # OR 或運算
print(1 ^ 1)  # XOR 異或
print(1 << 1) # 左移
print(1 >> 1) # 右移
```

（這些比較進階，有興趣可以再問老師喔！）

---

## 🎯 運算的順序（就像數學公式的順序）

1. 括號 `()` 最先
2. 次方 `**`
3. 乘除 `* / // %`
4. 加減 `+ -`

---

## 💬 字串是什麼？

字串就是「文字」，用引號 `"` 包起來。

### 🔗 把字串加起來（串在一起）

```python
a = "Hi"
b = "Hello"
c = "HelloWorld"
d = "HelloWorld!"

print(a + b + c + d)  # 結果是：HiHelloHelloWorldHelloWorld!
```

你也可以把很多段文字接起來，就會變成一大串！

---

## 🧩 字串格式化（把變數放進文字裡）

這是讓我們可以把變數的內容加進文字裡：

```python
name = "apple"
age = 10
print(f"My name is {name} and I am {age} years old.")
```

📌 執行結果會是：
**My name is apple and I am 10 years old.**

---

## 🎉 小結

今天我們學到了：

✅ 註解怎麼寫
✅ 什麼是變數
✅ 怎麼加減乘除
✅ 文字（字串）怎麼用
✅ 怎麼把變數放進文字裡

---





'''
    )
with st.expander("class2的筆記"):
    st.write(
        """## 🐍 今天的 Python 筆記

嗨！今天我們學了一些很酷的 Python 程式語言，這些指令可以讓電腦幫我們做計算、判斷成績，還可以和使用者互動喔！

---

### 🧮 1. 計算字的長度：`len()`

```python
print(len("apple"))
```

👆 這行程式會告訴我們「apple」這個字有幾個字母。答案是 5。

---

### 📦 2. 看資料的種類：`type()`

```python
print(type(1))      # 整數
print(type(1.0))    # 小數
print(type(True))   # 布林值，True 表示「對的」
```

💡 程式裡的資料可以有不同的「型態」，像是整數、文字、對或錯（布林值）。

---

### 🔢 3. 輸入數字（用 Streamlit 工具）

```python
import streamlit as st
number = st.number_input("請輸入一個數字：", step=1, min_value=0, max_value=100)
st.write(f"你輸入的數字是:{number}")
```

📥 這段程式會讓你輸入一個 0 到 100 之間的整數。
📤 程式會幫你顯示輸入的數字。

---

### 🎓 4. 判斷成績 A\~F

```python
score = st.number_input("請輸入你的成績：", step=1, min_value=0, max_value=100)

if score >= 90:
    st.write("你的成績是A")
elif score >= 80:
    st.write("你的成績是B")
elif score >= 70:
    st.write("你的成績是C")
elif score >= 60:
    st.write("你的成績是D")
else:
    st.write("你的成績是F")
```

📝 這段程式會根據你輸入的成績，幫你打等級！

---

### 🔄 5. 變來變去：型態轉換

```python
print(int(1.0))     # 變成整數 → 1
print(float(1))     # 變成小數 → 1.0
print(bool(1))      # 變成布林值 → True
print(bool(0))      # 變成布林值 → False
```

💡 有時候我們需要把一種資料變成另一種型態，這叫做「型態轉換」。

---

### 🗣️ 6. 輸入文字：`input()`

```python
name = input("請輸入你的名字：")
print("嗨～" + name)
```

👦 使用者可以打東西進去，電腦就會記住你輸入的內容。

---

### 🧠 7. 用公式算圓面積

```python
pi = 3.14
r = float(input("輸入圓的半徑："))
Area = pi * r * r
print(f"圓的面積為{Area}")
```

🔵 這段程式會請你輸入一個圓的半徑，然後幫你算出圓的面積！

---

### ⚙️ 8. 運算的順序

```python
# 1. 括號 ()
# 2. 次方 **
# 3. 乘 / 除 // 餘數 %
# 4. 加 - 減
# 5. 比大小 == != < <= > >=
# 6. not
# 7. and
# 8. or
```

🧮 程式也有「先後順序」，像數學一樣，我們要照順序算才會對。

---

### 🔐 9. 密碼判斷遊戲

```python
password = input("請輸入密碼:")
if password == "123456":
    print("歡迎大便!!!!!")
elif password == "1234567":
    print("笨蛋來啦！")
else:
    print("密碼錯誤,帳號已被封鎖")
```


---

### 💡 小補充：`and`, `or`, `not`

* `or`：只要有一個條件是「對的」，整體就算「對」
* `and`：要全部條件都「對」，才算「對」
* `not`：把「對」變成「錯」，「錯」變成「對」
"""
    )
