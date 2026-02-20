import random
import time
from typing import Dict, List, Optional

import streamlit as st

st.set_page_config(
    page_title="🎯 Guess: Myth or Fact?",
    page_icon="🌍",
    layout="centered",
    initial_sidebar_state="expanded",
)

CARDS: List[Dict[str, object]] = [
    {
        "id": 1,
        "statement": "French is the most romantic language.",
        "label": "MYTH",
        "explanation": "‘Romantic’ refers to Romance languages derived from Latin, not emotional qualities. The idea that French is inherently more romantic is a cultural stereotype.",
        "discussion": [
            "Why do certain languages get stereotyped as ‘romantic’ or ‘harsh’?",
            "How much does media influence our perception of languages?",
        ],
        "difficulty": "easy",
    },
    {
        "id": 2,
        "statement": "German has words that are impossible to translate.",
        "label": "MYTH",
        "explanation": "Any idea can be translated, though sometimes with a phrase instead of a single word. Translation is about meaning, not strict word-for-word matching.",
        "discussion": [
            "Does translation require word-for-word equivalence?",
            "Can cultural concepts be translated without losing nuance?",
        ],
        "difficulty": "medium",
    },
    {
        "id": 3,
        "statement": "Sanskrit is the most scientific language in the world.",
        "label": "MYTH",
        "explanation": "All languages are systematic and rule-governed. No language is inherently more scientific or superior than another.",
        "discussion": [
            "What do people usually mean by ‘scientific language’?",
            "Is systematic grammar the same as scientific superiority?",
        ],
        "difficulty": "hard",
    },
    {
        "id": 4,
        "statement": "African American English (AAE) is ‘bad English.’",
        "label": "MYTH",
        "explanation": "AAE has consistent grammar and linguistic patterns. It is a legitimate dialect, not incorrect English.",
        "discussion": [
            "Why are some dialects stigmatized?",
            "Who decides what counts as ‘correct’ English?",
        ],
        "difficulty": "easy",
    },
    {
        "id": 5,
        "statement": "Hindi and Urdu are completely different languages.",
        "label": "MYTH",
        "explanation": "In everyday speech, Hindi and Urdu are largely mutually intelligible. They differ mainly in script and formal vocabulary choices.",
        "discussion": [
            "What makes two varieties separate languages rather than dialects?",
            "Is the distinction linguistic or political?",
        ],
        "difficulty": "medium",
    },
    {
        "id": 6,
        "statement": "Sign language is the same everywhere in the world.",
        "label": "MYTH",
        "explanation": "There are many different sign languages, each with its own grammar and lexicon. ASL and BSL, for example, are not mutually intelligible.",
        "discussion": [
            "Why do people assume sign languages are universal?",
            "What does this reveal about misconceptions about Deaf communities?",
        ],
        "difficulty": "easy",
    },
    {
        "id": 7,
        "statement": "English will eventually replace all other languages.",
        "label": "MYTH",
        "explanation": "Language survival depends on community identity, policy, and intergenerational transmission. Multilingualism is the global norm.",
        "discussion": [
            "Is multilingualism the global norm?",
            "What factors actually cause language death?",
        ],
        "difficulty": "medium",
    },
    {
        "id": 8,
        "statement": "Shakespeare used perfect English.",
        "label": "MYTH",
        "explanation": "Shakespeare experimented with English creatively and extensively. His language reflects change and innovation, not an absolute perfect standard.",
        "discussion": [
            "Why do we treat older forms of language as ‘purer’?",
            "Is there such a thing as perfect grammar?",
        ],
        "difficulty": "medium",
    },
    {
        "id": 9,
        "statement": "Dictionaries decide what’s correct.",
        "label": "MYTH",
        "explanation": "Most dictionaries describe actual usage patterns. They document language; they do not single-handedly create it.",
        "discussion": [
            "What is the difference between prescriptive and descriptive grammar?",
            "Should dictionaries influence language use?",
        ],
        "difficulty": "easy",
    },
    {
        "id": 10,
        "statement": "Texting and social media are destroying language.",
        "label": "MYTH",
        "explanation": "Digital communication has its own conventions and creativity. People generally switch register effectively across informal and formal contexts.",
        "discussion": [
            "Do you change how you write in different contexts?",
            "Is informal writing a threat to formal language skills?",
        ],
        "difficulty": "easy",
    },
    {
        "id": 11,
        "statement": "There’s only one correct English.",
        "label": "MYTH",
        "explanation": "There are many valid Englishes globally. Standard English is one socially privileged variety among many.",
        "discussion": [
            "What is Standard English?",
            "Should schools teach only one variety?",
        ],
        "difficulty": "easy",
    },
    {
        "id": 12,
        "statement": "Babies can distinguish all speech sounds in the world at birth.",
        "label": "FACT",
        "explanation": "Infants initially perceive a broad range of phonetic contrasts, then specialize based on the sound patterns they hear most in their environment.",
        "discussion": [
            "Why does this ability narrow over time?",
            "What does this tell us about language acquisition?",
        ],
        "difficulty": "hard",
    },
    {
        "id": 13,
        "statement": "Some languages have no word for ‘blue.’",
        "label": "FACT",
        "explanation": "Languages categorize colors differently. Some do not separate blue and green into distinct basic color terms.",
        "discussion": [
            "Does language influence perception of color?",
            "How does this relate to linguistic relativity?",
        ],
        "difficulty": "hard",
    },
    {
        "id": 14,
        "statement": "Children today have a smaller vocabulary than previous generations.",
        "label": "MYTH",
        "explanation": "Vocabulary changes with social and technological change. New domains create new lexical knowledge rather than simply reducing it.",
        "discussion": [
            "Do digital environments create new lexical fields?",
            "How can vocabulary size be measured accurately?",
        ],
        "difficulty": "medium",
    },
]

