# app.py
# Streamlit flashcard game (Myths vs Facts about Languages) — visually upgraded + FIXED flip rendering
# Run: streamlit run app.py

import random
import base64
import html
from typing import List, Dict, Optional

import streamlit as st
import streamlit.components.v1 as components

# -----------------------------
# Page config
# -----------------------------
st.set_page_config(
    page_title="Myth or Fact? — Languages Flashcards",
    page_icon="🃏",
    layout="centered",
    initial_sidebar_state="expanded",
)

# -----------------------------
# Data
# -----------------------------
CARDS: List[Dict] = [
    {
        "id": 1,
        "statement": "French is the most romantic language.",
        "label": "MYTH",
        "explanation": "“Romantic” refers to Romance languages derived from Latin — not emotional qualities.",
        "discussion": [
            "Why do certain languages get stereotyped as “romantic” or “harsh”?",
            "How much does media influence our perception of languages?",
        ],
        "tags": ["stereotypes", "media", "romance languages"],
    },
    {
        "id": 2,
        "statement": "German has words that are impossible to translate.",
        "label": "MYTH",
        "explanation": "Any idea can be translated — sometimes using phrases instead of single words.",
        "discussion": [
            "Does translation require word-for-word equivalence?",
            "Can cultural concepts be translated without losing nuance?",
        ],
        "tags": ["translation", "meaning", "culture"],
    },
    {
        "id": 3,
        "statement": "Sanskrit is the most scientific language in the world.",
        "label": "MYTH",
        "explanation": "All languages are rule-governed systems. No language is inherently more “scientific.”",
        "discussion": [
            "What do people usually mean by “scientific language”?",
            "Is systematic grammar the same as scientific superiority?",
        ],
        "tags": ["grammar", "myths", "linguistics"],
    },
    {
        "id": 4,
        "statement": "African American English (AAE) is ‘bad English.’",
        "label": "MYTH",
        "explanation": "AAE has consistent grammar and linguistic rules. It is a legitimate dialect.",
        "discussion": [
            "Why are some dialects stigmatized?",
            "Who decides what counts as “correct” English?",
        ],
        "tags": ["dialects", "prestige", "sociolinguistics"],
    },
    {
        "id": 5,
        "statement": "Hindi and Urdu are completely different languages.",
        "label": "MYTH",
        "explanation": "They are largely mutually intelligible in everyday speech and mainly differ in script and formal vocabulary.",
        "discussion": [
            "What makes two varieties separate languages rather than dialects?",
            "Is the distinction linguistic or political?",
        ],
        "tags": ["mutual intelligibility", "script", "politics"],
    },
    {
        "id": 6,
        "statement": "Sign language is the same everywhere in the world.",
        "label": "MYTH",
        "explanation": "There are many distinct sign languages with their own grammars.",
        "discussion": [
            "Why do people assume sign languages are universal?",
            "What does this reveal about misconceptions about Deaf communities?",
        ],
        "tags": ["sign languages", "deaf culture", "grammar"],
    },
    {
        "id": 7,
        "statement": "English will eventually replace all other languages.",
        "label": "MYTH",
        "explanation": "Language survival depends on identity, policy, and community use.",
        "discussion": [
            "Is multilingualism the global norm?",
            "What factors actually cause language death?",
        ],
        "tags": ["language shift", "identity", "policy"],
    },
    {
        "id": 8,
        "statement": "Shakespeare used perfect English.",
        "label": "MYTH",
        "explanation": "Shakespeare innovated and experimented with English; his language was evolving.",
        "discussion": [
            "Why do we treat older forms of language as “purer”?",
            "Is there such a thing as perfect grammar?",
        ],
        "tags": ["history", "change", "standardization"],
    },
    {
        "id": 9,
        "statement": "Dictionaries decide what’s correct.",
        "label": "MYTH",
        "explanation": "Dictionaries describe usage; they do not invent or enforce rules.",
        "discussion": [
            "What is the difference between prescriptive and descriptive grammar?",
            "Should dictionaries influence language use?",
        ],
        "tags": ["prescriptivism", "descriptivism", "usage"],
    },
    {
        "id": 10,
        "statement": "Texting and social media are destroying language.",
        "label": "MYTH",
        "explanation": "Digital communication follows its own conventions and shows linguistic creativity.",
        "discussion": [
            "Do you change how you write in different contexts?",
            "Is informal writing a threat to formal language skills?",
        ],
        "tags": ["digital language", "register", "creativity"],
    },
    {
        "id": 11,
        "statement": "There’s only one correct English.",
        "label": "MYTH",
        "explanation": "There are many valid varieties of English worldwide. Standard English is just one variety.",
        "discussion": [
            "What is Standard English?",
            "Should schools teach only one variety?",
        ],
        "tags": ["world englishes", "standard language", "education"],
    },
    {
        "id": 12,
        "statement": "Babies can distinguish all speech sounds in the world at birth.",
        "label": "FACT",
        "explanation": "Infants initially perceive a wide range of phonetic contrasts but later specialize in their native language sounds.",
        "discussion": [
            "Why does this ability narrow over time?",
            "What does this tell us about language acquisition?",
        ],
        "tags": ["phonetics", "acquisition", "development"],
    },
    {
        "id": 13,
        "statement": "Some languages have no word for ‘blue.’",
        "label": "FACT",
        "explanation": "Some languages categorize colors differently and may not separate blue and green as distinct basic terms.",
        "discussion": [
            "Does language influence perception of color?",
            "How does this relate to linguistic relativity?",
        ],
        "tags": ["semantics", "color terms", "relativity"],
    },
    {
        "id": 14,
        "statement": "Children today have a smaller vocabulary than previous generations.",
        "label": "MYTH",
        "explanation": "Vocabulary shifts with cultural change; new domains create new words rather than shrinking vocabulary.",
        "discussion": [
            "Do digital environments create new lexical fields?",
            "How can vocabulary size be measured accurately?",
        ],
        "tags": ["lexicon", "change", "measurement"],
    },
]

