#Fungsi string
print("FUNGSI STRING")

str = "hello ramadhan"
print("Text Awal :", str)
#fungsi capitalize()
s = str.capitalize()
print(s)
#fungsi center()
s = str.center(20, '*')
print(s)
#fungsi count
a = str.count('l')
b = str.count('h')
print("jumlah huruf l= ", a)
print("jumlah huruf h= ", b)
#fungsi endswith
str = "hello ramadhan"
print(str.endswith("ramadhan"))
print(str.endswith("ramadhan:)"))
