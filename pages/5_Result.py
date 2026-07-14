import streamlit as st

from src.scoring.score_engine import calculate_scores
from src.prediction.decision_engine import predict
from src.prediction.confidence_engine import calculate_confidence
from src.prediction.explanation_engine import generate_explanation
from src.database.save_prediction import save_prediction

st.set_page_config(
    page_title="LoveLens AI Result",
    page_icon="❤️",
    layout="wide"
)

# =====================================================
# CUSTOM CSS — DARK ROSE THEME
# =====================================================

st.markdown("""
<style>

#MainMenu{visibility:hidden;}
footer{visibility:hidden;}
header{visibility:hidden;}

.stApp{
background:
radial-gradient(circle at 15% 10%, rgba(233,30,99,0.18), transparent 40%),
radial-gradient(circle at 85% 0%, rgba(139,0,30,0.25), transparent 45%),
linear-gradient(160deg, #1A0207 0%, #2B0410 35%, #3D0A18 65%, #1A0207 100%);
background-attachment: fixed;
}

.block-container{
padding-top:2rem;
padding-left:5%;
padding-right:5%;
}

/* HERO */
.rose-hero{
position:relative;
background:linear-gradient(135deg, #4A0B1E, #2B0410);
padding:45px;
border-radius:28px;
border:1px solid rgba(255,80,110,0.35);
box-shadow:0px 15px 45px rgba(139,0,30,0.45), inset 0px 0px 60px rgba(255,0,60,0.06);
margin-bottom:30px;
overflow:hidden;
text-align:center;
}

.rose-hero::before{
content:"🥀";
position:absolute;
font-size:180px;
opacity:0.07;
top:-40px;
right:-20px;
transform:rotate(15deg);
}

.rose-hero::after{
content:"🥀";
position:absolute;
font-size:140px;
opacity:0.06;
bottom:-50px;
left:-30px;
transform:rotate(-25deg);
}

.rose-hero h1{
color:#FFF0F3;
font-size:46px;
font-weight:900;
margin-bottom:6px;
text-shadow:0px 0px 25px rgba(255,60,90,0.55);
letter-spacing:0.5px;
}

.rose-hero p{
color:#FFC2D1;
font-size:17px;
opacity:0.85;
}

/* KPI CARDS */
.kpi-card{
background:linear-gradient(160deg, #3A0A18, #200309);
border:1px solid rgba(255,100,130,0.25);
border-radius:22px;
padding:26px 20px;
text-align:center;
box-shadow:0px 10px 30px rgba(0,0,0,0.4);
transition:transform 0.25s ease;
}

.kpi-card:hover{
transform:translateY(-4px);
box-shadow:0px 15px 35px rgba(233,30,99,0.35);
}

.kpi-label{
color:#FFB3C6;
font-size:15px;
font-weight:600;
text-transform:uppercase;
letter-spacing:1px;
margin-bottom:8px;
}

.kpi-value{
color:#FFFFFF;
font-size:38px;
font-weight:800;
text-shadow:0px 0px 18px rgba(255,60,90,0.5);
}

/* SECTION HEADERS */
.section-title{
color:#FF6FA4;
font-size:24px;
font-weight:800;
margin-top:10px;
margin-bottom:18px;
display:flex;
align-items:center;
gap:10px;
}

/* CATEGORY CARD */
.cat-card{
background:#2A0812;
border:1px solid rgba(255,105,150,0.18);
border-radius:16px;
padding:18px 22px;
margin-bottom:14px;
box-shadow:0px 6px 18px rgba(0,0,0,0.35);
}

.cat-name{
color:#FFE1E9;
font-size:17px;
font-weight:700;
margin-bottom:8px;
}

.cat-score{
color:#FF9EB8;
font-size:14px;
font-weight:600;
float:right;
}

.bar-track{
width:100%;
height:10px;
background:rgba(255,255,255,0.08);
border-radius:10px;
overflow:hidden;
margin-top:6px;
}

.bar-fill{
height:100%;
border-radius:10px;
background:linear-gradient(90deg, #E91E63, #FF5E98, #FF9AB8);
box-shadow:0px 0px 12px rgba(255,60,110,0.6);
}

/* EXPLANATION BOX */
.explain-box{
background:linear-gradient(150deg, #33091A, #1E0410);
border-left:5px solid #FF4D88;
border-radius:18px;
padding:26px;
color:#FFE3EC;
font-size:16px;
line-height:1.7;
box-shadow:0px 10px 25px rgba(0,0,0,0.4);
}

/* BUTTONS */
.stButton>button{
width:100%;
height:56px;
background:linear-gradient(90deg, #B0083A, #E91E63, #FF5E98);
border:none;
color:white;
font-size:17px;
font-weight:700;
border-radius:16px;
box-shadow:0px 8px 20px rgba(233,30,99,0.35);
transition:all 0.25s ease;
}

.stButton>button:hover{
transform:translateY(-3px);
box-shadow:0px 12px 28px rgba(255,60,110,0.55);
}

/* PREDICTION BADGE */
.pred-badge{
display:inline-block;
padding:8px 22px;
border-radius:30px;
font-size:20px;
font-weight:800;
margin-top:6px;
}

.pred-yes{ background:rgba(46,204,113,0.15); color:#4EF0A0; border:1px solid #4EF0A0; }
.pred-maybe{ background:rgba(255,193,7,0.15); color:#FFD35C; border:1px solid #FFD35C; }
.pred-no{ background:rgba(255,60,90,0.15); color:#FF6E8E; border:1px solid #FF6E8E; }

hr{ border-color:rgba(255,110,140,0.15) !important; }

</style>
""", unsafe_allow_html=True)

