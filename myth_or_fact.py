import random
from typing import Dict, List

import streamlit as st

st.set_page_config(page_title="🎯 Guess: Myth or Fact?", page_icon="📚", layout="centered")

CARDS: List[Dict[str, object]] = [
    {
        "statement": "French is the most romantic language.",
        "label": "MYTH",
        "explanation": "‘Romantic’ refers to Romance languages derived from Latin, not emotional qualities. French sounding romantic is a social stereotype.",
        "discussion": [
            "Why do certain languages get stereotyped as romantic or harsh?",
            "How much does media influence language perceptions?",
        ],
    },
    {
        "statement": "German has words that are impossible to translate.",
        "label": "MYTH",
        "explanation": "Any idea can be translated. Sometimes translators use a phrase or explanation instead of one exact word.",
        "discussion": [
            "Does translation require word-for-word equivalence?",
            "Can concepts be translated even when nuance shifts?",
        ],
    },
    {
        "statement": "Sanskrit is the most scientific language in the world.",
        "label": "MYTH",
        "explanation": "All natural languages are structured and rule-governed. No language is inherently more scientific than another.",
        "discussion": [
            "What do people usually mean by scientific language?",
            "How do language-superiority myths persist?",
        ],
    },
    {
        "statement": "African American English (AAE) is bad English.",
        "label": "MYTH",
        "explanation": "AAE has consistent grammar and linguistic rules. It is a legitimate dialect, not incorrect English.",
        "discussion": [
            "Why are some dialects stigmatized?",
            "Who decides what counts as correct language?",
        ],
    },
    {
        "statement": "Hindi and Urdu are completely different languages.",
        "label": "MYTH",
        "explanation": "In everyday conversation, Hindi and Urdu are largely mutually intelligible. Major differences are script and formal vocabulary.",
        "discussion": [
            "When do we call varieties different languages instead of dialects?",
            "How much is linguistic versus political?",
        ],
    },
    {
        "statement": "Sign language is the same everywhere in the world.",
        "label": "MYTH",
        "explanation": "There are many sign languages worldwide, each with its own grammar and history (for example, ASL and BSL are different).",
        "discussion": [
            "Why do people assume sign languages are universal?",
            "What misconceptions about Deaf communities does this reveal?",
        ],
    },
    {
        "statement": "English will eventually replace all other languages.",
        "label": "MYTH",
        "explanation": "Language survival depends on identity, policy, education, and community use. Multilingualism remains the global norm.",
        "discussion": [
            "Is multilingualism still the global norm?",
            "What factors actually cause language loss?",
        ],
    },
    {
        "statement": "Shakespeare used perfect English.",
        "label": "MYTH",
        "explanation": "Shakespeare played with and expanded English creatively. His language reflects change, not a fixed perfect standard.",
        "discussion": [
            "Why do people treat older language as purer?",
            "Is there such a thing as perfect grammar?",
        ],
    },
    {
        "statement": "Dictionaries decide what is correct.",
        "label": "MYTH",
        "explanation": "Most dictionaries describe language use; they do not single-handedly create language rules.",
        "discussion": [
            "What is the difference between prescriptive and descriptive grammar?",
            "Should dictionaries influence usage?",
        ],
    },
    {
        "statement": "Texting and social media are destroying language.",
        "label": "MYTH",
        "explanation": "Digital communication has its own conventions and often demonstrates creativity and context-aware writing.",
        "discussion": [
            "Do you write differently depending on context?",
            "Does informal writing harm formal writing skills?",
        ],
    },
    {
        "statement": "There is only one correct English.",
        "label": "MYTH",
        "explanation": "English has many valid varieties worldwide. Standard English is just one variety used in specific contexts.",
        "discussion": [
            "What is Standard English?",
            "Should schools teach only one variety?",
        ],
    },
    {
        "statement": "Babies can distinguish many speech sounds at birth.",
        "label": "FACT",
        "explanation": "Infants initially detect many phonetic contrasts. Over time, they specialize in sounds most relevant to the languages they hear.",
        "discussion": [
            "Why does this ability narrow over time?",
            "What does this reveal about language acquisition?",
        ],
    },
    {
        "statement": "Some languages use one basic term for what English calls blue and green.",
        "label": "FACT",
        "explanation": "Languages categorize color differently. Some use a broader basic category spanning colors English separates.",
        "discussion": [
            "How does language influence perception?",
            "How should we compare color systems across languages?",
        ],
    },
    {
        "statement": "Children today have a smaller vocabulary than previous generations.",
        "label": "MYTH",
        "explanation": "Vocabulary shifts with culture and technology. New domains create new words, so lexical knowledge changes rather than simply shrinking.",
        "discussion": [
            "How can vocabulary size be measured fairly?",
            "What counts as advanced vocabulary today?",
        ],
    },
]