# -----------------------------
# Themes
# -----------------------------
THEMES = {
    "Aurora Night": {
        "bg": "radial-gradient(1200px 800px at 20% 10%, rgba(77,224,195,0.18), rgba(0,0,0,0) 55%),"
              "radial-gradient(900px 700px at 80% 20%, rgba(130,87,229,0.20), rgba(0,0,0,0) 55%),"
              "radial-gradient(1000px 700px at 60% 90%, rgba(255,122,182,0.12), rgba(0,0,0,0) 60%),"
              "linear-gradient(180deg, rgba(10,12,18,1), rgba(7,9,14,1))",
        "card": "linear-gradient(180deg, rgba(255,255,255,0.10), rgba(255,255,255,0.05))",
        "accent": "#7ee7d6",
    },
    "Vintage Paper": {
        "bg": "radial-gradient(900px 700px at 30% 20%, rgba(255,216,155,0.20), rgba(0,0,0,0) 60%),"
              "radial-gradient(900px 700px at 80% 60%, rgba(255,170,170,0.10), rgba(0,0,0,0) 55%),"
              "linear-gradient(180deg, #1b1a17, #12110f)",
        "card": "linear-gradient(180deg, rgba(255,243,220,0.12), rgba(255,243,220,0.06))",
        "accent": "#ffd89b",
    },
    "Midnight Ink": {
        "bg": "radial-gradient(1000px 800px at 25% 20%, rgba(90,161,255,0.18), rgba(0,0,0,0) 60%),"
              "radial-gradient(1000px 700px at 80% 80%, rgba(255,196,90,0.10), rgba(0,0,0,0) 60%),"
              "linear-gradient(180deg, #0a0f1f, #070a12)",
        "card": "linear-gradient(180deg, rgba(255,255,255,0.09), rgba(255,255,255,0.045))",
        "accent": "#6aa8ff",
    },
}

