from PIL import Image, ImageDraw, ImageFont, ImageFilter
import math

def build_photo_manual_cover(output_path):
    # Load real high-res photography base
    base = Image.open("assets/images/differentiators_coach.png").convert("RGBA")
    
    # Crop square center 1024x1024
    w, h = base.size
    min_dim = min(w, h)
    left = (w - min_dim) // 2
    top = (h - min_dim) // 2
    base = base.crop((left, top, left + min_dim, top + min_dim)).resize((1024, 1024), Image.Resampling.LANCZOS)

    # Apply rich dark cinematic overlay with warm ember vignette
    overlay = Image.new("RGBA", (1024, 1024), (0, 0, 0, 0))
    odraw = ImageDraw.Draw(overlay)

    # Dark gradient from top to bottom
    for y in range(1024):
        alpha = int(140 + 100 * (y / 1024))
        odraw.line([(0, y), (1024, y)], fill=(14, 13, 8, alpha))

    # Ember radial highlight at center-left
    glow = Image.new("RGBA", (1024, 1024), (0,0,0,0))
    gdraw = ImageDraw.Draw(glow)
    gdraw.ellipse([100, 200, 700, 800], fill=(255, 75, 31, 80))
    glow = glow.filter(ImageFilter.GaussianBlur(100))

    base = Image.alpha_composite(base, overlay)
    base = Image.alpha_composite(base, glow)

    # Create Floating Glass Card
    card_w, card_h = 580, 760
    card_x, card_y = 222, 132

    # Card Drop Shadow
    shadow = Image.new("RGBA", (1024, 1024), (0,0,0,0))
    sdraw = ImageDraw.Draw(shadow)
    sdraw.rounded_rectangle([card_x, card_y + 20, card_x + card_w, card_y + card_h + 20], radius=16, fill=(0, 0, 0, 180))
    shadow = shadow.filter(ImageFilter.GaussianBlur(25))
    base = Image.alpha_composite(base, shadow)

    # Glass Card Body (semi-transparent dark ink with ember border)
    card = Image.new("RGBA", (card_w, card_h), (0,0,0,0))
    cdraw = ImageDraw.Draw(card)
    cdraw.rounded_rectangle([0, 0, card_w, card_h], radius=16, fill=(18, 17, 12, 225), outline=(255, 75, 31, 220), width=3)
    cdraw.rectangle([0, 0, card_w, 8], fill=(255, 75, 31, 255))
    cdraw.rounded_rectangle([15, 15, card_w - 15, card_h - 15], radius=12, outline=(236, 231, 222, 35), width=1)

    try:
        f_tag = ImageFont.truetype("arialbd.ttf", 20)
        f_h1 = ImageFont.truetype("arialbd.ttf", 52)
        f_sub = ImageFont.truetype("arialbd.ttf", 26)
        f_body = ImageFont.truetype("arial.ttf", 22)
        f_badge = ImageFont.truetype("arialbd.ttf", 22)
    except:
        f_tag = f_h1 = f_sub = f_body = f_badge = ImageFont.load_default()

    # Tag Top
    cdraw.rectangle([35, 45, 330, 82], fill=(228, 174, 35, 255))
    cdraw.text((48, 52), "MANUAL DO COACH", fill=(14, 13, 8, 255), font=f_tag)

    # Main Headline
    cdraw.text((35, 115), "GUIA TÉCNICO", fill=(236, 231, 222, 255), font=f_h1)
    cdraw.text((35, 175), "HYROX 2026", fill=(255, 75, 31, 255), font=f_h1)

    # Line
    cdraw.line([(35, 255), (card_w - 35, 255)], fill=(255, 75, 31, 255), width=3)

    # Subtitle
    cdraw.text((35, 275), "FISIOLOGIA & PERIODIZAÇÃO", fill=(228, 174, 35, 255), font=f_sub)

    # Features
    feats = [
        "• 150 Páginas em Formato PDF Digital",
        "• Metodologia das 8 Estações Oficiais",
        "• Guia de Prevenção de Lesões",
        "• Montagem de Mesociclo Passo a Passo"
    ]
    for i, ft in enumerate(feats):
        cdraw.text((35, 335 + i * 46), ft, fill=(236, 231, 222, 230), font=f_body)

    # Bottom Seal
    cdraw.rounded_rectangle([35, card_h - 105, card_w - 35, card_h - 45], radius=8, fill=(255, 75, 31, 255))
    cdraw.text((65, card_h - 86), "DOWNLOAD DIGITAL IMEDIATO • 150 PÁGS", fill=(255, 255, 255, 255), font=f_badge)

    base.paste(card, (card_x, card_y), card)
    base.save(output_path, "PNG")


