import streamlit as st

def render_ui():
    st.markdown("""
        <style>
            /* =========================================================
            SECTION 1: CSS CUSTOM PROPERTIES (VARIABLES)
            ========================================================= */
            
            /* 1.1 LIGHT MODE VARIABLES (DEFAULT OVERRIDES) */
            :root {
                --header-bg: rgba(255, 255, 255, 0.85);
                --footer-bg: rgba(255, 255, 255, 0.90);
                --card-bg: rgba(255, 255, 255, 0.6);
                --alert-bg: rgba(240, 242, 246, 0.8);
                --select-bg: rgba(255, 255, 255, 1);
                
                --text-main: #1f2937;
                --text-muted: #4b5563;
                --accent-color: #E50914;
                
                --border-subtle: rgba(0, 0, 0, 0.05);
                --shadow-header: 0 4px 20px rgba(0, 0, 0, 0.08);
                --shadow-footer: 0 -4px 20px rgba(0, 0, 0, 0.08);
                --shadow-card: 0 10px 20px rgba(0, 0, 0, 0.05);
                --shadow-card-hover: 0 15px 30px rgba(0, 0, 0, 0.12);
                
                --blur-intensity: blur(20px);
                --webkit-blur-intensity: blur(20px);
            }

            /* 1.2 DARK MODE VARIABLES (MEDIA QUERY AUTO-SWITCH) */
            @media (prefers-color-scheme: dark) {
                :root {
                    --header-bg: rgba(14, 17, 23, 0.85);
                    --footer-bg: rgba(14, 17, 23, 0.95);
                    --card-bg: rgba(30, 30, 30, 0.4);
                    --alert-bg: rgba(38, 39, 48, 0.7);
                    --select-bg: rgba(38, 39, 48, 1);
                    
                    --text-main: #ffffff;
                    --text-muted: #9ca3af;
                    --accent-color: #E50914;
                    
                    --border-subtle: rgba(255, 255, 255, 0.05);
                    --shadow-header: 0 4px 20px rgba(0, 0, 0, 0.5);
                    --shadow-footer: 0 -4px 20px rgba(0, 0, 0, 0.5);
                    --shadow-card: 0 10px 20px rgba(0, 0, 0, 0.4);
                    --shadow-card-hover: 0 15px 30px rgba(0, 0, 0, 0.6);
                }
            }

            /* =========================================================
            SECTION 2: GLOBAL RESETS & STREAMLIT UI HIDING
            ========================================================= */
            
            #MainMenu, footer, header[data-testid="stHeader"], [data-testid="stToolbar"], .stDeployButton {
                display: none !important;
            }

            .block-container {
                padding-top: 140px !important; 
                padding-bottom: 100px !important;
                max-width: 1200px !important;
                transition: padding 0.3s ease-in-out;
            }

            /* =========================================================
            SECTION 3: FIXED TOP HEADER STYLING
            ========================================================= */
            
            .adaptive-header {
                position: fixed !important;
                top: 0 !important;
                left: 0 !important;
                width: 100% !important;
                background: var(--header-bg) !important;
                backdrop-filter: var(--blur-intensity) !important;
                -webkit-backdrop-filter: var(--webkit-blur-intensity) !important;
                z-index: 999999 !important;
                text-align: center !important;
                padding: 20px 10px 15px 10px !important;
                border-bottom: 1px solid var(--border-subtle) !important;
                box-shadow: var(--shadow-header) !important;
                transition: background 0.3s ease, border 0.3s ease, box-shadow 0.3s ease;
                animation: slideDown 0.6s cubic-bezier(0.16, 1, 0.3, 1) forwards;
            }

            .adaptive-title {
                font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
                font-weight: 900 !important;
                font-size: clamp(28px, 5vw, 42px) !important;
                word-break: keep-all !important;
                color: var(--accent-color) !important;
                margin: 0 !important;
                margin-left: 30px !important;
                padding-bottom: 5px !important;
                letter-spacing: -0.5px !important;
                line-height: 1.1 !important;
            }

            .adaptive-subtitle {
                font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
                color: var(--text-muted) !important;
                font-size: clamp(14px, 3vw, 18px) !important;
                font-weight: 500 !important;
                margin: 0 !important;
                letter-spacing: 0.2px !important;
                line-height: 1.4 !important;
            }

            /* =========================================================
            SECTION 4: FIXED BOTTOM FOOTER STYLING
            ========================================================= */
            
            .adaptive-footer {
                position: fixed !important;
                left: 0 !important;
                bottom: 0 !important;
                width: 100% !important;
                background: var(--footer-bg) !important;
                backdrop-filter: var(--blur-intensity) !important;
                -webkit-backdrop-filter: var(--webkit-blur-intensity) !important;
                color: var(--text-main) !important;
                font-weight: 600 !important;
                border-top: 3px solid var(--accent-color) !important;
                z-index: 999999 !important;
                text-align: center !important;
                padding: 16px !important;
                font-size: 15px !important;
                box-shadow: var(--shadow-footer) !important;
                font-family: 'Inter', sans-serif !important;
                animation: slideUp 0.6s cubic-bezier(0.16, 1, 0.3, 1) forwards;
            }

            /* =========================================================
            SECTION 5: STREAMLIT INPUT WIDGETS OVERRIDES
            ========================================================= */
            
            div[data-baseweb="select"] {
                margin-top: 10px !important;
                margin-bottom: 20px !important;
            }

            div[data-baseweb="select"] > div {
                background-color: var(--select-bg) !important;
                border: 1px solid var(--border-subtle) !important;
                color: var(--text-main) !important;
                border-radius: 8px !important;
                box-shadow: inset 0 2px 4px rgba(0,0,0,0.02) !important;
                padding: 2px 5px !important;
            }
            
            div[data-baseweb="select"] > div:hover {
                border-color: var(--accent-color) !important;
            }

            div[data-baseweb="select"] * {
                color: var(--text-main) !important;
            }

            /* =========================================================
            SECTION 6: ALERTS & INFO BOXES
            ========================================================= */
            
            div[data-testid="stAlert"] {
                background-color: var(--alert-bg) !important;
                border: 1px solid var(--border-subtle) !important;
                color: var(--text-main) !important;
                backdrop-filter: blur(10px) !important;
                -webkit-backdrop-filter: blur(10px) !important;
                border-radius: 10px !important;
                padding: 15px 20px !important;
                margin-bottom: 25px !important;
                display: flex !important;
                align-items: center !important;
                justify-content: center !important;
            }

            div[data-testid="stAlert"] div {
                color: var(--text-main) !important;
                font-weight: 600 !important;
                font-size: 16px !important;
            }

            /* =========================================================
            SECTION 6.5: CATEGORY SECTION TITLES
            ========================================================= */
            .section-title {
                text-align: left !important;
                color: var(--text-main) !important; /* Adaptive: Dark in Light mode, White in Dark mode */
                font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
                font-weight: 800 !important;
                padding-top: 35px !important;
                padding-bottom: 15px !important;
                font-size: clamp(1.2rem, 3vw, 1.4rem) !important;
                letter-spacing: 0.5px !important;
                border-bottom: 2px solid var(--border-subtle) !important; /* Premium look ke liye ek halki line */
                margin-bottom: 20px !important;
            }

            /* =========================================================
            SECTION 7: MOVIE GRID SYSTEM
            ========================================================= */
            
            .poster-container {
                display: grid !important;
                grid-template-columns: repeat(2, 1fr) !important;
                gap: 15px !important;
                margin-bottom: 30px !important;
                padding: 10px 0 !important;
            }

            @media (min-width: 600px) {
                .poster-container { grid-template-columns: repeat(3, 1fr) !important; gap: 20px !important; }
            }
            
            @media (min-width: 900px) {
                .poster-container { grid-template-columns: repeat(5, 1fr) !important; gap: 25px !important; }
            }

            /* =========================================================
            SECTION 8: MOVIE CARD COMPONENT
            ========================================================= */
            
            .movie-card {
                text-align: center !important;
                border-radius: 14px !important;
                padding: 10px !important;
                transition: transform 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275), box-shadow 0.4s ease, background 0.3s ease !important;
                background-color: var(--card-bg) !important;
                border: 1px solid var(--border-subtle) !important;
                display: flex !important;
                flex-direction: column !important;
                justify-content: flex-start !important;
                align-items: center !important;
                height: 100% !important;
                box-shadow: var(--shadow-card) !important;
                position: relative !important;
                overflow: hidden !important;
                animation: fadeIn 0.8s ease forwards;
            }

            .movie-card:hover {
                transform: translateY(-10px) scale(1.02) !important;
                box-shadow: var(--shadow-card-hover) !important;
                background-color: var(--select-bg) !important;
                z-index: 10 !important;
            }

            .movie-poster {
                width: 100% !important;
                aspect-ratio: 2 / 3 !important;
                border-radius: 10px !important;
                margin-bottom: 15px !important;
                object-fit: cover !important;
                transition: filter 0.3s ease !important;
                background-color: #2a2a2a !important; 
            }
            
            .movie-card:hover .movie-poster {
                filter: brightness(1.05) contrast(1.05) !important;
            }

            .movie-title-card {
                font-family: 'Inter', sans-serif !important;
                font-size: clamp(13px, 1.5vw, 16px) !important;
                font-weight: 700 !important;
                color: var(--text-main) !important;
                line-height: 1.4 !important;
                letter-spacing: 0.2px !important;
                display: -webkit-box !important;
                -webkit-line-clamp: 2 !important;
                -webkit-box-orient: vertical !important;
                overflow: hidden !important;
                text-overflow: ellipsis !important;
                min-height: 45px !important;
                width: 100% !important;
                margin-top: auto !important;
                padding: 0 5px !important;
            }

            /* =========================================================
            SECTION 9: RESPONSIVE MEDIA QUERIES (MOBILE FIXES)
            ========================================================= */
            
            @media (max-width: 768px) {
                .block-container {
                    padding-top: 90px !important; /* Mobile me top space kam kiya */
                    padding-bottom: 70px !important;
                    padding-left: 10px !important;
                    padding-right: 10px !important;
                }
                
                .adaptive-header {
                    padding: 10px 5px 8px 5px !important; /* Mobile me padding ekdum compact ki */
                }

                .adaptive-title {
                    font-size: clamp(20px, 6vw, 24px) !important; /* Mobile me Title size adjust kiya */
                    padding-bottom: 2px !important;
                }

                .adaptive-subtitle {
                    font-size: clamp(11px, 3.5vw, 13px) !important; /* Mobile me subtitle ek line me lane ke liye adjust kiya */
                    line-height: 1.2 !important;
                }
                
                .adaptive-footer {
                    padding: 10px !important;
                    font-size: 12px !important;
                }
                
                .movie-card {
                    padding: 6px !important;
                    border-radius: 10px !important;
                }
                
                .movie-poster {
                    margin-bottom: 10px !important;
                    border-radius: 8px !important;
                }
                
                .movie-title-card {
                    min-height: 40px !important;
                    font-size: 12px !important;
                }
            }

            /* =========================================================
            SECTION 10: CUSTOM KEYFRAME ANIMATIONS
            ========================================================= */
            
            @keyframes fadeIn {
                0% { opacity: 0; transform: translateY(20px); }
                100% { opacity: 1; transform: translateY(0); }
            }
            
            @keyframes slideDown {
                0% { transform: translateY(-100%); opacity: 0; }
                100% { transform: translateY(0); opacity: 1; }
            }
            
            @keyframes slideUp {
                0% { transform: translateY(100%); opacity: 0; }
                100% { transform: translateY(0); opacity: 1; }
            }

            /* =========================================================
            SECTION 11: MISCELLANEOUS UTILITIES
            ========================================================= */
            
            ::-webkit-scrollbar { width: 8px !important; background: transparent !important; }
            ::-webkit-scrollbar-track { background: rgba(0,0,0,0.05) !important; }
            @media (prefers-color-scheme: dark) { ::-webkit-scrollbar-track { background: rgba(255,255,255,0.05) !important; } }
            ::-webkit-scrollbar-thumb { background: rgba(150, 150, 150, 0.5) !important; border-radius: 10px !important; }
            ::-webkit-scrollbar-thumb:hover { background: var(--accent-color) !important; }
            a { text-decoration: none !important; outline: none !important; }
        </style>

        <!-- =========================================================
            SECTION 12: HTML INJECTION (HEADER & FOOTER DOM)
            ========================================================= -->
            
        <!-- FIXED TOP HEADER -->
        <div class="adaptive-header">
            <h1 class="adaptive-title">The Movie Matrix 🍿</h1>
            <p class="adaptive-subtitle">Discover your next favorite movie based on your tastes!</p>
        </div>

        <!-- FIXED BOTTOM FOOTER -->
        <div class="adaptive-footer">
            Engineered with ❤️ by Lokendra Kushwaha
        </div>
    """, unsafe_allow_html=True)