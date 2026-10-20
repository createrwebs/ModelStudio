#!/usr/bin/env python3
"""
Comprehensive Thai Translation Generator for Nexior / Tora AI Studio.
Translates all untranslated strings in src/i18n/th/*.json using both
English and Chinese source files as references, preserving all parameter placeholders.
"""

import os
import glob
import json
import re

I18N_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../src/i18n'))
TH_DIR = os.path.join(I18N_DIR, 'th')
EN_DIR = os.path.join(I18N_DIR, 'en')
ZH_DIR = os.path.join(I18N_DIR, 'zh-CN')

THAI_CHAR_REGEX = re.compile(r'[\u0E00-\u0E7F]')

def has_thai(text: str) -> bool:
    if not text or not isinstance(text, str):
        return False
    return bool(THAI_CHAR_REGEX.search(text))

# Direct exact translation dictionary (supports matching against either EN or ZH)
EXACT_TRANSLATIONS = {
    # Common UI & Actions
    "Please select...": "กรุณาเลือก...",
    "Pending": "รอดำเนินการ",
    "Trace ID": "Trace ID",
    "Task ID": "รหัสงาน (Task ID)",
    "Failure Reason": "สาเหตุข้อผิดพลาด",
    "Elapsed Time": "เวลาที่ใช้ไป",
    "Starting task...": "กำลังเริ่มงาน...",
    "Processing": "กำลังประมวลผล...",
    "Select": "เลือก",
    "Type": "ประเภท",
    "All": "ทั้งหมด",
    "Created At": "สร้างเมื่อ",
    "Failure": "ล้มเหลว",
    "Failed": "ล้มเหลว",
    "Generating...": "กำลังสร้าง...",
    "No available operations": "ไม่มีการดำเนินการที่ใช้ได้",
    "Aspect Ratio": "อัตราส่วนภาพ",
    "Duration": "ความยาว/ระยะเวลา",
    "Name": "ชื่อ",
    "Connected": "เชื่อมต่อแล้ว",
    "Task initiated successfully": "เริ่มสร้างงานสำเร็จ",
    "Task initiation failed, please contact the administrator": "เริ่มงานไม่สำเร็จ กรุณาติดต่อผู้ดูแลระบบ",
    "Uploaded file must be in MP4 format!": "ไฟล์ที่อัปโหลดต้องเป็นรูปแบบ MP4 เท่านั้น!",
    "Reference Images": "รูปภาพอ้างอิง",
    "Free": "ฟรี",
    "Actions": "การกระทำ",
    "Image uploaded successfully": "อัปโหลดรูปภาพสำเร็จ",
    "Resolution": "ความละเอียด",
    "Square": "สี่เหลี่ยมจัตุรัส",
    "Custom": "กำหนดเอง",
    "Disabled": "ปิดใช้งาน",
    "Description": "คำอธิบาย",
    "Settings": "การตั้งค่า",
    "Cancel": "ยกเลิก",
    "Confirm": "ยืนยัน",
    "Save": "บันทึก",
    "Delete": "ลบ",
    "Edit": "แก้ไข",
    "Copy": "คัดลอก",
    "Copied": "คัดลอกแล้ว",
    "Search": "ค้นหา",
    "Refresh": "รีเฟรช",
    "Download": "ดาวน์โหลด",
    "Download Video": "ดาวน์โหลดวิดีโอ",
    "Download Image": "ดาวน์โหลดรูปภาพ",
    "Share": "แชร์",
    "Back": "ย้อนกลับ",
    "Close": "ปิด",
    "Clear": "ล้าง",
    "Clear All": "ล้างทั้งหมด",
    "Reset": "รีเซ็ต",
    "Submit": "ส่งข้อมูล",
    "Retry": "ลองใหม่อีกครั้ง",
    "Upload": "อัปโหลด",
    "Audio": "เสียง",
    "Video": "วิดีโอ",
    "Image": "รูปภาพ",
    "Text": "ข้อความ",
    "File": "ไฟล์",
    "Link": "ลิงก์",
    "Status": "สถานะ",
    "Success": "สำเร็จ",
    "Error": "ข้อผิดพลาด",
    "Warning": "คำเตือน",
    "Info": "ข้อมูล",
    "General": "ทั่วไป",
    "Advanced": "ขั้นสูง",
    "Advanced Parameters": "พารามิเตอร์ขั้นสูง",
    "Parameters": "พารามิเตอร์",
    "Standard": "มาตรฐาน",
    "High Definition": "ความคมชัดสูง (HD)",
    "Ultra High": "คมชัดพิเศษ (Ultra High)",
    "Mode": "โหมด",
    "Quality": "คุณภาพ",
    "Version": "เวอร์ชัน",
    "Speed": "ความเร็ว",
    "Model": "โมเดล",
    "Credits": "เครดิต",
    "Balance": "ยอดคงเหลือ",
    "History": "ประวัติ",
    "Recent": "ล่าสุด",
    "Favorites": "รายการโปรด",
    "Current Tasks": "งานปัจจุบัน",
    "Gallery": "แกลเลอรี",
    "Inspiration": "ไอเดียและแรงบันดาลใจ",
    "Prompt": "พรอมต์ (Prompt)",
    "Negative Prompt": "พรอมต์เชิงลบ (Negative Prompt)",
    "Seed": "Seed",
    "Steps": "จำนวนขั้นตอน (Steps)",

    # Midjourney & Image terms
    "Image Generation": "สร้างรูปภาพ",
    "Video Generation": "สร้างวิดีโอ",
    "Motion Control": "ควบคุมการเคลื่อนไหว",
    "Camera Movement": "การเคลื่อนที่ของกล้อง",
    "Character Reference Image": "รูปภาพอ้างอิงตัวละคร",
    "Motion Reference Video": "วิดีโออ้างอิงการเคลื่อนไหว",
    "Additional Prompt (Optional)": "พรอมต์เพิ่มเติม (ไม่บังคับ)",
    "Character Orientation": "ทิศทางการหันของตัวละคร",
    "Follow Image": "ตามรูปภาพ",
    "Follow Video": "ตามวิดีโอ",
    "Keep Original Sound": "เก็บเสียงต้นฉบับไว้",
    "First Frame": "เฟรมแรก",
    "Last Frame": "เฟรมสุดท้าย",
    "Start Image": "ภาพเริ่มต้น",
    "End Image": "ภาพสิ้นสุด",
    "Video Duration": "ความยาววิดีโอ",
    "Video Mode": "โหมดวิดีโอ",
    "Video Ratio": "อัตราส่วนวิดีโอ",
    "Extend Video": "ขยายความยาววิดีโอ",
    "Loop Video": "เล่นวิดีโอวนซ้ำ",
    "Prompt Enhancement": "เพิ่มประสิทธิภาพพรอมต์",
    "Custom Video": "วิดีโอกำหนดเอง",

    # Music & Audio terms
    "Voice Management": "จัดการเสียง",
    "Manage Voices": "จัดการเสียง",
    "Create Voice": "สร้างเสียงใหม่",
    "Create New Voice": "สร้างเสียงใหม่",
    "Give your voice a name...": "ตั้งชื่อเสียงของคุณ...",
    "Describe the features of this voice...": "อธิบายลักษณะหรือจุดเด่นของเสียงนี้...",
    "Source Type": "ประเภทแหล่งที่มา",
    "Create from Song": "สร้างจากบทเพลง",
    "Upload Audio Clone": "อัปโหลดไฟล์เสียงเพื่อโคลน",
    "Song ID": "รหัสเพลง (Song ID)",
    "Enter Song ID...": "กรอกรหัสเพลง...",
    "Audio URL": "URL ไฟล์เสียง",
    "Enter Audio File URL...": "กรอก URL ของไฟล์เสียง...",
    "Song Description": "คำอธิบายเพลง / สไตล์ดนตรี",
    "Describe the music you want, e.g., a warm folk song about autumn nostalgia...": "อธิบายดนตรีที่ต้องการ เช่น เพลงโฟล์กอบอุ่น เมโลดี้กีตาร์โปร่ง...",
    "Instrumental": "ดนตรีบรรเลง (ไม่มีเสียงร้อง)",
    "Simple": "โหมดเริ่มต้น",
    "Custom Mode": "โหมดกำหนดเอง",
    "Lyrics": "เนื้อเพลง",
    "Enter lyrics...": "ใส่เนื้อร้องที่ต้องการ...",
    "Style of Music": "แนวเพลง / สไตล์ดนตรี",
    "Enter music style, e.g., Acoustic pop, upbeat piano...": "ระบุแนวเพลง เช่น Acoustic pop, upbeat piano...",
    "Title": "ชื่อเพลง",
    "Enter song title...": "ตั้งชื่อเพลงของคุณ...",
    "Extend Audio": "ต่อความยาวเพลง",
    "Vocal Separation": "แยกเสียงร้อง / ดนตรี",
    "Reference Music": "เพลงอ้างอิง",

    # Chat & Reasoning
    "Thinking...": "กำลังคิดวิเคราะห์...",
    "Reasoning Process": "กระบวนการคิดและเหตุผล (Reasoning)",
    "Think Deeper": "คิดเชิงลึก",
    "Deep Search": "ค้นหาเชิงลึก",
    "Edit Message": "แก้ไขข้อความ",
    "Start new conversation": "เริ่มบทสนทนาใหม่",
    "Please enter your question...": "พิมพ์คำถามหรือข้อความของคุณที่นี่...",
    "AI may make mistakes, please verify important information.": "AI อาจให้ข้อมูลคลาดเคลื่อนได้ กรุณาตรวจสอบข้อมูลสำคัญอีกครั้ง",
    "Stop Generating": "หยุดสร้างข้อความ",
    "Regenerate": "สร้างใหม่อีกครั้ง",
    "Clear Context": "ล้างประวัติบริบท",
    "Copy Code": "คัดลอกโค้ด",
    "Copy Message": "คัดลอกข้อความ",
    "Pin Message": "ปักหมุดข้อความ",
    "Fork Conversation": "แยกสายการสนทนา",
    "System Prompt": "คำสั่งระบบ (System Prompt)",
    "Temperature": "ความสร้างสรรค์ (Temperature)",
    "Top P": "Top P",
    "Max Tokens": "จำนวนโทเค็นสูงสุด (Max Tokens)",
    "Web Search": "ค้นหาบนอินเทอร์เน็ต",
    "Artifacts": "สิ่งประดิษฐ์และไฟล์โค้ด (Artifacts)",

    # Chinese phrase mapping for accurate fallback
    "视频生成": "สร้างวิดีโอ",
    "动作控制": "ควบคุมการเคลื่อนไหว",
    "人物参考图片": "รูปภาพอ้างอิงตัวละคร",
    "动作参考视频": "วิดีโออ้างอิงการเคลื่อนไหว",
    "补充提示词（可选）": "พรอมต์เพิ่มเติม (ไม่บังคับ)",
    "人物朝向": "ทิศทางการหันของตัวละคร",
    "跟随图片": "ตามรูปภาพ",
    "跟随视频": "ตามวิดีโอ",
    "保留原声": "เก็บเสียงต้นฉบับไว้",
    "声音管理": "จัดการเสียง",
    "管理声音": "จัดการเสียง",
    "创建声音": "สร้างเสียงใหม่",
    "创建新声音": "สร้างเสียงใหม่",
    "名称": "ชื่อ",
    "为声音取个名称...": "ตั้งชื่อเสียงของคุณ...",
    "描述": "คำอธิบาย",
    "描述这个声音的特点...": "อธิบายลักษณะของเสียงนี้...",
    "来源类型": "ประเภทแหล่งที่มา",
    "从歌曲创建": "สร้างจากบทเพลง",
    "上传音频克隆": "อัปโหลดไฟล์เสียงเพื่อโคลน",
    "歌曲 ID": "รหัสเพลง (Song ID)",
    "输入歌曲 ID...": "กรอกรหัสเพลง...",
    "音频 URL": "URL ไฟล์เสียง",
    "输入音频文件 URL...": "กรอก URL ของไฟล์เสียง...",
    "图像生成": "สร้างรูปภาพ",
    "纯音乐": "ดนตรีบรรเลง",
    "歌词": "เนื้อเพลง",
    "音乐风格": "แนวเพลง / สไตล์ดนตรี",
    "歌曲标题": "ชื่อเพลง",
    "灵感与预设": "ไอเดียและพรีเซ็ต",
    "灵感": "ไอเดียสร้างสรรค์",
    "移除此预设": "นำพรีเซ็ตนี้ออก",
    "暂无可用预设": "ยังไม่มีพรีเซ็ต",
    "已选 {count} 项": "เลือกแล้ว {count} รายการ",
    "请输入提示词": "กรุณาใส่พรอมต์ (Prompt)",
    "请输入提示词或添加所需素材": "กรุณาใส่พรอมต์หรืออัปโหลดรูปภาพ/วิดีโอที่จำเป็น",
    "预览不可用": "ไม่สามารถแสดงตัวอย่างได้",
    "设置": "การตั้งค่า",
    "开始": "เริ่มต้น",
    "复制": "คัดลอก",
    "已复制": "คัดลอกแล้ว",
    "重新生成": "สร้างใหม่อีกครั้ง",
    "清空": "ล้างข้อมูล",
    "全部": "ทั้งหมด",
    "类型": "ประเภท",
    "状态": "สถานะ",
    "成功": "สำเร็จ",
    "失败": "ล้มเหลว",
    "删除": "ลบ",
    "确定": "ยืนยัน",
    "取消": "ยกเลิก",
    "保存": "บันทึก",
    "编辑": "แก้ไข",
    "下载": "ดาวน์โหลด",
    "分享": "แชร์",
    "搜索": "ค้นหา",
    "刷新": "รีเฟรช",
    "上传": "อัปโหลด",
    "未命名": "ไม่มีชื่อ",
    "自定义": "กำหนดเอง",
    "高级": "ขั้นสูง",
    "普通": "ทั่วไป",
    "标准": "มาตรฐาน",
    "高清": "ความคมชัดสูง (HD)",
    "超清": "คมชัดพิเศษ (Ultra HD)",
    "已连接": "เชื่อมต่อแล้ว",
    "未连接": "ยังไม่เชื่อมต่อ",
    "免费": "ฟรี",
    "额度": "โควต้า",
    "积分": "เครดิต",
    "点数": "คะแนน",
    "余额": "ยอดคงเหลือ",
    "订单": "คำสั่งซื้อ",
    "充值": "เติมเครดิต",
    "支付": "ชำระเงิน",
    "价格": "ราคา",
    "数量": "จำนวน",
    "操作": "การกระทำ",
    "操作成功": "ดำเนินการสำเร็จ",
    "操作失败": "ดำเนินการล้มเหลว",
    "网络错误": "เกิดข้อผิดพลาดในการเชื่อมต่อเครือข่าย",
    "请稍后重试": "กรุณาลองใหม่อีกครั้งภายหลัง",
    "暂无数据": "ไม่มีข้อมูล",
    "暂无历史记录": "ไม่มีประวัติการใช้งาน",
    "加载中...": "กำลังโหลด...",
    "生成中...": "กำลังสร้าง...",
    "处理中...": "กำลังประมวลผล...",
    "排队中...": "กำลังรอคิว..."
}

