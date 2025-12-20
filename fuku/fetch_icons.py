import urllib.request

icons = [
    "instagram", "map-pin", "clock", "wallet", "crosshair", "star", "zap", "menu",
    "youtube", "play-circle", "utensils", "alert-triangle", "hard-hat", "flame", "volume-2"
]
base_url = "https://unpkg.com/lucide-static@latest/icons/"

for icon in icons:
    try:
        url = f"{base_url}{icon}.svg"
        with urllib.request.urlopen(url) as response:
            content = response.read().decode('utf-8')
            start = content.find(">") + 1
            end = content.rfind("</svg>")
            inner = content[start:end].strip()
            inner = inner.replace("\n", " ").replace('"', "'")
            with open("icons.txt", "a", encoding="utf-8") as f:
                f.write(f"ICON_DATA|{icon}|{inner}\n")
    except Exception as e:
        with open("icons.txt", "a", encoding="utf-8") as f:
            f.write(f"ERROR|{icon}|{e}\n")
