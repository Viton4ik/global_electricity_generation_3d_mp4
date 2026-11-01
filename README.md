# ⚡ Global Electricity Generation (1960 – Oct 2026) | Smooth 3D Bar Chart Race Generator
# ⚡ Выработка электроэнергии по странам (1960 – Окт 2026) | 3D-генератор видео (Bar Chart Race)

![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![Format 9:16 MP4](https://img.shields.io/badge/Output-1080x1920%20MP4%20(30%20FPS)-38bdf8.svg)
![Audio CC0](https://img.shields.io/badge/Audio-CC0%201.0%20Public%20Domain-success.svg)

**[English](#english)** | **[Русский](#русский)**

---

<a name="english"></a>
## 🇬🇧 English

### Overview
An automated, self-contained Python pipeline that renders a **40-second vertical HD (9:16, 1080x1920, 30 FPS) MP4 video** with a driving electronic synth soundtrack. It visualizes the historical evolution of **Annual Electricity Generation by Country (in Terawatt-hours, TWh)** from **1960 to October 2026** based on International Energy Agency (IEA) and Energy Institute Statistical Review of World Energy data.

### Key Features
* **Classic Dark-Blue & Electric Cyan Palette with Dynamic Gradients:** Deep obsidian-navy background (`#070b14` / `#0b101e`) paired with sapphire-to-electric-cyan 3D gradient bars (`#1e3a8a` -> `#3b82f6` -> `#38bdf8`).
* **Smooth Rounded 3D Capsules (Zero Sharp Corners):** Every bar is rendered using aspect-corrected smooth rounded capsule geometry with cylindrical 3D Phong lighting, a cobalt lower extrusion bevel, and a soft drop shadow. National flags are masked with smooth rounded corners and a glowing cyan rim.
* **Dynamic Power-Surge Gradients & Multi-Layer Animations:**
  * **Power Surge Glow (`▲`):** When a nation's electricity generation accelerates rapidly, the bar tip dynamically shifts toward luminous ice-cyan (`#a5f3fc`).
  * **Travelling High-Voltage Pulse Wave:** An animated specular energy pulse continuously travels along each 3D bar.
  * **Floating Plasma Sparks & Live Grid Load Bar:** Rising and twinkling electric blue plasma particles in the background, plus a real-time timeline progress bar inside the top header capsule.
* **Royalty-Free Soundtrack (`CC0 1.0`):** Automatically synthesizes a 40-second stereo track (*"High-Voltage Grid Pulse"* — driving 120 BPM synth-bass, harmonic transformer pad, and crisp electric pulse arpeggio) and generates a `MUSIC_LICENSE_CC0.txt` certificate for safe monetization on YouTube Shorts, Instagram Reels, and TikTok.
* **Zero System Clutter (Auto-Venv & Self-Cleanup):** `run.py` automatically creates a temporary `.venv_energy_race` virtual environment, installs all required packages (including a portable `FFmpeg` binary via `imageio-ffmpeg`), renders the final `.mp4`, and completely removes the virtual environment and temporary files upon completion.

### Quick Start
1. Ensure **Python 3.8+** is installed on your machine.
2. Clone this repository or extract the project archive.
3. Run the generator with a single command:
   ```bash
   python run.py
   ```
   *(On macOS/Linux, you may use `python3 run.py`)*.

### Output Files
* `global_electricity_generation_1960_2026_shorts.mp4` — Final 40-second 1080x1920 vertical video with audio.
* `MUSIC_LICENSE_CC0.txt` — Public Domain (CC0 1.0) license certificate for the audio track.
* `YOUTUBE_DESCRIPTION.txt` — Ready-to-use title, description, data sources, and tags for social media publishing.

---

<a name="русский"></a>
## 🇷🇺 Русский

### Описание проекта
Полностью автономный генератор на Python, создающий **40-секундный вертикальный видеоролик высокой четкости (9:16, 1080x1920, 30 FPS) в формате `.mp4`** с энергичным электронным саундтреком. Видео наглядно демонстрирует динамику **годовой выработки электроэнергии по странам мира (в тераватт-часах, TWh)** с **1960 по октябрь 2026 года** на основе официальной статистики Международного энергетического агентства (IEA) и Energy Institute Statistical Review of World Energy.

### Ключевые особенности
* **Классическая темно-синяя неоновая палитра первого ролика с живым градиентом:** Глубокий темно-синий фон (`#070b14` / `#0b101e`) в сочетании с яркими сапфирово-циановыми 3D-полосками (`#1e3a8a` -> `#3b82f6` -> `#38bdf8`).
* **Гладкая 3D-геометрия без прямых углов:** Каждая полоска отрисовывается в виде обтекаемой 3D-капсулы со скругленными краями, цилиндрическим светотеневым шейдингом по модели Фонга, объемной кобальтовой нижней фаской и мягкой падающей тенью. Флаги стран также имеют плавно скругленные углы.
* **Реактивный градиент и многослойная анимация:**
  * **Индикация энергетического рывка (`▲`):** При стремительном росте генерации вершина капсулы плавно переливается в яркое ледяное циановое свечение (`#a5f3fc`).
  * **Бегущий высоковольтный импульс:** Вдоль каждой 3D-полоски непрерывно пробегает световая волна электрического импульса.
  * **Плазменные частицы и шкала нагрузки сети:** На фоне плавно поднимаются и пульсируют частицы электрической плазмы, а в верхней капсуле заголовка работает живая шкала прогресса времени.
* **Лицензионно чистая музыка (`CC0 1.0`):** Скрипт процедурно синтезирует 40-секундную стереодорожку (*«High-Voltage Grid Pulse»* — ритмичный синт-бас 120 BPM, гармонический пэд и импульсное арпеджио) и создает сертификат `MUSIC_LICENSE_CC0.txt` для безопасной монетизации в YouTube Shorts, Instagram Reels и TikTok.
* **Полная самоочистка (Auto-Venv & Cleanup):** При запуске `run.py` сам создает изолированную виртуальную среду `.venv_energy_race`, скачивает внутрь все библиотеки и портативный видеокодек `FFmpeg` (`imageio-ffmpeg`), собирает готовый `.mp4` и автоматически удаляет виртуальную среду и временные файлы после завершения.

### Быстрый запуск
1. Убедитесь, что у вас установлен **Python 3.8+**.
2. Склонируйте репозиторий или распакуйте архив проекта.
3. Запустите генерацию одной командой в терминале (PowerShell / Bash):
   ```bash
   python run.py
   ```
   *(На macOS / Linux может использоваться команда `python3 run.py`)*.

### Итоговые файлы после запуска
* `global_electricity_generation_1960_2026_shorts.mp4` — готовый 40-секундный вертикальный видеоролик со звуком.
* `MUSIC_LICENSE_CC0.txt` — сертификат свободной лицензии (CC0 1.0 Public Domain) на музыкальную дорожку.
* `YOUTUBE_DESCRIPTION.txt` — готовые заголовки, описание, источники и теги для загрузки на YouTube / Reels / TikTok.
