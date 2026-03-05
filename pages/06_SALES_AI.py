import streamlit as st
import pandas as pd
import plotly.express as px
import time

from ui_shared import init_page, render_demo_notice, render_header, render_sidebar

init_page()
render_header()
render_sidebar()

st.subheader("📊 Sales Pipeline Automation: AI-Powered Lead Intelligence")
render_demo_notice()
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
