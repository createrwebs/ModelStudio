import os
import json
import re

EN_DIR = 'src/i18n/en'
TH_DIR = 'src/i18n/th'

os.makedirs(TH_DIR, exist_ok=True)

# Comprehensive dictionary for phrases and words
TRANSLATIONS = {
    # Buttons
    "Login": "เข้าสู่ระบบ",
    "Logout": "ออกจากระบบ",
    "Sign in": "เข้าสู่ระบบ",
    "Sign up": "สมัครสมาชิก",
    "Register": "สมัครสมาชิก",
    "Start": "เริ่มต้น",
    "Setup": "ตั้งค่า",
    "Copy": "คัดลอก",
    "Copied": "คัดลอกแล้ว",
    "Regenerate": "สร้างใหม่",
    "Restart": "เริ่มใหม่",
    "Preview": "ดูตัวอย่าง",
    "View Original Image": "ดูรูปภาพต้นฉบับ",
    "View Video": "ดูวิดีโอ",
    "Edit": "แก้ไข",
    "New": "ใหม่",
    "Delete": "ลบ",
    "Confirm": "ยืนยัน",
    "Save": "บันทึก",
    "Saved": "บันทึกแล้ว",
    "Cancel": "ยกเลิก",
    "Close": "ปิด",
    "Send": "ส่ง",
    "Stop": "หยุด",
    "Open menu": "เปิดเมนู",
    "More actions": "การกระทำเพิ่มเติม",
    "Refresh": "รีเฟรช",
    "Try it now": "ทดลองใช้เลย",
    "See every capability": "ดูความสามารถทั้งหมด",
    "Think Deeper": "คิดเชิงลึก",
    "Deep Search": "ค้นหาเชิงลึก",
    "Search": "ค้นหา",
    "Edit Message": "แก้ไขข้อความ",
    "Explore": "สำรวจ",
    "Create Similar": "สร้างสรรค์ตามแบบนี้",
    "Generate": "สร้าง",
    "Submit": "ส่งข้อมูล",
    "Continue": "ดำเนินการต่อ",
    "Back": "ย้อนกลับ",
    "Apply": "นำไปใช้",
    "Reset": "รีเซ็ต",
    "Clear": "ล้าง",
    "Download": "ดาวน์โหลด",
    "Upload": "อัปโหลด",

    # Common terms
    "AI Chat": "แชทบอท AI",
    "AI Drawing": "วาดภาพด้วย AI",
    "AI Art QR Code": "คิวอาร์โค้ดศิลปะ AI",
    "AI Music": "สร้างเพลง AI",
    "AI Video": "สร้างวิดีโอ AI",
    "Customer Reviews": "รีวิวจากลูกค้า",
    "Our Services": "บริการของเรา",
    "Overview": "ภาพรวม",
    "Products": "ผลิตภัณฑ์",
    "Business": "สำหรับธุรกิจ",
    "Mobile App": "แอปมือถือ",
    "API Platform": "แพลตฟอร์ม API",
    "Support": "ช่วยเหลือและสนับสนุน",
    "Referral": "แนะนำเพื่อน",
    "Console": "คอนโซล",
    "Profile": "โปรไฟล์",
    "Settings": "การตั้งค่า",
    "General": "ทั่วไป",
    "Security": "ความปลอดภัย",
    "Account": "บัญชีผู้ใช้",
    "Credits": "เครดิต",
    "Credit": "เครดิต",
    "Balance": "ยอดคงเหลือ",
    "Quota": "โควต้า",
    "Tokens": "โทเคน",
    "Session": "เซสชัน",
    "Sessions": "เซสชันที่ใช้งาน",
    "Username": "ชื่อผู้ใช้",
    "Password": "รหัสผ่าน",
    "Email": "อีเมล",
    "Nickname": "ชื่อเล่น",
    "User ID": "รหัสผู้ใช้",
    "Registration Date": "วันที่ลงทะเบียน",
    "Thinking...": "กำลังคิดวิเคราะห์...",
    "Reasoning Process": "กระบวนการคิดและเหตุผล (Reasoning)",
    "Prompt": "พรอมต์ (Prompt)",
    "Negative Prompt": "พรอมต์เชิงลบ",
    "Parameters": "พารามิเตอร์",
    "Show More": "แสดงเพิ่มเติม",
    "Show Less": "แสดงน้อยลง",
    "Status": "สถานะ",
    "Success": "สำเร็จ",
    "Failed": "ล้มเหลว",
    "Error": "ข้อผิดพลาด",
    "Loading...": "กำลังโหลด...",
    "Online": "ออนไลน์",
    "Offline": "ออฟไลน์",
    "Active": "ใช้งานอยู่",
    "Expired": "หมดอายุ",

    # Hero and Titles
    "An all-in-one AI creation and business platform": "แพลตฟอร์ม AI อัจฉริยะ สร้างสรรค์ภาพ วิดีโอ เพลง และแชทบอทครบวงจร",
    "One account. Every major AI.": "บัญชีเดียว รวมทุกโมเดล AI ชั้นนำระดับโลก",
    "Chat, images, music, video, digital humans, search, and a coding assistant — all on one platform. No separate signups, no separate subscriptions.": "แชทบอท, สร้างภาพ, แต่งเพลง, วิดีโอ, มนุษย์ดิจิทัล, ระบบสืบค้น และผู้ช่วยเขียนโค้ด รวมไว้ในแพลตฟอร์มเดียว",
    "Frontier AI, ready for every idea": "พลัง AI รุ่นล่าสุด พร้อมเปลี่ยนทุกไอเดียของคุณให้เป็นจริง",
    "AI capabilities": "ความสามารถ AI",
    "Models to choose from": "โมเดลให้เลือกใช้งาน",
    "Available products": "ผลิตภัณฑ์ที่พร้อมใช้งาน",
    "Platforms you can connect": "แพลตฟอร์มที่เชื่อมต่อได้",
    "Every leading model, one place": "รวมทุกโมเดลชั้นนำไว้ในที่เดียว",
    "A world of intelligence, one conversation away": "โลกแห่งปัญญาประดิษฐ์ เริ่มต้นได้ในบทสนทนาเดียว",
    "Switch between ChatGPT, Claude, Gemini, Grok, DeepSeek, Kimi, and GLM at will — mid-conversation, without losing context.": "สลับเปลี่ยนระหว่าง ChatGPT, Claude, Gemini, Grok, DeepSeek, Kimi และ GLM ได้อย่างอิสระโดยไม่สูญเสียบริบท",
    
    # Placeholders & Alerts
    "Enter a prompt to continue": "กรุณากรอกพรอมต์เพื่อดำเนินการต่อ",
    "Enter a prompt or add the required media": "กรุณากรอกพรอมต์หรือเพิ่มไฟล์มีเดียที่ต้องการ",
    "Preview unavailable": "ไม่สามารถแสดงตัวอย่างได้",
    "An error occurred": "เกิดข้อผิดพลาดขึ้น",
    "The response stream ended before completion.": "การส่งข้อมูลสตรีมหยุดชะงักก่อนเสร็จสิ้น",
    "Type a message...": "พิมพ์ข้อความที่นี่...",
    "Search models...": "ค้นหาโมเดล...",
    "No messages yet": "ยังไม่มีข้อความ",
    "Start a new conversation": "เริ่มบทสนทนาใหม่",
    "Clear history": "ล้างประวัติการคุย",
    "Are you sure?": "คุณแน่ใจหรือไม่?",
    "Copied to clipboard": "คัดลอกไปยังคลิปบอร์ดแล้ว"
}

