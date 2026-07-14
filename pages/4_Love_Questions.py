import streamlit as st
from src.questions.question_loader import load_questions

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Love Questions",
    page_icon="❤️",
    layout="wide"
)

# =====================================================
# CUSTOM CSS
# =====================================================

st.markdown("""
<style>

#MainMenu{
visibility:hidden;
}

footer{
visibility:hidden;
}

header{
visibility:hidden;
}

.stApp{
background:linear-gradient(
135deg,
#160A12,
#1E1118,
#2A1520
);
}

.block-container{
padding-top:2rem;
padding-left:5%;
padding-right:5%;
}

.hero{
background:linear-gradient(
135deg,
#2A1622,
#341C28
);
padding:35px;
border-radius:25px;
box-shadow:0px 10px 30px rgba(233,30,99,.35);
margin-bottom:25px;
}

.hero h1{
color:white;
font-size:52px;
font-weight:800;
margin-bottom:5px;
}

.hero p{
color:#FFD5E5;
font-size:20px;
}

.question-card{
background:#24131D;
padding:30px;
border-radius:20px;
border:1px solid rgba(255,105,180,.30);
box-shadow:0px 8px 25px rgba(0,0,0,.30);
margin-top:25px;
}

.category{
color:#FF6FA4;
font-size:18px;
font-weight:bold;
}

.question{
color:white;
font-size:28px;
font-weight:700;
margin-top:10px;
margin-bottom:20px;
}

.info-card{
background:#2E1823;
padding:20px;
border-left:5px solid #FF4D88;
border-radius:15px;
color:white;
margin-top:25px;
}

.stButton>button{
width:100%;
height:55px;
background:linear-gradient(
90deg,
#E91E63,
#FF5E98
);
border:none;
color:white;
font-size:18px;
font-weight:bold;
border-radius:15px;
}

.stButton>button:hover{
transform:translateY(-3px);
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# LOAD QUESTIONS
# =====================================================

questions = load_questions()
TOTAL_QUESTIONS = len(questions)

# =====================================================
# SESSION STATE
# =====================================================

if "current_question" not in st.session_state:
    st.session_state.current_question = 0

if "answers" not in st.session_state:
    st.session_state.answers = {}

# =====================================================
# HERO
# =====================================================

st.markdown("""
<div class="hero">
<h1>❤️ Love Compatibility Assessment</h1>
<p>
Answer all 50 questions honestly.
Our AI Decision Engine will generate your
Love Score, Confidence Score,
Prediction and AI Explanation.
</p>
</div>
""", unsafe_allow_html=True)

# =====================================================
# PROGRESS
# =====================================================

progress = (st.session_state.current_question + 1) / TOTAL_QUESTIONS
st.progress(progress)

st.write(
    f"### Question {st.session_state.current_question + 1} of {TOTAL_QUESTIONS}"
)

# =====================================================
# CURRENT QUESTION
# =====================================================

current_index = st.session_state.current_question
question = questions[current_index]
category = question["category"]
text = question["question"]

st.markdown(
    f"""
<div class="question-card">
<div class="category">
📂 {category}
</div>
<div class="question">
{text}
</div>
""",
    unsafe_allow_html=True
)

options = ["Never", "Rarely", "Sometimes", "Often", "Always"]

# Pre-select the previously saved answer for this question, if any
existing_answer = st.session_state.answers.get(current_index)
default_index = options.index(existing_answer) if existing_answer in options else None

selected = st.radio(
    "Choose your answer",
    options,
    horizontal=False,
    index=default_index,
    key=f"question_{current_index}"
)

st.markdown("</div>", unsafe_allow_html=True)
st.write("")

# =====================================================
# SAVE ANSWER
# =====================================================

if selected is not None:
    st.session_state.answers[current_index] = selected

# =====================================================
# NAVIGATION
# =====================================================

nav_col1, nav_col2 = st.columns(2)

with nav_col1:
    if st.button("⬅️ Previous", use_container_width=True, disabled=current_index == 0):
        st.session_state.current_question -= 1
        st.rerun()

with nav_col2:
    if st.button("Next ➡️", use_container_width=True, disabled=current_index >= TOTAL_QUESTIONS - 1):
        st.session_state.current_question += 1
        st.rerun()

# =====================================================
# PROGRESS VARIABLES
# =====================================================

answers = st.session_state.get("answers", {})
completed = len(answers)
remaining = TOTAL_QUESTIONS - completed
percentage = int((completed / TOTAL_QUESTIONS) * 100)

# =====================================================
# FINAL SECTION
# =====================================================

st.divider()

if completed == TOTAL_QUESTIONS:
    st.success("🎉 Congratulations! You have completed all 50 questions.")
    st.balloons()
else:
    st.info(f"Answer {remaining} more question(s) to complete the assessment.")

# =====================================================
# FINISH ASSESSMENT
# =====================================================

finish = st.button("❤️ Finish Assessment", use_container_width=True)

if finish:
    if completed != TOTAL_QUESTIONS:
        st.error(f"Please answer all {TOTAL_QUESTIONS} questions before continuing.")
    else:
        st.success("Generating your AI Prediction...")
        st.session_state["assessment_completed"] = True
        st.switch_page("pages/5_Result.py")

# =====================================================
# ANSWER SUMMARY
# =====================================================

st.divider()
st.subheader("📋 Assessment Summary")

summary_col1, summary_col2, summary_col3 = st.columns(3)

with summary_col1:
    st.metric("❤️ Total Questions", TOTAL_QUESTIONS)

with summary_col2:
    st.metric("✅ Answered", completed)

with summary_col3:
    st.metric("⏳ Remaining", remaining)

# =====================================================
# COMPLETION PROGRESS
# =====================================================

st.progress(completed / TOTAL_QUESTIONS)
st.write(f"### Progress : {percentage}%")

# =====================================================
# CATEGORY INFORMATION
# =====================================================

st.divider()
st.subheader("📚 Question Categories")

categories = [
    "💬 Communication",
    "🤝 Trust",
    "❤️ Emotional Connection",
    "🌱 Personal Growth",
    "🎯 Compatibility",
    "💞 Commitment"
]

cols = st.columns(3)
for i, cat in enumerate(categories):
    with cols[i % 3]:
        st.success(cat)

# =====================================================
# TIPS
# =====================================================

st.divider()
st.subheader("💡 Tips")

st.info("""
✔ Answer honestly.

✔ Don't rush.

✔ There are no right or wrong answers.

✔ Better answers produce better AI explanations.

✔ Results are generated for entertainment purposes.
""")

# =====================================================
# FOOTER
# =====================================================

st.divider()
st.markdown(
    """
<div style="text-align:center;padding:20px;">
<h3 style="color:#FF4D88;">
❤️ LoveLens AI
</h3>
<p style="color:gray;">
AI Powered Relationship Prediction System
</p>
<p style="color:gray;font-size:14px;">
Python • Streamlit • SQLite • Rule-Based AI
</p>
</div>
""",
    unsafe_allow_html=True
)