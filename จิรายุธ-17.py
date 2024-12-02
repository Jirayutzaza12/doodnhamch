province = [
    "กรุงเทพมหานคร", "กาฬสินธุ์", "กาญจนบุรี", "จันทบุรี", 
    "ฉะเชิงเทรา", "ชลบุรี", "มะเยา", "ชุมพร", 
    "ชัยนาท", "ขอนแก่น", "ชัยภูมิ", "ยโสธร", 
    "นครพนม", "นครราชสีมา", "เชียงใหม่"
]

# 1. เปลี่ยน "กรุงเทพมหานคร" เป็น "Bangkok"
province[province.index("กรุงเทพมหานคร")] = "Bangkok"

# 2. เปลี่ยน "นครราชสีมา" เป็น "Korat"
province[province.index("นครราชสีมา")] = "Korat"

# 3. เปลี่ยน "ฉะเชิงเทรา" เป็น "Paet Riw"
province[province.index("ฉะเชิงเทรา")] = "Paet Riw"

# 4. เปลี่ยน "ชลบุรี" เป็น "Chon buri"
province[province.index("ชลบุรี")] = "Chon buri"

# 5. เปลี่ยน "ชุมพร" เป็น "Chum porn"
province[province.index("ชุมพร")] = "Chum porn"

# แสดงผลลัพธ์
print(province)