# =====================================================
# HERO
# =====================================================

st.markdown("""
<div class="rose-hero">
<h1>🥀 LoveLens AI Result</h1>
<p>Your relationship, decoded by AI — here's what the data says.</p>
</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# Check Answers
# ---------------------------------------------------

if "answers" not in st.session_state:
    st.warning("Please complete the Love Questions first.")
    st.stop()

# ---------------------------------------------------
# Calculate Scores
# ---------------------------------------------------

result = calculate_scores(st.session_state["answers"])
love_score = result["love_score"]
category_scores = result["category_scores"]

# ---------------------------------------------------
# Prediction
# ---------------------------------------------------

prediction = predict(love_score)
confidence = calculate_confidence(love_score)
explanation = generate_explanation(love_score, category_scores)

# ---------------------------------------------------
# Save Session
# ---------------------------------------------------

st.session_state["love_score"] = love_score
st.session_state["prediction"] = prediction
st.session_state["confidence"] = confidence
st.session_state["category_scores"] = category_scores
st.session_state["explanation"] = explanation

# ---------------------------------------------------
# Prediction badge styling helper
# ---------------------------------------------------

if "YES" in prediction:
    badge_class = "pred-yes"
elif "MAYBE" in prediction:
    badge_class = "pred-maybe"
else:
    badge_class = "pred-no"

# ---------------------------------------------------
# KPI CARDS
# ---------------------------------------------------

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-label">❤️ Love Score</div>
        <div class="kpi-value">{love_score}%</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-label">🎯 Confidence</div>
        <div class="kpi-value">{confidence}%</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-label">💖 Prediction</div>
        <div class="pred-badge {badge_class}">{prediction}</div>
    </div>
    """, unsafe_allow_html=True)

st.write("")
st.divider()

# ---------------------------------------------------
# Category Scores
# ---------------------------------------------------

st.markdown('<div class="section-title">📊 Category Scores</div>', unsafe_allow_html=True)

for category, score in category_scores.items():
    st.markdown(f"""
    <div class="cat-card">
        <span class="cat-name">{category}</span>
        <span class="cat-score">{score}%</span>
        <div class="bar-track">
            <div class="bar-fill" style="width:{score}%;"></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# ---------------------------------------------------
# AI Explanation
# ---------------------------------------------------

st.markdown('<div class="section-title">🤖 AI Explanation</div>', unsafe_allow_html=True)
st.markdown(f'<div class="explain-box">{explanation}</div>', unsafe_allow_html=True)

st.write("")
st.divider()

# ---------------------------------------------------
# Save Prediction
# ---------------------------------------------------

prediction_data = {
    "username": st.session_state.get("username", "Guest"),
    "love_score": love_score,
    "confidence": confidence,
    "prediction": prediction,
    "explanation": explanation
}

save_col1, save_col2 = st.columns(2)

with save_col1:
    if st.button("💾 Save Prediction", use_container_width=True):
        try:
            save_prediction(prediction_data)
            st.success("✅ Prediction saved successfully!")
        except Exception as e:
            st.error(f"Database Error : {e}")

with save_col2:
    if st.button("🔄 Predict Again", use_container_width=True):
        st.switch_page("pages/4_Love_Questions.py")

st.divider()

# ---------------------------------------------------
# Celebration
# ---------------------------------------------------

if prediction == "❤️ YES":
    st.balloons()
    st.success("Excellent Compatibility ❤️")
elif prediction == "😊 MAYBE":
    st.warning("There are positive signs 😊")
else:
    st.error("Current answers indicate low compatibility 💔")

# =====================================================
# FOOTER
# =====================================================

st.markdown("""
<div style="text-align:center;padding:30px 0 10px 0;">
<h3 style="color:#FF4D88;">🥀 LoveLens AI</h3>
<p style="color:#B98A97;font-size:13px;">
AI Powered Relationship Prediction System · Entertainment Purposes Only
</p>
</div>
""", unsafe_allow_html=True)