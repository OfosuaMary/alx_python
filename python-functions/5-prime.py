def is_prime(number):
 if number > 1:
      for x in range(2,9):
       if number % x == 0:
         return (False)
       else:
          continue
 return True