LANG_SVG = r"""
<svg width="100%" height="100%" viewBox="0 0 900 140" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <filter id="glow"><feGaussianBlur stdDeviation="2.5" result="coloredBlur"/><feMerge><feMergeNode in="coloredBlur"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
    <linearGradient id="g" x1="0" x2="1">
      <stop offset="0" stop-color="rgba(126,231,214,0.95)"/>
      <stop offset="0.5" stop-color="rgba(130,87,229,0.95)"/>
      <stop offset="1" stop-color="rgba(255,122,182,0.95)"/>
    </linearGradient>
  </defs>
  <g opacity="0.20">
    <circle cx="80" cy="60" r="40" fill="url(#g)"/>
    <circle cx="820" cy="50" r="36" fill="url(#g)"/>
    <circle cx="720" cy="102" r="26" fill="url(#g)"/>
    <circle cx="190" cy="108" r="22" fill="url(#g)"/>
  </g>
  <g filter="url(#glow)" opacity="0.85" fill="url(#g)" font-family="ui-sans-serif, system-ui" font-weight="700">
    <text x="60" y="74" font-size="44">Aa</text>
    <text x="160" y="116" font-size="34">あ</text>
    <text x="240" y="74" font-size="42">أ</text>
    <text x="310" y="116" font-size="34">क</text>
    <text x="390" y="74" font-size="42">Ω</text>
    <text x="470" y="116" font-size="34">你</text>
    <text x="540" y="74" font-size="42">ß</text>
    <text x="620" y="116" font-size="34">ש</text>
    <text x="690" y="74" font-size="42">∑</text>
    <text x="770" y="116" font-size="34">한</text>
  </g>
  <g opacity="0.18">
    <path d="M40 128 C140 116, 220 132, 320 120 C420 108, 500 132, 600 118 C700 104, 780 132, 860 120"
          fill="none" stroke="url(#g)" stroke-width="2" stroke-dasharray="4 10"/>
  </g>
</svg>
""".strip()

def svg_to_data_uri(svg: str) -> str:
    b64 = base64.b64encode(svg.encode("utf-8")).decode("utf-8")
    return f"data:image/svg+xml;base64,{b64}"

# -----------------------------
# State + helpers
# -----------------------------
def is_fact(label: str) -> bool:
    return label.strip().upper() == "FACT"

def new_deck(mode: str) -> List[int]:
    idxs = list(range(len(CARDS)))
    if mode == "Shuffle":
        random.shuffle(idxs)
    return idxs

def init_game(mode: str):
    st.session_state.deck = new_deck(mode)
    st.session_state.i = 0
    st.session_state.score = 0
    st.session_state.streak = 0
    st.session_state.best_streak = 0
    st.session_state.answered = False
    st.session_state.choice = None
    st.session_state.correct = None
    st.session_state.flipped = False
    st.session_state.wrong_ids = set()
    st.session_state.history = []

def get_card() -> Optional[Dict]:
    if st.session_state.i >= len(st.session_state.deck):
        return None
    return CARDS[st.session_state.deck[st.session_state.i]]

# -----------------------------
# Initialize session
# -----------------------------
if "theme" not in st.session_state:
    st.session_state.theme = "Aurora Night"
if "mode" not in st.session_state:
    st.session_state.mode = "Shuffle"
if "deck" not in st.session_state:
    init_game(st.session_state.mode)

# -----------------------------
# Sidebar controls
# -----------------------------
st.sidebar.title("🎛️ Control Panel")

st.session_state.theme = st.sidebar.selectbox(
    "Theme", list(THEMES.keys()),
    index=list(THEMES.keys()).index(st.session_state.theme),
)

st.session_state.mode = st.sidebar.radio(
    "Deck order", ["Shuffle", "In order"],
    index=0 if st.session_state.mode == "Shuffle" else 1,
)

