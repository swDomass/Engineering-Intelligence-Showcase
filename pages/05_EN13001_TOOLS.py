import streamlit as st
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import time

from ui_shared import init_page, render_demo_notice, render_header, render_sidebar

MATERIAL_YIELD_STRENGTHS = {
    "S235": 235,
    "S355": 355,
    "S460": 460,
    "S690": 690,
}

init_page()
render_header()
render_sidebar()

st.subheader("🏗️ EN13001 Tool-Suite: Structural Crane Component Design")
render_demo_notice()
st.markdown("""
*Präzision trifft Normkonformität: Eine umfassende Berechnungs-Suite für die Auslegung von Krankomponenten nach DIN EN 13001. 
Digitalisierung komplexer Nachweise für höchste Sicherheit und Effizienz.*
""")
st.caption("Praxisfokus: Konstruktion und Simulation im Maschinenbau, inkl. normnaher Nachweisführung.")
st.markdown(
    "Konstruktions- und Simulationsanfragen: "
    "[www.linked-engineering.com](https://www.linked-engineering.com)"
)

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
    f_yd = MATERIAL_YIELD_STRENGTHS.get(material, 235)
    # alpha_w calculation mock (Table 8 simplification)
    alpha_w = 0.9 if weld_quality == "Gruppe C (High)" else 0.6
    
    # Combined stress (Eq. 29)
    sigma_v = np.sqrt(stress_sigma**2 + 3 * stress_tau**2)
    allowable_stress = f_yd * alpha_w
    utilization = (sigma_v / allowable_stress) * 100 if allowable_stress > 0 else 0.0
    
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
        st.error(f"⚠️ **NACHWEIS NICHT ERFÜLLT!** Kombinierte Spannung ({sigma_v:.1f} MPa) überschreitet Grenzspannung ({allowable_stress:.1f} MPa).")
    elif utilization == 0:
        st.success("✅ **NACHWEIS ERFÜLLT.** Ausnutzung: 0.0%. Sicherheitsfaktor: ∞ (keine Last).")
    else:
        st.success(f"✅ **NACHWEIS ERFÜLLT.** Ausnutzung: {utilization:.1f}%. Sicherheitsfaktor: {(100 / utilization):.2f}")

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
