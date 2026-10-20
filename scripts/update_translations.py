#!/usr/bin/env python3
import json
import os

TH_DIR = 'src/i18n/th'
EN_DIR = 'src/i18n/en'

def load_json(path):
    if not os.path.exists(path):
        return {}
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json(path, data):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write('\n')

# 1. Update common.json
th_common = load_json(f'{TH_DIR}/common.json')
en_common = load_json(f'{EN_DIR}/common.json')

new_common_keys_th = {
    "nav.chat": {"message": "แชท AI", "description": "AI Chat"},
    "nav.image": {"message": "สร้างภาพ AI", "description": "AI Image Generation"},
    "nav.video": {"message": "สร้างวิดีโอ AI", "description": "AI Video Generation"},
    "nav.music": {"message": "สร้างเพลง & เสียง AI", "description": "AI Music & Audio"},
    "nav.promptLibrary": {"message": "คลังพร้อมต์ AI", "description": "Prompt Library"},
    "nav.more": {"message": "เครื่องมือเพิ่มเติม", "description": "More tools"},
    "nav.all": {"message": "ทั้งหมด", "description": "All tools"},
    "tooltip.refreshCredit": {"message": "คลิกเพื่อรีเฟรชเครดิต", "description": "Refresh credits"},
    "user.member": {"message": "สมาชิก Tora AI", "description": "Tora AI member"},
    "user.activeSessions": {"message": "เซสชันที่ใช้งาน (Sessions)", "description": "Active sessions"},
    "user.activeSessionsTitle": {"message": "เซสชันและคุกกี้ที่กำลังใช้งาน", "description": "Active sessions title"},
    "user.syncCredits": {"message": "รีเฟรชเครดิต (Sync Quota)", "description": "Sync credits"},
    "user.console": {"message": "คอนโซลจัดการ", "description": "Console"},
    "auth.title": {"message": "เข้าสู่ระบบ Tora AI", "description": "Login title"},
    "auth.subtitle": {"message": "เกตเวย์ AI อัจฉริยะ • ซิงค์เครดิตและเซสชันอัตโนมัติ", "description": "Auth subtitle"},
    "auth.tabLogin": {"message": "เข้าสู่ระบบ", "description": "Login tab"},
    "auth.tabRegister": {"message": "สมัครสมาชิก", "description": "Register tab"},
    "auth.tabApiKey": {"message": "ใส่ API Key", "description": "API Key tab"},
    "auth.usernamePlaceholder": {"message": "ชื่อผู้ใช้งานหรืออีเมล", "description": "Username placeholder"},
    "auth.passwordPlaceholder": {"message": "รหัสผ่าน", "description": "Password placeholder"},
    "auth.confirmPasswordPlaceholder": {"message": "ยืนยันรหัสผ่านอีกครั้ง", "description": "Confirm password placeholder"},
    "auth.apiKeyPlaceholder": {"message": "sk-... กรอกคีย์จาก toraapi.com", "description": "API Key placeholder"},
    "auth.btnSubmitLogin": {"message": "เข้าสู่ระบบทันที", "description": "Submit login"},
    "auth.btnSubmitRegister": {"message": "ลงทะเบียนบัญชีใหม่", "description": "Submit register"},
    "auth.btnSubmitApiKey": {"message": "เชื่อมต่อด้วย API Key", "description": "Submit API Key"},
    "auth.keyHelp": {"message": "คีย์จะถูกจัดเก็บในเครื่องอย่างปลอดภัย ใช้สำหรับเรียก API ของ toraapi.com โดยตรง", "description": "API Key help"},
    "auth.getKeyLink": {"message": "รับ API Key ได้ที่ toraapi.com", "description": "Get API key link"},
    "auth.successLogin": {"message": "เข้าสู่ระบบและซิงค์เครดิตเรียบร้อยแล้ว!", "description": "Login success"},
    "auth.successRegister": {"message": "สมัครสมาชิกสำเร็จและเข้าสู่ระบบเรียบร้อย!", "description": "Register success"},
    "auth.successApiKey": {"message": "บันทึกและเชื่อมต่อ API Key เรียบร้อยแล้ว!", "description": "API Key success"},
    "prompt.modalTitle": {"message": "คลังพร้อมต์ AI ยอดนิยม (Prompt Library)", "description": "Prompt library title"},
    "prompt.modalSubtitle": {"message": "เลือกพร้อมต์คุณภาพสูงเพื่อเริ่มต้นสร้างสรรค์ภาพ วิดีโอ หรือแชทได้ทันที", "description": "Prompt library subtitle"},
    "prompt.searchPlaceholder": {"message": "ค้นหาตามหัวข้อ สไตล์ หรือแท็ก...", "description": "Search prompt placeholder"},
    "prompt.btnUse": {"message": "ใช้ Prompt นี้", "description": "Use prompt button"},
    "prompt.btnCopy": {"message": "คัดลอก", "description": "Copy prompt button"},
    "prompt.copiedToast": {"message": "คัดลอกพร้อมต์ไปยังคลิปบอร์ดแล้ว!", "description": "Copied toast"},
    "prompt.appliedToast": {"message": "คัดลอกและนำไปใช้ในเครื่องมือแล้ว!", "description": "Applied toast"},
    "prompt.showcaseBadge": {"message": "💡 ศูนย์รวมพร้อมต์ AI ภาษาไทย", "description": "Showcase badge"},
    "prompt.showcaseTitle": {"message": "คลัง Prompt ยอดนิยมสำหรับสร้างสรรค์ผลงาน", "description": "Showcase title"},
    "prompt.showcaseDesc": {"message": "รวมพร้อมต์คุณภาพสูงสำหรับงานสร้างสรรค์ภาพถ่ายระดับสตูดิโอ, อนิเมะ, แฟชั่น, 3D, แผนธุรกิจ และเขียนโค้ด สามารถคลิกเพื่อเริ่มต้นสร้างผลงานได้ทันที", "description": "Showcase desc"},
    "prompt.showcaseBtnExplore": {"message": "✨ เปิดคลัง Prompt ทั้งหมด", "description": "Explore all prompts button"},
    "prompt.showcaseBtnChat": {"message": "💬 เริ่มบทสนทนาใหม่", "description": "Start new chat button"},
    "prompt.chatSuggestionsTitle": {"message": "✨ พร้อมต์แนะนำยอดนิยม (Prompts)", "description": "Chat suggestion title"},
    "prompt.chatSuggestionsMore": {"message": "💡 คลัง Prompt ทั้งหมด →", "description": "More prompts link"}
}

