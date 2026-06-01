from pathlib import Path
import json

p = Path(r"C:\Users\parte\Documents\Codex\2026-06-01\files-mentioned-by-the-user-pdf-2\outputs\tilda_portfolio_code.html")
c = p.read_text(encoding="utf-8")

checks = {
    "uses_title_font": 'font-family: "DN Title"' in c,
    "uses_mono_fonts": c.count('font-family: "DN Mono"') >= 4,
    "name_present": "Даниил" in c and "Неворотов" in c,
    "portfolio_accordion": '<details class="dn-work"' in c,
    "work_slots": c.count("dn-work-visual"),
    "selected_works_removed": "Selected works" not in c,
    "project_placeholders_removed": "PROJECT 001" not in c,
    "mojibake": any(x in c for x in ["Рќ", "Р°", "Рџ", "Р”", "����"]),
    "size_kb": round(p.stat().st_size / 1024, 1),
}

print(json.dumps(checks, ensure_ascii=False, indent=2))
