input:str="geeksforgeeks"
output:
e-4
s-2
k-2
g-2
r-1
o-1
f-1

def printChar(arr,len):
      #to store the
      occ={ }
      for i in range(len):
           
           if(arr[i] in occ):
                  occ[arr[i]]=occ[arr[i]]+1

           else:
                  occ[arr[i]]=1

      #Map's size
      size = len(occ0

     #while there are elements in the map
     while (size>0):
    
            #finding the maximum value
           #from the map
           currentmax=0
           arg_max=0
           for key,value in occ.items():

                if (value>currentmax or (value == currentmax and key > arg_max
                   arg_max=key
                   currentMax=value
         #Print the character
         # alongwith its frequency
         print(f"{currentmax}")

         #Delete the maximum value
        occ.pop(arg_max)
        size -= 1

#Driver code
Str = "geeksforgeeks"
Len = len(Str)

printChar(list(Str),Len)


 