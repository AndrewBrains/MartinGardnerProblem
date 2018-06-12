def num_mul(x):
 result = 1
 for i in str(x):
  result*=int(i)
 return result

#there will be solves for values : index+10
a=[] 
n = int(input())
cn = 10

while True:
 tcn = cn
 i=0
 while tcn>=10:
  if (len(a)+9)>=tcn:
   i+=a[tcn-10]
   break
  tcn = num_mul(tcn)
  i+=1
 a.append(i)
 if n == a[len(a)-1]:
  print (len(a)-1+10)
  break
 cn+=1
