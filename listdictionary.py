#NO.1
from typing import ValuesView


numbers=[1,2,3,4,5,6,7,8,9,10]
print('sum=',(sum(numbers)))

#NO.2
colours=["orange","purple","red","green","blue","pink"]
print(colours[1:4])

#NO.3
dict={"x":[11,12,13.14,15,16,17,18,19,20],"y":[21,22,23,24,25,26,27,28,29,30],"z":[31,32,33,34,35,36,37,38,39,40]}
for numbers in dict.values():
   print(numbers[4])




#NO.4
invetory={'gold':500,'pouch':['flint','twine','gemstone'],'backpack'
:['xylophone','dagger','bedroll','bread loaf']}
invetory.update({'pocket':['seashell','strange berry','lint']})
print(invetory)
invent=(invetory['backpack'])
invent.sort()
print(invent)
invent.remove('dagger')
print(invent)
invent_1=(invetory['gold']+50)
print(invent_1)




#NO.5a
prices={}
prices.update({"banana":4,"apples":2,"orange":1.5,"pear":3})
print(prices)
stock={"banana":1,"apples":3,"orange":2,"pear":1}
#print(stock)

#NO.5b
for fruits in prices:
   print(fruits)
   print("price:%s"%prices[fruits])
   print("stock:%s"%stock[fruits])

#NO.5c
Total= 0
for  key in prices:
     Ts=(prices[key]*stock[key])
     print(Ts)
     Total=Total+Ts
    # print("sum=",Total)   
print("Total=",Total)
