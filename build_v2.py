import re

with open("/Users/mac/Downloads/fryzo-demo-v2.html", "r", encoding="utf-8") as f:
    orig = f.read()

# Extract IMG dictionary
img_start = orig.find("const IMG = {")
img_end = orig.find("};", img_start) + 2
img_code = orig[img_start:img_end]

# Extract M and menu item adds
m_start = orig.find("const M = [];")
m_end = orig.find("const CATS =")
menu_adds_code = orig[m_start:m_end]

new_html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Fryzo - Say Yes To Yumm | Lahore Fast Food</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:ital,wght@0,600;0,700;0,800;1,700;1,800&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
:root {{
  --bg: #121316;
  --panel: #1b1c21;
  --panel2: #24252c;
  --panel3: #2d2f38;
  --line: rgba(255, 255, 255, 0.08);
  --line-gold: rgba(245, 184, 24, 0.35);
  
  --gold: #f5b818;
  --gold2: #ffd04d;
  --red: #e0283c;
  --red-hover: #ff384d;
  --green: #25d366;
  --green-online: #3ddc84;
  --ink: #ffffff;
  --mute: #a3a7b3;
  --dim: #6c7080;
  
  --display: 'Barlow Condensed', sans-serif;
  --body: 'Plus Jakarta Sans', system-ui, sans-serif;
  
  --shadow-card: 0 12px 28px -4px rgba(0, 0, 0, 0.5);
  --shadow-glow: 0 8px 24px rgba(245, 184, 24, 0.25);
  --shadow-red: 0 8px 24px rgba(224, 40, 60, 0.35);
}}

* {{ box-sizing: border-box; margin: 0; padding: 0; }}
html {{ scroll-behavior: smooth; scroll-padding-top: 130px; }}
body {{
  background: var(--bg);
  color: var(--ink);
  font-family: var(--body);
  font-size: 15px;
  line-height: 1.5;
  -webkit-font-smoothing: antialiased;
  overflow-x: hidden;
  padding-bottom: 90px;
}}

button {{ font: inherit; color: inherit; cursor: pointer; border: none; background: none; }}
a {{ color: inherit; text-decoration: none; }}
:focus-visible {{ outline: 2px solid var(--gold); outline-offset: 2px; }}

