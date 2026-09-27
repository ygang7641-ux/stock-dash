from __future__ import annotations

import html
import streamlit as st


NAV_ITEMS = [
    ("홈", "⌂"),
    ("시장 현황", "▥"),
    ("종목 분석", "◫"),
    ("공시 분석", "▤"),
    ("테마 & 섹터", "◇"),
    ("포트폴리오", "▣"),
    ("관심 종목", "☆"),
    ("AI 인사이트", "✦"),
    ("데이터 연결 관리", "⚙"),
]


def apply_theme():
    st.markdown(
        """
<style>
:root {
  color-scheme: dark;
  --bg: #0b0f14;
  --surface: #111820;
  --surface-raised: #151e28;
  --surface-hover: #1b2732;
  --line: #25313c;
  --line-soft: #1d2832;
  --text: #e8eef3;
  --muted: #94a3af;
  --subtle: #667684;
  --accent: #39d6b0;
  --accent-soft: rgba(57,214,176,.12);
  --up: #ff6b72;
  --down: #66aaff;
}
html, body, [class*="css"] {
  font-family: Inter, Pretendard, "Noto Sans KR", "Apple SD Gothic Neo", sans-serif;
}
.stApp { background: var(--bg); color: var(--text); }
.block-container { max-width: 1540px; padding: 1.6rem 2rem 4rem; }
header[data-testid="stHeader"] { background: rgba(11,15,20,.88); backdrop-filter: blur(14px); }
[data-testid="stToolbar"] { right: 1rem; }
section[data-testid="stSidebar"] { background: #0e141a; border-right: 1px solid var(--line-soft); }
section[data-testid="stSidebar"] > div { padding: 1.1rem .8rem; }
[data-testid="stSidebar"] .stRadio > label { display: none; }
[data-testid="stSidebar"] .stRadio div[role="radiogroup"] { gap: .3rem; }
[data-testid="stSidebar"] .stRadio div[role="radiogroup"] label {
  border: 1px solid transparent; border-radius: 10px; padding: .48rem .65rem;
  color: #a9b5bf; transition: background .16s ease, border-color .16s ease;
}
[data-testid="stSidebar"] .stRadio div[role="radiogroup"] label:hover { background: #151e27; }
[data-testid="stSidebar"] .stRadio div[role="radiogroup"] label:has(input:checked) {
  color: var(--accent); background: var(--accent-soft); border-color: rgba(57,214,176,.18); font-weight: 700;
}
h1, h2, h3, h4 { color: var(--text); letter-spacing: -.035em; }
h1 { font-weight: 760; }
h2, h3 { font-weight: 700; }
p, li { line-height: 1.65; }
[data-testid="stCaptionContainer"], .stMarkdown small { color: var(--muted); }
[data-testid="stMetric"] {
  background: linear-gradient(145deg, #141d26, #10171f); border: 1px solid var(--line);
  border-radius: 14px; padding: 16px 18px; box-shadow: 0 8px 24px rgba(0,0,0,.14);
}
[data-testid="stMetricLabel"] { color: var(--muted); }
[data-testid="stMetricValue"] { color: var(--text); font-weight: 750; }
[data-testid="stMetricDelta"] svg { display: inline-block; }
[data-testid="stVerticalBlockBorderWrapper"] {
  border-color: var(--line) !important; border-radius: 14px !important;
  background: var(--surface); box-shadow: 0 8px 24px rgba(0,0,0,.12);
}
.stButton > button, .stFormSubmitButton > button, .stDownloadButton > button {
  border-radius: 10px; min-height: 2.55rem; font-weight: 650;
  border-color: var(--line); background: #17212b; color: var(--text);
  transition: border-color .15s ease, background .15s ease;
}
.stButton > button:hover, .stDownloadButton > button:hover { border-color: #3d5965; background: #1c2a34; color: white; }
.stButton > button[kind="primary"], .stFormSubmitButton > button[kind="primary"] {
  color: #061510; background: var(--accent); border-color: var(--accent);
}
.stButton > button[kind="primary"]:hover, .stFormSubmitButton > button[kind="primary"]:hover {
  background: #55e3c0; border-color: #55e3c0; color: #061510;
}
.stTextInput input, .stTextArea textarea, .stSelectbox div[data-baseweb="select"] > div,
.stDateInput input, .stNumberInput input {
  border-radius: 10px !important; background: #0e151c !important; color: var(--text) !important;
  border-color: var(--line) !important;
}
[data-baseweb="popover"] [role="listbox"], [data-baseweb="menu"] { background: #141d26; }
[data-baseweb="menu"] [role="option"] { color: var(--text); }
.stTabs [data-baseweb="tab-list"] { gap: 6px; border-bottom-color: var(--line); }
.stTabs [data-baseweb="tab"] { border-radius: 8px 8px 0 0; padding: 9px 13px; color: var(--muted); }
.stTabs [aria-selected="true"] { color: var(--accent) !important; }
.stDataFrame, [data-testid="stDataFrame"] { border: 1px solid var(--line); border-radius: 12px; overflow: hidden; }
[data-testid="stExpander"] { background: var(--surface); border: 1px solid var(--line); border-radius: 12px; }
[data-testid="stExpander"] summary p { color: var(--text); }
[data-testid="stAlert"] { border-radius: 12px; }
hr { border-color: var(--line) !important; }
a { color: var(--accent); }
.planx-brand { display:flex; align-items:center; gap:10px; margin: 2px 0 20px; }
.planx-brand-mark {
  width:34px; height:34px; border-radius:10px; display:flex; align-items:center; justify-content:center;
  background:linear-gradient(145deg,#1fbf9c,#39d6b0); color:#071510; font-size:18px; font-weight:800;
}
.planx-brand-title { font-size:19px; line-height:1.15; font-weight:800; letter-spacing:-.04em; color:var(--text); }
.planx-brand-sub { font-size:9px; color:var(--subtle); margin-top:4px; letter-spacing:.14em; }
.planx-hero {
  background: radial-gradient(ellipse at 100% 0%, rgba(57,214,176,.10), transparent 43%),
              linear-gradient(135deg, #141e27, #10171f 72%);
  border:1px solid var(--line); border-radius:18px; padding:25px 28px; margin-bottom:18px;
  box-shadow:0 15px 38px rgba(0,0,0,.16);
}
.planx-eyebrow { color:var(--accent); font-size:10px; font-weight:800; letter-spacing:.14em; text-transform:uppercase; margin-bottom:9px; }
.planx-hero h1 { margin:0; font-size:31px; line-height:1.2; }
.planx-hero p { margin:9px 0 0; color:var(--muted); font-size:13px; }
.planx-card {
  background:linear-gradient(150deg,#141d26,#10171e); border:1px solid var(--line);
  border-radius:14px; padding:17px 18px; min-height:112px; box-shadow:0 8px 24px rgba(0,0,0,.13);
}
.planx-card-title { font-size:11px; color:var(--muted); margin-bottom:9px; font-weight:650; }
.planx-card-value { font-size:21px; color:var(--text); font-weight:760; letter-spacing:-.03em; }
.planx-card-note { margin-top:7px; font-size:10px; color:var(--subtle); }
.planx-empty { background:#111820; border:1px dashed #34424e; border-radius:14px; padding:20px; color:var(--muted); }
.planx-source { display:inline-flex; align-items:center; gap:5px; color:var(--muted); background:#18212a; border:1px solid var(--line); padding:4px 8px; border-radius:999px; font-size:10px; }
.planx-status-ok { color:#54dfba; background:rgba(57,214,176,.1); border-color:rgba(57,214,176,.24); }
.planx-status-wait { color:#e9be74; background:rgba(233,190,116,.09); border-color:rgba(233,190,116,.2); }
.planx-status-bad { color:#ff858b; background:rgba(255,107,114,.09); border-color:rgba(255,107,114,.2); }
@media (max-width: 900px) { .block-container { padding:1.2rem 1rem 3rem; } .planx-hero { padding:21px; } .planx-hero h1 { font-size:26px; } }
@media (max-width: 640px) { .block-container { padding:.8rem .75rem 2.5rem; } .planx-card { min-height:96px; padding:14px; } .planx-card-value { font-size:18px; } }
</style>
""",
        unsafe_allow_html=True,
    )


