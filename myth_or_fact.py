import random
from typing import Dict, List

import streamlit as st

st.set_page_config(page_title="Tongues of Deception: The Myths we speak", page_icon="📚", layout="centered")

ROUND_SIZE = 15
FACTS_PER_ROUND = 5
MYTHS_PER_ROUND = 10

CARDS: List[Dict[str, object]] = [
    {
        "statement": "Sanskrit is the mother of all Indian languages.",
        "label": "MYTH",
        "explanation": "Many North Indian languages were influenced by Sanskrit, but South Indian languages like Tamil and Telugu developed from a different language family. Languages can influence each other without being directly related.",
        "discussion": [
            "What does it mean for languages to belong to different families?",
            "How do languages borrow from each other?",
        ],
    },
    {
        "statement": "Hindi is the national language of India.",
        "label": "MYTH",
        "explanation": "India does not have a national language. The Constitution recognizes multiple official languages. Hindi and English are used by the central government, but many states use their own official languages.",
        "discussion": [
            "Why is this misunderstanding common?",
            "Should India adopt a single national language?",
        ],
    },
    {
        "statement": "Having a strong regional accent means weak English.",
        "label": "MYTH",
        "explanation": "Accent simply shows where someone is from. It does not reflect intelligence, education, or language skill. Every English speaker in the world speaks with an accent.",
        "discussion": [
            "Why are certain accents considered more prestigious?",
            "Have you ever been judged because of your accent?",
        ],
    },
    {
        "statement": "Mixing languages (Hinglish, Tanglish, etc.) is ruining languages.",
        "label": "MYTH",
        "explanation": "Mixing languages is common in multilingual societies like India. People switch languages naturally depending on situation, emotion, or audience. This does not damage languages — it shows flexibility.",
        "discussion": [
            "When do you mix languages?",
            "Does mixing languages help express ideas better?",
        ],
    },
    {
        "statement": "Tribal languages are backward or simple.",
        "label": "MYTH",
        "explanation": "Tribal languages are complete systems with their own grammar and rich cultural knowledge. Many have complex storytelling traditions and environmental knowledge passed through generations.",
        "discussion": [
            "Why are smaller languages often undervalued?",
            "Should endangered languages be preserved?",
        ],
    },
    {
        "statement": "If a language has no script, it is incomplete.",
        "label": "MYTH",
        "explanation": "For centuries, many communities passed down history, poetry, and knowledge orally. Writing is a tool, but a language can fully function without it.",
        "discussion": [
            "How were epics and folk stories preserved before writing?",
            "Does written language have more power than spoken language?",
        ],
    },
    {
        "statement": "English-medium education makes children smarter.",
        "label": "MYTH",
        "explanation": "Intelligence does not depend on language. Research shows children often learn better in their mother tongue, especially in early years. Understanding concepts clearly is more important than the language used.",
        "discussion": [
            "Is it easier to learn complex ideas in your first language?",
            "Should schools promote mother-tongue education?",
        ],
    },
    {
        "statement": "All South Indians speak the same language.",
        "label": "MYTH",
        "explanation": "South India has several major languages that are different from each other. Tamil is not the same as Telugu or Kannada. Each has its own history and literature.",
        "discussion": [
            "Why do people simplify linguistic diversity?",
            "How does language connect to regional pride?",
        ],
    },
    {
        "statement": "India is one of the most multilingual countries in the world.",
        "label": "FACT",
        "explanation": "Many Indians grow up speaking their home language, a regional language, and often English or Hindi. Multilingualism is normal and everyday life requires language switching.",
        "discussion": [
            "How many languages do you use daily?",
            "Does speaking multiple languages change how you think?",
        ],
    },
    {
        "statement": "Many Indian languages are disappearing.",
        "label": "FACT",
        "explanation": "Some languages are spoken by very few elderly speakers. When younger generations shift to dominant languages, smaller languages can fade away.",
        "discussion": [
            "Why do families stop teaching their native language?",
            "What can communities do to protect their language?",
        ],
    },
    {
        "statement": "Hindi is understood everywhere in India.",
        "label": "MYTH",
        "explanation": "Hindi is widely spoken in North and Central India, but many regions primarily use other languages. Not everyone is comfortable using Hindi.",
        "discussion": [
            "How does media create the idea of a dominant language?",
            "Should one language represent the whole country?",
        ],
    },
    {
        "statement": "Pronouncing English in an Indian way is wrong.",
        "label": "MYTH",
        "explanation": "Every country has its own way of pronouncing English. Indian pronunciation reflects Indian sound patterns and is natural.",
        "discussion": [
            "Do Americans and British pronounce English the same way?",
            "Why should one accent be considered superior?",
        ],
    },
    {
        "statement": "French is the most romantic language.",
        "label": "MYTH",
        "explanation": "The word ‘Romantic’ in linguistics refers to languages that come from Latin, such as French, Spanish, and Italian. It does not mean emotional or loving. The idea that French sounds romantic comes from culture, movies, and stereotypes.",
        "discussion": [
            "Why do some languages sound ‘beautiful’ or ‘harsh’ to us?",
            "How much do films and media shape our opinion of languages?",
        ],
    },
    {
        "statement": "German has words that are impossible to translate.",
        "label": "MYTH",
        "explanation": "Any idea can be translated into another language. Sometimes it takes a whole sentence instead of one word, but the meaning can still be explained. Translation is about meaning, not matching word for word.",
        "discussion": [
            "Is translation about words or ideas?",
            "Can meaning change slightly when translated?",
        ],
    },
    {
        "statement": "Sanskrit is the most scientific language in the world.",
        "label": "MYTH",
        "explanation": "Sanskrit has a very detailed grammar system, but all languages follow rules. No language is naturally more scientific or superior than another.",
        "discussion": [
            "What do people mean when they call a language ‘scientific’?",
            "Are rules enough to make something superior?",
        ],
    },
    {
        "statement": "Bambaiyya Hindi is ‘bad Hindi.’",
        "label": "MYTH",
        "explanation": "Bambaiyya Hindi has its own patterns, vocabulary, and cultural context. It is a living urban variety, not ‘wrong’ Hindi. Dialects and mixed varieties are natural forms of language.",
        "discussion": [
            "Why are some dialects respected while others are criticized?",
            "Who decides what is considered ‘proper’ language?",
        ],
    },
    {
        "statement": "Hindi and Urdu are completely different languages.",
        "label": "MYTH",
        "explanation": "In everyday conversation, Hindi and Urdu are very similar and speakers can usually understand each other. The main differences are script and some formal vocabulary.",
        "discussion": [
            "When do two ways of speaking become separate languages?",
            "Is the difference based more on language or politics?",
        ],
    },
    {
        "statement": "Sign language is the same everywhere in the world.",
        "label": "MYTH",
        "explanation": "Different countries have different sign languages, just like spoken languages. For example, American Sign Language and British Sign Language are not the same.",
        "discussion": [
            "Why do people assume sign language is universal?",
            "What does this show about how we view deaf communities?",
        ],
    },
    {
        "statement": "English will eventually replace all other languages.",
        "label": "MYTH",
        "explanation": "English is widely used, but people around the world continue to speak their home languages. Many people use English in addition to their native language, not instead of it.",
        "discussion": [
            "Is the world becoming monolingual or multilingual?",
            "What helps a language survive?",
        ],
    },
    {
        "statement": "Shakespeare used perfect English.",
        "label": "MYTH",
        "explanation": "Shakespeare actually played with language, created new words, and experimented with grammar. His English was changing, just like English today.",
        "discussion": [
            "Why do we think older language is more ‘pure’?",
            "Is there such a thing as perfect grammar?",
        ],
    },
    {
        "statement": "Dictionaries decide what’s correct.",
        "label": "MYTH",
        "explanation": "Dictionaries record how people use language. They do not create rules — they describe what speakers already say and write.",
        "discussion": [
            "What is the difference between describing language and controlling it?",
            "Should dictionaries guide how we speak?",
        ],
    },
    {
        "statement": "Texting and social media are destroying language.",
        "label": "MYTH",
        "explanation": "Online communication has its own style and rules. People often know when to use informal texting and when to use formal writing. Language is adapting, not being destroyed.",
        "discussion": [
            "Do you write differently in exams and on WhatsApp?",
            "Is informal writing harmful or creative?",
        ],
    },
    {
        "statement": "Babies can distinguish all speech sounds in the world at infancy.",
        "label": "FACT",
        "explanation": "Infants are able to hear many different speech sounds. As they grow, they focus more on the sounds of the language they hear around them.",
        "discussion": [
            "Why does this ability narrow as children grow?",
            "What does this tell us about how language learning works?",
        ],
    },
    {
        "statement": "Some languages have no word for ‘blue.’",
        "label": "FACT",
        "explanation": "Some languages group colors differently and may not separate blue and green into two basic words. This does not mean speakers cannot see the difference — just that they categorize colors differently.",
        "discussion": [
            "Does language affect how we think about colors?",
            "Can different languages organize the world differently?",
        ],
    },
    {
        "statement": "Children today have a smaller vocabulary than previous generations.",
        "label": "MYTH",
        "explanation": "Children today may know different words, especially related to technology and modern life. Vocabulary changes with culture, but it does not necessarily shrink.",
        "discussion": [
            "How do we measure vocabulary size?",
            "Are new digital words expanding language?",
        ],
    },
    {
        "statement": "If you make grammar mistakes, you are not intelligent.",
        "label": "MYTH",
        "explanation": "Grammar mistakes do not measure intelligence. Many highly intelligent people speak different dialects, multiple languages, or learned a language later in life. Intelligence and language style are not the same thing.",
        "discussion": [
            "Why do we judge intelligence based on speech?",
            "Is fluency the same as intelligence?",
        ],
    },
    {
        "statement": "If you stop speaking your mother tongue, you will forget it completely.",
        "label": "FACT",
        "explanation": "If a language is not used for many years, people may forget words or fluency. However, many people can quickly relearn their first language because it remains stored in memory.",
        "discussion": [
            "Have you ever forgotten words in your mother tongue?",
            "Why is it easier to relearn a childhood language?",
        ],
    },
    {
        "statement": "Learning a new language is only possible when you are young.",
        "label": "MYTH",
        "explanation": "Children may learn pronunciation more easily, but adults can also successfully learn new languages. Motivation and practice matter more than age.",
        "discussion": [
            "What advantages do adults have when learning languages?",
            "Is fear of making mistakes a bigger barrier than age?",
        ],
    },
    {
        "statement": "Using filler words like ‘um’, ‘like’, or ‘matlab’ means you are unprepared.",
        "label": "MYTH",
        "explanation": "Filler words are natural pauses while thinking. All languages have them. They help speakers organize thoughts in real time.",
        "discussion": [
            "What filler words do you use?",
            "Are fillers always negative, or can they help communication?",
        ],
    },
    {
        "statement": "If you watch movies in a language, you’ll automatically become fluent.",
        "label": "MYTH",
        "explanation": "Watching helps with exposure and listening skills, but fluency requires active practice — speaking, reading, and interacting.",
        "discussion": [
            "How much can you learn from subtitles?",
            "Is passive learning enough for fluency?",
        ],
    },
    {
        "statement": "If someone pauses while speaking, they don’t know what they’re talking about.",
        "label": "MYTH",
        "explanation": "Pauses are natural. Our brain needs time to organize thoughts. Even confident speakers pause frequently.",
        "discussion": [
            "Do you feel uncomfortable during silence?",
            "Why do we associate smooth speech with intelligence?",
        ],
    },
    {
        "statement": "If a language sounds angry, the speakers must be angry people.",
        "label": "MYTH",
        "explanation": "Some languages may sound harsh or loud to outsiders because of unfamiliar sounds, but that has nothing to do with personality.",
        "discussion": [
            "Which languages do you think sound ‘angry’?",
            "How much of this comes from stereotypes?",
        ],
    },
    {
        "statement": "If you translate something word-for-word, it will have the same meaning.",
        "label": "MYTH",
        "explanation": "Languages structure ideas differently. A direct word-for-word translation often sounds strange or changes meaning because grammar and cultural expressions differ.",
        "discussion": [
            "Have you ever seen a funny translation online?",
            "Why can literal translation cause confusion?",
        ],
    },
    {
        "statement": "You lose your culture if you start speaking English.",
        "label": "MYTH",
        "explanation": "Learning a new language does not erase your identity. Many people successfully maintain their mother tongue while using English.",
        "discussion": [
            "Can someone belong to multiple linguistic worlds?",
            "Is language loss about choice or pressure?",
        ],
    },
    {
        "statement": "Grammar rules never change.",
        "label": "MYTH",
        "explanation": "Grammar evolves over time. Many forms that were once ‘incorrect’ later became accepted.",
        "discussion": [
            "Can you think of grammar rules that changed?",
            "Who decides when a rule changes?",
        ],
    },
    {
        "statement": "If two languages share similar words, they must be the same language.",
        "label": "MYTH",
        "explanation": "Languages often borrow words from each other. Similar vocabulary does not mean they are identical.",
        "discussion": [
            "Can you think of English words from other languages?",
            "Does borrowing weaken or enrich a language?",
        ],
    },
    {
        "statement": "People who read more speak more ‘correctly.’",
        "label": "MYTH",
        "explanation": "Reading improves vocabulary, but spoken language follows different patterns. Everyday speech often differs from written language.",
        "discussion": [
            "Do you speak the same way you write?",
            "Is spoken language less important than written language?",
        ],
    },
    {
        "statement": "If a language doesn’t have a word for something, its speakers don’t understand that concept.",
        "label": "MYTH",
        "explanation": "People can understand ideas even if their language expresses them differently. Words are tools — not limits of thought.",
        "discussion": [
            "Can you describe something even if you don’t know the exact word?",
            "Does language limit thinking?",
        ],
    },
    {
        "statement": "You must speak ‘pure’ language without mixing words.",
        "label": "MYTH",
        "explanation": "No language is completely pure. All languages borrow words from others over time.",
        "discussion": [
            "Can you think of borrowed words in your language?",
            "Is linguistic purity realistic?",
        ],
    },
    {
        "statement": "Formal language is always better than informal language.",
        "label": "MYTH",
        "explanation": "Different situations require different styles. Informal language is not inferior — it is just used in different contexts.",
        "discussion": [
            "Do you speak differently with friends and teachers?",
            "Is casual language disrespectful?",
        ],
    },
    {
        "statement": "If a language sounds similar to yours, it must be easy to learn.",
        "label": "MYTH",
        "explanation": "Similar languages may share vocabulary, but differences in grammar and pronunciation can still be challenging.",
        "discussion": [
            "Have you tried learning a ‘similar’ language?",
            "Was it easier than expected?",
        ],
    },
    {
        "statement": "There are languages with no word for ‘yes’ or ‘no.’",
        "label": "FACT",
        "explanation": "Some languages answer questions by repeating the verb instead of saying yes or no. For example, instead of saying “yes,” a speaker might say “I did.”",
        "discussion": [
            "Is “yes/no” necessary for communication?",
            "How would this change everyday conversations?",
        ],
    },
    {
        "statement": "Some languages use clicks as normal speech sounds.",
        "label": "FACT",
        "explanation": "In parts of southern Africa, certain languages use click sounds as regular consonants, just like we use “b” or “t.”",
        "discussion": [
            "Have you ever heard a click language?",
            "Why do unfamiliar sounds seem unusual to us?",
        ],
    },
    {
        "statement": "One word can be a complete sentence in some languages.",
        "label": "FACT",
        "explanation": "In some languages, a single long word can include subject, tense, and object — expressing what would take a whole sentence in English.",
        "discussion": [
            "Is longer always more complicated?",
            "How do different languages pack information differently?",
        ],
    },
    {
        "statement": "You can lose the ability to hear certain sounds as you grow up.",
        "label": "FACT",
        "explanation": "Babies can hear many speech sounds from all languages, but as they grow, they become better at hearing the sounds of their own language and may struggle with others.",
        "discussion": [
            "Why do adults find foreign pronunciation difficult?",
            "Can we retrain our ears?",
        ],
    },
    {
        "statement": "Words can change meaning completely over time.",
        "label": "FACT",
        "explanation": "Many English words once meant something very different. For example, ‘awful’ once meant ‘full of awe.’",
        "discussion": [
            "Can you think of slang words that changed meaning?",
            "Why do meanings shift over time?",
        ],
    },
    {
        "statement": "The same gesture can mean different things in different cultures.",
        "label": "FACT",
        "explanation": "Even simple gestures like a thumbs-up can have different meanings depending on the country.",
        "discussion": [
            "Can gestures cause misunderstandings?",
            "Is communication only about words?",
        ],
    },
    {
        "statement": "You use different grammar when you speak than when you write.",
        "label": "FACT",
        "explanation": "Spoken language is usually more relaxed and flexible. Writing tends to follow stricter rules. Both are correct in their own contexts.",
        "discussion": [
            "Do you speak the same way you write emails?",
            "Is spoken language less ‘correct’ than written language?",
        ],
    },
]


