import tkinter as tk
from tkinter import filedialog, messagebox
from image_loader import load_image
from image_processor import create_contour_image
from image_viewer import display_image
import cv2

class ImageProcessingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Контурное изображение")
        
        self.load_button = tk.Button(root, text="Загрузить изображение", command=self.load_image)
        self.load_button.pack(pady=20)

        self.resize_var = tk.BooleanVar(value=False)
        self.resize_checkbox = tk.Checkbutton(root, text="Изменить разрешение", variable=self.resize_var)
        self.resize_checkbox.pack(pady=5)

        self.width_label = tk.Label(root, text="Ширина:")
        self.width_label.pack()
        self.width_entry = tk.Entry(root)
        self.width_entry.pack(pady=5)

        self.height_label = tk.Label(root, text="Высота:")
        self.height_label.pack()
        self.height_entry = tk.Entry(root)
        self.height_entry.pack(pady=5)

        self.process_button = tk.Button(root, text="Создать контур", command=self.process_image, state=tk.DISABLED)
        self.process_button.pack(pady=20)

        self.save_button = tk.Button(root, text="Сохранить изображение", command=self.save_image, state=tk.DISABLED)
        self.save_button.pack(pady=20)

        self.image_path = None
        self.contour_image = None

    def load_image(self):
        self.image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp")])
        if self.image_path:
            self.process_button.config(state=tk.NORMAL)

    def process_image(self):
        if self.image_path:
            if self.resize_var.get():
                try:
                    width = int(self.width_entry.get())
                    height = int(self.height_entry.get())
                except ValueError:
                    messagebox.showerror("Ошибка", "Пожалуйста, введите корректные значения ширины и высоты.")
                    return
            else:
                width, height = None, None  

            self.contour_image = create_contour_image(self.image_path, width, height)
            display_image(self.contour_image)
            self.save_button.config(state=tk.NORMAL) 

    def save_image(self):
        if self.contour_image is not None:
            file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg;*.jpeg"), ("All files", "*.*")])
            if file_path:
                cv2.imwrite(file_path, cv2.cvtColor(self.contour_image, cv2.COLOR_RGB2BGR))  

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageProcessingApp(root)
    root.mainloop()
