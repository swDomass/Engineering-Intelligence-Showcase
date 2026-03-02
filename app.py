import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import time

# --- PAGE CONFIG ---
st.set_page_config(page_title="Linked Engineering | Showcase", page_icon="⚙️", layout="wide")

# --- CUSTOM CSS (Linked Engineering Blueprint Fusion) ---
st.markdown("""
    <style>
    /* Blueprint Background Pattern */
    .stApp {
        background-color: #0d1117;
        background-image: 
            linear-gradient(rgba(108, 175, 43, 0.05) 1px, transparent 1px),
            linear-gradient(90deg, rgba(108, 175, 43, 0.05) 1px, transparent 1px);
        background-size: 50px 50px;
    }

    /* Brand Typography */
    @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;700&family=JetBrains+Mono&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Space Grotesk', sans-serif;
        color: #c9d1d9;
    }

    /* Header & Logos */
    [data-testid="stHeader"] {
        background: rgba(13, 17, 23, 0.95);
        backdrop-filter: blur(10px);
        border-bottom: 1px solid #30363d;
    }

    /* Technical Style for Metrics */
    [data-testid="stMetricValue"] {
        font-family: 'JetBrains Mono', monospace;
        color: #6caf2b;
        font-size: 2rem !important;
    }

    /* Modern Tabs Styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background-color: rgba(10, 22, 40, 0.8);
        padding: 8px;
        border-radius: 12px;
        border: 1px solid #30363d;
    }
    .stTabs [data-baseweb="tab"] {
        border-radius: 6px;
        padding: 8px 24px;
        color: #8b949e;
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.85rem;
    }
    .stTabs [aria-selected="true"] {
        background-color: #6caf2b;
        color: #0d1117 !important;
        font-weight: bold;
    }

    /* Buttons (Blueprint Style) */
    div.stButton > button:first-child {
        background-color: #6caf2b;
        color: #010409;
        border: none;
        border-radius: 8px;
        font-weight: 700;
        padding: 0.6rem 2rem;
        transition: all 0.3s ease;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    div.stButton > button:first-child:hover {
        background-color: #5a9624;
        box-shadow: 0 0 20px rgba(108, 175, 43, 0.3);
    }

    /* Cards / Containers */
    .stAlert {
        background-color: rgba(10, 22, 40, 0.6);
        border: 1px solid #30363d;
        border-left: 5px solid #6caf2b;
    }
    </style>
""", unsafe_allow_html=True)

# --- HEADER SECTION ---
col_logo, col_title = st.columns([1, 4])
with col_title:
    st.title("Linked Engineering Intelligence")
    st.markdown("*Showcase Dashboard | Specialized in Engineering-Python & AI Automation*")

st.divider()

# --- DASHBOARD TABS ---
tab_home, tab_ai, tab_eeg, tab_signal, tab_sales = st.tabs([
    "01_OVERVIEW", "02_AI_ORCHESTRATOR", "03_EEG_DATA", "04_SIGNAL_PROC", "05_SALES_AI"
])

# --- TAB: HOME ---
with tab_home:
    col_l, col_r = st.columns([3, 2])
    with col_l:
        st.markdown("""
        ### Blueprint: Professional Engineering Solutions
        Als **Mechanical Engineer** kombiniere ich Domänenwissen aus dem Maschinenbau mit moderner Software-Entwicklung.
        
        #### Fokusbereiche:
        - **Automatisierte Auswertung** von Zeitrohdaten (Campbell, NVH)
        - **Intelligente Agenten-Steuerung** für komplexe Engineering-Workflows
        - **Datengetriebene Prozessoptimierung** im KMU-Bereich
        """)
        st.info("⚡ Live-Interaktion in den technischen Modul-Tabs möglich.")
    
    with col_r:
        st.metric("Tech-Stack Projects", "15+", delta="3 (Q1)")
        st.metric("Automation Rate", "85%", delta="+10%")

# --- TAB: AI ORCHESTRATOR ---
with tab_ai:
    st.subheader("🤖 Autonomous Task Orchestration")
    st.write("Verwaltung und Verteilung von Tasks an Claude, Gemini und Codex via Multi-Agent-Routing.")
    
    if st.button("RUN PIPELINE"):
        progress_bar = st.progress(0)
        status_text = st.empty()
        tasks = ["Checking FEA Code", "Generating Report", "Syncing Database", "Updating Documentation"]
        for i, task in enumerate(tasks):
            status_text.code(f"EXECUTE: {task}...")
            time.sleep(1)
            progress_bar.progress((i + 1) / len(tasks))
        st.success("PIPELINE COMPLETED SUCCESSFULLY")

# --- TAB: EEG ---
with tab_eeg:
    st.subheader("🧠 EEG Neural Data Processing")
    st.write("Wissenschaftliche Aufbereitung neurologischer Zeitreihen-Daten.")
    
    t = np.linspace(0, 2, 1000)
    signal = np.sin(2 * np.pi * 10 * t) * 20 + np.random.normal(0, 5, 1000)
    
    fig = px.line(x=t, y=signal, labels={'x': 'TIME [S]', 'y': 'AMPLITUDE [µV]'}, 
                 title="SIGNAL STREAM: PROCESSED DATA")
    fig.update_layout(template="plotly_dark", plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', 
                     font_family="JetBrains Mono", font_color="#6caf2b")
    st.plotly_chart(fig, use_container_width=True)

# --- TAB: SIGNAL PROCESSING ---
with tab_signal:
    st.subheader("⚙️ NVH Signal Processing")
    st.write("Transformation von Zeitrohdaten zu Campbell-Diagrammen für Schwingungsanalysen.")
    
    speeds = np.linspace(500, 5000, 50)
    freqs = np.linspace(0, 1000, 100)
    z = np.random.rand(100, 50)
    
    fig = go.Figure(data=go.Heatmap(z=z, x=speeds, y=freqs, colorscale='Greens'))
    fig.update_layout(title="CAMPBELL DIAGRAM: SPECTRAL ANALYSIS", template="plotly_dark",
                     paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_family="JetBrains Mono")
    st.plotly_chart(fig, use_container_width=True)

# --- TAB: SALES AI ---
with tab_sales:
    st.subheader("📊 Sales Pipeline Automation")
    st.write("KI-basiertes Lead-Mining und CRM-Steuerung für Linked Engineering.")
    
    data = {'KW': ['05', '06', '07', '08'], 'Leads': [45, 82, 63, 110], 'Relevance': [12, 28, 15, 42]}
    df = pd.DataFrame(data)
    
    fig = px.bar(df, x='KW', y=['Leads', 'Relevance'], barmode='group', 
                 title="PERFORMANCE: SALES AGENT", color_discrete_map={'Leads': '#30363d', 'Relevance': '#6caf2b'})
    fig.update_layout(template="plotly_dark", paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_family="JetBrains Mono")
    st.plotly_chart(fig, use_container_width=True)

# --- FOOTER & CONTACT ---
st.divider()
st.sidebar.markdown("### 🌐 NETWORK")
st.sidebar.markdown("🔗 **[LinkedIn Profile](https://www.linkedin.com/in/dominik-f-840ab919a/)**")
st.sidebar.markdown("---")
st.sidebar.caption("© 2026 Linked Engineering Showcase Dashboard")
