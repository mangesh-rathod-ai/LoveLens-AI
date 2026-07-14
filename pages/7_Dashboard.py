import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

from src.database.load_history import load_history

st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
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
content:"📊";
position:absolute;
font-size:150px;
opacity:0.06;
top:-30px;
right:-10px;
transform:rotate(10deg);
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

/* KPI CARDS */
.kpi-card{
background:linear-gradient(160deg, #3A0A18, #200309);
border:1px solid rgba(255,100,130,0.25);
border-radius:20px;
padding:20px 12px;
text-align:center;
box-shadow:0px 10px 26px rgba(0,0,0,0.4);
transition:transform 0.25s ease;
}

.kpi-card:hover{
transform:translateY(-4px);
box-shadow:0px 15px 32px rgba(233,30,99,0.35);
}

.kpi-label{
color:#FFB3C6;
font-size:13px;
font-weight:600;
text-transform:uppercase;
letter-spacing:0.5px;
margin-bottom:6px;
}

.kpi-value{
color:#FFFFFF;
font-size:30px;
font-weight:800;
text-shadow:0px 0px 16px rgba(255,60,90,0.5);
}

.kpi-yes .kpi-value{ color:#4EF0A0; text-shadow:0px 0px 16px rgba(78,240,160,0.5); }
.kpi-maybe .kpi-value{ color:#FFD35C; text-shadow:0px 0px 16px rgba(255,211,92,0.5); }
.kpi-no .kpi-value{ color:#FF6E8E; text-shadow:0px 0px 16px rgba(255,110,142,0.5); }

/* SECTION TITLE */
.section-title{
color:#FF6FA4;
font-size:22px;
font-weight:800;
margin-top:8px;
margin-bottom:14px;
}

/* CHART CARD */
.chart-card{
background:#2A0812;
border:1px solid rgba(255,105,150,0.18);
border-radius:20px;
padding:14px;
box-shadow:0px 8px 24px rgba(0,0,0,0.35);
margin-bottom:22px;
}

/* TABLE WRAPPER */
.table-wrap{
background:#2A0812;
border:1px solid rgba(255,105,150,0.18);
border-radius:18px;
padding:14px;
box-shadow:0px 8px 22px rgba(0,0,0,0.35);
}

div[data-testid="stDataFrame"]{
border-radius:14px;
overflow:hidden;
}

/* WARNING BOX */
.warn-box{
background:linear-gradient(150deg, #33091A, #1E0410);
border-left:5px solid #FF4D88;
border-radius:18px;
padding:26px;
color:#FFE3EC;
font-size:16px;
text-align:center;
box-shadow:0px 10px 25px rgba(0,0,0,0.4);
}

hr{ border-color:rgba(255,110,140,0.15) !important; }

</style>
""", unsafe_allow_html=True)

# =====================================================
# HERO
# =====================================================

st.markdown("""
<div class="rose-hero">
<h1>📊 LoveLens AI Dashboard</h1>
<p>An overview of every prediction LoveLens AI has ever made.</p>
</div>
""", unsafe_allow_html=True)

# =====================================================
# LOAD DATA
# =====================================================

history = load_history()

if history.empty:
    st.markdown("""
    <div class="warn-box">
        💔 No prediction data available yet.<br>
        <span style="font-size:14px;opacity:0.75;">
            Complete a prediction from the Result page to populate this dashboard.
        </span>
    </div>
    """, unsafe_allow_html=True)
    st.stop()

# =====================================================
# ROSE-THEMED PLOTLY TEMPLATE
# =====================================================

ROSE_COLORS = ["#E91E63", "#FFD35C", "#FF6E8E", "#4EF0A0", "#FF9EB8", "#B0083A"]

PLOTLY_LAYOUT = dict(
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font=dict(color="#FFE3EC"),
    title_font=dict(color="#FF9EB8", size=18),
    legend=dict(bgcolor="rgba(0,0,0,0)"),
    margin=dict(t=60, b=40, l=20, r=20),
)

# =====================================================
# KPIs
# =====================================================

total_predictions = len(history)
yes_count = len(history[history["prediction"] == "❤️ YES"])
maybe_count = len(history[history["prediction"] == "😊 MAYBE"])
no_count = len(history[history["prediction"] == "💔 NO"])
avg_score = round(history["love_score"].mean(), 2)
avg_confidence = round(history["confidence"].mean(), 2)
match_rate = round((yes_count / total_predictions) * 100, 1) if total_predictions else 0

st.markdown('<div class="section-title">📌 Key Metrics</div>', unsafe_allow_html=True)

k1, k2, k3, k4, k5, k6 = st.columns(6)

with k1:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-label">Total</div>
        <div class="kpi-value">{total_predictions}</div>
    </div>
    """, unsafe_allow_html=True)

with k2:
    st.markdown(f"""
    <div class="kpi-card kpi-yes">
        <div class="kpi-label">❤️ Yes</div>
        <div class="kpi-value">{yes_count}</div>
    </div>
    """, unsafe_allow_html=True)

with k3:
    st.markdown(f"""
    <div class="kpi-card kpi-maybe">
        <div class="kpi-label">😊 Maybe</div>
        <div class="kpi-value">{maybe_count}</div>
    </div>
    """, unsafe_allow_html=True)

with k4:
    st.markdown(f"""
    <div class="kpi-card kpi-no">
        <div class="kpi-label">💔 No</div>
        <div class="kpi-value">{no_count}</div>
    </div>
    """, unsafe_allow_html=True)

with k5:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-label">Avg Score</div>
        <div class="kpi-value">{avg_score}%</div>
    </div>
    """, unsafe_allow_html=True)

with k6:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-label">Avg Confidence</div>
        <div class="kpi-value">{avg_confidence}%</div>
    </div>
    """, unsafe_allow_html=True)

st.write("")
st.markdown(f"""
<div class="kpi-card" style="margin-bottom:10px;">
    <div class="kpi-label">💘 Match Rate (share of "YES" predictions)</div>
    <div class="kpi-value">{match_rate}%</div>
</div>
""", unsafe_allow_html=True)

st.write("")
st.divider()

# =====================================================
# CHARTS ROW 1 — Pie + Score Distribution
# =====================================================

st.markdown('<div class="section-title">📈 Prediction Insights</div>', unsafe_allow_html=True)

chart_col1, chart_col2 = st.columns(2)

with chart_col1:
    st.markdown('<div class="chart-card">', unsafe_allow_html=True)
    pie = px.pie(
        history,
        names="prediction",
        title="Prediction Distribution",
        color="prediction",
        color_discrete_sequence=ROSE_COLORS,
        hole=0.45
    )
    pie.update_layout(PLOTLY_LAYOUT)
    pie.update_traces(textfont_color="#FFFFFF", marker=dict(line=dict(color="#1A0207", width=2)))
    st.plotly_chart(pie, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

with chart_col2:
    st.markdown('<div class="chart-card">', unsafe_allow_html=True)
    hist = px.histogram(
        history,
        x="love_score",
        nbins=10,
        title="Love Score Distribution",
        color_discrete_sequence=["#E91E63"]
    )
    hist.update_layout(PLOTLY_LAYOUT)
    hist.update_xaxes(gridcolor="rgba(255,255,255,0.06)")
    hist.update_yaxes(gridcolor="rgba(255,255,255,0.06)")
    st.plotly_chart(hist, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# =====================================================
# CHARTS ROW 2 — Bar + Scatter
# =====================================================

chart_col3, chart_col4 = st.columns(2)

with chart_col3:
    st.markdown('<div class="chart-card">', unsafe_allow_html=True)
    bar = px.bar(
        history,
        x="username",
        y="love_score",
        color="prediction",
        title="Love Score by User",
        color_discrete_sequence=ROSE_COLORS
    )
    bar.update_layout(PLOTLY_LAYOUT)
    bar.update_xaxes(gridcolor="rgba(255,255,255,0.06)")
    bar.update_yaxes(gridcolor="rgba(255,255,255,0.06)")
    st.plotly_chart(bar, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

with chart_col4:
    st.markdown('<div class="chart-card">', unsafe_allow_html=True)
    scatter = px.scatter(
        history,
        x="love_score",
        y="confidence",
        color="prediction",
        size="love_score",
        hover_name="username",
        title="Love Score vs Confidence",
        color_discrete_sequence=ROSE_COLORS
    )
    scatter.update_layout(PLOTLY_LAYOUT)
    scatter.update_xaxes(gridcolor="rgba(255,255,255,0.06)")
    scatter.update_yaxes(gridcolor="rgba(255,255,255,0.06)")
    st.plotly_chart(scatter, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# =====================================================
# TOP USERS
# =====================================================

if "username" in history:
    st.markdown('<div class="section-title">🏆 Top Love Scores</div>', unsafe_allow_html=True)
    top_users = history.sort_values("love_score", ascending=False).head(5)[
        ["username", "love_score", "confidence", "prediction"]
    ]

    st.markdown('<div class="table-wrap">', unsafe_allow_html=True)
    st.dataframe(top_users, use_container_width=True, hide_index=True)
    st.markdown('</div>', unsafe_allow_html=True)

st.write("")
st.divider()

# =====================================================
# RECENT PREDICTIONS
# =====================================================

st.markdown('<div class="section-title">🕒 Recent Predictions</div>', unsafe_allow_html=True)

st.markdown('<div class="table-wrap">', unsafe_allow_html=True)
st.dataframe(
    history,
    use_container_width=True,
    hide_index=True
)
st.markdown('</div>', unsafe_allow_html=True)

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