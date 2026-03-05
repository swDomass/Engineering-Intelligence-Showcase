import streamlit as st
import numpy as np
import plotly.graph_objects as go
import time

from ui_shared import COLOR_PRIMARY, PLOTLY_DARK_LAYOUT, init_page, render_demo_notice, render_header, render_sidebar

init_page()
render_header()
render_sidebar()

st.subheader("⚙️ NVH Signal Processing: Zeitrohdaten to Insights")
render_demo_notice()
st.markdown("""
*Vom Rauschen zur Resonanz: Automatisierte Aufbereitung von Zeitrohdaten für die Schwingungsanalyse.
Dieses Modul transformiert komplexe Sensor-Signale in klare Entscheidungsgrundlagen.*
""")
st.caption("Simulationsfokus: Fahrzeug- und Maschinenbau (NVH, Resonanzanalyse, FEM-Export).")
st.markdown(
    "Konstruktions- und Simulationsanfragen: "
    "[www.linked-engineering.com](https://www.linked-engineering.com)"
)

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
        - **FEM-Export:** Direkte Generierung von `.fem` RLOAD-Dateien für den Import der Lastdaten in die Simulationen.
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

@st.cache_data
def _build_campbell_data():
    np.random.seed(42)
    rpm_range = np.arange(500, 5001, 25)
    freq_range = np.arange(0, 1001, 2)
    z_campbell = np.random.normal(0.01, 0.005, (len(freq_range), len(rpm_range)))
    for order in [1, 2, 3, 4, 6]:
        for j, rpm in enumerate(rpm_range):
            target_freq = (rpm / 60.0) * order
            idx = np.argmin(np.abs(freq_range - target_freq))
            if idx < len(freq_range):
                resonance_factor = 1.0 + 2.0 * np.exp(-((rpm - 3200)**2) / (2 * 400**2))
                z_campbell[idx, j] += 0.5 * resonance_factor + np.random.normal(0, 0.05)
    idx_res = np.argmin(np.abs(freq_range - 240))
    z_campbell[idx_res, :] += 0.2 * np.exp(-((rpm_range - 3200)**2) / (2 * 1000**2))
    order_2 = 0.4 * (rpm_range / 1000)**1.5 + 0.8 * np.exp(-((rpm_range - 3250)**2) / (2 * 250**2))
    order_4 = 0.2 * (rpm_range / 1000)**1.2 + 0.3 * np.exp(-((rpm_range - 4100)**2) / (2 * 300**2))
    return rpm_range, freq_range, z_campbell, order_2, order_4

rpm_range, freq_range, z_campbell, order_2, order_4 = _build_campbell_data()

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

fig_camp.update_layout(**PLOTLY_DARK_LAYOUT, xaxis_title="DREHZAHL [RPM]", yaxis_title="FREQUENZ [Hz]", height=600)
st.plotly_chart(fig_camp, use_container_width=True)

# -- Motor Order Cut --
st.write("📈 **Motor Order Cuts (Structural Health Analysis)**")

col_cut1, col_cut2 = st.columns([2, 1])

with col_cut1:
    fig_order = go.Figure()
    fig_order.add_trace(go.Scatter(x=rpm_range, y=order_2, name="Order 2.0 (Resonance @3250)", line=dict(color=COLOR_PRIMARY, width=3)))
    fig_order.add_trace(go.Scatter(x=rpm_range, y=order_4, name="Order 4.0", line=dict(color='#8b949e', width=2, dash='dot')))

    fig_order.update_layout(**PLOTLY_DARK_LAYOUT, xaxis_title="RPM", yaxis_title="Amplitude [g]", legend=dict(orientation="h", y=1.1), height=400)
    st.plotly_chart(fig_order, use_container_width=True)

order_csv_rows = ["RPM,Order2.0,Order4.0"]
order_csv_rows.extend(
    f"{rpm},{order2:.6f},{order4:.6f}"
    for rpm, order2, order4 in zip(rpm_range, order_2, order_4)
)
order_csv_data = "\n".join(order_csv_rows)

with col_cut2:
    st.info("**ANALYSE:** Die 2. Motorordnung zeigt eine ausgeprägte Resonanz bei ca. 3.250 RPM. Dies deutet auf eine Kopplung mit der ersten Biegeeigenform des Kranauslegers hin.")
    st.write("🛠️ **Export Options:**")
    st.download_button(
        "DOWNLOAD CSV (ORDER DATA)",
        order_csv_data,
        file_name="orders.csv",
        mime="text/csv",
    )
    st.button("GENERATE .FEM (RLOAD)", help="Erstellt eine Hypermesh-kompatible Datei")

if st.button("RUN SIGNAL PIPELINE (MOCK)"):
    with st.status("Aufbereitung der Zeitrohdaten läuft..."):
        prog = st.progress(0)
        st.write("Lade Zeitreihen (8.192 Hz)...")
        time.sleep(0.8)
        st.write("Hanning-Fensterung & FFT-Berechnung...")
        prog.progress(0.4)
        time.sleep(1.0)
        st.write("Phasen-Referenzierung zu Sensor '00-REF'...")
        prog.progress(0.7)
        time.sleep(0.6)
        st.write("Mittelung über 4 Messreihen abgeschlossen.")
        prog.progress(1.0)
    st.success("CAMPBELL-MATRIX erfolgreich generiert.")
