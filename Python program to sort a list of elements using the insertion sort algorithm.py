def insertionSort(nlist):
   for i in range(1,len(nlist)):

     value = nlist[i]
     position = i

     while position>0 and nlist[position-1]>value:
         nlist[position]=nlist[position-1]
         position = position-1

     nlist[position]=value

nlist = [14,46,43,27,57,41,45,21,70]
insertionSort(nlist)
print(nlist)
