import os
import requests

# ดึงค่าจาก Environment Variables (GitHub Secrets)
TELEGRAM_TOKEN = os.environ.get('TELEGRAM_TOKEN')
TELEGRAM_CHAT_ID = os.environ.get('TELEGRAM_CHAT_ID')
IMAGE_PATH = '491527.jpg'  # อ้างอิงชื่อไฟล์ใน Repo โดยตรง

def send_telegram_photo():
    if not TELEGRAM_TOKEN or not TELEGRAM_CHAT_ID:
        print("Error: ไม่พบค่า TELEGRAM_TOKEN หรือ TELEGRAM_CHAT_ID ใน Secrets")
        return

    if not os.path.exists(IMAGE_PATH):
        print(f"Error: ไม่พบไฟล์รูปภาพ {IMAGE_PATH} ใน Repository")
        return

    caption = """🧭✨ *สิทธิประโยชน์ที่สมาชิก COMPASS จะได้รับ*

เพราะเราเชื่อว่าการเทรดที่ดี ต้องมีทั้งแนวทาง กลยุทธ์ และการบริหารความเสี่ยงที่เหมาะสม

📊 *เลือกระดับ Signal Room ให้เหมาะกับพอร์ตของคุณ*

🔹 *COMPASS START — 100 USD*
เทรด M5 เน้นการเทรดระยะสั้น

🔹 *COMPASS PRO — 500 USD*
จุดเข้าตามแผน เป้าหมาย 1,000 จุด

🔹 *COMPASS ELITE — 1,000 USD*
จุดเข้าตามโครงสร้างตลาด พร้อมแนวทางวางแผนการเทรด

👑 *COMPASS — เข็มทิศเทรดเดอร์*
เติบโตไปด้วยกัน เรียนรู้และพัฒนาทักษะอย่างเป็นระบบ

📩 *สนใจเข้าร่วม* ติดต่อสอบถามรายละเอียดเพิ่มเติมกับ Admin ได้เลย

⚠️ _เงื่อนไขเป็นไปตามที่บริษัทกำหนด_
_การลงทุนมีความเสี่ยง ผู้ลงทุนควรศึกษาข้อมูลและทำความเข้าใจก่อนตัดสินใจ ผลกำไรไม่สามารถรับประกันได้_"""

    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendPhoto"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "caption": caption,
        "parse_mode": "Markdown"
    }

    try:
        with open(IMAGE_PATH, 'rb') as photo_file:
            response = requests.post(url, data=payload, files={'photo': photo_file})
            response.raise_for_status()
            print("ส่งรูปภาพและประกาศสำเร็จเรียบร้อย!")
    except requests.exceptions.HTTPError as err:
        print(f"HTTP Error: {err} - รายละเอียด: {response.text}")
    except Exception as e:
        print(f"Failed: {e}")

if __name__ == "__main__":
    send_telegram_photo()
