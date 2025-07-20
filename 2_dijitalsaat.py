import time
from tkinter import Tk, Label

# Pencereyi oluşturma
app_window = Tk()
app_window.title("Dijital Saat")
app_window.geometry("400x200")# boyutlar
app_window.configure(bg="bisque")#arka plan rengi

# Saat etiketini oluşturma
label = Label(app_window, font=("Arial", 36, 'bold'), bg="bisque", fg="black")
label.pack(pady=20)

# Tarih etiketini oluşturma
date_label = Label(app_window, font=("Arial", 18), bg="bisque", fg="black")
date_label.pack()

def update_time():
    current_time = time.strftime("%H:%M:%S")
    label.config(text=current_time)
    current_date = time.strftime("%d %B %Y")
    date_label.config(text=current_date)
    label.after(1000, update_time)  # Her 1000 milisaniyede bir güncelleme yap

update_time()
app_window.mainloop()# sürekli hale getirir
# mac için python 3.13.3 ile çalıştırdım 3.9.6 hata verdi