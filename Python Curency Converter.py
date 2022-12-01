# Python Curency Converter 

from cgitb import reset 
from unittest import result 
from forex_python.converter import CurrencyRates 
curr = CurrencyRates()

amount = float(input("Enter Amount:"))
from_c = input("From Currency:").upper()
to_c = input("To Currency:").upper()


result = curr.convert(from_c, to_c, amount)

print(f"{amount} {from_c} = {result} {to_c}")

# THIS LIBARY DOES NOT SUPPOURT ALL CURRENCY RATES 