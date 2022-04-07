print("Please Enter your input to know it's length\nPlease enter done when you have completed")
while True:
  x = input('Enter your input: ')
  if x == 'done':
      break
  #print(len(x))
  sft = input('Enter the Encoding Key: ')
  y = range(len(x))
  z = list()
  m = 0
  #lalp = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
#Encoder Base
  salp = 'abcdefghijklmnopqrstuvwxyz0123456789'
  for a in y:
      new = 0
#Converting string into list
      z.append(x[a])
      m = salp.find(x[a])
      new = m + int(sft)
#Shifting the value using encoding key
      if new>36:
          ind = new-36
          z[a] = salp[ind]
      else:
          z[a] = salp[new]
      #print(m)
  #print(z)
  out = ''
  for i in range(len(z)):
      out = out + z[i]
  print(out)
