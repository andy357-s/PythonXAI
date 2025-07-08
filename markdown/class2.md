以下是根據你上課學到的內容，整理出來的一份**給國小學生看的 Python 筆記**，用簡單的話讓小朋友也能看懂：

---

## 🐍 今天的 Python 筆記

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

🤣 輸入不同的密碼，會看到不同的結果喔！（這段只是好玩！）

---

### 💡 小補充：`and`, `or`, `not`

- `or`：只要有一個條件是「對的」，整體就算「對」
- `and`：要全部條件都「對」，才算「對」
- `not`：把「對」變成「錯」，「錯」變成「對」

---
