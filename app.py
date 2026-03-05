import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import time

# --- PAGE CONFIG ---
st.set_page_config(page_title="Engineering Intelligence | Showcase", page_icon="⚙️", layout="wide")

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
    st.title("Engineering Intelligence")
    st.markdown("*Showcase Dashboard | Specialized in Engineering-Python & AI Automation*")

st.divider()

# --- DASHBOARD TABS ---
tab_home, tab_ai, tab_eeg, tab_signal, tab_en13001, tab_sales, tab_social = st.tabs([
    "01_OVERVIEW", "02_AI_ORCHESTRATOR", "03_SMART_GRID", "04_SIGNAL_PROC", "05_EN13001_TOOLS", "06_SALES_AI", "07_SOCIAL_MEDIA_AI"
])

# --- TAB: HOME ---
with tab_home:
    st.markdown("""
    ### 🚀 Willkommen beim Engineering Intelligence Showcase
    Willkommen! Ich bin **Maschinenbauingenieur** und **Python-Entwickler**. Meine Spezialisierung liegt an der Schnittstelle zwischen fundiertem technischen Fachwissen, Data Science und moderner KI-gestützter Automatisierung.
    
    Dieses Dashboard dient als **öffentliches Showcase** für meine Projekte in den Bereichen **KI-Orchestrierung, Signalverarbeitung und Prozessautomatisierung**.
    """)

    col_metrics_1, col_metrics_2, col_metrics_3 = st.columns(3)
    with col_metrics_1:
        st.metric("Projekt-Säulen", "6", help="Spezialisierte Engineering- & KI-Domänen")
    with col_metrics_2:
        st.metric("Tech-Stack Projekte", "15+", delta="3 (Q1)")
    with col_metrics_3:
        st.metric("Automatisierungsgrad", "85%", delta="+10%")

    st.divider()

    st.markdown("### 🏗️ Kernbereiche (Project Pillars)")
    
    # Grid für die 6 Säulen (analog zu den Tabs 02-07)
    p_col1, p_col2 = st.columns(2)
    
    with p_col1:
        with st.container(border=True):
            st.markdown("#### 🤖 02. AI Orchestrator")
            st.write("*Autonome Agenten-Steuerung & Multi-Provider Routing.*")
            st.write("Ein robuster Python-Orchestrator mit Markdown-Warteschlange, automatischem Provider-Fallback und Telegram-Anbindung zur Fernsteuerung.")
            st.caption("Tech: Python, Telegram API, Claude/Gemini, Policy Engine")
        
        with st.container(border=True):
            st.markdown("#### ⚙️ 04. Signalverarbeitung")
            st.write("*Automatisierte NVH-Analyse & Campbell-Diagramme.*")
            st.write("Hochleistungs-Pipeline zur Transformation von Zeitrohdaten in ingenieurtechnische Grafiken (FFT, Ordnungsanalyse).")
            st.caption("Tech: NumPy, FFT, Matplotlib, FEM Export (RLOAD)")

        with st.container(border=True):
            st.markdown("#### 📊 06. Sales Intelligence")
            st.write("*KI-gestützte Lead-Generierung & Qualifizierung.*")
            st.write("Automatisierte Pipeline für technisches Lead-Scoring, URL-Enrichment und lokale LLM-basierte Firmenrecherche.")
            st.caption("Tech: Ollama, BeautifulSoup4, Gmail API, SQLite")

    with p_col2:
        with st.container(border=True):
            st.markdown("#### ☀️ 03. Smart Grid Analytics")
            st.write("*EEG-Management & PV-Prognosen.*")
            st.write("Verwaltung von über 2.200 Zählpunkten mit hybrider ML-Architektur (XGBoost/Prophet) für präzise Solar-Ertragsprognosen.")
            st.caption("Tech: uv, SQLite (WAL), XGBoost, Prophet, pvlib")

        with st.container(border=True):
            st.markdown("#### 🏗️ 05. EN13001 Tool-Suite")
            st.write("*Normgerechte Kranstatik & Bauteilauslegung.*")
            st.write("Umfassende Python-Suite für Berechnungen nach DIN EN 13001, inklusive automatisierter PDF-Berichte und Hot-Spot-Ermüdungsanalyse.")
            st.caption("Tech: PyQt6, NumPy, ReportLab, IIW Hot-Spot Methode")

        with st.container(border=True):
            st.markdown("#### 🛋️ 07. Social Media AI")
            st.write("*Creative Automation für den Premium-Retail.*")
            st.write("KI-gesteuerter Content-Lebenszyklus – von der Bildanalyse über plattformübergreifende Texte bis zur regionalen SEO-Optimierung.")
            st.caption("Tech: Vision APIs, WordPress REST, ElevenLabs, Canva")

    st.divider()

    st.markdown("### 🧠 Der Engineering Intelligence Ansatz")
    approach_col1, approach_col2, approach_col3 = st.columns(3)
    
    with approach_col1:
        st.markdown("##### **1. Domain-First Data Science**")
        st.write("Nutzung des Maschinenbau-Hintergrunds, um physikalische Zusammenhänge (Schwingungen, Strahlung) vor der Modellwahl zu verstehen.")
    
    with approach_col2:
        st.markdown("##### **2. Autonome Zuverlässigkeit**")
        st.write("Fokus auf selbstheilende Pipelines, automatisierte Fallback-Mechanismen und proaktives Monitoring via Telegram/Heartbeats.")

    with approach_col3:
        st.markdown("##### **3. Handlungsrelevante Transparenz**")
        st.write("Transformation komplexer 'Black-Box' Daten in klare, verwertbare Erkenntnisse für Entscheidungsträger und Engineering-Workflows.")

    st.info("⚡ Nutzen Sie die Tabs oben, um die technischen Module und deren Live-Simulationen zu erkunden.")

