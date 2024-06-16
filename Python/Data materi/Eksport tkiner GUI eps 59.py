import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
#variabel tampilan
tampilan = tk.Tk()

#configurasi tampilan
tampilan.configure(bg="white")
tampilan.geometry("300x200")
tampilan.resizable(False,False)
tampilan.title("Po0023")

#Bagian input
bagian_masukan = ttk.Frame(tampilan)
# penempatan Grid, pack, place
bagian_masukan.pack(padx=10,pady=10,fill="x",expand=True)

#komponen (label,entry)

# Variabel
namaDep = tk.StringVar()
namaBel = tk.IntVar()

# Inputan dari variabel
nama_depan_l = ttk.Label(bagian_masukan,text="masukan nama mu :")
nama_depan_l.pack(padx=10,fill="x",expand=True)
nama_depan_E = ttk.Entry(bagian_masukan,textvariable=namaDep)
nama_depan_E.pack(padx=10,fill="x",expand=True)
nama_Belakang_l = ttk.Label(bagian_masukan,text="masukan nama mu :")
nama_Belakang_l.pack(padx=10,fill="x",expand=True)
nama_Belakang_E = ttk.Entry(bagian_masukan,textvariable=namaBel)
nama_Belakang_E.pack(padx=10,fill="x",expand=True)

# Tombol
def TBL():
    print("Nama Sudah di konfirmasi")
    # mengambil Data dari input dengan memasukan get() setiap variabel yang akan di masukan
    print(f"Nama Depan : {namaDep.get()}")
    print(f"Nama belakang : {namaBel.get()}")
    pesan = f"Data telah masuk \nNama Depan : {namaDep.get()} \nNama Belakang : {namaBel.get()}"
    showinfo(title="Notif",message=pesan)

tombol_s = ttk.Button(bagian_masukan,text="Oke",command=TBL)
tombol_s.pack(padx=10,pady=10,fill="x",expand=True)






#loop tampilan (agar tetap pada gui)
tampilan.mainloop()