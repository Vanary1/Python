# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#輸入兩個姓名，用First Last做提示
print("Welcome to the Mashup Game!")
name1=input("Enter one full name(First Last):   ")
name2=input("Enter another full name(First Last):   ")
#切分姓與名
space=name1.find(" ")
name1_first=name1[0:space]
name1_last=name1[space+1:len(name1)]
space=name2.find(" ")
name2_first=name2[0:space]
name2_last=name2[space+1:len(name2)]
#切分成前後半部，分別用不同變數儲存
len_name1_first=len(name1_first)
len_name2_first=len(name2_first)
len_name1_last=len(name1_last)
len_name2_last=len(name2_last)
index_name1_first=int(len_name1_first/2)
index_name2_first=int(len_name2_first/2)
index_name1_last=int(len_name1_last/2)
index_name2_last=int(len_name2_last/2)
lefthalf_name1_first=name1_first[0:index_name1_first]
righthalf_name1_first=name1_first[index_name1_first:len_name1_first]
lefthalf_name2_first=name2_first[0:index_name2_first]
righthalf_name2_first=name2_first[index_name2_first:len_name2_first]
lefthalf_name1_last=name1_last[0:index_name1_last]
righthalf_name1_last=name1_last[index_name1_last:len_name1_last]
lefthalf_name2_last=name2_last[0:index_name2_last]
righthalf_name2_last=name2_last[index_name2_last:len_name2_last]
#重組姓名
newname1_first=lefthalf_name1_first.capitalize()+righthalf_name2_first.lower()
newname1_last=lefthalf_name1_last.capitalize()+righthalf_name2_last.lower()
newname2_first=lefthalf_name2_first.capitalize()+righthalf_name1_first.lower()
newname2_last=lefthalf_name2_last.capitalize()+righthalf_name1_last.lower()
print("\n"+"All done! Here are two possibilities, pick the one you like best!"+"\n")
#顯示兩種組合結果
print(newname1_first,newname1_last)
print(newname2_first,newname2_last)