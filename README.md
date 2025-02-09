# MVC-2-67

อธิบายการทำงาน

View (view.py):
	เป็นส่วนที่สร้าง GUI สำหรับการโต้ตอบกับผู้ใช้ โดยใช้ tkinter ในการสร้างหน้าจอ แบ่งเป็น 2 หน้าจอหลักคือหน้า Insert และหน้า Report 
-หน้า Insert:
แสดงฟอร์มสำหรับกรอกข้อมูลสัตว์เลี้ยง มีปุ่มเลือกประเภทสัตว์ (นกฟินิกซ์, มังกร, นกฮูก) แสดงฟอร์มพิเศษตามประเภทสัตว์ที่เลือก เช่น ช่องติ๊กใบรับรองไฟไม่ลามสำหรับนกฟินิกซ์  แสดงสถานะการเพิ่มข้อมูล (สีเขียวเมื่อ approved, สีแดงเมื่อ rejected) และปุ่ม "Add Pet" จะส่งข้อมูลทั้งหมดไปให้ Controller ทำงานต่อ
-หน้า Report:
แสดงสถิติจำนวนสัตว์แต่ละประเภทตามข้อมูลที่  Controller ส่งมาให้ แยกแสดงจำนวน approved (สีเขียว) และ rejected (สีแดง)


Controller (controller.py):
ทำหน้าที่ควบคุมการทำงานและประสานงานระหว่าง Model และ View
-add_pet(): รับข้อมูลจาก View ตรวจสอบความถูกต้องของข้อมูลและเงื่อนไขพิเศษของแต่ละประเภทสัตว์ ส่งข้อมูลให้ Model เก็บบันทึก และ สั่งให้ View อัพเดทการแสดงผล
-update_report(): ดึงข้อมูลสถิติจาก Model และ สั่งให้ View อัพเดทการแสดงผลรายงาน

Model (model.py):
ทำหน้าที่จัดการข้อมูลและการเข้าถึงฐานข้อมูลจัดการการอ่านและเขียนไฟล์ CSV (Storage.csv)
-generate_food_code(): สร้างรหัสอาหารแบบสุ่ม 8 หลัก โดยตัวแรกไม่ใช่ 0 และไม่ซ้ำกับที่มีอยู่
-add_pet(): เพิ่มข้อมูลสัตว์เลี้ยงใหม่ลงในฐานข้อมูล
-get_stats(): ดึงสถิติจำนวนสัตว์ที่ approved และ rejected แยกตามประเภท

app.py:
- ทำหน้าที่สร้างและเชื่อมต่อองค์ประกอบทั้ง 3 ส่วนของ MVC เข้าด้วยกัน โดยจะสร้าง Model สำหรับจัดการข้อมูลก่อน ตามด้วย View สำหรับแสดงผล GUI และสุดท้ายคือสร้าง Controller พร้อมส่ง Model และ View ให้ Controller จัดการ จากนั้นเริ่มการทำงานของ GUI ด้วย mainloop() เพื่อให้โปรแกรมพร้อมรับการโต้ตอบจากผู้ใช้ การแบ่งแยกหน้าที่แบบ MVC ช่วยทำให้โค้ดเป็นระเบียบ ง่ายต่อการดูแลรักษา และสามารถปรับเปลี่ยนส่วนใดส่วนหนึ่งได้โดยไม่กระทบส่วนอื่น
