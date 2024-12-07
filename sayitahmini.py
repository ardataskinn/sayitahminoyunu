import random
import tkinter as tk
import os



pencere = tk.Tk()
pencere.title("Sayı Oyunu")
pencere.geometry("500x500+450+150")
pencere.resizable(width=False,height=False)
pencere.configure(bg="#F5F5DC")

label1 = tk.Label(pencere,text="Sayı Tahmin Oyunu",fg="#FF5722",bg="#F5F5DC",font=("Helvatica",40,"bold"))
label1.grid(row=0,column=1)

c = random.randint(2000,20000)
b = random.randint(0,1000)
a = random.randint(b,c)


label2 = tk.Label(pencere,text=f"Sayı {b} ile {c} arasında...",font=("Arial",20,"italic"),bg="#F5F5DC",fg="#37474F")
label2.grid(row=1,column=1)

entry = tk.Entry(pencere,width=20,font=("Arial",30,"bold"),justify="center",bg="#FFFFFF",fg="black",highlightbackground="#BDBDBD",relief="raised")
entry.grid(row=3,column= 1,pady=10,ipady=20)

label3 = tk.Label(pencere,text="",font=("Arial",40,"bold"),bg="#F5F5DC")
label3.grid(row=5,column=1,pady=10)


renkler = ["yellow", "green", "purple", "blue", "red", "white", "pink", "yellow", "green", "purple", "blue", "red", "white", "pink"]
def renk_degistir(renkler, index=0):
    if index < len(renkler):
        pencere.configure(bg=renkler[index])  
        pencere.after(500, renk_degistir, renkler, index + 1) 

def renk_degistir1(renkler, index=0):
    if index < len(renkler):
        label1.config(bg=renkler[index],fg=renkler[index+1])  
        pencere.after(500, renk_degistir1, renkler, index + 1)  

def renk_degistir2(renkler, index=0):
    if index < len(renkler):
        label2.config(bg=renkler[index],fg=renkler[index+1])  
        pencere.after(500, renk_degistir2, renkler, index + 1)

def renk_degistir3(renkler, index=0):
    if index < len(renkler):
        label3.config(bg=renkler[index],fg=renkler[index+1])  
        pencere.after(500, renk_degistir3, renkler, index + 1)


def tahmin():
    if entry.get().isdigit() == True: 
        sayi = int(entry.get())
        if sayi == a:
            label3.config(text="Doğru BİLDİN!!!!",bg="purple")
            entry.config(text="BAŞARDINNNNNN")
            renk_degistir(renkler)
            renk_degistir1(renkler)
            renk_degistir2(renkler)
            renk_degistir3(renkler)
        elif sayi > a:
            label3.config(text="Daha Küçük!",bg="red")
        elif sayi < a:
            label3.config(text="Daha Büyük!",bg="green")
    else:
        label3.config(text="LÜTFEN SAYI GİR",fg="red",bg="white")






def sifirla():
    pencere.quit()  
    pencere.destroy() 
    os.system(f"python3 {__file__}") 




buton1 = tk.Button(pencere, text="Tahmin Et!",fg="black",bg="red", command=tahmin, height=3, width=6)
buton1.grid(row=4,column=1,pady=5)

buton2= tk.Button(pencere,text="Sıfırla",fg="black",command=sifirla,height=1,width=1)
buton2.grid(row=150,column=2,pady=130)



pencere.grid_columnconfigure(0, weight=1)
pencere.grid_columnconfigure(1, weight=1)
pencere.grid_columnconfigure(2, weight=1)






pencere.mainloop()



