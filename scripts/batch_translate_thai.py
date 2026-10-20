#!/usr/bin/env python3
"""
Advanced bilingual translation generator for Nexior (EN/ZH -> TH)
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

# Broad dictionary from Chinese to Thai
ZH_TO_TH = {
    # Common UI
    "追踪 ID": "รหัสติดตาม (Trace ID)",
    "调用": "การเรียกใช้",
    "自动": "อัตโนมัติ",
    "尺寸": "ขนาดสัดส่วน",
    "风格": "สไตล์",
    "响应": "การตอบกลับ",
    "次": "ครั้ง",
    "过期时间": "วันหมดอายุ",
    "服务": "บริการ",
    "其他": "อื่นๆ",
    "默认": "ค่าเริ่มต้น",
    "推荐": "แนะนำ",
    "启用": "เปิดใช้งาน",
    "禁用": "ปิดใช้งาน",
    "连接器": "ตัวเชื่อมต่อ (Connectors)",
    "必填": "จำเป็นต้องระบุ",
    "任务类型": "ประเภทงาน",
    "参考图片": "รูปภาพอ้างอิง",
    "继续生成此视频": "สร้างต่อจากวิดีโอนี้",
    "随机": "สุ่ม",
    "开始时间 (秒)": "เวลาเริ่มต้น (วินาที)",
    "结束时间 (秒)": "เวลาสิ้นสุด (วินาที)",
    "请求头": "Request Headers",
    "请求体": "Request Body",
    "响应体": "Response Body",
    "响应头": "Response Headers",
    "示例": "ตัวอย่าง",
    "申请": "สมัครใช้งาน",
    "代理": "พร็อกซี (Proxy)",
    "技能": "ทักษะและความสามารถ (Skills)",
    "连接": "เชื่อมต่อ",
    "已完成": "เสร็จสมบูรณ์",
    "重命名": "เปลี่ยนชื่อ",
    "配对设备": "จับคู่อุปกรณ์",
    "移除": "นำออก",
    "推荐收益": "รายได้จากการแนะนำ",
    "语言": "ภาษา",
    "安装": "ติดตั้ง",
    "添加自定义连接器": "เพิ่มตัวเชื่อมต่อกำหนดเอง",
    "添加": "เพิ่ม",
    "快速": "รวดเร็ว (Fast Mode)",
    "慢速": "โหมดประหยัด (Relax Mode)",
    "创建图片": "สร้างรูปภาพ",
    "文生视频": "แปลงข้อความเป็นวิดีโอ (Text to Video)",
    "图生视频": "แปลงภาพเป็นวิดีโอ (Image to Video)",
    "参考视频": "วิดีโออ้างอิง",
    "圆形": "วงกลม",
    "加号": "เครื่องหมายบวก",
    "方框": "กล่องสี่เหลี่ยม",
    "成功发起生成任务": "เริ่มสร้างงานสำเร็จแล้ว",
    "替换片段": "แทนที่ช่วงท่อนเพลง",
    "约": "ประมาณ",
    "全屏": "เต็มหน้าจอ",
    "退出全屏": "ออกจากโหมดเต็มจอ",
    "深色模式": "โหมดมืด (Dark Mode)",
    "浅色模式": "โหมดสว่าง (Light Mode)",
    "跟随系统": "ตามการตั้งค่าระบบ",
    "主题": "ธีม",
    "个人中心": "ศูนย์ผู้ใช้งาน",
    "控制台": "คอนโซลจัดการ",
    "退出登录": "ออกจากระบบ",
    "登录": "เข้าสู่ระบบ",
    "注册": "สมัครสมาชิก",
    "账号": "บัญชีผู้ใช้",
    "密码": "รหัสผ่าน",
    "邮箱": "อีเมล",
    "手机号": "หมายเลขโทรศัพท์",
    "验证码": "รหัสยืนยัน",
    "获取验证码": "ขอรับรหัสยืนยัน",
    "重置密码": "รีเซ็ตรหัสผ่าน",
    "修改密码": "เปลี่ยนรหัสผ่าน",
    "绑定": "เชื่อมโยง",
    "解绑": "ยกเลิกการเชื่อมโยง",
    "复制成功": "คัดลอกสำเร็จ",
    "保存成功": "บันทึกสำเร็จ",
    "删除成功": "ลบสำเร็จ",
    "更新成功": "อัปเดตสำเร็จ",
    "提交成功": "ส่งข้อมูลสำเร็จ",
    "重置成功": "รีเซ็ตสำเร็จ",
    "支付成功": "ชำระเงินสำเร็จ",
    "操作失败，请稍后重试": "ดำเนินการไม่สำเร็จ กรุณาลองใหม่อีกครั้ง",
    "未知错误": "เกิดข้อผิดพลาดที่ไม่ทราบสาเหตุ",
    "权限不足": "ไม่มีสิทธิ์เข้าถึง",
    "请先登录": "กรุณาเข้าสู่ระบบก่อนดำเนินการ",
    "确认删除？": "ยืนยันการลบหรือไม่?",
    "此操作不可逆": "การดำเนินการนี้ไม่สามารถย้อนกลับได้",
    "暂无内容": "ยังไม่มีเนื้อหา",
    "加载更多": "โหลดเพิ่มเติม",
    "已加载全部": "โหลดเนื้อหาทั้งหมดแล้ว",
    "暂无更多": "ไม่มีข้อมูลเพิ่มเติมแล้ว",

    # Midjourney parameters and UI
    "生成图片": "สร้างรูปภาพ",
    "变化": "สร้างรูปแบบใหม่ (Variation)",
    "放大": "ขยายความละเอียด (Upscale)",
    "重新生成": "สร้างใหม่อีกครั้ง",
    "提示词": "พรอมต์ (Prompt)",
    "负向提示词": "พรอมต์เชิงลบ (Negative Prompt)",
    "垫图": "รูปภาพอ้างอิง (Image Prompt)",
    "图生图": "แปลงภาพเป็นภาพ (Image to Image)",
    "比例": "อัตราส่วนภาพ (Aspect Ratio)",
    "模型版本": "เวอร์ชันโมเดล",
    "画质": "คุณภาพงาน (Quality)",
    "风格化": "ความจัดจ้านของสไตล์ (Stylize)",
    "混乱度": "ความสุ่มสร้างสรรค์ (Chaos)",
    "怪异度": "ความแปลกใหม่แฟนตาซี (Weird)",
    "权重": "น้ำหนักภาพอ้างอิง (Image Weight)",
    "种子": "ค่า Seed",
    "停止比例": "หยุดสร้างกลางคัน (Stop %)",
    "平铺": "สร้างลวดลายไร้รอยต่อ (Tile Pattern)",
    "混音": "โหมดผสมผสาน (Remix Mode)",
    "平移": "ขยายมุมมอง (Pan)",
    "缩放": "ซูมมุมมอง (Zoom)",
    "重绘": "ระบายแก้ไขเฉพาะจุด (Inpaint / Vary Region)",
    "描述": "ถอดข้อความจากภาพ (Describe)",
    "混合": "ผสมผสานรูปภาพ (Blend)",
    "精简": "วิเคราะห์ย่อพรอมต์ (Shorten)",

    # Video parameters and UI
    "时长": "ความยาว",
    "帧率": "อัตราเฟรมเรต (FPS)",
    "运动幅度": "ระดับการเคลื่อนไหว",
    "镜头控制": "ควบคุมมุมกล้อง",
    "运镜": "การเคลื่อนไหวของกล้อง",
    "下移": "เลื่อนลง",
    "上移": "เลื่อนขึ้น",
    "左移": "เลื่อนซ้าย",
    "右移": "เลื่อนขวา",
    "顺时针旋转": "หมุนตามเข็มนาฬิกา",
    "逆时针旋转": "หมุนทวนเข็มนาฬิกา",
    "拉近": "ซูมเข้า (Zoom In)",
    "拉远": "ซูมออก (Zoom Out)",
    "首帧": "ภาพเฟรมแรก (First Frame)",
    "尾帧": "ภาพเฟรมสุดท้าย (Last Frame)",
    "首尾帧": "เฟรมเริ่มต้นและสิ้นสุด",
    "循环视频": "เล่นวิดีโอวนซ้ำ",
    "扩展视频": "ขยายความยาววิดีโอ",
    "口型同步": "ลิปซิงก์ตรงเสียงพูด (Lip Sync)",
    "数字人": "มนุษย์ดิจิทัล (Digital Human)",
    "视频画质": "ความคมชัดวิดีโอ",
    "标准画质": "ความคมชัดระดับมาตรฐาน (Standard)",
    "高清画质": "ความคมชัดระดับสูง (High Definition)",
    "超高清画质": "ความคมชัดระดับ 4K Ultra HD",

    # Music parameters and UI
    "生成音乐": "สร้างเพลงดนตรี",
    "自定义模式": "โหมดกำหนดเอง (Custom Mode)",
    "纯器乐": "ดนตรีบรรเลงล้วน (Instrumental)",
    "生成歌词": "สร้างเนื้อเพลงด้วย AI",
    "随机灵感": "สุ่มไอเดียสร้างสรรค์",
    "续写": "แต่งเพลงต่อ (Extend)",
    "重写": "เรียบเรียงใหม่ (Remake)",
    "人声分离": "แยกเสียงร้องและเสียงดนตรี",
    "声音克隆": "โคลนเสียงเอกลักษณ์ (Voice Clone)",
    "文本转语音": "แปลงข้อความเป็นเสียงพูด (Text to Speech)",
    "语音合成": "สังเคราะห์เสียงพูด (TTS)",
    "采样率": "อัตราการสุ่มตัวอย่างเสียง (Sample Rate)",
    "语速": "ความเร็วในการพูด",
    "音调": "ระดับโทนเสียง (Pitch)",
    "情感表达": "การถ่ายทอดอารมณ์เสียง",

    # Chat parameters and UI
    "发送": "ส่งข้อความ",
    "输入问题": "พิมพ์คำถามของคุณ...",
    "新建对话": "เริ่มการสนทนาใหม่",
    "历史对话": "ประวัติการสนทนา",
    "清除对话": "ล้างประวัติการสนทนา",
    "置顶": "ปักหมุด",
    "取消置顶": "ยกเลิกการปักหมุด",
    "分享对话": "แชร์บทสนทนา",
    "导出": "ส่งออกข้อมูล",
    "模型设置": "การตั้งค่าโมเดล",
    "上下文长度": "ความยาวบริบท (Context Length)",
    "最大长度": "จำนวนโทเค็นสูงสุด",
    "采样温度": "ความสร้างสรรค์ (Temperature)",
    "核采样": "Top-P Sampling",
    "系统指令": "คำสั่งระบบ (System Instructions)",
    "快捷指令": "คำสั่งด่วน (Prompt Presets)",
    "停止生成": "หยุดการสร้างข้อความ",
    "重新回答": "ตอบใหม่อีกครั้ง",
    "点赞": "ถูกใจ",
    "点踩": "ไม่ถูกใจ",
    "阅读全文": "อ่านทั้งหมด",
    "折叠": "ย่อเก็บ",
    "展开": "ขยายอ่าน",

    # Subsite, Domain, Business & Distribution
    "分站": "เว็บไซต์ย่อย (Subsite)",
    "子站": "เว็บไซต์ย่อย",
    "独立域名": "โดเมนส่วนตัว (Custom Domain)",
    "品牌名称": "ชื่อแบรนด์",
    "站点配置": "การกำหนดค่าเว็บไซต์",
    "分销中心": "ศูนย์ตัวแทนแนะนำ (Affiliate)",
    "推广链接": "ลิงก์แนะนำเพื่อน",
    "佣金比例": "อัตราส่วนคอมมิชชัน",
    "可提现金额": "ยอดเงินที่ถอนได้",
    "申请提现": "แจ้งถอนเงิน",
    "提现记录": "ประวัติการถอนเงิน",
    "直推用户": "ผู้ใช้ที่แนะนำโดยตรง",
    "团队用户": "สมาชิกในทีม",
    "累计收益": "รายได้สะสมทั้งหมด",
    "昨日收益": "รายได้เมื่อวาน",
    "今日收益": "รายได้วันนี้",
    "结算周期": "รอบการคิดผลตอบแทน",
    "分润规则": "เงื่อนไขการแบ่งรายได้"
}

# Regex patterns for Chinese phrases to Thai
ZH_PATTERNS = [
    (re.compile(r'^请输入(.*)'), r'กรุณากรอก \1'),
    (re.compile(r'^请选择(.*)'), r'กรุณาเลือก \1'),
    (re.compile(r'^上传(.*)'), r'อัปโหลด \1'),
    (re.compile(r'^(.*)不能为空$'), r'\1 ต้องไม่เว้นว่าง'),
    (re.compile(r'^(.*)失败$'), r'\1 ล้มเหลว'),
    (re.compile(r'^(.*)成功$'), r'\1 สำเร็จ'),
    (re.compile(r'^(.*)设置$'), r'การตั้งค่า \1'),
    (re.compile(r'^(.*)列表$'), r'รายการ \1'),
    (re.compile(r'^(.*)管理$'), r'จัดการ \1'),
    (re.compile(r'^(.*)详情$'), r'รายละเอียด \1'),
    (re.compile(r'^支持(.*)格式$'), r'รองรับรูปแบบ \1'),
    (re.compile(r'^最大不超过(.*)'), r'ขนาดสูงสุดไม่เกิน \1'),
    (re.compile(r'^是否确定(.*)\?$'), r'ยืนยัน \1 หรือไม่?'),
]

# Additional English translations
EN_TO_TH = {
    "Trace ID": "รหัสติดตาม (Trace ID)",
    "Size": "ขนาด",
    "Response": "การตอบกลับ",
    "API": "API",
    "Skills": "ทักษะและความสามารถ (Skills)",
    "Referral Earnings": "รายได้จากการแนะนำ",
    "Required": "จำเป็นต้องระบุ",
    "Task Type": "ประเภทงาน",
    "Reference Image": "รูปภาพอ้างอิง",
    "Random": "สุ่ม",
    "Style": "สไตล์",
    "Seed": "ค่า Seed",
    "Auto": "อัตโนมัติ",
    "Example": "ตัวอย่าง",
    "Call": "การเรียกใช้",
    "Calls": "ครั้ง",
    "Application": "แอปพลิเคชัน",
    "Service": "บริการ",
    "Hidden": "ซ่อนอยู่",
    "Rename": "เปลี่ยนชื่อ",
    "Connect": "เชื่อมต่อ",
    "Remove": "นำออก",
    "Default": "ค่าเริ่มต้น",
    "Language": "ภาษา",
    "View Details": "ดูรายละเอียด",
    "Install": "ติดตั้ง",
    "Phone": "หมายเลขโทรศัพท์",
    "Connectors": "ตัวเชื่อมต่อ (Connectors)",
    "Add Custom Connector": "เพิ่มตัวเชื่อมต่อกำหนดเอง",
    "Add": "เพิ่ม",
    "None": "ไม่มี",
    "Create Image": "สร้างรูปภาพ",
    "Text to Video": "แปลงข้อความเป็นวิดีโอ (Text to Video)",
    "Image to Video": "แปลงภาพเป็นวิดีโอ (Image to Video)",
    "Reference Video": "วิดีโออ้างอิง",
    "Circle": "วงกลม",
    "Plus": "เครื่องหมายบวก",
    "Box": "กล่องสี่เหลี่ยม",
    "Replace Section": "แทนที่ช่วงท่อนเพลง",
    "Enabled": "เปิดใช้งาน",
    "Pricing": "ราคาและแพ็กเกจ",
    "Balance": "ยอดคงเหลือ",
    "Orders": "รายการสั่งซื้อ",
    "Subsite": "เว็บไซต์ย่อย (Subsite)",
    "Custom Domain": "โดเมนส่วนตัว",
    "Branding": "เอกลักษณ์แบรนด์",
    "Admin": "ผู้ดูแลระบบ",
    "Logout": "ออกจากระบบ",
    "Login": "เข้าสู่ระบบ",
    "Register": "สมัครสมาชิก",
    "My Account": "บัญชีของฉัน"
}

def translate_entry(msg: str, zh_msg: str) -> str:
    # 1. Exact match in EN_TO_TH
    if msg in EN_TO_TH:
        return EN_TO_TH[msg]
    
    # 2. Exact match in ZH_TO_TH
    if zh_msg in ZH_TO_TH:
        return ZH_TO_TH[zh_msg]

    # 3. Match in ZH_PATTERNS
    for pattern, repl in ZH_PATTERNS:
        if pattern.search(zh_msg):
            translated = pattern.sub(repl, zh_msg)
            # Translate words inside translated string if needed
            for z, t in ZH_TO_TH.items():
                if z in translated:
                    translated = translated.replace(z, t)
            return translated

    # 4. English common phrases
    if msg.startswith("Please enter "):
        target = msg[13:].rstrip('.').strip()
        th_target = EN_TO_TH.get(target, target)
        return f"กรุณากรอก {th_target}"
    if msg.startswith("Enter "):
        target = msg[6:].rstrip('.').strip()
        th_target = EN_TO_TH.get(target, target)
        return f"กรอก {th_target}"
    if msg.startswith("Select "):
        target = msg[7:].rstrip('.').strip()
        th_target = EN_TO_TH.get(target, target)
        return f"เลือก {th_target}"
    if msg.startswith("Upload "):
        target = msg[7:].rstrip('.').strip()
        th_target = EN_TO_TH.get(target, target)
        return f"อัปโหลด {th_target}"

    return msg

def run_translation():
    total_updated = 0
    files = sorted(glob.glob(os.path.join(TH_DIR, '*.json')))
    for th_file in files:
        fname = os.path.basename(th_file)
        zh_file = os.path.join(ZH_DIR, fname)
        en_file = os.path.join(EN_DIR, fname)

        with open(th_file, 'r', encoding='utf-8') as f:
            th_data = json.load(f)

        zh_data = {}
        if os.path.exists(zh_file):
            with open(zh_file, 'r', encoding='utf-8') as f:
                zh_data = json.load(f)

        en_data = {}
        if os.path.exists(en_file):
            with open(en_file, 'r', encoding='utf-8') as f:
                en_data = json.load(f)

        updated_in_file = 0
        for k, v in th_data.items():
            if isinstance(v, dict):
                cur_msg = v.get('message', '')
                if not has_thai(cur_msg) and re.search(r'[a-zA-Z\u4E00-\u9FFF]', cur_msg):
                    zh_msg = zh_data.get(k, {}).get('message', '') if isinstance(zh_data.get(k), dict) else ''
                    new_msg = translate_entry(cur_msg, zh_msg)
                    if new_msg != cur_msg and has_thai(new_msg):
                        v['message'] = new_msg
                        updated_in_file += 1
            elif isinstance(v, str):
                if not has_thai(v) and re.search(r'[a-zA-Z\u4E00-\u9FFF]', v):
                    zh_msg = zh_data.get(k, '') if isinstance(zh_data.get(k), str) else ''
                    new_msg = translate_entry(v, zh_msg)
                    if new_msg != v and has_thai(new_msg):
                        th_data[k] = new_msg
                        updated_in_file += 1

        if updated_in_file > 0:
            with open(th_file, 'w', encoding='utf-8') as f:
                json.dump(th_data, f, ensure_ascii=False, indent=2)
            print(f"[{fname}] Translated {updated_in_file} keys")
            total_updated += updated_in_file

    print(f"\nSuccessfully translated {total_updated} keys across all files!")

if __name__ == '__main__':
    run_translation()
