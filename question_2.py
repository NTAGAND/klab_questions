item = [ {'name': 'Bike', 'price':100}, 
{'name': 'TV', 'price':200},
{'name': 'Album', 'price':10}, 
{'name': 'Book', 'price':5}, 
{'name': 'Phone', 'price':500}, 
{'name': 'Computer', 'price':1000} 
]

print('\n'+"Q1 . Filter and show the product that will bebought when you don't have much money I mean Cheap one")

max=item[0]['price']
for n in range(0,len(item)):
  r=item[n]['price']
  if r <=max:
    max=item[n]['price']
    product=item[n]
print(product)

print('\n'+'Q2.Filter and show the product that will be expensive in the array')


max=item[0]['price']
for n in range(0,len(item)):
  r=item[n]['price']
  if r >=max:
    max=item[n]['price']
    product=item[n]
print(product)

print('\n'+ 'Q3 . Calculate the full price of all product combined')
  
total=0 
for n in range(0,len(item)):
  total=total+item[n]['price']
print(total)

print('4 . Calculate the full price of all product combined and remove product that are under the 10 dollar')

total=0 
for n in range(0,len(item)):
    if item[n]['price']<10:
        item[n]['price']=0
    total=total+item[n]['price']
  
print(total)