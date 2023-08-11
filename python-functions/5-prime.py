def is_prime(number):
 if number <= 1:
    return False
 elif number > 1:
      for x in range(2,number):
       if number % x == 0:
         return (False)
       else:
          continue
 return True

