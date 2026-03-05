import streamlit as st

from ui_shared import init_page, render_demo_notice, render_header, render_sidebar

init_page()
render_header()
render_sidebar()

render_demo_notice()
st.markdown("""
### 🎯 Für wen dieses Showcase gebaut ist (Kern-ICP)
Ich positioniere mich als Projektpartner für **Python- und KI-Automatisierung** in technischen Umfeldern.
Fokus ist nicht "Code um des Codes willen", sondern messbare Entlastung in echten Betriebsprozessen.
Schwerpunkte: **Automatisierung in Entwicklungs-/Engineering-Teams**, **Datenanalyse & Zeitreihen-Forecasting** sowie technische Simulationsthemen.
""")

icp_col1, icp_col2, icp_col3 = st.columns(3)
with icp_col1:
    with st.container(border=True):
        st.markdown("#### 1) Automatisierung für Entwicklungs-Teams")
        st.write("Typische Probleme: wiederholte Routineaufgaben, Medienbrüche zwischen Tools, hoher manueller Abstimmungsaufwand.")
        st.caption("Zielnutzen: stabilere Workflows, weniger Kontextwechsel, schnellere Umsetzung.")
with icp_col2:
    with st.container(border=True):
        st.markdown("#### 2) Datenanalyse & Zeitreihen-Forecasting")
        st.write("Typische Probleme: unübersichtliche Prozessdaten, fehlende Prognosen, Entscheidungen ohne belastbare Datengrundlage.")
        st.caption("Zielnutzen: transparente Kennzahlen, bessere Forecasts, fundiertere Planung.")
with icp_col3:
    with st.container(border=True):
        st.markdown("#### 3) Digitalisierung & KI-gestützte Prozessautomatisierung")
        st.write("Hilfe bei der Digitalisierung und Automatisierung von Prozessen mit Web-Apps, Python-Skripten und KI-Workflows.")
        st.caption("Zielnutzen: weniger manuelle Arbeit, weniger Fehler, schnellere Abläufe.")

st.divider()

col_metrics_1, col_metrics_2, col_metrics_3 = st.columns(3)
with col_metrics_1:
    st.metric("Kern-ICP", "3", help="Zielsegmente mit klarem Problemfit")
with col_metrics_2:
    st.metric("Showcase-Module", "6", help="Interaktive Demo-Module in den Seiten")
with col_metrics_3:
    st.metric("Pilot-Zeitrahmen", "2-6 Wochen", help="Typischer Zeitraum bis zum ersten nutzbaren Ergebnis")

st.divider()

st.markdown("### 🏗️ Umgesetzte Projekte (Auszug)")
p_col1, p_col2 = st.columns(2)

with p_col1:
    with st.container(border=True):
        st.markdown("#### 🤖 AI Orchestrator")
        st.write("*Autonome Agenten-Steuerung & Multi-Provider Routing.*")
        st.write("Ein robuster Python-Orchestrator mit Markdown-Warteschlange, automatischem Provider-Fallback und Telegram-Anbindung zur Fernsteuerung.")
        st.caption("Relevanz: interne Developer-/Ops-Automatisierung")
        st.page_link("pages/02_AI_ORCHESTRATOR.py", label="Zur Seite", icon="➡️")

    with st.container(border=True):
        st.markdown("#### ⚙️ Signalverarbeitung")
        st.write("*Automatisierte NVH-Analyse & Campbell-Diagramme.*")
        st.write("Hochleistungs-Pipeline zur Transformation von Zeitrohdaten in ingenieurtechnische Grafiken (FFT, Ordnungsanalyse).")
        st.caption("Relevanz: Maschinenbau, Prüfstand, Entwicklungsabteilung")
        st.page_link("pages/04_SIGNAL_PROC.py", label="Zur Seite", icon="➡️")

    with st.container(border=True):
        st.markdown("#### 📊 Sales Intelligence")
        st.write("*KI-gestützte Lead-Generierung & Qualifizierung.*")
        st.write("Automatisierte Pipeline für technisches Lead-Scoring, URL-Enrichment und lokale LLM-basierte Firmenrecherche.")
        st.caption("Relevanz: technische Dienstleister mit kleinem Vertriebsteam")
        st.page_link("pages/06_SALES_AI.py", label="Zur Seite", icon="➡️")

with p_col2:
    with st.container(border=True):
        st.markdown("#### ☀️ Smart Grid Analytics")
        st.write("*EEG-Management & PV-Prognosen.*")
        st.write("Verwaltung von über 2.200 Zählpunkten mit hybrider ML-Architektur (XGBoost/Prophet) für präzise Solar-Ertragsprognosen.")
        st.caption("Relevanz: Energie-Communities und regionales Lastmanagement")
        st.page_link("pages/03_SMART_GRID.py", label="Zur Seite", icon="➡️")

    with st.container(border=True):
        st.markdown("#### 🏗️ EN13001 Tool-Suite")
        st.write("*Normgerechte Kranstatik & Bauteilauslegung.*")
        st.write("Umfassende Python-Suite für Berechnungen nach DIN EN 13001, inklusive automatisierter PDF-Berichte und Hot-Spot-Ermüdungsanalyse.")
        st.caption("Relevanz: Nachweisführung, Qualitätssicherung, Dokumentation")
        st.page_link("pages/05_EN13001_TOOLS.py", label="Zur Seite", icon="➡️")

    with st.container(border=True):
        st.markdown("#### 🛋️ Social Media AI")
        st.write("*Creative Automation für den Premium-Retail.*")
        st.write("KI-gesteuerter Content-Lebenszyklus von der Bildanalyse über plattformübergreifende Texte bis zur regionalen SEO-Optimierung.")
        st.caption("Relevanz: Retail-Teams ohne großes internes Content-Team")
        st.page_link("pages/07_SOCIAL_MEDIA_AI.py", label="Zur Seite", icon="➡️")

st.divider()

st.markdown("### 🔧 Simulation & Konstruktion")
st.markdown(
    "Für Anfragen zu **Konstruktion, FEM-Analysen und Simulation im Fahrzeug- und Maschinenbau**: "
    "[www.linked-engineering.com](https://www.linked-engineering.com)"
)
st.info("Nutze die Seitenliste links, um die einzelnen Lösungsbausteine als interaktive Demo anzusehen.")