# --- TAB: AI ORCHESTRATOR ---
with tab_ai:
    st.subheader("🤖 Autonomous Task Orchestration")
    st.markdown("""
    *Das Herzstück der Automatisierung: Ein Multi-Agent-System, das Tasks autonom priorisiert, 
    die passenden LLM-Provider (Claude, Gemini, Codex) auswählt und via Telegram gesteuert wird.*
    """)

    # -- Core Benefits & Problem Solving --
    with st.expander("💡 WARUM AI ORCHESTRATION? (PROBLEME & LÖSUNGEN)", expanded=True):
        col_p1, col_p2 = st.columns(2)
        with col_p1:
            st.markdown("### ❌ Die Probleme")
            st.error("""
            - **Fragmentierung:** Ständiges Wechseln zwischen Claude, Gemini & IDE-Tools kostet Zeit.
            - **Ungenutzte Limits:** Teure Abos (Claude Pro) verfallen oft ungenutzt am Tagesende.
            - **Kontext-Verlust:** Manuelles Kopieren von Code & Obsidian-Notizen in Chats ist fehleranfällig.
            - **Fehlende Autonomie:** Standard-KI kann keine iterativen Review-Fix-Test Schleifen.
            - **Sicherheitsrisiken:** Angst vor destruktiven KI-Aktionen (rm -rf, Force-Push).
            """)
        with col_p2:
            st.markdown("### ✅ Meine Lösungen")
            st.success("""
            - **Unified Interface:** Eine Markdown-Queue für alle Provider mit automatischem Fallback.
            - **Usage Suggester:** Proaktive Vorschläge nutzen 100% der Kapazität vor dem Limit-Reset.
            - **Deep Integration:** Direkter Zugriff auf Obsidian Vault (`[[Links]]`) & lokale Repos (`cwd:`).
            - **Skill-Loops:** Autonome `#tool` Schleifen lösen komplexe Aufgaben bis zum Erfolg.
            - **Policy Engine:** Gated Execution (AUTO/APPROVE) mit Telegram-Freigabe-Layer.
            """)

    # -- Status Overview --
    col_s1, col_s2, col_s3, col_s4 = st.columns(4)
    col_s1.metric("Engine Status", "ACTIVE", delta="--watch mode")
    col_s2.metric("Queue Size", "0", delta="All Done")
    col_s3.metric("Avg Success", "94.2%")
    col_s4.metric("Last Heartbeat", "2m ago", delta="OK", delta_color="normal")

    st.divider()

    # -- Visual Analytics (Mocked from real Engine Data) --
    col_left, col_right = st.columns([3, 2])
    
    with col_left:
        st.write("📈 **Provider Capacity (Last 24h)**")
        # Mocking timeline data for capacity
        times = pd.date_range(end=pd.Timestamp.now(), periods=24, freq='H')
        capacity_data = pd.DataFrame({
            'Time': times,
            'Claude': 60 + 30 * np.sin(np.linspace(0, 3, 24)) + np.random.normal(0, 5, 24),
            'Gemini': 80 + 10 * np.cos(np.linspace(0, 3, 24)) + np.random.normal(0, 3, 24),
            'Codex': np.random.uniform(90, 100, 24)
        })
        fig_cap = px.line(capacity_data, x='Time', y=['Claude', 'Gemini', 'Codex'],
                         labels={'value': 'REMAINING %', 'Time': 'TIME (UTC)'},
                         color_discrete_map={'Claude': '#6caf2b', 'Gemini': '#30363d', 'Codex': '#c9d1d9'})
        fig_cap.update_layout(template="plotly_dark", paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', 
                             font_family="JetBrains Mono", legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1))
        st.plotly_chart(fig_cap, use_container_width=True)

    with col_right:
        st.write("📂 **Task Distribution**")
        dist_data = pd.DataFrame({'Provider': ['Claude', 'Gemini', 'Codex'], 'Tasks': [142, 45, 12]})
        fig_pie = px.pie(dist_data, values='Tasks', names='Provider', hole=0.4,
                         color_discrete_sequence=['#6caf2b', '#30363d', '#444c56'])
        fig_pie.update_layout(template="plotly_dark", paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', 
                             font_family="JetBrains Mono", showlegend=False)
        st.plotly_chart(fig_pie, use_container_width=True)

    # -- Live Interaction Mockup --
    st.write("📟 **Live Execution Log**")
    with st.expander("VIEW LIVE ORCHESTRATOR LOG", expanded=False):
        st.code(r"""
[2026-03-05 08:15:22] [heartbeat] INFO: Running check-limits... Claude: 82%, Gemini: 91%
[2026-03-05 08:20:45] [usage-suggest] INFO: Low queue + high capacity. Suggesting tasks...
[2026-03-05 08:21:10] [telegram] INFO: User picked 'Skill: vault-gardener'
[2026-03-05 08:21:12] [orchestrator] INFO: Starting task: 'Bereinige Vault-Tags und verwaiste Links'
[2026-03-05 08:21:15] [cwd] D:\obsidian\vault
[2026-03-05 08:21:45] [provider] Claude: Task completed successfully (33s)
[2026-03-05 08:21:46] [notifier] INFO: Telegram notification sent.
        """, language="bash")

    st.divider()

    # -- New Section: Control & Interface --
    col_ctrl, col_chat = st.columns([3, 2])

    with col_ctrl:
        st.write("📝 **Queue Syntax & Task Control**")
        st.markdown("""
        Aufgaben werden in einer einfachen Markdown-Datei im Obsidian Vault gepflegt. 
        Durch Tags lässt sich das Verhalten der Engine präzise steuern.
        """)
        
        st.code(r"""
# Beispiel agent-queue.md
- [ ] Refactor signal processing module cwd:D:\proj #claude_sonnet #timeout:10m
- [ ] Review performance issues #tool:review-loop #agent:engineering
- [ ] Sync database #parallel #approve:push
  - check integrity
  - backup tables
- [ ] Run cleanup #shutdown
        """, language="markdown")

        with st.expander("⚙️ VERFÜGBARE EINSTELLUNGEN"):
            st.markdown("""
            | Tag | Funktion | Beispiel |
            | :--- | :--- | :--- |
            | `cwd:` | Setzt das Arbeitsverzeichnis | `cwd:D:\projects\app` |
            | `#tool:` | Startet eine iterative Skill-Schleife | `#tool:test-loop` |
            | `#agent:` | Nutzt ein spezifisches Ausführungsprofil | `#agent:work` |
            | `#timeout:` | Limitiert die Laufzeit (s/m/h) | `#timeout:15m` |
            | `#parallel` | Führt Unteraufgaben parallel aus | `#parallel` |
            | `#shutdown` | Fährt PC nach Abschluss herunter | `#shutdown` |
            | `#approve:` | Gibt riskante Aktionen vorab frei | `#approve:push` |
            | `#claude` | Erzwingt einen bestimmten Provider | `#gemini`, `#codex` |
            """)

    with col_chat:
        st.write("📱 **Telegram AI Interface (Simulation)**")
        
        # Simple Chat Simulation using a container
        chat_container = st.container(height=400, border=True)
        with chat_container:
            st.chat_message("user").write("/status")
            st.chat_message("assistant").write("📊 **Orchestrator Status:**\nQueue: 0 offene Tasks\nClaude: 82% (Reset in 12m)\nGemini: 95%\nEngine: ACTIVE")
            
            st.chat_message("user").write("/task Fixe Bug in analytics.py cwd:D:\proj #claude")
            st.chat_message("assistant").write("✅ Task zur Queue hinzugefügt.")
            
            st.divider()
            
            st.chat_message("assistant").write("💡 **Freie Kapazität verfügbar!**\nClaude: 82% übrig.\n\nVorschläge:\n1. Skill: vault-gardener\n2. Git: AI_orchestrator (3 Änderungen)\n3. Retry: Fix Unicode-Bug\n\n/pick 1-3 oder /decline")
            st.chat_message("user").write("/pick 1")
            st.chat_message("assistant").write("👍 Vorschlag 1 angenommen. Starte `vault-gardener`...")

    if st.button("TRIGGER TEST PIPELINE (MOCK)"):
        progress_bar = st.progress(0)
        status_text = st.empty()
        steps = [
            "Syncing Obsidian Vault Context...", 
            "Checking Provider Limits (npx cclimits)...",
            "Routing Task to Claude (Best available)...",
            "Executing Review-Loop Skill...",
            "Stashing Git changes for safety...",
            "Finalizing Queue entry and notifying Telegram..."
        ]
        for i, step in enumerate(steps):
            status_text.info(f"RUNNING: {step}")
            time.sleep(0.7)
            progress_bar.progress((i + 1) / len(steps))
        st.success("TEST RUN COMPLETED: Agent-Queue synchronized and tasks processed.")

