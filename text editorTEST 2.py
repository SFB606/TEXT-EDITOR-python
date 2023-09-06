import tkinter as tk
from tkinter import filedialog

window = tk.Tk()
window.geometry("800x600")
window.title("TEXT EDITOR MARK 1")


# button=Button(text='ok')
# button.pack()
def Open():
    file_path = filedialog.askopenfile(defaultextension='.txt', filetype=[("text files", '*txt'), ("All files", '*.*')])
    if file_path:
        with open(file_path, 'r') as file:
            text.delete(1.0, tk.END)
            text.insert(tk.END, file.read())


def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, 'w') as file:
            file.write(text.get(1.0, tk.END))



window.configure(bg='grey')
text = tk.Text(window)
text.pack()
text.configure(bg='light gray')


text.pack(fill=tk.BOTH, expand=True)


menu = tk.Menu(window)
window.config(menu=menu)


file_menu = tk.Menu()
menu.add_cascade(label="File", menu=file_menu)


file_menu.add_separator()
file_menu.add_command(label="Exit", command=window.quit)
file_menu.add_command(label="Open (Ctrl+O)", command=Open)
file_menu.add_command(label="Save (Ctrl+S)", command=save_file)



def exit_application():
    result = tk.messagebox.askquestion("Exit", "Are you sure you want to exit?")
    if result == "yes":
        window.quit()

file_menu.add_command(label="Exit", command=exit_application)




window.mainloop()
