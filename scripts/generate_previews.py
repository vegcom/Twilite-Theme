import json
from PIL import Image
import os

def generate_previews(json_file, output_dir):
with open(json_file, 'r') as f:
    theme = json.load(f)
colors = theme['colors']
os.makedirs(output_dir, exist_ok=True)
for color_name, hex_code in colors.items():
    # Remove # and convert to RGB
    rgb = tuple(int(hex_code.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))
    img = Image.new('RGB', (100, 100), rgb)
    # Save as PNG with color code as filename
    filename = f'{color_name.replace(\" \", \"_\")}_{hex_code.lstrip(\"#\")}.png'
    img.save(os.path.join(output_dir, filename))

generate_previews('twilite.json', 'assets/img/twilite')
generate_previews('twilite-darker.json', 'assets/img/twilite-darker')