# Controller.py
class PetController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.set_add_pet_command(self.add_pet)
        self.update_report()
    
    # เพิ่มสัตว์เข้าไปในระบบ
    def add_pet(self):

        # ดึงข้อมูลมา input มาจาก view
        values = self.view.get_input_values()
        
        try:
            vaccine_count = int(values["vaccine_count"])
            # ตรวจสอบว่า vaccine_count เป็นจำนวนบวก
            if vaccine_count <= 0:
                self.view.update_status("Vaccine count must be positive")
                return
        except ValueError:
            self.view.update_status("Invalid vaccine count")
            return
        #  status Default เป็น Rejected
        status = "Rejected"
        pet_type_map = {
            "Phoenix": "นกฟินิกซ์",
            "Dragon": "มังกร",
            "Owl": "นกฮูก"
        }
        #  ถ้า Phoenix มีใบกันไฟลาม ให้ status เป็น Approved
        if values["pet_type"] == "Phoenix":
            if values["special_value"]:
                status = "Approved"
        elif values["pet_type"] == "Dragon":
            try:
                #  ถ้า Phoenix มีระดับมลพิษที่เกิดจากควันไม่เกิน 70% ให้ status เป็น Approved
                pollution = float(values["special_value"])
                if pollution <= 70:
                    status = "Approved"
            except ValueError:
                self.view.update_status("Invalid pollution level")
                return
        elif values["pet_type"] == "Owl":
            try:
                #  ถ้า Owl มีระยะทางบินได้โดยไม่ทานข้าวไม่ต่ำกว่า 100km ให้ status เป็น Approved
                distance = float(values["special_value"])
                if distance >= 100:
                    status = "Approved"
            except ValueError:
                self.view.update_status("Invalid flight distance")
                return
        # เพิ่มสัตว์ไปในการข้อมูลโดยส่งข้อมูลไปให้ Model
        self.model.add_pet(
            pet_type_map[values["pet_type"]],
            values["health_check_date"],
            vaccine_count,
            values["special_value"],
            status
        )
        # แสดงสถานะการเพิ่ม
        self.view.update_status(f"Pet {status}")
        self.update_report()

    # อัปเดตรายงานสัตว์
    def update_report(self):
        stats = self.model.get_stats()
        self.view.update_report(stats)