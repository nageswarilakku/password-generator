#password generator
import random
user_name=input("enter user_name:")
print(user_name)
lower="abcdefghijklmnopqrstuvxyz"
upper="ABCDEFGHIJKLMNOPQRSTUVXYZ"
numbers="0123456789"
symbols="{}?@#$%^&*()-+"
all=lower+upper+numbers+symbols
length=16
password="".join(random.sample(all,length))
print(password)