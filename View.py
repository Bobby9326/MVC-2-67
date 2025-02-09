# View.py
import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from datetime import datetime

class PetView:
    def __init__(self, root):
        self.root = root
        self.root.title("Magical Pets Management")
        
        #กำหนดขนาดหน้าต่าง
        self.root.geometry("500x400")
        
        # กำหนด style
        self.style = ttk.Style()
        self.style.configure("Approved.TLabel", foreground="green")
        self.style.configure("Rejected.TLabel", foreground="red")
        

        self.notebook = ttk.Notebook(root)
        self.notebook.pack(pady=10, expand=True, fill='both')
        self.insert_frame = ttk.Frame(self.notebook)
        self.report_frame = ttk.Frame(self.notebook)
        
        self.notebook.add(self.insert_frame, text='Insert')
        self.notebook.add(self.report_frame, text='Report')
        
        self._setup_insert_frame()
        self._setup_report_frame()
        
    def _setup_insert_frame(self):

        # เลือกประเภทสัตว์
        self.pet_type_var = tk.StringVar()
        self.pet_type_label = ttk.Label(self.insert_frame, text="Select Pet Type:")
        self.pet_type_label.pack(pady=5)
        
        # ประเภทสัตว์
        types = [("Phoenix", "นกฟินิกซ์"), ("Dragon", "มังกร"), ("Owl", "นกฮูก")]
        for value, text in types:
            ttk.Radiobutton(self.insert_frame, text=text, value=value,
                          variable=self.pet_type_var, command=self._update_form).pack()
        
        # กำหนด input
        self.input_frame = ttk.Frame(self.insert_frame)
        self.input_frame.pack(pady=10)
        self.health_check_date = DateEntry(self.input_frame, width=12, background='darkblue',
                                         foreground='white', borderwidth=2)
        self.vaccine_count = ttk.Entry(self.input_frame)
        
        self.fire_cert_var = tk.BooleanVar()
        self.pollution_level = ttk.Entry(self.input_frame)
        self.flight_distance = ttk.Entry(self.input_frame)
        
        # สถานะการยืนยัน
        self.status_label = ttk.Label(self.insert_frame, text="")
        self.status_label.pack(pady=5)
        
        # ปุ่มเพิ่มสัตว์
        self.add_button = ttk.Button(self.insert_frame, text="Add Pet")
        self.add_button.pack()
        
    def _setup_report_frame(self):
        
        # กำหนดประเภทของสัตว์
        pet_types = ["Phoenix", "Dragon", "Owl"]
        for pet_type in pet_types:
            frame = ttk.Frame(self.report_frame)
            frame.pack(pady=10, padx=10, fill="x")
            
            ttk.Label(frame, text=f"{pet_type}:").pack(side="left", padx=5)
            ttk.Label(frame, text="Approved: ").pack(side="left")
            
            # แสดงสัตว์ที่ approved เป็นสีเขียว
            approved_label = ttk.Label(frame, text="0", style="Approved.TLabel")
            approved_label.pack(side="left", padx=5)
            setattr(self, f"{pet_type.lower()}_approved", approved_label)
            
            ttk.Label(frame, text="Rejected: ").pack(side="left")
            
            # แสดงสัตว์ที่ rejected เป็นสีแดง
            rejected_label = ttk.Label(frame, text="0", style="Rejected.TLabel")
            rejected_label.pack(side="left", padx=5)
            setattr(self, f"{pet_type.lower()}_rejected", rejected_label)
    
    def _update_form(self):

        # เคลียร์ input
        for widget in self.input_frame.winfo_children():
            widget.pack_forget()
        
        ttk.Label(self.input_frame, text="Health Check Date:").pack(pady=5)
        self.health_check_date.pack(pady=5)
        
        ttk.Label(self.input_frame, text="Vaccine Count:").pack(pady=5)
        self.vaccine_count.pack(pady=5)
        
        pet_type = self.pet_type_var.get()
        if pet_type == "Phoenix":
            ttk.Label(self.input_frame, text="Fire Certificate:").pack(pady=5)
            ttk.Checkbutton(self.input_frame, variable=self.fire_cert_var).pack(pady=5)
        elif pet_type == "Dragon":
            ttk.Label(self.input_frame, text="Pollution Level (%):").pack(pady=5)
            self.pollution_level.pack(pady=5)
        elif pet_type == "Owl":
            ttk.Label(self.input_frame, text="Flight Distance (km):").pack(pady=5)
            self.flight_distance.pack(pady=5)
    
    # เพิ่มฟังก์ชันให้ปุ่ม
    def set_add_pet_command(self, command):
        self.add_button.config(command=command)
    
    # แสดงสถานะการยืนยัน
    def update_status(self, message): 
        status_style = "Approved.TLabel" if "Approved" in message else "Rejected.TLabel"
        self.status_label.configure(style=status_style)
        self.status_label.config(text=message)
    
    # แสดงรายงานของสัตว์ทั้งหมด
    def update_report(self, stats):
        for pet_type in ["phoenix", "dragon", "owl"]:
            getattr(self, f"{pet_type}_approved").config(text=str(stats[pet_type]["approved"]))
            getattr(self, f"{pet_type}_rejected").config(text=str(stats[pet_type]["rejected"]))
    
    # ดึงข้อมูลที่อยู่ใน input ทั้งหมด
    def get_input_values(self):

        # ข้อมูล input พื้นฐาน
        values = {
            "pet_type": self.pet_type_var.get(),
            "health_check_date": self.health_check_date.get_date(),
            "vaccine_count": self.vaccine_count.get()
        }

        # ข้อมูล input พิเศษตามชนิดสัตว์
        if values["pet_type"] == "Phoenix":
            values["special_value"] = self.fire_cert_var.get()
        elif values["pet_type"] == "Dragon":
            values["special_value"] = self.pollution_level.get()
        elif values["pet_type"] == "Owl":
            values["special_value"] = self.flight_distance.get()
            
        return values