def build_photo_daily_wod_cover(output_path):
    # Load real high-res photography base
    base = Image.open("assets/images/results_stats_bg.png").convert("RGBA")
    
    w, h = base.size
    min_dim = min(w, h)
    left = (w - min_dim) // 2
    top = (h - min_dim) // 2
    base = base.crop((left, top, left + min_dim, top + min_dim)).resize((1024, 1024), Image.Resampling.LANCZOS)

    # Dark overlay with gold/ember vignette
    overlay = Image.new("RGBA", (1024, 1024), (0, 0, 0, 0))
    odraw = ImageDraw.Draw(overlay)

    for y in range(1024):
        alpha = int(150 + 90 * (y / 1024))
        odraw.line([(0, y), (1024, y)], fill=(14, 13, 8, alpha))

    glow = Image.new("RGBA", (1024, 1024), (0,0,0,0))
    gdraw = ImageDraw.Draw(glow)
    gdraw.ellipse([300, 200, 900, 800], fill=(228, 174, 35, 70))
    glow = glow.filter(ImageFilter.GaussianBlur(120))

    base = Image.alpha_composite(base, overlay)
    base = Image.alpha_composite(base, glow)

    # Create Floating Glass Card
    card_w, card_h = 580, 760
    card_x, card_y = 222, 132

    # Card Drop Shadow
    shadow = Image.new("RGBA", (1024, 1024), (0,0,0,0))
    sdraw = ImageDraw.Draw(shadow)
    sdraw.rounded_rectangle([card_x, card_y + 20, card_x + card_w, card_y + card_h + 20], radius=16, fill=(0, 0, 0, 180))
    shadow = shadow.filter(ImageFilter.GaussianBlur(25))
    base = Image.alpha_composite(base, shadow)

    # Glass Card Body
    card = Image.new("RGBA", (card_w, card_h), (0,0,0,0))
    cdraw = ImageDraw.Draw(card)
    cdraw.rounded_rectangle([0, 0, card_w, card_h], radius=16, fill=(18, 17, 12, 225), outline=(228, 174, 35, 230), width=3)
    cdraw.rectangle([0, 0, card_w, 8], fill=(228, 174, 35, 255))
    cdraw.rounded_rectangle([15, 15, card_w - 15, card_h - 15], radius=12, outline=(236, 231, 222, 35), width=1)

    try:
        f_num = ImageFont.truetype("arialbd.ttf", 96)
        f_h1 = ImageFont.truetype("arialbd.ttf", 46)
        f_sub = ImageFont.truetype("arialbd.ttf", 26)
        f_body = ImageFont.truetype("arial.ttf", 22)
        f_badge = ImageFont.truetype("arialbd.ttf", 22)
        f_tag = ImageFont.truetype("arialbd.ttf", 18)
    except:
        f_num = f_h1 = f_sub = f_body = f_badge = f_tag = ImageFont.load_default()

    # Tag Top Right
    cdraw.rectangle([card_w - 235, 40, card_w - 30, 78], fill=(255, 75, 31, 255))
    cdraw.text((card_w - 220, 48), "CATÁLOGO 2026", fill=(255, 255, 255, 255), font=f_tag)

    # Big Number + Title
    cdraw.text((35, 40), "250", fill=(255, 75, 31, 255), font=f_num)
    cdraw.text((230, 50), "DAILY WODs", fill=(236, 231, 222, 255), font=f_h1)
    cdraw.text((230, 105), "AULAS PRONTAS", fill=(228, 174, 35, 255), font=f_h1)

    # Line
    cdraw.line([(35, 175), (card_w - 35, 175)], fill=(228, 174, 35, 255), width=3)

    # Subtitle
    cdraw.text((35, 195), "COLEÇÃO ANUAL COMPLETA", fill=(236, 231, 222, 255), font=f_sub)

    # Features Box
    feats = [
        "⚡ 250 Treinos (1 para cada dia útil)",
        "⏱️ Aquecimento, Tempos & Blocos",
        "📊 3 Níveis de Adaptação por Aula",
        "🎯 Foco nas 8 Estações Oficial HYROX"
    ]
    for i, ft in enumerate(feats):
        fy = 250 + i * 56
        cdraw.rounded_rectangle([35, fy, card_w - 35, fy + 44], radius=6, fill=(14, 13, 8, 255), outline=(255, 75, 31, 90), width=1)
        cdraw.text((50, fy + 10), ft, fill=(236, 231, 222, 235), font=f_body)

    # Bottom Seal
    cdraw.rounded_rectangle([35, card_h - 105, card_w - 35, card_h - 45], radius=8, fill=(228, 174, 35, 255))
    cdraw.text((70, card_h - 86), "APLIQUE AMANHÃ • ACESSO IMEDIATO", fill=(14, 13, 8, 255), font=f_badge)

    base.paste(card, (card_x, card_y), card)
    base.save(output_path, "PNG")


if __name__ == "__main__":
    build_photo_manual_cover("assets/images/manual_coach_cover.png")
    build_photo_daily_wod_cover("assets/images/daily_wod_cover.png")
    print("Photo composite covers generated successfully!")
