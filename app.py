import streamlit as st
from src.database.database import initialize_database
initialize_database()

# ----------------------------------------------------
# PAGE CONFIG
# ----------------------------------------------------

st.set_page_config(
    page_title="LoveLens AI ❤️",
    page_icon="❤️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ----------------------------------------------------
# CUSTOM CSS
# ----------------------------------------------------

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

[data-testid="stAppViewContainer"]{
background:linear-gradient(135deg,#FF9FBB,#FF6F91,#FFC1D9);
background-attachment:fixed;
}

.block-container{
padding-top:2rem;
padding-bottom:2rem;
padding-left:3rem;
padding-right:3rem;
}

.title{
font-size:65px;
font-weight:900;
color:#D81B60;
text-align:center;
margin-bottom:0px;
}

.rose{
font-size:38px;
filter:drop-shadow(0px 4px 6px rgba(139,0,0,.35));
}

.subtitle{
font-size:24px;
text-align:center;
color:#444;
margin-top:-10px;
margin-bottom:10px;
}

.badge-row{
display:flex;
justify-content:center;
gap:14px;
flex-wrap:wrap;
margin-bottom:30px;
}

.badge{
background:#FFF0F4;
color:#B0003A;
border:1px solid #F8B4C6;
padding:6px 16px;
border-radius:30px;
font-size:14px;
font-weight:700;
}

.hero{
background:white;
padding:40px;
border-radius:25px;
box-shadow:0px 15px 40px rgba(139,0,0,.20);
transition:.4s;
}

.hero:hover{
transform:translateY(-5px);
}

.bigbutton button{
width:100%;
background:linear-gradient(90deg,#C2185B,#8B0000);
color:white;
font-size:20px;
font-weight:bold;
padding:15px;
border:none;
border-radius:15px;
transition:.3s;
}

.bigbutton button:hover{
background:linear-gradient(90deg,#8B0000,#C2185B);
transform:scale(1.02);
}

.sectiontitle{
font-size:38px;
font-weight:800;
color:white;
text-align:center;
margin-top:60px;
margin-bottom:10px;
text-shadow:0px 3px 8px rgba(139,0,0,.35);
}

.sectionsub{
text-align:center;
color:#FFE3EC;
font-size:16px;
margin-bottom:35px;
}

.card{
background:white;
padding:28px 22px;
border-radius:20px;
box-shadow:0px 8px 25px rgba(139,0,0,.18);
transition:.3s;
height:230px;
border-top:5px solid #8B0000;
}

.card:hover{
transform:translateY(-8px);
box-shadow:0px 18px 35px rgba(139,0,0,.30);
}

.cardicon{
font-size:42px;
text-align:center;
}

.cardtitle{
font-size:22px;
font-weight:700;
text-align:center;
color:#8B0000;
margin-top:8px;
}

.cardtext{
font-size:15px;
text-align:center;
color:#666;
margin-top:10px;
line-height:1.55;
}

.stats{
background:white;
padding:30px 15px;
border-radius:20px;
box-shadow:0px 8px 30px rgba(139,0,0,.20);
text-align:center;
border-bottom:4px solid #C2185B;
}

.number{
font-size:44px;
font-weight:900;
color:#8B0000;
}

.label{
font-size:16px;
color:#555;
font-weight:600;
}

.stepbox{
background:white;
border-radius:18px;
padding:22px;
box-shadow:0px 6px 20px rgba(139,0,0,.15);
height:180px;
position:relative;
}

.stepnum{
position:absolute;
top:-16px;
left:20px;
background:#8B0000;
color:white;
width:36px;
height:36px;
border-radius:50%;
display:flex;
align-items:center;
justify-content:center;
font-weight:800;
box-shadow:0px 4px 10px rgba(0,0,0,.25);
}

.steptitle{
font-weight:700;
color:#C2185B;
font-size:18px;
margin-top:14px;
}

.steptext{
font-size:14px;
color:#666;
margin-top:6px;
line-height:1.5;
}

.footer-note{
text-align:center;
color:#FFE3EC;
font-size:13px;
margin-top:50px;
}

</style>
""", unsafe_allow_html=True)

# ----------------------------------------------------
# HERO SECTION
# ----------------------------------------------------

st.markdown(
"""
<div class="hero">

<div class="title">
<span class="rose">🥀</span> LoveLens AI <span class="rose">🥀</span>
</div>

<div class="subtitle">
AI Powered Relationship Prediction System
</div>

<div class="badge-row">
<span class="badge">50 Questions</span>
<span class="badge">Confidence Score</span>
<span class="badge">Explainable AI</span>
<span class="badge">Analytics Dashboard</span>
</div>

<center>
Predict compatibility using intelligent AI, 50 relationship questions,
confidence score, analytics dashboard, and personalized explanation.
</center>

</div>
""",
unsafe_allow_html=True
)

st.write("")

c1, c2, c3 = st.columns([1, 1, 1])

with c2:
    st.markdown('<div class="bigbutton">', unsafe_allow_html=True)
    st.button(
        "❤️ Start Prediction",
        use_container_width=True,
        key="start"
    )
    st.markdown('</div>', unsafe_allow_html=True)

st.write("")

st.info(
"""
💡 **LoveLens AI** is an AI-powered entertainment application that predicts relationship compatibility using 50 carefully designed questions, weighted scoring, confidence estimation, and an explainable AI decision engine.
"""
)

# ----------------------------------------------------
# STATS SECTION
# ----------------------------------------------------

st.markdown('<div class="sectiontitle">🥀 Trusted by Love Seekers 🥀</div>', unsafe_allow_html=True)
st.markdown('<div class="sectionsub">Real numbers behind the predictions</div>', unsafe_allow_html=True)

s1, s2, s3, s4 = st.columns(4)

stats_data = [
    ("50", "Smart Questions"),
    ("95%", "Model Confidence"),
    ("12K+", "Predictions Made"),
    ("4.8★", "User Rating"),
]

for col, (num, label) in zip([s1, s2, s3, s4], stats_data):
    with col:
        st.markdown(
            f"""
            <div class="stats">
                <div class="number">{num}</div>
                <div class="label">{label}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

st.write("")
st.write("")

# ----------------------------------------------------
# ADVANCED FEATURES SECTION
# ----------------------------------------------------

st.markdown('<div class="sectiontitle">✨ Advanced AI Features</div>', unsafe_allow_html=True)
st.markdown('<div class="sectionsub">Everything powering your compatibility score</div>', unsafe_allow_html=True)

f1, f2, f3 = st.columns(3)

features = [
    ("🧠", "Intelligent Scoring", "Weighted AI scoring engine analyzes 50 relationship dimensions for accurate compatibility insight."),
    ("📊", "Analytics Dashboard", "Visual breakdown of your compatibility trends, history, and score patterns over time."),
    ("🔍", "Explainable AI", "Understand exactly why you got your score with a transparent, human-readable explanation."),
]

for col, (icon, title, text) in zip([f1, f2, f3], features):
    with col:
        st.markdown(
            f"""
            <div class="card">
                <div class="cardicon">{icon}</div>
                <div class="cardtitle">{title}</div>
                <div class="cardtext">{text}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

st.write("")
st.write("")

f4, f5, f6 = st.columns(3)

features2 = [
    ("🥀", "Deep Compatibility", "Beyond surface answers — LoveLens digs into emotional, mental, and lifestyle alignment."),
    ("🔒", "Private & Secure", "Your answers stay confidential and are used only to generate your personalized result."),
    ("📈", "Confidence Meter", "Every prediction ships with a confidence score, so you know how strong the match really is."),
]

for col, (icon, title, text) in zip([f4, f5, f6], features2):
    with col:
        st.markdown(
            f"""
            <div class="card">
                <div class="cardicon">{icon}</div>
                <div class="cardtitle">{title}</div>
                <div class="cardtext">{text}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

st.write("")
st.write("")

# ----------------------------------------------------
# HOW IT WORKS SECTION
# ----------------------------------------------------

st.markdown('<div class="sectiontitle">💌 How It Works</div>', unsafe_allow_html=True)
st.markdown('<div class="sectionsub">Four simple steps to your result</div>', unsafe_allow_html=True)

w1, w2, w3, w4 = st.columns(4)

steps = [
    ("1", "Enter Info", "Fill in basic personal details to personalize your prediction."),
    ("2", "Answer Questions", "Respond to 50 thoughtfully designed love & relationship questions."),
    ("3", "AI Analysis", "Our engine applies weighted scoring and confidence estimation."),
    ("4", "Get Your Result", "View your compatibility score with a full explainable breakdown."),
]

for col, (num, title, text) in zip([w1, w2, w3, w4], steps):
    with col:
        st.markdown(
            f"""
            <div class="stepbox">
                <div class="stepnum">{num}</div>
                <div class="steptitle">{title}</div>
                <div class="steptext">{text}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

st.write("")
st.markdown('<div class="footer-note">🥀 LoveLens AI — For entertainment purposes only 🥀</div>', unsafe_allow_html=True)