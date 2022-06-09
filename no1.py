##Iqbal Riyandi
##L200200226
##Quiz No 1

import re

username = input('Masukkan Username Anda : ')
cocok = re.findall(r'@+[a-z]+[0-9]+\w', username)
if cocok:
    print('PASS')
else:
    print('FAILED')
