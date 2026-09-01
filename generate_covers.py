import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

def create_manual_coach_cover(filename):
    width, height = 1024, 1024
    img = Image.new("RGBA", (width, height), (23, 22, 15, 255))
    draw = ImageDraw.Draw(img)

    # Background gradient & ambient glow
    for y in range(height):
        ratio = y / height
        r = int(23 * (1 - ratio*0.5))
        g = int(22 * (1 - ratio*0.5))
        b = int(15 * (1 - ratio*0.5))
        draw.line([(0, y), (width, y)], fill=(r, g, b, 255))

    # Radial ember glow behind book
    glow = Image.new("RGBA", (width, height), (0,0,0,0))
    glow_draw = ImageDraw.Draw(glow)
    glow_draw.ellipse([200, 150, 824, 774], fill=(255, 75, 31, 70))
    glow = glow.filter(ImageFilter.GaussianBlur(120))
    img.alpha_composite(glow)

    # Grid pattern lines
    for x in range(0, width, 40):
        draw.line([(x, 0), (x + 200, height)], fill=(255, 75, 31, 8), width=1)

    # Shadow under book
    shadow = Image.new("RGBA", (width, height), (0,0,0,0))
    sh_draw = ImageDraw.Draw(shadow)
    sh_draw.polygon([(260, 840), (800, 840), (840, 920), (220, 920)], fill=(0, 0, 0, 180))
    shadow = shadow.filter(ImageFilter.GaussianBlur(30))
    img.alpha_composite(shadow)

    # 3D Book Base
    book_x1, book_y1, book_x2, book_y2 = 280, 140, 760, 820

    # Book pages thickness 3D effect
    draw.rectangle([book_x2, book_y1 + 15, book_x2 + 35, book_y2 - 15], fill=(225, 218, 202, 255))
    for p in range(book_y1 + 25, book_y2 - 25, 6):
        draw.line([(book_x2, p), (book_x2 + 35, p)], fill=(180, 172, 155, 255), width=1)

    # Book cover main rect
    draw.rectangle([book_x1, book_y1, book_x2, book_y2], fill=(14, 13, 8, 255), outline=(255, 75, 31, 255), width=3)
    
    # Spine accent line
    draw.rectangle([book_x1, book_y1, book_x1 + 35, book_y2], fill=(255, 75, 31, 255))
    draw.rectangle([book_x1 + 35, book_y1, book_x1 + 42, book_y2], fill=(228, 174, 35, 255))

    # Inner decorative border
    draw.rectangle([book_x1 + 65, book_y1 + 35, book_x2 - 35, book_y2 - 35], outline=(236, 231, 222, 60), width=1)

    # Try loading fonts, fallback to default
    try:
        font_huge = ImageFont.truetype("arialbd.ttf", 64)
        font_large = ImageFont.truetype("arialbd.ttf", 44)
        font_sub = ImageFont.truetype("arialbd.ttf", 26)
        font_tag = ImageFont.truetype("arial.ttf", 20)
    except:
        font_huge = font_large = font_sub = font_tag = ImageFont.load_default()

    # Header tag
    draw.rectangle([book_x1 + 65, book_y1 + 60, book_x1 + 340, book_y1 + 95], fill=(228, 174, 35, 255))
    draw.text((book_x1 + 80, book_y1 + 66), "EDITION 2026 • MANUAL TÉCNICO", fill=(14, 13, 8, 255), font=font_tag)

    # Main Title
    draw.text((book_x1 + 65, book_y1 + 130), "MANUAL DO", fill=(236, 231, 222, 255), font=font_huge)
    draw.text((book_x1 + 65, book_y1 + 205), "COACH", fill=(255, 75, 31, 255), font=font_huge)

    # Divider line
    draw.line([(book_x1 + 65, book_y1 + 295), (book_x2 - 65, book_y1 + 295)], fill=(255, 75, 31, 255), width=4)

    # Subtitle / Features
    draw.text((book_x1 + 65, book_y1 + 320), "PERIODIZAÇÃO & FISIOLOGIA", fill=(228, 174, 35, 255), font=font_sub)
    draw.text((book_x1 + 65, book_y1 + 360), "TREINO FUNCIONAL HYROX", fill=(236, 231, 222, 220), font=font_sub)

    # 8 Stations Bullet points box
    draw.rectangle([book_x1 + 65, book_y1 + 420, book_x2 - 65, book_y1 + 610], fill=(23, 22, 15, 255), outline=(255, 75, 31, 100), width=2)
    stations = [
        "✓ 150 Páginas de Fundamentação",
        "✓ Guias das 8 Estações Oficiais",
        "✓ Prevenção de Lesão & Carga",
        "✓ Tabelas de Mesociclo Prontas"
    ]
    for idx, st in enumerate(stations):
        draw.text((book_x1 + 85, book_y1 + 440 + idx*40), st, fill=(236, 231, 222, 240), font=font_tag)

    # Bottom Seal
    draw.rectangle([book_x1 + 65, book_y2 - 95, book_x2 - 65, book_y2 - 50], fill=(255, 75, 31, 255))
    draw.text((book_x1 + 110, book_y2 - 86), "FORMATO DIGITAL PDF • 150 PÁGS", fill=(255, 255, 255, 255), font=font_sub)

    img.save(filename, "PNG")

