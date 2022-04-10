import os # operating system（作業系統模組）

# 讀取檔案
products = []
if os.path.isfile('products_clean.csv'): # 檢查檔案在不在
	print('yeah! 找到檔案了!')
	with open('products_clean.csv', 'r') as f:
		for line in f:
			if '項目,價格' in line:
			    continue #繼續下一回
			name, price = line.strip().split(',')
			products.append([name, price])
	print(products)
else:
	print('找不到檔案.....')

# 讓使用者輸入
while True:
 	name = input('請輸入商品名稱: ')
 	if name == 'q':
 		break
 	price = input('請輸入商品價格: ')
 	products.append([name, price]) 
print(products)

# 印出所有購買紀錄
for p in products:
	print(p[0],'的價格是',p[1])	

# 寫入檔案
with open('products_clean.csv', 'w') as f:
	f.write('項目,價格\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')
	
