def prime_checker(number):
  count=0
  if number % 1 ==0 and number%number == 0:
    for i in range(2,number-1):
      if number % i == 0:
        count+=1
        print(f"divisible by {i}")
    if count > 0:
      print(f"{number} is not a prime number")
    else:
      print(f"{number} is a prime number")  
        

n = int(input("Check this number: "))
prime_checker(number=n)


Sample outputs:
For composite:
Check this number: 189
divisible by 3
divisible by 7
divisible by 9
divisible by 21
divisible by 27
divisible by 63
189 is not a prime number


For prime:
Check this number: 211
211 is a prime number
