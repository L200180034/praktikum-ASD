def jumlahHurufKonsonan(x):
    konsonan="BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz"
    jmlhuruf=len(x)
    jmlkonsonan=0
    for karakter in x:
        if karakter in konsonan:
            jmlkonsonan+=1
    return (jmlhuruf, jmlkonsonan)
k=jumlahHurufKonsonan("Surakarta")
print(k)


