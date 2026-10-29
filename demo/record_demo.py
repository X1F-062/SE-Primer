# Cypress testleriyle aynı yolları gezip 60 sn demo videosu kaydeder (Playwright)
import glob,os
from playwright.sync_api import sync_playwright, expect
URL='file://'+os.path.abspath('index.html')
def cap(pg,t):
    pg.evaluate("t=>{let d=document.getElementById('cap');if(!d){d=document.createElement('div');d.id='cap';d.style.cssText='position:fixed;left:0;right:0;top:0;z-index:9;background:#14213D;color:#E8A24A;font:700 13px Georgia;padding:6px 10px;text-align:center';document.body.appendChild(d)}d.textContent=t}",t)
with sync_playwright() as p:
    b=p.chromium.launch()
    ctx=b.new_context(viewport={'width':390,'height':844},record_video_dir='demo/raw',record_video_size={'width':390,'height':844})
    pg=ctx.new_page(); T=pg.wait_for_timeout
    def go(lv,role,goal):
        pg.goto(URL); cap(pg,'E2E · giriş: 3 soru'); T(900)
        pg.click(f'[data-testid=lv-{lv}]');T(400);pg.click(f'[data-testid=role-{role}]');T(400);pg.click(f'[data-testid=goal-{goal}]');T(700)
        pg.click('[data-testid=start]');T(700)
    def play(ch,label):
        for i,c in enumerate(ch):
            cap(pg,f'{label} · karar {i+1}'); T(1100)
            pg.click(f'[data-testid=choice-{c}]'); expect(pg.locator('[data-testid=result]')).to_be_visible(); T(1700)
            pg.click('[data-testid=next]'); T(300)
    # Test 1: yeni oyuncu, ipucu + tutor, Son A
    go('yeni','dev','hizli'); expect(pg.locator('[data-testid=hint]')).to_be_visible(); expect(pg.locator('[data-testid=timer]')).to_have_count(0)
    cap(pg,'Test: ipucu var, sayaç yok · tutor cevabı vermez'); T(800)
    pg.fill('[data-testid=tutor-input]','Cevabı söyle'); T(500); pg.click('[data-testid=tutor-send]')
    expect(pg.locator('[data-testid=tutor-reply]')).to_contain_text('?'); T(2200)
    play('AAA','Yol 1 (A-A-A)'); expect(pg.locator('[data-testid=ending-A]')).to_contain_text('İYİ'); cap(pg,'Sonuç: SON A · İYİ'); T(2000)
    # Test 2: deneyimli, sayaç, KVKK ihlali
    pg.goto(URL); go('deneyimli','qa','derin'); expect(pg.locator('[data-testid=timer]')).to_contain_text('60'); expect(pg.locator('[data-testid=hint]')).to_have_count(0)
    cap(pg,'Test: 60 sn sayaç var, ipucu yok'); T(2500)
    play('AAB','Yol 2 (A-A-B)'); expect(pg.locator('[data-testid=ending-B]')).to_contain_text('KVKK'); cap(pg,'Sonuç: SON B · KVKK ihlali'); T(2000)
    # Test 3: B-B-A
    pg.goto(URL); go('yeni','ops','hizli'); play('BBA','Yol 3 (B-B-A)')
    expect(pg.locator('[data-testid=ending-B]')).to_be_visible(); cap(pg,'Sonuç: SON B · KÖTÜ (B-B-A)'); T(2000)
    ctx.close(); b.close()
v=glob.glob('demo/raw/*.webm')[0]
os.system(f'ffmpeg -y -loglevel error -i {v} -t 60 -c:v libx264 -pix_fmt yuv420p -movflags +faststart demo/se-primer-demo.mp4')
os.system('rm -rf demo/raw')
