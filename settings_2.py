from pathlib import Path
import sys

file_path = Path(__file__).resolve()
root_path = file_path.parent
if root_path not in sys.path:
    sys.path.append(str(root_path))
ROOT = root_path.relative_to(Path.cwd())

# ML Model config
MODEL_DIR = ROOT / 'weights'
DETECTION_MODEL = MODEL_DIR / 'best.pt'
# Webcam
WEBCAM_PATH = 0

RECOMMENDED = {
    "gelas_bekas":[{"nama":"gelas cangkir",
                    "link":"https://iili.io/3qxQsLJ.jpg",
                    "harga":"3000",
                    "satuan":"unit"},
                   {"nama":"cangkir stainless steel",
                    "link":"https://iili.io/3qxykjS.jpg",
                    "harga":"7000",
                    "satuan":"unit"}],
    "botol_bekas":[{"nama":"botol pelembut bekas",
                    "link":"https://iili.io/3qIpKbV.jpg",
                    "harga":"20000",
                    "satuan":"kilogram"},
                    {"nama":"botol tumblr 1.5 L",
                     "link":"https://iili.io/3qIpx0g.md.jpg",
                     "harga":"10000",
                     "satuan":"unit"},
                     {"nama":"botol tumblr 0.7 L",
                      "link":"https://iili.io/3qIpzga.jpg",
                      "harga":"80000",
                      "satuan":"kilogram"}]
}