# --- TAB: SMART GRID ---
with tab_eeg:
    st.subheader("☀️ Smart Grid Analytics: Energy Community & PV Forecast")
    st.markdown("""
    *Vom Daten-Chaos zur intelligenten Energiegemeinschaft: Management von 2.200+ Zählpunkten 
    und hochpräzise PV-Prognosen für eine ganze Region.*
    """)

    # -- Core Benefits & Problem Solving --
    with st.expander("💡 ENERGIEGEMEINSCHAFTEN: PROBLEME & LÖSUNGEN", expanded=True):
        col_e1, col_e2 = st.columns(2)
        with col_e1:
            st.markdown("### ❌ Die Herausforderung")
            st.error("""
            - **Komplexität:** Manuelle Abrechnung von hunderten Haushalten ist unmöglich.
            - **Volatilität:** PV-Erzeugung schwankt extrem durch Wetter (Nebelrisiko!).
            - **Netzlast:** Unkontrollierte Einspeisung belastet die lokalen Netze.
            - **Intransparenz:** Mitglieder wissen oft nicht, wann sie ihren Strom verbrauchen sollten.
            """)
        with col_e2:
            st.markdown("### ✅ Meine Lösung")
            st.success("""
            - **Automatisierte ETL:** 15-Minuten Intervalle werden via Excel-Stream direkt in SQL verarbeitet.
            - **Smart Forecasting:** XGBoost & Prophet sagen Erzeugung voraus – inkl. Nebel-Risiko-Features.
            - **Eigendeckungs-Analyse:** Automatische Berechnung von Eigenverbrauch & Gemeinschafts-Anteil.
            - **Dashboarding:** Visuelle Aufbereitung für Vorstände & Mitglieder (Eigendeckung, Netzbezug).
            """)

    # -- Key Metrics --
    col_m1, col_m2, col_m3, col_m4 = st.columns(4)
    col_m1.metric("Mitglieder (Zählpunkte)", "2.245", delta="+12 (MTD)")
    col_m2.metric("Eigendeckungs-Rate", "68.4%", delta="+2.1%")
    col_m3.metric("PV Forecast MAE", "4.2%", delta="-0.5%", delta_color="inverse")
    col_m4.metric("Datenpunkte (SQL)", "148M", delta="Weekly Sync")

    st.divider()

    # -- Visual Analysis: Load Profile vs. Generation --
    st.write("📊 **Energy Balance: 72h Forecast (incl. 24h Projection)**")
    
    # Generate realistic 15-min data for 72 hours (3 days)
    # Total periods: 72h * 4 periods/h = 288
    # Actual data: first 48h (192 periods)
    total_periods = 72 * 4
    actual_periods = 48 * 4
    times_eeg = pd.date_range(end=pd.Timestamp.now() + pd.Timedelta(hours=24), periods=total_periods, freq='15min')
    
    # Time helper for seasonality
    hour = (times_eeg.hour + times_eeg.minute / 60).to_numpy()
    
    # 1. ACTUAL CONSUMPTION (only first 48h, then NaN)
    base_cons = 40 + 15 * np.sin((hour - 6) * np.pi / 12)**2 + 10 * np.sin((hour - 18) * np.pi / 6)**2
    consumption = base_cons + np.random.normal(0, 4, total_periods)
    
    # 2. ACTUAL GENERATION (only first 48h, then NaN)
    generation = 120 * np.maximum(0, np.sin((hour - 6) * np.pi / 12)) + np.random.normal(0, 2, total_periods)
    # Apply "fog" effect to part of the second day
    generation[96:192] *= 0.35 
    
    # 3. FORECASTS (Full 72h)
    # PV Forecast with some bias and phase shift
    pv_forecast = 110 * np.maximum(0, np.sin((hour - 5.8) * np.pi / 12)) + np.random.normal(0, 5, total_periods)
    # Consumption Forecast with different noise and amplitude
    cons_forecast = base_cons * 1.1 + np.random.normal(0, 8, total_periods)

    # Create DataFrame and mask actual values after 48h
    df_energy = pd.DataFrame({
        'Time': times_eeg,
        'Consumption': consumption,
        'Generation': generation,
        'PV Forecast': pv_forecast,
        'Cons Forecast': cons_forecast
    })
    
    # Masking the "Actuals" for the last 24h
    df_energy.loc[actual_periods:, ['Consumption', 'Generation']] = np.nan

    fig_energy = go.Figure()
    
    # Forecasts (Dashed lines)
    fig_energy.add_trace(go.Scatter(x=df_energy['Time'], y=df_energy['Cons Forecast'], name='Forecast: Consumption', 
                                  line=dict(color='#8b949e', width=1, dash='dot')))
    fig_energy.add_trace(go.Scatter(x=df_energy['Time'], y=df_energy['PV Forecast'], name='Forecast: PV', 
                                  line=dict(color='#ffcc00', width=1, dash='dot')))
    
    # Actuals (Solid lines / Fills)
    fig_energy.add_trace(go.Scatter(x=df_energy['Time'], y=df_energy['Consumption'], name='Actual: Consumption', 
                                  line=dict(color='#c9d1d9', width=2)))
    fig_energy.add_trace(go.Scatter(x=df_energy['Time'], y=df_energy['Generation'], name='Actual: Generation', 
                                  fill='tozeroy', line=dict(color='#6caf2b', width=3)))
    
    # Indicator for now
    now_ts = times_eeg[actual_periods-1]
    fig_energy.add_vline(x=now_ts, line_width=2, line_dash="dash", line_color="#ff4b4b")
    fig_energy.add_annotation(x=now_ts, y=140, text="JETZT (Start Prognose)", showarrow=False, font_color="#ff4b4b")
    
    fig_energy.update_layout(template="plotly_dark", paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', 
                           font_family="JetBrains Mono", legend=dict(orientation="h", y=1.15),
                           yaxis_title="Leistung [kW]", height=500)
    st.plotly_chart(fig_energy, use_container_width=True)

    # -- Technical Deep Dive: Feature Engineering --
    col_f1, col_f2 = st.columns([2, 1])
    with col_f1:
        st.write("🧠 **ML Model: Hybrid XGBoost + Prophet Architecture**")
        st.markdown("""
        Um die Volatilität der PV-Erzeugung zu bändigen, nutzt das System über **140 Features**:
        - **Astronomisch:** Sonnenhöhenwinkel, Azimut, Clear-Sky-Index (via `pvlib`).
        - **Meteorologisch:** Einstrahlung, Bewölkung, Luftfeuchtigkeit (Open-Meteo API).
        - **Spezial-Features:** "Nebel-Risiko-Index" (Kombination aus Luftdruck & Feuchte).
        - **Zeitreihen:** Lags (15min, 1h, 24h), gleitende Durchschnitte.
        """)
        
    with col_f2:
        st.write("🛠️ **Tech Stack Details**")
        st.code("""
# Training Pipeline
python -m src.models.train
# DB WAL-Mode for Speed
PRAGMA journal_mode=WAL;
# Feature Engineering
astronomical_features = 
    get_sun_position(lat, lon)
        """, language="python")

    if st.button("RUN ETL PIPELINE (SIMULATION)"):
        with st.status("Processing Raw Energy Data..."):
            st.write("Initializing SQLite Connection (WAL-Mode)...")
            time.sleep(1.0)
            st.write("Streaming 2.200+ Metering Points (15-min resolution)...")
            st.progress(0.4)
            time.sleep(1.2)
            st.write("Calculating Self-Sufficiency (Eigendeckung) for all members...")
            st.progress(0.8)
            time.sleep(0.8)
            st.write("Updating ML Forecast with newest weather data...")
            st.progress(1.0)
        st.success("SUCCESS: Database updated. Analysis results available in Dashboard.")

