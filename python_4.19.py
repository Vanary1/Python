# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

"""題目
讓使用者一次同時在"同一行"一起輸入中文名和姓，例如周 天成，中間會空一格，名字限定不可有空格。一共輸入三個人名。
然後將人的姓和名，存成tuple，將三個人的姓名存成一個tuple。在用print顯示整個tuple在螢幕上。
例如你輸入的人名是 周 天成，就存成tuple ("周", "天成")；然後三個人名會存成(("周", "天成"), ("戴", "資穎"), ("王", "子維"))
"""

result=()
name=input("請輸入中文姓名：")
space_index=name.find(" ")
last=name[0:space_index]
first=name[space_index+1::]
result=result+(last, first)
print(result)