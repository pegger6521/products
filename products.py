# 讓使用者重複輸入商品名稱
# 因為要重複的次數未定, 因此使用WHILE LOOP比FOR LOOP合適
# 二維清單的介紹

products = []
while True:
 	name = input('請輸入商品名稱: ')
 	if name == 'q':
 		break
 	price = input('請輸入商品價格: ')
 	person = input('請輸入付款人: ')
 	p = [name, price, person]
 	products.append(p) # 這裡可以把p直接寫進來變成->products.append([name,price])
print(products)

# 用for loop搞清楚每個東西是什麼

for product in products:
	print(product[0],'的價格是',product[1],',付款人是',product[2])	

# 自己玩玩記帳功能:

sum_ANAN = 0
sum_Peggy = 0
for product in products:
	product[1] = int(product[1])
	if product[2] == '安安':
		sum_ANAN = sum_ANAN + product[1]
	elif product[2] == '阿藍':
		sum_Peggy = sum_Peggy + product[1]
print('安安_總共先付了: ', sum_ANAN, '元')
print('阿藍_總共先付了: ', sum_Peggy, '元')

if sum_ANAN - sum_Peggy > 0:
	print('阿藍要給安安: ',sum_ANAN-sum_Peggy, '元')
elif sum_ANAN - sum_Peggy == 0:
    print('真巧,剛好一人付一半!哈哈!') 
else:
	print('安安要給阿藍: ',sum_Peggy-sum_ANAN, '元')

# 字串可以做+跟*
# 'abc' + '123' = 'abc123'
# 'abc' * 3 = 'abcabcabc'
# 寫入功能的練習
# 可以是txt檔案, 也可以是csv檔案

with open('products.txt', 'w') as f:
	for pp in products:
		pp[1] = str(pp[1])
		f.write(pp[0] + ',' + pp[1] + ',' + pp[2] + '\n')

with open('products.csv', 'w') as f:
	for pp in products:
		f.write(pp[0] + ',' + str(pp[1]) + ',' + pp[2] + '\n')
	f.write('安安總共先付了: ' + ',' + str(sum_ANAN) + ',' + '元' + '\n') 
	f.write('阿藍總共先付了: ' + ',' + str(sum_Peggy) + ',' + '元' + '\n') 
	if sum_ANAN - sum_Peggy > 0:
		f.write('阿藍要給安安: ' + ',' + str(sum_ANAN-sum_Peggy) + ',' + '元' + '\n') 
	elif sum_ANAN - sum_Peggy == 0:
		f.write('真巧,剛好一人付一半!哈哈!' + '\n')
	else:
		f.write('阿藍要給安安: ' + ',' + str(sum_Peggy-sum_ANAN) + ',' + '元' + '\n')
