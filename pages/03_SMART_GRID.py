import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import time

from ui_shared import init_page, render_demo_notice, render_header, render_sidebar

init_page()
render_header()
render_sidebar()

st.subheader("☀️ Smart Grid Analytics: Energy Community & PV Forecast")
render_demo_notice()
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
        - **Komplexität:** Manuelle Auswertung von 2.200+ Zählpunkten in 15-Minuten-Intervallen ist nicht skalierbar.
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