def restart_game() -> None:
    fact_indexes = [idx for idx, card in enumerate(CARDS) if card["label"] == "FACT"]
    myth_indexes = [idx for idx, card in enumerate(CARDS) if card["label"] == "MYTH"]

    selected_facts = random.sample(fact_indexes, min(FACTS_PER_ROUND, len(fact_indexes)))
    selected_myths = random.sample(myth_indexes, min(MYTHS_PER_ROUND, len(myth_indexes)))

    deck = selected_facts + selected_myths

    target_size = min(ROUND_SIZE, len(CARDS))
    if len(deck) < target_size:
        remaining = [idx for idx in range(len(CARDS)) if idx not in deck]
        deck.extend(random.sample(remaining, min(target_size - len(deck), len(remaining))))

    random.shuffle(deck)

    st.session_state.deck = deck
    st.session_state.index = 0
    st.session_state.flipped = False
    st.session_state.answered = False
    st.session_state.message = ""
    st.session_state.score = 0
    st.session_state.last_action = ""


if "deck" not in st.session_state:
    restart_game()
if "last_action" not in st.session_state:
    st.session_state.last_action = ""

st.markdown(
    """
        <style>
    .stApp {
        background:
            radial-gradient(circle at 8% 8%, rgba(255, 199, 221, 0.55), transparent 32%),
            radial-gradient(circle at 88% 5%, rgba(198, 226, 255, 0.55), transparent 35%),
            radial-gradient(circle at 50% 100%, rgba(199, 245, 221, 0.55), transparent 40%),
            linear-gradient(150deg, #fff6fb 0%, #f3f8ff 44%, #f6fff8 100%);
        color: #2d2942;
    }

    /* Force Streamlit metrics to remain visible */
    [data-testid="stMetric"] {
        background: rgba(255, 255, 255, 0.8);
        border: 1px solid rgba(190, 176, 235, 0.6);
        border-radius: 14px;
        padding: .45rem .7rem;
        box-shadow: 0 6px 14px rgba(116, 105, 165, 0.14);
    }
    [data-testid="stMetricLabel"],
    [data-testid="stMetricValue"],
    [data-testid="stMetricDelta"] {
        color: #2a2543 !important;
    }
    .hero {
        background: rgba(255, 255, 255, 0.92);
        border: 1px solid rgba(184, 166, 245, 0.65);
        border-radius: 24px;
        box-shadow: 0 16px 34px rgba(125, 115, 174, 0.22);
        padding: 1.1rem 1.3rem;
        margin-bottom: 1rem;
        position: relative;
        overflow: hidden;
    }
    .hero::before {
        content: "✨ 🌈 🫧";
        position: absolute;
        right: 1rem;
        top: .7rem;
        letter-spacing: .3rem;
        opacity: .6;
    }
    .flashcard {
        border-radius: 22px;
        padding: 1.2rem;
        margin-bottom: .8rem;
        background-image:
            radial-gradient(circle at 12% 12%, rgba(255, 255, 255, 0.45) 0%, transparent 26%),
            radial-gradient(circle at 80% 76%, rgba(255, 255, 255, 0.30) 0%, transparent 30%);
        border: 1px solid rgba(255, 255, 255, 0.95);
        box-shadow: 0 18px 30px rgba(99, 108, 142, 0.24);
        position: relative;
        overflow: hidden;
        animation: cardIn .42s ease-out;
        transition: transform .25s ease, box-shadow .25s ease;
    }
    .flashcard:hover {
        transform: translateY(-2px);
        box-shadow: 0 22px 32px rgba(99, 108, 142, 0.28);
    }
    .flashcard::after {
        content: "";
        position: absolute;
        right: -45px;
        top: -45px;
        width: 130px;
        height: 130px;
        background: rgba(255, 255, 255, .46);
        border-radius: 50%;
        z-index: 0;
    }
    .flashcard::before {
        content: "";
        position: absolute;
        left: -40px;
        bottom: -40px;
        width: 120px;
        height: 120px;
        background: rgba(255, 255, 255, .32);
        border-radius: 50%;
        z-index: 0;
    }
    .flashcard > * { position: relative; z-index: 1; }
    .pastel-a { background: linear-gradient(145deg, #ffe6f2 0%, #ffdced 100%); }
    .pastel-b { background: linear-gradient(145deg, #e7f4ff 0%, #dcecff 100%); }
    .pastel-c { background: linear-gradient(145deg, #e6fff2 0%, #d7f8e8 100%); }
    .pastel-d { background: linear-gradient(145deg, #fff8dd 0%, #ffefc4 100%); }
    .chip {
        display: inline-block;
        padding: .22rem .7rem;
        border-radius: 999px;
        font-size: .82rem;
        font-weight: 800;
        letter-spacing: .04em;
        color: #2d2942;
    }
    .myth { background: rgba(255, 110, 146, 0.33); border: 1px solid rgba(201, 63, 105, 0.65); }
    .fact { background: rgba(99, 214, 150, 0.35); border: 1px solid rgba(39, 161, 103, 0.62); }
    .subtle { opacity: .88; color: #3b3658; }
    .decor {
        font-size: 1.1rem;
        opacity: 0.75;
        margin-top: .3rem;
    }
    .statement-tag {
        display: inline-block;
        background: rgba(255, 255, 255, 0.75);
        color: #3b325d;
        border: 1px dashed rgba(138, 118, 211, 0.6);
        border-radius: 999px;
        font-size: .78rem;
        padding: .18rem .6rem;
        margin-bottom: .3rem;
        font-weight: 700;
    }
    .statement-text {
        margin: .15rem 0 .65rem 0;
        color: #2a2543;
        font-size: 1.06rem;
        font-weight: 600;
        line-height: 1.5;
    }

    /* Strong contrast buttons */
    .stButton > button {
        background: #ffffff !important;
        color: #2a2543 !important;
        border: 1px solid #bfaee8 !important;
        font-weight: 800 !important;
        box-shadow: 0 4px 10px rgba(80, 60, 140, 0.10) !important;
    }
    .stButton > button:hover {
        background: #efe8ff !important;
        color: #1f1a35 !important;
        border-color: #9e88dc !important;
    }
    .stButton > button:focus,
    .stButton > button:focus-visible,
    .stButton > button:active {
        color: #1f1a35 !important;
        border-color: #8f78d8 !important;
        box-shadow: 0 0 0 0.2rem rgba(143, 120, 216, 0.25) !important;
    }

    @keyframes cardIn {
        from { opacity: 0; transform: translateY(8px) scale(.99); }
        to { opacity: 1; transform: translateY(0) scale(1); }
    }
    @keyframes flipCard {
        0% { transform: perspective(1000px) rotateY(0deg) scale(1); }
        50% { transform: perspective(1000px) rotateY(90deg) scale(0.98); }
        100% { transform: perspective(1000px) rotateY(0deg) scale(1); }
    }
    @keyframes nextCard {
        0% { transform: translateX(26px) scale(0.98); opacity: .15; }
        100% { transform: translateX(0) scale(1); opacity: 1; }
    }
    .animate-flip {
        animation: flipCard .55s ease;
        transform-origin: center;
        will-change: transform;
    }
    .animate-next {
        animation: nextCard .38s ease-out;
        will-change: transform, opacity;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class='hero'>
        <h2 style='margin: 0;'>🎯 Tongues of Deception: The Myths we speak</h2>
        <p class='subtle' style='margin: .3rem 0 0 0;'>Pick Myth or Fact, flip to reveal, and learn from each explanation.</p>
        <div class='decor'>🧠 💬 🌸 📘</div>
    </div>
    """,
    unsafe_allow_html=True,
)