show_discussion = st.sidebar.toggle("Show discussion starters", value=True)
show_tags = st.sidebar.toggle("Show topic chips", value=True)
hard_mode = st.sidebar.toggle("Hard mode (no hints)", value=False)

st.sidebar.divider()

c1, c2 = st.sidebar.columns(2)
with c1:
    if st.button("🔄 Restart", use_container_width=True):
        init_game(st.session_state.mode)
        st.rerun()

with c2:
    if st.button("🎯 Practice wrong", use_container_width=True):
        if st.session_state.wrong_ids:
            wrong_idxs = [i for i, c in enumerate(CARDS) if c["id"] in st.session_state.wrong_ids]
            random.shuffle(wrong_idxs)
            st.session_state.deck = wrong_idxs
            st.session_state.i = 0
            st.session_state.score = 0
            st.session_state.streak = 0
            st.session_state.answered = False
            st.session_state.flipped = False
            st.session_state.history = []
        st.rerun()

# -----------------------------
# Apply global styling
# -----------------------------
theme = THEMES[st.session_state.theme]
banner_uri = svg_to_data_uri(LANG_SVG)

st.markdown(
    f"""
<style>
.stApp {{
  background: {theme["bg"]};
}}
.block-container {{
  padding-top: 1.1rem;
  max-width: 860px;
}}
.lang-banner {{
  width: 100%;
  height: 120px;
  border-radius: 22px;
  overflow: hidden;
  border: 1px solid rgba(255,255,255,0.12);
  box-shadow: 0 14px 40px rgba(0,0,0,0.25);
  background: rgba(255,255,255,0.03);
}}
div.stButton > button {{
  border-radius: 16px !important;
  padding: 0.85rem 1rem !important;
  border: 1px solid rgba(255,255,255,0.14) !important;
  background: rgba(255,255,255,0.06) !important;
  box-shadow: 0 10px 30px rgba(0,0,0,0.25) !important;
}}
div.stButton > button:hover {{
  background: rgba(255,255,255,0.09) !important;
  transform: translateY(-1px);
}}
</style>
""",
    unsafe_allow_html=True,
)

# -----------------------------
# Header
# -----------------------------
st.markdown(
    f"""
<div class="lang-banner">
  <img src="{banner_uri}" style="width:100%; height:100%; object-fit:cover;" />
</div>
""",
    unsafe_allow_html=True,
)

st.title("🃏 Myth or Fact? — Languages Flashcards")
st.caption("Choose **True** or **False**, then **flip** to reveal the explanation + discussion prompts.")

# -----------------------------
# Game
# -----------------------------
card = get_card()
if card is None:
    total = len(st.session_state.deck)
    st.success(f"Finished! Score: **{st.session_state.score}/{total}**  ·  Best streak: **{st.session_state.best_streak} 🔥**")
    with st.expander("📋 Review session"):
        for h in st.session_state.history:
            icon = "✅" if h["correct"] else "❌"
            st.markdown(
                f"**{h['n']}. “{h['statement']}”** {icon}\n\n"
                f"- Correct answer: **{h['answer']}** ({h['label']})\n"
                f"- You chose: **{h['choice']}**\n"
                f"- Note: {h['explanation']}\n"
            )
    if st.button("🔁 Play again", use_container_width=True):
        init_game(st.session_state.mode)
        st.rerun()
    st.stop()

# Progress / metrics
n = st.session_state.i + 1
total = len(st.session_state.deck)
st.progress((n - 1) / total, text=f"Card {n} of {total}")

m1, m2, m3 = st.columns(3)
m1.metric("Score", f"{st.session_state.score}/{max(0, n-1)}")
m2.metric("Streak", f"{st.session_state.streak} 🔥")
m3.metric("Best", f"{st.session_state.best_streak}")

# -----------------------------
# Answer logic
# -----------------------------
truth = is_fact(card["label"])
correct_answer = "True" if truth else "False"

