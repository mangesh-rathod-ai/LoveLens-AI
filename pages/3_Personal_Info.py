import streamlit as st

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Personal Information",
    page_icon="👤",
    layout="wide"
)

# =====================================================
# CUSTOM CSS
# =====================================================

st.markdown("""
<style>

#MainMenu{visibility:hidden;}
footer{visibility:hidden;}
header{visibility:hidden;}

.stApp{

background:linear-gradient(
135deg,
#160A12,
#1D1018,
#29141F
);

}

.block-container{

padding-top:2rem;
padding-left:5%;
padding-right:5%;

}

/* Hero */

.hero{

background:linear-gradient(
135deg,
#2A1621,
#341C28
);

padding:35px;

border-radius:25px;

box-shadow:0 10px 35px rgba(233,30,99,.30);

margin-bottom:30px;

}

.hero h1{

color:white;

font-size:55px;

font-weight:800;

margin-bottom:5px;

}

.hero p{

color:#FFD5E5;

font-size:20px;

}

/* Progress */

.progress-card{

background:#24131D;

padding:20px;

border-radius:20px;

margin-bottom:25px;

border:1px solid #FF4D88;

}

/* Form Card */

.form-card{

background:#24131D;

padding:35px;

border-radius:25px;

border:1px solid rgba(255,105,180,.25);

box-shadow:0 10px 30px rgba(0,0,0,.35);

}

/* Input */

div[data-baseweb="input"]{

border-radius:15px;

}

div[data-baseweb="select"]{

border-radius:15px;

}

/* Button */

.stButton>button{

width:100%;

height:55px;

background:linear-gradient(
90deg,
#E91E63,
#FF5A97
);

color:white;

font-size:18px;

font-weight:bold;

border:none;

border-radius:15px;

transition:.3s;

}

.stButton>button:hover{

transform:translateY(-3px);

box-shadow:0 10px 25px rgba(233,30,99,.35);

}

/* Info */

.info-card{

background:#2C1822;

padding:20px;

border-left:5px solid #FF4D88;

border-radius:15px;

color:white;

margin-top:25px;

}

</style>
""", unsafe_allow_html=True)

# =====================================================
# HERO
# =====================================================

st.markdown("""

<div class="hero">

<h1>👤 Personal Information</h1>

<p>

Tell us a little about yourself before starting
the LoveLens AI prediction.

</p>

</div>

""", unsafe_allow_html=True)

# =====================================================
# PROGRESS
# =====================================================

st.markdown("""

<div class="progress-card">

### ❤️ Step 2 of 7

</div>

""", unsafe_allow_html=True)

st.progress(2/7)

st.write("")

# =====================================================
# FORM
# =====================================================

st.markdown("<div class='form-card'>", unsafe_allow_html=True)

left,right = st.columns(2)

with left:

    full_name = st.text_input(
        "👤 Full Name *",
        placeholder="Enter your full name"
    )

    age = st.number_input(
        "🎂 Age *",
        min_value=18,
        max_value=100,
        value=18
    )

    gender = st.selectbox(
        "🚻 Gender *",
        [
            "Male",
            "Female",
            "Other"
        ]
    )

    country = st.text_input(
        "🌍 Country",
        placeholder="India"
    )

with right:

    occupation = st.text_input(
        "💼 Occupation",
        placeholder="Student / Engineer"
    )

    relationship = st.selectbox(
        "❤️ Relationship Status",
        [
            "Single",
            "Committed",
            "Married",
            "Complicated"
        ]
    )

    prediction_for = st.selectbox(
        "💕 Prediction For",
        [
            "Boyfriend",
            "Girlfriend",
            "Partner",
            "Spouse",
            "Friend"
        ]
    )

    crush_name = st.text_input(
        "💖 Crush Name (Optional)"
    )

st.write("")

continue_btn = st.button(
    "❤️ Continue to Questions"
)

st.markdown("</div>", unsafe_allow_html=True)

# =====================================================
# PRIVACY
# =====================================================

st.markdown("""

<div class="info-card">

### 🔒 Privacy

Your information is stored only inside your
local SQLite database and is never shared.

</div>

""", unsafe_allow_html=True)



# =====================================================
# VALIDATION
# =====================================================

if continue_btn:

    if full_name.strip() == "":

        st.error("❌ Please enter your Full Name.")

        st.stop()

    if age < 18:

        st.error("❌ Age must be at least 18 years.")

        st.stop()

    # ---------------------------------------------
    # Save User Information
    # ---------------------------------------------

    st.session_state["personal_info"] = {

        "full_name": full_name,

        "age": age,

        "gender": gender,

        "country": country,

        "occupation": occupation,

        "relationship": relationship,

        "prediction_for": prediction_for,

        "crush_name": crush_name

    }

    # Username for History

    st.session_state["username"] = full_name

    st.success("✅ Personal Information Saved Successfully!")

    st.balloons()

    st.switch_page("pages/4_Love_Questions.py")


# =====================================================
# SIDEBAR
# =====================================================

with st.sidebar:

    st.markdown("## ❤️ LoveLens AI")

    st.success("Profile Progress")

    st.progress(2/7)

    st.write("")

    st.markdown("### 📌 Current Step")

    st.info("Step 2 : Personal Information")

    st.write("")

    st.markdown("### 🚀 Upcoming")

    st.write("❤️ Love Questions")

    st.write("🤖 AI Prediction")

    st.write("📊 Dashboard")

    st.write("📜 History")

    st.write("")

    st.markdown("---")

    st.caption("Version 1.0")

# =====================================================
# INFORMATION SECTION
# =====================================================

st.write("")

st.markdown("## 💡 Why do we collect this information?")

col1, col2, col3 = st.columns(3)

with col1:

    st.info("""

### 🎯 Better Prediction

Your information helps
LoveLens AI generate
better compatibility
predictions.

""")

with col2:

    st.info("""

### 🤖 Personalized AI

The AI explanation
becomes more relevant
using your profile.

""")

with col3:

    st.info("""

### 🔒 Secure Storage

Everything is stored
inside your local
SQLite database.

""")

# =====================================================
# HOW IT WORKS
# =====================================================

st.write("")

st.markdown("## ⚙️ Prediction Workflow")

st.markdown("""""")