# Style tag translations for Midjourney / Art
STYLE_TAGS = {
    "Infographic Drawing": "ภาพวาดอินโฟกราฟิก",
    "Double Exposure": "ภาพถ่ายซ้อนสองชั้น (Double Exposure)",
    "Diagrammatic Drawing": "ภาพวาดแผนผังไดอะแกรม",
    "2D Illustration": "ภาพวาดประกอบ 2D",
    "Diagrammatic Portrait": "ภาพพอร์ตเทรตไดอะแกรม",
    "Pixel Art": "พิกเซลอาร์ต (Pixel Art)",
    "Dark Fantasy": "ดาร์กแฟนตาซี (Dark Fantasy)",
    "Ukiyo-e Art": "ภาพพิมพ์อุกิโยะเอะ (Ukiyo-e)",
    "Paper Quilling": "ศิลปะม้วนกระดาษ (Paper Quilling)",
    "Paper Cutting Craft": "ศิลปะตัดกระดาษ (Paper Cutting)",
    "Iridescent": "ประกายเหลือบสีรุ้ง (Iridescent)",
    "Patchwork Collage": "ภาพปะติดปะต่อ (Collage)",
    "Op Art": "ศิลปะภาพลวงตา (Op Art)",
    "Japanese Ink Painting": "ภาพวาดหมึกจีน/ญี่ปุ่น (Ink Painting)",
    "Pastel Drawing": "ภาพวาดสีชอล์กพาสเทล",
    "Dripping Art": "ศิลปะหยดสี (Dripping Art)",
    "Tattoo Art": "ลายสักศิลปะ (Tattoo Art)",
    "16-Bit": "กราฟิก 16-บิต",
    "8-Bit": "กราฟิก 8-บิต ย้อนยุค",
    "Amber": "สีอำพันอบอุ่น",
    "Anatomical Drawing": "ภาพวาดกายวิภาคศาสตร์",
    "Ancient": "โบราณย้อนยุค",
    "Anime": "ลายเส้นอนิเมะญี่ปุ่น",
    "Arabic": "ศิลปะอาหรับ",
    "Blocky": "บล็อก 3 มิติ (Voxel)",
    "Blueprint": "พิมพ์เขียวสถาปัตยกรรม",
    "Comic Book": "คอมิกการ์ตูนฝรั่ง",
    "Caribbean": "สไตล์แคริบเบียน",
    "Celestial": "ดวงดาวและจักรวาล (Celestial)",
    "Cellulose": "เนื้อเยื่อเซลลูโลส",
    "Charcoal Style": "ภาพสเก็ตช์ถ่านชาร์โคล",
    "Chromatic": "สีสันสดใสจัดจ้าน (Chromatic)",
    "Coral": "สีปะการังธรรมชาติ",
    "Concept Art": "คอนเซ็ปต์อาร์ต (Concept Art)",
    "Fibonacci": "สัดส่วนทองคำฟีโบนักชี",
    "Cyberpunk": "ไซเบอร์พังก์ (Cyberpunk)",
    "Diabolic": "ปีศาจลึกลับ",
    "Diffraction Grading": "การเลี้ยวเบนของแสง",
    "Lightspeed": "ความเร็วแสงเรืองรอง",
    "Liquid": "ของเหลวเคลื่อนไหว (Liquid)",
    "Retro": "เรโทรย้อนยุค",
    "Vintage": "วินเทจคลาสสิก",
    "Minimalist": "มินิมอลเรียบหรู",
    "Surrealism": "สัจนิยมเหนือจริง (Surrealism)",
    "Impressionism": "อิมเพรสชันนิสม์",
    "Watercolor": "สีน้ำชวนฝัน (Watercolor)",
    "Oil Painting": "ภาพวาดสีน้ำมันคลาสสิก",
    "Claymation": "ดินน้ำมันสต็อปโมชัน (Clay)",
    "Origami": "พับกระดาษโอริกามิ",
    "Stained Glass": "กระจกสีโบสถ์ (Stained Glass)",
    "Isometric": "มุมมองสามมิติ Isometric",
    "Low Poly": "โลว์โพลี 3D (Low Poly)",
    "Synthwave": "ซินธ์เวฟนีออนยุค 80s",
    "Steampunk": "สตีมพังก์จักรกลไอน้ำ",
    "Vaporwave": "เวเพอร์เวฟ (Vaporwave)",
    "Cute": "น่ารักสดใส",
    "Expressive": "เปี่ยมอารมณ์ความรู้สึก",
    "Original": "ต้นฉบับดั้งเดิม",
    "Scenic": "ทิวทัศน์ธรรมชาติ",
    "Raw": "สมจริงเป็นธรรมชาติ (Raw Mode)",
    "Special": "พิเศษ",
    "Chinese Style": "สไตล์จีนโบราณ",
    "Emotion": "อารมณ์และความรู้สึก"
}