def submit(choice: str):
    st.session_state.answered = True
    st.session_state.choice = choice
    user_true = (choice == "True")
    st.session_state.correct = (user_true == truth)

    if st.session_state.correct:
        st.session_state.score += 1
        st.session_state.streak += 1
        st.session_state.best_streak = max(st.session_state.best_streak, st.session_state.streak)
        st.toast("Nice! ✅", icon="✨")
    else:
        st.session_state.streak = 0
        st.session_state.wrong_ids.add(card["id"])
        st.toast("Flip to learn. ❌", icon="🧠")

# -----------------------------
# Render the flip-card via components.html (FIX)
# -----------------------------
statement = html.escape(card["statement"])
explanation = html.escape(card["explanation"])
label = card["label"].strip().upper()
kind = "FACT ✅" if label == "FACT" else "MYTH 🚫"

hint_line = "Decide if the statement is true."
if not hard_mode:
    hint_line += " (Hint: some are FACT, most are MYTH.)"

chips_html = ""
if show_tags and card.get("tags"):
    chips = "".join(
        f'<span class="chip"><span class="dot"></span>{html.escape(t)}</span>'
        for t in card["tags"]
    )
    chips_html = f'<div class="chips">{chips}</div>'

discussion_html = ""
if show_discussion and card.get("discussion"):
    items = "".join(f"<li>{html.escape(q)}</li>" for q in card["discussion"])
    discussion_html = f"""
      <div class="box">
        <div class="boxTitle">Discussion starters 💬</div>
        <ul class="ul">{items}</ul>
      </div>
    """

flip_class = "flipped" if st.session_state.flipped else ""

card_html = f"""
<!doctype html>
<html>
<head>
<meta charset="utf-8"/>
<style>
  :root {{
    --accent: {theme["accent"]};
    --cardbg: {theme["card"]};
  }}
  body {{
    margin: 0;
    font-family: ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Arial;
    color: rgba(255,255,255,0.95);
  }}
  .stage {{
    perspective: 1200px;
  }}
  .card {{
    position: relative;
    width: 100%;
    min-height: 320px;
    border-radius: 22px;
    transform-style: preserve-3d;
    transition: transform 0.75s cubic-bezier(.2,.8,.2,1);
    border: 1px solid rgba(255,255,255,0.12);
    box-shadow: 0 22px 70px rgba(0,0,0,0.35);
    background: var(--cardbg);
    overflow: hidden;
  }}
  .card.flipped {{
    transform: rotateY(180deg);
  }}
  .face {{
    position: absolute;
    inset: 0;
    padding: 18px;
    backface-visibility: hidden;
    -webkit-backface-visibility: hidden;
  }}
  .back {{
    transform: rotateY(180deg);
  }}
  .stamp {{
    position: absolute;
    top: 14px;
    right: 14px;
    padding: 6px 10px;
    border-radius: 999px;
    font-size: 0.82rem;
    border: 1px solid rgba(255,255,255,0.14);
    background: rgba(0,0,0,0.18);
  }}
  .subtitle {{
    opacity: 0.85;
    font-size: 0.98rem;
    margin-top: 6px;
  }}
  .statement {{
    font-size: 1.55rem;
    line-height: 1.22;
    margin-top: 14px;
    margin-bottom: 12px;
  }}
  .smallnote {{
    opacity: 0.88;
    font-size: 0.95rem;
    line-height: 1.35;
  }}
  .box {{
    margin-top: 12px;
    padding: 12px;
    border-radius: 16px;
    border: 1px solid rgba(255,255,255,0.14);
    background: rgba(0,0,0,0.16);
  }}
  .boxTitle {{
    font-weight: 800;
    margin-bottom: 6px;
  }}
  .chips {{
    display:flex;
    flex-wrap:wrap;
    gap: 8px;
    margin-top: 12px;
  }}
  .chip {{
    display:inline-flex;
    align-items:center;
    gap: 6px;
    padding: 6px 10px;
    border-radius: 999px;
    border: 1px solid rgba(255,255,255,0.14);
    background: rgba(255,255,255,0.05);
    font-size: 0.82rem;
    opacity: 0.92;
  }}
  .dot {{
    width: 8px;
    height: 8px;
    border-radius: 999px;
    background: var(--accent);
    box-shadow: 0 0 12px rgba(255,255,255,0.12);
  }}
  .ul {{
    margin: 0;
    padding-left: 18px;
  }}
</style>
</head>
<body>
  <div class="stage">
    <div class="card {flip_class}">
      <div class="face front">
        <div class="stamp">Front 🧩</div>
        <div class="subtitle">🎯 GUESS: Myth or Fact?</div>
        <div class="statement">“{statement}”</div>
        <div class="smallnote">{html.escape(hint_line)}</div>
        {chips_html}
        <div class="box">
          <div class="boxTitle">How to play</div>
          <div class="smallnote">Pick <b>True</b> or <b>False</b>. Then flip the card to reveal the note.</div>
        </div>
      </div>

      <div class="face back">
        <div class="stamp">Back 🔎</div>
        <div class="subtitle"><b>{kind}</b></div>
        <div class="box">
          <div class="boxTitle">Note 📝</div>
          <div class="smallnote">{explanation}</div>
        </div>
        {discussion_html}
      </div>
    </div>
  </div>
</body>
</html>
"""

