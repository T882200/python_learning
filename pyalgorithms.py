#Bubble Sort
def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
       for i in range(passnum):
        if alist[i]>alist[i+1]:
            temp=alist[i]
            alist[i]=alist[i+1]
            alist[i+1]=temp

alist = [54,26,93,17,77,31,44,55,20]
bubbleSort(alist)
print(alist)



#Selection Sort
def selectionSort(alist):
   for fillslot in range(len(alist)-1,0,-1):
       positionOfMax=0
       for location in range(1,fillslot+1):
           if alist[location]>alist[positionOfMax]:
               positionOfMax = location

       temp = alist[fillslot]
       alist[fillslot] = alist[positionOfMax]
       alist[positionOfMax] = temp

alist = [54,26,93,17,77,31,44,55,20]
selectionSort(alist)
print(alist)




#Insertion Sort
def insertionSort(alist):
   for index in range(1,len(alist)):

     currentvalue = alist[index]
     position = index

     while position>0 and alist[position-1]>currentvalue:
         alist[position]=alist[position-1]
         position = position-1

     alist[position]=currentvalue

alist = [54,26,93,17,77,31,44,55,20]
insertionSort(alist)
print(alist)





