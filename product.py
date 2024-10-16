import datetime

# ฟังก์ชันสำหรับรับข้อมูลลูกค้าจากผู้ใช้
def get_customer_data():
    customer_data = {
        'ชื่อ': input("กรุณากรอกชื่อ: "),
        'ที่อยู่': input("กรุณากรอกที่อยู่: "),
        'เบอร์โทร': input("กรุณากรอกเบอร์โทร: ")
    }
    return customer_data

# รายชื่อสินค้า
products = ['แตงโม', 'แอปเปิ้ล', 'ส้ม', 'กล้วย', 'ทุเรียน']

# ฟังก์ชันสำหรับแสดงรายการสินค้าและให้ผู้ใช้เลือก
def select_products():
    selected_products = []
    print("\nรายการสินค้า:")
    for i, product in enumerate(products, 1):
        print(f"{i}. {product}")

    while True:
        choice = input("\nกรุณาเลือกสินค้าตามหมายเลข (หรือพิมพ์ 'สำเร็จ' เพื่อหยุดเลือก): ")
        if choice.lower() == 'สำเร็จ':
            break
        if choice.isdigit() and 1 <= int(choice) <= len(products):
            selected_products.append(products[int(choice) - 1])
        else:
            print("กรุณาเลือกหมายเลขที่ถูกต้อง")

    return selected_products

# ฟังก์ชันสำหรับบันทึกข้อมูลลงไฟล์
def save_data_to_txt(customer_data, selected_products):
    # สร้างชื่อไฟล์ที่ไม่ซ้ำโดยใช้วันที่และเวลา
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"./order/customer_data_{timestamp}.txt"
    
    with open(filename, 'w', encoding='utf-8') as file:
        # บันทึกข้อมูลลูกค้า
        file.write("ข้อมูลลูกค้า:\n")
        for key, value in customer_data.items():
            file.write(f"{key}: {value}\n")

        # บันทึกสินค้าที่ผู้ใช้เลือก
        file.write("\nสินค้าที่สั่งซื้อ:\n")
        for i, product in enumerate(selected_products, 1):
            file.write(f"{i}. {product}\n")

    print(f"\nข้อมูลถูกบันทึกในไฟล์: {filename}")

# เรียกใช้ฟังก์ชันเพื่อรับข้อมูลลูกค้าและเลือกสินค้า
customer_data = get_customer_data()
selected_products = select_products()

# บันทึกข้อมูลลูกค้าและสินค้าที่เลือกลงไฟล์
save_data_to_txt(customer_data, selected_products)