# Render it (this is the important fix)
components.html(card_html, height=380, scrolling=False)

# -----------------------------
# Controls
# -----------------------------
st.write("")
b1, b2 = st.columns(2)

with b1:
    if st.button("✅ True · ‘It holds up’", use_container_width=True, disabled=st.session_state.answered):
        submit("True")
        st.rerun()

with b2:
    if st.button("❌ False · ‘Not quite’", use_container_width=True, disabled=st.session_state.answered):
        submit("False")
        st.rerun()

if st.session_state.answered:
    if st.session_state.correct:
        st.success(f"Correct! ✅ The right answer is **{correct_answer}**.")
    else:
        st.error(f"Not quite. ❌ The right answer is **{correct_answer}**.")

cA, cB, cC = st.columns(3)

with cA:
    flip_label = "🔄 Flip card" if not st.session_state.flipped else "↩️ Unflip"
    if st.button(flip_label, use_container_width=True, disabled=not st.session_state.answered):
        st.session_state.flipped = not st.session_state.flipped
        st.rerun()

with cB:
    if st.button("✨ Reveal hint", use_container_width=True, disabled=st.session_state.answered or hard_mode):
        st.info(f"Hint: classification is **{card['label']}** (still answer yourself!)")

with cC:
    can_next = st.session_state.answered and st.session_state.flipped
    if st.button("➡️ Next card", use_container_width=True, disabled=not can_next):
        # log history
        st.session_state.history.append(
            {
                "n": n,
                "statement": card["statement"],
                "label": card["label"],
                "answer": correct_answer,
                "choice": st.session_state.choice,
                "correct": st.session_state.correct,
                "explanation": card["explanation"],
            }
        )
        # advance
        st.session_state.i += 1
        st.session_state.answered = False
        st.session_state.choice = None
        st.session_state.correct = None
        st.session_state.flipped = False
        st.rerun()

if not st.session_state.answered:
    st.info("Make your guess (True/False).")
elif st.session_state.answered and not st.session_state.flipped:
    st.info("Now flip the card to see the explanation + prompts.")
else:
    st.caption("Flip back to reread, or go next.")

st.markdown(
    """
<div style="opacity:0.75; margin-top: 18px; text-align:center; font-size:0.9rem;">
  Made for language nerds 💬 · Use “Practice wrong” for spaced repetition vibes.
</div>
""",
    unsafe_allow_html=True,
)
