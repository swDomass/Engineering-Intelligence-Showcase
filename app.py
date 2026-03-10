import streamlit as st

from ui_shared import init_page, render_demo_notice, render_header, render_sidebar

init_page()
render_header()
render_sidebar()

render_demo_notice()

# ── Intro ───────────────────────────────────────────────────────────────
st.markdown("""
**Ich unterstütze Engineering- und Tech-Teams dabei, Routineaufgaben zu automatisieren,
Prozessdaten sichtbar zu machen und KI sinnvoll in bestehende Abläufe zu integrieren.**

Kein "Code um des Codes willen" — Fokus auf messbare Entlastung in echten Betriebsprozessen.
""")

# ── Zielgruppen ─────────────────────────────────────────────────────────
icp_col1, icp_col2, icp_col3 = st.columns(3)
with icp_col1:
    with st.container(border=True):
        st.markdown("#### ⚡ Automatisierung für Entwicklungs-Teams")
        st.write("Wiederholte Routineaufgaben, Medienbrüche zwischen Tools, hoher manueller Abstimmungsaufwand.")
        st.caption("→ Stabilere Workflows, weniger Kontextwechsel, schnellere Umsetzung.")
with icp_col2:
    with st.container(border=True):
        st.markdown("#### 📈 Datenanalyse & Forecasting")
        st.write("Unübersichtliche Prozessdaten, fehlende Prognosen, Entscheidungen ohne belastbare Datengrundlage.")
        st.caption("→ Transparente Kennzahlen, bessere Forecasts, fundiertere Planung.")
with icp_col3:
    with st.container(border=True):
        st.markdown("#### 🤖 KI-gestützte Prozessautomatisierung")
        st.write("Digitalisierung mit Web-Apps, Python-Skripten und LLM-Workflows — direkt integrierbar in bestehende Prozesse.")
        st.caption("→ Weniger manuelle Arbeit, weniger Fehler, schnellere Abläufe.")

st.divider()

# ── Metriken ────────────────────────────────────────────────────────────
col_m1, col_m2, col_m3 = st.columns(3)
with col_m1:
    st.metric("Kern-Segmente", "3", help="Zielsegmente mit klarem Problemfit")
with col_m2:
    st.metric("Showcase-Module", "6", help="Interaktive Demo-Module in den Seiten")
with col_m3:
    st.metric("Pilot-Zeitrahmen", "2–6 Wo.", help="Typischer Zeitraum bis zum ersten nutzbaren Ergebnis")

st.divider()

# ── Projekte ────────────────────────────────────────────────────────────
st.markdown("### 🏗️ Umgesetzte Projekte")
st.caption("Alle Module sind live interaktiv — Kennzahlen aus Datenschutzgründen simuliert/anonymisiert (NDA).")

_TAG_STYLE = (
    "background:rgba(108,175,43,0.12);"
    "color:#6caf2b;"
    "border:1px solid rgba(108,175,43,0.3);"
    "border-radius:4px;"
    "padding:2px 8px;"
    "font-size:0.72rem;"
    "font-family:'JetBrains Mono',monospace;"
)


def _tags_html(*tags: str) -> str:
    badges = "".join(f'<span style="{_TAG_STYLE}">{t}</span>' for t in tags)
    return f'<div style="display:flex;gap:6px;flex-wrap:wrap;margin:10px 0 4px;">{badges}</div>'


def project_card(icon: str, title: str, subtitle: str, body: str, relevance: str, page: str, *tags: str) -> None:
    with st.container(border=True):
        st.markdown(
            f'<div style="border-left:3px solid #6caf2b;padding-left:12px;margin-bottom:8px;">'
            f'<span style="font-size:1.05rem;font-weight:700;">{icon} {title}</span><br>'
            f'<span style="color:#8b949e;font-size:0.85rem;font-style:italic;">{subtitle}</span>'
            f'</div>',
            unsafe_allow_html=True,
        )
        st.write(body)
        if tags:
            st.markdown(_tags_html(*tags), unsafe_allow_html=True)
        st.caption(f"Relevanz: {relevance}")
        st.page_link(page, label="Demo ansehen", icon="➡️")


p_col1, p_col2 = st.columns(2)

with p_col1:
    project_card(
        "🤖", "AI Orchestrator", "Autonome Agenten-Steuerung & Multi-Provider Routing",
        "Robuster Python-Orchestrator mit Markdown-Warteschlange, automatischem Provider-Fallback "
        "und Telegram-Anbindung zur Fernsteuerung.",
        "Developer-/Ops-Automatisierung",
        "pages/02_AI_ORCHESTRATOR.py",
        "Python", "LLM", "Telegram", "Multi-Provider",
    )
    project_card(
        "⚙️", "Signalverarbeitung", "Automatisierte NVH-Analyse & Campbell-Diagramme",
        "Hochleistungs-Pipeline zur Transformation von Zeitrohdaten in ingenieurtechnische "
        "Grafiken (FFT, Ordnungsanalyse).",
        "Maschinenbau, Prüfstand, Entwicklungsabteilung",
        "pages/04_SIGNAL_PROC.py",
        "FFT", "NVH", "SciPy", "Plotly",
    )
    project_card(
        "📊", "Sales Intelligence", "KI-gestützte Lead-Generierung & Qualifizierung",
        "Automatisierte Pipeline für technisches Lead-Scoring, URL-Enrichment "
        "und lokale LLM-basierte Firmenrecherche.",
        "Technische Dienstleister mit kleinem Vertriebsteam",
        "pages/06_SALES_AI.py",
        "LLM", "Web-Scraping", "Lead-Scoring", "Python",
    )

with p_col2:
    project_card(
        "☀️", "Smart Grid Analytics", "EEG-Management & PV-Prognosen",
        "Verwaltung von über 2.200 Zählpunkten mit hybrider ML-Architektur (XGBoost/Prophet) "
        "für präzise Solar-Ertragsprognosen.",
        "Energie-Communities und regionales Lastmanagement",
        "pages/03_SMART_GRID.py",
        "XGBoost", "Prophet", "ML", "Timeseries",
    )
    project_card(
        "🏗️", "EN13001 Tool-Suite", "Normgerechte Kranstatik & Bauteilauslegung",
        "Umfassende Python-Suite für Berechnungen nach DIN EN 13001, inklusive "
        "automatisierter PDF-Berichte und Hot-Spot-Ermüdungsanalyse.",
        "Nachweisführung, Qualitätssicherung, Dokumentation",
        "pages/05_EN13001_TOOLS.py",
        "DIN EN 13001", "FEM", "PDF-Reports", "Python",
    )
    project_card(
        "🛋️", "Social Media AI", "Creative Automation für den Premium-Retail",
        "KI-gesteuerter Content-Lebenszyklus von der Bildanalyse über plattformübergreifende "
        "Texte bis zur regionalen SEO-Optimierung.",
        "Retail-Teams ohne großes internes Content-Team",
        "pages/07_SOCIAL_MEDIA_AI.py",
        "LLM", "SEO", "Content AI", "Instagram",
    )

st.divider()

st.markdown("### 🔧 Simulation & Konstruktion")
st.markdown(
    "Für Anfragen zu **Konstruktion, FEM-Analysen und Simulation im Fahrzeug- und Maschinenbau**: "
    "[www.linked-engineering.com](https://www.linked-engineering.com)"
)
st.info("Nutze die Seitenliste links, um die einzelnen Lösungsbausteine als interaktive Demo anzusehen.")
