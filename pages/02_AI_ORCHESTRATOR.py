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

st.subheader("🤖 Autonomous Task Orchestration")
render_demo_notice()
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
        | `cwd:` | Setzt das Arbeitsverzeichnis | `cwd:D:\\projects\\app` |
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
        
        st.chat_message("user").write("/task Fixe Bug in analytics.py cwd:D:\\proj #claude")
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
