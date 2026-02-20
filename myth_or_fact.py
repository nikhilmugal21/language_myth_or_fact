# app.py
# Enhanced Language Myths & Facts Flashcard Game - Visually Upgraded with Advanced Features
# Run: streamlit run app.py

import random
import base64
import html
import time
from typing import List, Dict, Optional

import streamlit as st
import streamlit.components.v1 as components

# -----------------------------
# Page config
# -----------------------------
st.set_page_config(
    page_title="🌍 LinguaCard - Language Myths & Facts",
    page_icon="🃏",
    layout="centered",
    initial_sidebar_state="expanded",
)

# -----------------------------
# Enhanced Data with more cards
# -----------------------------
CARDS: List[Dict] = [
    {
        "id": 1,
        "statement": "French is the most romantic language.",
        "label": "MYTH",
        "explanation": "'Romantic' refers to Romance languages derived from Latin — not emotional qualities. The perception of French as 'romantic' is a cultural stereotype, not a linguistic property.",
        "discussion": [
            "Why do certain languages get stereotyped as 'romantic' or 'harsh'?",
            "How much does media influence our perception of languages?",
            "What role does cultural association play in language perception?"
        ],
        "tags": ["stereotypes", "media", "romance languages"],
        "difficulty": "easy",
        "category": "sociolinguistics",
    },
    {
        "id": 2,
        "statement": "German has words that are impossible to translate.",
        "label": "MYTH",
        "explanation": "Any idea can be translated — sometimes using phrases instead of single words. Translation is about conveying meaning, not finding exact word equivalents.",
        "discussion": [
            "Does translation require word-for-word equivalence?",
            "Can cultural concepts be translated without losing nuance?",
            "What's the difference between translatable and untranslatable concepts?"
        ],
        "tags": ["translation", "meaning", "culture"],
        "difficulty": "medium",
        "category": "translation studies",
    },
    {
        "id": 3,
        "statement": "Sanskrit is the most scientific language in the world.",
        "label": "MYTH",
        "explanation": "All languages are rule-governed systems. No language is inherently more 'scientific.' Sanskrit has systematic grammar, but so do all natural languages.",
        "discussion": [
            "What do people usually mean by 'scientific language'?",
            "Is systematic grammar the same as scientific superiority?",
            "How do linguistic myths about ancient languages persist?"
        ],
        "tags": ["grammar", "myths", "linguistics"],
        "difficulty": "hard",
        "category": "historical linguistics",
    },
    {
        "id": 4,
        "statement": "African American English (AAE) is 'bad English.'",
        "label": "MYTH",
        "explanation": "AAE has consistent grammar and linguistic rules. It is a legitimate dialect with its own systematic patterns, not a deficient form of Standard English.",
        "discussion": [
            "Why are some dialects stigmatized?",
            "Who decides what counts as 'correct' English?",
            "How does linguistic prejudice affect speakers?"
        ],
        "tags": ["dialects", "prestige", "sociolinguistics"],
        "difficulty": "easy",
        "category": "sociolinguistics",
    },
    {
        "id": 5,
        "statement": "Babies can distinguish all speech sounds in the world at birth.",
        "label": "FACT",
        "explanation": "Infants initially perceive a wide range of phonetic contrasts but later specialize in their native language sounds through a process called 'perceptual narrowing.'",
        "discussion": [
            "Why does this ability narrow over time?",
            "What does this tell us about language acquisition?",
            "How might this affect second language learning?"
        ],
        "tags": ["phonetics", "acquisition", "development"],
        "difficulty": "medium",
        "category": "psycholinguistics",
    },
    {
        "id": 6,
        "statement": "Some languages have no word for 'blue.'",
        "label": "FACT",
        "explanation": "Some languages categorize colors differently and may not separate blue and green as distinct basic terms. The Himba people, for example, use one word for both blue and green.",
        "discussion": [
            "Does language influence perception of color?",
            "How does this relate to linguistic relativity?",
            "What are basic color terms and how do they evolve?"
        ],
        "tags": ["semantics", "color terms", "relativity"],
        "difficulty": "hard",
        "category": "cognitive linguistics",
    },
    {
        "id": 7,
        "statement": "Sign language is the same everywhere in the world.",
        "label": "MYTH",
        "explanation": "There are many distinct sign languages with their own grammars, vocabularies, and cultural variations. American Sign Language (ASL) is different from British Sign Language (BSL).",
        "discussion": [
            "Why do people assume sign languages are universal?",
            "What does this reveal about misconceptions about Deaf communities?",
            "How do sign languages develop and evolve?"
        ],
        "tags": ["sign languages", "deaf culture", "grammar"],
        "difficulty": "easy",
        "category": "sign linguistics",
    },
    {
        "id": 8,
        "statement": "Texting and social media are destroying language.",
        "label": "MYTH",
        "explanation": "Digital communication follows its own conventions and shows linguistic creativity. Young people adapt their language use to different contexts appropriately.",
        "discussion": [
            "Do you change how you write in different contexts?",
            "Is informal writing a threat to formal language skills?",
            "How does digital language show creativity?"
        ],
        "tags": ["digital language", "register", "creativity"],
        "difficulty": "easy",
        "category": "sociolinguistics",
    },
    {
        "id": 9,
        "statement": "Artificial languages like Esperanto can never become natural languages.",
        "label": "MYTH",
        "explanation": "While rare, artificial languages can become nativized. Some children have grown up speaking Esperanto as a native language, making it natural for them.",
        "discussion": [
            "What makes a language 'natural'?",
            "Can constructed languages evolve like natural ones?",
            "What happens when children learn constructed languages natively?"
        ],
        "tags": ["constructed languages", "acquisition", "evolution"],
        "difficulty": "hard",
        "category": "constructed languages",
    },
    {
        "id": 10,
        "statement": "Dolphins and whales have complex communication systems that could be considered languages.",
        "label": "FACT",
        "explanation": "Marine mammals have sophisticated communication systems with syntax-like properties, though whether they constitute 'language' depends on how we define language.",
        "discussion": [
            "What distinguishes human language from animal communication?",
            "Could animal communication systems be considered proto-languages?",
            "How do we study non-human communication?"
        ],
        "tags": ["animal communication", "syntax", "cognition"],
        "difficulty": "hard",
        "category": "biolinguistics",
    },
    {
        "id": 11,
        "statement": "There's only one correct English.",
        "label": "MYTH", 
        "explanation": "There are many valid varieties of English worldwide. Standard English is just one variety among many World Englishes, each with their own legitimate features.",
        "discussion": [
            "What is Standard English?",
            "Should schools teach only one variety?",
            "How do World Englishes differ from each other?"
        ],
        "tags": ["world englishes", "standard language", "education"],
        "difficulty": "medium",
        "category": "sociolinguistics",
    },
    {
        "id": 12,
        "statement": "Children today have smaller vocabularies than previous generations.",
        "label": "MYTH",
        "explanation": "Vocabulary shifts with cultural change; new domains create new words. Digital natives may know different words, not necessarily fewer words.",
        "discussion": [
            "Do digital environments create new lexical fields?",
            "How can vocabulary size be measured accurately?",
            "What factors influence vocabulary development?"
        ],
        "tags": ["lexicon", "change", "measurement"],
        "difficulty": "easy",
        "category": "developmental linguistics",
    }
]

