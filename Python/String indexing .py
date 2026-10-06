creditcard_num = '1234-5678-9012-3456'

#print(creditcard_num[0])
#print(creditcard_num[0:4])
#print(creditcard_num[:4])
#print(creditcard_num[4:8])
#print(creditcard_num[4:])
#print(creditcard_num[-1])
#print(creditcard_num[-4])
#print(creditcard_num[:2])
#print(creditcard_num[:3])


#last_digits = creditcard_num[-4:]
#print(f'XXXX-XXXX-XXXX-{last_digits}')


last_digits = creditcard_num[::-1]
print(last_digits)