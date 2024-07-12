import tkinter as tk
from tkinter import filedialog
import PyPDF2
import pyttsx3

class PDFReader:
    def __init__(self, master):
        self.master = master
        self.master.title("PDF Reader")
        self.master.geometry("500x500")

        self.file_path = ""
        self.content = []

        self.text_box = tk.Text(self.master)
        self.text_box.pack()

        self.read_button = tk.Button(self.master, text="Read", command=self.read_pdf)
        self.read_button.pack()

        self.open_button = tk.Button(self.master, text="Open", command=self.open_pdf)
        self.open_button.pack()

        self.audio_button = tk.Button(self.master, text="Generate Audiobook", command=self.generate_audiobook)
        self.audio_button.pack()

    def read_pdf(self):
        self.content = read_pdf(self.file_path)
        self.text_box.delete("1.0", tk.END)
        self.text_box.insert(tk.END, "\n".join(self.content))

    def open_pdf(self):
        self.file_path = filedialog.askopenfilename()
        self.content = read_pdf(self.file_path)
        self.text_box.delete("1.0", tk.END)
        self.text_box.insert(tk.END, "\n".join(self.content))

    def generate_audiobook(self):
        create_audiobook(self.file_path)

def read_pdf(file_path):
    with open(file_path, 'rb') as file:
        pdf_file = PyPDF2.PdfFileReader(file)
        num_pages = pdf_file.numPages

        content = []
        for page_num in range(num_pages):
            page = pdf_file.getPage(page_num)
            content.append(page.extractText())

        return content

def create_audiobook(file_path):
    content = read_pdf(file_path)
    text = ' '.join(content)
    engine = pyttsx3.init()
    engine.save_to_file(text, 'audio.mp3')
    engine.runAndWait()

root = tk.Tk()
app = PDFReader(root)
root.mainloop()