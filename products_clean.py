import os # operating system（作業系統模組）

# 讀取檔案
def read_file(filename):
    products = []
    with open(filename, 'r') as f:
        for line in f:
            if '項目,價格' in line:
                continue #繼續下一回
            name, price = line.strip().split(',')
            products.append([name, price])
        print(products)
    return products

# 讓使用者輸入
def user_input(products):
    while True:
         name = input('請輸入商品名稱: ')
         if name == 'q':
             break
         price = input('請輸入商品價格: ')
         products.append([name, price]) 
    print(products)
    return products

# 印出所有購買紀錄
def print_products(products):
    for p in products:
        print(p[0],'的價格是', p[1])

# 寫入檔案
def write_file(filename, products):
    with open(filename, 'w') as f:
        f.write('項目,價格\n')
        for p in products:
            f.write(p[0] + ',' + str(p[1]) + '\n')

#MAIN
def main():
    filename = 'products_clean.csv'
    if os.path.isfile(filename): # 檢查檔案在不在
        print('yeah! 找到檔案了!')
        products = read_file(filename)
    else:
        print('找不到檔案.....')
    products = user_input(products)
    print_products(products)
    write_file('products_clean.csv', products)

main() #這是程式的進入點