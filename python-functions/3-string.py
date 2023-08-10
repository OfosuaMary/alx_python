def reverse_string(string):
   b = len(string)+1
   c=''
   for x in range(1,b):
    c = c+ string[-x]
   return(c)