new_common_keys_en = {
    "nav.chat": {"message": "AI Chat", "description": "AI Chat"},
    "nav.image": {"message": "AI Image", "description": "AI Image Generation"},
    "nav.video": {"message": "AI Video", "description": "AI Video Generation"},
    "nav.music": {"message": "AI Music", "description": "AI Music & Audio"},
    "nav.promptLibrary": {"message": "Prompt Library", "description": "Prompt Library"},
    "nav.more": {"message": "More Tools", "description": "More tools"},
    "nav.all": {"message": "All Tools", "description": "All tools"},
    "tooltip.refreshCredit": {"message": "Click to refresh credits", "description": "Refresh credits"},
    "user.member": {"message": "Tora AI Member", "description": "Tora AI member"},
    "user.activeSessions": {"message": "Active Sessions", "description": "Active sessions"},
    "user.activeSessionsTitle": {"message": "Active Sessions & Cookies", "description": "Active sessions title"},
    "user.syncCredits": {"message": "Sync Quota & Credits", "description": "Sync credits"},
    "user.console": {"message": "Management Console", "description": "Console"},
    "auth.title": {"message": "Sign In to Tora AI", "description": "Login title"},
    "auth.subtitle": {"message": "Smart AI Gateway • Automatic credit & session sync", "description": "Auth subtitle"},
    "auth.tabLogin": {"message": "Sign In", "description": "Login tab"},
    "auth.tabRegister": {"message": "Sign Up", "description": "Register tab"},
    "auth.tabApiKey": {"message": "API Key", "description": "API Key tab"},
    "auth.usernamePlaceholder": {"message": "Username or email", "description": "Username placeholder"},
    "auth.passwordPlaceholder": {"message": "Password", "description": "Password placeholder"},
    "auth.confirmPasswordPlaceholder": {"message": "Confirm password", "description": "Confirm password placeholder"},
    "auth.apiKeyPlaceholder": {"message": "sk-... Enter key from toraapi.com", "description": "API Key placeholder"},
    "auth.btnSubmitLogin": {"message": "Sign In Now", "description": "Submit login"},
    "auth.btnSubmitRegister": {"message": "Create Account", "description": "Submit register"},
    "auth.btnSubmitApiKey": {"message": "Connect API Key", "description": "Submit API Key"},
    "auth.keyHelp": {"message": "Key is stored securely on device and used to query toraapi.com directly", "description": "API Key help"},
    "auth.getKeyLink": {"message": "Get API Key at toraapi.com", "description": "Get API key link"},
    "auth.successLogin": {"message": "Signed in and credits synced successfully!", "description": "Login success"},
    "auth.successRegister": {"message": "Account created and signed in successfully!", "description": "Register success"},
    "auth.successApiKey": {"message": "API Key connected successfully!", "description": "API Key success"},
    "prompt.modalTitle": {"message": "Curated AI Prompt Library", "description": "Prompt library title"},
    "prompt.modalSubtitle": {"message": "Select high-quality prompts to create images, videos, or chats instantly", "description": "Prompt library subtitle"},
    "prompt.searchPlaceholder": {"message": "Search by topic, style, or tag...", "description": "Search prompt placeholder"},
    "prompt.btnUse": {"message": "Use Prompt", "description": "Use prompt button"},
    "prompt.btnCopy": {"message": "Copy", "description": "Copy prompt button"},
    "prompt.copiedToast": {"message": "Prompt copied to clipboard!", "description": "Copied toast"},
    "prompt.appliedToast": {"message": "Prompt applied to studio!", "description": "Applied toast"},
    "prompt.showcaseBadge": {"message": "💡 Curated Thai AI Prompts", "description": "Showcase badge"},
    "prompt.showcaseTitle": {"message": "Popular Prompts for Creative Work", "description": "Showcase title"},
    "prompt.showcaseDesc": {"message": "High-quality prompts for studio portraits, anime, 3D, marketing, and coding. Click to create instantly.", "description": "Showcase desc"},
    "prompt.showcaseBtnExplore": {"message": "✨ Explore All Prompts", "description": "Explore all prompts button"},
    "prompt.showcaseBtnChat": {"message": "💬 Start New Chat", "description": "Start new chat button"},
    "prompt.chatSuggestionsTitle": {"message": "✨ Recommended Prompts", "description": "Chat suggestion title"},
    "prompt.chatSuggestionsMore": {"message": "💡 All Prompts →", "description": "More prompts link"}
}

