# app.py
# Streamlit flashcard game: "Guess: Myth or Fact? (Languages Edition)" — visually upgraded
# Run: streamlit run app.py

import random
import textwrap
import time
import base64
from dataclasses import dataclass
from typing import List, Dict

import streamlit as st

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
        "statement": "African American English (AAE) is “bad English.”",
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
        "statement": "Some languages have no word for “blue.”",
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
# Theme + visuals
# -----------------------------
THEMES = {
    "Aurora Night": {
        "bg": "radial-gradient(1200px 800px at 20% 10%, rgba(77,224,195,0.18), rgba(0,0,0,0) 55%),"
              "radial-gradient(900px 700px at 80% 20%, rgba(130,87,229,0.20), rgba(0,0,0,0) 55%),"
              "radial-gradient(1000px 700px at 60% 90%, rgba(255,122,182,0.12), rgba(0,0,0,0) 60%),"
              "linear-gradient(180deg, rgba(10,12,18,1), rgba(7,9,14,1))",
        "card": "linear-gradient(180deg, rgba(255,255,255,0.08), rgba(255,255,255,0.04))",
        "accent": "#7ee7d6",
    },
    "Vintage Paper": {
        "bg": "radial-gradient(900px 700px at 30% 20%, rgba(255,216,155,0.20), rgba(0,0,0,0) 60%),"
              "radial-gradient(900px 700px at 80% 60%, rgba(255,170,170,0.10), rgba(0,0,0,0) 55%),"
              "linear-gradient(180deg, #1b1a17, #12110f)",
        "card": "linear-gradient(180deg, rgba(255,243,220,0.10), rgba(255,243,220,0.05))",
        "accent": "#ffd89b",
    },
    "Midnight Ink": {
        "bg": "radial-gradient(1000px 800px at 25% 20%, rgba(90,161,255,0.18), rgba(0,0,0,0) 60%),"
              "radial-gradient(1000px 700px at 80% 80%, rgba(255,196,90,0.10), rgba(0,0,0,0) 60%),"
              "linear-gradient(180deg, #0a0f1f, #070a12)",
        "card": "linear-gradient(180deg, rgba(255,255,255,0.07), rgba(255,255,255,0.035))",
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

  <!-- Floating glyph bubbles -->
  <g opacity="0.20">
    <circle cx="80" cy="60" r="40" fill="url(#g)"/>
    <circle cx="820" cy="50" r="36" fill="url(#g)"/>
    <circle cx="720" cy="102" r="26" fill="url(#g)"/>
    <circle cx="190" cy="108" r="22" fill="url(#g)"/>
  </g>

  <!-- Icon-ish letters -->
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

  <!-- Subtle dotted baseline -->
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
# Helpers
# -----------------------------
def is_true_answer(card_label: str) -> bool:
    return card_label.strip().upper() == "FACT"

def wrap(s: str, width: int = 86) -> str:
    return "\n".join(textwrap.wrap(s, width=width))

def new_order(mode: str) -> List[int]:
    idxs = list(range(len(CARDS)))
    if mode == "Shuffle":
        random.shuffle(idxs)
    return idxs

def reset_round(mode: str = "Shuffle"):
    st.session_state.order = new_order(mode)
    st.session_state.idx = 0
    st.session_state.score = 0
    st.session_state.streak = 0
    st.session_state.best_streak = 0
    st.session_state.answered = False
    st.session_state.user_choice = None
    st.session_state.is_correct = None
    st.session_state.flipped = False
    st.session_state.history = []  # per-card outcome
    st.session_state.wrong_ids = set()

def current_card():
    if st.session_state.idx >= len(st.session_state.order):
        return None
    return CARDS[st.session_state.order[st.session_state.idx]]

def award_title(score: int, total: int) -> str:
    pct = (score / total) * 100 if total else 0
    if pct >= 90:
        return "🏆 Linguistics Wizard"
    if pct >= 75:
        return "🎓 Language Sleuth"
    if pct >= 55:
        return "🧭 Curious Communicator"
    return "🌱 Myth-Hunter in Training"

# -----------------------------
# Session init
# -----------------------------
if "order" not in st.session_state:
    reset_round(mode="Shuffle")

if "theme_name" not in st.session_state:
    st.session_state.theme_name = "Aurora Night"

if "mode" not in st.session_state:
    st.session_state.mode = "Shuffle"

# -----------------------------
# Sidebar (controls + personalization)
# -----------------------------
st.sidebar.title("🎛️ Control Panel")

st.session_state.theme_name = st.sidebar.selectbox(
    "Theme",
    list(THEMES.keys()),
    index=list(THEMES.keys()).index(st.session_state.theme_name),
)

st.session_state.mode = st.sidebar.radio(
    "Deck order",
    ["Shuffle", "In order"],
    index=0 if st.session_state.mode == "Shuffle" else 1,
    help="Shuffle is best for replayability. In order matches your original list.",
)

show_discussion = st.sidebar.toggle("Show discussion starters", value=True)
show_tag_chips = st.sidebar.toggle("Show topic chips", value=True)
hard_mode = st.sidebar.toggle("Hard mode (no hints)", value=False, help="Hides MYTH/FACT hints until after flipping.")
sound_fx = st.sidebar.toggle("Tiny sound effect (simple)", value=False, help="Plays a very small audio beep on reveal.")

st.sidebar.divider()

col_r1, col_r2 = st.sidebar.columns(2)
with col_r1:
    if st.button("🔄 Restart", use_container_width=True):
        reset_round(mode=st.session_state.mode)
        st.rerun()
with col_r2:
    if st.button("🎯 Practice wrong", use_container_width=True, help="After you miss some, practice only those."):
        # If no wrong answers yet, just keep normal.
        if st.session_state.wrong_ids:
            # Build order from wrong ids (keep it shuffled for practice)
            wrong_idxs = [i for i, c in enumerate(CARDS) if c["id"] in st.session_state.wrong_ids]
            random.shuffle(wrong_idxs)
            st.session_state.order = wrong_idxs
            st.session_state.idx = 0
            st.session_state.score = 0
            st.session_state.streak = 0
            st.session_state.answered = False
            st.session_state.flipped = False
            st.session_state.history = []
        st.rerun()

st.sidebar.divider()

st.sidebar.caption("Tip: Answer first → flip → next. The flip reveals the learning moment.")

# -----------------------------
# Global styling (artistic background + card templates + buttons)
# -----------------------------
theme = THEMES[st.session_state.theme_name]
lang_banner_uri = svg_to_data_uri(LANG_SVG)

st.markdown(
    f"""
<style>
/* App background */
.stApp {{
    background: {theme["bg"]};
}}

/* Narrow the content and soften typography */
.block-container {{
    padding-top: 1.1rem;
    max-width: 820px;
}}

/* Top banner graphic container */
.lang-banner {{
    width: 100%;
    height: 120px;
    border-radius: 20px;
    overflow: hidden;
    border: 1px solid rgba(255,255,255,0.10);
    box-shadow: 0 14px 40px rgba(0,0,0,0.25);
    background: rgba(255,255,255,0.03);
}}

/* Flashcard stage */
.stage {{
    perspective: 1200px;
    margin-top: 6px;
}}

/* Flashcard base */
.card {{
    position: relative;
    width: 100%;
    min-height: 320px;
    border-radius: 22px;
    transform-style: preserve-3d;
    transition: transform 0.75s cubic-bezier(.2,.8,.2,1);
    border: 1px solid rgba(255,255,255,0.12);
    box-shadow: 0 22px 70px rgba(0,0,0,0.35);
    background: {theme["card"]};
}}

/* “Flipped” state */
.card.flipped {{
    transform: rotateY(180deg);
}}

/* Front/back faces */
.face {{
    position: absolute;
    inset: 0;
    backface-visibility: hidden;
    border-radius: 22px;
    padding: 18px 18px 16px 18px;
    overflow: hidden;
}}

.back {{
    transform: rotateY(180deg);
}}

/* Decorative corner stamps */
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
    opacity: 0.80;
    font-size: 0.96rem;
    margin-top: 6px;
}}

.statement {{
    font-size: 1.55rem;
    line-height: 1.22;
    margin-top: 14px;
    margin-bottom: 14px;
}}

.smallnote {{
    opacity: 0.85;
    font-size: 0.95rem;
    line-height: 1.35;
}}

.rulebox {{
    margin-top: 10px;
    padding: 12px 12px;
    border-radius: 16px;
    border: 1px solid rgba(255,255,255,0.14);
    background: rgba(0,0,0,0.16);
}}

/* “Chips” for tags */
.chips {{
    display:flex;
    flex-wrap: wrap;
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
    background: {theme["accent"]};
    box-shadow: 0 0 12px rgba(255,255,255,0.12);
}}

/* Button styling: make Streamlit buttons feel “game-y” */
div.stButton > button {{
    border-radius: 16px !important;
    padding: 0.85rem 1rem !important;
    border: 1px solid rgba(255,255,255,0.14) !important;
    background: rgba(255,255,255,0.06) !important;
    box-shadow: 0 10px 30px rgba(0,0,0,0.25) !important;
    transition: transform .06s ease-in-out, background .2s ease-in-out;
}}
div.stButton > button:hover {{
    transform: translateY(-1px);
    background: rgba(255,255,255,0.09) !important;
}}
div.stButton > button:active {{
    transform: translateY(0px) scale(0.99);
}}

/* Progress bar look */
.stProgress > div > div > div {{
    border-radius: 999px;
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
  <img src="{lang_banner_uri}" style="width:100%; height:100%; object-fit:cover;" />
</div>
""",
    unsafe_allow_html=True,
)

st.title("🃏 Myth or Fact? — Languages Flashcards")
st.caption("Choose **True** or **False**, then **flip** to reveal the explanation + discussion prompts.")

# -----------------------------
# Game state
# -----------------------------
card = current_card()
total = len(st.session_state.order)

# End screen
if card is None:
    score = st.session_state.score
    title = award_title(score, total)
    st.success(f"Finished! **{title}** — Score: **{score}/{total}**")
    st.write(f"🔥 Best streak: **{st.session_state.best_streak}**")

    with st.expander("📋 Review", expanded=False):
        for h in st.session_state.history:
            icon = "✅" if h["is_correct"] else "❌"
            st.markdown(
                f"""
**{h['n']}. “{h['statement']}”** {icon}  
- Correct: **{h['correct_answer']}** ({h['label']})  
- You chose: **{h['user_choice']}**  
- Note: {h['explanation']}
"""
            )

    c1, c2 = st.columns(2)
    with c1:
        if st.button("🔁 Play again", use_container_width=True):
            reset_round(mode=st.session_state.mode)
            st.rerun()
    with c2:
        # Export the session review as a lightweight text log
        export_lines = []
        for h in st.session_state.history:
            export_lines.append(
                f'{h["n"]}. {h["statement"]}\n'
                f'   Correct: {h["correct_answer"]} ({h["label"]}) | You: {h["user_choice"]}\n'
                f'   Note: {h["explanation"]}\n'
            )
        st.download_button(
            "⬇️ Download session log",
            data="\n".join(export_lines).encode("utf-8"),
            file_name="myth_fact_session_log.txt",
            mime="text/plain",
            use_container_width=True,
        )
    st.stop()

# Progress + scoreboard
i1 = st.session_state.idx + 1
progress_ratio = (i1 - 1) / total if total else 0

top1, top2, top3 = st.columns([1.25, 1, 1])
with top1:
    st.progress(progress_ratio, text=f"Card {i1} of {total}")
with top2:
    st.metric("Score", f"{st.session_state.score}/{i1-1 if i1>0 else 0}")
with top3:
    st.metric("Streak", f"{st.session_state.streak} 🔥")

# -----------------------------
# Answer logic
# -----------------------------
truth = is_true_answer(card["label"])
correct_answer_text = "True" if truth else "False"

def answer(choice: str):
    st.session_state.answered = True
    st.session_state.user_choice = choice
    user_true = (choice == "True")
    st.session_state.is_correct = (user_true == truth)

    if st.session_state.is_correct:
        st.session_state.score += 1
        st.session_state.streak += 1
        st.session_state.best_streak = max(st.session_state.best_streak, st.session_state.streak)
        # tiny delight
        st.toast("Nice! ✅", icon="✨")
        st.balloons()
    else:
        st.session_state.streak = 0
        st.session_state.wrong_ids.add(card["id"])
        st.toast("Oof—flip to learn. ❌", icon="🧠")

# -----------------------------
# Flashcard HTML (3D flip)
# -----------------------------
front_hint = "Decide if the statement is true."
if not hard_mode:
    front_hint += " (Hint: some are FACT, most are MYTH.)"

# Provide a subtle label on the back for learning
back_kind = "FACT ✅" if card["label"].upper() == "FACT" else "MYTH 🚫"

# Optional tiny sound (base64 wav beep)
BEEP_WAV_B64 = (
    "UklGRhQAAABXQVZFZm10IBAAAAABAAEARKwAABCxAgAEABAAZGF0YQAAAAA="
)
beep_audio_html = ""
if sound_fx and st.session_state.flipped:
    beep_audio_html = f"""
    <audio autoplay>
      <source src="data:audio/wav;base64,{BEEP_WAV_B64}" type="audio/wav">
    </audio>
    """

flipped_class = "flipped" if st.session_state.flipped else ""
chips_html = ""
if show_tag_chips and card.get("tags"):
    chips = "".join([f'<span class="chip"><span class="dot"></span>{t}</span>' for t in card["tags"]])
    chips_html = f'<div class="chips">{chips}</div>'

discussion_html = ""
if show_discussion and card.get("discussion"):
    items = "".join([f"<li>{q}</li>" for q in card["discussion"]])
    discussion_html = f"""
    <div class="rulebox" style="margin-top:12px;">
      <div style="font-weight:700; margin-bottom:6px;">Discussion starters 💬</div>
      <ul style="margin:0; padding-left: 18px;">{items}</ul>
    </div>
    """

st.markdown(
    f"""
{beep_audio_html}
<div class="stage">
  <div class="card {flipped_class}">
    <div class="face front">
      <div class="stamp">Front 🧩</div>
      <div class="subtitle">🎯 GUESS: Myth or Fact?</div>
      <div class="statement">“{card["statement"]}”</div>
      <div class="smallnote">{front_hint}</div>
      {chips_html}
      <div class="rulebox" style="margin-top:14px;">
        <div style="font-weight:700; margin-bottom:6px;">How to play</div>
        <div class="smallnote">Pick <b>True</b> or <b>False</b>. Then flip the card to reveal the note.</div>
      </div>
    </div>

    <div class="face back">
      <div class="stamp">Back 🔎</div>
      <div class="subtitle"><b>{back_kind}</b></div>
      <div class="statement" style="font-size:1.15rem; margin-top:10px;">
        Note 📝
      </div>
      <div class="rulebox">
        <div class="smallnote">{card["explanation"]}</div>
      </div>
      {discussion_html}
    </div>
  </div>
</div>
""",
    unsafe_allow_html=True,
)

# -----------------------------
# Buttons (visual + interactive)
# -----------------------------
st.write("")  # spacing

a1, a2 = st.columns(2)
with a1:
    if st.button("✅ True  ·  ‘It holds up’", use_container_width=True, disabled=st.session_state.answered):
        answer("True")
        st.rerun()
with a2:
    if st.button("❌ False  ·  ‘Not quite’", use_container_width=True, disabled=st.session_state.answered):
        answer("False")
        st.rerun()

# Feedback bar
if st.session_state.answered:
    if st.session_state.is_correct:
        st.success(f"Correct! ✅ The right answer is **{correct_answer_text}**.")
    else:
        st.error(f"Not quite. ❌ The right answer is **{correct_answer_text}**.")

# Flip / Next controls
b1, b2, b3 = st.columns([1, 1, 1])

with b1:
    flip_label = "🔄 Flip card" if not st.session_state.flipped else "↩️ Unflip"
    if st.button(flip_label, use_container_width=True, disabled=not st.session_state.answered):
        st.session_state.flipped = not st.session_state.flipped
        st.rerun()

with b2:
    if st.button("✨ Reveal hint", use_container_width=True, disabled=st.session_state.answered or hard_mode):
        st.info(f"Hint: the correct classification is **{card['label']}**. (Still answer yourself!)")

with b3:
    can_next = st.session_state.answered and st.session_state.flipped
    if st.button("➡️ Next card", use_container_width=True, disabled=not can_next):
        # Save to history
        st.session_state.history.append(
            {
                "n": i1,
                "statement": card["statement"],
                "label": card["label"],
                "correct_answer": correct_answer_text,
                "user_choice": st.session_state.user_choice,
                "is_correct": st.session_state.is_correct,
                "explanation": card["explanation"],
            }
        )

        # Advance + reset per-card state
        st.session_state.idx += 1
        st.session_state.answered = False
        st.session_state.user_choice = None
        st.session_state.is_correct = None
        st.session_state.flipped = False
        st.rerun()

# Gentle guidance
if not st.session_state.answered:
    st.info("Make your guess (True/False).")
elif st.session_state.answered and not st.session_state.flipped:
    st.info("Now flip the card to see the explanation and prompts.")
else:
    st.caption("Flip back if you want to reread, or go next.")

# Footer micro-easter egg
st.markdown(
    """
<div style="opacity:0.75; margin-top: 18px; text-align:center; font-size:0.9rem;">
  Made for language nerds 💬 · Try “Practice wrong” after a run for spaced repetition vibes.
</div>
""",
    unsafe_allow_html=True,
)