THEMES = {
    "Aurora": {
        "bg": "linear-gradient(145deg, #0f172a 0%, #1e1b4b 50%, #052e2b 100%)",
        "accent": "#7dd3fc",
        "accent2": "#c4b5fd",
    },
    "Sunset": {
        "bg": "linear-gradient(145deg, #2e1065 0%, #7c2d12 45%, #451a03 100%)",
        "accent": "#fcd34d",
        "accent2": "#fda4af",
    },
    "Ocean": {
        "bg": "linear-gradient(145deg, #082f49 0%, #0f766e 50%, #111827 100%)",
        "accent": "#67e8f9",
        "accent2": "#86efac",
    },
}


if "theme" not in st.session_state:
    st.session_state.theme = "Aurora"
if "order" not in st.session_state:
    st.session_state.order = "Shuffle"
if "difficulty" not in st.session_state:
    st.session_state.difficulty = "all"
if "deck" not in st.session_state:
    st.session_state.deck = []
if "i" not in st.session_state:
    st.session_state.i = 0
if "score" not in st.session_state:
    st.session_state.score = 0
if "answered" not in st.session_state:
    st.session_state.answered = False
if "choice" not in st.session_state:
    st.session_state.choice = None
if "is_correct" not in st.session_state:
    st.session_state.is_correct = None
if "flipped" not in st.session_state:
    st.session_state.flipped = False
if "start_time" not in st.session_state:
    st.session_state.start_time = time.time()


def build_deck(order: str, difficulty: str) -> List[int]:
    idxs = [i for i, c in enumerate(CARDS) if difficulty == "all" or c["difficulty"] == difficulty]
    if order == "Shuffle":
        random.shuffle(idxs)
    return idxs


def new_game() -> None:
    st.session_state.deck = build_deck(st.session_state.order, st.session_state.difficulty)
    st.session_state.i = 0
    st.session_state.score = 0
    st.session_state.answered = False
    st.session_state.choice = None
    st.session_state.is_correct = None
    st.session_state.flipped = False
    st.session_state.start_time = time.time()


if not st.session_state.deck:
    new_game()


current_theme = THEMES[st.session_state.theme]
st.markdown(
    f"""
    <style>
    .stApp {{
        background: {current_theme['bg']};
        color: #f8fafc;
    }}
    .title-card {{
        background: rgba(255,255,255,0.08);
        border: 1px solid rgba(255,255,255,0.24);
        border-radius: 22px;
        padding: 1rem 1.3rem;
        margin-bottom: 1rem;
        box-shadow: 0 15px 35px rgba(0,0,0,0.25);
    }}
    .flashcard {{
        background: rgba(255,255,255,0.09);
        border: 1px solid rgba(255,255,255,0.22);
        border-radius: 22px;
        padding: 1.1rem 1.2rem;
        box-shadow: 0 18px 38px rgba(0,0,0,0.25);
    }}
    .chip {{
        display:inline-block;
        padding: .25rem .65rem;
        border-radius: 999px;
        font-weight: 700;
        font-size: .78rem;
    }}
    .chip-myth {{background: rgba(251,113,133,.22); border: 1px solid rgba(251,113,133,.65);}}
    .chip-fact {{background: rgba(74,222,128,.22); border: 1px solid rgba(74,222,128,.65);}}
    .subtle {{color: #e2e8f0; opacity: .95;}}
    </style>
    """,
    unsafe_allow_html=True,
)

