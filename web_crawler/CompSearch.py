import customtkinter
from webCrawlerMain import webCrawler
from exceltodictionary import valuesfordropdown #val i dropdown meny

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("green") #can have blue also

#val i dropdown meny
nacetemp = valuesfordropdown()
nacekoder = list(nacetemp.keys())
last_button = None
thecode = None
buttons = []
label2 = None
strignumber = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

root = customtkinter.CTk()
root.geometry("1000x700") #storlek på fönstret 

def knappfunk(): #funktion för vad som händer när man klickar på knappen
    """
        Function to handle button click event.
        Validates the input region and Nace code, and prints the selected Nace code and region.
    """
    global label2
    global thecode
    global strignumber
    if label2 is not None:
        label2.destroy()
    if len(neighbor.get()) < 2:
        label2 = customtkinter.CTkLabel(master=frame, text="You need more characters in Region", text_color="red")
        label2.pack(pady=1, padx=10)
    elif any(num in neighbor.get() for num in strignumber):
        label2 = customtkinter.CTkLabel(master=frame, text="The region cant have a nuber in it", text_color="red")
        label2.pack(pady=1, padx=10)
    elif thecode is None:
        label2 = customtkinter.CTkLabel(master=frame, text="You need to pick a Nace code", text_color="red")
        label2.pack(pady=1, padx=10)
    else:
        print(nacetemp[nacekoder[int(thecode)]], neighbor.get()) #skriver ut nacekoden
        webCrawler(nacetemp[nacekoder[int(thecode)]], neighbor.get())


    #print(nacekoder[int(thecode)])
    #print(entrytest.get())
    #print(naceval.get())

def thenacecode(variable):
    """
        Function to handle the selection of a Nace code button.
        Changes the appearance of the selected button and updates the selected Nace code.

        Args:
            variable (int): The index of the selected Nace code button.
    """

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

