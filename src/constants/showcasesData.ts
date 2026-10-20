import type { IShowcase } from '@/models';

export const STATIC_SHOWCASES: IShowcase[] = [
  {
    id: 'sc-cyberpunk-thai-girl',
    service: 'flux',
    task_id: 'task-sc-01',
    data: {
      type: 'image',
      presentation: {
        title: 'Cyberpunk Portrait in Neo-Bangkok',
        description: 'ภาพถ่ายพอร์ตเทรตสาวไซเบอร์พังก์ท่ามกลางแสงไฟนีออนสไตล์กรุงเทพฯ ยามค่ำคืน'
      },
      request: {
        prompt:
          'Cinematic portrait of a Thai cyberpunk woman in rain-soaked street, vibrant cyan and magenta neon lights, hyper-detailed skin texture, shallow depth of field, f/1.4, 85mm lens, volumetric smoke, photorealistic, 8k resolution',
        model: 'flux.1-pro',
        aspect_ratio: '3:4',
        size: '768x1024'
      },
      response: {
        data: [
          {
            url: 'https://images.unsplash.com/photo-1578632767115-351597cf2477?w=1080&auto=format&fit=crop&q=80',
            image_url: 'https://images.unsplash.com/photo-1578632767115-351597cf2477?w=1080&auto=format&fit=crop&q=80'
          }
        ]
      }
    }
  },
  {
    id: 'sc-macro-lotus-waterdrop',
    service: 'midjourney',
    task_id: 'task-sc-02',
    data: {
      type: 'image',
      presentation: {
        title: 'Morning Dew on Sacred Lotus',
        description: 'ภาพมาโครหยดน้ำค้างประกายเพชรบนกลีบดอกบัวสีชมพู สะท้อนแสงแดดยามเช้า'
      },
      request: {
        prompt:
          'Extreme macro photography of crystal clear morning water droplets on delicate pink lotus petal, refracted golden sunlight, shallow depth of field, sharp focus, 8k resolution, National Geographic style',
        model: 'midjourney-v6.1',
        aspect_ratio: '1:1',
        size: '1024x1024'
      },
      response: {
        data: [
          {
            url: 'https://images.unsplash.com/photo-1518531933037-91b2f5f229cc?w=1080&auto=format&fit=crop&q=80',
            image_url: 'https://images.unsplash.com/photo-1518531933037-91b2f5f229cc?w=1080&auto=format&fit=crop&q=80'
          }
        ]
      }
    }
  },
  {
    id: 'sc-ghibli-teahouse',
    service: 'openai',
    task_id: 'task-sc-03',
    data: {
      type: 'image',
      presentation: {
        title: 'Studio Ghibli Hillside Tea House',
        description: 'ภาพวาดอนิเมะบ้านน้ำชาบนเนินเขา แดดยามบ่าย แมวนอนริมหน้าต่าง อบอุ่นสบายใจ'
      },
      request: {
        prompt:
          'Studio Ghibli aesthetic cozy hillside wooden teahouse in summer, sunlight streaming through large open windows, lush green potted plants, sleeping calico cat on windowsill, steaming green tea, vibrant watercolor textures',
        model: 'dall-e-3',
        aspect_ratio: '16:9',
        size: '1792x1024'
      },
      response: {
        data: [
          {
            url: 'https://images.unsplash.com/photo-1554118811-1e0d58224f24?w=1080&auto=format&fit=crop&q=80',
            image_url: 'https://images.unsplash.com/photo-1554118811-1e0d58224f24?w=1080&auto=format&fit=crop&q=80'
          }
        ]
      }
    }
  },
  {
    id: 'sc-tropical-luxury-villa',
    service: 'flux',
    task_id: 'task-sc-04',
    data: {
      type: 'image',
      presentation: {
        title: 'Minimalist Seafront Villa Phuket',
        description: 'สถาปัตยกรรมวิลล่าสุดหรูริมหน้าผา วิวทะเลพระอาทิตย์ตกพร้อมสระว่ายน้ำอินฟินิตี้'
      },
      request: {
        prompt:
          'Architectural photography of modern minimalist luxury tropical concrete villa overlooking turquoise ocean, infinity edge pool reflecting golden sunset clouds, teak wood accents, lush exotic garden, editorial photoshoot',
        model: 'flux.1-schnell',
        aspect_ratio: '16:9',
        size: '1920x1080'
      },
      response: {
        data: [
          {
            url: 'https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=1080&auto=format&fit=crop&q=80',
            image_url: 'https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=1080&auto=format&fit=crop&q=80'
          }
        ]
      }
    }
  },
  {
    id: 'sc-perfume-product-render',
    service: 'openai',
    task_id: 'task-sc-05',
    data: {
      type: 'image',
      presentation: {
        title: 'Luxury Amber Perfume 3D Commercial',
        description: 'ภาพถ่ายผลิตภัณฑ์ขวดน้ำหอมระดับพรีเมียมบนแท่นหินอ่อนธรรมชาติพร้อมแสงสตูดิโอ'
      },
      request: {
        prompt:
          'Luxury commercial product photography of an amber glass perfume bottle resting on raw travertine marble slab, soft crystal water ripples, delicate studio rim lighting, luxury advertising visual, 8k resolution',
        model: 'dall-e-3',
        aspect_ratio: '1:1',
        size: '1024x1024'
      },
      response: {
        data: [
          {
            url: 'https://images.unsplash.com/photo-1592945403244-b3fbafd7f539?w=1080&auto=format&fit=crop&q=80',
            image_url: 'https://images.unsplash.com/photo-1592945403244-b3fbafd7f539?w=1080&auto=format&fit=crop&q=80'
          }
        ]
      }
    }
  },
  {
    id: 'sc-futuristic-mecha-titan',
    service: 'seedream',
    task_id: 'task-sc-06',
    data: {
      type: 'image',
      presentation: {
        title: 'Advanced Titanium Mech Warrior',
        description: 'การออกแบบหุ่นรบไซเบอร์เนติกเกราะไททาเนียมขาวพร้อมระบบพลังงานแสงออโรร่า'
      },
      request: {
        prompt:
          'Futuristic combat mech robot standing in hangar, matte white and dark titanium armor, glowing energy lines, detailed joints and hydraulics, dramatic rim light, ray tracing, unreal engine 5 render',
        model: 'seedream-v3',
        aspect_ratio: '3:4',
        size: '768x1024'
      },
      response: {
        data: [
          {
            url: 'https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?w=1080&auto=format&fit=crop&q=80',
            image_url: 'https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?w=1080&auto=format&fit=crop&q=80'
          }
        ]
      }
    }
  }
];
