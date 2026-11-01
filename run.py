import os
import sys
import subprocess
import shutil
import venv

VENV_DIR = ".venv_energy_race"
TEMP_DIR = ".temp_energy_assets"


def create_venv():
    if not os.path.exists(VENV_DIR):
        print("[1/5] Creating isolated virtual environment (.venv_energy_race)...")
        venv.create(VENV_DIR, with_pip=True)


def get_venv_python():
    if sys.platform == "win32":
        return os.path.join(VENV_DIR, "Scripts", "python.exe")
    return os.path.join(VENV_DIR, "bin", "python")


def run_bootstrap():
    print("=====================================================================")
    print("  3D VIDEO GENERATOR: GLOBAL ELECTRICITY GENERATION (1960 - 2026)    ")
    print("=====================================================================")

    os.makedirs(TEMP_DIR, exist_ok=True)
    create_venv()
    venv_python = get_venv_python()

    print("[2/5] Installing required libraries and portable FFmpeg into virtual environment...")
    subprocess.check_call([venv_python, "-m", "pip", "install", "--upgrade", "pip", "-q"])
    subprocess.check_call([
        venv_python, "-m", "pip", "install",
        "pandas", "numpy", "matplotlib", "requests", "pillow", "imageio-ffmpeg", "-q"
    ])

    try:
        print("[3/5] Launching smooth 3D rendering, audio synthesis, and MP4 assembly...")
        subprocess.check_call([venv_python, os.path.abspath(__file__), "--worker"])
    finally:
        print("[4/5] Self-cleanup: removing virtual environment and temporary assets...")
        shutil.rmtree(TEMP_DIR, ignore_errors=True)
        shutil.rmtree(VENV_DIR, ignore_errors=True)
        print("[5/5] Cleanup complete! Final MP4 video and license files are ready in the project folder.")


