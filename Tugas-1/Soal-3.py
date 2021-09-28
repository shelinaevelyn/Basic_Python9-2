nilaiteori = float(input("Nilai Ujian Teori = "))
nilaipraktek = float(input("Nilai Ujian Praktek = "))

if nilaiteori>=70 and nilaipraktek>=70:
    print ("Selamat, anda lulus!")
elif nilaiteori>=70 and nilaipraktek<70:
    print ("Anda harus mengulang ujian praktek.")
elif nilaiteori<70 and nilaipraktek>=70:
    print ("Anda harus mengulang ujian teori.")
else: 
    print ("Anda harus mengulang ujian teori dan praktek.")