# Regex replacements for common patterns
REGEX_REPLACEMENTS = [
    (r'\bLogin\b', 'เข้าสู่ระบบ'),
    (r'\bLogout\b', 'ออกจากระบบ'),
    (r'\bSign in\b', 'เข้าสู่ระบบ'),
    (r'\bSign up\b', 'สมัครสมาชิก'),
    (r'\bRegister\b', 'สมัครสมาชิก'),
    (r'\bUsername\b', 'ชื่อผู้ใช้'),
    (r'\bPassword\b', 'รหัสผ่าน'),
    (r'\bConfirm\b', 'ยืนยัน'),
    (r'\bCancel\b', 'ยกเลิก'),
    (r'\bDelete\b', 'ลบ'),
    (r'\bEdit\b', 'แก้ไข'),
    (r'\bSave\b', 'บันทึก'),
    (r'\bRefresh\b', 'รีเฟรช'),
    (r'\bClose\b', 'ปิด'),
    (r'\bCopy\b', 'คัดลอก'),
    (r'\bCopied\b', 'คัดลอกแล้ว'),
    (r'\bDownload\b', 'ดาวน์โหลด'),
    (r'\bUpload\b', 'อัปโหลด'),
    (r'\bPrompt\b', 'พรอมต์'),
    (r'\bCredits?\b', 'เครดิต'),
    (r'\bBalance\b', 'ยอดคงเหลือ'),
    (r'\bQuota\b', 'โควต้า'),
    (r'\bTokens?\b', 'โทเคน'),
    (r'\bSessions?\b', 'เซสชัน'),
    (r'\bSuccess\b', 'สำเร็จ'),
    (r'\bFailed\b', 'ล้มเหลว'),
    (r'\bError\b', 'ข้อผิดพลาด'),
    (r'\bLoading\.\.\.\b', 'กำลังโหลด...'),
    (r'\bThinking\.\.\.\b', 'กำลังคิดวิเคราะห์...'),
    (r'\bReasoning Process\b', 'กระบวนการคิดและเหตุผล'),
    (r'\bAI Chat\b', 'แชทบอท AI'),
    (r'\bAI Drawing\b', 'วาดภาพด้วย AI'),
    (r'\bAI Music\b', 'สร้างเพลง AI'),
    (r'\bAI Video\b', 'สร้างวิดีโอ AI'),
    (r'\bGenerate\b', 'สร้าง'),
    (r'\bGenerating\.\.\.\b', 'กำลังสร้าง...'),
    (r'\bModel\b', 'โมเดล'),
    (r'\bModels\b', 'โมเดล'),
    (r'\bSettings\b', 'การตั้งค่า'),
    (r'\bProfile\b', 'โปรไฟล์'),
    (r'\bConsole\b', 'คอนโซล'),
    (r'\bOverview\b', 'ภาพรวม'),
    (r'\bProducts\b', 'ผลิตภัณฑ์'),
    (r'\bSupport\b', 'ช่วยเหลือ'),
    (r'\bDocumentation\b', 'เอกสารคู่มือ'),
    (r'\bAPI Key\b', 'คีย์ API'),
    (r'\bAPI Keys\b', 'คีย์ API'),
    (r'\bActive\b', 'ใช้งานอยู่'),
    (r'\bOnline\b', 'ออนไลน์'),
    (r'\bOffline\b', 'ออฟไลน์'),
]

