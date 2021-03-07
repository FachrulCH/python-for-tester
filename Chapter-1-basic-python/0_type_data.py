print(" === Boolean === ")
x = True
y = False

print(x or y) # if x is False then y otherwise x
print(x and y) # if x is False then x otherwise y
print(not x) # if x is True then False, otherwise True

print(" === Numbers === ")
print("- Integer")
a = 10
b = 123456789
print(a * b)
print("- Float")
phi = 3.14
r = 21
print("Luas lingkaran: ", 2 * phi * r)

print(" === Strings === ")
akun = 'Tester Gadungan'
pesan = "Don't forget to Subscribe:"
multiline = """My website:
https://fachrul.id
there're plenty of automations test content there
"""
print("Hello "+akun+" viewer")
print(pesan, akun)
print(f"Thank you {akun} viewer")
print(multiline)

print(" === List === ")
print("a list is more like an array in other languages")
keranjang = ['telur', 'mie', 'cabe']
print(keranjang[0])   # first in list
print(keranjang[-1])  # latest in list
keranjang.append('pakcoy')
keranjang.remove('cabe')
print(len(keranjang), keranjang)

print(" === Tuples === ")
print("A tuple is similar to a list except that it is fixed-length and immutable.")
keranjang = ('telur', 'mie', 'cabe')
print(keranjang[2])


print(" === Set === ")
print("A set is a collection of elements with no repeats and without insertion order but sorted order.")
keluarga = {'ayah', 'ibu', 'kaka', 'adik'}
if 'saya' in keluarga:
    print('Hallo')
else:
    print(keluarga)

print(" === Dict === ")
print("A dictionary in Python is a collection of key-value pairs.")
daftar_belanja = {
    "tomat": 3,
    "bawang merah": 5,
    "bawang putih": 7,
    "tambahan": ['bakso', 'bumbu', 'cabe']
}
print(daftar_belanja['tambahan'])
print(daftar_belanja.get('bawang merah'))

print("Converting between data type")
a = '123'
b = int(a)
c = list(a)
print(b)
print(c)
