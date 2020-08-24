def numbert(n):
   if n % 10 == 9:
       if n % 9 == 8:
           if n % 8 == 7:
               if n % 7 == 6:
                   if n % 6 == 5:
                       if n % 5 == 4:
                           if n % 4 ==3:
                               if n % 3 == 2:
                                   if n % 2 ==1:
                                       return True
                                   else:
                                       return False
                               else:
                                   return False
                           else:
                               return False
                       else:
                           return False
                   else:
                       return False
               else:
                   return False
           else:
               return False
       else:
           return False
   else:
       return False


a = 1
while numbert(a) is False:
    a += 1
    print('Current number is:', a)
print('Answer is:',a)