# --- TAB: SIGNAL PROCESSING ---
with tab_signal:
    st.subheader("⚙️ NVH Signal Processing: Zeitrohdaten to Insights")
    st.markdown("""
    *Vom Rauschen zur Resonanz: Automatisierte Aufbereitung von Zeitrohdaten für die Schwingungsanalyse.
    Dieses Modul transformiert komplexe Sensor-Signale in klare Entscheidungsgrundlagen.*
    """)

    # -- Core Benefits & Problem Solving --
    with st.expander("💡 SCHWINGUNGSANALYSE: PROBLEME & LÖSUNGEN", expanded=True):
        col_sig1, col_sig2 = st.columns(2)
        with col_sig1:
            st.markdown("### ❌ Die Herausforderung")
            st.error("""
            - **Daten-Volumen:** Terabytes an Zeitrohdaten (CSV/Binary) sind manuell nicht auswertbar.
            - **Synchronität:** Verknüpfung von RPM-Gebern mit Beschleunigungs-Sensoren ist fehleranfällig.
            - **Rauschen:** Ohne Hanning-Fensterung & präzise FFT gehen relevante Peaks im Rauschen unter.
            - **Simulation-Gap:** Messergebnisse müssen mühsam für FEM-Tools (Hypermesh) aufbereitet werden.
            """)
        with col_sig2:
            st.markdown("### ✅ Meine Lösung")
            st.success("""
            - **Batch-Processing:** Vollautomatischer Import & Filterung ganzer Messkampagnen.
            - **Campbell-Automatisierung:** Zeit-zu-Frequenz Transformation inkl. Phasen-Referenzierung.
            - **Order-Extraction:** Automatisches Tracking von Motorordnungen zur Resonanz-Identifikation.
            - **FEM-Export:** Direkte Generierung von `.fem` RLOAD-Dateien für den Abgleich mit Simulationen.
            """)

    # -- Technical Specs Metrics --
    col_t1, col_t2, col_t3, col_t4 = st.columns(4)
    col_t1.metric("Sampling Rate", "8.192 Hz", help="Standard-Abtastrate für NVH-Messungen")
    col_t2.metric("Frequency Res.", "2.0 Hz", help="Blockzeit: 0.5s | Hanning-Window")
    col_t3.metric("RPM Steps", "25 RPM", help="Abtastung über den Drehzahlhochlauf")
    col_t4.metric("Engine Orders", "1.0 - 5.0", help="Extraktion in 0.5er Schritten")

    st.divider()

    # -- Visual Analytics: Campbell Diagram --
    st.write("📊 **Interactive Campbell Diagram (Frequency vs. RPM)**")

    # Generate realistic-looking Campbell data
    rpm_range = np.arange(500, 5001, 25)
    freq_range = np.arange(0, 1001, 2)

    # Create a base noise floor
    z_campbell = np.random.normal(0.01, 0.005, (len(freq_range), len(rpm_range)))

    # Add Engine Orders (Straight lines through origin)
    # Order line: freq = (RPM / 60) * Order
    orders = [1, 2, 3, 4, 6]
    for order in orders:
        for j, rpm in enumerate(rpm_range):
            target_freq = (rpm / 60.0) * order
            idx = np.argmin(np.abs(freq_range - target_freq))
            if idx < len(freq_range):
                # Amplitude increases with RPM (simple resonance simulation)
                resonance_factor = 1.0 + 2.0 * np.exp(-((rpm - 3200)**2) / (2 * 400**2))
                z_campbell[idx, j] += 0.5 * resonance_factor + np.random.normal(0, 0.05)

    # Add a structural resonance (Horizontal line)
    resonance_freq = 240 # Hz
    idx_res = np.argmin(np.abs(freq_range - resonance_freq))
    z_campbell[idx_res, :] += 0.2 * np.exp(-((rpm_range - 3200)**2) / (2 * 1000**2))

    fig_camp = go.Figure(data=go.Heatmap(
        z=z_campbell,
        x=rpm_range,
        y=freq_range,
        colorscale='Viridis',
        colorbar=dict(title="Amplitude [g]"),
        hovertemplate='RPM: %{x}<br>Freq: %{y} Hz<br>Amp: %{z:.3f} g<extra></extra>'
    ))

    # Add Order Lines as annotation
    for order in [1, 2, 3]:
        fig_camp.add_trace(go.Scatter(
            x=[500, 5000],
            y=[(500/60)*order, (5000/60)*order],
            mode='lines',
            line=dict(color='rgba(255,255,255,0.3)', width=1, dash='dash'),
            name=f"Order {order}",
            showlegend=False
        ))

    fig_camp.update_layout(
        template="plotly_dark",
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font_family="JetBrains Mono",
        xaxis_title="DREHZAHL [RPM]",
        yaxis_title="FREQUENZ [Hz]",
        height=600
    )
    st.plotly_chart(fig_camp, use_container_width=True)

    # -- Motor Order Cut --
    st.write("📈 **Motor Order Cuts (Structural Health Analysis)**")

    col_cut1, col_cut2 = st.columns([2, 1])

    with col_cut1:
        # Generate order cut data for 2.0 Order
        order_2 = 0.4 * (rpm_range/1000)**1.5 + 0.8 * np.exp(-((rpm_range - 3250)**2) / (2 * 250**2))
        order_4 = 0.2 * (rpm_range/1000)**1.2 + 0.3 * np.exp(-((rpm_range - 4100)**2) / (2 * 300**2))

        fig_order = go.Figure()
        fig_order.add_trace(go.Scatter(x=rpm_range, y=order_2, name="Order 2.0 (Resonance @3250)", line=dict(color='#6caf2b', width=3)))
        fig_order.add_trace(go.Scatter(x=rpm_range, y=order_4, name="Order 4.0", line=dict(color='#8b949e', width=2, dash='dot')))

        fig_order.update_layout(
            template="plotly_dark",
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font_family="JetBrains Mono",
            xaxis_title="RPM",
            yaxis_title="Amplitude [g]",
            legend=dict(orientation="h", y=1.1),
            height=400
        )
        st.plotly_chart(fig_order, use_container_width=True)

    with col_cut2:
        st.info("**ANALYSE:** Die 2. Motorordnung zeigt eine ausgeprägte Resonanz bei ca. 3.250 RPM. Dies deutet auf eine Kopplung mit der ersten Biegeeigenform des Kranauslegers hin.")
        st.write("🛠️ **Export Options:**")
        st.download_button("DOWNLOAD CSV (ORDER DATA)", "RPM;Order2.0;Order4.0\n500;0.1;0.05...", file_name="orders.csv")
        st.button("GENERATE .FEM (RLOAD)", help="Erstellt eine Hypermesh-kompatible Datei")

    if st.button("RUN SIGNAL PIPELINE (MOCK)"):
        with st.status("Aufbereitung der Zeitrohdaten läuft..."):
            st.write("Lade Zeitreihen (8.192 Hz)...")
            time.sleep(0.8)
            st.write("Hanning-Fensterung & FFT-Berechnung...")
            st.progress(0.4)
            time.sleep(1.0)
            st.write("Phasen-Referenzierung zu Sensor '00-REF'...")
            st.progress(0.7)
            time.sleep(0.6)
            st.write("Mittelung über 4 Messreihen abgeschlossen.")
            st.progress(1.0)
        st.success("CAMPBELL-MATRIX erfolgreich generiert.")

