import math
from PIL import Image, ImageDraw, ImageFont, ImageFilter

def draw_gloss_highlight(draw, box, color=(255, 255, 255, 20)):
    # Subtle diagonal glossy streak
    x1, y1, x2, y2 = box
    w = x2 - x1
    h = y2 - y1
    polygon = [(x1, y1), (x1 + w*0.4, y1), (x1, y1 + h*0.6)]
    draw.polygon(polygon, fill=color)

def generate_enhanced_manual_cover(output_path):
    width, height = 1024, 1024
    canvas = Image.new("RGBA", (width, height), (23, 22, 15, 255))
    draw = ImageDraw.Draw(canvas)

    # 1. Background: Dark warm slate gradient with subtle radial glow
    for y in range(height):
        t = y / height
        r = int(23 * (1 - t*0.4))
        g = int(22 * (1 - t*0.4))
        b = int(15 * (1 - t*0.4))
        draw.line([(0, y), (width, y)], fill=(r, g, b, 255))

    # Radial ambient spotlight behind book
    spotlight = Image.new("RGBA", (width, height), (0,0,0,0))
    sdraw = ImageDraw.Draw(spotlight)
    sdraw.ellipse([150, 100, 874, 824], fill=(255, 75, 31, 75))
    spotlight = spotlight.filter(ImageFilter.GaussianBlur(130))
    canvas = Image.alpha_composite(canvas, spotlight)

    # Subtle tech grid pattern in background
    for i in range(0, width, 50):
        draw.line([(i, 0), (i, height)], fill=(236, 231, 222, 8), width=1)
        draw.line([(0, i), (width, i)], fill=(236, 231, 222, 8), width=1)

    # 2. 3D Book Shadow
    shadow = Image.new("RGBA", (width, height), (0,0,0,0))
    sh_draw = ImageDraw.Draw(shadow)
    # Isometric drop shadow shape
    sh_draw.polygon([
        (280, 830), (740, 830), (810, 910), (210, 910)
    ], fill=(0, 0, 0, 190))
    shadow = shadow.filter(ImageFilter.GaussianBlur(35))
    canvas = Image.alpha_composite(canvas, shadow)

    # 3. Book 3D Structure
    # Pages Stack (Right side thickness)
    p_x1, p_y1, p_x2, p_y2 = 735, 150, 775, 830
    draw.polygon([(p_x1, p_y1 + 15), (p_x2, p_y1 + 30), (p_x2, p_y2 + 15), (p_x1, p_y2)], fill=(225, 218, 202, 255))
    # Page lines
    for ly in range(p_y1 + 25, p_y2, 7):
        draw.line([(p_x1, ly), (p_x2, ly + 15)], fill=(185, 176, 160, 255), width=1)

    # Front Cover
    b_x1, b_y1, b_x2, b_y2 = 270, 140, 735, 830
    
    # Book Cover Background (Matte Dark Charcoal with Ember Accent)
    draw.rectangle([b_x1, b_y1, b_x2, b_y2], fill=(14, 13, 8, 255), outline=(255, 75, 31, 255), width=3)

    # Spine (Left Edge)
    draw.rectangle([b_x1, b_y1, b_x1 + 40, b_y2], fill=(255, 75, 31, 255))
    draw.rectangle([b_x1 + 40, b_y1, b_x1 + 48, b_y2], fill=(228, 174, 35, 255))

    # Inner Frame
    draw.rectangle([b_x1 + 70, b_y1 + 35, b_x2 - 35, b_y2 - 35], outline=(236, 231, 222, 50), width=1)

    try:
        f_badge = ImageFont.truetype("arialbd.ttf", 18)
        f_title1 = ImageFont.truetype("arialbd.ttf", 64)
        f_title2 = ImageFont.truetype("arialbd.ttf", 68)
        f_sub = ImageFont.truetype("arialbd.ttf", 26)
        f_list = ImageFont.truetype("arial.ttf", 22)
        f_footer = ImageFont.truetype("arialbd.ttf", 22)
    except:
        f_badge = f_title1 = f_title2 = f_sub = f_list = f_footer = ImageFont.load_default()

    # Badge Top
    draw.rectangle([b_x1 + 70, b_y1 + 55, b_x1 + 360, b_y1 + 92], fill=(228, 174, 35, 255))
    draw.text((b_x1 + 85, b_y1 + 62), "MANUAL DO COACH • ED. 2026", fill=(14, 13, 8, 255), font=f_badge)

    # Title
    draw.text((b_x1 + 70, b_y1 + 125), "MANUAL DO", fill=(236, 231, 222, 255), font=f_title1)
    draw.text((b_x1 + 70, b_y1 + 200), "COACH", fill=(255, 75, 31, 255), font=f_title2)

    # Accent Line
    draw.line([(b_x1 + 70, b_y1 + 295), (b_x2 - 50, b_y1 + 295)], fill=(255, 75, 31, 255), width=4)

    # Subtitle
    draw.text((b_x1 + 70, b_y1 + 320), "FISIOLOGIA & PERIODIZAÇÃO", fill=(228, 174, 35, 255), font=f_sub)
    draw.text((b_x1 + 70, b_y1 + 360), "TREINO FUNCIONAL HYROX", fill=(236, 231, 222, 210), font=f_sub)

    # Feature List Box
    draw.rectangle([b_x1 + 70, b_y1 + 420, b_x2 - 50, b_y1 + 600], fill=(23, 22, 15, 255), outline=(255, 75, 31, 100), width=2)
    items = [
        "✔ 150 Páginas de Fundamentação",
        "✔ Fisiologia & Periodização Funcional",
        "✔ Prevenção de Lesões nas 8 Estações",
        "✔ Tabelas de Progressão Passo a Passo"
    ]
    for idx, item in enumerate(items):
        draw.text((b_x1 + 90, b_y1 + 440 + idx*40), item, fill=(236, 231, 222, 240), font=f_list)

    # Bottom Seal
    draw.rectangle([b_x1 + 70, b_y2 - 90, b_x2 - 50, b_y2 - 45], fill=(255, 75, 31, 255))
    draw.text((b_x1 + 115, b_y2 - 82), "PDF DIGITAL • ACESSO IMEDIATO", fill=(255, 255, 255, 255), font=f_footer)

    # Gloss overlay
    draw_gloss_highlight(draw, (b_x1, b_y1, b_x2, b_y2))

    canvas.save(output_path, "PNG")


