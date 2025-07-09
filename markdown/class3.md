'''

### 🔁 `if`, `elif`, `else` 的差別是什麼？

`/`/`python
if 條件 1:
做事情 1
elif 條件 2:
做事情 2
else:
做其他的事情

````

* `if`：如果成立，就做這件事
* `elif`：只有前面不成立，才檢查這個
* `else`：其他都不成立，才執行這個

👉 `elif` 幫助我們**縮短判斷流程**，不用一直寫很多 `if`！

---

### 🔄 `for` 迴圈是什麼？

幫我們**重複做事情**！

```python
for i in range(1, 10):
    print(i)  # 印出 1~9
````

```python
for i in range(1, 10, 2):
    print(i)  # 印出 1、3、5、7、9（每次+2）
```

---

### 🎮 按鈕互動：用 Streamlit 做小遊戲！

```python
import streamlit as st

if st.button("按我一下"):
    st.balloons()  # 出現氣球動畫

if st.button("再按我一下"):
    st.snow()  # 出現下雪動畫
```

---

### 🔢 數字金字塔

```python
number = st.number_input("輸入一個數字：", step=1, min_value=1, max_value=9)
for i in range(1, number + 1):
    st.write(f"{i}" * i)
```

👆 輸入 5 會出現這樣的畫面：

```
1
22
333
4444
55555
```

---

### 📦 List（清單）是什麼？

```python
L = [1, 2, 3, "a", "b", "c"]
print(L[0])  # 印出第1個元素：1
```

---

### 🚶‍♂️ 走過 List 裡的每個元素

```python
for item in L:
    print(item)
```

或是用：

```python
for i in range(0, len(L), 2):
    print(L[i])  # 每隔一個印一次
```

---

### 🛠 修改 List 的內容

```python
L[0] = 100  # 把第一個數字改成 100
```

---

### 📌 List 加東西：`append()`

```python
L.append(99)
print(L)
```

---

### ❌ 刪掉 List 裡的東西

```python
L.remove(99)  # 把第一個出現的 99 移除
L.pop(0)      # 把第 0 個元素刪掉
```

---

### 🔃 排序 List：`sort()`

```python
L = [3, 1, 4, 2]
L.sort()  # 排完會變成 [1, 2, 3, 4]
```

---

### 💾 開檔案來讀資料

```python
with open("pages/class1-1.py", "r") as f:
    content = f.read()
    print(content)
```

> 這樣可以把電腦裡的檔案內容讀出來！

---

### 🔍 字串小技巧：檢查檔名

```python
filename = "class1.md"
print(filename.endswith(".md"))  # 看是不是 Markdown 檔
```

---

如果你想要我幫你做成簡單的「Python 學習卡」、「互動網頁遊戲」或「進度追蹤表」，我都可以幫你喔！

要加上圖片版教學或練習題也沒問題 😄
需要嗎？我可以現在幫你做！
'''