def brand():
    st.markdown(
        """
<div class="planx-brand">
  <div class="planx-brand-mark">↗</div>
  <div>
    <div class="planx-brand-title">PlanX</div>
    <div class="planx-brand-sub">STOCK INTELLIGENCE</div>
  </div>
</div>
""",
        unsafe_allow_html=True,
    )


def hero(title: str, subtitle: str, eyebrow: str = "PLANX INVESTMENT OS"):
    st.markdown(
        f"""
<div class="planx-hero">
  <div class="planx-eyebrow">{html.escape(eyebrow)}</div>
  <h1>{html.escape(title)}</h1>
  <p>{html.escape(subtitle)}</p>
</div>
""",
        unsafe_allow_html=True,
    )


def card(title: str, value: str, note: str = "", status: str = ""):
    status_html = f'<div class="planx-card-note">{html.escape(status)}</div>' if status else ""
    st.markdown(
        f"""
<div class="planx-card">
  <div class="planx-card-title">{html.escape(title)}</div>
  <div class="planx-card-value">{html.escape(value)}</div>
  <div class="planx-card-note">{html.escape(note)}</div>
  {status_html}
</div>
""",
        unsafe_allow_html=True,
    )


def empty_state(title: str, message: str):
    st.markdown(
        f"""
<div class="planx-empty">
  <strong style="color:#e8eef3">{html.escape(title)}</strong><br>
  <span>{html.escape(message)}</span>
</div>
""",
        unsafe_allow_html=True,
    )


def source_badge(label: str, state: str = "wait"):
    cls = {"ok": "planx-status-ok", "bad": "planx-status-bad"}.get(state, "planx-status-wait")
    st.markdown(
        f'<span class="planx-source {cls}">{html.escape(label)}</span>',
        unsafe_allow_html=True,
    )