def generate_enhanced_daily_wod_cover(output_path):
    width, height = 1024, 1024
    canvas = Image.new("RGBA", (width, height), (14, 13, 8, 255))
    draw = ImageDraw.Draw(canvas)

    # Background gradient
    for y in range(height):
        t = y / height
        r = int(14 + (28 - 14) * t)
        g = int(13 + (24 - 13) * t)
        b = int(8 + (16 - 8) * t)
        draw.line([(0, y), (width, y)], fill=(r, g, b, 255))

    # Gold radial spotlight
    spotlight = Image.new("RGBA", (width, height), (0,0,0,0))
    sdraw = ImageDraw.Draw(spotlight)
    sdraw.ellipse([150, 100, 874, 824], fill=(228, 174, 35, 70))
    spotlight = spotlight.filter(ImageFilter.GaussianBlur(130))
    canvas = Image.alpha_composite(canvas, spotlight)

    # Tech circle rings
    draw.ellipse([160, 160, 864, 864], outline=(228, 174, 35, 35), width=2)
    draw.ellipse([190, 190, 834, 834], outline=(255, 75, 31, 45), width=1)

    # Card Shadow
    shadow = Image.new("RGBA", (width, height), (0,0,0,0))
    sh_draw = ImageDraw.Draw(shadow)
    sh_draw.rectangle([210, 150, 814, 870], fill=(0, 0, 0, 190))
    shadow = shadow.filter(ImageFilter.GaussianBlur(35))
    canvas = Image.alpha_composite(canvas, shadow)

    # Main Card Container
    c_x1, c_y1, c_x2, c_y2 = 230, 140, 794, 860
    draw.rectangle([c_x1, c_y1, c_x2, c_y2], fill=(23, 22, 15, 255), outline=(228, 174, 35, 255), width=3)
    draw.rectangle([c_x1, c_y1, c_x2, c_y1 + 14], fill=(228, 174, 35, 255))

    try:
        f_num = ImageFont.truetype("arialbd.ttf", 115)
        f_h1 = ImageFont.truetype("arialbd.ttf", 52)
        f_h2 = ImageFont.truetype("arialbd.ttf", 56)
        f_sub = ImageFont.truetype("arialbd.ttf", 26)
        f_list = ImageFont.truetype("arial.ttf", 22)
        f_badge = ImageFont.truetype("arialbd.ttf", 22)
        f_tag = ImageFont.truetype("arialbd.ttf", 18)
    except:
        f_num = f_h1 = f_h2 = f_sub = f_list = f_badge = f_tag = ImageFont.load_default()

    # Top Tag
    draw.rectangle([c_x2 - 250, c_y1 + 35, c_x2 - 35, c_y1 + 75], fill=(255, 75, 31, 255))
    draw.text((c_x2 - 235, c_y1 + 43), "🔥 MAIS VENDIDO", fill=(255, 255, 255, 255), font=f_tag)

    # Big "250" Number
    draw.text((c_x1 + 45, c_y1 + 45), "250", fill=(255, 75, 31, 255), font=f_num)
    draw.text((c_x1 + 300, c_y1 + 75), "AULAS", fill=(236, 231, 222, 255), font=f_h1)
    draw.text((c_x1 + 300, c_y1 + 135), "PRONTAS", fill=(228, 174, 35, 255), font=f_h2)

    # Line
    draw.line([(c_x1 + 45, c_y1 + 215), (c_x2 - 45, c_y1 + 215)], fill=(228, 174, 35, 200), width=3)

    # Subtitle
    draw.text((c_x1 + 45, c_y1 + 240), "DAILY WOD • CATÁLOGO ANUAL", fill=(236, 231, 222, 255), font=f_sub)

    # Feature List
    feats = [
        "⏱️ 250 Treinos (1 pra cada dia útil do ano)",
        "🏋️ Aquecimento, Blocos & Tempos Definidos",
        "📊 3 Níveis de Adaptação (Iniciante ao Pro)",
        "⚡ Estruturado nas 8 Estações HYROX"
    ]

    for idx, ft in enumerate(feats):
        fy = c_y1 + 310 + idx*58
        draw.rectangle([c_x1 + 45, fy, c_x2 - 45, fy + 48], fill=(14, 13, 8, 255), outline=(255, 75, 31, 100), width=1)
        draw.text((c_x1 + 65, fy + 12), ft, fill=(236, 231, 222, 240), font=f_list)

    # Bottom Seal
    draw.rectangle([c_x1 + 45, c_y2 - 95, c_x2 - 45, c_y2 - 45], fill=(228, 174, 35, 255))
    draw.text((c_x1 + 95, c_y2 - 82), "ACESSO DIGITAL IMEDIATO • DAILY WOD", fill=(14, 13, 8, 255), font=f_badge)

    # Gloss overlay
    draw_gloss_highlight(draw, (c_x1, c_y1, c_x2, c_y2))

    canvas.save(output_path, "PNG")


if __name__ == "__main__":
    generate_enhanced_manual_cover("assets/images/manual_coach_cover.png")
    generate_enhanced_daily_wod_cover("assets/images/daily_wod_cover.png")
    print("Enhanced original covers generated successfully!")
