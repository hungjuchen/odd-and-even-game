from microbit import *
import random

display.scroll("After you start, you will see a random number. Press A if you think it’s odd, or B if you think’s even. Then it will indicate if you are right or wrong.")

random_num = random.randint(1, 9)
display.show(str(random_num))

is_odd = random_num % 2


while True:
   if button_a.is_pressed():
       if is_odd:
           display.show(Image.YES)
       else:
           display.show(Image.NO)
       sleep(5000)
       random_num = random.randint(1, 9)
       display.show(str(random_num))
       is_odd = random_num % 2
   elif button_b.is_pressed():
       if is_odd:
           display.show(Image.NO)
       else:
           display.show(Image.YES)
       sleep(5000)
       random_num = random.randint(1, 9)
       display.show(str(random_num))
       is_odd = random_num % 2