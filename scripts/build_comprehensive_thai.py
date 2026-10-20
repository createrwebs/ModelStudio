#!/usr/bin/env python3
"""
Comprehensive Thai i18n builder for Nexior/Tora AI Studio.
Translates remaining English keys into professional, natural Thai terminology.
"""
import os
import json
import re

I18N_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../src/i18n'))
TH_DIR = os.path.join(I18N_DIR, 'th')
EN_DIR = os.path.join(I18N_DIR, 'en')

def has_thai(text):
    return bool(re.search(r'[\u0e00-\u0e7f]', str(text)))

# Comprehensive dictionary for common and technical UI terms
TRANSLATIONS = {
    # Actions & Buttons
    "Create now": "สร้างสรรค์ทันที",
    "Turn an idea into a cinematic moment": "เปลี่ยนไอเดียให้กลายเป็นภาพยนตร์เสมือนจริง",
    "Text, images, and references become shots in a polished, cinematic short.": "ข้อความ รูปภาพ และข้อมูลอ้างอิง จะถูกสร้างเป็นวิดีโอซีนระดับภาพยนตร์",
    "AI images": "สร้างภาพ AI",
    "Start creating from a single description": "เริ่มต้นสร้างภาพสวยจากคำบรรยายสั้นๆ",
    "สร้าง, แก้ไข, expand, and restyle until the picture matches the one in your head.": "สร้าง แก้ไข ขยายภาพ และปรับแต่งสไตล์จนตรงใจกับจินตนาการของคุณ",
    "Complete production": "สร้างสรรค์ครบวงจร",
    "Give AI a topic. Get a finished video.": "บอกแค่หัวข้อ ได้คลิปวิดีโอฉบับสมบูรณ์ทันที",
    "Script, visuals, voiceover, captions, and music come together automatically.": "ทั้งบท ภาพ เสียงพากย์ คำบรรยาย และเพลงประกอบ จะถูกสร้างอัตโนมัติอย่างลงตัว",
    "Quick start": "เริ่มต้นด่วน",
    "What do you want to create today?": "วันนี้คุณต้องการสร้างสรรค์อะไร?",
    "Start with your goal instead of researching โมเดล first.": "เริ่มต้นจากสิ่งที่คุณต้องการสร้าง แทนที่จะต้องเสียเวลาค้นหาชื่อโมเดล",
    "Chat with AI": "แชทและสนทนากับ AI",
    "Write, analyze, learn, and develop ideas": "เขียนบทความ วิเคราะห์ข้อมูล เรียนรู้ และต่อยอดไอเดีย",
    "Create an image": "สร้างรูปภาพ AI",
    "Posters, product shots, characters, and design": "โปสเตอร์ ภาพถ่ายสินค้า ตัวละคร และงานออกแบบ 3D",
    "Create a song": "แต่งเพลงและเสียงดนตรี",
    "From style and lyrics to a complete track": "ตั้งแต่เลือกสไตล์และแต่งเนื้อร้อง สู่เพลงฉบับสมบูรณ์",
    "Make a video": "สร้างวิดีโอ AI",
    "Short clips, animations, and cinematic scenes": "คลิปสั้น แอนิเมชัน และวิดีโอระดับภาพยนตร์",
    "Explore": "สำรวจเครื่องมือ",
    "Close": "ปิด",
    "See every capability": "ดูเครื่องมือ AI ทั้งหมด",
    "Try it now": "ทดลองใช้งานทันที",
    "Every capability": "ครบทุกฟีเจอร์ AI",
    "One account. Every major AI.": "บัญชีเดียว รวมทุก AI ชั้นนำระดับโลก",
    "Chat, images, music, video, digital humans, search, and a coding assistant — all on one platform. No separate signups, no separate subscriptions.": "แชท รูปภาพ ดนตรี วิดีโอ มนุษย์ดิจิทัล ค้นหา และเขียนโค้ด ครบครันในแพลตฟอร์มเดียว ไม่ต้องสมัครหรือจ่ายแยกหลายบริการ",
    "Frontier AI, ready for every idea": "สุดยอด AI ระดับแถวหน้า พร้อมสำหรับทุกไอเดียของคุณ",
    "From intelligent conversation to visual creation, music, video, and productivity — every capability shown here is ready when inspiration strikes.": "ตั้งแต่การสนทนาอัจฉริยะ งานภาพ ดนตรี วิดีโอ ไปจนถึงการเพิ่มผลผลิต ทุกความสามารถพร้อมใช้งานทันทีเมื่อเกิดแรงบันดาลใจ",
    "AI capabilities": "ความสามารถ AI",
    "Models to choose from": "โมเดลให้เลือกใช้งาน",
    "Available products": "ผลิตภัณฑ์ที่พร้อมใช้งาน",
    "Featured creative recommendations": "ผลงานสร้างสรรค์แนะนำ",
    "Previous recommendation": "คำแนะนำก่อนหน้า",
    "Next recommendation": "คำแนะนำถัดไป",
    "Back to top": "กลับขึ้นด้านบน",
    "Load more": "โหลดเพิ่มเติม",
    "Image": "สร้างภาพ AI",
    "Music": "สร้างเพลง & เสียง AI",
    "Video": "สร้างวิดีโอ AI",
    "Chat": "แชท AI",
    "Prompt Library": "คลังพร้อมต์ AI",
    "Active Sessions": "เซสชันที่ใช้งาน",
    "Sync Quota": "รีเฟรชเครดิต",
    "Console": "คอนโซลจัดการ",
    "Login": "เข้าสู่ระบบ",
    "Logout": "ออกจากระบบ",
    "Register": "สมัครสมาชิก",
    "API Key": "ใส่ API Key",
    "Use Prompt": "ใช้ Prompt นี้",
    "Copy": "คัดลอก",
    "Copied": "คัดลอกแล้ว",
    "Generate": "สร้างผลงาน",
    "Generating": "กำลังสร้าง...",
    "Task ID": "รหัสงาน (Task ID)",
    "Task": "งาน",
    "Status": "สถานะ",
    "Created At": "สร้างเมื่อ",
    "Duration": "ความยาว",
    "Ratio": "สัดส่วนภาพ",
    "Resolution": "ความละเอียด",
    "Quality": "คุณภาพ",
    "Standard": "มาตรฐาน",
    "High Definition": "ความคมชัดสูง (HD)",
    "Ultra High": "ความคมชัดระดับสูงพิเศษ",
    "Download": "ดาวน์โหลด",
    "Share": "แชร์",
    "Delete": "ลบ",
    "Cancel": "ยกเลิก",
    "Confirm": "ยืนยัน",
    "Save": "บันทึก",
    "Search": "ค้นหา",
    "All": "ทั้งหมด",
    "Recent": "ล่าสุด",
    "History": "ประวัติการสร้าง",
    "Settings": "การตั้งค่า",
    "General": "ทั่วไป",
    "Advanced": "ขั้นสูง",
    "Custom": "กำหนดเอง",
    "Success": "สำเร็จ",
    "Failed": "ล้มเหลว",
    "Pending": "รอดำเนินการ",
    "Processing": "กำลังประมวลผล",
    "First Frame": "ภาพเฟรมแรก (First Frame)",
    "Last Frame": "ภาพเฟรมท้าย (Last Frame)",
    "Reference Image": "รูปภาพอ้างอิง",
    "Reference Audio": "เสียงอ้างอิง",
    "Prompt": "พร้อมต์ (Prompt)",
    "Negative Prompt": "พร้อมต์เชิงลบ (Negative Prompt)",
    "Enter a prompt": "กรุณาใส่คำบรรยายพร้อมต์...",
    "Enter negative prompt": "ใส่สิ่งที่ไม่ต้องการให้ปรากฏ...",
    "Upload": "อัปโหลด",
    "Upload Image": "อัปโหลดรูปภาพ",
    "Upload Video": "อัปโหลดวิดีโอ",
    "Upload Audio": "อัปโหลดไฟล์เสียง",
    "Motion": "การเคลื่อนไหว",
    "Camera": "มุมกล้อง",
    "Speed": "ความเร็ว",
    "Style": "สไตล์",
    "Cute": "น่ารัก",
    "Expressive": "แสดงออกอารมณ์สูง",
    "Original": "ต้นฉบับดั้งเดิม",
    "Photorealistic": "ภาพถ่ายสมจริง",
    "Anime": "อนิเมะ",
    "Cinematic": "ระดับภาพยนตร์",
    "Fantasy": "แฟนตาซี",
    "Cyberpunk": "ไซเบอร์พังก์",
    "Architecture": "สถาปัตยกรรม",
    "Voice": "เสียงพากย์",
    "Instrumental": "ดนตรีบรรเลง (ไม่มีเสียงร้อง)",
    "Lyrics": "เนื้อเพลง",
    "Title": "ชื่อเรื่อง / หัวข้อ",
    "Description": "คำอธิบาย",
    "Model": "โมเดล",
    "Version": "เวอร์ชัน",
    "Mode": "โหมด",
    "Fast Mode": "โหมดเร็ว (Fast)",
    "Relax Mode": "โหมดประหยัด (Relax)",
    "Turbo Mode": "โหมดเทอร์โบ (Turbo)",
    "Credits": "เครดิต",
    "Balance": "ยอดเงินคงเหลือ",
    "Price": "ราคา",
    "Free": "ฟรี",
    "Unlimited": "ไม่จำกัด"
}

def translate_phrase(text):
    if not text or not isinstance(text, str):
        return text
    if has_thai(text):
        return text
    
    # Direct match
    if text in TRANSLATIONS:
        return TRANSLATIONS[text]
    
    # Strip whitespace
    stripped = text.strip()
    if stripped in TRANSLATIONS:
        return TRANSLATIONS[stripped]
        
    return text

print("Comprehensive translation loaded.")
