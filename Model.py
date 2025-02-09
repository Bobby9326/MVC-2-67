# Model.py
import pandas as pd
from datetime import datetime
import random

class PetModel:
    def __init__(self):
        self.file_path = "Storage.csv"
        try:
            self.df = pd.read_csv(self.file_path)
        except FileNotFoundError:
            # สร้างไฟล์ Storage.csv หากยังไม่มี
            self.df = pd.DataFrame(columns=[
                "ลำดับ", "รหัสอาหาร", "ประเภทของสัตว์เลี้ยง",
                "วันที่ตรวจสุขภาพล่าสุด", "จํานวนวัคซีนที่ได้รับแล้ว",
                "ค่าพิจารณา", "สถานะพิจารณา"
            ])
            self.df.to_csv(self.file_path, index=False)

    def generate_food_code(self):
        while True:
            # สร้างรหัส 8 ตัวโดยขึ้นต้นที่ 1
            code = random.randint(10000000, 99999999)
            # ตรวจสอบว่ารหัสถูกหลัก และ มีรหัสนี้หรือยัง
            if str(code)[0] != '0' and not self.df['รหัสอาหาร'].astype(str).str.contains(str(code)).any():
                return code

    def add_pet(self, pet_type, health_check_date, vaccine_count, special_value, status):
        # สร้าง record ข้อมูลที่ได้รหัส
        new_row = {
            "ลำดับ": len(self.df) + 1,
            "รหัสอาหาร": self.generate_food_code(),
            "ประเภทของสัตว์เลี้ยง": pet_type,
            "วันที่ตรวจสุขภาพล่าสุด": health_check_date.strftime("%d/%m/%Y"),
            "จํานวนวัคซีนที่ได้รับแล้ว": vaccine_count,
            "ค่าพิจารณา": special_value,
            "สถานะพิจารณา": status
        }
        # เพิ่ม record ที่สร้างลงไปในไฟล์ Storage.csv 
        self.df = pd.concat([self.df, pd.DataFrame([new_row])], ignore_index=True)
        self.df.to_csv(self.file_path, index=False)

    # ส่งข้อมูลสถานะของสัตว์ทั้งหมด
    def get_stats(self):
        # กำหนด Default
        stats = {
            "phoenix": {"approved": 0, "rejected": 0},
            "dragon": {"approved": 0, "rejected": 0},
            "owl": {"approved": 0, "rejected": 0}
        }
        # จับ key ของข้อมูลที่กำหนดและข้อมูลในตาราง
        pet_type_map = {
            "นกฟินิกซ์": "phoenix",
            "มังกร": "dragon",
            "นกฮูก": "owl"
        }
        # เพิ่มข้อมูลตามตาราง
        for _, row in self.df.iterrows():
            pet_type = pet_type_map[row["ประเภทของสัตว์เลี้ยง"]]
            status = "approved" if row["สถานะพิจารณา"] == "Approved" else "rejected"
            stats[pet_type][status] += 1
            
        return stats