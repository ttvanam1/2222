from base64 import b64encode
from pathlib import Path

ROOT = Path(r"C:\Users\parte\Documents\Codex\2026-06-01\files-mentioned-by-the-user-pdf-2")
OUT = ROOT / "outputs" / "tilda_portfolio_code.html"

FONTS = {
    "TITLE": Path(r"C:\Users\parte\Downloads\DrukCyr\Druk Condensed Cyrillic\Druk XXCondensed Cyr Super.otf"),
    "MONO_REG": Path(r"C:\Users\parte\Downloads\IBMPlexMono-Regular.ttf"),
    "MONO_MED": Path(r"C:\Users\parte\Downloads\IBMPlexMono-Medium.ttf"),
    "MONO_SEMI": Path(r"C:\Users\parte\Downloads\IBMPlexMono-SemiBold.ttf"),
    "MONO_BOLD": Path(r"C:\Users\parte\Downloads\IBMPlexMono-Bold.ttf"),
}
PHOTO = Path(r"C:\Users\parte\Documents\Codex\2026-06-01\files-mentioned-by-the-user-pdf-2\work\resume_images\resume_photo.jpg")
WORK_001 = Path(r"C:\Users\parte\Documents\Codex\2026-06-01\files-mentioned-by-the-user-pdf-2\work\portfolio_work_001.jpg")
WORK_002 = Path(r"C:\Users\parte\Documents\Codex\2026-06-01\files-mentioned-by-the-user-pdf-2\work\portfolio_work_002.jpg")
WORK_003 = Path(r"C:\Users\parte\Documents\Codex\2026-06-01\files-mentioned-by-the-user-pdf-2\work\omsk_bekon_booklet_page1.jpg")


def font_data(path: Path) -> str:
    return b64encode(path.read_bytes()).decode("ascii")


