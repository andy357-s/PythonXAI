# 優先順序
# 1.()括號
# 2.**'次方
# 3.* / // % '乘法 除 取商 取於數
# 4.+ - '加減
# 5.(1==1)
# 6.(1!=1)
# 7.(1<1)
# 8.(1<=1)
# 9.(1>1)
# 10.(1>=1)
# 11.not
# 12.and
# 13.or
# or運算子,只要有一個條件為True,就是True。
# and運算子,只要有一個條件為False,就是False。
# not運算子,只要條件為True,就是False。
password = input("請輸入密碼:")
if password == "123456":
    print("歡迎大便!!!!!")
elif password == "1234567":
    print("笨蛋來啦！")
else:
    print("密碼錯誤,帳號已被封鎖")
