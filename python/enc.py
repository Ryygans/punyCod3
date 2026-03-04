#!usr/bin/python

import time,os,sys

def encode_puny(domain):
        try:
                encoded_url = domain.encode('idna').decode('ascii')
                return encoded_url
        except Exception as err:
                return f"Error: {err}"
def decode_puny(domain):
        try:
                decoded_url = domain.encode('ascii').decode('idna')
                return decoded_url
        except Exception as err:
                return f"Error: {err}"
# the code

os.system('clear')
print('***'*20)
print('PunyCode Tools Python')
print('coded by: @zoxxtzy')
print('***'*20)
print("Choose one menu")
print("1) Encode ~> (Unicode to PunyCode)")
print("2) Decode ~> (PunyCode to Unicode)")
print("\n")
user_choice = int(input("Choose (1/2): "))

if user_choice == 1:
        time.sleep(3)
        domain = input("Enter your domain/word Unicode: ")
        print("Result: ", encode_puny(domain))
elif user_choice == 2:
        time.sleep(2)
        domain = input("Enter your domain/word PunyCode: ")
        print("Result: ", decode_puny(domain))
else:
        print("Are you blind dawg?")
