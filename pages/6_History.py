import streamlit as st

from src.database.load_history import load_history

st.set_page_config(
    page_title="Prediction History",
    page_icon="📜",
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
padding:40px;
border-radius:28px;
border:1px solid rgba(255,80,110,0.35);
box-shadow:0px 15px 45px rgba(139,0,30,0.45), inset 0px 0px 60px rgba(255,0,60,0.06);
margin-bottom:28px;
overflow:hidden;
}

.rose-hero::before{
content:"📜";
position:absolute;
font-size:150px;
opacity:0.06;
top:-30px;
right:-10px;
transform:rotate(12deg);
}

.rose-hero h1{
color:#FFF0F3;
font-size:42px;
font-weight:900;
margin-bottom:4px;
text-shadow:0px 0px 25px rgba(255,60,90,0.5);
}

.rose-hero p{
color:#FFC2D1;
font-size:16px;
opacity:0.85;
}

/* STAT CARDS */
.stat-card{
background:linear-gradient(160deg, #3A0A18, #200309);
border:1px solid rgba(255,100,130,0.25);
border-radius:20px;
padding:22px;
text-align:center;
box-shadow:0px 10px 26px rgba(0,0,0,0.4);
}

.stat-label{
color:#FFB3C6;
font-size:14px;
font-weight:600;
text-transform:uppercase;
letter-spacing:1px;
margin-bottom:6px;
}

.stat-value{
color:#FFFFFF;
font-size:32px;
font-weight:800;
text-shadow:0px 0px 16px rgba(255,60,90,0.5);
}

/* SEARCH */
div[data-testid="stTextInput"] input{
background:#2A0812 !important;
color:#FFE3EC !important;
border:1px solid rgba(255,105,150,0.3) !important;
border-radius:14px !important;
padding:12px !important;
}

/* EMPTY STATE */
.empty-box{
background:linear-gradient(150deg, #33091A, #1E0410);
border-left:5px solid #FF4D88;
border-radius:18px;
padding:26px;
color:#FFE3EC;
font-size:16px;
text-align:center;
box-shadow:0px 10px 25px rgba(0,0,0,0.4);
}

/* SECTION TITLE */
.section-title{
color:#FF6FA4;
font-size:22px;
font-weight:800;
margin-top:6px;
margin-bottom:14px;
}

/* TABLE WRAPPER */
.table-wrap{
background:#2A0812;
border:1px solid rgba(255,105,150,0.18);
border-radius:18px;
padding:14px;
box-shadow:0px 8px 22px rgba(0,0,0,0.35);
margin-bottom:20px;
}

div[data-testid="stDataFrame"]{
border-radius:14px;
overflow:hidden;
}

/* BUTTONS */
.stButton>button, .stDownloadButton>button{
width:100%;
height:52px;
background:linear-gradient(90deg, #B0083A, #E91E63, #FF5E98);
border:none;
color:white;
font-size:16px;
font-weight:700;
border-radius:14px;
box-shadow:0px 8px 20px rgba(233,30,99,0.35);
transition:all 0.25s ease;
}

.stButton>button:hover, .stDownloadButton>button:hover{
transform:translateY(-3px);
box-shadow:0px 12px 28px rgba(255,60,110,0.55);
}

hr{ border-color:rgba(255,110,140,0.15) !important; }

</style>
""", unsafe_allow_html=True)

# =====================================================
# HERO
# =====================================================

st.markdown("""
<div class="rose-hero">
<h1>📜 Prediction History</h1>
<p>Every love prediction you've made, saved and searchable in one place.</p>
</div>
""", unsafe_allow_html=True)

# =====================================================
# LOAD DATA
# =====================================================

history = load_history()

# =====================================================
# SEARCH
# =====================================================

st.markdown('<div class="section-title">🔍 Search</div>', unsafe_allow_html=True)
search = st.text_input(
    "Search Username",
    placeholder="Type a username to filter results...",
    label_visibility="collapsed"
)

filtered = history

if search:
    filtered = filtered[
        filtered["username"].str.contains(search, case=False, na=False)
    ]

st.write("")

# =====================================================
# EMPTY STATE
# =====================================================

if filtered.empty:

    st.markdown("""
    <div class="empty-box">
        💔 No prediction history found.<br>
        <span style="font-size:14px;opacity:0.75;">
            Try a different username, or complete a new prediction from the Result page.
        </span>
    </div>
    """, unsafe_allow_html=True)

else:

    # -------------------------------------------------
    # SUMMARY STATS
    # -------------------------------------------------

    total = len(filtered)
    avg_score = round(filtered["love_score"].mean(), 1) if "love_score" in filtered else 0
    avg_confidence = round(filtered["confidence"].mean(), 1) if "confidence" in filtered else 0

    if "prediction" in filtered:
        yes_count = filtered["prediction"].astype(str).str.contains("YES", case=False, na=False).sum()
    else:
        yes_count = 0

    stat_col1, stat_col2, stat_col3, stat_col4 = st.columns(4)

    with stat_col1:
        st.markdown(f"""
        <div class="stat-card">
            <div class="stat-label">📊 Total Predictions</div>
            <div class="stat-value">{total}</div>
        </div>
        """, unsafe_allow_html=True)

    with stat_col2:
        st.markdown(f"""
        <div class="stat-card">
            <div class="stat-label">❤️ Avg Love Score</div>
            <div class="stat-value">{avg_score}%</div>
        </div>
        """, unsafe_allow_html=True)

    with stat_col3:
        st.markdown(f"""
        <div class="stat-card">
            <div class="stat-label">🎯 Avg Confidence</div>
            <div class="stat-value">{avg_confidence}%</div>
        </div>
        """, unsafe_allow_html=True)

    with stat_col4:
        st.markdown(f"""
        <div class="stat-card">
            <div class="stat-label">💖 "YES" Matches</div>
            <div class="stat-value">{yes_count}</div>
        </div>
        """, unsafe_allow_html=True)

    st.write("")
    st.write("")

    # -------------------------------------------------
    # OPTIONAL PREDICTION FILTER
    # -------------------------------------------------

    if "prediction" in filtered:
        options = ["All"] + sorted(filtered["prediction"].astype(str).unique().tolist())
        choice = st.selectbox("Filter by prediction", options)

        if choice != "All":
            filtered = filtered[filtered["prediction"].astype(str) == choice]

        st.write("")

    # -------------------------------------------------
    # TABLE
    # -------------------------------------------------

    st.markdown('<div class="section-title">📋 Records</div>', unsafe_allow_html=True)

    st.markdown('<div class="table-wrap">', unsafe_allow_html=True)
    st.dataframe(
        filtered,
        use_container_width=True,
        hide_index=True
    )
    st.markdown('</div>', unsafe_allow_html=True)

    # -------------------------------------------------
    # DOWNLOAD
    # -------------------------------------------------

    csv = filtered.to_csv(index=False)

    st.download_button(
        "⬇️ Download History (CSV)",
        csv,
        "prediction_history.csv",
        "text/csv",
        use_container_width=True
    )

# =====================================================
# FOOTER
# =====================================================

st.write("")
st.markdown("""
<div style="text-align:center;padding:24px 0 10px 0;">
<h3 style="color:#FF4D88;">🥀 LoveLens AI</h3>
<p style="color:#B98A97;font-size:13px;">
AI Powered Relationship Prediction System · Entertainment Purposes Only
</p>
</div>
""", unsafe_allow_html=True)