# -----------------------------
# Enhanced Themes with more visual variety
# -----------------------------
THEMES = {
    "Aurora Borealis": {
        "bg": "radial-gradient(1200px 800px at 20% 10%, rgba(77,224,195,0.25), rgba(0,0,0,0) 60%),"
              "radial-gradient(900px 700px at 80% 20%, rgba(130,87,229,0.30), rgba(0,0,0,0) 60%),"
              "radial-gradient(1000px 700px at 60% 90%, rgba(255,122,182,0.18), rgba(0,0,0,0) 65%),"
              "linear-gradient(180deg, rgba(8,15,25,1), rgba(5,8,15,1))",
        "card": "linear-gradient(145deg, rgba(255,255,255,0.12), rgba(255,255,255,0.06))",
        "accent": "#7ee7d6",
        "accent_secondary": "#8257e5",
        "text_glow": "0 0 20px rgba(126,231,214,0.3)",
    },
    "Golden Hour": {
        "bg": "radial-gradient(900px 700px at 30% 20%, rgba(255,180,65,0.25), rgba(0,0,0,0) 65%),"
              "radial-gradient(900px 700px at 80% 60%, rgba(255,120,120,0.15), rgba(0,0,0,0) 60%),"
              "radial-gradient(700px 500px at 50% 80%, rgba(255,200,100,0.12), rgba(0,0,0,0) 55%),"
              "linear-gradient(180deg, #2d1810, #1a0f08)",
        "card": "linear-gradient(145deg, rgba(255,243,220,0.15), rgba(255,243,220,0.08))",
        "accent": "#ffb441",
        "accent_secondary": "#ff7878", 
        "text_glow": "0 0 20px rgba(255,180,65,0.3)",
    },
    "Deep Ocean": {
        "bg": "radial-gradient(1000px 800px at 25% 20%, rgba(65,150,255,0.22), rgba(0,0,0,0) 65%),"
              "radial-gradient(1000px 700px at 80% 80%, rgba(120,255,180,0.12), rgba(0,0,0,0) 65%),"
              "radial-gradient(800px 600px at 60% 40%, rgba(180,120,255,0.08), rgba(0,0,0,0) 55%),"
              "linear-gradient(180deg, #0a1320, #040810)",
        "card": "linear-gradient(145deg, rgba(255,255,255,0.1), rgba(255,255,255,0.05))",
        "accent": "#4196ff",
        "accent_secondary": "#78ffb4",
        "text_glow": "0 0 20px rgba(65,150,255,0.3)",
    },
    "Neon Synthwave": {
        "bg": "radial-gradient(900px 700px at 20% 30%, rgba(255,20,147,0.18), rgba(0,0,0,0) 60%),"
              "radial-gradient(800px 600px at 80% 70%, rgba(0,255,255,0.15), rgba(0,0,0,0) 60%),"
              "radial-gradient(1000px 800px at 50% 10%, rgba(138,43,226,0.12), rgba(0,0,0,0) 65%),"
              "linear-gradient(180deg, #1a0820, #0d0410)",
        "card": "linear-gradient(145deg, rgba(255,20,147,0.12), rgba(0,255,255,0.06))",
        "accent": "#ff1493",
        "accent_secondary": "#00ffff",
        "text_glow": "0 0 25px rgba(255,20,147,0.4)",
    },
}

