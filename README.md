# Engineering Intelligence Showcase 🚀

Welcome! I am a **Mechanical Engineer** and **Python Developer** specializing in bridging the gap between deep technical engineering, data science, and modern AI-driven automation.

This repository serves as a **public dashboard** for my private projects in the fields of **AI Orchestration, Signal Processing, and Process Automation**.

---

## 🏗️ Core Project Pillars

### 2. AI Orchestrator: Autonomous Agent Control (AI / Sales Ops)
*   **Project:** `AI_orchestrator`
*   **Problem:** Managing multiple AI agents and long-running tasks across different providers (Claude, Gemini, Codex) without manual intervention.
*   **Solution:** A robust Python-based orchestrator with a Markdown-based queue system, automated provider fallbacks, and a **Telegram integration** for remote control and approvals.
*   **Advanced Features:**
    *   **Usage Suggester:** Proactively suggests tasks (Vault-Skills, Git-Changes, failed retries) via Telegram when provider limits (Claude) are about to reset and capacity is unused.
    *   **Heartbeat Mechanism:** Continuous monitoring of system health, disk space, and git status, with automated summaries and cleanup tasks.
    *   **Policy Engine:** Fine-grained security layer (AUTO / APPROVE / DENY) with interactive Telegram approvals for risky operations.
    *   **Analytics Dashboard:** Built-in web dashboard (Chart.js) for tracking task success rates, provider utilization, and capacity timelines.
*   **Key Tech:** Python 3.10+, Telegram Bot API, Multi-Provider Routing (Claude/Gemini/Codex), YAML-based Policy Engine, TF-IDF Memory System.
*   **Impact:** Fully autonomous execution of coding, review, and documentation tasks with human-in-the-loop safety layers.

### 3. Smart Grid Analytics: Energy Community Management & PV Forecast (Energy / ML)
*   **Project:** `energy_community_analysis`
*   **Problem:** Managing decentralized energy communities (EEG) with thousands of members requires precise tracking of 15-minute consumption/generation data and accurate forecasting to optimize local energy usage.
*   **Solution:** A comprehensive energy management system for a **regional energy community** (2,200+ metering points). It features a robust ETL pipeline, quarterly data partitioning in SQLite, and an interactive Dash dashboard for real-time analytics.
*   **Advanced Features:**
    *   **PV Forecasting:** Hybrid ML approach using **XGBoost and Prophet** to predict solar generation based on 140+ features (temporal, astronomical, and weather-specific like fog risk).
    *   **Weather Integration:** Real-time data from Open-Meteo and Solcast, combined with clear-sky models for high-accuracy predictions.
    *   **Smart Analytics:** Automated calculation of self-sufficiency (Eigendeckung), grid interaction, and community-wide energy balance.
*   **Key Tech:** Python (uv), SQLite (WAL-mode), XGBoost, Prophet, pvlib, Dash/Plotly, Optuna.
*   **Impact:** Optimized local energy consumption and improved grid stability for an entire region.

### 4. Engineering Signal Processing: Zeitrohdaten (Mechanical Engineering)
*   **Project:** `Aufbereitung_Zeitrohdaten`
*   **Problem:** Raw vibration data from machinery (NVH - Noise, Vibration, Harshness) is complex and unorganized. Manual transformation of time-series data into frequency-domain insights (Campbell diagrams) is time-consuming and prone to errors.
*   **Solution:** A high-performance automated pipeline for cleaning and transforming raw 15-minute sensor data into engineering-grade charts. It handles multi-sensor synchronization, Hanning windowing, and high-resolution FFT (Fast Fourier Transform).
*   **Advanced Features:**
    *   **Automated Campbell Generation:** Converts time-series + RPM data into interactive Campbell matrices (Magnitude & Phase).
    *   **Motor Order Extraction:** Automatically extracts the first 5 motor orders (0.5 steps) for structural resonance analysis.
    *   **FEM Integration:** Generates `.fem` files (RLOAD curves) for direct import into Hypermesh/OptiStruct simulation workflows.
    *   **Phase-Reference Matching:** Calculates phase relationships relative to a specific reference sensor for mode shape identification.
*   **Key Tech:** Python, Signal Processing (FFT), NumPy, Hanning Windowing, Matplotlib/Plotly, FEM Export (RLOAD).
*   **Impact:** 90% reduction in manual data preparation time. Enables rapid structural health monitoring and precise identification of resonance issues in cranes and automotive components.

### 5. EN13001 Tool-Suite: Structural Crane Component Design (Mechanical Engineering)
*   **Project:** `EN13001_Tool-Suite`
*   **Problem:** Manual crane statics calculations according to EN 13001 are complex, time-consuming, and error-prone. Legacy tools (Matcad) were outdated and lacked modern integration.
*   **Solution:** A comprehensive Python-based suite for norm-compliant (DIN EN 13001) design of crane components. It features a modern PyQt6 GUI, automated PDF reporting, and high-precision calculation modules.
*   **Advanced Features:**
    *   **Multi-Module Architecture:** Specialized calculators for Bolts, Welds (V2.0 fully norm-compliant), Fatigue, Pins, Wheel-Rail contact, and Elastic Stability (Buckling/Piping).
    *   **Hot-Spot Integration:** Advanced fatigue analysis using the Hot-Spot method (IIW recommendations) with automated FEM node interpolation and extrapolation.
    *   **Norm-Compliance:** Rigorous implementation of DIN EN 13001-3-1 and 13001-3-3, including complex factors (e.g., weld quality factors $\alpha_w$ from Table 8).
    *   **Professional Output:** Generates detailed, audit-ready PDF reports with all calculation steps and norm references.
