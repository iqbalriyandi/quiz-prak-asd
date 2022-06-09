##Iqbal Riyandi
##L200200226
##Quiz No 3

class pohonbiner(object):
    def __init__(self,data):
        self.data = data 
        self.kanan = None
        self.kiri = None

A = pohonbiner('9')
B = pohonbiner('3')
C = pohonbiner('8')
D = pohonbiner('1')
E = pohonbiner('5')
F = pohonbiner('2')
G = pohonbiner('7')

A.kiri = B ; A.kanan = C
B.kiri = D ; B.kanan = E
C.kiri = F ; C.kanan = G

def tampilLuarKanan(data):
    if data.kanan is not None:
        tampilLuarKanan(data.kanan)
    print(data.data)
def tampilLuarKiri(data):
    if data.kiri is not None:
        tampilLuarKiri(data.kiri)
    print(data.data)

tampilLuarKanan(A)
tampilLuarKiri(A)