def restart_game() -> None:
    st.session_state.deck = random.sample(range(len(CARDS)), len(CARDS))
    st.session_state.index = 0
    st.session_state.flipped = False
    st.session_state.answered = False
    st.session_state.message = ""
    st.session_state.score = 0


if "deck" not in st.session_state:
    restart_game()

st.markdown(
    """
    <style>
    .stApp {
        background:
            radial-gradient(circle at 12% 10%, rgba(101, 169, 255, 0.30), transparent 40%),
            radial-gradient(circle at 85% 0%, rgba(215, 132, 255, 0.24), transparent 35%),
            radial-gradient(circle at 0% 100%, rgba(120, 232, 190, 0.22), transparent 46%),
            linear-gradient(145deg, #0f1630 0%, #171f40 48%, #0d1327 100%);
        color: #f8fbff;
    }
    .hero, .flashcard {
        background: rgba(255, 255, 255, 0.08);
        border: 1px solid rgba(255, 255, 255, 0.24);
        border-radius: 20px;
        box-shadow: 0 12px 35px rgba(0, 0, 0, 0.28);
        backdrop-filter: blur(8px);
    }
    .hero { padding: 1.1rem 1.2rem; margin-bottom: 1rem; }
    .flashcard { padding: 1.2rem; margin-bottom: .8rem; }
    .chip {
        display: inline-block;
        padding: .2rem .65rem;
        border-radius: 999px;
        font-size: .8rem;
        font-weight: 700;
        letter-spacing: .04em;
    }
    .myth { background: rgba(255, 106, 133, 0.22); border: 1px solid rgba(255, 106, 133, 0.70); }
    .fact { background: rgba(103, 223, 165, 0.22); border: 1px solid rgba(103, 223, 165, 0.75); }
    .subtle { opacity: .88; }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class='hero'>
        <h2 style='margin: 0;'>🎯 Language Myth or Fact</h2>
        <p class='subtle' style='margin: .3rem 0 0 0;'>Pick Myth or Fact, flip to reveal, and learn from each explanation.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

col1, col2, col3 = st.columns(3)
col1.metric("Score", f"{st.session_state.score}")
col2.metric("Card", f"{st.session_state.index + 1}/{len(CARDS)}")
progress = st.session_state.index / len(CARDS)
col3.metric("Progress", f"{progress * 100:.0f}%")
st.progress(progress)

if st.session_state.index >= len(st.session_state.deck):
    st.success(f"🎉 You finished! Final score: {st.session_state.score}/{len(CARDS)}")
    if st.button("🔄 Play Again", use_container_width=True):
        restart_game()
        st.rerun()
    st.stop()

card = CARDS[st.session_state.deck[st.session_state.index]]

st.markdown("<div class='flashcard'>", unsafe_allow_html=True)
st.markdown("### 🗣️ Statement")
st.write(card["statement"])

if not st.session_state.answered:
    c1, c2 = st.columns(2)
    if c1.button("🧠 Myth", use_container_width=True):
        st.session_state.answered = True
        correct = card["label"] == "MYTH"
        if correct:
            st.session_state.score += 1
            st.session_state.message = "✅ Correct! Nice myth-busting."
        else:
            st.session_state.message = "❌ Not quite. Flip the card to learn why."
        st.rerun()

    if c2.button("📘 Fact", use_container_width=True):
        st.session_state.answered = True
        correct = card["label"] == "FACT"
        if correct:
            st.session_state.score += 1
            st.session_state.message = "✅ Correct! You spotted the fact."
        else:
            st.session_state.message = "❌ Not quite. Flip the card to learn why."
        st.rerun()

if st.session_state.message:
    if st.session_state.message.startswith("✅"):
        st.success(st.session_state.message)
    else:
        st.error(st.session_state.message)

if st.button("🔁 Flip Card" if not st.session_state.flipped else "🙈 Hide Back", use_container_width=True):
    st.session_state.flipped = not st.session_state.flipped
    st.rerun()

if st.session_state.flipped:
    label = str(card["label"])
    cls = "fact" if label == "FACT" else "myth"
    st.markdown(f"<span class='chip {cls}'>{label}</span>", unsafe_allow_html=True)
    st.markdown("#### Explanation")
    st.write(card["explanation"])
    st.markdown("#### Discussion starters")
    for item in card["discussion"]:
        st.markdown(f"- {item}")

st.markdown("</div>", unsafe_allow_html=True)

if st.session_state.answered and st.button("➡️ Next Card", use_container_width=True):
    st.session_state.index += 1
    st.session_state.flipped = False
    st.session_state.answered = False
    st.session_state.message = ""
    st.rerun()

with st.sidebar:
    st.header("Settings")
    st.caption("Restart to reshuffle the deck.")
    if st.button("🔄 Restart Game", use_container_width=True):
        restart_game()
        st.rerun()
