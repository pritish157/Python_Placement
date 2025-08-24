#print[1,4,9,16,25,36,49,64,81,100] using while loop
# list_a=[1,4,9,16,25,36,49,64,81,100]
# index = 0
# while index<=9 :
#     list_items = (index+1)*(index+1)
#     list_a.append(list_items)
#     index+=1
# print (list_a)
# while index<=len(list_a)-1 :
#     print (list_a[index])
#     index += 1
tuple_a=(1,4,9,16,25,36,49,64,81,100)
index = 0
x = 56
while index in range(0,len(tuple_a)-1) :
    if x == tuple_a[index] :
        print ("x is in list_a")
        break
    index+=1
    
    
       
