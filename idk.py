import tkinter as tk
from tkinter import filedialog, messagebox
from typing import Dict, Any

class HealthcareDashboard:
    def __init__(self, master):
        self.master = master
        master.title("=Dashboard")
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
            text="Dashboard", 
            font=('Arial', 18, 'bold'), 
            bg=self.bg_color, 
            fg=self.accent_color
        )
        title_label.pack(pady=(10, 20))

        
        subtitle_label = tk.Label(
            main_frame, 
            text="Patient Information Submission", 
            font=('Arial', 10), 
            bg=self.bg_color, 
            fg=self.text_color
        )
        subtitle_label.pack(pady=(0, 15))

        
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
        self.age_entry = tk.Entry(
            age_frame, 
            width=30, 
            bg=self.input_bg, 
            relief=tk.FLAT, 
            font=('Arial', 10),
            fg=self.text_color
        )
        self.age_entry.pack(side='left', padx=5, pady=10)

        
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

        
        self.status_label = tk.Label(
            main_frame, 
            text="", 
            bg=self.bg_color, 
            fg=self.accent_color
        )
        self.status_label.pack(pady=10)

    def upload_file(self):
        self.file_path = filedialog.askopenfilename(
            title="Select Medical File",
            filetypes=[
                ("PDF files", "*.pdf"), 
                ("Image files", "*.png *.jpg *.jpeg"), 
                ("All files", "*.*")
            ]
        )
        if self.file_path:
            self.status_label.config(
                text=f"File selected: {self.file_path.split('/')[-1]}"
            )

    def submit_form(self):
        name = self.name_entry.get().strip()
        age = self.age_entry.get().strip()

        if not name or not age:
            messagebox.showerror("Error", "Please fill in all fields")
            return

        try:
            age = int(age)
            if age < 0 or age > 120:
                raise ValueError("Invalid age")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid age")
            return

        patient_data: Dict[str, Any] = {
            "name": name,
            "age": age,
            "file": self.file_path
        }

        self.process_patient_data(patient_data)

    def process_patient_data(self, data: Dict[str, Any]):
        print("Patient Data Submitted:")
        for key, value in data.items():
            print(f"{key.capitalize()}: {value}")
        
        self.name_entry.delete(0, tk.END)
        self.age_entry.delete(0, tk.END)
        self.file_path = None
        
        messagebox.showinfo("Success", "Patient information submitted successfully!")

def main():
    root = tk.Tk()
    dashboard = HealthcareDashboard(root)
    root.mainloop()

if __name__ == "__main__":
    main()