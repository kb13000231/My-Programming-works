def is_even(p):
  temp=0
  parity = 1
  for i in range(len(p)-1):
        for j in range(i+1, len(p)):
         if p[i]>p[j]:
           temp=p[i]
           p[i]=p[j]
           p[j]=temp
           parity=parity+1
  return parity%2==0
p = [6, 2, 1, 0, 4, 5, 3]
print(is_even(p,1))
