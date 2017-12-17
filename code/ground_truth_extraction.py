fo = open('/home/adil/image_classification/test.txt', 'rw+')
with open('/home/adil/image_classification/sc5-2013-Mar-Apr-Test-20130412/ground_truth.txt') as f:
      lines = f.readlines()
      newlist = []
      for word in lines:
              word = word.split(";")
              newlist.extend(word)
      listOdd = newlist[1::2]
      listEven = newlist[::2]
      listOdd = [x.replace("\r\n","\n") for x in listOdd]
      line = fo.writelines(listOdd)