/* Moving Announcement Marquee */
.ribbon {{
  background: linear-gradient(90deg, #870e1c 0%, #d31e33 50%, #870e1c 100%);
  color: #fff;
  font-size: 13px;
  font-weight: 600;
  padding: 7px 0;
  overflow: hidden;
  white-space: nowrap;
  box-shadow: 0 2px 10px rgba(0,0,0,0.35);
  position: relative;
  display: flex;
}}
.marquee-track {{
  display: inline-flex;
  gap: 36px;
  align-items: center;
  white-space: nowrap;
  animation: marqueeScroll 26s linear infinite;
  will-change: transform;
}}
.marquee-track:hover {{
  animation-play-state: paused;
}}
@keyframes marqueeScroll {{
  0% {{ transform: translateX(0); }}
  100% {{ transform: translateX(-50%); }}
}}
.ribbon-item {{
  display: inline-flex;
  align-items: center;
  gap: 9px;
}}
.ribbon-badge {{
  background: #fff;
  color: var(--red);
  padding: 2px 8px;
  border-radius: 4px;
  font-size: 11px;
  text-transform: uppercase;
  font-weight: 800;
  letter-spacing: 0.5px;
}}
.ribbon-sep {{
  color: var(--gold);
  font-size: 14px;
  opacity: 0.9;
}}

/* Sticky Header */
header.top {{
  position: sticky;
  top: 0;
  z-index: 40;
  background: rgba(18, 19, 22, 0.94);
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  border-bottom: 1px solid var(--line);
}}
.bar {{
  max-width: 1180px;
  margin: auto;
  padding: 10px 16px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
}}
.logo-wrap {{
  display: flex;
  align-items: center;
  gap: 10px;
  cursor: pointer;
  user-select: none;
  transition: transform 0.2s cubic-bezier(0.2, 0.8, 0.2, 1);
}}
.logo-wrap:hover {{
  transform: scale(1.05);
}}
.logo-wrap:active {{
  transform: scale(0.96);
}}
.logo-wrap img.mark {{
  height: 48px;
  width: auto;
  display: block;
  filter: drop-shadow(0 4px 12px rgba(245, 184, 24, 0.2));
}}

.status {{
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 13px;
  color: var(--mute);
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: 999px;
  padding: 6px 14px;
  white-space: nowrap;
  flex-shrink: 0;
}}
.dot {{
  width: 9px;
  height: 9px;
  border-radius: 50%;
  background: var(--green-online);
  animation: pulse-online 1.8s infinite;
}}
.dot.closed {{
  background: var(--red);
  animation: none;
}}
@keyframes pulse-online {{
  0% {{ box-shadow: 0 0 0 0 rgba(61,220,132,0.6); }}
  70% {{ box-shadow: 0 0 0 9px rgba(61,220,132,0); }}
  100% {{ box-shadow: 0 0 0 0 rgba(61,220,132,0); }}
}}

.cartbtn {{
  position: relative;
  background: var(--gold);
  color: #121316;
  border-radius: 999px;
  padding: 9px 18px;
  font-weight: 700;
  font-size: 14px;
  display: flex;
  align-items: center;
  gap: 8px;
  box-shadow: var(--shadow-glow);
  transition: all 0.2s ease;
}}
.cartbtn:hover {{ background: var(--gold2); transform: translateY(-1px); }}
.cartbtn i {{
  font-style: normal;
  background: var(--red);
  color: #fff;
  border-radius: 999px;
  min-width: 22px;
  height: 22px;
  display: none;
  place-items: center;
  font-size: 11.5px;
  font-weight: 800;
  padding: 0 5px;
}}
.cartbtn i.on {{ display: grid; }}

/* Horizontal Chips Navigation */
.chips {{
  max-width: 1180px;
  margin: auto;
  padding: 4px 16px 10px;
  display: flex;
  gap: 8px;
  overflow-x: auto;
  scrollbar-width: none;
  -webkit-overflow-scrolling: touch;
}}
.chips::-webkit-scrollbar {{ display: none; }}
.chip {{
  flex: none;
  border: 1.5px solid var(--line);
  background: var(--panel);
  color: var(--mute);
  border-radius: 999px;
  padding: 7px 16px;
  font-weight: 600;
  font-size: 13.5px;
  transition: all 0.2s ease;
  display: flex;
  align-items: center;
  gap: 6px;
}}
.chip.on, .chip:hover {{
  background: var(--gold);
  border-color: var(--gold);
  color: #121316;
  font-weight: 700;
  box-shadow: 0 4px 14px rgba(245, 184, 24, 0.35);
}}

/* Hero Section - Luxury Dark Gourmet Atmosphere */
.hero {{
  position: relative;
  overflow: hidden;
  border-bottom: 1px solid var(--line);
  background:
    radial-gradient(900px 520px at 80% 40%, rgba(180, 20, 35, 0.12), transparent 70%),
    radial-gradient(650px 420px at 15% 30%, rgba(245, 184, 24, 0.05), transparent 60%),
    linear-gradient(180deg, #121317 0%, #0a0b0e 100%);
  padding: 46px 16px 56px;
}}
.hero::before {{
  content: "";
  position: absolute;
  right: -5%;
  top: -25%;
  width: 55%;
  height: 160%;
  background: radial-gradient(ellipse at center, rgba(180, 20, 35, 0.08) 0%, transparent 70%);
  pointer-events: none;
  filter: blur(60px);
}}
.hero-in {{
  position: relative;
  z-index: 2;
  max-width: 1180px;
  margin: auto;
  display: grid;
  grid-template-columns: 1.08fr .92fr;
  gap: 32px;
  align-items: center;
}}

/* Eyebrow badge with slide-in animation */
.hero-badge {{
  display: inline-flex;
  align-items: center;
  gap: 8px;
  background: rgba(245, 184, 24, 0.1);
  border: 1px solid rgba(245, 184, 24, 0.35);
  border-radius: 999px;
  padding: 6px 15px;
  font-size: 12px;
  font-weight: 700;
  letter-spacing: 0.8px;
  text-transform: uppercase;
  color: var(--gold2);
  margin-bottom: 16px;
  backdrop-filter: blur(8px);
  box-shadow: 0 4px 14px rgba(245, 184, 24, 0.12);
  animation: heroFadeDown 0.75s cubic-bezier(0.16, 1, 0.3, 1) both 0.1s;
}}
.hero-badge .badge-dot {{
  width: 7px;
  height: 7px;
  border-radius: 50%;
  background: var(--gold);
  box-shadow: 0 0 8px var(--gold);
}}
.hero-badge .badge-sep {{
  opacity: 0.4;
}}

.hero .logo {{
  width: min(370px, 85%);
  display: block;
  filter: drop-shadow(0 14px 28px rgba(0,0,0,0.7)) drop-shadow(0 2px 10px rgba(245, 184, 24, 0.22));
  margin-bottom: 14px;
  animation: heroScaleIn 0.85s cubic-bezier(0.16, 1, 0.3, 1) both 0.2s;
}}

/* Headline with slide-up entrance */
.hero-headline {{
  font-family: var(--display);
  font-size: clamp(30px, 4.2vw, 44px);
  font-weight: 800;
  font-style: italic;
  line-height: 1.1;
  letter-spacing: 0.5px;
  color: #ffffff;
  margin-bottom: 14px;
  text-transform: uppercase;
  animation: heroSlideUp 0.85s cubic-bezier(0.16, 1, 0.3, 1) both 0.35s;
}}

/* Dynamic animated metallic gold shimmer light-sweep */
.gold-shimmer {{
  background: linear-gradient(
    105deg,
    #f5b818 0%,
    #ffd04d 20%,
    #ffffff 45%,
    #ffd04d 70%,
    #f5b818 100%
  );
  background-size: 250% auto;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  display: inline-block;
  animation: gold-sweep 3.5s ease-in-out infinite;
}}
@keyframes gold-sweep {{
  0% {{ background-position: -200% center; }}
  100% {{ background-position: 200% center; }}
}}

.hero p.lead {{
  margin: 0 0 16px;
  max-width: 48ch;
  font-size: 16.5px;
  color: #d1d5de;
  line-height: 1.6;
  animation: heroSlideUp 0.85s cubic-bezier(0.16, 1, 0.3, 1) both 0.5s;
}}
.hero p.lead strong {{
  color: #fff;
  font-weight: 700;
}}

/* Social proof / Rating bar */
.hero-trust {{
  display: flex;
  align-items: center;
  gap: 10px;
  font-size: 13px;
  color: var(--mute);
  margin-bottom: 22px;
  animation: heroSlideUp 0.85s cubic-bezier(0.16, 1, 0.3, 1) both 0.65s;
}}
.hero-trust .stars {{
  color: var(--gold);
  letter-spacing: 2px;
  font-size: 13.5px;
}}
.hero-trust b {{
  color: #fff;
}}
.hero-trust .trust-sep {{
  opacity: 0.3;
}}

.cta-group {{
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
  margin-bottom: 24px;
  animation: heroSlideUp 0.85s cubic-bezier(0.16, 1, 0.3, 1) both 0.78s;
}}
.cta {{
  display: inline-flex;
  align-items: center;
  gap: 9px;
  background: linear-gradient(135deg, #ffd04d 0%, #f5b818 55%, #df9400 100%);
  color: #0c0d10;
  border-radius: 12px;
  padding: 13px 26px;
  font-weight: 800;
  font-size: 15.5px;
  letter-spacing: 0.2px;
  box-shadow: 0 10px 26px rgba(245, 184, 24, 0.35), inset 0 1px 0 rgba(255,255,255,0.4);
  transition: all 0.25s cubic-bezier(0.2, 0.8, 0.2, 1);
  position: relative;
  overflow: hidden;
}}
.cta::after {{
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  width: 45%;
  height: 100%;
  background: linear-gradient(90deg, transparent, rgba(255,255,255,0.4), transparent);
  transform: translateX(-150%) skewX(-20deg);
  animation: cta-beam 4.5s ease-in-out infinite;
}}
@keyframes cta-beam {{
  0% {{ transform: translateX(-150%) skewX(-20deg); }}
  30%, 100% {{ transform: translateX(280%) skewX(-20deg); }}
}}
.cta:hover {{
  transform: translateY(-2px);
  box-shadow: 0 14px 34px rgba(245, 184, 24, 0.52);
  filter: brightness(1.04);
}}
.cta.sec {{
  background: rgba(255, 255, 255, 0.05);
  color: #ffffff;
  border: 1.5px solid rgba(255, 255, 255, 0.18);
  backdrop-filter: blur(10px);
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.3);
}}
.cta.sec:hover {{
  background: rgba(255, 255, 255, 0.12);
  border-color: rgba(245, 184, 24, 0.45);
  transform: translateY(-2px);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.45);
}}

/* Hero Facts Cards */
.facts {{
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 10px;
  max-width: 520px;
}}
.fact-card {{
  background: rgba(23, 24, 30, 0.7);
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 12px;
  padding: 8px 12px;
  display: flex;
  align-items: center;
  gap: 10px;
  backdrop-filter: blur(10px);
  transition: all 0.2s ease;
  animation: heroSlideUp 0.75s cubic-bezier(0.16, 1, 0.3, 1) both;
}}
.fact-card:nth-child(1) {{ animation-delay: 0.9s; }}
.fact-card:nth-child(2) {{ animation-delay: 1.0s; }}
.fact-card:nth-child(3) {{ animation-delay: 1.1s; }}
.fact-card:nth-child(4) {{ animation-delay: 1.2s; }}
.fact-card:hover {{
  border-color: rgba(245, 184, 24, 0.35);
  background: rgba(30, 31, 38, 0.85);
  transform: translateY(-1px);
}}
.fact-icon {{
  font-size: 19px;
  line-height: 1;
}}
.fact-text {{
  display: flex;
  flex-direction: column;
  line-height: 1.25;
}}
.fact-text strong {{
  font-size: 13px;
  color: #ffffff;
  font-weight: 700;
}}
.fact-text small {{
  font-size: 11px;
  color: var(--mute);
}}

/* 3D Floating Food Stage - Luxury Studio Showcase */
.stage {{
  position: relative;
  min-height: 440px;
  display: flex;
  align-items: center;
  justify-content: center;
  animation: stageFadeIn 1s cubic-bezier(0.16, 1, 0.3, 1) both 0.3s;
}}

/* Soft diffused ambient backlight - NO muddy brown! */
.stage-glow {{
  position: absolute;
  width: 440px;
  height: 440px;
  border-radius: 50%;
  background: radial-gradient(circle at 50% 45%, rgba(224, 40, 60, 0.14) 0%, rgba(255, 180, 30, 0.06) 40%, transparent 68%);
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  filter: blur(45px);
  pointer-events: none;
  z-index: 0;
}}

/* Dark Obsidian Pedestal Disc */
.stage-disc {{
  position: absolute;
  width: 370px;
  height: 370px;
  border-radius: 50%;
  background: radial-gradient(circle at 50% 35%, rgba(26, 27, 34, 0.95) 0%, rgba(13, 14, 18, 0.9) 65%, rgba(10, 11, 14, 0.2) 100%);
  border: 1px solid rgba(255, 255, 255, 0.08);
  box-shadow:
    0 24px 60px rgba(0, 0, 0, 0.8),
    inset 0 1px 2px rgba(255, 255, 255, 0.12),
    inset 0 -18px 36px rgba(0, 0, 0, 0.7);
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  z-index: 1;
  pointer-events: none;
}}

/* Elegant slow-spinning golden outer ring */
.stage-ring-outer {{
  position: absolute;
  width: 430px;
  height: 430px;
  border-radius: 50%;
  border: 1px dashed rgba(245, 184, 24, 0.22);
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  z-index: 1;
  animation: spinRing 55s linear infinite;
  pointer-events: none;
}}
@keyframes spinRing {{
  100% {{ transform: translate(-50%, -50%) rotate(360deg); }}
}}

/* Inner crisp accent circle */
.stage-ring-inner {{
  position: absolute;
  width: 310px;
  height: 310px;
  border-radius: 50%;
  border: 1px solid rgba(245, 184, 24, 0.12);
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  z-index: 1;
  pointer-events: none;
}}

.stage-pedestal {{
  position: absolute;
  width: 340px;
  height: 70px;
  border-radius: 50%;
  background: radial-gradient(ellipse at center, rgba(0, 0, 0, 0.9) 0%, transparent 72%);
  bottom: 4%;
  left: 50%;
  transform: translateX(-50%);
  z-index: 1;
  pointer-events: none;
}}
.stage img {{
  position: absolute;
  filter: drop-shadow(0 20px 28px rgba(0,0,0,0.65));
  transition: transform 0.35s ease;
}}
.stage .s-duo {{
  width: 190px;
  left: 0;
  top: 6%;
  z-index: 2;
  animation: float-duo 6s ease-in-out infinite;
}}
.stage .s-main {{
  width: 205px;
  right: 5%;
  top: 8%;
  z-index: 3;
  animation: float-main 5s ease-in-out infinite;
}}
.stage .s-pizza {{
  width: 260px;
  left: 5%;
  bottom: 2%;
  z-index: 2;
  animation: float-pizza 7s ease-in-out infinite;
}}

@keyframes float-main {{
  0%, 100% {{ transform: translateY(0) rotate(0deg); }}
  50% {{ transform: translateY(-13px) rotate(1deg); }}
}}
@keyframes float-duo {{
  0%, 100% {{ transform: translateY(0) rotate(0deg); }}
  50% {{ transform: translateY(-10px) rotate(-1.5deg); }}
}}
@keyframes float-pizza {{
  0%, 100% {{ transform: translateY(0); }}
  50% {{ transform: translateY(-8px); }}
}}

/* Luxury Deal Sticker with Pulse */
.sticker {{
  position: absolute;
  right: 2%;
  bottom: 8%;
  z-index: 4;
  background: linear-gradient(135deg, #e0283c 0%, #a81525 100%);
  border: 2px solid rgba(255, 215, 0, 0.85);
  color: #fff;
  border-radius: 16px;
  padding: 10px 16px;
  transform: rotate(-5deg);
  text-align: left;
  box-shadow: 0 14px 32px rgba(224, 40, 60, 0.45), inset 0 1px 0 rgba(255,255,255,0.3);
  cursor: pointer;
  transition: all 0.25s cubic-bezier(0.175, 0.885, 0.32, 1.275);
  animation: sticker-attract 3.8s ease-in-out infinite;
}}
@keyframes sticker-attract {{
  0%, 100% {{
    transform: rotate(-5deg) scale(1);
    box-shadow: 0 14px 32px rgba(224, 40, 60, 0.45), inset 0 1px 0 rgba(255,255,255,0.3);
  }}
  50% {{
    transform: rotate(-3deg) scale(1.05);
    box-shadow: 0 18px 38px rgba(224, 40, 60, 0.65), 0 0 22px rgba(245, 184, 24, 0.45), inset 0 1px 0 rgba(255,255,255,0.5);
  }}
}}
.sticker:hover {{
  transform: rotate(-2deg) scale(1.08) !important;
  box-shadow: 0 20px 42px rgba(224, 40, 60, 0.75), 0 0 25px rgba(245, 184, 24, 0.6);
}}
.sticker .badge-sub {{
  display: block;
  font-size: 11px;
  letter-spacing: 0.6px;
  text-transform: uppercase;
  color: var(--gold2);
  font-weight: 800;
  margin-bottom: 2px;
}}
.sticker strong {{
  display: block;
  font-family: var(--display);
  font-weight: 800;
  font-style: italic;
  font-size: 34px;
  line-height: 1;
  color: #fff;
  text-shadow: 0 2px 6px rgba(0,0,0,0.4);
}}
.sticker .badge-title {{
  display: block;
  font-size: 13px;
  font-weight: 700;
  color: #fff;
  opacity: 0.95;
}}
.sticker em {{
  font-style: normal;
  font-size: 11.5px;
  background: var(--gold);
  color: #121316;
  border-radius: 6px;
  padding: 3px 8px;
  font-weight: 800;
  display: inline-block;
  margin-top: 6px;
  text-transform: uppercase;
  letter-spacing: 0.3px;
  box-shadow: 0 2px 6px rgba(0,0,0,0.25);
}}

/* Animation Keyframes */
@keyframes heroFadeDown {{
  from {{ opacity: 0; transform: translateY(-18px); }}
  to {{ opacity: 1; transform: translateY(0); }}
}}
@keyframes heroScaleIn {{
  from {{ opacity: 0; transform: scale(0.9) translateY(12px); }}
  to {{ opacity: 1; transform: scale(1) translateY(0); }}
}}
@keyframes heroSlideUp {{
  from {{ opacity: 0; transform: translateY(24px); }}
  to {{ opacity: 1; transform: translateY(0); }}
}}
@keyframes stageFadeIn {{
  from {{ opacity: 0; transform: translateX(40px) scale(0.95); }}
  to {{ opacity: 1; transform: translateX(0) scale(1); }}
}}

/* How It Works Section */
.how {{
  max-width: 1180px;
  margin: -14px auto 26px;
  padding: 0 16px;
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 14px;
  position: relative;
  z-index: 5;
}}
.step {{
  display: flex;
  gap: 14px;
  align-items: center;
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: 16px;
  padding: 14px 18px;
  box-shadow: 0 6px 18px rgba(0,0,0,0.3);
  transition: transform 0.2s ease, border-color 0.2s ease;
}}
.step:hover {{
  transform: translateY(-2px);
  border-color: var(--line-gold);
}}
.step b {{
  font-family: var(--display);
  font-style: italic;
  font-weight: 800;
  font-size: 38px;
  line-height: 1;
  color: var(--gold);
  min-width: 26px;
}}
.step span {{ font-size: 13.5px; color: var(--mute); line-height: 1.35; }}
.step strong {{ display: block; font-weight: 700; color: #fff; font-size: 15px; margin-bottom: 2px; }}

/* Main Menu Container */
main#menu {{
  max-width: 1180px;
  margin: auto;
  padding: 0 16px 100px;
}}
section.cat {{
  padding-top: 48px;
}}
.cathead {{
  display: flex;
  align-items: flex-end;
  justify-content: space-between;
  gap: 16px;
  border-bottom: 3px solid var(--gold);
  padding-bottom: 12px;
  margin-bottom: 10px;
}}
.cathead h2 {{
  font-family: var(--display);
  font-style: italic;
  font-weight: 800;
  font-size: clamp(38px, 6vw, 56px);
  line-height: .95;
  text-transform: uppercase;
}}
.cathead h2 small {{
  display: block;
  font-family: var(--body);
  font-style: normal;
  font-weight: 500;
  font-size: 14px;
  color: var(--mute);
  margin-top: 6px;
  text-transform: none;
}}
.cathead img {{
  height: 84px;
  width: auto;
  margin-bottom: -4px;
  filter: drop-shadow(0 8px 14px rgba(0,0,0,.6));
}}
h3.grp {{
  font-family: var(--display);
  font-weight: 800;
  font-size: 26px;
  color: var(--gold);
  margin: 28px 0 8px;
  display: flex;
  align-items: center;
  gap: 12px;
  text-transform: uppercase;
}}
h3.grp::after {{
  content: "";
  flex: 1;
  height: 1px;
  background: var(--line);
}}
.grid {{
  display: grid;
  gap: 16px;
  margin-top: 14px;
}}
.grid.deals {{ grid-template-columns: repeat(auto-fill, minmax(260px, 1fr)); }}
.grid.items {{ grid-template-columns: repeat(auto-fill, minmax(310px, 1fr)); }}

/* Deal Card */
.dcard {{
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: 18px;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  transition: transform .25s ease, border-color .25s ease, box-shadow .25s ease;
}}
.dcard:hover {{
  transform: translateY(-5px);
  border-color: var(--gold);
  box-shadow: 0 14px 30px rgba(0,0,0,0.5), 0 0 16px rgba(245, 184, 24, 0.2);
}}
.dcard .ph {{
  height: 164px;
  display: grid;
  place-items: center;
  background: radial-gradient(circle at 50% 55%, rgba(245,184,24,.25), transparent 65%), var(--panel2);
  position: relative;
  overflow: hidden;
}}
.dcard .ph img {{
  max-height: 130px;
  max-width: 88%;
  width: auto;
  filter: drop-shadow(0 10px 14px rgba(0,0,0,.65));
  transition: transform 0.4s ease;
}}
.dcard:hover .ph img {{ transform: scale(1.07); }}
.dcard .tag {{
  position: absolute;
  left: 12px;
  top: 12px;
  background: var(--red);
  color: #fff;
  border-radius: 6px;
  padding: 3px 10px;
  font-size: 11.5px;
  font-weight: 700;
  text-transform: uppercase;
}}
.dcard .bd {{
  padding: 16px;
  display: flex;
  flex-direction: column;
  gap: 6px;
  flex: 1;
}}
.dcard h4 {{
  font-family: var(--display);
  font-weight: 800;
  font-style: italic;
  font-size: 26px;
  line-height: 1.05;
}}
.dcard p {{
  color: var(--mute);
  font-size: 13.5px;
  line-height: 1.4;
  flex: 1;
}}
.dcard .row {{
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 8px;
  margin-top: 12px;
  padding-top: 10px;
  border-top: 1px dashed var(--line);
}}
.price {{
  font-family: var(--display);
  font-weight: 800;
  font-size: 28px;
  line-height: 1;
  color: var(--gold);
}}
.price small {{
  font-size: 16px;
  font-weight: 600;
  margin-right: 3px;
}}
.add {{
  border: 0;
  background: var(--gold);
  color: #121316;
  font-weight: 700;
  border-radius: 10px;
  padding: 9px 16px;
  white-space: nowrap;
  font-size: 14px;
  transition: all 0.2s ease;
}}
.add:hover {{ background: var(--gold2); transform: scale(1.04); }}
.add.ok, .opt.ok {{
  background: var(--green-online) !important;
  border-color: var(--green-online) !important;
  color: #0b2b16 !important;
}}

/* Item Card */
.icard {{
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: 16px;
  padding: 16px;
  display: flex;
  flex-direction: column;
  gap: 8px;
  transition: transform .2s ease, border-color .2s ease;
}}
.icard:hover {{
  border-color: var(--line-gold);
  transform: translateY(-2px);
}}
.icard .top {{
  display: flex;
  gap: 12px;
  align-items: flex-start;
}}
.icard .txt {{ flex: 1; }}
.icard h4 {{
  font-size: 17px;
  font-weight: 700;
  line-height: 1.25;
  color: #fff;
}}
.icard p {{
  color: var(--mute);
  font-size: 13px;
  line-height: 1.4;
  margin-top: 3px;
}}
.icard .th {{
  width: 72px;
  height: 60px;
  display: grid;
  place-items: center;
  flex: none;
  background: radial-gradient(circle, rgba(245,184,24,.2), transparent 70%);
  border-radius: 8px;
}}
.icard .th img {{
  max-width: 100%;
  max-height: 100%;
  filter: drop-shadow(0 4px 8px rgba(0,0,0,0.4));
}}
.opts {{
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-top: 8px;
}}
.opt {{
  border: 1.5px solid var(--gold);
  background: rgba(245, 184, 24, 0.05);
  color: var(--gold);
  border-radius: 8px;
  padding: 6px 12px;
  font-weight: 700;
  font-size: 13.5px;
  transition: all 0.2s ease;
}}
.opt:hover {{
  background: var(--gold);
  color: #121316;
  transform: scale(1.04);
}}
.note {{
  margin-top: 14px;
  color: var(--mute);
  font-size: 13.5px;
  background: var(--panel2);
  border: 1px dashed var(--line-gold);
  border-radius: 10px;
  padding: 9px 14px;
  display: inline-block;
}}

/* Footer */
footer {{
  background: #0f1012;
  border-top: 3px solid var(--gold);
  padding: 44px 16px 120px;
  text-align: center;
  color: var(--mute);
  font-size: 14.5px;
}}
footer img {{
  height: 74px;
  margin-bottom: 14px;
  filter: drop-shadow(0 6px 16px rgba(245,184,24,0.25));
}}
footer p {{ margin-top: 4px; line-height: 1.6; }}
footer a.cta {{ margin-top: 18px; }}

/* Floating Action Button (FAB) - Vibrant Liquid Gold */
.fab {{
  position: fixed;
  left: 50%;
  bottom: calc(20px + env(safe-area-inset-bottom, 0px));
  transform: translateX(-50%);
  z-index: 50;
  background: linear-gradient(135deg, #ffd04d 0%, #f5b818 55%, #df9400 100%);
  color: #0c0d10;
  border-radius: 999px;
  padding: 12px 26px;
  font-weight: 800;
  font-size: 15px;
  letter-spacing: 0.2px;
  box-shadow: 0 14px 36px rgba(245, 184, 24, 0.48), 0 0 0 2px rgba(255, 255, 255, 0.35);
  display: none; /* hidden completely when empty! */
  gap: 12px;
  align-items: center;
  cursor: pointer;
  white-space: nowrap;
  transition: all 0.25s cubic-bezier(0.2, 0.8, 0.2, 1);
}}
.fab:hover {{
  transform: translateX(-50%) translateY(-2px);
  box-shadow: 0 18px 42px rgba(245, 184, 24, 0.65);
}}
.fab.show {{
  display: flex !important;
  animation: fabBounceIn 0.35s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}}
@keyframes fabBounceIn {{
  from {{ transform: translateX(-50%) translateY(100px); opacity: 0; }}
  to {{ transform: translateX(-50%) translateY(0); opacity: 1; }}
}}
.fab-badge {{
  background: rgba(0, 0, 0, 0.22);
  color: #0c0d10;
  padding: 3px 12px;
  border-radius: 999px;
  font-size: 13px;
  font-weight: 800;
}}

/* Cart Drawer */
.drawer {{
  position: fixed;
  inset: 0;
  z-index: 100;
  display: none;
}}
.drawer.open {{ display: block; }}
.drawer .back {{
  position: absolute;
  inset: 0;
  background: rgba(0,0,0,.7);
  backdrop-filter: blur(4px);
}}
.sheet {{
  position: absolute;
  right: 0;
  top: 0;
  bottom: 0;
  width: min(460px, 100%);
  background: #141518;
  display: flex;
  flex-direction: column;
  box-shadow: -12px 0 40px rgba(0,0,0,0.7);
  animation: slideDrawer 0.28s ease-out;
  overflow: hidden;
}}
@keyframes slideDrawer {{
  from {{ transform: translateX(100%); }}
  to {{ transform: translateX(0); }}
}}
.sheet header {{
  flex-shrink: 0;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 16px 20px;
  border-bottom: 1px solid var(--line);
  background: #141518;
  z-index: 2;
}}
.sheet header h2 {{
  font-family: var(--display);
  font-size: 30px;
  font-weight: 800;
  font-style: italic;
  line-height: 1;
}}
.x {{
  background: none;
  border: 0;
  font-size: 32px;
  line-height: 1;
  color: var(--mute);
  padding: 4px;
  cursor: pointer;
}}
.x:hover {{ color: #fff; }}

.sheet-body {{
  flex: 1;
  overflow-y: auto;
  overscroll-behavior: contain;
  -webkit-overflow-scrolling: touch;
  display: flex;
  flex-direction: column;
  background: #141518;
}}
.lines {{
  flex: 1;
  min-height: 70px;
  padding: 10px 20px;
}}
.line {{
  display: flex;
  gap: 12px;
  align-items: center;
  padding: 12px 0;
  border-bottom: 1px solid var(--line);
}}
.line div:first-child {{ flex: 1; }}
.line strong {{ display: block; color: #fff; font-size: 15px; }}
.line small {{ color: var(--gold); font-weight: 600; font-size: 13px; }}
.qty {{
  display: flex;
  align-items: center;
  gap: 8px;
  background: var(--panel2);
  border: 1px solid var(--line);
  border-radius: 8px;
  padding: 2px 6px;
}}
.qty button {{
  width: 28px;
  height: 28px;
  border-radius: 6px;
  background: none;
  font-size: 17px;
  font-weight: 700;
  color: #fff;
}}
.qty span {{
  font-size: 14px;
  font-weight: 700;
  min-width: 18px;
  text-align: center;
}}
.empty-state-box {{
  padding: 50px 20px;
  text-align: center;
  color: var(--mute);
}}
.empty-state-box .empty-icon {{
  font-size: 50px;
  margin-bottom: 12px;
}}
.empty-state-box h3 {{
  color: #fff;
  font-size: 18px;
  margin-bottom: 6px;
}}
.empty-state-box p {{
  font-size: 13.5px;
  color: var(--mute);
  margin-bottom: 18px;
}}
.btn-browse {{
  background: var(--gold);
  color: #121316;
  font-weight: 700;
  padding: 10px 22px;
  border-radius: 10px;
  font-size: 14px;
  display: inline-block;
}}
.btn-browse:hover {{ background: var(--gold2); }}

.foot {{
  margin-top: auto;
  padding: 16px 20px 24px;
  border-top: 1px solid var(--line);
  background: #141518;
  display: grid;
  gap: 10px;
}}
.input-row {{
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 8px;
}}
@media(max-width: 480px) {{
  .input-row {{ grid-template-columns: 1fr; }}
}}
.foot.hide-checkout {{
  display: none !important;
}}
.foot input, .foot textarea {{
  width: 100%;
  background: var(--bg);
  border: 1.5px solid var(--line);
  border-radius: 8px;
  color: var(--ink);
  padding: 11px 13px;
  font: inherit;
  font-size: 14px;
}}
.foot input:focus, .foot textarea:focus {{
  border-color: var(--gold);
  outline: none;
}}
.total {{
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-weight: 700;
  font-size: 18px;
}}
.total span:last-child {{
  font-family: var(--display);
  font-size: 28px;
  color: var(--gold);
  font-weight: 800;
}}

/* Payment Selection Grid */
.pay-title {{
  font-size: 12px;
  font-weight: 700;
  color: var(--mute);
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin-top: 2px;
}}
.pay-grid {{
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 8px;
}}
.pay-btn {{
  background: var(--bg);
  border: 1.5px solid var(--line);
  color: var(--mute);
  font-weight: 700;
  font-size: 13px;
  padding: 9px 8px;
  border-radius: 8px;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 3px;
  cursor: pointer;
  transition: all 0.2s ease;
}}
.pay-btn.active {{
  border-color: var(--gold);
  background: rgba(245, 184, 24, 0.08);
  color: #fff;
}}
.pay-btn.active.ep-active {{
  border-color: var(--green-online);
  background: rgba(61, 220, 132, 0.1);
  color: #fff;
}}

/* Easypaisa Box */
.ep-box {{
  display: none;
  background: linear-gradient(135deg, #0e291a 0%, #06180d 100%);
  border: 1.5px solid #1f6b3e;
  border-radius: 10px;
  padding: 11px 13px;
  animation: fadeIn 0.25s ease;
}}
.ep-box.show {{ display: block; }}
@keyframes fadeIn {{
  from {{ opacity: 0; transform: translateY(-4px); }}
  to {{ opacity: 1; transform: translateY(0); }}
}}
.ep-top-row {{
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 5px;
}}
.ep-tag {{
  background: #22c55e;
  color: #04200d;
  font-size: 11px;
  font-weight: 800;
  padding: 2px 7px;
  border-radius: 4px;
  text-transform: uppercase;
}}
.ep-acct {{ font-size: 12px; color: #a7f3d0; }}
.ep-dial-row {{
  display: flex;
  align-items: center;
  justify-content: space-between;
  background: #041009;
  border: 1px dashed #22c55e;
  border-radius: 6px;
  padding: 6px 12px;
  margin: 5px 0;
}}
.ep-val {{
  font-family: var(--display);
  font-size: 22px;
  font-weight: 800;
  color: var(--green-online);
  letter-spacing: 1px;
}}
.ep-copy {{
  background: #22c55e;
  color: #04190c;
  font-weight: 700;
  font-size: 12px;
  padding: 4px 10px;
  border-radius: 4px;
  cursor: pointer;
}}
.ep-note {{
  font-size: 11.5px;
  color: #a7f3d0;
  line-height: 1.35;
}}
.ep-amount-row {{
  display: flex;
  align-items: center;
  justify-content: space-between;
  font-size: 12.5px;
  color: #a7f3d0;
  margin: 6px 0 10px;
  padding: 5px 0;
  border-bottom: 1px dashed rgba(34, 197, 94, 0.3);
}}
.ep-amount-row strong {{
  font-family: var(--display);
  font-size: 20px;
  color: #3ddc84;
  font-weight: 800;
}}
.ep-status-tabs {{
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 6px;
  margin: 8px 0;
}}
.ep-status-btn {{
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(34, 197, 94, 0.3);
  color: #a7f3d0;
  border-radius: 6px;
  padding: 7px 6px;
  font-size: 11px;
  font-weight: 600;
  cursor: pointer;
  text-align: center;
  transition: all 0.2s ease;
  line-height: 1.3;
}}
.ep-status-btn.active {{
  background: #22c55e;
  border-color: #22c55e;
  color: #04190c;
  font-weight: 800;
  box-shadow: 0 2px 8px rgba(34, 197, 94, 0.3);
}}
.ep-input {{
  width: 100%;
  background: #031208 !important;
  border: 1px solid #1f6b3e !important;
  border-radius: 6px !important;
  color: #fff !important;
  padding: 8px 10px !important;
  font-size: 12.5px !important;
  margin-top: 8px;
}}
.ep-input:focus {{
  border-color: #3ddc84 !important;
  outline: none;
}}

.ep-hint {{
  font-size: 11.5px;
  color: #a7f3d0;
  background: rgba(34, 197, 94, 0.08);
  border-left: 3px solid #22c55e;
  padding: 6px 9px;
  border-radius: 4px;
  margin-top: 6px;
  line-height: 1.35;
}}

.send {{
  background: #25d366;
  color: #062410;
  border: 0;
  border-radius: 10px;
  padding: 14px;
  font-weight: 700;
  font-size: 16px;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  transition: all 0.2s ease;
  box-shadow: 0 4px 16px rgba(37, 211, 102, 0.3);
}}
.send:hover {{ background: #22c55e; }}
.send:disabled {{ opacity: .45; cursor: not-allowed; box-shadow: none; }}
.tiny {{ font-size: 12px; color: var(--dim); text-align: center; }}

@media(max-width:860px){{
  .hero-in {{ grid-template-columns: 1fr; padding-top: 18px; gap: 24px; }}
  .hero::before {{ width: 80%; right: -20%; opacity: .15; }}
  .facts {{ grid-template-columns: 1fr; max-width: 100%; }}
  .stage {{ min-height: 380px; }}
  .stage-disc {{ width: 290px; height: 290px; }}
  .stage-ring-outer {{ width: 330px; height: 330px; }}
  .stage-ring-inner {{ width: 240px; height: 240px; }}
  .stage-glow {{ width: 320px; height: 320px; }}
  .stage .s-duo {{ width: 140px; left: 0; }}
  .stage .s-main {{ width: 155px; right: 2%; }}
  .stage .s-pizza {{ width: 230px; left: 2%; }}
  .how {{ grid-template-columns: 1fr; }}
  .bar img.mark {{ height: 42px; }}
  .cathead img {{ height: 60px; }}
}}

@media(max-width: 580px){{
  .bar {{
    padding: 8px 12px;
    gap: 8px;
  }}
  .logo-wrap img.mark {{
    height: 38px;
  }}
  .status {{
    font-size: 11.5px;
    padding: 5px 10px;
    gap: 5px;
  }}
  .status .hours-text {{
    display: none !important;
  }}
  .cartbtn {{
    padding: 7px 13px;
    font-size: 13px;
    gap: 6px;
  }}
  .cartbtn i {{
    width: 20px;
    height: 20px;
    font-size: 11px;
    line-height: 20px;
  }}
  .fab {{
    width: calc(100% - 24px);
    max-width: 360px;
    padding: 11px 16px;
    font-size: 14px;
    gap: 8px;
    justify-content: space-between;
    bottom: calc(14px + env(safe-area-inset-bottom, 0px));
  }}
  .fab-badge {{
    padding: 3px 10px;
    font-size: 12px;
  }}
}}

@media(max-width: 480px){{
  .grid.deals {{ grid-template-columns: 1fr; }}
  .grid.items {{ grid-template-columns: 1fr; }}
  .hero-headline {{ font-size: 32px; }}
}}
@media(prefers-reduced-motion:reduce){{
  .dot, .stage .s-main, .stage .s-duo, .stage .s-pizza, .gold-shimmer, .stage-ring-outer, .cta::after, .sticker {{ animation: none; }}
  html {{ scroll-behavior: auto; }}
}}
</style>
</head>
<body>

<div class="ribbon" aria-label="Announcements">
  <div class="marquee-track">
    <div class="ribbon-item">
      <span class="ribbon-badge">Free Delivery</span>
      <span>🛵 Free Home Delivery in Lahore on Orders Above Rs 999! (3:00 PM to 3:00 AM)</span>
    </div>
    <span class="ribbon-sep">✦</span>
    <div class="ribbon-item">
      <span class="ribbon-badge">Hot Deals</span>
      <span>🔥 Craving Zinger, Pizza or Shawarma? 1-Tap Direct WhatsApp Order!</span>
    </div>
    <span class="ribbon-sep">✦</span>
    <div class="ribbon-item">
      <span class="ribbon-badge">Payment</span>
      <span>🟢 Cash on Delivery &amp; Easypaisa Accepted</span>
    </div>
    <span class="ribbon-sep">✦</span>
    <!-- Seamless Loop Duplicate -->
    <div class="ribbon-item">
      <span class="ribbon-badge">Free Delivery</span>
      <span>🛵 Free Home Delivery in Lahore on Orders Above Rs 999! (3:00 PM to 3:00 AM)</span>
    </div>
    <span class="ribbon-sep">✦</span>
    <div class="ribbon-item">
      <span class="ribbon-badge">Hot Deals</span>
      <span>🔥 Craving Zinger, Pizza or Shawarma? 1-Tap Direct WhatsApp Order!</span>
    </div>
    <span class="ribbon-sep">✦</span>
    <div class="ribbon-item">
      <span class="ribbon-badge">Payment</span>
      <span>🟢 Cash on Delivery &amp; Easypaisa Accepted</span>
    </div>
    <span class="ribbon-sep">✦</span>
  </div>
</div>

<header class="top">
  <div class="bar">
    <div class="logo-wrap" onclick="window.scrollTo({{top: 0, behavior: 'smooth'}})" title="Fryzo - Back to top">
      <img class="mark" id="logoTop" alt="Fryzo - Say Yes To Yumm">
    </div>
    <div class="status">
      <i class="dot" id="dot"></i>
      <span id="stat">Checking</span>
      <span class="hours-text" style="opacity:0.6">&bull; 3pm - 3am</span>
    </div>
    <button class="cartbtn" id="cartbtn">
      <span>Order</span>
      <i id="cartN">0</i>
    </button>
  </div>
  <nav class="chips" id="chips" aria-label="Menu categories"></nav>
</header>

<section class="hero">
  <div class="hero-in">
    <div>
      <div class="hero-badge">
        <span class="badge-dot"></span>
        <span>Lahore’s Craved Fast Food</span>
        <span class="badge-sep">•</span>
        <span>Open Till 3 AM</span>
      </div>
      
      <img class="logo" id="logoHero" alt="Fryzo - Say Yes To Yumm" onclick="window.scrollTo({{top: 0, behavior: 'smooth'}})" style="cursor:pointer;" title="Back to top">
      
      <h1 class="hero-headline">
        Say Yes To <span class="gold-shimmer">Unmatched Crunch</span> & Melted Cheese.
      </h1>
      
      <p class="lead">
        Golden crispy Zinger, melting mozzarella artisan pizza, saucy wings aur authentic Arabian shawarma — <strong>garma garam, fresh</strong> aur sirf ek tap mein seedha aap ke darwazay par!
      </p>

      <div class="hero-trust">
        <span class="stars">★★★★★</span>
        <b>4.9 / 5</b>
        <span class="trust-sep">|</span>
        <span>15,000+ Happy Foodies in Lahore</span>
      </div>

      <div class="cta-group">
        <a class="cta" href="#deals">🔥 Explore Deals & Offers</a>
        <a class="cta sec" href="#burgers">📋 Browse Full Menu</a>
      </div>

      <div class="facts">
        <div class="fact-card">
          <span class="fact-icon">🛵</span>
          <div class="fact-text">
            <strong>Free Home Delivery</strong>
            <small>Lahore orders Rs 999+</small>
          </div>
        </div>
        <div class="fact-card">
          <span class="fact-icon">🕒</span>
          <div class="fact-text">
            <strong>3:00 PM – 3:00 AM</strong>
            <small>Late-night cravings sorted</small>
          </div>
        </div>
        <div class="fact-card">
          <span class="fact-icon">💬</span>
          <div class="fact-text">
            <strong>Instant WhatsApp</strong>
            <small>1-Tap direct order receipt</small>
          </div>
        </div>
        <div class="fact-card">
          <span class="fact-icon">🟢</span>
          <div class="fact-text">
            <strong>Easypaisa & COD</strong>
            <small>Cash or 03434096282</small>
          </div>
        </div>
      </div>
    </div>

    <div class="stage" aria-hidden="false">
      <div class="stage-glow"></div>
      <div class="stage-disc"></div>
      <div class="stage-ring-outer"></div>
      <div class="stage-ring-inner"></div>
      <div class="stage-pedestal"></div>
      <img class="s-duo" id="sDuo" alt="Fryzo Duo Box">
      <img class="s-pizza" id="sPizza" alt="Fryzo Platter">
      <img class="s-main" id="sMain" alt="Hunger Box">
      <button class="sticker" id="sticker" aria-label="Add Hunger Box to your order">
        <span class="badge-sub">★ Chef's Special</span>
        <span class="badge-title">Hunger Box Combo</span>
        <strong>Rs 1,280</strong>
        <em>⚡ Tap to add</em>
      </button>
    </div>
  </div>
</section>

<div class="how">
  <div class="step">
    <b>1</b>
    <span><strong>Choose Food</strong>Pick your favorite deals or menu items</span>
  </div>
  <div class="step">
    <b>2</b>
    <span><strong>Select Payment</strong>Pay Cash on Delivery or via Easypaisa</span>
  </div>
  <div class="step">
    <b>3</b>
    <span><strong>Send on WhatsApp</strong>Instant receipt sent &amp; delivered fresh!</span>
  </div>
</div>

<main id="menu"></main>

<footer>
  <img id="logoFoot" alt="Fryzo" onclick="window.scrollTo({{top: 0, behavior: 'smooth'}})" style="cursor:pointer;" title="Back to top">
  <p><strong>Fryzo Lahore</strong> &bull; Shop No 4, Rasheed Plaza, T&amp;T Abpara Housing Society, Raiwind Road, Lahore</p>
  <p>Hotline WhatsApp: <strong>0328-4551176</strong> &bull; Easypaisa: <strong>0343-4096282</strong> &bull; 3:00 PM to 3:00 AM</p>
  <a class="cta" id="waFoot" href="https://wa.me/923284551176" target="_blank" rel="noopener">Message us on WhatsApp</a>
</footer>

<!-- Bottom Floating Cart Button (Hidden by default, shown ONLY when cart > 0) -->
<button class="fab" id="fab" aria-label="Open your order">
  <span class="fab-badge" id="fabN">0 items</span>
  <span id="fabT">Rs 0</span>
  <span>View order &rarr;</span>
</button>

<div class="drawer" id="drawer" role="dialog" aria-modal="true" aria-label="Your order">
  <div class="back" id="back"></div>
  <div class="sheet">
    <header>
      <h2>Your order</h2>
      <button class="x" id="close" aria-label="Close">&times;</button>
    </header>
    <div class="sheet-body" id="sheetBody">
      <div class="lines" id="lines"></div>
      <div class="foot" id="cartFoot">
      <div class="total">
        <span>Grand Total</span>
        <span id="total">Rs 0</span>
      </div>

      <div class="input-row">
        <input id="nm" placeholder="Customer Name (e.g. Areej)" autocomplete="name">
        <input id="ph" type="tel" placeholder="Phone # for Rider (e.g. 0335-1234567)" autocomplete="tel">
      </div>
      <textarea id="ad" rows="2" placeholder="Full Delivery Address (House #, Street, Block/Phase, Society)" autocomplete="street-address"></textarea>
      <input id="lm" placeholder="Nearby Landmark / Instructions (e.g. Near Bilal Masjid, Gate 2)" autocomplete="off">

      <!-- Payment Method Selection -->
      <div class="pay-title">Select Payment Method:</div>
      <div class="pay-grid">
        <button type="button" class="pay-btn active" id="btnPayCod" onclick="setPayMethod('cod')">
          <span>💵</span>
          <span>Cash on Delivery</span>
        </button>
        <button type="button" class="pay-btn" id="btnPayEp" onclick="setPayMethod('easypaisa')">
          <span>🟢</span>
          <span>Easypaisa</span>
        </button>
      </div>

      <!-- Easypaisa Details Box -->
      <div class="ep-box" id="epCard">
        <div class="ep-top-row">
          <span class="ep-tag">Easypaisa Official</span>
          <span class="ep-acct">Account Title: <strong>Fryzo</strong></span>
        </div>
        <div class="ep-dial-row">
          <span class="ep-val" id="epNum">0343-4096282</span>
          <button type="button" class="ep-copy" id="btnCopy" onclick="copyEp()">Copy Number</button>
        </div>
        <div class="ep-amount-row">
          <span>Exact Bill to Transfer:</span>
          <strong id="epBillAmount">Rs 0</strong>
        </div>

        <div class="ep-status-tabs">
          <button type="button" class="ep-status-btn active" id="epTabLater" onclick="setEpStatus('later')">
            🕒 Order Confirm Hone Par Transfer
          </button>
          <button type="button" class="ep-status-btn" id="epTabPaid" onclick="setEpStatus('paid')">
            ✅ Abhi Transfer Kar Diya
          </button>
        </div>

        <div class="ep-hint" id="epHintLater">
          👍 <strong>No Advance Needed:</strong> Pehle order verify karwayen, Fryzo team WhatsApp par reply karegi to aap Easypaisa transfer kar ke receipt share kar sakte hain.
        </div>

        <div id="epPaidWrap" style="display:none;">
          <input class="ep-input" id="epTid" placeholder="Sender Name ya Mobile # (e.g. Areej - 0335...)" autocomplete="off">
          <div class="ep-hint">
            📎 <strong>Payment Screenshot:</strong> Order send karne ke baad WhatsApp chat mein paperclip (📎) daba kar receipt ka screenshot bhej dein.
          </div>
        </div>
      </div>

      <button class="send" id="send" disabled>
        <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
          <path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.893 11.892-1.99-.001-3.951-.5-5.688-1.448l-6.305 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-.999 3.648 3.742-.981zm11.387-5.464c-.074-.124-.272-.198-.57-.347-.297-.149-1.758-.868-2.031-.967-.272-.099-.47-.149-.669.149-.198.297-.768.967-.941 1.165-.173.198-.347.223-.644.074-.297-.149-1.255-.462-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.297-.347.446-.521.151-.172.2-.296.3-.495.099-.198.05-.372-.025-.521-.075-.148-.669-1.611-.916-2.206-.242-.579-.487-.501-.669-.51l-.57-.01c-.198 0-.52.074-.792.372s-1.04 1.016-1.04 2.479 1.065 2.876 1.213 3.074c.149.198 2.095 3.2 5.076 4.487.709.306 1.263.489 1.694.626.712.226 1.36.194 1.872.118.571-.085 1.758-.719 2.006-1.413.248-.695.248-1.29.173-1.414z"/>
        </svg>
        Send Order on WhatsApp
      </button>
      <p class="tiny" id="sendHint" style="font-size:12px; margin-top:4px;">Fill Name, Phone &amp; Address to activate order button.</p>
    </div>
  </div>
</div>
</div>

<script>
const FRYZO_OFFICIAL_PHONE = "923284551176";
const TEST_PHONE = "923354936649"; // User test number
const PHONE = FRYZO_OFFICIAL_PHONE;
const EASYPAISA_NUM = "03434096282";
const EASYPAISA_DISP = "0343-4096282";

{img_code}

{menu_adds_code}

const CATS = [
  {{n:"Deals", sub:"Meals with drinks, ready to order", img:"hunger", icon:"🔥"}},
  {{n:"Pizza", sub:"Regular and premium, three sizes", img:"pizzabig", icon:"🍕"}},
  {{n:"Burgers", sub:"Zinger, grill, patty and beef smash", img:"burger", icon:"🍔"}},
  {{n:"Shawarma", sub:"Authentic Arabian platters & rolls", img:"platter", icon:"🌯"}},
  {{n:"Wraps & rolls", sub:"Wraps, paratha rolls and sandwiches", img:"wrap", icon:"🥪"}},
  {{n:"Chicken", sub:"Crispy pieces, wings, tenders and broast", img:"wings", icon:"🍗"}},
  {{n:"Fries & pasta", sub:"Loaded cheese fries & creamy pasta", img:"fries", icon:"🍟"}}
];

const slug = s => s.toLowerCase().replace(/[^a-z]+/g,"-").replace(/^-|-$/g,"");
const rs = n => "Rs " + n.toLocaleString("en-PK");
const cart = {{}}; // key "id|i" -> qty
let currentPayMethod = 'cod';
let epPaymentTiming = 'later';

/* Logos and hero photos */
["logoTop","logoHero","logoFoot"].forEach(id => document.getElementById(id).src = IMG.logo);
document.getElementById("sMain").src = IMG.hunger;
document.getElementById("sPizza").src = IMG.platter;
document.getElementById("sDuo").src = IMG.duo;
const hungerId = M.find(m => m.name === "Hunger Box").id;
document.getElementById("waFoot").href = "https://wa.me/" + PHONE + "?text=" + encodeURIComponent("Assalam o Alaikum Fryzo! Mujhe menu k baray mein poochna hai.");

/* Render menu */
const menu = document.getElementById("menu"), chips = document.getElementById("chips");
CATS.forEach(c => {{
  const a = document.createElement("button"); a.className = "chip"; a.innerHTML = `${{c.icon}} ${{c.n}}`;
  a.onclick = () => document.getElementById(slug(c.n)).scrollIntoView();
  a.dataset.c = slug(c.n); chips.appendChild(a);
  const sec = document.createElement("section"); sec.className = "cat"; sec.id = slug(c.n);
  let html = `<div class="cathead"><h2>${{c.n}}<small>${{c.sub}}</small></h2><img src="${{IMG[c.img]}}" alt=""></div>`;
  if (c.n === "Pizza") html += `<p class="note">Crust charges: Small Rs 150, Medium Rs 250, Large Rs 300 &bull; Extra topping: Small Rs 100, Medium Rs 150, Large Rs 200</p>`;
  const groups = [...new Set(M.filter(m => m.cat === c.n).map(m => m.group))];
  groups.forEach(g => {{
    if (g) html += `<h3 class="grp">${{g}}</h3>`;
    const items = M.filter(m => m.cat === c.n && m.group === g);
    html += `<div class="grid ${{c.n === "Deals" ? "deals" : "items"}}">` + items.map(c.n === "Deals" ? dcard : icard).join("") + `</div>`;
  }});
  sec.innerHTML = html; menu.appendChild(sec);
}});

function dcard(m){{
  const tag = m.pop ? `<span class="tag">Bestseller</span>` : "";
  return `<article class="dcard">
    <div class="ph">${{tag}}<img src="${{IMG[m.img]}}" alt="${{m.name}}"></div>
    <div class="bd">
      <h4>${{m.name}}</h4>
      ${{m.desc ? `<p>${{m.desc}}</p>` : ""}}
      <div class="row">
        <div class="price"><small>Rs</small>${{m.prices[0][1].toLocaleString()}}</div>
        <button class="add" data-k="${{m.id}}|0">+ Add to Order</button>
      </div>
    </div>
  </article>`;
}}

function icard(m){{
  const opts = m.prices.length
    ? m.prices.map((p,i) => `<button class="opt" data-k="${{m.id}}|${{i}}">${{p[0] ? p[0] + " " : "+ Add "}}${{rs(p[1])}}</button>`).join(" ")
    : `<span class="tiny">Ask on WhatsApp</span>`;
  return `<article class="icard">
    <div class="top">
      <div class="txt">
        <h4>${{m.name}}</h4>
        ${{m.desc ? `<p>${{m.desc}}</p>` : ""}}
      </div>
      <div class="th"><img src="${{IMG[m.img]}}" alt="${{m.name}}"></div>
    </div>
    <div class="opts">${{opts}}</div>
  </article>`;
}}

/* Payment selection logic */
function setPayMethod(m) {{
  currentPayMethod = m;
  const bCod = document.getElementById("btnPayCod");
  const bEp = document.getElementById("btnPayEp");
  const epBox = document.getElementById("epCard");

  if (m === 'easypaisa') {{
    bCod.classList.remove("active");
    bEp.classList.add("active", "ep-active");
    epBox.classList.add("show");
    setTimeout(() => {{
      const sb = document.getElementById("sheetBody");
      if (sb) sb.scrollTo({{ top: sb.scrollHeight, behavior: "smooth" }});
    }}, 120);
  }} else {{
    bEp.classList.remove("active", "ep-active");
    bCod.classList.add("active");
    epBox.classList.remove("show");
  }}
}}

function setEpStatus(status) {{
  epPaymentTiming = status;
  const bLater = document.getElementById("epTabLater");
  const bPaid = document.getElementById("epTabPaid");
  const hintLater = document.getElementById("epHintLater");
  const paidWrap = document.getElementById("epPaidWrap");

  if (status === 'paid') {{
    bPaid.classList.add("active");
    bLater.classList.remove("active");
    if (paidWrap) paidWrap.style.display = "block";
    if (hintLater) hintLater.style.display = "none";
    setTimeout(() => {{
      const sb = document.getElementById("sheetBody");
      if (sb) sb.scrollTo({{ top: sb.scrollHeight, behavior: "smooth" }});
    }}, 120);
  }} else {{
    bLater.classList.add("active");
    bPaid.classList.remove("active");
    if (paidWrap) paidWrap.style.display = "none";
    if (hintLater) hintLater.style.display = "block";
  }}
}}

function copyEp() {{
  navigator.clipboard.writeText(EASYPAISA_NUM).then(() => {{
    const b = document.getElementById("btnCopy");
    b.innerText = "✓ Copied!";
    b.style.background = "#3ddc84";
    setTimeout(() => {{
      b.innerText = "Copy Number";
      b.style.background = "#22c55e";
    }}, 1500);
  }}).catch(() => {{
    alert("Easypaisa Number: " + EASYPAISA_DISP);
  }});
}}



/* Cart logic */
function addKey(k, btn){{
  cart[k] = (cart[k] || 0) + 1;
  if (btn){{ btn.classList.add("ok"); setTimeout(() => btn.classList.remove("ok"), 600); }}
  update();
}}
document.addEventListener("click", e => {{
  const b = e.target.closest("[data-k]"); if (b) addKey(b.dataset.k, b);
}});
document.getElementById("sticker").onclick = () => {{ addKey(hungerId + "|0"); dr.classList.add("open"); }};

const entries = () => Object.keys(cart).filter(k => cart[k] > 0).map(k => {{
  const [id,i] = k.split("|").map(Number), m = M[id], p = m.prices[i];
  return {{k, name: m.name + (p[0] ? " (" + p[0] + ")" : ""), price: p[1], qty: cart[k]}};
}});

function update(){{
  const es = entries(), n = es.reduce((a,x) => a + x.qty, 0), t = es.reduce((a,x) => a + x.qty * x.price, 0);
  const fab = document.getElementById("fab");
  const cartFoot = document.getElementById("cartFoot");
  
  // Show FAB only when items exist! Completely hide when empty
  if (n > 0) {{
    fab.classList.add("show");
  }} else {{
    fab.classList.remove("show");
  }}

  const cn = document.getElementById("cartN"); cn.textContent = n; cn.classList.toggle("on", n > 0);
  document.getElementById("fabN").textContent = n + (n === 1 ? " item" : " items");
  document.getElementById("fabT").textContent = rs(t);
  document.getElementById("total").textContent = rs(t);
  const epBill = document.getElementById("epBillAmount");
  if (epBill) epBill.textContent = rs(t);

  const linesEl = document.getElementById("lines");
  if (es.length > 0) {{
    linesEl.innerHTML = es.map(x =>
      `<div class="line">
        <div>
          <strong>${{x.name}}</strong>
          <small>${{rs(x.price)}} each</small>
        </div>
        <div class="qty">
          <button data-d="-1" data-q="${{x.k}}">&minus;</button>
          <span>${{x.qty}}</span>
          <button data-d="1" data-q="${{x.k}}">&plus;</button>
        </div>
      </div>`
    ).join("");
    cartFoot.classList.remove("hide-checkout");
  }} else {{
    linesEl.innerHTML = `
      <div class="empty-state-box">
        <div class="empty-icon">🍔</div>
        <h3>Your order is empty</h3>
        <p>Pick some delicious deals or zinger burgers from the menu to start your order!</p>
        <button class="btn-browse" onclick="dr.classList.remove('open'); document.getElementById('deals').scrollIntoView({{behavior:'smooth'}});">
          Explore Menu Deals &rarr;
        </button>
      </div>
    `;
    cartFoot.classList.add("hide-checkout");
  }}
  valid();
}}

document.getElementById("lines").addEventListener("click", e => {{
  const b = e.target.closest("[data-q]"); if (!b) return;
  cart[b.dataset.q] = Math.max(0, cart[b.dataset.q] + Number(b.dataset.d)); update();
}});

const nm = document.getElementById("nm"), ph = document.getElementById("ph"), ad = document.getElementById("ad"), lm = document.getElementById("lm"), send = document.getElementById("send");
function valid(){{
  const ok = Boolean(entries().length && nm.value.trim() && ph.value.trim() && ad.value.trim());
  send.disabled = !ok;
  const hintEl = document.getElementById("sendHint");
  if (hintEl) {{
    if (!ok) {{
      hintEl.textContent = "Please fill Name, Phone & Address to enable order button.";
      hintEl.style.color = "var(--dim)";
    }} else {{
      hintEl.textContent = "Ready! Tap button to send order directly to WhatsApp.";
      hintEl.style.color = "#3ddc84";
      hintEl.style.fontWeight = "600";
    }}
  }}
}}
[nm, ph, ad, lm].forEach(el => el && (el.oninput = valid));

send.onclick = () => {{
  const es = entries(), t = es.reduce((a,x) => a + x.qty * x.price, 0);
  const isEp = (currentPayMethod === 'easypaisa');
  const orderId = "FZ-" + Math.floor(1000 + Math.random() * 9000);

  const customerName = nm.value.trim();
  const customerPhone = ph.value.trim();
  const customerAddress = ad.value.trim();
  const customerLandmark = lm ? lm.value.trim() : "";

  let msg = `*FRYZO LAHORE - ONLINE ORDER* (#${{orderId}})\\n`;
  msg += `------------------------------------\\n`;
  msg += `Assalam o Alaikum Fryzo team! Mera delivery order record kar lein:\\n\\n`;
  msg += `*CUSTOMER & RIDER DETAILS:*\\n`;
  msg += `• Name: ${{customerName}}\\n`;
  msg += `• Phone: ${{customerPhone}} (Call/WhatsApp for Rider)\\n`;
  msg += `• Delivery Address: ${{customerAddress}}\\n`;
  if (customerLandmark) {{
    msg += `• Nearby Landmark / Note: ${{customerLandmark}}\\n`;
  }}
  msg += `\\n*ORDERED ITEMS:*\\n`;

  es.forEach((x, idx) => {{
    msg += `${{idx + 1}}. *${{x.name}}*  (Qty: ${{x.qty}}x)  -  ${{rs(x.qty * x.price)}}\\n`;
  }});

  msg += `\\n------------------------------------\\n`;
  msg += `*PAYMENT SUMMARY:*\\n`;
  msg += `• Items Subtotal: ${{rs(t)}}\\n`;
  msg += `• Delivery Charges: FREE (Lahore)\\n`;
  msg += `• *GRAND TOTAL: ${{rs(t)}}*\\n`;
  if (isEp) {{
    const epRef = (document.getElementById("epTid") ? document.getElementById("epTid").value.trim() : "");
    msg += `• Payment Mode: Easypaisa Online (${{EASYPAISA_DISP}})\\n`;
    if (epPaymentTiming === 'paid') {{
      msg += `• Payment Status: Paid / Transferred`;
      if (epRef) msg += ` (Sender: ${{epRef}})`;
      msg += `\\n`;
      msg += `  (Note: Payment screenshot WhatsApp chat mein share kar rahe hain)\\n`;
    }} else {{
      msg += `• Payment Status: Pay on Confirmation\\n`;
      msg += `  (Note: Fryzo team pehle order confirm karein, hum foran ${{rs(t)}} transfer kar k screenshot share karenge)\\n`;
    }}
  }} else {{
    msg += `• Payment Mode: Cash on Delivery (COD)\\n`;
    msg += `• Cash to Collect by Rider: ${{rs(t)}}\\n`;
  }}
  msg += `------------------------------------\\n`;
  msg += `Please confirm my order & share estimated delivery time. Shukriya!`;

  window.open("https://wa.me/" + PHONE + "?text=" + encodeURIComponent(msg), "_blank");
}};

const dr = document.getElementById("drawer");
document.getElementById("fab").onclick = document.getElementById("cartbtn").onclick = () => dr.classList.add("open");
document.getElementById("close").onclick = document.getElementById("back").onclick = () => dr.classList.remove("open");
document.addEventListener("keydown", e => {{ if (e.key === "Escape") dr.classList.remove("open"); }});

/* Open / closed, Pakistan time, 3pm to 3am */
function openNow(){{
  const h = Number(new Intl.DateTimeFormat("en-GB",{{hour:"numeric",hour12:false,timeZone:"Asia/Karachi"}}).format(new Date()));
  const open = h >= 15 || h < 3;
  document.getElementById("dot").classList.toggle("closed", !open);
  document.getElementById("stat").textContent = open ? "Open now" : "Opens at 3pm";
}}
openNow(); setInterval(openNow, 60000);

/* Active chip on scroll */
const io = new IntersectionObserver(es => es.forEach(x => {{
  if (x.isIntersecting) document.querySelectorAll(".chip").forEach(c => c.classList.toggle("on", c.dataset.c === x.target.id));
}}), {{rootMargin:"-30% 0px -60% 0px"}});
document.querySelectorAll("section.cat").forEach(s => io.observe(s));
update();
</script>
</body>
</html>"""

# Write to both locations
with open("/Users/mac/Downloads/fryzo-demo-v2.html", "w", encoding="utf-8") as f:
    f.write(new_html)
print("Updated /Users/mac/Downloads/fryzo-demo-v2.html successfully!")

with open("/Users/mac/.gemini/antigravity-ide/scratch/fryzo/index.html", "w", encoding="utf-8") as f:
    f.write(new_html)
print("Updated /Users/mac/.gemini/antigravity-ide/scratch/fryzo/index.html successfully!")