def translate_text(text: str) -> str:
    if not isinstance(text, str) or not text.strip():
        return text
    
    # Exact match
    trimmed = text.strip()
    if trimmed in TRANSLATIONS:
        return TRANSLATIONS[trimmed]
    
    # If starting with something standard
    res = text
    for eng, th in TRANSLATIONS.items():
        if len(eng) > 10 and eng in res:
            res = res.replace(eng, th)
            
    # Pattern substitutions
    for pat, rep in REGEX_REPLACEMENTS:
        res = re.sub(pat, rep, res, flags=re.IGNORECASE)
        
    return res

for filename in os.listdir(EN_DIR):
    if not filename.endswith('.json'):
        continue
    en_path = os.path.join(EN_DIR, filename)
    th_path = os.path.join(TH_DIR, filename)
    
    with open(en_path, 'r', encoding='utf-8') as f:
        try:
            data = json.load(f)
        except Exception as e:
            print(f"Error loading {en_path}: {e}")
            continue
            
    th_data = {}
    for key, val in data.items():
        if isinstance(val, dict):
            msg = val.get('message', '')
            desc = val.get('description', '')
            th_msg = translate_text(msg)
            th_data[key] = {
                'message': th_msg,
                'description': desc
            }
        elif isinstance(val, str):
            th_data[key] = translate_text(val)
        else:
            th_data[key] = val
            
    with open(th_path, 'w', encoding='utf-8') as f:
        json.dump(th_data, f, ensure_ascii=False, indent=2)

print(f"Successfully generated {len(os.listdir(TH_DIR))} Thai i18n files in {TH_DIR}")
