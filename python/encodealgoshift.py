print("Please Enter your input to know it's length\nPlease enter done when you have completed")
while True:
  x = input('Enter your input: ')
  if x == 'done':
      break
  #print(len(x))
  sft = input('Enter the shifting number: ')
  y = range(len(x))
  z = list()
  m = 0
  #lalp = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
  salp = 'abcdefghijklmnopqrstuvwxyz'
  for a in y:
      new = 0
      z.append(x[a])
      m = salp.find(x[a])
      new = m + int(sft)
      if new>26:
          ind = new-26
          z[a] = salp[ind]
      else:
          z[a] = salp[new]
      #print(m)
  #print(z)
  out = ''
  for i in range(len(z)):
      out = out + z[i]
  print(out)
