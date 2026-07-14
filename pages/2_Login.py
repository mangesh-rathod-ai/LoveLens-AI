import streamlit as st
import sqlite3
from pathlib import Path

# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="LoveLens AI | Login",
    page_icon="❤️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================================
# DATABASE PATH
# ==========================================================

DATABASE = Path("database/lovelens.db")

# ==========================================================
# CSS
# ==========================================================

st.markdown("""
<style>

/* Hide Streamlit Branding */

#MainMenu{
visibility:hidden;
}

footer{
visibility:hidden;
}

header{
visibility:hidden;
}

/* Background */

.stApp{

background:
linear-gradient(
135deg,
#160A12 0%,
#1D0F17 40%,
#2A1420 100%
);

}

/* Main Container */

.block-container{

padding-top:2rem;
padding-left:5%;
padding-right:5%;

}

/* Hero */

.hero{

text-align:center;

padding:20px;

margin-bottom:30px;

}

.hero h1{

font-size:60px;

font-weight:800;

color:white;

margin-bottom:10px;

}

.hero h3{

color:#FF78A6;

font-size:28px;

margin-bottom:20px;

}

.hero p{

font-size:18px;

color:#D8D8D8;

line-height:1.8;

}

/* Login Card */

.login-card{

background:rgba(42,20,32,.88);

padding:40px;

border-radius:25px;

border:1px solid rgba(255,105,180,.25);

box-shadow:
0 10px 30px rgba(0,0,0,.4);

}

/* Titles */

.section-title{

font-size:32px;

font-weight:bold;

color:white;

margin-bottom:15px;

}

.section-sub{

color:#CFCFCF;

margin-bottom:30px;

}

/* Input */

div[data-baseweb="input"]{

background:#2E1A26;

border-radius:14px;

}

/* Login Button */

.stButton>button{

width:100%;

height:52px;

background:
linear-gradient(
90deg,
#E91E63,
#FF5E9C
);

color:white;

border:none;

border-radius:14px;

font-size:18px;

font-weight:bold;

transition:.3s;

}

.stButton>button:hover{

transform:translateY(-3px);

box-shadow:
0 10px 25px rgba(233,30,99,.35);

}

/* Divider */

hr{

border:1px solid #412433;

}

/* Info Box */

.info-box{

background:#2C1A25;

padding:18px;

border-left:5px solid #FF4D88;

border-radius:12px;

color:white;

margin-top:25px;

}

/* Footer */

.footer{

text-align:center;

margin-top:40px;

color:#999;

font-size:14px;

}

</style>
""", unsafe_allow_html=True)

# ==========================================================
# HERO
# ==========================================================

st.markdown("""

<div class="hero">

<h1>❤️ LoveLens AI</h1>

<h3>Welcome Back</h3>

<p>

Sign in to continue your relationship journey.

Access your saved predictions,

AI explanations,

history,

and dashboard analytics.

</p>

</div>

""", unsafe_allow_html=True)

# ==========================================================
# LOGIN AREA
# ==========================================================

left, right = st.columns([1,1])

with left:

    st.markdown(
        "<div class='login-card'>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<div class='section-title'>🔐 Login</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<div class='section-sub'>Login using your registered account.</div>",
        unsafe_allow_html=True
    )

    username = st.text_input(
        "👤 Username",
        placeholder="Enter username"
    )

    password = st.text_input(
        "🔑 Password",
        type="password",
        placeholder="Enter password"
    )

    login_btn = st.button("❤️ Login")

    st.markdown(
        "<hr>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<div class='section-title'>Continue as Guest</div>",
        unsafe_allow_html=True
    )

    guest_btn = st.button("👤 Continue as Guest")

    st.markdown(
        "</div>",
        unsafe_allow_html=True
    )

with right:

    st.image(
        "https://images.unsplash.com/photo-1516589178581-6cd7833ae3b2?w=800",
        use_container_width=True
    )

    st.markdown("""

<div class="info-box">

<h4>✨ Why Login?</h4>

✅ Save Prediction History

✅ Personal Dashboard

✅ AI Explanations

✅ Relationship Analytics

✅ Future Updates

</div>

""", unsafe_allow_html=True)

st.markdown("""

<div class="footer">

LoveLens AI © 2026

AI Powered Relationship Prediction

</div>

""", unsafe_allow_html=True)

# ==========================================================
# LOGIN LOGIC
# ==========================================================

def login_user(username, password):
    """
    Login verification
    """

    try:

        conn = sqlite3.connect(DATABASE)

        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT username
            FROM users
            WHERE username=? AND password=?
            """,
            (username, password)
        )

        user = cursor.fetchone()

        conn.close()

        return user

    except Exception as e:

        st.error(f"Database Error : {e}")

        return None


# ==========================================================
# LOGIN BUTTON
# ==========================================================

if login_btn:

    if username == "" or password == "":

        st.warning("⚠ Please enter Username and Password.")

    else:

        user = login_user(username, password)

        if user:

            st.session_state["logged_in"] = True

            st.session_state["guest"] = False

            st.session_state["username"] = username

            st.success(f"❤️ Welcome {username}")

            st.balloons()

            st.switch_page("pages/3_Personal_Info.py")

        else:

            st.error("❌ Invalid Username or Password")


# ==========================================================
# GUEST LOGIN
# ==========================================================

if guest_btn:

    st.session_state["logged_in"] = True

    st.session_state["guest"] = True

    st.session_state["username"] = "Guest"

    st.success("Welcome Guest ❤️")

    st.switch_page("pages/3_Personal_Info.py")


# ==========================================================
# SESSION INFO
# ==========================================================

if "logged_in" not in st.session_state:

    st.session_state["logged_in"] = False

if "guest" not in st.session_state:

    st.session_state["guest"] = False


# ==========================================================
# QUICK INFO
# ==========================================================

st.divider()

c1, c2, c3 = st.columns(3)

with c1:

    st.metric(
        "❤️ Questions",
        "50"
    )

with c2:

    st.metric(
        "🤖 AI Engine",
        "Enabled"
    )

with c3:

    st.metric(
        "📊 Dashboard",
        "Ready"
    )


# ==========================================================
# HOW IT WORKS
# ==========================================================

st.subheader("💖 How LoveLens AI Works")

st.markdown("""

1️⃣ Login or Continue as Guest

⬇

2️⃣ Enter Personal Information

⬇

3️⃣ Answer 50 Love Questions

⬇

4️⃣ AI Decision Engine Calculates

⬇

5️⃣ Love Score Generated

⬇

6️⃣ Confidence Score

⬇

7️⃣ AI Explanation

⬇

8️⃣ Save Prediction History

⬇

9️⃣ Dashboard Analytics

""")


# ==========================================================
# DISCLAIMER
# ==========================================================

st.info(
"""
LoveLens AI is an educational AI project.

Predictions are generated using a rule-based
AI Decision Engine and weighted scoring.

This application is intended for entertainment purposes only.
"""
)


# ==========================================================
# FOOTER
# ==========================================================

st.markdown("---")

st.caption("❤️ LoveLens AI | Version 1.0")

st.caption("Built using Streamlit • SQLite • Python • AI Decision Engine")