card_total = len(st.session_state.deck)
col1, col2, col3 = st.columns(3)
col1.metric("Score", f"{st.session_state.score}")
col2.metric("Card", f"{min(st.session_state.index + 1, card_total)}/{card_total}")
progress = st.session_state.index / card_total if card_total else 0
col3.metric("Progress", f"{progress * 100:.0f}%")
st.progress(progress)

if st.session_state.index >= card_total:
    st.success(f"🎉 You finished! Final score: {st.session_state.score}/{card_total}")
    if st.button("🔄 Play Again", use_container_width=True):
        restart_game()
        st.rerun()
    st.stop()

card = CARDS[st.session_state.deck[st.session_state.index]]
pastel_class = ["pastel-a", "pastel-b", "pastel-c", "pastel-d"][st.session_state.index % 4]
anim_class = ""
if st.session_state.last_action == "flip":
    anim_class = "animate-flip"
elif st.session_state.last_action == "next":
    anim_class = "animate-next"
st.session_state.last_action = ""

st.markdown(f"<div class='flashcard {pastel_class} {anim_class}'>", unsafe_allow_html=True)
st.markdown("<span class='statement-tag'>✨ Statement Card</span>", unsafe_allow_html=True)
st.markdown("### 🗣️ Statement")
st.markdown(f"<p class='statement-text'>{card['statement']}</p>", unsafe_allow_html=True)

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
    st.session_state.last_action = "flip"
    st.rerun()

if st.session_state.flipped:
    label = str(card["label"])
    cls = "fact" if label == "FACT" else "myth"
    icon = "✅" if label == "FACT" else "🧠"
    st.markdown(f"<span class='chip {cls}'>{icon} {label}</span>", unsafe_allow_html=True)
    st.markdown("#### Explanation")
    st.write(card["explanation"])
    st.markdown("#### Discussion starters 💬")
    for item in card["discussion"]:
        st.markdown(f"- {item}")

st.markdown("</div>", unsafe_allow_html=True)

if st.session_state.answered and st.button("➡️ Next Card", use_container_width=True):
    st.session_state.index += 1
    st.session_state.flipped = False
    st.session_state.answered = False
    st.session_state.message = ""
    st.session_state.last_action = "next"
    st.rerun()

with st.sidebar:
    st.header("Settings")
    st.caption(f"Each game uses {FACTS_PER_ROUND} facts + {MYTHS_PER_ROUND} myths (total {ROUND_SIZE}).")
    if st.button("🔄 Restart Game", use_container_width=True):
        restart_game()
        st.rerun()
