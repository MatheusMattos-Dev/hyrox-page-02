from PIL import Image, ImageDraw, ImageFont, ImageFilter
import math

def generate_open_manual_mockup(output_path):
    w, h = 1024, 1024
    img = Image.new("RGBA", (w, h), (38, 32, 26, 255))
    draw = ImageDraw.Draw(img)

    # 1. Wooden Desk Background Texture (Rich warm wood grain)
    for y in range(h):
        r = int(55 + 15 * math.sin(y * 0.05) + (y / h) * 10)
        g = int(42 + 12 * math.sin(y * 0.05) + (y / h) * 8)
        b = int(30 + 8 * math.sin(y * 0.05) + (y / h) * 5)
        draw.line([(0, y), (w, y)], fill=(r, g, b, 255))

    # Add subtle wood planks lines
    for x in range(0, w, 180):
        draw.line([(x, 0), (x, h)], fill=(25, 20, 15, 120), width=3)

    # Ambient vignetting
    vignette = Image.new("RGBA", (w, h), (0,0,0,0))
    vdraw = ImageDraw.Draw(vignette)
    for r_idx in range(500, 0, -10):
        alpha = int(140 * (1 - r_idx / 500))
        vdraw.ellipse([512 - r_idx*1.4, 512 - r_idx*1.4, 512 + r_idx*1.4, 512 + r_idx*1.4], fill=(0,0,0, alpha))
    vignette = vignette.filter(ImageFilter.GaussianBlur(60))
    img = Image.alpha_composite(img, vignette)

    # 2. Open Book Drop Shadow
    shadow = Image.new("RGBA", (w, h), (0,0,0,0))
    shdraw = ImageDraw.Draw(shadow)
    shdraw.polygon([(110, 220), (914, 220), (934, 840), (90, 840)], fill=(0, 0, 0, 200))
    shadow = shadow.filter(ImageFilter.GaussianBlur(35))
    img = Image.alpha_composite(img, shadow)

    # 3. Open Book Base (Left & Right Pages)
    # Book Dimensions: Left (130 -> 505), Right (519 -> 894), Top 200, Bottom 820
    draw = ImageDraw.Draw(img)

    # Book paper thickness (Bottom edges)
    draw.polygon([(120, 815), (505, 825), (505, 840), (110, 830)], fill=(215, 205, 190, 255))
    draw.polygon([(519, 825), (904, 815), (914, 830), (519, 840)], fill=(215, 205, 190, 255))

    # Left Page
    draw.polygon([(130, 200), (505, 210), (505, 825), (120, 815)], fill=(236, 231, 222, 255))
    # Right Page
    draw.polygon([(519, 210), (894, 200), (904, 815), (519, 825)], fill=(236, 231, 222, 255))

    # Center Spine Shadow
    spine_shadow = Image.new("RGBA", (w, h), (0,0,0,0))
    spdraw = ImageDraw.Draw(spine_shadow)
    spdraw.rectangle([495, 200, 529, 835], fill=(0, 0, 0, 90))
    spdraw.line([(512, 200), (512, 835)], fill=(0, 0, 0, 180), width=2)
    spine_shadow = spine_shadow.filter(ImageFilter.GaussianBlur(8))
    img = Image.alpha_composite(img, spine_shadow)
    draw = ImageDraw.Draw(img)

    # Load Fonts
    try:
        f_h1 = ImageFont.truetype("arialbd.ttf", 26)
        f_h2 = ImageFont.truetype("arialbd.ttf", 20)
        f_body = ImageFont.truetype("arial.ttf", 15)
        f_bold = ImageFont.truetype("arialbd.ttf", 15)
        f_tag = ImageFont.truetype("arialbd.ttf", 13)
    except:
        f_h1 = f_h2 = f_body = f_bold = f_tag = ImageFont.load_default()

    # --- LEFT PAGE CONTENT ---
    # Top Chapter Header Bar
    draw.rectangle([155, 235, 480, 280], fill=(255, 75, 31, 255))
    draw.text((170, 248), "MANUAL DO COACH: HYROX 2026", fill=(255, 255, 255, 255), font=f_h2)

    draw.text((155, 300), "Capítulo 2: Fisiologia & Periodização", fill=(23, 22, 15, 255), font=f_h1)
    
    body_l1 = [
        "O treinamento funcional estruturado para o HYROX exige a",
        "combinação exata entre capacidade aeróbica e força muscular",
        "resistente. A chave da periodização por mesociclo reside em:",
        "",
        "1. Aceleração de Recuperação Metabólica entre Estações",
        "2. Manutenção do Pace de Corrida (1KM) Sob Fadiga",
        "3. Eficiência Biomassa nos Exercícios de Arraste (Sled Push/Pull)"
    ]
    for i, line in enumerate(body_l1):
        draw.text((155, 345 + i*22), line, fill=(50, 48, 40, 255), font=f_body)

    # Station Diagram Box on Left Page
    draw.rectangle([155, 520, 480, 770], fill=(225, 218, 202, 255), outline=(255, 75, 31, 255), width=2)
    draw.rectangle([155, 520, 480, 550], fill=(23, 22, 15, 255))
    draw.text((165, 528), "ESTAÇÕES OFICIAIS DE TREINO", fill=(228, 174, 35, 255), font=f_tag)

    stations = [
        "01. SkiErg (1000m) • Foco Potência",
        "02. Sled Push (50m) • Carga Máxima",
        "03. Sled Pull (50m) • Tração Posterior",
        "04. Burpee Broad Jump (80m) • Plyo",
        "05. Rowing (1000m) • Ritmo Cardiovascular",
        "06. Farmers Carry (200m) • Pegada & Core",
        "07. Sandbag Lunges (100m) • Estabilidade",
        "08. Wall Balls (100 Reps) • Resistência"
    ]
    for idx, st in enumerate(stations):
        draw.text((165, 560 + idx*25), st, fill=(23, 22, 15, 255), font=f_tag)

    draw.text((155, 790), "GUIA TÉCNICO DO COACH  |  PÁG 34", fill=(120, 115, 100, 255), font=f_tag)

    # --- RIGHT PAGE CONTENT ---
    # Header Right
    draw.rectangle([545, 235, 870, 280], fill=(23, 22, 15, 255))
    draw.text((560, 248), "PREVENÇÃO DE LESÕES & PROGRESSÃO", fill=(228, 174, 35, 255), font=f_h2)

    draw.text((545, 300), "Ajuste de Carga & Biomecânica", fill=(23, 22, 15, 255), font=f_h1)

    body_r1 = [
        "Para evitar a sobrecarga articular nos movimentos de alto impacto",
        "(como Burpee Broad Jump e Wall Balls), aplique a tabela de",
        "progressão semanal abaixo antes de transicionar pro nível RX:",
    ]
    for i, line in enumerate(body_r1):
        draw.text((545, 345 + i*22), line, fill=(50, 48, 40, 255), font=f_body)

    # Table on Right Page
    draw.rectangle([545, 425, 870, 680], fill=(255, 255, 255, 255), outline=(23, 22, 15, 180), width=1)
    draw.rectangle([545, 425, 870, 460], fill=(255, 75, 31, 255))
    draw.text((555, 435), "SEMANA / MESOCICLO", fill=(255, 255, 255, 255), font=f_bold)
    draw.text((710, 435), "CARGA (%)", fill=(255, 255, 255, 255), font=f_bold)
    draw.text((800, 435), "VOLUME", fill=(255, 255, 255, 255), font=f_bold)

    table_data = [
        ("Semana 1 - Base Técnica", "60% RX", "3 Blocos"),
        ("Semana 2 - Adaptação Neuromuscular", "70% RX", "4 Blocos"),
        ("Semana 3 - Capacidade Específica", "85% RX", "4 Blocos"),
        ("Semana 4 - Simulado de Prova", "100% RX", "5 Blocos"),
        ("Semana 5 - Polimento (Tapering)", "50% RX", "2 Blocos")
    ]
    for idx, (s, c, v) in enumerate(table_data):
        ty = 470 + idx*40
        draw.line([(545, ty + 35), (870, ty + 35)], fill=(220, 215, 200, 255), width=1)
        draw.text((555, ty + 8), s, fill=(23, 22, 15, 255), font=f_tag)
        draw.text((715, ty + 8), c, fill=(255, 75, 31, 255), font=f_bold)
        draw.text((805, ty + 8), v, fill=(23, 22, 15, 255), font=f_tag)

    # Note Box on Right Page
    draw.rectangle([545, 700, 870, 770], fill=(228, 174, 35, 40), outline=(228, 174, 35, 255), width=1)
    draw.text((555, 710), "💡 DICA DO COACH:", fill=(180, 120, 0, 255), font=f_bold)
    draw.text((555, 732), "Sempre valide a amplitude do squat no Wall Ball", fill=(23, 22, 15, 255), font=f_tag)
    draw.text((555, 750), "antes de aumentar o peso da medball do atleta.", fill=(23, 22, 15, 255), font=f_tag)

    draw.text((750, 790), "HYROX DAILY WOD  |  PÁG 35", fill=(120, 115, 100, 255), font=f_tag)

    # 4. Desk Props (Coach Glasses & Whistle on table)
    # Glasses on left desk area
    g_layer = Image.new("RGBA", (w, h), (0,0,0,0))
    gdraw = ImageDraw.Draw(g_layer)
    # Left lens & right lens frames
    gdraw.ellipse([40, 300, 110, 390], outline=(30, 25, 20, 240), width=5)
    gdraw.ellipse([110, 300, 180, 390], outline=(30, 25, 20, 240), width=5)
    gdraw.line([(110, 340), (110, 340)], fill=(30, 25, 20, 240), width=4)
    gdraw.line([(30, 320), (50, 335)], fill=(30, 25, 20, 240), width=4)
    img = Image.alpha_composite(img, g_layer)

    img.save(output_path, "PNG")


