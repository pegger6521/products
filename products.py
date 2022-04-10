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
for A in products:
	A[1] = int(A[1])
	if A[2] == '安安':
		sum_ANAN = sum_ANAN + A[1]
	elif A[2] == '阿藍':
		sum_Peggy = sum_Peggy + A[1]
print('安安_總共先付了: ', sum_ANAN, '元')
print('阿藍_總共先付了: ', sum_Peggy, '元')

if sum_ANAN - sum_Peggy > 0:
	print('阿藍要給安安: ',sum_ANAN-sum_Peggy, '元')
elif sum_ANAN - sum_Peggy == 0:
    print('真巧,剛好一人付一半!哈哈!') 
else:
	print('安安要給阿藍: ',sum_Peggy-sum_ANAN, '元')

	