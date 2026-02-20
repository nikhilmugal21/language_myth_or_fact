import random
from typing import Dict, List

import streamlit as st

st.set_page_config(
    page_title="🎯 Guess: Myth or Fact?",
    page_icon="📚",
    layout="centered",
)

CARDS: List[Dict[str, object]] = [
    {
        "statement": "French is the most romantic language.",
        "label": "MYTH",
        "explanation": "‘Romantic’ refers to Romance languages derived from Latin, not emotional qualities. French sounding romantic is a social stereotype, not a linguistic fact.",
        "discussion": [
            "Why do certain languages get stereotyped as ‘romantic’ or ‘harsh’?",
            "How much does media influence our perception of languages?",
        ],
    },
    {
        "statement": "German has words that are impossible to translate.",
        "label": "MYTH",
        "explanation": "Any idea can be translated. Sometimes translators use a phrase or explanation instead of one exact word.",
        "discussion": [
            "Does translation require word-for-word equivalence?",
            "Can cultural concepts be translated without losing nuance?",
        ],
    },
    {
        "statement": "Sanskrit is the most scientific language in the world.",
        "label": "MYTH",
        "explanation": "All human languages are structured and rule-governed. No language is inherently more scientific or superior than others.",
        "discussion": [
            "What do people usually mean by ‘scientific language’?",
            "Is systematic grammar the same as scientific superiority?",
        ],
    },
    {
        "statement": "African American English (AAE) is ‘bad English.’",
        "label": "MYTH",
        "explanation": "AAE has consistent grammar and linguistic rules. It is a legitimate dialect, not incorrect English.",
        "discussion": [
            "Why are some dialects stigmatized?",
            "Who decides what counts as ‘correct’ English?",
        ],
    },
    {
        "statement": "Hindi and Urdu are completely different languages.",
        "label": "MYTH",
        "explanation": "In everyday speech, Hindi and Urdu are largely mutually intelligible. Major differences are mostly script and formal vocabulary.",
        "discussion": [
            "What makes two varieties separate languages rather than dialects?",
            "Is the distinction linguistic or political?",
        ],
    },
    {
        "statement": "Sign language is the same everywhere in the world.",
        "label": "MYTH",
        "explanation": "There are many sign languages worldwide, each with its own grammar and history (for example, ASL and BSL are different languages).",
        "discussion": [
            "Why do people assume sign languages are universal?",
            "What does this reveal about misconceptions about Deaf communities?",
        ],
    },
    {
        "statement": "English will eventually replace all other languages.",
        "label": "MYTH",
        "explanation": "Language survival depends on identity, policy, education, and community use. Multilingualism remains the global norm.",
        "discussion": [
            "Is multilingualism the global norm?",
            "What factors actually cause language death?",
        ],
    },
    {
        "statement": "Shakespeare used perfect English.",
        "label": "MYTH",
        "explanation": "Shakespeare played with and expanded English creatively. His language reflects a changing system, not a perfect fixed standard.",
        "discussion": [
            "Why do we treat older forms of language as ‘purer’?",
            "Is there such a thing as perfect grammar?",
        ],
    },
    {
        "statement": "Dictionaries decide what’s correct.",
        "label": "MYTH",
        "explanation": "Most dictionaries describe how people use language; they do not create language rules by themselves.",
        "discussion": [
            "What is the difference between prescriptive and descriptive grammar?",
            "Should dictionaries influence language use?",
        ],
    },
    {
        "statement": "Texting and social media are destroying language.",
        "label": "MYTH",
        "explanation": "Digital communication has its own conventions and often demonstrates creativity, adaptation, and context-aware writing.",
        "discussion": [
            "Do you change how you write in different contexts?",
            "Is informal writing a threat to formal language skills?",
        ],
    },
    {
        "statement": "There’s only one correct English.",
        "label": "MYTH",
        "explanation": "English has many valid varieties worldwide. Standard English is one variety used in particular contexts.",
        "discussion": [
            "What is Standard English?",
            "Should schools teach only one variety?",
        ],
    },
    {
        "statement": "Babies can distinguish all speech sounds in the world at birth.",
        "label": "FACT",
        "explanation": "Infants initially detect many phonetic contrasts. Over time, they specialize in contrasts most relevant to the languages they hear.",
        "discussion": [
            "Why does this ability narrow over time?",
            "What does this tell us about language acquisition?",
        ],
    },
    {
        "statement": "Some languages have no word for ‘blue.’",
        "label": "FACT",
        "explanation": "Languages categorize color differently. Some use one basic term spanning what English separates as blue and green.",
        "discussion": [
            "Does language influence perception of color?",
            "How does this relate to linguistic relativity?",
        ],
    },
    {
        "statement": "Children today have a smaller vocabulary than previous generations.",
        "label": "MYTH",
        "explanation": "Vocabulary changes with culture and technology. New domains create new words, so lexical knowledge shifts rather than simply shrinking.",
        "discussion": [
            "Do digital environments create new lexical fields?",
            "How can vocabulary size be measured accurately?",
        ],
    },
]

if "deck" not in st.session_state:
    st.session_state.deck = random.sample(range(len(CARDS)), len(CARDS))
