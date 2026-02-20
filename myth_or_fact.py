# app.py
# Streamlit flashcard game: "Guess: Myth or Fact? (Languages Edition)"
# Run: streamlit run app.py

import random
import textwrap
import streamlit as st

st.set_page_config(page_title="Myth or Fact? — Languages Flashcards", page_icon="🃏", layout="centered")

# -----------------------------
# Data
# -----------------------------
CARDS = [
    {
        "id": 1,
        "statement": "French is the most romantic language.",
        "label": "MYTH",
        "explanation": "“Romantic” refers to Romance languages derived from Latin — not emotional qualities.",
        "discussion": [
            "Why do certain languages get stereotyped as “romantic” or “harsh”?",
            "How much does media influence our perception of languages?",
        ],
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
    },
]

# -----------------------------
# Helpers
# -----------------------------
def is_true_answer(card_label: str) -> bool:
    """Return True if the statement should be marked 'True'."""
    # FACT -> True, MYTH -> False
    return card_label.strip().upper() == "FACT"


def reset_game(shuffle: bool = True):
    order = list(range(len(CARDS)))
    if shuffle:
        random.shuffle(order)
    st.session_state.order = order
    st.session_state.idx = 0
    st.session_state.score = 0
    st.session_state.answered = False
    st.session_state.user_choice = None
    st.session_state.is_correct = None
    st.session_state.flipped = False
    st.session_state.history = []  # list of dicts


def current_card():
    if st.session_state.idx >= len(st.session_state.order):
        return None
    return CARDS[st.session_state.order[st.session_state.idx]]


def wrap(s: str, width: int = 80) -> str:
    return "\n".join(textwrap.wrap(s, width=width))


# -----------------------------
# Session init
# -----------------------------
if "order" not in st.session_state:
    reset_game(shuffle=True)

# -----------------------------
# Sidebar controls
# -----------------------------
st.sidebar.title("🧠 Game Controls")

shuffle_on_reset = st.sidebar.toggle("Shuffle on restart", value=True)
show_discussion = st.sidebar.toggle("Show discussion starters", value=True)
show_progress = st.sidebar.toggle("Show progress", value=True)

if st.sidebar.button("🔄 Restart game", use_container_width=True):
    reset_game(shuffle=shuffle_on_reset)
    st.rerun()

st.sidebar.divider()
st.sidebar.caption("Tip: Answer first, then flip the card to reveal the explanation + prompts.")

# -----------------------------
# Styles (simple “flip card” feel)
# -----------------------------
st.markdown(
    """
<style>
/* Card container */
.fc-wrap {
    border: 1px solid rgba(255,255,255,0.12);
    border-radius: 18px;
    padding: 18px 18px 14px 18px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.18);
    background: linear-gradient(180deg, rgba(255,255,255,0.06), rgba(255,255,255,0.03));
}

/* “Front/Back” headings */
.fc-tag {
    display: inline-block;
    font-size: 0.85rem;
    padding: 6px 10px;
    border-radius: 999px;
    border: 1px solid rgba(255,255,255,0.14);
    background: rgba(255,255,255,0.04);
    margin-bottom: 10px;
}

/* Big statement */
.fc-statement {
    font-size: 1.35rem;
    line-height: 1.35;
    margin: 6px 0 12px 0;
}

/* Result badge */
.fc-result {
    display:inline-block;
    padding: 7px 10px;
    border-radius: 10px;
    border: 1px solid rgba(255,255,255,0.18);
    background: rgba(255,255,255,0.06);
    margin-top: 8px;
}

/* Explanation */
.fc-expl {
    margin-top: 10px;
    padding: 12px 12px;
    border-radius: 14px;
    border: 1px solid rgba(255,255,255,0.14);
    background: rgba(0,0,0,0.16);
}

/* Discussion list */
.fc-disc li { margin: 4px 0; }
</style>
""",
    unsafe_allow_html=True,
)

# -----------------------------
# Header
# -----------------------------
st.title("🃏 Myth or Fact? — Languages Flashcards")
st.caption("Pick **True** or **False**. Then **flip** the card to reveal the explanation and discussion starters.")

card = current_card()

