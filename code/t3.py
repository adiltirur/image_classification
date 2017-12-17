fo = open('/home/adil/Image_classification/test/some3.txt', 'rw+')
lines = fo.readlines()

listOdd = [x.replace("\r\n","") for x in lines]
line = fo.writelines(listOdd)
[x for xs in listOdd for x in xs.split(',')]
Odd = listOdd[1::2] 
Even = listOdd[::2]
print len(xs)

#for i in range(1682):
    #if listOdd[i] == listEven[i]:
    #    mylist.append(1)
    #else:
    #    mylist.append(0)
