import customtkinter
import peter

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("dark-blue") #can have blue also

nacekoder = ["nacecode 1", "nacecode 2"] #val i dropdown meny

root = customtkinter.CTk()
root.geometry("1000x700") #storlek på fönstret 

def knappfunk(): #funktion för vad som händer när man klickar på knappen
    print("hello")
    print(entrytest.get())
    print(naceval.get())

root.title("CompSearch")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Fyll i dina Nace koder")
label.pack(pady=12, padx=10)

entrytest = customtkinter.CTkEntry(master=frame, placeholder_text="TEST") 
entrytest.pack(pady=12, padx=10)

naceval = customtkinter.CTkOptionMenu(master=frame, values=nacekoder)
naceval.pack(padx=20, pady=10)
naceval.set("choose nace code")  #välj starttext

button = customtkinter.CTkButton(master=frame, text="tesssset", command=lambda:knappfunk()) #lambda gör så att programmet körs när man klickar på knappen
button.pack(pady=12, padx=10)


#startar fönstret
root.wm_attributes("-toolwindow", "True") #Tar bort standardbilden i fönstret
root.mainloop()
