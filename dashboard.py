import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from typing import Dict, Any

class HealthcareDashboard:
    def __init__(self, master):
        self.master = master
        master.title("Dashboard")
        master.geometry("400x500")
        
        self.bg_color = '#f0f4f8'
        self.accent_color = '#2563eb'
        self.text_color = '#1e3a8a'
        self.input_bg = 'white'

        master.configure(bg=self.bg_color)
        self.create_widgets()

    def create_widgets(self):
        
        main_frame = tk.Frame(self.master, bg=self.bg_color)
        main_frame.pack(padx=20, pady=20, fill='both', expand=True)

        
        title_label = tk.Label(
            main_frame, 
            text="Healthcare Dashboard", 
            font=('Arial', 18, 'bold'), 
            bg=self.bg_color, 
            fg=self.accent_color
        )
        title_label.pack(pady=(10, 20))

        
        name_frame = tk.Frame(main_frame, bg=self.input_bg, relief=tk.FLAT, borderwidth=1)
        name_frame.pack(fill='x', pady=5)
        name_icon = tk.Label(name_frame, text="👤", bg=self.input_bg, fg=self.accent_color)
        name_icon.pack(side='left', padx=(10, 5))
        self.name_entry = tk.Entry(
            name_frame, 
            width=30, 
            bg=self.input_bg, 
            relief=tk.FLAT, 
            font=('Arial', 10),
            fg=self.text_color
        )
        self.name_entry.pack(side='left', padx=5, pady=10)

        
        age_frame = tk.Frame(main_frame, bg=self.input_bg, relief=tk.FLAT, borderwidth=1)
        age_frame.pack(fill='x', pady=5)
        age_icon = tk.Label(age_frame, text="🎂", bg=self.input_bg, fg=self.accent_color)
        age_icon.pack(side='left', padx=(10, 5))

        
        self.age_var = tk.StringVar(value="Select Age")
        age_dropdown = ttk.Combobox(
            age_frame, 
            textvariable=self.age_var, 
            values=[str(age) for age in range(101)],
            width=27,
            state="readonly"
        )
        age_dropdown.pack(side='left', padx=5, pady=10)

        
        self.file_path = None
        upload_btn = tk.Button(
            main_frame, 
            text="Upload Medical File", 
            command=self.upload_file,
            bg=self.accent_color, 
            fg='white',
            relief=tk.FLAT,
            font=('Arial', 10, 'bold')
        )
        upload_btn.pack(pady=10, fill='x')

        
        submit_btn = tk.Button(
            main_frame, 
            text="Submit Patient Information", 
            command=self.submit_form,
            bg=self.accent_color, 
            fg='white',
            relief=tk.FLAT,
            font=('Arial', 12, 'bold')
        )
        submit_btn.pack(pady=20, fill='x')

    def upload_file(self):
        self.file_path = filedialog.askopenfilename(
            title="Select Medical File",
            filetypes=[
                ("PDF files", "*.pdf"), 
                ("Image files", "*.png *.jpg *.jpeg"), 
                ("All files", "*.*")
            ]
        )

    def submit_form(self):
        name = self.name_entry.get().strip()
        age = self.age_var.get()

        if not name or age == "Select Age":
            messagebox.showerror("Error", "Please fill in all fields")
            return

        patient_data: Dict[str, Any] = {
            "name": name,
            "age": age,
            "file": self.file_path
        }

        print("Patient Data Submitted:")
        for key, value in patient_data.items():
            print(f"{key.capitalize()}: {value}")
        
        messagebox.showinfo("Success", "Patient information submitted successfully!")

def main():
    root = tk.Tk()
    dashboard = HealthcareDashboard(root)
    root.mainloop()

if __name__ == "__main__":
    main()
