from pathlib import Path

from pypdf import PdfReader

pdf = Path(r"C:\Users\parte\Desktop\резюме.pdf")
out_dir = Path(r"C:\Users\parte\Documents\Codex\2026-06-01\files-mentioned-by-the-user-pdf-2\work\resume_images")
out_dir.mkdir(parents=True, exist_ok=True)

reader = PdfReader(str(pdf))
saved = []
for page_index, page in enumerate(reader.pages, start=1):
    for image_index, image in enumerate(page.images, start=1):
        suffix = Path(image.name).suffix or ".png"
        out = out_dir / f"page{page_index}_image{image_index}{suffix}"
        out.write_bytes(image.data)
        saved.append((out, len(image.data), image.name))

for out, size, name in saved:
    print(f"{out} | {size} | {name}")

if not saved:
    print("NO_IMAGES_FOUND")