# --- TAB: EN13001 TOOLS ---
with tab_en13001:
    st.subheader("🏗️ EN13001 Tool-Suite: Structural Crane Component Design")
    st.markdown("""
    *Präzision trifft Normkonformität: Eine umfassende Berechnungs-Suite für die Auslegung von Krankomponenten nach DIN EN 13001. 
    Digitalisierung komplexer Nachweise für höchste Sicherheit und Effizienz.*
    """)

    # -- Core Benefits & Problem Solving --
    with st.expander("💡 KRANBAU-STATIK: PROBLEME & LÖSUNGEN", expanded=True):
        col_en1, col_en2 = st.columns(2)
        with col_en1:
            st.markdown("### ❌ Die Herausforderung")
            st.error("""
            - **Norm-Komplexität:** Die DIN EN 13001 umfasst tausende Seiten mit komplexen Faktoren (z.B. $\\alpha_w$).
            - **Fehleranfälligkeit:** Manuelle Rechnungen in Excel oder Matcad sind schwer zu validieren.
            - **Dokumentations-Aufwand:** Die Erstellung prüffähiger PDF-Berichte dauert oft länger als die Rechnung selbst.
            - **Legacy-Tools:** Veraltete Software bietet keine modernen Schnittstellen zu FEM oder AI.
            """)
        with col_en2:
            st.markdown("### ✅ Meine Lösung")
            st.success("""
            - **Umfassende Suite:** Spezialisierte Module für Schrauben, Schweißnähte, Bolzen und Stabilität.
            - **Automatisierte Berichte:** Generierung detaillierter, normgerechter PDF-Nachweise auf Knopfdruck.
            - **Hot-Spot Methode:** Integration moderner Ermüdungsanalysen direkt aus FEM-Knotenspannungen.
            - **Validierte Logik:** V2.0 mit vollständig korrigierten Faktoren (Table 8) und Anhang C Referenzen.
            """)

    # -- Performance Metrics --
    col_em1, col_em2, col_em3, col_em4 = st.columns(4)
    col_em1.metric("Berechnungs-Module", "7+", delta="Hot-Spot added")
    col_em2.metric("Zeitersparnis (Doku)", "70%", delta="+15%")
    col_em3.metric("Norm-Konformität", "EN 13001-3-x", delta="2019-03")
    col_em4.metric("Validierte Nachweise", "100%", delta="V2.0 Core")

    st.divider()

    # -- Multi-Module Overview --
    st.write("🛠️ **Multi-Module Architecture: Specialized Engineering Tools**")
    
    col_mod1, col_mod2, col_mod3 = st.columns(3)
    
    with col_mod1:
        with st.container(border=True):
            st.markdown("#### 🔩 **Schrauben & Bolzen**")
            st.write("- Statische Festigkeit nach §5.")
            st.write("- Vorspannkraft & Montagesicherheit.")
            st.write("- Flächenpressung (Hertzsche Pressung).")
            st.caption("Modules: `bolt_design`, `pin_design`")

    with col_mod2:
        with st.container(border=True):
            st.markdown("#### ⚡ **Schweißnähte & Ermüdung**")
            st.write("- V2.0: Vollständige $\\alpha_w$-Logik.")
            st.write("- Ermüdung nach Palmgren-Miner.")
            st.write("- Anhang C.1 - C.3 Nachweise.")
            st.caption("Modules: `weld_design`, `fatigue_design`")

    with col_mod3:
        with st.container(border=True):
            st.markdown("#### 📐 **Stabilität & Hot-Spot**")
            st.write("- Knicken & Beulen nach §8.")
            st.write("- IIW Hot-Spot Spannungsextrapolation.")
            st.write("- FEM-Knoten-Interpolation.")
            st.caption("Modules: `elastic_stability`, `hotspot_fatigue`")

    st.divider()

    # -- Live Calculation Simulation (Weld Module) --
    st.write("🎮 **Interactive Simulation: Weld Connection (V2.0)**")
    
    col_calc1, col_calc2 = st.columns([1, 2])
    
    with col_calc1:
        st.write("**Eingabeparameter:**")
        weld_type = st.selectbox("Nahttyp", ["Stumpfnaht", "Kehlnaht (T-Stoß)", "Punktbelastung"])
        material = st.selectbox("Grundmaterial", ["S235", "S355", "S460", "S690"])
        weld_quality = st.radio("Schweißnahtgüte", ["Gruppe C (High)", "Gruppe D (Standard)"])
        stress_sigma = st.slider("Normalspannung $\\sigma_{w}$ [MPa]", 0, 400, 120)
        stress_tau = st.slider("Schubspannung $\\tau_{w}$ [MPa]", 0, 250, 45)
        
    with col_calc2:
        st.write("**Echtzeit-Validierung (Norm-Logik):**")
        
        # Simple Calculation Logic Mockup based on EN13001-3-1
        f_yd = 355 if material == "S355" else 235
        # alpha_w calculation mock (Table 8 simplification)
        alpha_w = 0.9 if weld_quality == "Gruppe C (High)" else 0.6
        
        # Combined stress (Eq. 29)
        sigma_v = np.sqrt(stress_sigma**2 + 3 * stress_tau**2)
        utilization = (sigma_v / (f_yd * alpha_w)) * 100
        
        # Visualizing Utilization
        fig_gauge = go.Figure(go.Indicator(
            mode = "gauge+number",
            value = utilization,
            domain = {'x': [0, 1], 'y': [0, 1]},
            title = {'text': "Ausnutzungsgrad [%]", 'font': {'size': 24}},
            gauge = {
                'axis': {'range': [None, 120], 'tickwidth': 1, 'tickcolor': "#c9d1d9"},
                'bar': {'color': "#6caf2b" if utilization < 100 else "#ff4b4b"},
                'bgcolor': "rgba(0,0,0,0)",
                'borderwidth': 2,
                'bordercolor': "#30363d",
                'steps': [
                    {'range': [0, 80], 'color': 'rgba(108, 175, 43, 0.1)'},
                    {'range': [80, 100], 'color': 'rgba(255, 204, 0, 0.2)'},
                    {'range': [100, 120], 'color': 'rgba(255, 75, 75, 0.3)'}
                ],
                'threshold': {
                    'line': {'color': "red", 'width': 4},
                    'thickness': 0.75,
                    'value': 100
                }
            }
        ))
        fig_gauge.update_layout(template="plotly_dark", paper_bgcolor='rgba(0,0,0,0)', font_family="JetBrains Mono", height=350)
        st.plotly_chart(fig_gauge, use_container_width=True)
        
        if utilization > 100:
            st.error(f"⚠️ **NACHWEIS NICHT ERFÜLLT!** Kombinierte Spannung ({sigma_v:.1f} MPa) überschreitet Grenzspannung ({f_yd*alpha_w:.1f} MPa).")
        else:
            st.success(f"✅ **NACHWEIS ERFÜLLT.** Ausnutzung: {utilization:.1f}%. Sicherheitsfaktor: {(100/utilization):.2f}")

    # -- Technical Deep Dive: Hot-Spot Method --
    st.write("🔬 **Technical Focus: Hot-Spot Fatigue Analysis (IIW)**")
    col_hs1, col_hs2 = st.columns([3, 2])
    
    with col_hs1:
        st.markdown("""
        Bei komplexen Schweißknoten versagt die klassische Nennspannungskonzept. Das Hot-Spot Modul automatisiert die:
        1. **Knoten-Extraktion:** Einlesen von FEM-Spannungen an Referenzpunkten (0.4t / 1.0t).
        2. **Extrapolation:** Lineare oder quadratische Extrapolation zur Schweißnahtzehe.
        3. **Lebensdauer:** Schadensakkumulation nach Palmgren-Miner basierend auf FAT-Klassen.
        """)
        
        # Mock-up plot for Extrapolation
        x_hs = np.array([0.4, 0.7, 1.0])
        y_hs = np.array([210, 185, 160]) # Stress values
        # Extrapolate to 0.0
        p = np.polyfit(x_hs, y_hs, 1)
        x_ext = np.linspace(0, 1.2, 50)
        y_ext = np.polyval(p, x_ext)
        
        fig_hs = px.line(x=x_ext, y=y_ext, labels={'x': 'Distanz / Blechdicke [t]', 'y': 'Spannung [MPa]'}, title="Hot-Spot Extrapolation (Type A)")
        fig_hs.add_scatter(x=x_hs, y=y_hs, mode='markers', name='FEM Knoten', marker=dict(size=10, color='#6caf2b'))
        fig_hs.add_scatter(x=[0], y=[np.polyval(p, 0)], mode='markers', name='Hot-Spot Stress', marker=dict(size=12, color='#ff4b4b', symbol='star'))
        fig_hs.update_layout(template="plotly_dark", paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_family="JetBrains Mono", height=300)
        st.plotly_chart(fig_hs, use_container_width=True)

    with col_hs2:
        st.write("🛠️ **Export & Reporting**")
        st.code("""
# Example: JSON Export for Fatigue
{
  "module": "hotspot_fatigue",
  "fat_class": 90,
  "sigma_hotspot": 224.5,
  "utilization": 0.84,
  "status": "PASSED"
}
        """, language="json")
        st.button("DOWNLOAD SAMPLE PDF REPORT", help="Generiert einen Beispieldokumentation")

    if st.button("RUN VALIDATION SUITE (MOCK)"):
        with st.status("Validierung aller EN13001 Nachweise..."):
            st.write("Lade Materialdatenbank (Stahl/Guss)...")
            time.sleep(0.6)
            st.write("Prüfe geometrische Grenzbedingungen (§5.3)...")
            st.progress(0.3)
            time.sleep(0.8)
            st.write("Iterative Stabilitätsberechnung (Knicklängen)...")
            st.progress(0.7)
            time.sleep(1.0)
            st.write("Finalisierung der PDF-Berichtsstruktur...")
            st.progress(1.0)
        st.success("VALIDATION COMPLETE: 124 Checks passed. No critical errors found.")