# Enhanced Language SVG with more visual elements
LANG_SVG = r"""
<svg width="100%" height="100%" viewBox="0 0 900 140" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <filter id="glow">
      <feGaussianBlur stdDeviation="3" result="coloredBlur"/>
      <feMerge>
        <feMergeNode in="coloredBlur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
    <linearGradient id="main-grad" x1="0" x2="1">
      <stop offset="0" stop-color="rgba(126,231,214,1)"/>
      <stop offset="0.3" stop-color="rgba(130,87,229,1)"/>
      <stop offset="0.7" stop-color="rgba(255,122,182,1)"/>
      <stop offset="1" stop-color="rgba(255,180,65,1)"/>
    </linearGradient>
    <radialGradient id="circle-grad" cx="0.5" cy="0.5">
      <stop offset="0" stop-color="rgba(126,231,214,0.8)"/>
      <stop offset="0.5" stop-color="rgba(130,87,229,0.6)"/>
      <stop offset="1" stop-color="rgba(255,122,182,0.3)"/>
    </radialGradient>
  </defs>
  
  <g opacity="0.15">
    <circle cx="80" cy="60" r="45" fill="url(#circle-grad)"/>
    <circle cx="820" cy="50" r="40" fill="url(#circle-grad)"/>
    <circle cx="720" cy="102" r="30" fill="url(#circle-grad)"/>
    <circle cx="190" cy="108" r="25" fill="url(#circle-grad)"/>
    <circle cx="450" cy="30" r="20" fill="url(#circle-grad)"/>
    <circle cx="350" cy="115" r="18" fill="url(#circle-grad)"/>
  </g>
  
  <g filter="url(#glow)" opacity="0.95" fill="url(#main-grad)" font-family="ui-sans-serif, system-ui" font-weight="700">
    <text x="60" y="74" font-size="48">Aa</text>
    <text x="160" y="116" font-size="36">あ</text>
    <text x="240" y="74" font-size="44">أ</text>
    <text x="310" y="116" font-size="36">क</text>
    <text x="390" y="74" font-size="46">Ω</text>
    <text x="470" y="116" font-size="36">你</text>
    <text x="540" y="74" font-size="44">ß</text>
    <text x="620" y="116" font-size="36">ש</text>
    <text x="690" y="74" font-size="44">Σ</text>
    <text x="770" y="116" font-size="36">한</text>
  </g>
  
  <g opacity="0.25">
    <path d="M40 128 C140 116, 220 132, 320 120 C420 108, 500 132, 600 118 C700 104, 780 132, 860 120"
          fill="none" stroke="url(#main-grad)" stroke-width="2.5" stroke-dasharray="6 8"/>
    <path d="M60 15 C160 25, 240 12, 340 22 C440 32, 540 18, 640 28 C740 15, 820 25, 880 18"
          fill="none" stroke="url(#main-grad)" stroke-width="1.5" stroke-dasharray="4 6" opacity="0.6"/>
  </g>
  
  <g fill="url(#main-grad)" opacity="0.4">
    <circle cx="130" cy="25" r="2"/>
    <circle cx="280" cy="35" r="2"/>
    <circle cx="420" cy="20" r="2"/>
    <circle cx="580" cy="30" r="2"/>
    <circle cx="750" cy="25" r="2"/>
  </g>
</svg>
""".strip()

