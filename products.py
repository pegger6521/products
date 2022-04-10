# 讓使用者重複輸入商品名稱
# 因為要重複的次數未定, 因此使用WHILE LOOP比FOR LOOP合適
# 二維清單的介紹

products = []
while True:
 	name = input('請輸入商品名稱: ')
 	if name == 'q':
 		break
 	price = input('請輸入商品價格: ')
 	p = [name, price]
 	products.append(p) # 這裡可以把p直接寫進來變成->products.append([name,price])
print(products)