# --- TAB: SALES AI ---
with tab_sales:
    st.subheader("📊 Sales Pipeline Automation: AI-Powered Lead Intelligence")
    st.markdown("""
    *Vom digitalen Grundrauschen zum qualifizierten Engineering-Lead: Ein autonomes System, das Leads identifiziert, 
    technisch bewertet und Akquise-Strategien vorbereitet.*
    """)

    # -- Core Benefits & Problem Solving --
    with st.expander("💡 SALES AUTOMATION: PROBLEME & LÖSUNGEN", expanded=True):
        col_sa1, col_sa2 = st.columns(2)
        with col_sa1:
            st.markdown("### ❌ Die Herausforderung")
            st.error("""
            - **Informationsflut:** Tausende Job-Postings & Emails manuell nach "EN 13001" oder "NVH" zu filtern ist ineffizient.
            - **Generic Scoring:** Standard-Keywords (z.B. "Statik") liefern zu viele False Positives.
            - **Blind-Research:** Vor jedem Telefonat manuell die Website & Ansprechpartner zu suchen kostet Stunden.
            - **CRM-Pflege:** Kontakte & Interaktionen manuell zu loggen wird oft vernachlässigt.
            """)
        with col_sa2:
            st.markdown("### ✅ Meine Lösung")
            st.success("""
            - **Multi-Stage Scoring:** Kombination aus Regex-Pattern (EN-Normen) und semantischer LLM-Analyse.
            - **URL Enrichment:** Automatisches Fetching & Parsing von Job-Details nur für vielversprechende Leads.
            - **AI Analyst:** Autonome Recherche von Firmen-Websites (Impressum, News, Standorte) via LLM-Tools.
            - **Chat-Centric CRM:** Ein KI-Assistent mit DB-Zugriff ermöglicht Lead-Management per Sprache/Chat.
            """)

    # -- Performance Metrics --
    col_p1, col_p2, col_p3, col_p4 = st.columns(4)
    col_p1.metric("Leads Collected", "1.482", delta="+112 (KW09)")
    col_p2.metric("Prequalified (High-Score)", "156", delta="10.5%")
    col_p3.metric("Research Accuracy", "92%", delta="+4%")
    col_p4.metric("Draft Conversion", "18%", delta="+2.5%")

    st.divider()

    # -- Visualizing the Two-Stage Pipeline --
    st.write("🔄 **Two-Stage Intelligence Pipeline**")
    st.image("https://mermaid.ink/svg/pako:eNptkE1LxEAQhv_KMGcv_QPePCh4U_Ag6MWLh8W0O7Wp6SSTTbeI-N-dtatV8Obh9XnfZ0Y75S6N0mI9fK-K8hZ8m0u9n29E0b7TfO500vK4V4eT0Yre-9Bq432-8kXpQ_FkRre8N8bYI78XvTf-zK8f9Wf-eAof6Vv-eA4f6W_58zl8pA_k98I_5I_X8JF-Iu8X_jE_vYWP9At5v_D3-eM9fKS_vL--P89yK_OllVpU7i-N0vA0", caption="Logic: Fast Filter -> Deep Enrichment -> Final Score", use_container_width=False)

    # -- Lead Detail Example Card --
    st.write("📝 **Example: AI-Enriched Lead Detail**")
    with st.container(border=True):
        col_l1, col_l2 = st.columns([2, 1])
        with col_l1:
            st.markdown("### **Senior Berechnungsingenieur (m/w/d) - Kranbau**")
            st.caption("📍 Industrial Region A | 🏢 SteelWorks Heavy Industries GmbH | 📅 2026-03-04")
            st.write("**Gefundene Keywords:** `EN 13001` (+15), `Kran` (+10), `Ansys` (+5), `FEM` (+5)")
            st.success("**AI Summary:** Fokus auf Strukturmechanik und Normprüfung nach EN 13001. Erfordert Expertise in der Auslegung von Schweißkonstruktionen.")
            
            with st.expander("🔍 AUTOMATED COMPANY RESEARCH RESULTS"):
                st.markdown("""
                - **Branche:** Baumaschinen / Mobilkrane
                - **Ansprechpartner:** Dr. Michael Schmidt (Technischer Leiter - LinkedIn match)
                - **Aktuelle Projekte:** Erweiterung der HeavyLift-Serie, Fokus auf Leichtbau.
                - **Technologien:** Ansys Mechanical, PTC Creo.
                """)
        
        with col_l2:
            st.metric("Lead Score", "85 / 100", delta="HOT LEAD")
            st.button("CREATE GMAIL DRAFT", use_container_width=True)
            st.button("MARK AS 'INTERESSANT'", type="primary", use_container_width=True)

    st.divider()

    # -- Sales Analytics Charts --
    col_g1, col_g2 = st.columns(2)
    
    with col_g1:
        st.write("📈 **Lead Performance by Source**")
        source_data = pd.DataFrame({
            'Source': ['JobPortal-A', 'LinkedIn', 'RSS Feeds', 'Email Alerts'],
            'Volume': [450, 320, 580, 132],
            'High-Quality %': [12, 18, 5, 22]
        })
        fig_source = px.bar(source_data, x='Source', y='Volume', color='High-Quality %',
                          color_continuous_scale='Viridis', title="Volume vs. Quality Density")
        fig_source.update_layout(template="plotly_dark", paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_family="JetBrains Mono")
        st.plotly_chart(fig_source, use_container_width=True)

    with col_g2:
        st.write("📊 **Pipeline Conversion (Funnel)**")
        funnel_data = dict(
            number=[1482, 650, 156, 42, 12],
            stage=["Collected", "Scored > 20", "Enriched (High Score)", "Drafts Created", "Meetings"]
        )
        fig_funnel = px.funnel(funnel_data, x='number', y='stage', color_discrete_sequence=['#6caf2b'])
        fig_funnel.update_layout(template="plotly_dark", paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_family="JetBrains Mono")
        st.plotly_chart(fig_funnel, use_container_width=True)

    # -- Chat Interface for CRM (Simulation) --
    st.write("🤖 **AI Sales Assistant (Chat-to-CRM)**")
    chat_sales = st.container(height=350, border=True)
    with chat_sales:
        st.chat_message("user").write("Zeige mir die 3 besten Leads aus dieser Woche mit Fokus auf 'Kranbau'.")
        st.chat_message("assistant").write("""
        Gefunden: 3 High-Score Leads (> 75)
        1. **SteelWorks** (City Alpha) - Score: 85 (EN 13001 Fokus)
        2. **HydraLift Systems** (City Beta) - Score: 82 (Hydraulik & Statik)
        3. **SkyLine Crane Ops** (City Gamma) - Score: 78 (Instandhaltung & NVH)
        
        Soll ich für SteelWorks eine Firmen-Recherche starten?
        """)
        st.chat_message("user").write("Ja, bitte recherche starten und danach einen Gmail Entwurf vorbereiten.")
        st.chat_message("assistant").write("🚀 Recherche läuft... (Web-Mining aktiviert). Entwurf wird in 30s erstellt.")

    if st.button("RUN SALES PIPELINE (KW09)"):
        with st.status("Pipeline-Vorgang gestartet..."):
            st.write("Polling RSS Feeds & Gmail Alerts...")
            time.sleep(0.8)
            st.write("Initial Scoring (Regex Engine)...")
            st.progress(0.3)
            time.sleep(1.0)
            st.write("URL Enrichment: Deep-Parsing 15 promising leads...")
            st.progress(0.7)
            time.sleep(1.5)
            st.write("Deduplication & CRM Sync...")
            st.progress(1.0)
        st.success("SUCCESS: 8 neue High-Score Leads identifiziert und in CRM importiert.")