def svg_to_data_uri(svg: str) -> str:
    b64 = base64.b64encode(svg.encode("utf-8")).decode("utf-8")
    return f"data:image/svg+xml;base64,{b64}"

# -----------------------------
# Enhanced State Management
# -----------------------------
def is_fact(label: str) -> bool:
    return label.strip().upper() == "FACT"

def new_deck(mode: str, difficulty_filter: str = "all") -> List[int]:
    idxs = list(range(len(CARDS)))
    
    # Filter by difficulty if specified
    if difficulty_filter != "all":
        idxs = [i for i, card in enumerate(CARDS) if CARDS[i].get("difficulty", "easy") == difficulty_filter]
    
    if mode == "Shuffle":
        random.shuffle(idxs)
    
    return idxs

def init_game(mode: str, difficulty: str = "all"):
    st.session_state.deck = new_deck(mode, difficulty)
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
    st.session_state.start_time = time.time()

def get_card() -> Optional[Dict]:
    if st.session_state.i >= len(st.session_state.deck):
        return None
    return CARDS[st.session_state.deck[st.session_state.i]]

def get_achievement_level(score: int, total: int) -> str:
    percentage = score / max(total, 1) * 100
    if percentage >= 95: return "🏆 Linguistics Master"
    elif percentage >= 85: return "🥇 Language Expert"
    elif percentage >= 75: return "🥈 Myth Buster"
    elif percentage >= 60: return "🥉 Language Learner"
    else: return "📚 Getting Started"

# -----------------------------
# Initialize Enhanced Session State
# -----------------------------
if "theme" not in st.session_state:
    st.session_state.theme = "Aurora Borealis"
if "mode" not in st.session_state:
    st.session_state.mode = "Shuffle"
if "difficulty" not in st.session_state:
    st.session_state.difficulty = "all"
