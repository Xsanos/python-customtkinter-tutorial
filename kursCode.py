import customtkinter


okno = customtkinter.CTk()
okno.geometry("360x240")
okno.title("okno")

def Nowe(okno_poprzednie, okno_nowe):
    okno_poprzednie.destroy()
    okno_nowe

def Okno_Startowe():
    warstwa = customtkinter.CTkFrame(master=okno)
    warstwa.pack()

    zawartosc = customtkinter.CTkLabel(master=warstwa, height=200, width=200, text="Okno Startowe", text_color="black", bg_color="white")
    zawartosc.pack()

    button = customtkinter.CTkButton(master=warstwa, width=200, height=50, text="Przejdź do Okna 1", command=lambda:Nowe(warstwa, Okno_1()))
    button.place(relx=0.5, rely=0.7, anchor=customtkinter.CENTER)    

def Okno_1():
    warstwa = customtkinter.CTkFrame(master=okno)
    warstwa.pack()

    zawartosc = customtkinter.CTkLabel(master=warstwa, height=200, width=200, text="Okno 1", text_color="black", bg_color="white")
    zawartosc.pack()

    button = customtkinter.CTkButton(master=warstwa, width=200, height=50, text="Wróć", command=lambda:Nowe(warstwa, Okno_Startowe()))
    button.place(relx=0.5, rely=0.7, anchor=customtkinter.CENTER)    


Okno_Startowe()

okno.mainloop()