def create_daily_wod_cover(filename):
    width, height = 1024, 1024
    img = Image.new("RGBA", (width, height), (14, 13, 8, 255))
    draw = ImageDraw.Draw(img)

    # Background gradient
    for y in range(height):
        ratio = y / height
        r = int(14 + (30 - 14) * ratio)
        g = int(13 + (25 - 13) * ratio)
        b = int(8 + (15 - 8) * ratio)
        draw.line([(0, y), (width, y)], fill=(r, g, b, 255))

    # Gold radial glow
    glow = Image.new("RGBA", (width, height), (0,0,0,0))
    glow_draw = ImageDraw.Draw(glow)
    glow_draw.ellipse([150, 150, 874, 874], fill=(228, 174, 35, 60))
    glow = glow.filter(ImageFilter.GaussianBlur(130))
    img.alpha_composite(glow)

    # Decorative tech circle ring
    draw.ellipse([180, 180, 844, 844], outline=(228, 174, 35, 40), width=2)
    draw.ellipse([210, 210, 814, 814], outline=(255, 75, 31, 50), width=1)

    # Drop shadow under central card
    shadow = Image.new("RGBA", (width, height), (0,0,0,0))
    sh_draw = ImageDraw.Draw(shadow)
    sh_draw.rectangle([210, 190, 814, 854], fill=(0, 0, 0, 200))
    shadow = shadow.filter(ImageFilter.GaussianBlur(35))
    img.alpha_composite(shadow)

    # Central Box Card
    box_x1, box_y1, box_x2, box_y2 = 230, 170, 794, 830
    draw.rectangle([box_x1, box_y1, box_x2, box_y2], fill=(23, 22, 15, 255), outline=(228, 174, 35, 255), width=3)

    # Top accent bar
    draw.rectangle([box_x1, box_y1, box_x2, box_y1 + 16], fill=(228, 174, 35, 255))

    try:
        font_number = ImageFont.truetype("arialbd.ttf", 110)
        font_huge = ImageFont.truetype("arialbd.ttf", 54)
        font_large = ImageFont.truetype("arialbd.ttf", 36)
        font_sub = ImageFont.truetype("arialbd.ttf", 24)
        font_tag = ImageFont.truetype("arial.ttf", 20)
    except:
        font_number = font_huge = font_large = font_sub = font_tag = ImageFont.load_default()

    # Badge top right
    draw.rectangle([box_x2 - 240, box_y1 + 35, box_x2 - 30, box_y1 + 75], fill=(255, 75, 31, 255))
    draw.text((box_x2 - 225, box_y1 + 43), "ACESSO IMEDIATO", fill=(255, 255, 255, 255), font=font_tag)

    # Big Number "250"
    draw.text((box_x1 + 45, box_y1 + 50), "250", fill=(255, 75, 31, 255), font=font_number)
    draw.text((box_x1 + 290, box_y1 + 80), "AULAS", fill=(236, 231, 222, 255), font=font_huge)
    draw.text((box_x1 + 290, box_y1 + 140), "PRONTAS", fill=(228, 174, 35, 255), font=font_huge)

    # Divider line
    draw.line([(box_x1 + 45, box_y1 + 215), (box_x2 - 45, box_y1 + 215)], fill=(228, 174, 35, 180), width=3)

    # Subtitle
    draw.text((box_x1 + 45, box_y1 + 240), "CATÁLOGO COMPLETO DAILY WOD", fill=(236, 231, 222, 255), font=font_large)

    # Feature List Pills
    features = [
        "⏱️ Aquecimentos & Tempo Definidos",
        "🏋️ 8 Estações HYROX Mapeadas",
        "📊 3 Níveis de Adaptação (Iniciante ao Pro)",
        "⚡ 1 Aula Pronta para Cada Dia Útil do Ano"
    ]

    for idx, ft in enumerate(features):
        fy1 = box_y1 + 310 + idx*58
        fy2 = fy1 + 46
        draw.rectangle([box_x1 + 45, fy1, box_x2 - 45, fy2], fill=(14, 13, 8, 255), outline=(255, 75, 31, 100), width=1)
        draw.text((box_x1 + 65, fy1 + 10), ft, fill=(236, 231, 222, 240), font=font_sub)

    # Bottom Seal Button
    draw.rectangle([box_x1 + 45, box_y2 - 95, box_x2 - 45, box_y2 - 45], fill=(228, 174, 35, 255))
    draw.text((box_x1 + 100, box_y2 - 82), "COLEÇÃO ANUAL • APLIQUE AMANHÃ", fill=(14, 13, 8, 255), font=font_large)

    img.save(filename, "PNG")

if __name__ == "__main__":
    create_manual_coach_cover("assets/images/manual_coach_cover.png")
    create_daily_wod_cover("assets/images/daily_wod_cover.png")
    print("Covers updated successfully!")