if "deck" not in st.session_state:
    init_game(st.session_state.mode, st.session_state.difficulty)
if "animations_enabled" not in st.session_state:
    st.session_state.animations_enabled = True

# -----------------------------
# Enhanced Sidebar Controls
# -----------------------------
st.sidebar.markdown("""
<div style="text-align: center; margin-bottom: 20px;">
    <h2 style="color: #7ee7d6; text-shadow: 0 0 10px rgba(126,231,214,0.3);">🎛️ Control Panel</h2>
</div>
""", unsafe_allow_html=True)

# Theme selection
st.session_state.theme = st.sidebar.selectbox(
    "🎨 Visual Theme", 
    list(THEMES.keys()),
    index=list(THEMES.keys()).index(st.session_state.theme),
    help="Choose your preferred visual theme"
)

# Game mode options
st.session_state.mode = st.sidebar.radio(
    "🃏 Card Order", 
    ["Shuffle", "In order"],
    index=0 if st.session_state.mode == "Shuffle" else 1,
    help="How cards are presented"
)

# Difficulty filter
st.session_state.difficulty = st.sidebar.selectbox(
    "⚡ Difficulty Level", 
    ["all", "easy", "medium", "hard"],
    index=["all", "easy", "medium", "hard"].index(st.session_state.difficulty),
    help="Filter cards by difficulty level"
)

st.sidebar.divider()

# Enhanced toggles
col1, col2 = st.sidebar.columns(2)
with col1:
    show_discussion = st.toggle("💬 Discussions", value=True)
    show_tags = st.toggle("🏷️ Topic chips", value=True)
    
with col2:
    hard_mode = st.toggle("🔥 Hard mode", value=False)
    st.session_state.animations_enabled = st.toggle("✨ Animations", value=True)

st.sidebar.divider()

# Action buttons
btn1, btn2 = st.sidebar.columns(2)
with btn1:
    if st.button("🔄 New Game", use_container_width=True):
        init_game(st.session_state.mode, st.session_state.difficulty)
        st.rerun()

with btn2:
    if st.button("🎯 Practice", use_container_width=True):
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

# Statistics
if st.session_state.history:
    total_played = len(st.session_state.history)
    correct_answers = sum(1 for h in st.session_state.history if h["correct"])
    accuracy = (correct_answers / total_played) * 100
    
    st.sidebar.markdown("### 📊 Session Stats")
    st.sidebar.metric("Accuracy", f"{accuracy:.1f}%")
    st.sidebar.metric("Total Cards", total_played)
    st.sidebar.metric("Best Streak", st.session_state.best_streak)

# -----------------------------
# Enhanced Global Styling
# -----------------------------
theme = THEMES[st.session_state.theme]
banner_uri = svg_to_data_uri(LANG_SVG)