def translate_phrase(text: str, zh_text: str = '') -> str:
    if not text:
        return text
    
    # Check exact translations
    if text in EXACT_TRANSLATIONS:
        return EXACT_TRANSLATIONS[text]
    if zh_text in EXACT_TRANSLATIONS:
        return EXACT_TRANSLATIONS[zh_text]
    if text in STYLE_TAGS:
        return STYLE_TAGS[text]
    
    # Normalize
    t = text.strip()
    
    # Placeholder / Parameter patterns
    if t.startswith("Please enter "):
        field = t[len("Please enter "):].rstrip('.').strip()
        field_th = EXACT_TRANSLATIONS.get(field, field)
        return f"กรุณากรอก {field_th}"
    if t.startswith("Enter "):
        field = t[len("Enter "):].rstrip('.').strip()
        field_th = EXACT_TRANSLATIONS.get(field, field)
        return f"กรอก {field_th}"
    if t.startswith("Upload "):
        field = t[len("Upload "):].rstrip('.').strip()
        field_th = EXACT_TRANSLATIONS.get(field, field)
        return f"อัปโหลด {field_th}"
    if t.startswith("Select "):
        field = t[len("Select "):].rstrip('.').strip()
        field_th = EXACT_TRANSLATIONS.get(field, field)
        return f"เลือก {field_th}"
    if t.startswith("Failed to "):
        action = t[len("Failed to "):].rstrip('.').strip()
        return f"ไม่สามารถ {action} ได้"
    if t.startswith("Successfully "):
        action = t[len("Successfully "):].rstrip('.').strip()
        return f"{action} สำเร็จ"

    # Chinese prefix patterns
    if zh_text:
        z = zh_text.strip()
        if z.startswith("请输入"):
            field = z[len("请输入"):].rstrip('。').rstrip('...')
            field_th = EXACT_TRANSLATIONS.get(field, field)
            return f"กรุณากรอก {field_th}"
        if z.startswith("请选择"):
            field = z[len("请选择"):].rstrip('。').rstrip('...')
            field_th = EXACT_TRANSLATIONS.get(field, field)
            return f"กรุณาเลือก {field_th}"
        if z.startswith("上传"):
            field = z[len("上传"):].rstrip('。')
            field_th = EXACT_TRANSLATIONS.get(field, field)
            return f"อัปโหลด {field_th}"
        if z.endswith("失败"):
            action = z[:-len("失败")].rstrip('。')
            action_th = EXACT_TRANSLATIONS.get(action, action)
            return f"{action_th} ล้มเหลว"
        if z.endswith("成功"):
            action = z[:-len("成功")].rstrip('。')
            action_th = EXACT_TRANSLATIONS.get(action, action)
            return f"{action_th} สำเร็จ"

    # Default fallback: return original if no suitable match
    return text

