import streamlit as st

from ui_shared import init_page, render_demo_notice, render_header, render_sidebar

init_page()
render_header()
render_sidebar()

st.subheader("🛋️ Premium Interior: Social Media & SEO Automation")
render_demo_notice()
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