st.markdown(
    f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

:root {{
    --primary-accent: {theme["accent"]};
    --secondary-accent: {theme["accent_secondary"]};
    --text-glow: {theme["text_glow"]};
}}

.stApp {{
    background: {theme["bg"]};
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
}}

.block-container {{
    padding-top: 1rem;
    max-width: 900px;
}}

.lang-banner {{
    width: 100%;
    height: 140px;
    border-radius: 24px;
    overflow: hidden;
    border: 1px solid rgba(255,255,255,0.15);
    box-shadow: 
        0 20px 60px rgba(0,0,0,0.3),
        inset 0 1px 0 rgba(255,255,255,0.1);
    background: rgba(255,255,255,0.04);
    position: relative;
    margin-bottom: 1.5rem;
}}

.lang-banner::before {{
    content: '';
    position: absolute;
    inset: 0;
    background: linear-gradient(135deg, 
        rgba(255,255,255,0.1) 0%, 
        rgba(255,255,255,0.05) 50%, 
        rgba(255,255,255,0.02) 100%);
    pointer-events: none;
}}

div.stButton > button {{
    border-radius: 18px !important;
    padding: 0.9rem 1.2rem !important;
    border: 1px solid rgba(255,255,255,0.18) !important;
    background: rgba(255,255,255,0.08) !important;
    box-shadow: 
        0 12px 35px rgba(0,0,0,0.25),
        inset 0 1px 0 rgba(255,255,255,0.1) !important;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
    font-weight: 600 !important;
    font-size: 0.95rem !important;
    backdrop-filter: blur(10px) !important;
}}

div.stButton > button:hover {{
    background: rgba(255,255,255,0.12) !important;
    transform: translateY(-2px) !important;
    box-shadow: 
        0 16px 45px rgba(0,0,0,0.3),
        inset 0 1px 0 rgba(255,255,255,0.15) !important;
}}

div.stButton > button:active {{
    transform: translateY(0) !important;
    box-shadow: 
        0 8px 25px rgba(0,0,0,0.2),
        inset 0 1px 0 rgba(255,255,255,0.1) !important;
}}

.stProgress > div > div > div > div {{
    background: linear-gradient(90deg, var(--primary-accent), var(--secondary-accent)) !important;
    border-radius: 10px !important;
    box-shadow: 0 0 20px rgba(126,231,214,0.3) !important;
}}

div[data-testid="metric-container"] {{
    background: rgba(255,255,255,0.06);
    border: 1px solid rgba(255,255,255,0.12);
    border-radius: 16px;
    padding: 1rem;
    backdrop-filter: blur(10px);
    box-shadow: 0 8px 25px rgba(0,0,0,0.15);
}}

div[data-testid="metric-container"] > label {{
    font-weight: 600 !important;
    color: rgba(255,255,255,0.8) !important;
}}

div[data-testid="metric-container"] > div {{
    color: var(--primary-accent) !important;
    font-weight: 700 !important;
    text-shadow: var(--text-glow) !important;
}}

.stSuccess, .stError, .stInfo {{
    border-radius: 12px !important;
    border: none !important;
    backdrop-filter: blur(10px) !important;
}}

.stSuccess {{
    background: rgba(76, 175, 80, 0.15) !important;
    border-left: 4px solid #4caf50 !important;
}}

.stError {{
    background: rgba(244, 67, 54, 0.15) !important;
    border-left: 4px solid #f44336 !important;
}}

.stInfo {{
    background: rgba(33, 150, 243, 0.15) !important;
    border-left: 4px solid #2196f3 !important;
}}

.fade-in {{
    animation: fadeIn 0.5s ease-in-out;
}}

@keyframes fadeIn {{
    from {{ opacity: 0; transform: translateY(20px); }}
    to {{ opacity: 1; transform: translateY(0); }}
}}

.pulse {{
    animation: pulse 2s infinite;
}}

@keyframes pulse {{
    0% {{ transform: scale(1); }}
    50% {{ transform: scale(1.05); }}
    100% {{ transform: scale(1); }}
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

st.title("🌍 LinguaCard - Language Myths & Facts")
st.caption("🎯 Choose **True** or **False**, then **flip** to reveal explanations and discussion prompts.")

# -----------------------------
# Game Logic
# -----------------------------
card = get_card()
if card is None:
    # Game complete screen
    total = len(st.session_state.deck)
    elapsed_time = time.time() - st.session_state.start_time
    minutes = int(elapsed_time // 60)
    seconds = int(elapsed_time % 60)
    achievement = get_achievement_level(st.session_state.score, total)
    
    st.success(f"🎉 **Game Complete!** {achievement}")
    
    # Results display
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Final Score", f"{st.session_state.score}/{total}")
    with col2:
        percentage = (st.session_state.score / total) * 100
        st.metric("Accuracy", f"{percentage:.1f}%")
    with col3:
        st.metric("Best Streak", f"{st.session_state.best_streak} 🔥")
    with col4:
        st.metric("Time", f"{minutes}:{seconds:02d}")
    
    with st.expander("📋 Review Your Session", expanded=False):
        for h in st.session_state.history:
            icon = "✅" if h["correct"] else "❌"*
