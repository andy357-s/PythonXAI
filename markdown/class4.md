## **Python 知識筆記：學習編程的基礎**

### **1. 基本運算**

Python 可以用來做數學運算，像是加法、減法、乘法和除法。你可以這樣寫：

```python
a = 1
a += 1  # a = a + 1
print(a)  # 輸出: 2

a -= 1  # a = a - 1
print(a)  # 輸出: 1

a *= 2  # a = a * 2
print(a)  # 輸出: 2

a /= 2  # a = a / 2
print(a)  # 輸出: 1.0
```

**加法、減法、乘法、除法**是最常用的運算方式，而我們也可以用\*\*次方（`**`）\*\*來計算像是 2 的 3 次方（`2 ** 3`）。

### **2. 優先順序**

當我們寫很多運算式時，有一些運算會先進行，這叫做**運算優先順序**：

- 第一優先：小括號 `()`
- 第二優先：次方 `**`
- 第三優先：乘法、除法、取餘數 `%`
- 第四優先：加法、減法

這是 Python 先計算的順序。

### **3. 使用 `if` 和 `else` 來決定事情**

如果你想根據不同情況做不同的事情，可以使用**條件語句**（`if`）：

```python
num = 10
if num > 5:
    print("數字比5大")
else:
    print("數字比5小或等於5")
```

這段程式會先檢查 `num` 是否大於 5，如果是，就印出「數字比 5 大」，如果不是，就印出「數字比 5 小或等於 5」。

### **4. 用迴圈重複做事：`for` 和 `while`**

有時候我們想重複做某件事，可以使用**迴圈**。

#### **`for` 迴圈**：用來對著一個範圍或清單重複執行。

```python
for i in range(5):  # 從 0 開始，一直到 4
    print(i)
```

這段程式會印出：

```
0
1
2
3
4
```

#### **`while` 迴圈**：當條件符合時，一直做下去。

```python
i = 0
while i < 5:
    print(i)
    i += 1
```

這段程式也會印出：

```
0
1
2
3
4
```

### **5. 隨機數字**

有時候我們需要隨機數字，Python 提供了一些方法可以做到這一點。

```python
import random
random_number = random.randint(1, 6)  # 隨機產生 1 到 6 的數字
print(random_number)
```

這樣程式會隨機給你一個從 1 到 6 的數字。

### **6. 字典：存放資料的地方**

字典就像是一個有「名稱」和「數值」的資料庫。你可以用字典來存放對應的資料。

```python
# 創建一個字典
fruits = {"蘋果": 20, "香蕉": 30, "梨": 40}

# 查詢字典中的資料
print(fruits["蘋果"])  # 輸出: 20
```

你還可以**增加**、**修改**和**刪除**字典中的資料。

```python
# 修改資料
fruits["蘋果"] = 10  # 修改蘋果的數量
print(fruits)

# 增加資料
fruits["蓮霧"] = 35  # 加入新水果
print(fruits)

# 刪除資料
fruits.pop("香蕉")  # 刪除香蕉
print(fruits)
```

### **7. 互動式網頁：Streamlit**

Streamlit 是一個很棒的工具，可以讓你輕鬆建立自己的互動式網頁應用程式！例如，做一個**點餐系統**：

```python
import streamlit as st

# 初始化訂單
if "訂單" not in st.session_state:
    st.session_state.訂單 = []

# 輸入餐點
餐點 = st.text_input("請輸入餐點名稱:")

# 加入訂單
if st.button("加入餐點"):
    if 餐點:
        st.session_state.訂單.append(餐點)
        st.success(f"已加入: {餐點}")
    else:
        st.warning("請輸入餐點名稱")

# 顯示訂單
if len(st.session_state.訂單) > 0:
    for i, 餐點 in enumerate(st.session_state.訂單):
        st.write(f"{i + 1}. {餐點}")
else:
    st.write("目前沒有餐點，請加入餐點")
```

### **8. 使用 `session_state` 保持資料**

在 Streamlit 中，你可以使用 `session_state` 來記錄用戶的資料，這樣即使網頁重新整理，資料也不會消失。

```python
if "ans1" not in st.session_state:
    st.session_state.ans1 = 1

if st.button("按下去ans+1"):
    st.session_state.ans1 += 1

st.write(f"ans={st.session_state.ans1}")
```

### **9. 重新整理畫面**

有時候你想要重新載入網頁，可以使用 `st.rerun()` 來強制刷新畫面。

```python
if st.button("重新整理畫面"):
    st.rerun()
```

---

## **總結**

這些就是 Python 基本的知識！我們學到了如何進行數學運算、使用條件語句來判斷事情、用迴圈重複做事、隨機生成數字、存放資料的字典，以及如何利用 Streamlit 建立簡單的網頁應用。

編程是一項非常有趣的技能，學會了基本的 Python 語法，你可以創造出很多有趣的程式和應用！希望這些筆記能幫助你開始學習 Python，並在未來創作更多有趣的專案！🚀

---