template = r'''<meta charset="UTF-8">
<section class="dn-profile" id="portfolio">
  <style>
    @font-face {
      font-family: "DN Title";
      src: url("data:font/otf;base64,__TITLE__") format("opentype");
      font-weight: 900;
      font-style: normal;
      font-display: swap;
    }

    @font-face {
      font-family: "DN Mono";
      src: url("data:font/ttf;base64,__MONO_REG__") format("truetype");
      font-weight: 400;
      font-style: normal;
      font-display: swap;
    }

    @font-face {
      font-family: "DN Mono";
      src: url("data:font/ttf;base64,__MONO_MED__") format("truetype");
      font-weight: 500;
      font-style: normal;
      font-display: swap;
    }

    @font-face {
      font-family: "DN Mono";
      src: url("data:font/ttf;base64,__MONO_SEMI__") format("truetype");
      font-weight: 600;
      font-style: normal;
      font-display: swap;
    }

    @font-face {
      font-family: "DN Mono";
      src: url("data:font/ttf;base64,__MONO_BOLD__") format("truetype");
      font-weight: 700;
      font-style: normal;
      font-display: swap;
    }

    .dn-profile {
      --bg: #050505;
      --paper: #eef2ed;
      --soft: #c8cec4;
      --muted: #858d81;
      --line: rgba(238, 242, 237, .22);
      --grid: rgba(238, 242, 237, .065);
      --acid: #b6ff00;
      --panel: rgba(9, 10, 8, .88);
      width: 100%;
      min-height: 100vh;
      overflow: hidden;
      background:
        linear-gradient(90deg, var(--grid) 1px, transparent 1px),
        linear-gradient(180deg, var(--grid) 1px, transparent 1px),
        var(--bg);
      background-size: 8.333% 100%, 100% 24px, auto;
      color: var(--paper);
      font-family: "DN Mono", "IBM Plex Mono", Consolas, monospace;
      letter-spacing: 0;
    }

    .dn-profile *,
    .dn-profile *::before,
    .dn-profile *::after {
      box-sizing: border-box;
    }

    .dn-wrap {
      width: min(1240px, calc(100% - 32px));
      margin: 0 auto;
      display: grid;
      grid-template-columns: repeat(12, minmax(0, 1fr));
      gap: 12px;
    }

    .dn-title-font {
      font-family: "DN Title", Impact, "Arial Narrow", sans-serif;
      font-weight: 900;
      text-transform: uppercase;
      letter-spacing: 0;
    }

    .dn-span-3 { grid-column: span 3; }
    .dn-span-4 { grid-column: span 4; }
    .dn-span-5 { grid-column: span 5; }
    .dn-span-6 { grid-column: span 6; }
    .dn-span-7 { grid-column: span 7; }
    .dn-span-8 { grid-column: span 8; }
    .dn-span-12 { grid-column: 1 / -1; }

    .dn-top {
      padding: 24px 0 12px;
      border-bottom: 1px solid var(--line);
    }

    .dn-cell {
      min-height: 54px;
      padding-top: 8px;
      border-top: 1px solid var(--line);
      color: var(--muted);
      font-size: 11px;
      line-height: 1.2;
      text-transform: uppercase;
    }

    .dn-cell strong {
      display: block;
      margin-top: 7px;
      color: var(--paper);
      font-size: 14px;
      line-height: 1.05;
      font-weight: 500;
    }

    .dn-hero {
      --hero-card-h: clamp(560px, 46vw, 640px);
      padding: 40px 0 24px;
      border-bottom: 1px solid var(--line);
    }

    .dn-hero .dn-wrap {
      min-height: 410px;
      align-items: end;
    }

    .dn-name {
      grid-column: 3 / 6;
      align-self: end;
      min-height: var(--hero-card-h);
      display: flex;
      flex-direction: column;
      justify-content: flex-end;
      border: 1px solid transparent;
    }

    .dn-name h1 {
      margin: 0;
      font-size: clamp(92px, 16.4vw, 224px);
      line-height: .82;
      letter-spacing: .018em;
      word-spacing: .04em;
    }

    .dn-name h1 span {
      display: block;
    }

    .dn-role {
      margin-top: 14px;
      color: var(--paper);
      font-size: clamp(15px, 1.7vw, 22px);
      line-height: 1.1;
      font-weight: 500;
      text-transform: uppercase;
    }

    .dn-quote {
      max-width: 720px;
      margin-top: 24px;
      color: var(--paper);
      font-size: clamp(16px, 2.2vw, 30px);
      line-height: 1.08;
      font-weight: 600;
      text-transform: uppercase;
    }

    .dn-photo-card {
      grid-column: 6 / 9;
      align-self: end;
      height: var(--hero-card-h);
      border: 1px solid var(--line);
      background: var(--panel);
      overflow: hidden;
      display: grid;
      grid-template-rows: auto 1fr;
    }

    .dn-photo-card .dn-side-head {
      border-bottom: 1px solid var(--line);
    }

    .dn-side {
      grid-column: 9 / 12;
      align-self: end;
      height: var(--hero-card-h);
      border: 1px solid var(--line);
      background: var(--panel);
      display: grid;
      grid-template-rows: auto 1fr auto;
    }

    .dn-side-head {
      padding: 14px;
      border-bottom: 1px solid var(--line);
      color: var(--acid);
      font-size: 12px;
      line-height: 1.22;
      font-weight: 500;
      text-transform: uppercase;
    }

    .dn-photo {
      min-height: 0;
      overflow: hidden;
      background: #0a0d0c;
    }

    .dn-photo img {
      width: 100%;
      height: 100%;
      display: block;
      object-fit: contain;
      object-position: center center;
      filter: grayscale(100%) contrast(1.08);
    }

    .dn-side-row {
      display: grid;
      grid-template-columns: 1fr 1.35fr;
      gap: 12px;
      padding: 13px 14px;
      border-bottom: 1px solid var(--line);
      font-size: 11px;
      line-height: 1.25;
      text-transform: uppercase;
    }

    .dn-side-row span {
      color: var(--muted);
    }

    .dn-side-row strong,
    .dn-side-row a {
      color: var(--paper) !important;
      font-weight: 500;
      text-align: right;
      text-decoration: none !important;
      overflow-wrap: anywhere;
    }

    .dn-binary {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      border-top: 1px solid var(--line);
    }

    .dn-binary div {
      min-height: 72px;
      display: grid;
      place-items: center;
      border-right: 1px solid var(--line);
      color: var(--acid);
      font-size: 22px;
      line-height: 1;
      font-weight: 600;
    }

    .dn-binary div:last-child {
      border-right: 0;
    }

    .dn-ticker {
      border-bottom: 1px solid var(--line);
      overflow: hidden;
      color: var(--acid);
      font-size: 12px;
      line-height: 1;
      text-transform: uppercase;
      white-space: nowrap;
    }

    .dn-ticker span {
      display: inline-block;
      padding: 15px 0;
      animation: dn-run 28s linear infinite;
    }

    @keyframes dn-run {
      from { transform: translateX(0); }
      to { transform: translateX(-50%); }
    }

    .dn-board {
      padding: 16px 0 52px;
    }

    .dn-card {
      min-height: 214px;
      border: 1px solid var(--line);
      background: var(--panel);
      padding: 16px;
      display: flex;
      flex-direction: column;
    }

    .dn-card--flat {
      min-height: 150px;
    }

    .dn-label {
      color: var(--acid);
      font-size: 12px;
      line-height: 1.25;
      font-weight: 500;
      text-transform: uppercase;
    }

    .dn-card h2,
    .dn-card h3 {
      margin: 18px 0 0;
      color: var(--paper);
      font-size: clamp(19px, 2.2vw, 31px);
      line-height: 1.12;
      font-weight: 600;
      text-transform: uppercase;
    }

    .dn-card p {
      margin: 15px 0 0;
      color: var(--soft);
      font-size: 14px;
      line-height: 1.62;
      font-weight: 400;
    }

    .dn-list {
      display: grid;
      grid-template-columns: repeat(2, minmax(0, 1fr));
      gap: 8px;
      margin-top: auto;
      padding-top: 20px;
    }

    .dn-pill {
      min-height: 44px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 10px;
      border: 1px solid var(--line);
      padding: 10px;
      color: var(--paper);
      font-size: 12px;
      line-height: 1.15;
      font-weight: 500;
      text-transform: uppercase;
    }

    .dn-pill em {
      color: var(--acid);
      font-style: normal;
    }

    .dn-tools {
      display: grid;
      grid-template-columns: repeat(5, minmax(0, 1fr));
      gap: 8px;
      margin-top: auto;
      padding-top: 18px;
    }

    .dn-tool {
      min-height: 96px;
      border: 1px solid var(--line);
      padding: 10px;
      display: grid;
      grid-template-rows: auto 1fr;
      gap: 8px;
      color: var(--paper);
      font-size: 11px;
      line-height: 1.12;
      font-weight: 500;
      text-transform: uppercase;
    }

    .dn-tool-top {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 10px;
    }

    .dn-tool b {
      color: var(--acid);
      font-size: 15px;
      line-height: 1;
      font-weight: 600;
    }

    .dn-tool-name {
      align-self: end;
    }

    .dn-app-icon {
      width: 34px;
      height: 34px;
      flex: 0 0 34px;
      display: grid;
      place-items: center;
      border: 1px solid currentColor;
      font-size: 13px;
      line-height: 1;
      font-weight: 700;
      letter-spacing: 0;
      text-transform: none;
    }

    .dn-app-corel {
      background: #041b10;
      color: #65ff74;
    }

    .dn-app-ai {
      background: #2b1600;
      color: #ff9a00;
    }

    .dn-app-ps {
      background: #001e36;
      color: #31a8ff;
    }

    .dn-app-id {
      background: #2b0014;
      color: #ff3366;
    }

    .dn-app-figma {
      border-color: var(--line);
      background: #050505;
      display: grid;
      grid-template-columns: repeat(2, 10px);
      grid-template-rows: repeat(3, 10px);
      gap: 0;
      padding: 5px 6px;
      place-items: stretch;
    }

    .dn-app-figma i {
      display: block;
      width: 10px;
      height: 10px;
    }

    .dn-app-figma i:nth-child(1) { background: #f24e1e; border-radius: 10px 0 0 10px; }
    .dn-app-figma i:nth-child(2) { background: #ff7262; border-radius: 0 10px 10px 0; }
    .dn-app-figma i:nth-child(3) { background: #a259ff; border-radius: 10px 0 0 10px; }
    .dn-app-figma i:nth-child(4) { background: #1abcfe; border-radius: 10px; }
    .dn-app-figma i:nth-child(5) { background: #0acf83; border-radius: 10px 0 10px 10px; }

    .dn-works {
      grid-column: 1 / -1;
      border: 1px solid var(--line);
      background: var(--panel);
      padding: 16px;
    }

    .dn-works-head {
      display: grid;
      grid-template-columns: 220px 1fr;
      gap: 16px;
      align-items: start;
      padding-bottom: 16px;
      border-bottom: 1px solid var(--line);
    }

    .dn-works-head h2 {
      margin: 0;
      color: var(--paper);
      font-size: clamp(21px, 2.7vw, 38px);
      line-height: 1.08;
      font-weight: 600;
      text-transform: uppercase;
    }

    .dn-work-list {
      margin-top: 10px;
    }

    .dn-work {
      border-bottom: 1px solid var(--line);
    }

    .dn-work:last-child {
      border-bottom: 0;
    }

    .dn-work summary {
      min-height: 58px;
      display: grid;
      grid-template-columns: 120px 1fr 170px 28px;
      gap: 14px;
      align-items: center;
      cursor: pointer;
      list-style: none;
      color: var(--paper);
      font-size: 12px;
      line-height: 1.2;
      font-weight: 500;
      text-transform: uppercase;
    }

    .dn-work summary::-webkit-details-marker {
      display: none;
    }

    .dn-work summary span {
      color: var(--acid);
    }

    .dn-work summary strong {
      font-weight: 600;
    }

    .dn-work summary em {
      color: var(--muted);
      font-style: normal;
      text-align: right;
    }

    .dn-work summary::after {
      content: "+";
      color: var(--acid);
      font-size: 20px;
      line-height: 1;
      text-align: right;
    }

    .dn-work[open] summary::after {
      content: "-";
    }

    .dn-work-body {
      display: grid;
      grid-template-columns: 1.25fr .75fr;
      gap: 12px;
      padding: 0 0 16px 134px;
      animation: dn-slide .22s ease;
    }

    @keyframes dn-slide {
      from { opacity: 0; transform: translateY(-8px); }
      to { opacity: 1; transform: translateY(0); }
    }

    .dn-work-visual {
      min-height: 260px;
      border: 1px solid var(--line);
      position: relative;
      overflow: hidden;
      background:
        linear-gradient(90deg, rgba(238,242,237,.08) 1px, transparent 1px),
        linear-gradient(180deg, rgba(238,242,237,.08) 1px, transparent 1px),
        #080908;
      background-size: 32px 100%, 100% 32px, auto;
    }

    .dn-work-visual::before {
      content: "IMAGE / WORK SLOT";
      position: absolute;
      left: 14px;
      bottom: 14px;
      color: var(--acid);
      font-size: 11px;
      line-height: 1;
      text-transform: uppercase;
    }

    .dn-work-visual img {
      width: 100%;
      height: 100%;
      display: block;
      object-fit: contain;
      object-position: center center;
    }

    .dn-work-copy {
      border: 1px solid var(--line);
      padding: 14px;
    }

    .dn-work-copy p {
      margin: 0;
      color: var(--soft);
      font-size: 13px;
      line-height: 1.55;
    }

    .dn-work-copy p + p {
      margin-top: 12px;
    }

    .dn-contact-actions {
      display: grid;
      grid-template-columns: repeat(2, minmax(0, 1fr));
      gap: 8px;
      margin-top: auto;
      padding-top: 20px;
    }

    .dn-btn {
      min-height: 46px;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      border: 1px solid var(--acid);
      background: var(--acid);
      color: var(--bg) !important;
      padding: 0 12px;
      font-size: 12px;
      font-weight: 600;
      line-height: 1;
      text-transform: uppercase;
      text-decoration: none !important;
    }

    .dn-btn--dark {
      background: transparent;
      color: var(--paper) !important;
      border-color: var(--line);
    }

    @media (max-width: 980px) {
      .dn-profile {
        background-size: 16.666% 100%, 100% 24px, auto;
      }

      .dn-wrap {
        grid-template-columns: repeat(6, minmax(0, 1fr));
      }

      .dn-span-3,
      .dn-span-4,
      .dn-span-5,
      .dn-span-6,
      .dn-span-7,
      .dn-span-8 {
        grid-column: span 3;
      }

      .dn-name,
      .dn-photo-card,
      .dn-side,
      .dn-span-12 {
        grid-column: 1 / -1;
      }
    }

    @media (max-width: 640px) {
      .dn-profile {
        background-size: 25% 100%, 100% 22px, auto;
      }

      .dn-wrap {
        width: min(100% - 22px, 1240px);
        grid-template-columns: repeat(4, minmax(0, 1fr));
        gap: 10px;
      }

      .dn-top {
        padding-top: 14px;
      }

      .dn-cell,
      .dn-span-3,
      .dn-span-4,
      .dn-span-5,
      .dn-span-6,
      .dn-span-7,
      .dn-span-8,
      .dn-span-12,
      .dn-name,
      .dn-photo-card,
      .dn-side {
        grid-column: 1 / -1;
      }

      .dn-hero {
        --hero-card-h: 360px;
        padding: 30px 0 16px;
      }

      .dn-hero .dn-wrap {
        min-height: auto;
      }

      .dn-name h1 {
        font-size: clamp(68px, 22.6vw, 110px);
        line-height: .84;
        letter-spacing: .014em;
      }

      .dn-role {
        font-size: 14px;
      }

      .dn-quote {
        font-size: clamp(17px, 6vw, 28px);
        line-height: 1.1;
      }

      .dn-list,
      .dn-tools,
      .dn-contact-actions {
        grid-template-columns: 1fr;
      }

      .dn-works-head,
      .dn-work summary,
      .dn-work-body {
        grid-template-columns: 1fr;
      }

      .dn-work summary {
        gap: 7px;
        padding: 13px 0;
      }

      .dn-work summary em {
        text-align: left;
      }

      .dn-work summary::after {
        position: absolute;
        right: 0;
      }

      .dn-work-body {
        padding: 0 0 14px;
      }

      .dn-work-visual {
        min-height: 190px;
      }
    }

    @media (min-width: 520px) and (max-width: 640px) {
      .dn-hero .dn-wrap {
        grid-template-columns: repeat(6, minmax(0, 1fr));
      }

      .dn-name {
        grid-column: 1 / 3;
        align-self: end;
        min-height: var(--hero-card-h);
      }

      .dn-photo-card {
        grid-column: 3 / 5;
        align-self: end;
        height: var(--hero-card-h);
      }

      .dn-side {
        grid-column: 5 / 7;
        align-self: end;
        height: var(--hero-card-h);
        grid-template-rows: auto auto;
      }

      .dn-side-info {
        display: none;
      }

      .dn-side-head {
        padding: 10px;
        font-size: 10px;
        line-height: 1.25;
      }

      .dn-photo {
        min-height: 0;
      }

      .dn-binary div {
        min-height: 50px;
        font-size: 16px;
      }

      .dn-name h1 {
        font-size: clamp(48px, 10.5vw, 66px);
        line-height: .88;
        letter-spacing: .018em;
      }

      .dn-role {
        margin-top: 12px;
        font-size: 12px;
      }

      .dn-quote {
        max-width: 100%;
        margin-top: 18px;
        font-size: clamp(15px, 3.3vw, 20px);
        line-height: 1.18;
      }
    }
  </style>

  <div class="dn-top">
    <div class="dn-wrap">
      <div class="dn-cell dn-span-3">Designer profile<strong>Graphic designer</strong></div>
      <div class="dn-cell dn-span-3">Build<strong>Design / destroy / rebuild</strong></div>
      <div class="dn-cell dn-span-3">Based in<strong>Omsk, Russia</strong></div>
      <div class="dn-cell dn-span-3">Local time<strong>UTC+6 / MSK+3</strong></div>
    </div>
  </div>

  <div class="dn-hero">
    <div class="dn-wrap">
      <div class="dn-name">
        <h1 class="dn-title-font"><span>Даниил</span><span>Неворотов</span></h1>
        <div class="dn-role">GRAPHIC DESIGNER / VER 2.0.1</div>
        <div class="dn-quote">Не бойтесь того, что подумают другие, ибо они редко вообще о чем-либо думают.</div>
      </div>

      <div class="dn-photo-card">
        <div class="dn-side-head">PHOTO / PROFILE / SYS_02</div>
        <div class="dn-photo"><img src="data:image/jpeg;base64,__PHOTO__" alt="Даниил Неворотов"></div>
      </div>

      <aside class="dn-side">
        <div class="dn-side-head">WIEW PORTFOLIO / STATUS: ONLINE / SYS_02</div>
        <div class="dn-side-info">
          <div class="dn-side-row"><span>Born on</span><strong>24.12.2004</strong></div>
          <div class="dn-side-row"><span>Telegram</span><a href="https://t.me/ANAM1I" target="_blank" rel="noopener">@ANAM1ITELEGRAM</a></div>
          <div class="dn-side-row"><span>Discord</span><strong>@ANAM1I</strong></div>
          <div class="dn-side-row"><span>Email</span><a href="mailto:PARTEZAN03@GMAIL.COM">PARTEZAN03@GMAIL.COM</a></div>
          <div class="dn-side-row"><span>MAX</span><strong>+7908(790)80-43</strong></div>
        </div>
        <div class="dn-binary"><div>001</div><div>010</div><div>101</div></div>
      </aside>
    </div>
  </div>

  <div class="dn-ticker">
    <span>BUILD / DESIGN / DESTROY / REBUILD / LOGO / PACKAGING / PRINT / LAYOUT / WEB / PRESENTATION / VER 2.0.1 / 2026 / BUILD / DESIGN / DESTROY / REBUILD / LOGO / PACKAGING / PRINT / LAYOUT / WEB / PRESENTATION / VER 2.0.1 / 2026 / </span>
  </div>

  <div class="dn-board">
    <div class="dn-wrap">
      <section class="dn-card dn-span-7">
        <div class="dn-label">// 01 / Профиль</div>
        <h2>Начинающий графический дизайнер</h2>
        <p>Разрабатываю фирменный стиль, логотипы, упаковку, презентации и полиграфическую продукцию. Стремлюсь создавать понятные, современные и эффективные визуальные решения.</p>
        <p>Лучше всего раскрываюсь в условиях понятных целей и конкретных сроков.</p>
      </section>

      <section class="dn-card dn-span-5">
        <div class="dn-label">// 02 / Кредо</div>
        <h2>Система. Дисциплина. Развитие.</h2>
        <p>Любознательный, дисциплинированный и ориентированный на развитие. Люблю изучать новые инструменты, получать практический опыт и отвечать за результат.</p>
      </section>

      <section class="dn-card dn-span-8">
        <div class="dn-label">// 03 / Инструмент & навыки</div>
        <div class="dn-tools">
          <div class="dn-tool">
            <div class="dn-tool-top"><span class="dn-app-icon dn-app-corel">C</span><b>CDR</b></div>
            <div class="dn-tool-name">CorelDRAW</div>
          </div>
          <div class="dn-tool">
            <div class="dn-tool-top"><span class="dn-app-icon dn-app-ai">Ai</span><b>Ai</b></div>
            <div class="dn-tool-name">Illustrator</div>
          </div>
          <div class="dn-tool">
            <div class="dn-tool-top"><span class="dn-app-icon dn-app-ps">Ps</span><b>Ps</b></div>
            <div class="dn-tool-name">Photoshop</div>
          </div>
          <div class="dn-tool">
            <div class="dn-tool-top">
              <span class="dn-app-icon dn-app-figma" aria-label="Figma">
                <i></i><i></i><i></i><i></i><i></i>
              </span>
              <b>Fg</b>
            </div>
            <div class="dn-tool-name">Figma</div>
          </div>
          <div class="dn-tool">
            <div class="dn-tool-top"><span class="dn-app-icon dn-app-id">Id</span><b>Id</b></div>
            <div class="dn-tool-name">InDesign</div>
          </div>
        </div>
      </section>

      <section class="dn-card dn-span-4">
        <div class="dn-label">// 04 / Образование</div>
        <h3>2022-2026</h3>
        <p>БПОУ «Омский авиационный колледж имени Н.Е. Жуковского»<br>«Графический дизайн» 54.01.20</p>
      </section>

      <section class="dn-card dn-card--flat dn-span-12">
        <div class="dn-label">// 05 / Опыт работы / направления</div>
        <div class="dn-list">
          <div class="dn-pill">Логотипы <em>001</em></div>
          <div class="dn-pill">Упаковка <em>010</em></div>
          <div class="dn-pill">Полиграфия <em>101</em></div>
          <div class="dn-pill">Верстка <em>002</em></div>
          <div class="dn-pill">Веб-дизайн <em>011</em></div>
          <div class="dn-pill">Презентации <em>100</em></div>
        </div>
      </section>

      <section class="dn-works" id="dn-works">
        <div class="dn-works-head">
          <div class="dn-label">// 06 / Portfolio list</div>
          <h2>Место для работ: выезжающий список кейсов</h2>
        </div>

        <div class="dn-work-list">
          <details class="dn-work" open>
            <summary><span>WORK 001</span><strong>STO / Sport Training Optimization</strong><em>Логотип / айдентика</em></summary>
            <div class="dn-work-body">
              <div class="dn-work-visual"><img src="data:image/jpeg;base64,__WORK_001__" alt="Мокап вывески STO для магазина спортивного питания"></div>
              <div class="dn-work-copy">
                <p>Задача: разработать логотип с нуля для магазина спортивного питания. Нужен был знак, который быстро читается на вывеске, упаковке, стикерах и цифровых носителях.</p>
                <p>Решение: минималистичная капсульная форма как отсылка к спортивному питанию и добавкам. Красный блок отвечает за энергию и действие, темно-синий - за надежность, режим и системный подход.</p>
                <p>STO раскрывается как Sport Training Optimization: короткая аббревиатура, простая геометрия, чистая типографика и понятная визуальная система без лишнего шума.</p>
              </div>
            </div>
          </details>

          <details class="dn-work">
            <summary><span>WORK 002</span><strong>Маленькие чудеса / адвент-календарь</strong><em>Упаковка / развертка</em></summary>
            <div class="dn-work-body">
              <div class="dn-work-visual"><img src="data:image/jpeg;base64,__WORK_002__" alt="Развертка упаковки адвент-календаря Маленькие чудеса"></div>
              <div class="dn-work-copy">
                <p>Задача: разработать упаковку для адвент-календаря «Маленькие чудеса» с тематикой 1 сентября. Формат должен был быть ярким, детским и запоминающимся.</p>
                <p>Решение: упаковка построена вокруг формы карандаша. Высокая коробка работает как главный объект, а маленький модуль дополняет набор и может использоваться для заданий, подарков или бонусов.</p>
                <p>Развертка разработана самостоятельно: конструкция, визуальная система, иллюстрации, декоративные маршруты, наклейки и подготовка макета к сборке. Акцент сделан на игровой характер, школьную тему и ощущение маленького праздника.</p>
              </div>
            </div>
          </details>

          <details class="dn-work">
            <summary><span>WORK 003</span><strong>Омский бекон / буклет</strong><em>Верстка / печать</em></summary>
            <div class="dn-work-body">
              <div class="dn-work-visual"><img src="data:image/jpeg;base64,__WORK_003__" alt="Буклет Омский бекон"></div>
              <div class="dn-work-copy">
                <p>Задача: сверстать печатный буклет для «Омского бекона» по строгому техническому заданию и в рамках уже сформированного фирменного стиля.</p>
                <p>Проект требовал аккуратной работы с готовой айдентикой крупной компании: логотип, фирменные цвета, продуктовые фотографии, композиция разворота и рекламные сообщения должны были выглядеть цельно.</p>
                <p>Решение: чистая сетка, понятная иерархия, крупные визуальные акценты на продукте и подготовка макета к печати без нарушения брендовых правил.</p>
              </div>
            </div>
          </details>

          <details class="dn-work">
            <summary><span>WORK 004</span><strong>Название проекта</strong><em>Веб / презентация</em></summary>
            <div class="dn-work-body">
              <div class="dn-work-visual"><!-- Вставьте сюда изображение: <img src="ССЫЛКА_НА_РАБОТУ" alt=""> --></div>
              <div class="dn-work-copy">
                <p>Задача: лендинг, презентация или цифровой материал.</p>
                <p>Решение: структура, визуальный сценарий, понятная подача.</p>
              </div>
            </div>
          </details>
        </div>
      </section>

      <section class="dn-card dn-card--flat dn-span-12">
        <div class="dn-label">// 07 / Contact</div>
        <h3>Готов к проектам и практике</h3>
        <p>Если нужен логотип, упаковка, презентация, полиграфия или лендинг - напишите мне. Обсудим задачу, сроки и формат работы.</p>
        <div class="dn-contact-actions">
          <a class="dn-btn" href="https://t.me/ANAM1I" target="_blank" rel="noopener">Написать в Telegram</a>
          <a class="dn-btn dn-btn--dark" href="mailto:PARTEZAN03@GMAIL.COM">Отправить Email</a>
        </div>
      </section>
    </div>
  </div>
</section>
'''

html = template
for key, path in FONTS.items():
    html = html.replace(f"__{key}__", font_data(path))
html = html.replace("__PHOTO__", font_data(PHOTO))
html = html.replace("__WORK_001__", font_data(WORK_001))
html = html.replace("__WORK_002__", font_data(WORK_002))
html = html.replace("__WORK_003__", font_data(WORK_003))

OUT.write_text(html, encoding="utf-8", newline="\n")
print(OUT)