if "index" not in st.session_state:
    st.session_state.index = 0
if "flipped" not in st.session_state:
    st.session_state.flipped = False
if "answered" not in st.session_state:
    st.session_state.answered = False
if "message" not in st.session_state:
    st.session_state.message = ""
if "score" not in st.session_state:
    st.session_state.score = 0


def restart_game() -> None:
    st.session_state.deck = random.sample(range(len(CARDS)), len(CARDS))
    st.session_state.index = 0
    st.session_state.flipped = False
    st.session_state.answered = False
    st.session_state.message = ""
    st.session_state.score = 0


st.markdown(
    """
    <style>
        .stApp {
            background:
                radial-gradient(circle at 20% 20%, rgba(116, 188, 255, 0.35), transparent 40%),
                radial-gradient(circle at 80% 0%, rgba(221, 154, 255, 0.28), transparent 35%),
                radial-gradient(circle at 0% 100%, rgba(145, 242, 208, 0.25), transparent 45%),
                linear-gradient(140deg, #11182b, #1a2140 45%, #101326);
            color: #f8fbff;
        }

        .hero {
            padding: 1.3rem;
            border-radius: 20px;
            background: rgba(255, 255, 255, 0.08);
            border: 1px solid rgba(255, 255, 255, 0.22);
            backdrop-filter: blur(6px);
            margin-bottom: 1rem;
            box-shadow: 0 10px 35px rgba(0, 0, 0, 0.25);
        }

        .flashcard {
            border-radius: 22px;
            padding: 1.4rem;
            background: rgba(255, 255, 255, 0.09);
            border: 1px solid rgba(255, 255, 255, 0.25);
            box-shadow: 0 16px 40px rgba(0,0,0,0.25);
        }

        .chip {
            display: inline-block;
            font-size: 0.8rem;
            font-weight: 600;
            letter-spacing: .03rem;
            padding: .2rem .65rem;
            border-radius: 999px;
            margin-right: .4rem;
        }

        .myth { background: rgba(255, 107, 129, 0.22); border: 1px solid rgba(255, 107, 129, .6); }
        .fact { background: rgba(106, 214, 161, 0.24); border: 1px solid rgba(106, 214, 161, .7); }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="hero">
        <h1>🎯 Guess: Myth or Fact?</h1>
        <p>📚 Language edition — choose <b>True</b> or <b>False</b>, then flip the card to reveal the explanation and discussion starters.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

col_a, col_b, col_c = st.columns([1, 1, 1])
with col_a:
    st.metric("Score", f"{st.session_state.score}/{len(CARDS)}")
with col_b:
    st.metric("Card", f"{min(st.session_state.index + 1, len(CARDS))}/{len(CARDS)}")
with col_c:
    if st.button("🔄 Restart", use_container_width=True):
        restart_game()
        st.rerun()

if st.session_state.index >= len(CARDS):
    st.success(f"🎉 Finished! Final score: {st.session_state.score}/{len(CARDS)}")
    st.balloons()
    st.stop()

card = CARDS[st.session_state.deck[st.session_state.index]]

st.markdown('<div class="flashcard">', unsafe_allow_html=True)
st.markdown(f"### 🃏 {card['statement']}")

if st.session_state.answered:
    st.info(st.session_state.message)
else:
    c1, c2 = st.columns(2)
    with c1:
        if st.button("✅ True", use_container_width=True):
            picked = "FACT"
            actual = str(card["label"])
            st.session_state.answered = True
            if picked == actual:
                st.session_state.score += 1
                st.session_state.message = "Correct! This statement is a FACT."
            else:
                st.session_state.message = "Not quite. This statement is a MYTH."
            st.rerun()
    with c2:
        if st.button("❌ False", use_container_width=True):
            picked = "MYTH"
            actual = str(card["label"])
            st.session_state.answered = True
            if picked == actual:
                st.session_state.score += 1
                st.session_state.message = "Correct! This statement is a MYTH."
            else:
                st.session_state.message = "Not quite. This statement is a FACT."
            st.rerun()

st.divider()

flip_text = "🔁 Flip Card" if not st.session_state.flipped else "🙈 Hide Back"
if st.button(flip_text, use_container_width=True):
    st.session_state.flipped = not st.session_state.flipped
    st.rerun()

if st.session_state.flipped:
    label = str(card["label"])
    cls = "fact" if label == "FACT" else "myth"
    st.markdown(f'<span class="chip {cls}">{label}</span>', unsafe_allow_html=True)

    if label == "FACT":
        st.markdown("#### ✅ Why this is true")
    else:
        st.markdown("#### 🧠 Why this is a myth")

    st.write(str(card["explanation"]))

    st.markdown("#### 💬 Discussion starters")
    for q in card["discussion"]:
        st.markdown(f"- {q}")

st.markdown("</div>", unsafe_allow_html=True)

if st.session_state.answered and st.button("➡️ Next Card", use_container_width=True):
    st.session_state.index += 1
    st.session_state.flipped = False
    st.session_state.answered = False
    st.session_state.message = ""
    st.rerun()
