print("Please Enter your input to know it's length\nPlease enter done when you have completed")
while True:
  x = input('Enter your input: ')
  if x == 'done':
      break
  #print(len(x))
  sft = input('Enter the Encoding Key: ')
  y = range(len(x))
  z = list()
  key_length = len(sft)
  m = 0
  #lalp = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
#Encoder Base
  sbase = input('Enter your base: ')
  base_len = len(sbase)
  loop_multiple_1 = int(len(sbase)/key_length)
  loop_multiple_2 = len(sbase)%key_length
  for a in y:
      new = 0
#Converting string into list
      z.append(x[a])
      m = sbase.find(x[a])
      #new = m + int(sft)
#Shifting the value using encoding key
      #if new>len(sbase):
#          ind = new-len(sbase)
#          z[a] = sbase[ind]
#      else:
#          z[a] = sbase[new]
      #print(m)
  #print(z)
  out = ''
  for i in range(len(z)):
      out = out + z[i]
  print(out)