# --- TAB: SOCIAL MEDIA AI ---
with tab_social:
    st.subheader("🛋️ Premium Interior: Social Media & SEO Automation")
    st.markdown("""
    *Vom Produktfoto zum viralen Content: Ein spezialisiertes KI-System für den gehobenen Einrichtungs-Einzelhandel. 
    Automatisierte Bild-Analyse, cross-plattform Texterstellung und regionale SEO-Optimierung.*
    """)

    # -- Core Benefits & Problem Solving --
    with st.expander("💡 CREATIVE AUTOMATION: PROBLEME & LÖSUNGEN", expanded=True):
        col_sm1, col_sm2 = st.columns(2)
        with col_sm1:
            st.markdown("### ❌ Die Herausforderung")
            st.error("""
            - **Zeitaufwand:** Täglicher Content für 5+ Plattformen (Insta, TikTok, Pinterest, FB, YT) ist im Tagesgeschäft kaum machbar.
            - **Konsistenz:** Den richtigen "Vibe" (exklusiv, wohnlich, modern) über alle Kanäle hinweg zu halten ist schwierig.
            - **Fachwissen:** KI-Modelle kennen oft keine feinen Unterschiede bei Design-Stilen (Skandinavisch vs. Mid-Century).
            - **Regionale Sichtbarkeit:** SEO für lokale Showrooms erfordert spezifische Keyword-Strategien.
            """)
        with col_sm2:
            st.markdown("### ✅ Meine Lösung")
            st.success("""
            - **AI Design Consultant:** Ein spezialisierter Skill, der Bilder wie ein Experte analysiert (Materialien, Lichtführung, Stilelemente).
            - **Cross-Platform Engine:** Ein Workflow generiert aus einem Bild passende Texte, Hashtags & Voiceover-Scripts für alle Kanäle.
            - **SEO Copy Optimizer:** WordPress-Integration für Produktseiten mit Fokus auf Showroom-Termine (Conversion) statt reiner Katalog-Ansicht.
            - **Canva & ElevenLabs Sync:** Direkte Vorbereitung von Design-Prompts und Audio-Scripts für die schnelle Produktion.
            """)

    # -- Key Metrics --
    col_k1, col_k2, col_k3, col_k4 = st.columns(4)
    col_k1.metric("Content Creation Time", "-95%", delta="Fast Pipeline")
    col_k2.metric("Platforms Covered", "5", delta="Instagram to YT")
    col_k3.metric("SEO Reach (Region)", "+42%", delta="Regional Focus")
    col_k4.metric("Conversion (Termine)", "High", delta="CTA focus")

    st.divider()

    # -- Interactive Demo: The Content Engine --
    st.write("🎬 **Interactive Demo: Multi-Platform Content Engine**")
    
    col_demo1, col_demo2, col_demo3 = st.columns([1, 1, 2])
    
    with col_demo1:
        st.write("**1. Input: Analyse**")
        st.info("Simulation: Upload eines Designer-Sessels (Samt, Walnuss, Mid-Century)")
        
        with st.container(border=True):
            st.markdown("#### **KI-Experten-Analyse:**")
            st.write("**Stil:** Mid-Century Modern")
            st.write("**Material:** Samt & Walnuss")
            st.write("**Vibe:** Zeitlose Eleganz")
            st.caption("Analysiert von: `interior-design-social-media` Skill")

    with col_demo2:
        st.write("**2. Visual Branding**")
        st.info("Automatisierte Bildaufbereitung & Branding")
        
        with st.container(border=True):
            st.markdown("#### **Processing Engine:**")
            st.success("✅ Logo-Placement (Top Right)")
            st.success("✅ Brand Overlay (Exklusive Serifen-Schrift)")
            st.success("✅ Color Grading (Warm/Luxury Vibe)")
            st.success("✅ Aspect Ratio (9:16 für Reels/TikTok)")
            st.caption("Engine: `Python Image Processor` (OpenCV/PIL)")

    with col_demo3:
        st.write("**3. Output: Multi-Platform Content**")
        
        tab_ig, tab_tk, tab_pin, tab_seo = st.tabs(["INSTAGRAM REEL", "TIKTOK", "PINTEREST", "SEO PRODUCT PAGE"])
        
        with tab_ig:
            st.markdown("#### **Instagram Reel Content**")
            st.code("""
POST-TEXT:
Bereit für ein Upgrade in deinem Wohnzimmer? ✨ Unser neuer Samt-Sessel vereint 
höchsten Komfort mit zeitlosem Design. Die perfekte Kombination aus Walnuss 
und edlen Stoffen für dein Zuhause.

HASHTAGS:
#InteriorDesign #LuxuryLiving #HomeDecor2025 #InteriorInspo #ShowroomStyle

TEXT-OVERLAYS:
1. Dein neues Highlight?
2. Edler Samt-Komfort
3. Echtes Walnussholz
4. Jetzt Termin buchen!

VOICEOVER-SCRIPT (22s):
"Suchst du nach dem gewissen Etwas für dein Zuhause? Entdecke diesen luxuriösen 
Designer-Sessel... (70 Wörter optimiert für ElevenLabs)"
            """, language="markdown")

        with tab_tk:
            st.markdown("#### **TikTok (Authentic & Fast)**")
            st.code("""
POST-TEXT:
POV: Du hast das perfekte Statement-Piece für dein Wohnzimmer gefunden 🛋️✨ 
Welche Farbe würdest du wählen? #InteriorCheck #HomeGoals

HASHTAGS:
#DesignFurniture #InteriorTok #ModernHome2025 #LivingRoomVibes
            """, language="markdown")

        with tab_pin:
            st.markdown("#### **Pinterest (SEO Optimized)**")
            st.code("""
TITEL:
Luxuriöser Samt-Sessel Mid-Century Stil - Premium Interior Design

BESCHREIBUNG:
Entdecke diesen exklusiven Designer-Sessel in unserem Showroom. 
Perfekt für Ästheten, die hochwertige Materialien wie Walnuss und Samt 
schätzen. Jetzt Beratungstermin im lokalen Showroom vereinbaren.
            """, language="markdown")

        with tab_seo:
            st.markdown("#### **WordPress SEO Block (Stackable)**")
            st.code("""
<!-- WP:stackable/text-block -->
<h2 class="wp-block-stackable-text__title">
    Exklusives Design für dein Zuhause in deiner Region
</h2>
<p class="wp-block-stackable-text__text">
    Dieses handgefertigte Möbelstück besticht durch seine einzigartige Kombination aus... 
    [SEO-optimierter Text mit Fokus auf regionale Keywords]
</p>
<!-- /WP:stackable/text-block -->
            """, language="html")

    st.divider()

    # -- Technical Architecture --
    st.write("🏗️ **Technical Architecture: The 'Skill-System'**")
    col_arch1, col_arch2 = st.columns([3, 2])
    
    with col_arch1:
        st.markdown("""
        Das System basiert auf einem **Agentic Workflow** innerhalb eines Obsidian Vaults:
        1. **Vision-Layer:** GPT-4o / Claude 3.5 Vision analysieren Produktbilder.
        2. **Context-Layer:** Einbindung der `Brand-DNA` (Tonalität, Slogan, regionale Präsenz).
        3. **Generation-Layer:** Spezialisierte Prompts für jede Plattform (Pinterest SEO vs. TikTok Slang).
        4. **Automation-Layer:** Export von strukturierten Markdown-Files für den Orchestrator.
        """)
        
    with col_arch2:
        st.write("**Workflow Trigger:**")
        st.code("""
# Skill Execution Trigger
run_skill(
  name="interior-design-social-media",
  input=["image1.jpg", "info.docx"],
  output_format="multi_platform_bundle"
)
        """, language="python")

    if st.button("GENERATE CONTENT BUNDLE (MOCK)"):
        with st.status("KI-Experte analysiert Bilder..."):
            st.write("Extrahiere visuelle Merkmale (Materialien, Stil, Farben)...")
            time.sleep(1.2)
            st.write("Wende Brand-DNA an (Tonalität: exklusiv/wohnlich)...")
            st.progress(0.4)
            time.sleep(1.0)
            st.write("Generiere Texte für 5 Plattformen & SEO-Tags...")
            st.progress(0.7)
            time.sleep(1.5)
            st.write("Erstelle Voiceover-Script & Canva Prompts...")
            st.progress(1.0)
        st.success("SUCCESS: Content-Bundle erstellt. Bereit für Export nach Instagram & WordPress.")

# --- FOOTER & CONTACT ---
st.divider()
st.sidebar.markdown("### 🌐 NETWORK")
st.sidebar.markdown("🔗 **[LinkedIn Profile](https://www.linkedin.com/in/dominik-f-840ab919a/)**")
st.sidebar.markdown("---")
st.sidebar.caption("© 2026 Engineering Intelligence Showcase Dashboard")
