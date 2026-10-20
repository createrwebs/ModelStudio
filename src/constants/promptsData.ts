export interface IPromptTemplate {
  id: string;
  title: string;
  category: string;
  icon: string;
  model: string;
  targetType: 'chat' | 'image' | 'video' | 'music';
  targetRoute: string;
  prompt: string;
  description: string;
  previewImage?: string;
  tags: string[];
}

export const PROMPT_CATEGORIES = [
  { id: 'all', name: 'ทั้งหมด (All)', icon: '✨' },
  { id: 'photo', name: 'ภาพถ่ายสมจริง (Photography)', icon: '📸' },
  { id: 'anime', name: 'อนิเมะ & แฟนตาซี (Anime & Fantasy)', icon: '🎌' },
  { id: 'architecture', name: 'สถาปัตยกรรม (Architecture)', icon: '🏛️' },
  { id: 'product', name: 'ออกแบบผลิตภัณฑ์ (Product 3D)', icon: '🛍️' },
  { id: 'business', name: 'ธุรกิจ & การตลาด (Business & Copy)', icon: '💡' },
  { id: 'coding', name: 'เขียนโค้ด & ไอที (Tech & Code)', icon: '💻' },
  { id: 'video', name: 'สร้างวิดีโอ (AI Video)', icon: '🎬' }
];