def process_file(filename: str):
    th_path = os.path.join(TH_DIR, filename)
    en_path = os.path.join(EN_DIR, filename)
    zh_path = os.path.join(ZH_DIR, filename)

    if not os.path.exists(th_path):
        return

    with open(th_path, 'r', encoding='utf-8') as f:
        th_data = json.load(f)

    en_data = {}
    if os.path.exists(en_path):
        with open(en_path, 'r', encoding='utf-8') as f:
            en_data = json.load(f)

    zh_data = {}
    if os.path.exists(zh_path):
        with open(zh_path, 'r', encoding='utf-8') as f:
            zh_data = json.load(f)

    updated_count = 0
    for key, th_val in th_data.items():
        if isinstance(th_val, dict):
            current_msg = th_val.get('message', '')
            if not has_thai(current_msg) and (re.search(r'[a-zA-Z]', current_msg) or re.search(r'[\u4E00-\u9FFF]', current_msg)):
                en_msg = en_data.get(key, {}).get('message', '') if isinstance(en_data.get(key), dict) else ''
                zh_msg = zh_data.get(key, {}).get('message', '') if isinstance(zh_data.get(key), dict) else ''
                
                new_msg = translate_phrase(current_msg or en_msg, zh_msg)
                if new_msg != current_msg and has_thai(new_msg):
                    th_val['message'] = new_msg
                    updated_count += 1
        elif isinstance(th_val, str):
            if not has_thai(th_val) and (re.search(r'[a-zA-Z]', th_val) or re.search(r'[\u4E00-\u9FFF]', th_val)):
                en_msg = en_data.get(key, '') if isinstance(en_data.get(key), str) else ''
                zh_msg = zh_data.get(key, '') if isinstance(zh_data.get(key), str) else ''
                new_msg = translate_phrase(th_val or en_msg, zh_msg)
                if new_msg != th_val and has_thai(new_msg):
                    th_data[key] = new_msg
                    updated_count += 1

    if updated_count > 0:
        with open(th_path, 'w', encoding='utf-8') as f:
            json.dump(th_data, f, ensure_ascii=False, indent=2)
        print(f"[{filename}] Translated {updated_count} keys")

def main():
    files = sorted(os.listdir(TH_DIR))
    for f in files:
        if f.endswith('.json'):
            process_file(f)

if __name__ == '__main__':
    main()
