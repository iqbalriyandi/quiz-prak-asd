##Iqbal Riyandi
##L200200226
##Quiz Nomor 2

import re
f = open("quiz2.txt")
teks = f.read()
f.close()
p = r'[\w.-]+@[\w.-]+'
cocok = re.findall(p, teks)
print(cocok[0])