export const CURATED_PROMPTS: IPromptTemplate[] = [
  {
    id: 'photo-portrait-cyberpunk',
    title: 'ภาพถ่ายบุคคลสไตล์นีออนไซเบอร์พังก์',
    category: 'photo',
    icon: '📸',
    model: 'Flux.1 Pro / Midjourney',
    targetType: 'image',
    targetRoute: '/flux',
    previewImage: 'https://images.unsplash.com/photo-1578632767115-351597cf2477?w=800&auto=format&fit=crop&q=80',
    description: 'ภาพถ่ายพอร์ตเทรตหญิงสาวท่ามกลางแสงไฟนีออนในเมืองโตเกียวตอนกลางคืน มีประกายละอองฝนและความลึกของโบเก้',
    tags: ['Portrait', 'Cyberpunk', 'Neon', 'Cinematic', '8K'],
    prompt:
      'Cinematic portrait of a Thai futuristic cyberpunk woman in rainy night street of Neo-Tokyo, vibrant cyan and magenta neon lights reflecting on wet pavement, hyper-detailed skin texture, shallow depth of field, f/1.4, 85mm lens, volumetric smoke, photorealistic, 8k resolution, Masterpiece'
  },
  {
    id: 'photo-nature-macro',
    title: 'ภาพมาโครหยดน้ำบนกลีบดอกไม้',
    category: 'photo',
    icon: '🌸',
    model: 'Midjourney v6.1',
    targetType: 'image',
    targetRoute: '/midjourney',
    previewImage: 'https://images.unsplash.com/photo-1518531933037-91b2f5f229cc?w=800&auto=format&fit=crop&q=80',
    description: 'ภาพมาโครระยะประชิดจับหยดน้ำค้างใสแจ๋วบนกลีบดอกบัวสีชมพู พร้อมแสงแดดยามเช้าที่ส่องผ่าน',
    tags: ['Macro', 'Nature', 'Dew', 'Waterdrop', 'Ultra-detailed'],
    prompt:
      'Extreme macro photography of crystal clear morning water droplets perched delicately on a vibrant pink lotus petal, refracted golden morning sunlight, ultra sharp focus on droplet, dreamy soft bokeh background, Canon EOS R5 100mm f/2.8L Macro lens, national geographic award winner'
  },
  {
    id: 'anime-cozy-cafe',
    title: 'คาเฟ่อบอุ่นสไตล์สตูดิโอจิบลิ',
    category: 'anime',
    icon: '🎌',
    model: 'Flux.1 / Midjourney',
    targetType: 'image',
    targetRoute: '/flux',
    previewImage: 'https://images.unsplash.com/photo-1554118811-1e0d58224f24?w=800&auto=format&fit=crop&q=80',
    description: 'ภาพวาดอนิเมะคาเฟ่ไม้สไตล์ญี่ปุ่นแสนอบอุ่น มีแมวนอนข้างหน้าต่าง แสงแดดยามบ่ายส่องกระทบถ้วยกาแฟ',
    tags: ['Anime', 'Ghibli', 'Cozy', 'Illustration', 'Vibrant'],
    prompt:
      'Studio Ghibli aesthetic cozy hillside wooden coffee shop in summer, sunlight streaming through large open windows, lush green potted plants, sleeping calico cat on windowsill, steaming coffee cup on rustic table, hand-drawn anime background art, vibrant watercolor textures, Hayao Miyazaki style'
  },
  {
    id: 'anime-mecha-warrior',
    title: 'หุ่นยนต์เมกะไซไฟความละเอียดสูง',
    category: 'anime',
    icon: '🤖',
    model: 'Midjourney v6.1',
    targetType: 'image',
    targetRoute: '/midjourney',
    previewImage: 'https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?w=800&auto=format&fit=crop&q=80',
    description: 'การออกแบบหุ่นรบไซเบอร์เนติกขั้นสูงพร้อมเกราะโลหะสีขาวด้านและไฟสีส้มที่ทรงพลัง',
    tags: ['Sci-fi', 'Mecha', 'Robot', 'Futuristic', 'Artstation'],
    prompt:
      'Next-gen titanium combat mech standing dramatically on a launch platform, matte white armor plates with bright glowing orange energy conduits, intricate mechanical joints, hydraulic pistons, cinematic angle, octane render, unreal engine 5, artstation trending'
  },
  {
    id: 'arch-modern-villa',
    title: 'วิลล่าสไตล์มินิมอลโมเดิร์นริมทะเล',
    category: 'architecture',
    icon: '🏛️',
    model: 'Flux.1 Pro',
    targetType: 'image',
    targetRoute: '/flux',
    previewImage: 'https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=800&auto=format&fit=crop&q=80',
    description: 'บ้านพักตากอากาศสไตล์โมเดิร์นทรอปิคอล มีสระว่ายน้ำอินฟินิตี้หันหน้าสู่ทะเลอันดามันยามพระอาทิตย์ตกดิน',
    tags: ['Architecture', 'Villa', 'Interior', 'Minimalist', 'Luxury'],
    prompt:
      'Architectural digest photograph of a luxury minimalist tropical concrete villa overlooking Andaman Sea at golden hour, infinity edge pool reflecting sunset clouds, open-air living room with teak wood louvers, lush palm garden, warm ambient interior lighting, photorealistic 8k'
  },
  {
    id: 'product-perfume-bottle',
    title: 'ขวดน้ำหอมหรูหราพร้อมฉาก 3D สตูดิโอ',
    category: 'product',
    icon: '🛍️',
    model: 'DALL-E 3 / Flux.1',
    targetType: 'image',
    targetRoute: '/openaiimage',
    previewImage: 'https://images.unsplash.com/photo-1592945403244-b3fbafd7f539?w=800&auto=format&fit=crop&q=80',
    description: 'การถ่ายภาพผลิตภัณฑ์ขวดน้ำหอมแก้วคริสตัลตั้งบนแท่นหินอ่อน มีคลื่นน้ำกระเซ็นและแสงสตูดิโอนุ่มนวล',
    tags: ['Product Design', 'Commercial', 'Luxury', 'Perfume', 'Studio Lighting'],
    prompt:
      'High-end commercial product photography of an amber crystal luxury perfume bottle on raw travertine stone pedestal, gentle crystal water splash around base, soft studio rim lighting, minimal cosmetic advertising banner, hyper-detailed glass refraction, 8k commercial print quality'
  },
  {
    id: 'biz-swot-marketing',
    title: 'วางแผนกลยุทธ์การตลาดและเจาะกลุ่มลูกค้าไทย',
    category: 'business',
    icon: '📈',
    model: 'GPT-4o / Claude 3.5 Sonnet',
    targetType: 'chat',
    targetRoute: '/chatgpt',
    previewImage: 'https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=800&auto=format&fit=crop&q=80',
    description: 'วิเคราะห์โอกาสทางการตลาด แผนคอนเทนต์ TikTok และสร้างแคมเปญการขายที่มี Conversion สูง',
    tags: ['Marketing', 'Strategy', 'TikTok', 'SME', 'Business Plan'],
    prompt: `ช่วยวางแผนกลยุทธ์การเปิดตัวสินค้าใหม่ในตลาดประเทศไทย:
1. วิเคราะห์จุดแข็ง จุดอ่อน และโอกาส (SWOT Analysis)
2. แผนคอนเทนต์ TikTok & Short-form video 30 วันแรกเพื่อสร้าง Brand Awareness
3. กลยุทธ์การตั้งราคาและโปรโมชั่นดึงดูดลูกค้าช่วงสัปดาห์เปิดตัว
4. การคำนวณ CAC (Customer Acquisition Cost) และ LTV เบื้องต้น`
  },
  {
    id: 'code-fullstack-architecture',
    title: 'ออกแบบสถาปัตยกรรม High-Performance Backend',
    category: 'coding',
    icon: '⚡',
    model: 'DeepSeek-R1 / Claude 3.5 Sonnet',
    targetType: 'chat',
    targetRoute: '/deepseek',
    previewImage: 'https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=800&auto=format&fit=crop&q=80',
    description: 'วางโครงสร้าง Clean Architecture สำหรับ REST & SSE Streaming ใน Go/Node.js พร้อม Redis Caching',
    tags: ['Coding', 'Architecture', 'Go', 'Backend', 'System Design'],
    prompt: `กรุณาออกแบบระบบและสถาปัตยกรรม (System Architecture) สำหรับ High-Concurrency AI Gateway:
1. แนะนำ Clean Architecture folder structure สำหรับ Go (Gin / Chi)
2. วาง Flow การจัดการ Rate Limit และ Quota ด้วย Redis Sliding Window
3. โค้ดตัวอย่างการทำ SSE Streaming chat completion แบบ Non-blocking
4. แนะนำวิธีทำ Graceful Shutdown และ Circuit Breaker ป้องกัน Upstream ล่ม`
  },
  {
    id: 'video-drone-shot',
    title: 'วิดีโอโดรนบินผ่านเกาะเขตร้อนกลางทะเล',
    category: 'video',
    icon: '🎬',
    model: 'Luma / Kling / Sora',
    targetType: 'video',
    targetRoute: '/luma',
    previewImage: 'https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=800&auto=format&fit=crop&q=80',
    description: 'มุมมองโดรนมุมกว้างบินลอดผ่านหน้าผาหินปูนลงสู่หาดทรายขาวและน้ำทะเลสีเทอร์ควอยซ์สดใส',
    tags: ['Video', 'Drone', 'Cinematic', 'Island', '4K'],
    prompt:
      'Cinematic FPV drone shot sweeping gracefully through majestic karst limestone cliffs of southern Thailand, diving down toward pristine white sand beach and crystal turquoise lagoon, golden hour sun flare, smooth 60fps motion, ultra realistic'
  }
];
