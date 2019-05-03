# 刘敬宇 16521125
# 购物小票
database = {}
sum = 0
totalLen = int(input('请输入小票长度:'))
for i in range(4):
    items = input('商品名称:')
    price = float(input('商品价格:'))
    sum += price
    database[i] = {'items': items, 'price': price}
print('='*totalLen)
print('items'+' '*(totalLen-10)+'price')
a = len(database[i]['items'])
replace = '{items}' + ' ' * (totalLen - len(database[i]['items']) - 5) + '{price:5.2f}'
for i in range(4):
    replace = '{items}' + ' ' * (totalLen - len(database[i]['items']) - 5) + '{price:5.2f}'
    print(replace.format_map(database[i]))
print('='*totalLen)
print('total'+' '*(totalLen-11) + '{:.2f}'.format(sum))