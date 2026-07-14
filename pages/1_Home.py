import streamlit as st

st.set_page_config(
    page_title="LoveLens AI",
    page_icon="❤️",
    layout="wide"
)

# -----------------------------
# Custom CSS
# -----------------------------

st.markdown("""
<style>

.main{
background:linear-gradient(135deg,#160B12,#201018,#2B1822);
}

.block-container{
padding-top:2rem;
padding-left:3rem;
padding-right:3rem;
}

.hero{

background:linear-gradient(135deg,#2B1822,#351D29);

padding:50px;

border-radius:25px;

box-shadow:0px 15px 35px rgba(233,30,99,.30);

}

.hero h1{

font-size:65px;

color:white;

margin-bottom:0;

}

.hero h3{

color:#FF8FB6;

font-size:34px;

}

.hero p{

color:#DDDDDD;

font-size:21px;

line-height:1.8;

}

.feature{

background:#2A1822;

padding:25px;

border-radius:20px;

border:1px solid #E91E63;

transition:.4s;

height:240px;

}

.feature:hover{

transform:translateY(-8px);

box-shadow:0px 15px 35px rgba(233,30,99,.40);

}

.feature h2{

color:white;

text-align:center;

}

.feature p{

color:#CCCCCC;

text-align:center;

}

.stats{

background:#311A25;

padding:25px;

border-radius:18px;

text-align:center;

border:1px solid #E91E63;

}

.stats h1{

color:#FF4D88;

font-size:48px;

margin-bottom:0;

}

.stats p{

color:white;

font-size:18px;

}

</style>
""",unsafe_allow_html=True)

# -----------------------------
# Hero
# -----------------------------

st.markdown("""

<div class="hero">

<h1>❤️ LoveLens AI</h1>

<h3>Can Artificial Intelligence Predict Love?</h3>

<p>

LoveLens AI analyzes your answers to
50 carefully designed relationship questions
using an AI-inspired Decision Engine.

Receive

❤️ Love Score

🎯 Confidence Score

🤖 AI Explanation

📈 Dashboard Analytics

📜 Prediction History

</p>

</div>

""",unsafe_allow_html=True)

st.write("")

col1,col2,col3,col4=st.columns(4)

with col1:

    st.button("❤️ Start Prediction",use_container_width=True)

with col2:

    st.button("📊 Dashboard",use_container_width=True)

with col3:

    st.button("📜 History",use_container_width=True)

with col4:

    st.button("👤 Profile",use_container_width=True)

st.divider()

# -----------------------------
# Features
# -----------------------------

st.header("✨ Features")

c1,c2,c3=st.columns(3)

with c1:

    st.markdown("""

<div class="feature">

<h2>❤️ Love Prediction</h2>

<p>

Predict compatibility using

50 intelligent questions.

</p>

</div>

""",unsafe_allow_html=True)

with c2:

    st.markdown("""

<div class="feature">

<h2>🤖 AI Decision Engine</h2>

<p>

Weighted AI scoring

with explainable prediction.

</p>

</div>

""",unsafe_allow_html=True)

with c3:

    st.markdown("""

<div class="feature">

<h2>📈 Dashboard</h2>

<p>

Interactive analytics

and relationship insights.

</p>

</div>

""",unsafe_allow_html=True)

st.write("")

c4,c5,c6=st.columns(3)

with c4:

    st.markdown("""

<div class="feature">

<h2>👤 Personal Profile</h2>

<p>

Store secure user information.

</p>

</div>

""",unsafe_allow_html=True)

with c5:

    st.markdown("""

<div class="feature">

<h2>📜 Prediction History</h2>

<p>

Save every prediction

inside SQLite database.

</p>

</div>

""",unsafe_allow_html=True)

with c6:

    st.markdown("""

<div class="feature">

<h2>🎯 Confidence Score</h2>

<p>

AI confidence percentage

for every prediction.

</p>

</div>

""",unsafe_allow_html=True)

st.divider()

# -----------------------------
# Statistics
# -----------------------------

st.header("📊 Project Overview")

a,b,c,d=st.columns(4)

with a:

    st.markdown("""

<div class="stats">

<h1>50</h1>

<p>Questions</p>

</div>

""",unsafe_allow_html=True)

with b:

    st.markdown("""

<div class="stats">

<h1>6</h1>

<p>Categories</p>

</div>

""",unsafe_allow_html=True)

with c:

    st.markdown("""

<div class="stats">

<h1>AI</h1>

<p>Decision Engine</p>

</div>

""",unsafe_allow_html=True)

with d:

    st.markdown("""

<div class="stats">

<h1>100%</h1>

<p>Entertainment</p>

</div>

""",unsafe_allow_html=True)

st.divider()

st.info("⚠️ LoveLens AI is built for entertainment and educational purposes only.")