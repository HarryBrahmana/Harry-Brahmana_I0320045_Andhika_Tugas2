#menampilkan informasi program

print("Konversi suhu (Farenheit ke Celcius)")

#input suhu dalam fahrenheit
F = float(input("Masukkan suhu(fahrenheit): "))

#melakukan keonversi suhu ke celcius
C = 5 * (F-32) / 9

#menampilkan hasil konversi ke layar
print("Fahrenheit: ", F)
print("Celcius: ",C)