th_common.update(new_common_keys_th)
en_common.update(new_common_keys_en)

save_json(f'{TH_DIR}/common.json', th_common)
save_json(f'{EN_DIR}/common.json', en_common)
print("Updated common.json")

# 2. Update intro.json with flawless Thai translations
th_intro = load_json(f'{TH_DIR}/intro.json')
intro_overrides_th = {
    "badge.hero": {"message": "ครบทุกฟีเจอร์ AI ชั้นนำ", "description": "介绍页顶部徽章"},
    "title.hero": {"message": "บัญชีเดียว เข้าถึงทุก AI ตัวท็อปของโลก", "description": "介绍页主标题"},
    "subtitle.hero": {"message": "แชท สร้างภาพ แต่งเพลง ทำวิดีโอ ดิจิทัลฮิวแมน และผู้ช่วยเขียนโค้ด ครบครันในที่เดียว ไม่ต้องสมัครแยก ไม่ต้องจ่ายหลายแพ็กเกจ", "description": "介绍页副标题"},
    "title.site": {"message": "สุดยอด AI แถวหน้า พร้อมรับทุกจินตนาการของคุณ", "description": "按站点配置展示时的主标题"},
    "subtitle.site": {"message": "ตั้งแต่บทสนทนาอัจฉริยะไปจนถึงงานภาพ ดนตรี วิดีโอ และการเพิ่มประสิทธิภาพการทำงาน ทุกเครื่องมือพร้อมใช้งานทันที", "description": "按站点配置展示时的副标题"},
    "button.explore": {"message": "สำรวจฟีเจอร์ทั้งหมด", "description": "探索按钮"},
    "button.try": {"message": "ทดลองใช้งานทันที", "description": "体验按钮"},
    "stat.capabilities": {"message": "ความสามารถ AI", "description": "能力数量统计"},
    "stat.models": {"message": "โมเดลระดับแนวหน้า", "description": "模型数量统计"},
    "stat.products": {"message": "บริการที่พร้อมใช้", "description": "当前站点可用产品数量"},
    "home.createNow": {"message": "สร้างสรรค์ทันที", "description": "首页卡片行动文案"},
    "home.banner.video.eyebrow": {"message": "สร้างวิดีโอ AI", "description": "视频 Banner 标签"},
    "home.banner.video.title": {"message": "เปลี่ยนไอเดียของคุณให้กลายเป็นภาพยนตร์เสมือนจริง", "description": "视频 Banner 标题"},
    "home.banner.video.description": {"message": "ข้อความ รูปภาพ และข้อมูลอ้างอิง จะถูกสร้างเป็นวิดีโอระดับภาพยนตร์อย่างมืออาชีพ", "description": "视频 Banner 说明"},
    "home.banner.image.eyebrow": {"message": "สร้างรูปภาพ AI", "description": "图片 Banner 标签"},
    "home.banner.image.title": {"message": "เริ่มต้นสร้างสรรค์ภาพจากคำบรรยายสั้นๆ", "description": "图片 Banner 标题"},
    "home.banner.image.description": {"message": "สร้าง แก้ไข ขยายภาพ และปรับแต่งสไตล์จนตรงใจกับจินตนาการของคุณ", "description": "图片 Banner 说明"},
    "home.banner.production.eyebrow": {"message": "งานสร้างสรรค์ครบวงจร", "description": "成片 Banner 标签"},
    "home.banner.production.title": {"message": "บอกแค่หัวข้อ ได้คลิปวิดีโอฉบับสมบูรณ์ทันที", "description": "成片 Banner 标题"},
    "home.banner.production.description": {"message": "ทั้งบท ภาพ เสียงพากย์ ซับไตเติล และเพลงประกอบ จะถูกสร้างอัตโนมัติอย่างลงตัว", "description": "成片 Banner 说明"},
    "home.quick.eyebrow": {"message": "เริ่มต้นด่วน", "description": "快速入口区标签"},
    "home.quick.title": {"message": "วันนี้คุณต้องการสร้างสรรค์อะไร?", "description": "快速入口区标题"},
    "home.quick.subtitle": {"message": "เริ่มต้นจากสิ่งที่คุณต้องการสร้าง แทนที่จะต้องเสียเวลาค้นหาชื่อโมเดล", "description": "快速入口区说明"},
    "home.quick.chat.title": {"message": "แชทและสนทนากับ AI", "description": "对话快速入口标题"},
    "home.quick.chat.description": {"message": "เขียนบทความ วิเคราะห์ข้อมูล เรียนรู้ และต่อยอดไอเดีย", "description": "对话快速入口说明"},
    "home.quick.image.title": {"message": "สร้างรูปภาพ AI", "description": "图片快速入口标题"},
    "home.quick.image.description": {"message": "โปสเตอร์ ภาพถ่ายสินค้า ตัวละคร และงานออกแบบ", "description": "图片快速入口说明"},
    "home.quick.music.title": {"message": "แต่งเพลงและเสียงดนตรี", "description": "音乐快速入口标题"},
    "home.quick.music.description": {"message": "ตั้งแต่กำหนดสไตล์และเนื้อร้อง สู่เพลงฉบับสมบูรณ์", "description": "音乐快速入口说明"},
    "home.quick.video.title": {"message": "สร้างวิดีโอ AI", "description": "视频快速入口标题"},
    "home.quick.video.description": {"message": "คลิปสั้น แอนิเมชัน และวิดีโอระดับภาพยนตร์", "description": "视频快速入口说明"},
    "home.quick.explore": {"message": "สำรวจ", "description": "卡片展开文案"},
    "home.quick.close": {"message": "ปิดแถบ", "description": "卡片收起文案"},
    "home.showcase.eyebrow": {"message": "แกลเลอรีสร้างสรรค์", "description": "社区示例区标签"},
    "home.showcase.title": {"message": "แรงบันดาลใจจากผลงานจริง", "description": "社区示例区主标题"},
    "home.showcase.subtitle": {"message": "ดูสิ่งที่ผู้อื่นสร้างสรรค์ แล้วเริ่มทำผลงานของคุณเองได้ทันที", "description": "社区示例区副标题"},
    "home.showcase.loadMore": {"message": "โหลดผลงานเพิ่มเติม", "description": "社区示例加载更多按钮"},
    "home.backToTop": {"message": "กลับขึ้นด้านบน", "description": "返回顶部按钮"},
    "home.carousel.label": {"message": "คำแนะนำผลงานสร้างสรรค์แนะนำ", "description": "首页轮播区域无障碍标签"},
    "home.carousel.previous": {"message": "คำแนะนำก่อนหน้า", "description": "首页轮播上一张按钮"},
    "home.carousel.next": {"message": "คำแนะนำถัดไป", "description": "首页轮播下一张按钮"}
}
th_intro.update(intro_overrides_th)
save_json(f'{TH_DIR}/intro.json', th_intro)
print("Updated intro.json")

