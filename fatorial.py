def FirstFactorial(num):
  x = 1
  for i in range(num):
    x = x*(i+1)
  return x

# keep this function call here
print(FirstFactorial(int(input())))