def generate_open_daily_wod_mockup(output_path):
    w, h = 1024, 1024
    img = Image.new("RGBA", (w, h), (32, 28, 24, 255))
    draw = ImageDraw.Draw(img)

    # 1. Dark Rustic Wood Grain Desk
    for y in range(h):
        r = int(45 + 12 * math.sin(y * 0.04) + (y / h) * 8)
        g = int(36 + 10 * math.sin(y * 0.04) + (y / h) * 6)
        b = int(28 + 6 * math.sin(y * 0.04) + (y / h) * 4)
        draw.line([(0, y), (w, y)], fill=(r, g, b, 255))

    for x in range(0, w, 190):
        draw.line([(x, 0), (x, h)], fill=(20, 16, 12, 130), width=3)

    vignette = Image.new("RGBA", (w, h), (0,0,0,0))
    vdraw = ImageDraw.Draw(vignette)
    for r_idx in range(500, 0, -10):
        alpha = int(150 * (1 - r_idx / 500))
        vdraw.ellipse([512 - r_idx*1.4, 512 - r_idx*1.4, 512 + r_idx*1.4, 512 + r_idx*1.4], fill=(0,0,0, alpha))
    vignette = vignette.filter(ImageFilter.GaussianBlur(60))
    img = Image.alpha_composite(img, vignette)

    # 2. Book Drop Shadow
    shadow = Image.new("RGBA", (w, h), (0,0,0,0))
    shdraw = ImageDraw.Draw(shadow)
    shdraw.polygon([(110, 220), (914, 220), (934, 840), (90, 840)], fill=(0, 0, 0, 210))
    shadow = shadow.filter(ImageFilter.GaussianBlur(35))
    img = Image.alpha_composite(img, shadow)

    # 3. Open WOD Binder Base
    draw = ImageDraw.Draw(img)

    # Thickness
    draw.polygon([(120, 815), (505, 825), (505, 840), (110, 830)], fill=(215, 205, 190, 255))
    draw.polygon([(519, 825), (904, 815), (914, 830), (519, 840)], fill=(215, 205, 190, 255))

    # Left Page
    draw.polygon([(130, 200), (505, 210), (505, 825), (120, 815)], fill=(236, 231, 222, 255))
    # Right Page
    draw.polygon([(519, 210), (894, 200), (904, 815), (519, 825)], fill=(236, 231, 222, 255))

    # Spine Shadow
    spine_shadow = Image.new("RGBA", (w, h), (0,0,0,0))
    spdraw = ImageDraw.Draw(spine_shadow)
    spdraw.rectangle([495, 200, 529, 835], fill=(0, 0, 0, 95))
    spdraw.line([(512, 200), (512, 835)], fill=(0, 0, 0, 190), width=2)
    spine_shadow = spine_shadow.filter(ImageFilter.GaussianBlur(8))
    img = Image.alpha_composite(img, spine_shadow)
    draw = ImageDraw.Draw(img)

    try:
        f_h1 = ImageFont.truetype("arialbd.ttf", 26)
        f_h2 = ImageFont.truetype("arialbd.ttf", 20)
        f_body = ImageFont.truetype("arial.ttf", 15)
        f_bold = ImageFont.truetype("arialbd.ttf", 15)
        f_tag = ImageFont.truetype("arialbd.ttf", 13)
    except:
        f_h1 = f_h2 = f_body = f_bold = f_tag = ImageFont.load_default()

    # --- LEFT PAGE: DAILY WOD PLAN #087 ---
    draw.rectangle([155, 235, 480, 280], fill=(228, 174, 35, 255))
    draw.text((170, 248), "250 DAILY WODS • CATÁLOGO COMPLETO", fill=(14, 13, 8, 255), font=f_h2)

    draw.text((155, 300), "AULA #087: Sled Push & Burpee Day", fill=(23, 22, 15, 255), font=f_h1)

    # Meta Tags
    draw.rectangle([155, 340, 240, 368], fill=(255, 75, 31, 255))
    draw.text((165, 347), "45 MIN", fill=(255, 255, 255, 255), font=f_tag)

    draw.rectangle([250, 340, 360, 368], fill=(23, 22, 15, 255))
    draw.text((260, 347), "3 ESTAÇÕES", fill=(228, 174, 35, 255), font=f_tag)

    # Section 1: Aquecimento
    draw.rectangle([155, 385, 480, 480], fill=(225, 218, 202, 255), outline=(23, 22, 15, 100), width=1)
    draw.text((165, 395), "🔥 AQUECIMENTO GERAL (10 MINUTOS)", fill=(255, 75, 31, 255), font=f_bold)
    draw.text((165, 420), "• 400m Corrida Leve em Ritmo de Transição", fill=(23, 22, 15, 255), font=f_tag)
    draw.text((165, 440), "• 3 Rodadas: 10 Air Squats + 8 Inchworms + 10 Scapular Pushups", fill=(23, 22, 15, 255), font=f_tag)

    # Section 2: Bloco Principal
    draw.rectangle([155, 495, 480, 770], fill=(255, 255, 255, 255), outline=(255, 75, 31, 255), width=2)
    draw.rectangle([155, 495, 480, 525], fill=(255, 75, 31, 255))
    draw.text((165, 503), "🏋️ BLOCO PRINCIPAL (FORÇA & RESISTÊNCIA)", fill=(255, 255, 255, 255), font=f_bold)

    wod_details = [
        "EMOM 24 MINUTOS (4 ESTAÇÕES CONTINUADAS):",
        "Minuto 1: 12.5m Sled Push (Carga Padrão)",
        "Minuto 2: 10 Burpee Broad Jumps Contínuos",
        "Minuto 3: 200m Corrida de Recuperação Ativa",
        "Minuto 4: Descanso Obrigatório / Ajuste de Hidratação",
        "",
        "🎯 FOCO TÉCNICO: Manter a pegada firme no sled e",
        "ritmo constante na transição pra corrida."
    ]
    for idx, line in enumerate(wod_details):
        draw.text((165, 538 + idx*26), line, fill=(23, 22, 15, 255), font=f_tag)

    draw.text((155, 790), "AULA PRONTA PARA APLICAR  |  PÁG 87", fill=(120, 115, 100, 255), font=f_tag)

    # --- RIGHT PAGE: 3 NÍVEIS DE ADAPTAÇÃO ---
    draw.rectangle([545, 235, 870, 280], fill=(23, 22, 15, 255))
    draw.text((560, 248), "3 NÍVEIS DE ADAPTAÇÃO DA TURMA", fill=(228, 174, 35, 255), font=f_h2)

    draw.text((545, 300), "Adaptação de Nível por Aluno", fill=(23, 22, 15, 255), font=f_h1)

    # Level 1 Card
    draw.rectangle([545, 345, 870, 470], fill=(236, 231, 222, 255), outline=(100, 180, 100, 255), width=2)
    draw.rectangle([545, 345, 680, 375], fill=(100, 180, 100, 255))
    draw.text((555, 352), "NÍVEL 1: INICIANTE", fill=(255, 255, 255, 255), font=f_bold)
    draw.text((555, 385), "• Sled Push: Sem peso adicional no carrinho", fill=(23, 22, 15, 255), font=f_tag)
    draw.text((555, 405), "• Burpee: Step-back burpee sem salto de distância", fill=(23, 22, 15, 255), font=f_tag)
    draw.text((555, 425), "• Corrida: Caminhada acelerada 150m", fill=(23, 22, 15, 255), font=f_tag)

    # Level 2 Card
    draw.rectangle([545, 485, 870, 610], fill=(236, 231, 222, 255), outline=(228, 174, 35, 255), width=2)
    draw.rectangle([545, 485, 710, 515], fill=(228, 174, 35, 255))
    draw.text((555, 492), "NÍVEL 2: INTERMEDIÁRIO", fill=(14, 13, 8, 255), font=f_bold)
    draw.text((555, 525), "• Sled Push: 75kg (Masc) / 50kg (Fem)", fill=(23, 22, 15, 255), font=f_tag)
    draw.text((555, 545), "• Burpee: Broad Jump com 1.5m de alcance", fill=(23, 22, 15, 255), font=f_tag)
    draw.text((555, 565), "• Corrida: Trotar continuo 200m", fill=(23, 22, 15, 255), font=f_tag)

    # Level 3 Card
    draw.rectangle([545, 625, 870, 750], fill=(236, 231, 222, 255), outline=(255, 75, 31, 255), width=2)
    draw.rectangle([545, 625, 690, 655], fill=(255, 75, 31, 255))
    draw.text((555, 632), "NÍVEL 3: HYROX PRO", fill=(255, 255, 255, 255), font=f_bold)
    draw.text((555, 665), "• Sled Push: 152kg (Masc) / 102kg (Fem)", fill=(23, 22, 15, 255), font=f_tag)
    draw.text((555, 685), "• Burpee: Broad Jump máximo alcance continuo", fill=(23, 22, 15, 255), font=f_tag)
    draw.text((555, 705), "• Corrida: Pace de prova 4:15 min/km", fill=(23, 22, 15, 255), font=f_tag)

    draw.text((740, 790), "COLEÇÃO ANUAL DAILY WOD  |  PÁG 88", fill=(120, 115, 100, 255), font=f_tag)

    img.save(output_path, "PNG")


if __name__ == "__main__":
    generate_open_manual_mockup("assets/images/manual_coach_cover.png")
    generate_open_daily_wod_mockup("assets/images/daily_wod_cover.png")
    print("Open manual photography mockups generated successfully!")