st.sidebar.markdown("## ⚙️ Game Options")
st.session_state.theme = st.sidebar.selectbox("Theme", list(THEMES.keys()), index=list(THEMES.keys()).index(st.session_state.theme))
st.session_state.order = st.sidebar.radio("Card order", ["Shuffle", "In order"], index=0 if st.session_state.order == "Shuffle" else 1)
st.session_state.difficulty = st.sidebar.selectbox("Difficulty", ["all", "easy", "medium", "hard"], index=["all", "easy", "medium", "hard"].index(st.session_state.difficulty))

if st.sidebar.button("🔄 Apply & New Game", use_container_width=True):
    new_game()
    st.rerun()

st.sidebar.caption("Tip: Flip each card after guessing to read the reason + discussion prompts.")

st.markdown(
    """
    <div class="title-card">
      <h1>🎯 Guess: Myth or Fact?</h1>
      <p class="subtle">Language Edition — decide True/False, then flip the card for explanation and discussion starters.</p>
      <p>🗣️ Aa · あ · العربية · हिन्दी · 中文 · 한국어 · Ελληνικά</p>
    </div>
    """,
    unsafe_allow_html=True,
)

if st.session_state.i >= len(st.session_state.deck):
    elapsed = int(time.time() - st.session_state.start_time)
    st.success(f"Finished! Score: {st.session_state.score}/{len(st.session_state.deck)}")
    st.info(f"Session time: {elapsed // 60}m {elapsed % 60}s")
    if st.button("▶️ Play again", use_container_width=True):
        new_game()
        st.rerun()
    st.stop()

card = CARDS[st.session_state.deck[st.session_state.i]]

c1, c2, c3 = st.columns(3)
with c1:
    st.metric("Score", f"{st.session_state.score}/{len(st.session_state.deck)}")
with c2:
    st.metric("Card", f"{st.session_state.i + 1}/{len(st.session_state.deck)}")
with c3:
    remaining = len(st.session_state.deck) - st.session_state.i - 1
    st.metric("Remaining", str(remaining))

st.markdown('<div class="flashcard">', unsafe_allow_html=True)
st.markdown(f"### 🃏 {card['statement']}")

if not st.session_state.answered:
    t_col, f_col = st.columns(2)
    with t_col:
        if st.button("✅ True", use_container_width=True):
            st.session_state.choice = "FACT"
            st.session_state.is_correct = st.session_state.choice == card["label"]
            st.session_state.answered = True
            if st.session_state.is_correct:
                st.session_state.score += 1
            st.rerun()
    with f_col:
        if st.button("❌ False", use_container_width=True):
            st.session_state.choice = "MYTH"
            st.session_state.is_correct = st.session_state.choice == card["label"]
            st.session_state.answered = True
            if st.session_state.is_correct:
                st.session_state.score += 1
            st.rerun()
else:
    if st.session_state.is_correct:
        st.success("Correct guess! ✅")
    else:
        st.error("Not quite — good attempt! 💡")

st.divider()
flip_label = "🔁 Flip Card" if not st.session_state.flipped else "🙈 Hide Back"
if st.button(flip_label, use_container_width=True):
    st.session_state.flipped = not st.session_state.flipped
    st.rerun()

if st.session_state.flipped:
    label = str(card["label"])
    chip_class = "chip-fact" if label == "FACT" else "chip-myth"
    st.markdown(f"<span class='chip {chip_class}'>{label}</span>", unsafe_allow_html=True)

    if label == "FACT":
        st.markdown("#### ✅ Why this is true")
    else:
        st.markdown("#### 🧠 Why this is a myth")

    st.write(card["explanation"])
    st.markdown("#### 💬 Discussion starters")
    for question in card["discussion"]:
        st.markdown(f"- {question}")

st.markdown("</div>", unsafe_allow_html=True)

if st.session_state.answered:
    if st.button("➡️ Next Card", use_container_width=True):
        st.session_state.i += 1
        st.session_state.answered = False
        st.session_state.choice = None
        st.session_state.is_correct = None
        st.session_state.flipped = False
        st.rerun()