def create_rounded_flag(code, width=80, height=52, radius=10):
    from PIL import Image, ImageDraw
    import numpy as np

    canvas = Image.new("RGBA", (width + 10, height + 10), (0, 0, 0, 0))

    mask = Image.new("L", (width, height), 0)
    mask_draw = ImageDraw.Draw(mask)
    mask_draw.rounded_rectangle([0, 0, width - 1, height - 1], radius=radius, fill=255)

    shadow = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    sh_draw = ImageDraw.Draw(shadow)
    sh_draw.rounded_rectangle([0, 0, width - 1, height - 1], radius=radius, fill=(2, 6, 16, 210))
    canvas.paste(shadow, (5, 5))

    img = Image.new("RGBA", (width, height), (255, 255, 255, 255))
    draw = ImageDraw.Draw(img)
    w, h = width, height

    if code == "us":
        stripe_h = h / 13.0
        for i in range(13):
            color = (178, 34, 52) if i % 2 == 0 else (245, 247, 250)
            draw.rectangle([0, int(i * stripe_h), w, int((i + 1) * stripe_h)], fill=color)
        draw.rectangle([0, 0, int(w * 0.42), int(h * 7 / 13.0)], fill=(40, 53, 107))
        for r in range(3):
            for c in range(4):
                cx = int(w * 0.06 + c * (w * 0.09))
                cy = int(h * 0.08 + r * (h * 0.16))
                draw.ellipse([cx - 1, cy - 1, cx + 1, cy + 1], fill=(255, 255, 255))
    elif code == "cn":
        draw.rectangle([0, 0, w, h], fill=(222, 41, 16))
        draw.ellipse([int(w * 0.1), int(h * 0.15), int(w * 0.28), int(h * 0.42)], fill=(255, 222, 0))
    elif code == "in":
        draw.rectangle([0, 0, w, h // 3], fill=(255, 153, 51))
        draw.rectangle([0, h // 3, w, 2 * h // 3], fill=(248, 250, 252))
        draw.rectangle([0, 2 * h // 3, w, h], fill=(19, 136, 8))
        r = int(h * 0.12)
        draw.ellipse([w // 2 - r, h // 2 - r, w // 2 + r, h // 2 + r], outline=(0, 0, 128), width=2)
    elif code == "ru":
        draw.rectangle([0, 0, w, h // 3], fill=(248, 250, 252))
        draw.rectangle([0, h // 3, w, 2 * h // 3], fill=(0, 57, 166))
        draw.rectangle([0, 2 * h // 3, w, h], fill=(213, 43, 30))
    elif code == "jp":
        draw.rectangle([0, 0, w, h], fill=(248, 250, 252))
        r = int(h * 0.3)
        draw.ellipse([w // 2 - r, h // 2 - r, w // 2 + r, h // 2 + r], fill=(188, 0, 45))
    elif code == "br":
        draw.rectangle([0, 0, w, h], fill=(0, 156, 59))
        draw.polygon([(w // 2, int(h * 0.12)), (int(w * 0.88), h // 2), (w // 2, int(h * 0.88)), (int(w * 0.12), h // 2)], fill=(255, 223, 0))
        r = int(h * 0.18)
        draw.ellipse([w // 2 - r, h // 2 - r, w // 2 + r, h // 2 + r], fill=(0, 39, 118))
    elif code == "ca":
        draw.rectangle([0, 0, w // 4, h], fill=(216, 6, 33))
        draw.rectangle([w // 4, 0, 3 * w // 4, h], fill=(248, 250, 252))
        draw.rectangle([3 * w // 4, 0, w, h], fill=(216, 6, 33))
        r = int(h * 0.18)
        draw.polygon([(w // 2, h // 2 - r), (w // 2 - r, h // 2 + r // 2), (w // 2 + r, h // 2 + r // 2)], fill=(216, 6, 33))
    elif code == "kr":
        draw.rectangle([0, 0, w, h], fill=(248, 250, 252))
        r = int(h * 0.22)
        draw.ellipse([w // 2 - r, h // 2 - r, w // 2 + r, h // 2 + r], fill=(205, 46, 58))
        draw.chord([w // 2 - r, h // 2 - r, w // 2 + r, h // 2 + r], start=0, end=180, fill=(0, 71, 160))
    elif code == "de":
        draw.rectangle([0, 0, w, h // 3], fill=(20, 20, 20))
        draw.rectangle([0, h // 3, w, 2 * h // 3], fill=(210, 16, 26))
        draw.rectangle([0, 2 * h // 3, w, h], fill=(255, 206, 0))
    elif code == "fr":
        draw.rectangle([0, 0, w // 3, h], fill=(0, 38, 84))
        draw.rectangle([w // 3, 0, 2 * w // 3, h], fill=(248, 250, 252))
        draw.rectangle([2 * w // 3, 0, w, h], fill=(237, 41, 57))
    elif code == "sa":
        draw.rectangle([0, 0, w, h], fill=(0, 108, 53))
        draw.rectangle([int(w * 0.25), int(h * 0.62), int(w * 0.75), int(h * 0.68)], fill=(255, 255, 255))
    elif code == "ir":
        draw.rectangle([0, 0, w, h // 3], fill=(35, 159, 64))
        draw.rectangle([0, h // 3, w, 2 * h // 3], fill=(248, 250, 252))
        draw.rectangle([0, 2 * h // 3, w, h], fill=(218, 0, 0))
        draw.ellipse([w // 2 - 4, h // 2 - 4, w // 2 + 4, h // 2 + 4], fill=(218, 0, 0))
    elif code == "mx":
        draw.rectangle([0, 0, w // 3, h], fill=(0, 104, 71))
        draw.rectangle([w // 3, 0, 2 * w // 3, h], fill=(248, 250, 252))
        draw.rectangle([2 * w // 3, 0, w, h], fill=(206, 17, 38))
        draw.ellipse([w // 2 - 4, h // 2 - 4, w // 2 + 4, h // 2 + 4], fill=(139, 69, 19))
    elif code == "tr":
        draw.rectangle([0, 0, w, h], fill=(227, 10, 23))
        r = int(h * 0.22)
        draw.ellipse([w // 2 - r - 4, h // 2 - r, w // 2 + r - 4, h // 2 + r], fill=(255, 255, 255))
        r2 = int(h * 0.17)
        draw.ellipse([w // 2 - r2, h // 2 - r2, w // 2 + r2, h // 2 + r2], fill=(227, 10, 23))
    elif code == "id":
        draw.rectangle([0, 0, w, h // 2], fill=(255, 0, 0))
        draw.rectangle([0, h // 2, w, h], fill=(248, 250, 252))
    elif code == "gb":
        draw.rectangle([0, 0, w, h], fill=(1, 33, 105))
        draw.line([(0, 0), (w, h)], fill=(255, 255, 255), width=7)
        draw.line([(0, h), (w, 0)], fill=(255, 255, 255), width=7)
        draw.line([(0, 0), (w, h)], fill=(200, 16, 46), width=3)
        draw.line([(0, h), (w, 0)], fill=(200, 16, 46), width=3)
        draw.rectangle([w // 2 - 6, 0, w // 2 + 6, h], fill=(255, 255, 255))
        draw.rectangle([0, h // 2 - 6, w, h // 2 + 6], fill=(255, 255, 255))
        draw.rectangle([w // 2 - 3, 0, w // 2 + 3, h], fill=(200, 16, 46))
        draw.rectangle([0, h // 2 - 3, w, h // 2 + 3], fill=(200, 16, 46))
    elif code == "it":
        draw.rectangle([0, 0, w // 3, h], fill=(0, 140, 69))
        draw.rectangle([w // 3, 0, 2 * w // 3, h], fill=(248, 250, 252))
        draw.rectangle([2 * w // 3, 0, w, h], fill=(205, 33, 42))
    elif code == "au":
        draw.rectangle([0, 0, w, h], fill=(1, 33, 105))
        draw.line([(0, 0), (w // 2, h // 2)], fill=(255, 255, 255), width=3)
        draw.line([(0, h // 2), (w // 2, 0)], fill=(255, 255, 255), width=3)
        draw.rectangle([w // 4 - 2, 0, w // 4 + 2, h // 2], fill=(200, 16, 46))
        draw.rectangle([0, h // 4 - 2, w // 2, h // 4 + 2], fill=(200, 16, 46))

    rounded_flag = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    rounded_flag.paste(img, (0, 0), mask=mask)
    rim_draw = ImageDraw.Draw(rounded_flag)
    rim_draw.rounded_rectangle([0, 0, width - 1, height - 1], radius=radius, outline=(56, 189, 248, 175), width=2)
    canvas.paste(rounded_flag, (0, 0), mask=rounded_flag)
    return np.array(canvas)


def make_smooth_capsule_polygon(x0, y0, width, height, rx_left, rx_right, ry, n_arc=24):
    import numpy as np

    ry = min(ry, height * 0.48)
    rx_r = min(rx_right, width * 0.55)
    rx_l = min(rx_left, max(0.0, width - rx_r) * 0.90)

    angles_br = np.linspace(-np.pi / 2, 0, n_arc)
    angles_tr = np.linspace(0, np.pi / 2, n_arc)
    angles_tl = np.linspace(np.pi / 2, np.pi, n_arc)
    angles_bl = np.linspace(np.pi, 3 * np.pi / 2, n_arc)

    x_br = (x0 + width - rx_r) + rx_r * np.cos(angles_br)
    y_br = (y0 + ry) + ry * np.sin(angles_br)

    x_tr = (x0 + width - rx_r) + rx_r * np.cos(angles_tr)
    y_tr = (y0 + height - ry) + ry * np.sin(angles_tr)

    x_tl = (x0 + rx_l) + rx_l * np.cos(angles_tl)
    y_tl = (y0 + height - ry) + ry * np.sin(angles_tl)

    x_bl = (x0 + rx_l) + rx_l * np.cos(angles_bl)
    y_bl = (y0 + ry) + ry * np.sin(angles_bl)

    xs = np.concatenate([x_br, x_tr, x_tl, x_bl])
    ys = np.concatenate([y_br, y_tr, y_tl, y_bl])
    return np.column_stack([xs, ys])


def build_electric_blue_3d_texture(norm_rank, delta_rate, pulse_phase, alpha=1.0, h_px=64, w_px=220):
    import numpy as np

    y_norm = np.linspace(0.0, 1.0, h_px)[:, None]
    x_norm = np.linspace(0.0, 1.0, w_px)[None, :]

    surge_strength = float(np.clip(delta_rate * 8.0, 0.0, 1.0))

    r_left = 0.08 + 0.06 * norm_rank
    g_left = 0.28 + 0.20 * norm_rank
    b_left = 0.72 + 0.18 * norm_rank

    r_right = 0.20 + 0.22 * norm_rank + 0.25 * surge_strength
    g_right = 0.68 + 0.22 * norm_rank + 0.10 * surge_strength
    b_right = 0.96 + 0.04 * norm_rank

    grad_curve = x_norm ** 0.78
    r_base = r_left + (r_right - r_left) * grad_curve
    g_base = g_left + (g_right - g_left) * grad_curve
    b_base = b_left + (b_right - b_left) * grad_curve

    wave_pos = pulse_phase % 1.0
    pulse_wave = (0.16 + 0.12 * surge_strength) * np.exp(-((x_norm - wave_pos) ** 2) / (2 * 0.016))

    cylinder_diffuse = 0.56 + 0.48 * np.sin(np.pi * (y_norm ** 0.82))
    specular = 0.38 * np.exp(-((y_norm - 0.73) ** 2) / (2 * 0.007)) * (0.35 + 0.65 * np.sin(np.pi * x_norm))
    bottom_rim = 0.12 * np.exp(-((y_norm - 0.10) ** 2) / (2 * 0.005))

    r = np.clip(r_base * cylinder_diffuse + specular * 0.85 + pulse_wave * 0.75, 0.0, 1.0)
    g = np.clip(g_base * cylinder_diffuse + specular * 0.95 + pulse_wave * 0.95 + bottom_rim * 0.6, 0.0, 1.0)
    b = np.clip(b_base * cylinder_diffuse + specular + pulse_wave + bottom_rim, 0.0, 1.0)
    a = np.full_like(r, alpha)

    return np.dstack([r, g, b, a])


def run_worker():
    import math
    import wave
    import pandas as pd
    import numpy as np
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import matplotlib.ticker as ticker
    import matplotlib.animation as animation
    from matplotlib.patches import Polygon, FancyBboxPatch
    from matplotlib.offsetbox import OffsetImage, AnnotationBbox
    import imageio_ffmpeg

    FPS = 30
    DURATION_SEC = 40
    TOTAL_FRAMES = FPS * DURATION_SEC

    COUNTRIES_ISO = {
        "China": "cn", "United States": "us", "India": "in", "Russia": "ru",
        "Japan": "jp", "Brazil": "br", "Canada": "ca", "South Korea": "kr",
        "France": "fr", "Germany": "de", "Saudi Arabia": "sa", "Iran": "ir",
        "Mexico": "mx", "Turkey": "tr", "Indonesia": "id", "United Kingdom": "gb",
        "Italy": "it", "Australia": "au"
    }

    START_YEAR = 1960.0
    END_YEAR = 2026.83
    TITLE_MAIN = "GLOBAL ELECTRICITY GENERATION"
    TITLE_SUB = "ANNUAL POWER GENERATION IN TERAWATT-HOURS (1960 - OCT 2026)"
    FINAL_OUTPUT = "global_electricity_generation_1960_2026_shorts.mp4"

    # Historical Annual Electricity Generation in Terawatt-hours (TWh) — IEA & Energy Institute Statistical Review
    ANCHORS = {
        "United States":  {1960: 844.0, 1970: 1623.0, 1980: 2427.0, 1990: 3218.0, 2000: 4025.0, 2010: 4354.0, 2020: 4260.0, 2026: 4420.0},
        "China":          {1960: 59.0,  1970: 116.0,  1980: 300.6,  1990: 621.2,  2000: 1355.6, 2010: 4207.2, 2020: 7779.1, 2026: 10080.0},
        "India":          {1960: 20.1,  1970: 61.2,   1980: 119.3,  1990: 289.4,  2000: 560.8,  2010: 965.7,  2020: 1560.9, 2026: 2140.0},
        "Russia":         {1960: 195.0, 1970: 470.0,  1980: 805.0,  1990: 1082.2, 2000: 877.8,  2010: 1038.0, 2020: 1085.4, 2026: 1210.0},
        "Japan":          {1960: 115.5, 1970: 359.5,  1980: 576.3,  1990: 835.5,  2000: 1058.0, 2010: 1156.0, 2020: 1004.8, 2026: 1020.0},
        "Brazil":         {1960: 22.9,  1970: 45.5,   1980: 139.5,  1990: 222.8,  2000: 348.9,  2010: 515.8,  2020: 621.2,  2026: 745.0},
        "Canada":         {1960: 116.1, 1970: 209.7,  1980: 373.4,  1990: 482.0,  2000: 605.6,  2010: 603.0,  2020: 644.2,  2026: 660.0},
        "South Korea":    {1960: 1.8,   1970: 9.6,    1980: 37.2,   1990: 105.4,  2000: 288.5,  2010: 499.5,  2020: 578.0,  2026: 625.0},
        "France":         {1960: 75.0,  1970: 146.8,  1980: 258.0,  1990: 420.8,  2000: 540.0,  2010: 569.3,  2020: 524.9,  2026: 545.0},
        "Germany":        {1960: 159.0, 1970: 310.3,  1980: 467.6,  1990: 549.9,  2000: 576.6,  2010: 633.1,  2020: 574.2,  2026: 525.0},
        "Saudi Arabia":   {1960: 0.4,   1970: 1.8,    1980: 20.5,   1990: 69.2,   2000: 126.2,  2010: 240.1,  2020: 365.9,  2026: 455.0},
        "Iran":           {1960: 1.1,   1970: 6.8,    1980: 22.4,   1990: 59.1,   2000: 121.4,  2010: 233.0,  2020: 337.2,  2026: 395.0},
        "Mexico":         {1960: 10.8,  1970: 28.7,   1980: 67.0,   1990: 122.7,  2000: 204.2,  2010: 275.6,  2020: 326.4,  2026: 368.0},
        "Turkey":         {1960: 2.8,   1970: 8.6,    1980: 23.3,   1990: 57.5,   2000: 124.9,  2010: 211.2,  2020: 306.7,  2026: 355.0},
        "Indonesia":      {1960: 1.5,   1970: 3.1,    1980: 8.4,    1990: 33.3,   2000: 93.3,   2010: 169.8,  2020: 291.7,  2026: 375.0},
        "United Kingdom": {1960: 138.7, 1970: 249.1,  1980: 285.3,  1990: 319.7,  2000: 377.1,  2010: 382.1,  2020: 312.8,  2026: 295.0},
        "Italy":          {1960: 56.2,  1970: 117.4,  1980: 185.7,  1990: 216.6,  2000: 276.6,  2010: 302.1,  2020: 280.5,  2026: 272.0},
        "Australia":      {1960: 23.2,  1970: 53.9,   1980: 96.1,   1990: 155.1,  2000: 210.2,  2010: 252.7,  2020: 265.2,  2026: 282.0}
    }

    print(" -> Generating smooth rounded 3D flags for all countries...")
    flags = {country: create_rounded_flag(code, 80, 52, 10) for country, code in COUNTRIES_ISO.items()}

    print(" -> Synthesizing royalty-free soundtrack (High-Voltage Grid Pulse - CC0 License)...")
    audio_path = os.path.join(TEMP_DIR, "high_voltage_pulse.wav")
    license_lines = [
        "MUSIC LICENSE CERTIFICATE (CC0 1.0 Universal - Public Domain Dedication)",
        "=======================================================================",
        "Track Title: High-Voltage Grid Pulse (Driving Electronic Synth-Bass & Harmonic Score)",
        "License: Creative Commons Zero (CC0 1.0 Universal)",
        "Status: 100% Royalty-Free / Safe for YouTube Shorts, Instagram Reels, TikTok monetization.",
        "Permissions: Commercial and non-commercial use, modification, and distribution permitted without attribution."
    ]
    with open("MUSIC_LICENSE_CC0.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(license_lines) + "\n")

    sample_rate = 44100
    n_samples = sample_rate * DURATION_SEC
    t = np.linspace(0, DURATION_SEC, n_samples, endpoint=False)

    # Energetic electronic progression: E minor -> C major -> G major -> D major
    freqs_base = np.select(
        [(t % 8) < 2.0, (t % 8) < 4.0, (t % 8) < 6.0, (t % 8) >= 6.0],
        [82.41, 65.41, 98.00, 73.42]
    )

    # Driving 120 BPM (8 Hz sixteenth-note pulse) synth bassline
    bass_gate = 0.55 + 0.45 * np.sin(2 * math.pi * 4.0 * t)
    synth_bass = (0.24 * np.sin(2 * math.pi * freqs_base * t) + 0.08 * np.sin(2 * math.pi * (freqs_base * 2.0) * t)) * bass_gate

    # Warm harmonic power-grid pad
    grid_pad_l = 0.13 * np.sin(2 * math.pi * (freqs_base * 1.5) * t + 0.3 * np.sin(2 * math.pi * 0.6 * t))
    grid_pad_r = 0.13 * np.sin(2 * math.pi * (freqs_base * 2.0) * t + 0.7)

    # Crisp 8th-note electric pulse arpeggiator
    step_phase = (t * 8.0) % 1.0
    spark_env = np.exp(-6.5 * step_phase) * (1.0 - np.exp(-80.0 * step_phase))
    arp_mult = np.select(
        [((t * 8.0).astype(int) % 4) == 0, ((t * 8.0).astype(int) % 4) == 1,
         ((t * 8.0).astype(int) % 4) == 2, ((t * 8.0).astype(int) % 4) == 3],
        [2.0, 3.0, 4.0, 3.0]
    )
    electric_arp = 0.11 * np.sin(2 * math.pi * (freqs_base * arp_mult) * t) * spark_env

    envelope = np.ones_like(t)
    fade_len = sample_rate * 2
    envelope[:fade_len] = np.linspace(0, 1, fade_len)
    envelope[-fade_len:] = np.linspace(1, 0, fade_len)

    stereo_left = np.clip((synth_bass + grid_pad_l + electric_arp) * envelope, -0.95, 0.95)
    stereo_right = np.clip((synth_bass + grid_pad_r + electric_arp * 0.92) * envelope, -0.95, 0.95)

    interleaved = np.empty((n_samples * 2,), dtype=np.int16)
    interleaved[0::2] = (stereo_left * 32767).astype(np.int16)
    interleaved[1::2] = (stereo_right * 32767).astype(np.int16)

    with wave.open(audio_path, "wb") as wf:
        wf.setnchannels(2)
        wf.setsampwidth(2)
        wf.setframerate(sample_rate)
        wf.writeframes(interleaved.tobytes())

    print(" -> Building 1960-2026 electricity generation matrix with smooth Hann-window rank transitions...")
    fine_years = np.linspace(START_YEAR, END_YEAR, TOTAL_FRAMES)
    val_dict = {}
    for country, anchors in ANCHORS.items():
        yrs = sorted(list(anchors.keys()))
        vals = [anchors[y] for y in yrs]
        val_dict[country] = np.interp(fine_years, yrs, vals)

    df_values = pd.DataFrame(val_dict, index=fine_years)
    df_values = df_values.where(df_values > 0.1, np.nan)

    df_deltas = df_values.pct_change(periods=15).fillna(0.0)
    df_deltas_smooth = df_deltas.rolling(window=20, min_periods=1, center=True).mean().fillna(0.0)

    df_ranks = df_values.rank(axis=1, method='first', ascending=True).fillna(0.0)
    win_size = 35
    hann_win = np.hanning(win_size)
    hann_win /= hann_win.sum()
    df_ranks_smooth = df_ranks.apply(
        lambda col: np.convolve(np.pad(col.values, (win_size // 2, win_size // 2), mode='edge'), hann_win, mode='valid')[:len(col)]
    )

    ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()
    plt.rcParams['animation.ffmpeg_path'] = ffmpeg_exe

    print(f" -> Rendering 40-second smooth 3D HD 9:16 video ({TOTAL_FRAMES} frames at {FPS} FPS)...")
    BG_OUTER = '#070b14'
    BG_PLOT = '#0b101e'

    fig = plt.figure(figsize=(9, 16), dpi=120)
    fig.patch.set_facecolor(BG_OUTER)

    # Animated background electric plasma nodes
    spark_ax = fig.add_axes([0, 0, 1, 1], frameon=False)
    spark_ax.set_xlim(0, 1)
    spark_ax.set_ylim(0, 1)
    spark_ax.set_xticks([])
    spark_ax.set_yticks([])

    np.random.seed(42)
    n_particles = 85
    base_px = np.random.uniform(0.03, 0.97, n_particles)
    base_py = np.random.uniform(0.03, 0.97, n_particles)
    base_ps = np.random.uniform(4, 30, n_particles)
    base_pa = np.random.uniform(0.10, 0.42, n_particles)
    spark_scatter = spark_ax.scatter(base_px, base_py, s=base_ps, color='#38bdf8', alpha=0.25, edgecolors='none')

    # Smooth Rounded Header Capsule (First Video Dark-Blue Neon Aesthetic)
    header_box = FancyBboxPatch(
        (0.04, 0.882), 0.92, 0.092,
        boxstyle="round,pad=0.01,rounding_size=0.035",
        transform=fig.transFigure,
        facecolor='#0f172a', edgecolor='#3b82f6', linewidth=1.8, alpha=0.96, zorder=2
    )
    fig.patches.append(header_box)

    fig.text(
        0.5, 0.946, TITLE_MAIN,
        color='#ffffff', fontsize=20.5, fontweight='bold', fontfamily='DejaVu Sans', ha='center', va='center', zorder=4
    )
    fig.text(
        0.5, 0.916, TITLE_SUB,
        color='#60a5fa', fontsize=9.8, fontweight='bold', fontfamily='DejaVu Sans', ha='center', va='center', zorder=4
    )

    prog_bg = FancyBboxPatch(
        (0.10, 0.893), 0.80, 0.006,
        boxstyle="round,pad=0,rounding_size=0.003",
        transform=fig.transFigure,
        facecolor='#1e293b', edgecolor='none', alpha=0.9, zorder=3
    )
    prog_fg = FancyBboxPatch(
        (0.10, 0.893), 0.01, 0.006,
        boxstyle="round,pad=0,rounding_size=0.003",
        transform=fig.transFigure,
        facecolor='#38bdf8', edgecolor='none', alpha=0.95, zorder=4
    )
    fig.patches.extend([prog_bg, prog_fg])

    ax = fig.add_axes([0.38, 0.06, 0.58, 0.79])

    top_n = 12
    max_rank = len(COUNTRIES_ISO)
    min_visible_rank = max_rank - top_n + 1.0

    ax_w_in = 0.58 * 9.0
    ax_h_in = 0.79 * 16.0
    bar_h = 0.56
    ry = bar_h * 0.45

    def update(frame_idx):
        ax.clear()
        ax.set_facecolor(BG_PLOT)

        progress = (frame_idx + 1) / float(TOTAL_FRAMES)
        prog_fg.set_width(max(0.01, 0.80 * progress))

        # Animate rising and pulsing electric plasma sparks
        cur_py = (base_py + frame_idx * 0.0010) % 1.0
        cur_px = (base_px + 0.009 * np.sin(frame_idx * 0.06 + np.arange(n_particles))) % 1.0
        spark_scatter.set_offsets(np.column_stack([cur_px, cur_py]))
        twinkle = base_pa * (0.60 + 0.40 * np.sin(frame_idx * 0.15 + np.arange(n_particles)))
        spark_scatter.set_alpha(twinkle)

        current_time = df_values.index[frame_idx]
        year_int = int(current_time)
        month_int = min(12, max(1, int((current_time - year_int) * 12) + 1))
        month_names = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]
        date_str = f"{month_names[month_int - 1]} {year_int}"

        vals_row = df_values.iloc[frame_idx]
        ranks_row = df_ranks_smooth.iloc[frame_idx]
        deltas_row = df_deltas_smooth.iloc[frame_idx]

        visible = ranks_row[ranks_row >= min_visible_rank - 0.7].dropna()
        max_val = max(vals_row.max(), 50.0)

        x_max = max_val * 1.34
        y_min, y_max = min_visible_rank - 0.65, max_rank + 0.65
        ax.set_xlim(0, x_max)
        ax.set_ylim(y_min, y_max)

        ax.xaxis.grid(True, color='#1e293b', linestyle='--', linewidth=1.0, alpha=0.65, zorder=0)
        ax.set_axisbelow(True)

        rx_right = ry * (x_max / (y_max - y_min)) * (ax_h_in / ax_w_in) * 0.68
        rx_left = rx_right * 0.22
        pulse_global = (frame_idx * 0.028) % 1.0

        for country, smooth_y in visible.items():
            val = vals_row[country]
            if pd.isna(val) or val <= 0:
                continue

            alpha = 1.0
            if smooth_y < min_visible_rank:
                alpha = max(0.0, min(1.0, (smooth_y - (min_visible_rank - 0.7)) / 0.7))

            norm_rank = np.clip((smooth_y - min_visible_rank) / max(1, top_n - 1), 0, 1)
            rank_num = max(1, min(top_n, int(round(max_rank - smooth_y + 1))))
            y0 = smooth_y - bar_h / 2.0
            d_rate = float(deltas_row[country])

            vis_val = max(val, max_val * 0.062)

            # 1. Soft 3D Rounded Drop Shadow
            shadow_verts = make_smooth_capsule_polygon(
                max_val * 0.008, y0 - 0.085, vis_val, bar_h, rx_left, rx_right, ry, n_arc=20
            )
            shadow_poly = Polygon(
                shadow_verts, closed=True, facecolor='#02040a', alpha=0.85 * alpha, edgecolor='none', zorder=2
            )
            ax.add_patch(shadow_poly)

            # 2. Smooth 3D Lower Extrusion Base
            base_color = '#0284c7' if d_rate > 0.025 else '#1e3a8a'
            base_verts = make_smooth_capsule_polygon(
                max_val * 0.004, y0 - 0.042, vis_val, bar_h, rx_left, rx_right, ry, n_arc=20
            )
            base_poly = Polygon(
                base_verts, closed=True, facecolor=base_color, alpha=0.90 * alpha, edgecolor='none', zorder=2.5
            )
            ax.add_patch(base_poly)

            # 3. Main Smooth Rounded 3D Capsule with Electric Blue Gradient & Pulse Wave
            bar_verts = make_smooth_capsule_polygon(0, y0, vis_val, bar_h, rx_left, rx_right, ry, n_arc=24)
            clip_poly = Polygon(bar_verts, closed=True, facecolor='none', edgecolor='none', zorder=3)
            ax.add_patch(clip_poly)

            tex = build_electric_blue_3d_texture(
                norm_rank, d_rate, pulse_phase=pulse_global - norm_rank * 0.35, alpha=alpha
            )
            im = ax.imshow(
                tex, extent=[0, vis_val, y0, y0 + bar_h],
                aspect='auto', origin='lower', interpolation='bicubic', zorder=3.5
            )
            im.set_clip_path(clip_poly)

            # 4. Subtle Smooth Rounded Neon-Cyan Rim Outline
            rim_color = '#a5f3fc' if d_rate > 0.025 else '#60a5fa'
            rim_poly = Polygon(
                bar_verts, closed=True, facecolor='none',
                edgecolor=rim_color, linewidth=1.15, alpha=0.75 * alpha, zorder=4.5
            )
            ax.add_patch(rim_poly)

            # 5. Rank Badge
            rank_color = '#38bdf8' if rank_num <= 3 else '#64748b'
            ax.text(
                -0.62, smooth_y, f"#{rank_num:02d}",
                transform=ax.get_yaxis_transform(),
                color=rank_color, fontsize=10.5, fontweight='bold', fontfamily='DejaVu Sans Mono',
                va='center', ha='left', alpha=alpha, zorder=6, clip_on=False
            )

            # 6. Country Name
            ax.text(
                -0.165, smooth_y, country,
                transform=ax.get_yaxis_transform(),
                color='#f8fafc', fontsize=12.0, fontweight='bold', fontfamily='DejaVu Sans',
                va='center', ha='right', alpha=alpha, zorder=6, clip_on=False
            )

            # 7. Rounded Flag
            if country in flags:
                imagebox = OffsetImage(flags[country], zoom=0.44, alpha=alpha)
                ab = AnnotationBbox(
                    imagebox, (-0.078, smooth_y),
                    xycoords=('axes fraction', 'data'),
                    frameon=False,
                    box_alignment=(0.5, 0.5),
                    zorder=5,
                    annotation_clip=False
                )
                ax.add_artist(ab)

            # 8. Value Label in TWh + Surge Indicator
            surge_tag = " ▲" if d_rate > 0.025 else ""
            label_color = '#a5f3fc' if d_rate > 0.025 else '#38bdf8'
            ax.text(
                vis_val + max_val * 0.022, smooth_y, f"{val:,.0f} TWh{surge_tag}",
                color=label_color, fontsize=11.8, fontweight='bold', fontfamily='DejaVu Sans',
                va='center', ha='left', alpha=alpha, zorder=6
            )

        ax.set_yticks([])
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_color('#3b82f6')
        ax.spines['left'].set_linewidth(1.5)
        ax.spines['bottom'].set_color('#1e293b')
        ax.tick_params(axis='x', colors='#94a3b8', labelsize=9.5)
        ax.xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: f"{int(x):,}"))

        # Smooth Rounded Grid HUD Box in bottom-right corner
        hud_box = FancyBboxPatch(
            (0.48, 0.025), 0.48, 0.15,
            boxstyle="round,pad=0.015,rounding_size=0.04",
            transform=ax.transAxes,
            facecolor='#0f172a', edgecolor='#3b82f6', linewidth=1.6, alpha=0.94, zorder=5
        )
        ax.add_patch(hud_box)

        ax.text(
            0.93, 0.125, f"{year_int}", transform=ax.transAxes,
            color='#ffffff', fontsize=38, fontweight='bold', fontfamily='DejaVu Sans',
            ha='right', va='center', zorder=6
        )
        ax.text(
            0.93, 0.075, f"{date_str}", transform=ax.transAxes,
            color='#38bdf8', fontsize=13.5, fontweight='bold', fontfamily='DejaVu Sans',
            ha='right', va='center', zorder=6
        )
        total_twh = int(vals_row.dropna().sum())
        ax.text(
            0.93, 0.043, f"GRID OUTPUT: {total_twh:,} TWh", transform=ax.transAxes,
            color='#93c5fd', fontsize=8.8, fontweight='bold', fontfamily='DejaVu Sans',
            ha='right', va='center', zorder=6
        )

        if frame_idx % 120 == 0 or frame_idx == TOTAL_FRAMES - 1:
            pct = int((frame_idx + 1) / TOTAL_FRAMES * 100)
            print(f"    Rendering progress: {pct}% ({frame_idx + 1}/{TOTAL_FRAMES} frames)")

    temp_video = os.path.join(TEMP_DIR, "silent_energy_video.mp4")
    writer = animation.FFMpegWriter(fps=FPS, codec='libx264', bitrate=5500, extra_args=['-pix_fmt', 'yuv420p'])
    anim = animation.FuncAnimation(fig, update, frames=TOTAL_FRAMES, interval=1000 / FPS, repeat=False)
    anim.save(temp_video, writer=writer)
    plt.close(fig)

    print(" -> Mixing audio track and encoding final MP4...")
    subprocess.check_call([
        ffmpeg_exe, "-y",
        "-i", temp_video,
        "-i", audio_path,
        "-c:v", "copy",
        "-c:a", "aac",
        "-b:a", "192k",
        "-shortest",
        FINAL_OUTPUT
    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f" -> SUCCESS! Final video saved as: {FINAL_OUTPUT}")


if __name__ == "__main__":
    if "--worker" in sys.argv:
        run_worker()
    else:
        run_bootstrap()
