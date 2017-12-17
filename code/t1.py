bad_words = ['Snapshot Barca Parziale']


with open('/home/adil/tensorflow-for-poets-2/sc5-2013-Mar-Apr-Test-20130412/test1.txt') as oldfile, open('/home/adil/tensorflow-for-poets-2/sc5-2013-Mar-Apr-Test-20130412/test2.txt', 'w') as newfile:
    for line in oldfile:
        if not any(bad_word in line for bad_word in bad_words):
            newfile.write(line)
