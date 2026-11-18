import os
import requests

# ดึงค่าจาก Secrets ตามชื่อตัวแปรของคุณ
TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
raw_chat_ids = os.environ.get("TELEGRAM_CHAT_ID", "")
CHAT_IDS = [cid.strip() for cid in raw_chat_ids.split(",") if cid.strip()]

IMAGE_PATH = "491527.jpg"

CAPTION_TEXT = """🧭✨ สิทธิประโยชน์ที่สมาชิก COMPASS จะได้รับ

เพราะเราเชื่อว่าการเทรดที่ดี ต้องมีทั้งแนวทาง กลยุทธ์ และการบริหารความเสี่ยงที่เหมาะสม

📊 เลือกระดับ Signal Room ให้เหมาะกับพอร์ตของคุณ

🔹 COMPASS START — 100 USD
เทรด M5 เน้นการเทรดระยะสั้น

🔹 COMPASS PRO — 500 USD
จุดเข้าตามแผน เป้าหมาย 1,000 จุด

🔹 COMPASS ELITE — 1,000 USD
จุดเข้าตามโครงสร้างตลาด พร้อมแนวทางวางแผนการเทรด

👑 COMPASS — เข็มทิศเทรดเดอร์
เติบโตไปด้วยกัน เรียนรู้และพัฒนาทักษะอย่างเป็นระบบ

📩 สนใจเข้าร่วม ติดต่อสอบถามรายละเอียดเพิ่มเติมกับ Admin ได้เลย

⚠️ เงื่อนไขเป็นไปตามที่บริษัทกำหนด
การลงทุนมีความเสี่ยง ผู้ลงทุนควรศึกษาข้อมูลและทำความเข้าใจก่อนตัดสินใจ ผลกำไรไม่สามารถรับประกันได้"""


def send_telegram_photo():
  if not TELEGRAM_TOKEN or not CHAT_IDS:
    print("❌ ไม่พบค่า TELEGRAM_TOKEN หรือ TELEGRAM_CHAT_ID ใน Secrets")
    return

  url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendPhoto"

  try:
    with open(IMAGE_PATH, "rb") as image_file:
      for chat_id in CHAT_IDS:
        # รีเซ็ตตำแหน่งการอ่านไฟล์รูปใหม่ทุกครั้งที่วนลูปส่งห้องถัดไป
        image_file.seek(0)

        files = {"photo": image_file}
        data = {"chat_id": chat_id, "caption": CAPTION_TEXT}
        response = requests.post(url, files=files, data=data)
        result = response.json()

        if result.get("ok"):
          print(f"✅ ส่งรูปภาพเข้าห้อง {chat_id} สำเร็จ!")
        else:
          print(f"❌ ส่งเข้าห้อง {chat_id} ไม่สำเร็จ: {result.get('description')}")

  except FileNotFoundError:
    print(f"❌ ไม่พบไฟล์รูปภาพ '{IMAGE_PATH}' กรุณาอัปโหลดไฟล์ขึ้น GitHub ด้วย")
  except Exception as e:
    print(f"❌ เกิดข้อผิดพลาด: {e}")


if __name__ == "__main__":
  send_telegram_photo()
