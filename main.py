import qrcode
from tkinter import *
from tkinter import messagebox

def main():
    createWindow()

#Function to generate the QR code and save it
def generateCode(size, text, loc, name):
    #Creating a QRCode object of the size specified by the user
    #Generate QR code
    url = qrcode.QRCode(version=int(size.get()), box_size=10, border=5)
    url.add_data(text.get())
    url.make(fit=True)
    qrImage = url.make_image()

    # Create and save the png file naming it by the name of the pdf
    fileLoc = loc.get() + "\\" + name.get()
    qrImage.save(f'{fileLoc}.png')

    # Showing the pop up message on saving the file
    messagebox.showinfo("QR Code Generator", "QR Code is saved successfully!")

def createWindow():
    #Creating the window
    window = Tk()
    window.title("mar-mus-crete QR generator")
    window.geometry('700x700')
    window.config(bg='SteelBlue3');

    #Label for the window
    headingFrame = Frame(window, bg="azure", bd=5)
    headingFrame.place(relx=0.15, rely=0.05, relwidth=0.7, relheight=0.1)
    headingLabel = Label(headingFrame, text="Generate QR Code", bg='azure', font=('Times',20,'bold'))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    # Taking the input of the text or URL to get QR code
    Frame1 = Frame(window, bg="SteelBlue3")
    Frame1.place(relx=0.1, rely=0.15, relwidth=0.7, relheight=0.3)
    label1 = Label(Frame1, text="Enter URL code: ", bg="SteelBlue3", fg='azure', font=('Courier', 13, 'bold'))
    label1.place(relx=0.05, rely=0.2, relheight=0.08)
    text = Entry(Frame1, font=('Century 12'))
    text.place(relx=0.05, rely=0.4, relwidth=1, relheight=0.2)

    # Getting input of the location to save QR Code
    Frame2 = Frame(window, bg="SteelBlue3")
    Frame2.place(relx=0.1, rely=0.35, relwidth=0.7, relheight=0.3)
    label2 = Label(Frame2, text="Enter the location to save the QR Code: ", bg="SteelBlue3", fg='azure', font=('Courier', 13, 'bold'))
    label2.place(relx=0.05, rely=0.2, relheight=0.08)
    loc = Entry(Frame2, font=('Century 12'))
    loc.place(relx=0.05, rely=0.4, relwidth=1, relheight=0.2)

    # Getting input of the QR Code image name
    Frame3 = Frame(window, bg="SteelBlue3")
    Frame3.place(relx=0.1, rely=0.55, relwidth=0.7, relheight=0.3)
    label3 = Label(Frame3, text="Enter the name of the QR Code: ", bg="SteelBlue3", fg='azure', font=('Courier', 13, 'bold'))
    label3.place(relx=0.05, rely=0.2, relheight=0.08)
    name = Entry(Frame3, font=('Century 12'))
    name.place(relx=0.05, rely=0.4, relwidth=1, relheight=0.2)
 #   name = name + 'png'

    # Getting the input of the size of the QR Code
    Frame4 = Frame(window, bg="SteelBlue3")
    Frame4.place(relx=0.1, rely=0.75, relwidth=0.7, relheight=0.2)
    label4 = Label(Frame4, text="Enter the size from 1 to 40 with 1 being 21x21: ", bg="SteelBlue3", fg='azure', font=('Courier', 13, 'bold'))
    label4.place(relx=0.05, rely=0.2, relheight=0.08)
    size = Entry(Frame4, font=('Century 12'))
    size.place(relx=0.05, rely=0.4, relwidth=0.5, relheight=0.2)

    # Button to generate and save the QR Code
    button = Button(window, text='Generate Code', font=('Courier', 15, 'normal'), command=lambda: generateCode(size, text, loc, name))
    button.place(relx=0.35, rely=0.9, relwidth=0.25, relheight=0.05)

    #Runs the window till it is closed manually
    window.mainloop()

if __name__ == "__main__":
    main()