import tkinter as tk
from PIL import Image, ImageTk

def display_image(image):
    window = tk.Toplevel()
    window.title("Контурное изображение")

    img = Image.fromarray(image)
    img_tk = ImageTk.PhotoImage(img)

    label = tk.Label(window, image=img_tk)
    label.image = img_tk  
    label.pack()
