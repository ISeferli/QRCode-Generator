# QR Code Generator – Maritime Museum of Crete Internship

This project is a Python-based **QR Code Generator** developed as part of an internship at the [Maritime Museum of Crete](https://mar-mus-crete.gr), located in Chania, Greece. It provides a graphical user interface (GUI) for generating and saving QR codes from user-provided input. The program was used to assist in digital archiving and interactive display labels for museum exhibits.

---

## ✨ Features

- Create QR codes from any URL or text
- Simple and intuitive GUI using `tkinter`
- Save QR code images as `.png` files
- Customizable file location and filename

---

## 🖼️ User Interface

The GUI consists of three input fields:
1. **Text/URL** – The content encoded in the QR code
2. **Location** – File path where the QR code should be saved
3. **Filename** – Desired name of the QR code image

A single **Generate Code** button creates the image and notifies the user when it is successfully saved.

---

## 🛠 Installation

Make sure Python 3 is installed on your system. You can install the required libraries using pip:

```bash
pip install qrcode[pil]
```

Then simply run the script:

```bash
python qr_generator.py
```

---

## 📚 Source

Initial inspiration and structure adapted from: [DataFlair QR Code Generator Tutorial](https://data-flair.training/blogs/python-qr-code-generator-project/)