# 3. Update index.json
th_index = load_json(f'{TH_DIR}/index.json')
index_overrides_th = {
    "title.chat": {"message": "แชทและสนทนา AI", "description": "Title for chat"},
    "title.midjourney": {"message": "สร้างภาพ Midjourney", "description": "Title for midjourney"},
    "title.flux": {"message": "สร้างภาพ Flux.1", "description": "Title for flux"},
    "title.suno": {"message": "แต่งเพลง Suno", "description": "Title for suno"},
    "title.luma": {"message": "สร้างวิดีโอ Luma Dream Machine", "description": "Title for luma"},
    "title.kling": {"message": "สร้างวิดีโอ Kling AI", "description": "Title for kling"},
    "title.veo": {"message": "สร้างวิดีโอ Google Veo", "description": "Title for veo"},
    "title.sora": {"message": "สร้างวิดีโอ OpenAI Sora", "description": "Title for sora"},
    "title.openaiimage": {"message": "สร้างภาพ DALL-E 3", "description": "Title for openaiimage"},
    "subtitle.chat": {"message": "พูดคุย ปรึกษา และคิดค้นไอเดียใหม่ๆ กับโมเดลชั้นนำ", "description": "Subtitle for chat"},
    "subtitle.midjourney": {"message": "เนรมิตภาพวาดและภาพถ่ายระดับมืออาชีพด้วย Midjourney", "description": "Subtitle for midjourney"},
    "subtitle.flux": {"message": "ภาพถ่ายความละเอียดสูงและเรนเดอร์ข้อความบนภาพได้แม่นยำ", "description": "Subtitle for flux"},
    "subtitle.suno": {"message": "แต่งเพลงเต็มรูปแบบพร้อมเนื้อร้องและเสียงดนตรีสมจริง", "description": "Subtitle for suno"},
    "subtitle.luma": {"message": "แปลงข้อความหรือภาพให้เป็นคลิปวิดีโอที่มีการเคลื่อนไหวสมจริง", "description": "Subtitle for luma"},
    "subtitle.kling": {"message": "สร้างวิดีโอแอนิเมชันและการเคลื่อนไหวที่คมชัดลื่นไหล", "description": "Subtitle for kling"}
}
th_index.update(index_overrides_th)
save_json(f'{TH_DIR}/index.json', th_index)
print("Updated index.json")

print("All translations written successfully.")