# -----------------------------
# End screen
# -----------------------------
if card is None:
    total = len(CARDS)
    score = st.session_state.score
    st.success(f"Game complete! Your score: **{score}/{total}**")

    # Summary
    with st.expander("📋 Review your answers", expanded=False):
        for h in st.session_state.history:
            st.markdown(
                f"""
**{h['n']}. {h['statement']}**  
- Correct answer: **{h['correct_answer']}** ({h['label']})  
- You chose: **{h['user_choice']}** → {"✅" if h["is_correct"] else "❌"}  
- Note: {h['explanation']}
"""
            )

    colA, colB = st.columns(2)
    with colA:
        if st.button("🔁 Play again", use_container_width=True):
            reset_game(shuffle=shuffle_on_reset)
            st.rerun()
    with colB:
        st.download_button(
            "⬇️ Download questions (JSON)",
            data=str(CARDS).encode("utf-8"),
            file_name="language_myth_fact_cards.json",
            mime="application/json",
            use_container_width=True,
        )
    st.stop()

# -----------------------------
# Progress + Score
# -----------------------------
total = len(CARDS)
index_1 = st.session_state.idx + 1

if show_progress:
    st.progress((index_1 - 1) / total, text=f"Card {index_1} of {total}")

st.markdown(f"**Score:** {st.session_state.score} / {st.session_state.idx}")

# -----------------------------
# Card UI
# -----------------------------
truth = is_true_answer(card["label"])
correct_answer_text = "True" if truth else "False"

st.markdown('<div class="fc-wrap">', unsafe_allow_html=True)

st.markdown(
    f'<span class="fc-tag">Front</span>',
    unsafe_allow_html=True,
)
st.markdown(
    f'<div class="fc-statement">“{card["statement"]}”</div>',
    unsafe_allow_html=True,
)

# Answer buttons (locked after answering)
b1, b2 = st.columns(2)

def answer(choice: str):
    st.session_state.answered = True
    st.session_state.user_choice = choice
    user_true = choice == "True"
    st.session_state.is_correct = (user_true == truth)
    if st.session_state.is_correct:
        st.session_state.score += 1

with b1:
    if st.button("✅ True", use_container_width=True, disabled=st.session_state.answered):
        answer("True")
        st.rerun()

with b2:
    if st.button("❌ False", use_container_width=True, disabled=st.session_state.answered):
        answer("False")
        st.rerun()

# Feedback after answering
if st.session_state.answered:
    icon = "✅" if st.session_state.is_correct else "❌"
    msg = "Correct!" if st.session_state.is_correct else "Not quite!"
    st.markdown(
        f'<div class="fc-result">{icon} <b>{msg}</b> '
        f'&nbsp;•&nbsp; Correct answer: <b>{correct_answer_text}</b></div>',
        unsafe_allow_html=True,
    )

# Flip control
flip_col1, flip_col2 = st.columns([1, 1])
with flip_col1:
    flip_label = "🔄 Flip card" if not st.session_state.flipped else "↩️ Unflip"
    if st.button(flip_label, use_container_width=True, disabled=not st.session_state.answered):
        st.session_state.flipped = not st.session_state.flipped
        st.rerun()

with flip_col2:
    # Next card (only after flip to encourage reading)
    if st.button("➡️ Next card", use_container_width=True, disabled=not (st.session_state.answered and st.session_state.flipped)):
        # save history
        st.session_state.history.append(
            {
                "n": index_1,
                "statement": card["statement"],
                "label": card["label"],
                "correct_answer": correct_answer_text,
                "user_choice": st.session_state.user_choice,
                "is_correct": st.session_state.is_correct,
                "explanation": card["explanation"],
            }
        )
        # advance + reset per-card state
        st.session_state.idx += 1
        st.session_state.answered = False
        st.session_state.user_choice = None
        st.session_state.is_correct = None
        st.session_state.flipped = False
        st.rerun()

# Back side (revealed)
if st.session_state.flipped:
    kind = "FACT ✅" if card["label"].upper() == "FACT" else "MYTH 🚫"
    st.markdown(
        f"""
<div class="fc-expl">
  <span class="fc-tag">Back — {kind}</span>
  <div><b>Note:</b> {card["explanation"]}</div>
</div>
""",
        unsafe_allow_html=True,
    )

    if show_discussion and card.get("discussion"):
        st.markdown("**Discussion starters:**")
        st.markdown('<ul class="fc-disc">', unsafe_allow_html=True)
        for q in card["discussion"]:
            st.markdown(f"- {q}")
        st.markdown("</ul>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# -----------------------------
# Gentle nudge before answer/flip
# -----------------------------
if not st.session_state.answered:
    st.info("Choose **True** or **False** to lock your answer.")
elif st.session_state.answered and not st.session_state.flipped:
    st.info("Now **flip** the card to reveal the explanation. Then you can go to the next card.")