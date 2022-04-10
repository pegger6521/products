#假設有一些整數裝在data清單裡, 你要一行一行的把這些數字寫到test.txt檔去, 請寫出這樣的程式碼!

data = [1, 3, 5, 7, 9]
with open('test.txt', 'w') as f:
    for d in data:
    	f.write(str(d) + '\n') 
 