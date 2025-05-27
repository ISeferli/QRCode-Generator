import os
import PIL.Image
import qrcode
from qrcode.constants import ERROR_CORRECT_H
from tkinter import *
from tkinter import messagebox

def main():
    create_window()

#Function to generate the QR code and save it
def generate_code(text, name, image_name):
    qr_color = '#082640'

    #Creating a QRCode object of the size specified by the user
    #Generate QR code
    url = qrcode.QRCode(
        version=1,
        error_correction=ERROR_CORRECT_H,
        box_size=10,
        border=4
    )
    url.add_data(text.get())
    url.make(fit=True)
    qr_image = url.make_image(
        fill_color=qr_color, back_color="white").convert('RGB')

    # Only add logo if provided
    logo_path = image_name.get().strip()
    if logo_path:
        try:
            logo = adjust_logo(image_name.get())
            pos = ((qr_image.size[0] - logo.size[0]) // 2,
                   (qr_image.size[1] - logo.size[1]) // 2)
            qr_image.paste(logo, pos, mask=logo.split()[3] if logo.mode == 'RGBA' else None)
        except Exception as e:
            messagebox.showerror("QR Code Generator", f"Error loading logo image: {e}")
            return

    # Create and save the png file naming it by the name of the pdf
    current_dir = os.getcwd()
    file_loc = os.path.join(current_dir, name.get())
    qr_image.save(f'{file_loc}.png')

    # Showing the popup message on saving the file
    messagebox.showinfo("QR Code Generator", "QR Code is saved successfully!")

    # Clear text boxes
    text.delete(0, END)
    name.delete(0, END)
    image_name.delete(0, END)


def adjust_logo(image_name):
    logo = PIL.Image.open(image_name)
    basewidth = 100

    # Adjust image size
    wpercent = (basewidth / float(logo.size[0]))
    hsize = int((float(logo.size[1]) * float(wpercent)))
    return logo.resize((basewidth, hsize))


def create_window():
    #Creating the window
    window = Tk()
    window.title("QR generator")
    window.config(bg='SteelBlue3')

    #Label for the window
    headingFrame = Frame(window, bg="SteelBlue3", bd=5)
    headingFrame.pack(pady=20, fill='x', padx=40)
    headingLabel = Label(headingFrame, text="Generate QR Code",
                         bg='SteelBlue3', font=('Times',20,'bold'))
    headingLabel.pack(fill='both')

    # Taking the input of the text or URL to get QR code
    Frame1 = Frame(window, bg="SteelBlue3")
    Frame1.pack(pady=10, fill='x', padx=40)
    label1 = Label(Frame1, text="Enter URL code: ",
                   bg="SteelBlue3", fg='azure', font=('Courier', 13, 'bold'))
    label1.pack(anchor='w', pady=(10, 0), padx=10)
    text = Entry(Frame1, font=('Century 12'))
    text.pack(padx=10, pady=10, fill='x')

    # Getting input of the QR Code image name
    Frame2 = Frame(window, bg="SteelBlue3")
    Frame2.pack(pady=10, fill='x', padx=40)
    label2 = Label(Frame2, text="Enter the name of the QR Code: ",
                   bg="SteelBlue3", fg='azure', font=('Courier', 13, 'bold'))
    label2.pack(anchor='w', pady=(10, 0), padx=10)
    name = Entry(Frame2, font=('Century 12'))
    name.pack(padx=10, pady=10, fill='x')

    # Getting input of the logo name
    Frame3 = Frame(window, bg="SteelBlue3")
    Frame3.pack(pady=10, fill='x', padx=40)
    label3 = Label(Frame3, text="Enter the name of the logo: ",
                   bg="SteelBlue3", fg='azure', font=('Courier', 13, 'bold'))
    label3.pack(anchor='w', pady=(10, 0), padx=10)
    image_name = Entry(Frame3, font=('Century 12'))
    image_name.pack(padx=10, pady=10, fill='x')

    # Button to generate and save the QR Code
    button = Button(window, text='Generate Code', font=('Courier', 15, 'normal'),
                    command=lambda: generate_code(text, name, image_name))
    button.pack(padx=10, pady=10)

    #Runs the window till it is closed manually
    window.mainloop()


if __name__ == "__main__":
    main()
