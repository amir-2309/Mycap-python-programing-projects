n=int(input("13":))
print("0 1 1 2 3 5 8 13 21 34 55 89 144":)
for n in range(0,n):
   print (fibnocci(13))


n_terms=int(input("13"))

n_1=0
n_2=1
count=0

if n_terms <= 0:
     print ("1")
elif n_terms == 1:
       print(n_1)
else:
       print("the fibonacci is:")
       while count < n_terms:
             print(n_1)
             nth = n_1+n_2
             n_1 = n_2
             n_2 = nth
             count += 1
             #count = count + 1


