
import urllib.request
import csv
import codecs

url = "https://gist.githubusercontent.com/netj/8836201/raw/6f9306ad21398ea43cba4f7d537619d0e07d5ae3/iris.csv"




class Extendelist:
    def __init__(self,list1):
        self.list1=list1
        # self.list2=list2


    def equall(self,list1,list2):
        if len(list1)>len(list2):
            print("list1 is bigger than list2")
        if(len(list1)<len(list2)):
            print("list2 is bigger than list1")
        if(len(list1)==len(list2)):
            print("list2 is equal with list1")

        @staticmethod
        def NextVal(list1):
            for i in list1:
                yield  int(i)

            my_generator = NextVal(row)
            print(my_generator)
            my_generator.__next__()






class TypeList(Extendelist):
    def __init__(self, list1):
            super().__init__(list1)

    def true(self, list1, list2):
        if len(list1)==len(list2):
            a=len(list1)
            b=len(list2)
            if list1[int(a)-1]==list1[int(b)-1]:
                print("True")



def main():


    # list1=input("enter your first list: \n")
    # list2=input("enter your second list: \n")
    # lst=Extendelist(list1,list2)
    # lst1=TypeList(list1,list2)
    #
    # print(lst.equall(list1,list2))
    # print(lst1.true(list1, list2))
    stream = urllib.request.urlopen(url)
    csv_file = csv.reader(codecs.iterdecode(stream, 'utf-8'))




    for row in csv_file:
            # row = lines[m].split(",")

            print(row)
            lst=Extendelist(row)
            lst1=TypeList(row)

            print(lst.equall(row[1],row[2]))
            print(lst1.true(row[1],row[2]))


main()