*   **Key Tech:** Python 3.11, PyQt6, NumPy, Matplotlib, ReportLab (PDF), PyInstaller (EXE).
*   **Impact:** 70% faster verification cycles for crane components. Direct transition from "raw FEM results" to "norm-compliant documentation".

### 6. AI-Driven Sales Automation (Sales Ops / AI)
*   **Project:** `Engineering-Sales-Intelligence`
*   **Problem:** High manual effort in lead generation, qualification, and CRM management for specialized engineering consultancies (FEM/CAE). Standard tools are too generic for deep-tech keyword requirements (e.g., distinguishing "EN 13001" from generic "statics").
*   **Solution:** A full-stack automation pipeline that collects leads from RSS, job portals (JobPortal-A), and Gmail alerts, scores them with engineering-specific logic, and manages them in a custom CRM.
*   **Advanced Features:**
    *   **Two-Stage Scoring:** Initial fast-scoring on metadata followed by deep-scoring via **URL Enrichment** (fetching full job descriptions only for promising leads) to save bandwidth and avoid rate limits.
    *   **Intelligent Parsing:** Uses **Local LLMs (Ollama/Qwen2.5)** and BeautifulSoup4 to extract structured data (salary, requirements, contacts) from messy email digests and HTML.
    *   **AI Chat Assistant:** A GUI-integrated chatbot (multi-provider: Claude/Gemini/Ollama) with **22 specialized tools** to query the database, move leads, update CRM interactions, and perform company research.
    *   **CRM & Orchestration:** Full lifecycle tracking from "Scout" (lead detection) to "Analyst" (company research) and "Author" (automated Gmail drafts with engineer-focused tone).
    *   **Multi-User Sync:** Coordinated access via a **Write Reservation System** for OneDrive or remote access via **Tailscale**.
*   **Key Tech:** Python 3.12, SQLite (WAL mode), Ollama, Gmail API (OAuth 2.0), Flask, Sentence Transformers (Semantic Search).
*   **Impact:** 80% reduction in lead-sourcing time. Transition from manual browsing to a "Human-in-the-loop" approval workflow where the engineer only reviews high-value, pre-qualified leads.

### 7. Social Media AI: Creative Ops & SEO Automation (Creative Ops / AI)
*   **Project:** `Boutique-SocialMedia` & `Vault-Skills`
*   **Problem:** High manual effort in creating consistent, high-quality social media content and SEO-optimized product pages for a specialized retail boutique across multiple platforms (Instagram, Facebook, Pinterest, TikTok, YouTube).
*   **Solution:** A specialized AI skill system integrated into an Obsidian vault that automates the entire content lifecycle—from professional image analysis to cross-platform copy generation and SEO optimization.
*   **Advanced Features:**
    *   **Multi-Platform Content Engine:** Generates tailored posts for 5+ platforms (Reels, TikToks, Pins) from a single set of product images, including voiceover scripts and text overlays.
    *   **Automated Image Branding Pipeline:** A Python-based processing engine that automatically applies brand-compliant overlays, logos, and color grading to raw product photos, ensuring 100% visual consistency across all channels.
    *   **Expert Image Analysis:** AI-driven analysis of products (e.g., designer furniture, lighting, materials) by an "AI Design Consultant" to ensure technically accurate and emotional descriptions.
    *   **Regional SEO Optimizer:** Specialized WordPress/Stackable block generator that crafts SEO-rich copy focused on regional keywords and appointment conversion for showroom visits.
    *   **Canva Integration:** Automated design suggestions and direct asset preparation for rapid visual content creation.
*   **Key Tech:** Python, Obsidian (Vault-Skills), OpenAI/Anthropic Vision APIs, WordPress REST API, Canva API, ElevenLabs (Voiceover).
*   **Impact:** 95% reduction in content creation time. Professional, consistent brand presence across all digital channels with a focus on local lead generation (showroom appointments).

---

## 🧪 Tech Stack & Standards
*   **AI/ML:** Autonomous Agents, Local LLMs (Ollama), OpenAI/Anthropic APIs.
*   **Engineering:** Signal Processing, Vibration Analysis (NVH), Structural Dynamics.
*   **Software Quality:** `uv` (Package Management), `ruff` (Linting), `mypy` (Type Safety), `pytest` (Testing).

---

## 🧠 The Engineering Intelligence Approach

My work is driven by three core principles that bridge the gap between classical engineering and modern data science:

1.  **Domain-First Data Science:** I don't just apply algorithms; I leverage my background as a **Mechanical Engineer** to understand the underlying physics (e.g., vibration modes, solar radiation patterns) before selecting a model.
2.  **Autonomous Reliability:** Systems should work for humans, not the other way around. My projects focus on **self-healing pipelines**, automated fallback mechanisms, and proactive monitoring.
3.  **Actionable Transparency:** Whether it's a Campbell diagram for a crane or an energy balance for a community, the goal is always to turn complex "black-box" data into clear, actionable insights for decision-makers.

---

## 🚀 Work with Me
I focus on **efficient, maintainable code** that delivers **measurable business value**.

*   **Status:** Available for freelance projects in Python automation, AI integration, and technical data analysis.
*   **Access:** These projects contain proprietary IP and are kept in private repositories. **Code access for specific modules can be granted upon request** after an initial consultation.

📧 **Contact:** https://www.linkedin.com/in/dominik-f-840ab919a/
