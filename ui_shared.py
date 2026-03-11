import streamlit as st

SHOWCASE_TITLE = "Python-Automatisierung | Showcase"
SIMULATION_NOTICE = (
    "Aus Datenschutz- und NDA-Gründen zeigt dieses Dashboard ausschließlich "
    "simulierte bzw. anonymisierte Beispieldaten."
)

# Brand colours — single source of truth for Python/Plotly code
# (CSS in apply_styles uses these values inline as strings)
COLOR_PRIMARY = "#6caf2b"
COLOR_BG = "#0d1117"
COLOR_BORDER = "#30363d"
COLOR_TEXT = "#c9d1d9"
COLOR_MUTED = "#8b949e"
COLOR_DANGER = "#ff4b4b"
COLOR_ACCENT = "#ffcc00"

# Base Plotly layout — spread with ** into every fig.update_layout()
PLOTLY_DARK_LAYOUT: dict = dict(
    template="plotly_dark",
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font_family="JetBrains Mono",
)


def init_page(page_title: str | None = None) -> None:
    st.set_page_config(page_title=page_title or SHOWCASE_TITLE, page_icon="⚙️", layout="wide")
    apply_styles()


def apply_styles() -> None:
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #0d1117;
            background-image:
                linear-gradient(rgba(108, 175, 43, 0.05) 1px, transparent 1px),
                linear-gradient(90deg, rgba(108, 175, 43, 0.05) 1px, transparent 1px);
            background-size: 50px 50px;
        }

        @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;700&family=JetBrains+Mono&display=swap');

        html, body {
            font-family: 'Space Grotesk', sans-serif !important;
            color: #c9d1d9 !important;
        }

        /* Streamlit text elements — explicit selectors, browser-safe */
        /* Note: span intentionally excluded to not break Material Icons font */
        p, li, label,
        h1, h2, h3, h4, h5, h6,
        .stMarkdown, .stText,
        [data-testid="stMarkdownContainer"],
        [data-testid="stText"],
        [data-testid="stCaptionContainer"],
        [data-testid="stWidgetLabel"],
        [data-testid="stSidebarContent"] {
            color: #c9d1d9 !important;
            font-family: 'Space Grotesk', sans-serif !important;
        }

        [data-testid="stHeader"] {
            background: rgba(13, 17, 23, 0.95);
            backdrop-filter: blur(10px);
            border-bottom: 1px solid #30363d;
        }

        [data-testid="stMetricValue"] {
            font-family: 'JetBrains Mono', monospace;
            color: #6caf2b;
            font-size: 2rem !important;
        }

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

        .stAlert {
            background-color: rgba(10, 22, 40, 0.6);
            border: 1px solid #30363d;
            border-left: 5px solid #6caf2b;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def render_header() -> None:
    col_logo, col_title = st.columns([1, 4])
    with col_title:
        st.title("Python und KI Automatisierung für Unternehmen")
        st.markdown("*Showcase: KI-Workflows, Engineering-Analytik und Prozessautomatisierung*")
    st.divider()


def render_demo_notice() -> None:
    st.caption(f"🔒 {SIMULATION_NOTICE}")


def render_sidebar() -> None:
    st.sidebar.markdown("### 🧭 Navigation")
    st.sidebar.page_link("app.py", label="Übersicht", icon="🏠")
    st.sidebar.page_link("pages/02_AI_ORCHESTRATOR.py", label="AI Orchestrator", icon="🤖")
    st.sidebar.page_link("pages/03_SMART_GRID.py", label="Smart Grid", icon="☀️")
    st.sidebar.page_link("pages/04_SIGNAL_PROC.py", label="Signal Processing", icon="⚙️")
    st.sidebar.page_link("pages/05_EN13001_TOOLS.py", label="EN13001 Tools", icon="🏗️")
    st.sidebar.page_link("pages/06_SALES_AI.py", label="Sales AI", icon="📊")
    st.sidebar.page_link("pages/07_SOCIAL_MEDIA_AI.py", label="Social Media AI", icon="🛋️")
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 🤝 So starten wir")
    st.sidebar.markdown(
        """
1. Kurz-Check (15-20 Min)
2. Mini-Scoping (48h)
3. Pilot (2-6 Wochen)
4. Rollout bei KPI-Fit
"""
    )
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 🌐 NETWORK")
    st.sidebar.markdown("🔗 **[LinkedIn Profile](https://www.linkedin.com/in/dominik-f-840ab919a/)**")
    st.sidebar.markdown("🔗 **[Linked Engineering (Konstruktion & Simulation)](https://www.linked-engineering.com)**")
    st.sidebar.markdown("---")
    st.sidebar.caption("🔒 Alle Kennzahlen und Ausgaben sind simulierte bzw. anonymisierte Beispieldaten (NDA).")
    st.sidebar.caption("© 2026 Engineering Intelligence Showcase Dashboard")
