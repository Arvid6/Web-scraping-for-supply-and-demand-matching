import customtkinter
import tkinter
#from peter import webCrawler
from  exceltodictionary import valuesfordropdown #val i dropdown meny

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("green") #can have blue also

#val i dropdown meny
nacetemp = valuesfordropdown()
nacekoder = list(nacetemp.keys())
last_button = None
buttons = []

root = customtkinter.CTk()
root.geometry("1000x700") #storlek på fönstret 

def knappfunk(): #funktion för vad som händer när man klickar på knappen
    #webCrawler(nacetemp[nacekoder[int(thecode)]], neighbor.get())
    #print(nacekoder[int(thecode)])
    print(nacetemp[nacekoder[int(thecode)]], neighbor.get()) #skriver ut nacekoden
    #print(entrytest.get())
    #print(naceval.get())

def thenacecode(variable):
    global last_button
    global thecode 
    if last_button:
        last_button.configure(fg_color="white")  #byt tbx till förra färgen
    scbutton = buttons[variable]  #hämtar nuvarande knapp
    scbutton.configure(fg_color="#7a97ff")  #ändrar nuvarande knapps färg | grön = #71de85
    last_button = scbutton  #uppdatera förra knappen
    thecode = variable
    #print(variable)

root.title("CompSearch")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=30, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Welcome to CompSerch")
label.pack(pady=12, padx=10)

label = customtkinter.CTkLabel(master=frame, text="Fill in the region")
label.pack(pady=1, padx=10)

neighbor = customtkinter.CTkEntry(master=frame, placeholder_text="Region", width=400) 
neighbor.pack(pady=1, padx=10)

my_frame = customtkinter.CTkScrollableFrame(master=frame, width=600, height=400)
my_frame.pack(padx=20, pady=10)
for x in range(len(nacekoder)):
    scbutton = customtkinter.CTkButton(my_frame, text=nacekoder[x], height= 5, corner_radius=0, width=800, fg_color="white", text_color="black", anchor="w", command=lambda x=x:thenacecode(x)) #för att få knapparan att fungera
    scbutton.pack(pady=0)
    buttons.append(scbutton)

button = customtkinter.CTkButton(master=frame, text="Submit", command=lambda:knappfunk()) #lambda gör så att programmet körs när man klickar på knappen
button.pack(pady=12, padx=10)

#startar fönstret
root.wm_attributes("-toolwindow", "True") #Tar bort standardbilden i fönstret
root.mainloop()
