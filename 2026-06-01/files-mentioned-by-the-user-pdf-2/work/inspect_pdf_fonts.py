from pathlib import Path

from pypdf import PdfReader

pdf = Path(r"C:\Users\parte\Desktop\резюме.pdf")
page = PdfReader(str(pdf)).pages[0]

print("FONT RESOURCES")
fonts = page["/Resources"].get("/Font", {})
for name, ref in fonts.items():
    font = ref.get_object()
    print(name, font.get("/BaseFont"), font.get("/Subtype"))

print("\nTEXT RUNS")
runs = []


def visitor_text(text, cm, tm, font_dict, font_size):
    if not text or not text.strip():
        return
    base = font_dict.get("/BaseFont") if font_dict else None
    runs.append((text.strip(), str(base), float(font_size), float(tm[4]), float(tm[5])))


page.extract_text(visitor_text=visitor_text)
for text, base, size, x, y in runs:
    print(repr(text), base, round(size, 2), round(x, 1), round(y, 1))
