"""
CropCare AI - Plant Disease Identification System
Senior Agricultural AI Decision Support Application
Optimized with Streamlit Resource & Data Caching, Image Deduplication,
and Fail-Fast Initialization.
"""

import os
import sys
from datetime import datetime
from PIL import Image
import pandas as pd
import streamlit as st

# Ensure local imports work whether run from repo root or inside CropCare_AI
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
if CURRENT_DIR not in sys.path:
    sys.path.insert(0, CURRENT_DIR)

from model import (
    load_model,
    reset_model_cache,
    predict_image,
    compute_image_hash,
    get_model_info,
    MODEL_ID
)
from disease_info import (
    get_disease_info,
    get_all_disease_profiles,
    get_unique_crops,
    DISEASE_DATABASE
)


# ==========================================
# PAGE CONFIGURATION
# ==========================================
st.set_page_config(
    page_title="CropCare AI - Plant Disease Diagnosis",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ==========================================
# CUSTOM CSS: AGRICULTURE GREEN THEME
# ==========================================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
    }
    
    /* Hero Banner */
    .hero-banner {
        background: linear-gradient(135deg, #1B5E20 0%, #2E7D32 60%, #388E3C 100%);
        border-radius: 16px;
        padding: 28px 36px;
        color: #FFFFFF;
        box-shadow: 0 10px 25px rgba(27, 94, 32, 0.15);
        margin-bottom: 24px;
    }
    
    .hero-title {
        font-size: 2.1rem;
        font-weight: 800;
        margin-bottom: 8px;
        color: #FFFFFF;
        letter-spacing: -0.5px;
    }
    
    .hero-subtitle {
        font-size: 1.05rem;
        color: #E8F5E9;
        font-weight: 400;
        max-width: 850px;
        line-height: 1.5;
    }

    /* Metric Cards */
    .metric-card {
        background: #FFFFFF;
        border: 1px solid #E0E7E1;
        border-radius: 14px;
        padding: 18px 22px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.03);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    
    .metric-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 16px rgba(46, 125, 50, 0.08);
    }
    
    .metric-label {
        font-size: 0.85rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.6px;
        color: #556B59;
        margin-bottom: 6px;
    }
    
    .metric-value {
        font-size: 1.9rem;
        font-weight: 800;
        color: #1B5E20;
    }
    
    .metric-subtext {
        font-size: 0.8rem;
        color: #78909C;
        margin-top: 4px;
    }

    /* Content Cards */
    .cc-card {
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 14px;
        padding: 22px;
        margin-bottom: 20px;
        box-shadow: 0 3px 10px rgba(0, 0, 0, 0.02);
    }

    /* Badges */
    .badge-healthy {
        background-color: #E8F5E9;
        color: #2E7D32;
        border: 1px solid #A5D6A7;
        font-weight: 700;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 0.85rem;
        display: inline-block;
    }
    
    .badge-diseased {
        background-color: #FFEBEE;
        color: #C62828;
        border: 1px solid #FFCDD2;
        font-weight: 700;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 0.85rem;
        display: inline-block;
    }

    .badge-rank {
        background-color: #2E7D32;
        color: #FFFFFF;
        border-radius: 50%;
        width: 24px;
        height: 24px;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        font-size: 0.75rem;
        font-weight: bold;
    }

    /* Primary Result Banner */
    .result-banner {
        border-radius: 12px;
        padding: 18px 22px;
        margin-bottom: 20px;
    }
    
    .result-banner-healthy {
        background: linear-gradient(135deg, #E8F5E9 0%, #C8E6C9 100%);
        border: 1px solid #81C784;
    }
    
    .result-banner-diseased {
        background: linear-gradient(135deg, #FFF8E1 0%, #FFECB3 100%);
        border: 1px solid #FFD54F;
    }

    /* Sidebar custom styling */
    section[data-testid="stSidebar"] {
        background-color: #F8FAF8;
        border-right: 1px solid #E0E7E1;
    }
    
    /* Clean Buttons */
    .stButton > button {
        background-color: #2E7D32;
        color: #FFFFFF;
        border-radius: 8px;
        font-weight: 600;
        border: none;
        padding: 0.5rem 1.2rem;
        transition: background-color 0.2s ease, transform 0.1s ease;
    }
    
    .stButton > button:hover {
        background-color: #1B5E20;
        color: #FFFFFF;
        transform: translateY(-1px);
    }
</style>
""", unsafe_allow_html=True)


# ==========================================
# OPTIMIZED CACHING: MODEL & STATIC DATA
# ==========================================
@st.cache_resource(show_spinner=False)
def get_cached_model():
    """
    Loads and caches the pretrained MobileNetV2 model once across the runtime.
    Subsequent calls execute in ~0.0ms, avoiding model reloads across interactions.
    """
    return load_model(MODEL_ID)


@st.cache_data(show_spinner=False)
def get_cached_disease_info(class_name: str) -> dict:
    """Cached lookup of disease information to avoid re-parsing."""
    return get_disease_info(class_name)


@st.cache_data(show_spinner=False)
def get_cached_all_diseases() -> dict:
    """Cached retrieval of the 38-class agricultural database."""
    return get_all_disease_profiles()


@st.cache_data(show_spinner=False)
def get_cached_crops() -> list:
    """Cached list of unique host plant crops."""
    return get_unique_crops()


# ==========================================
# SESSION STATE INITIALIZATION
# ==========================================
if "history" not in st.session_state:
    st.session_state.history = []

if "total_scans" not in st.session_state:
    st.session_state.total_scans = 0

if "healthy_scans" not in st.session_state:
    st.session_state.healthy_scans = 0

if "diseased_scans" not in st.session_state:
    st.session_state.diseased_scans = 0

if "current_image" not in st.session_state:
    st.session_state.current_image = None

if "current_image_hash" not in st.session_state:
    st.session_state.current_image_hash = None

if "processed_image_hash" not in st.session_state:
    st.session_state.processed_image_hash = None

if "current_predictions" not in st.session_state:
    st.session_state.current_predictions = None

if "active_sample_name" not in st.session_state:
    st.session_state.active_sample_name = None

if "model_initialized" not in st.session_state:
    st.session_state.model_initialized = False


# ==========================================
# SIDEBAR
# ==========================================
with st.sidebar:
    st.markdown("### 🌿 **CropCare AI**")
    st.markdown("<div style='font-size:0.85rem; color:#556B59; margin-bottom:16px;'>Plant Disease Identification & Diagnostic System</div>", unsafe_allow_html=True)
    st.divider()

    nav_choice = st.radio(
        "Navigation Menu",
        options=[
            "🩺 Plant Disease Diagnosis",
            "📊 Analytics Dashboard",
            "📖 Disease Knowledge Base",
            "ℹ️ Model & System Info"
        ],
        index=0
    )

    st.divider()

    # Sidebar Quick Live Stats
    st.markdown("#### 📈 **Session Activity**")
    sc1, sc2 = st.columns(2)
    with sc1:
        st.metric("Total Scans", st.session_state.total_scans)
    with sc2:
        st.metric("Diseases", st.session_state.diseased_scans)

    if st.session_state.total_scans > 0:
        health_pct = (st.session_state.healthy_scans / st.session_state.total_scans) * 100
        st.progress(health_pct / 100)
        st.caption(f"Healthy Crop Ratio: **{health_pct:.1f}%**")

    st.divider()

    # Model Status Indicator
    st.markdown("#### 🧠 **Model Engine**")
    st.markdown(f"<div style='font-size:0.8rem; color:#2E7D32;'><strong>ID:</strong> {MODEL_ID}</div>", unsafe_allow_html=True)
    st.markdown("<div style='font-size:0.8rem; color:#556B59;'><strong>Architecture:</strong> MobileNetV2 (38 Classes)</div>", unsafe_allow_html=True)
    st.markdown("<div style='font-size:0.8rem; color:#556B59; margin-top:4px;'><span style='color:#2E7D32;'>●</span> Cached In-Memory</div>", unsafe_allow_html=True)


# ==========================================
# TAB 1: PLANT DISEASE DIAGNOSIS
# ==========================================
if nav_choice == "🩺 Plant Disease Diagnosis":
    # Hero Banner
    st.markdown("""
    <div class="hero-banner">
        <div class="hero-title">🌱 CropCare AI - Intelligent Plant Disease Diagnostic</div>
        <div class="hero-subtitle">
            Upload clear leaf photographs to run real-time CNN feature extraction, obtain genuine confidence scores,
            and inspect actionable agronomic care guidelines and preventive treatments.
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Friendly loading indicator during initial neural network initialization
    if not st.session_state.model_initialized:
        with st.spinner("🌱 Initializing neural network weights and preprocessor... (This runs only once)"):
            model, processor, model_err = get_cached_model()
        if model is not None:
            st.session_state.model_initialized = True
    else:
        # Instant cache retrieval (~0.0ms)
        model, processor, model_err = get_cached_model()

    # Handle model download failures cleanly without repeated retries
    if model_err:
        st.error(f"⚠️ Model Initialization Error:\n\n{model_err}")
        st.info("The application interface is fully operational. To attempt reconnecting, use the button below:")
        if st.button("🔄 Retry Model Initialization"):
            reset_model_cache()
            get_cached_model.clear()
            st.session_state.model_initialized = False
            st.rerun()

    # Top Section: Input Selector (Upload vs. Demo Samples)
    input_col1, input_col2 = st.columns([3, 2])

    with input_col1:
        st.markdown("#### 📤 **1. Upload Plant Leaf Image**")
        uploaded_file = st.file_uploader(
            "Choose a plant leaf image (JPG, JPEG, PNG)",
            type=["jpg", "jpeg", "png"],
            help="For best diagnostic accuracy, use a well-lit photograph focusing on single leaves against a plain background."
        )

    with input_col2:
        st.markdown("#### 🧪 **Or Try Demonstration Samples**")
        st.caption("Click any sample leaf to immediately test without uploading files:")
        sample_dir = os.path.join(CURRENT_DIR, "samples")
        
        sample_c1, sample_c2 = st.columns(2)
        with sample_c1:
            if st.button("🍎 Apple (Healthy)", use_container_width=True):
                sample_path = os.path.join(sample_dir, "apple_healthy.jpg")
                if os.path.exists(sample_path):
                    loaded_img = Image.open(sample_path)
                    new_hash = compute_image_hash(loaded_img)
                    if new_hash != st.session_state.current_image_hash:
                        st.session_state.current_image = loaded_img
                        st.session_state.current_image_hash = new_hash
                        st.session_state.active_sample_name = "Sample: Healthy Apple Leaf"
                        st.session_state.current_predictions = None

            if st.button("🍅 Tomato (Early Blight)", use_container_width=True):
                sample_path = os.path.join(sample_dir, "tomato_early_blight.jpg")
                if os.path.exists(sample_path):
                    loaded_img = Image.open(sample_path)
                    new_hash = compute_image_hash(loaded_img)
                    if new_hash != st.session_state.current_image_hash:
                        st.session_state.current_image = loaded_img
                        st.session_state.current_image_hash = new_hash
                        st.session_state.active_sample_name = "Sample: Tomato Early Blight"
                        st.session_state.current_predictions = None

        with sample_c2:
            if st.button("🌽 Corn (Common Rust)", use_container_width=True):
                sample_path = os.path.join(sample_dir, "corn_common_rust.jpg")
                if os.path.exists(sample_path):
                    loaded_img = Image.open(sample_path)
                    new_hash = compute_image_hash(loaded_img)
                    if new_hash != st.session_state.current_image_hash:
                        st.session_state.current_image = loaded_img
                        st.session_state.current_image_hash = new_hash
                        st.session_state.active_sample_name = "Sample: Corn Common Rust"
                        st.session_state.current_predictions = None

            if st.button("🔄 Reset Image", use_container_width=True):
                st.session_state.current_image = None
                st.session_state.current_image_hash = None
                st.session_state.processed_image_hash = None
                st.session_state.active_sample_name = None
                st.session_state.current_predictions = None
                st.rerun()

    # Process Uploaded File with deduplication check
    if uploaded_file is not None:
        try:
            uploaded_img = Image.open(uploaded_file)
            up_hash = compute_image_hash(uploaded_img)
            if up_hash != st.session_state.current_image_hash:
                st.session_state.current_image = uploaded_img
                st.session_state.current_image_hash = up_hash
                st.session_state.active_sample_name = uploaded_file.name
                st.session_state.current_predictions = None
        except Exception as e:
            st.error(f"Error reading image: {e}")

    st.markdown("<br>", unsafe_allow_html=True)

    # Main Workflow: 2 Columns (Image Preview Left, Diagnostics Right)
    left_col, right_col = st.columns([1, 1], gap="large")

    with left_col:
        st.markdown("### 🖼️ **Leaf Image Preview**")
        if st.session_state.current_image is not None:
            img = st.session_state.current_image
            st.image(img, use_container_width=True, caption=st.session_state.active_sample_name or "Active Leaf Photograph")
            
            # Metadata badge
            st.markdown(
                f"<div style='font-size:0.85rem; color:#556B59; background:#F1F8E9; padding:8px 14px; border-radius:8px; border:1px solid #DCEDC8;'>"
                f"📏 <strong>Dimensions:</strong> {img.width} × {img.height} px &nbsp;|&nbsp; "
                f"🎨 <strong>Color Mode:</strong> {img.mode} &nbsp;|&nbsp; "
                f"🏷️ <strong>Source:</strong> {st.session_state.active_sample_name or 'Uploaded File'}"
                f"</div>",
                unsafe_allow_html=True
            )
            
            st.markdown("<br>", unsafe_allow_html=True)
            run_btn = st.button("⚡ Run Plant Disease Diagnosis", use_container_width=True, type="primary")
            
            if run_btn:
                if model is None or processor is None:
                    st.error("Model engine is currently not loaded. Cannot run inference.")
                else:
                    curr_hash = st.session_state.current_image_hash or compute_image_hash(img)

                    # Performance Optimization: Avoid unnecessary repeated image processing
                    if (
                        st.session_state.processed_image_hash == curr_hash 
                        and st.session_state.current_predictions is not None
                    ):
                        st.toast("⚡ Reused cached diagnostic results (image unchanged).", icon="🍃")
                    else:
                        with st.spinner("Running CNN inference and calculating genuine class probabilities..."):
                            preds = predict_image(img, model, processor, top_k=3, use_cache=True)
                            st.session_state.current_predictions = preds
                            st.session_state.processed_image_hash = curr_hash
                            
                            # Record in history
                            top1 = preds[0]
                            st.session_state.total_scans += 1
                            if top1["is_healthy"]:
                                st.session_state.healthy_scans += 1
                            else:
                                st.session_state.diseased_scans += 1

                            history_entry = {
                                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                                "display_name": top1["display_name"],
                                "plant": top1["plant"],
                                "condition": top1["condition"],
                                "probability": top1["probability"],
                                "percentage": top1["percentage"],
                                "status": "Healthy" if top1["is_healthy"] else "Diseased",
                                "is_healthy": top1["is_healthy"]
                            }
                            st.session_state.history.insert(0, history_entry)
                        st.rerun()

        else:
            st.info("👆 Please upload a plant leaf photograph or select one of the demonstration samples above to begin.")
            st.markdown("""
            <div style="border: 2px dashed #C8E6C9; border-radius: 12px; padding: 40px; text-align: center; color: #556B59;">
                <div style="font-size: 3rem; margin-bottom: 10px;">🍃</div>
                <strong>Awaiting Leaf Image Input</strong><br>
                Supported Formats: JPG, JPEG, PNG
            </div>
            """, unsafe_allow_html=True)

    with right_col:
        st.markdown("### 📋 **Diagnostic Results & Prognosis**")
        
        if st.session_state.current_predictions is not None:
            predictions = st.session_state.current_predictions
            top_pred = predictions[0]
            # Use cached disease info lookup
            d_info = get_cached_disease_info(top_pred["class_name"])
            
            # Status Badge and Banner
            is_healthy = top_pred["is_healthy"]
            banner_class = "result-banner-healthy" if is_healthy else "result-banner-diseased"
            status_badge = (
                '<span class="badge-healthy">🌿 Healthy Foliage</span>' 
                if is_healthy else 
                '<span class="badge-diseased">⚠️ Disease Detected</span>'
            )

            st.markdown(f"""
            <div class="result-banner {banner_class}">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                    {status_badge}
                    <span style="font-size: 1.3rem; font-weight: 800; color: #1B5E20;">{top_pred['percentage']}</span>
                </div>
                <div style="font-size: 1.45rem; font-weight: 800; color: #1B5E20; margin-bottom: 4px;">
                    {top_pred['display_name']}
                </div>
                <div style="font-size: 0.9rem; color: #37474F;">
                    <strong>Host Crop:</strong> {top_pred['plant']} &nbsp;|&nbsp; 
                    <strong>Pathogen:</strong> {d_info.get('pathogen_type', 'N/A')} &nbsp;|&nbsp;
                    <strong>Severity:</strong> {d_info.get('severity', 'N/A')}
                </div>
            </div>
            """, unsafe_allow_html=True)

            # Top 3 Predicted Classes Breakdown
            st.markdown("#### 🎯 **Top 3 Predicted Classes (Model Confidence)**")
            
            for p in predictions:
                prob_val = p["probability"]
                st.markdown(f"""
                <div style="display: flex; justify-content: space-between; align-items: baseline; font-size: 0.95rem; font-weight: 600; margin-top: 6px;">
                    <div>
                        <span class="badge-rank">{p['rank']}</span> &nbsp;
                        <strong>{p['display_name']}</strong>
                    </div>
                    <span style="color: #2E7D32; font-weight: 700;">{p['percentage']}</span>
                </div>
                """, unsafe_allow_html=True)
                st.progress(min(max(prob_val, 0.0), 1.0))

            st.divider()

            # Agronomic Action Plan & Disease Details
            st.markdown("#### 🌿 **Agronomic Treatment & Care Recommendations**")
            
            tab_sym, tab_treat, tab_prev = st.tabs(["🔍 Symptoms & Causes", "💊 Treatment Plan", "🛡️ Prevention"])

            with tab_sym:
                st.markdown("**Identified Symptoms:**")
                st.write(d_info.get("symptoms", "No specific symptoms recorded."))
                st.markdown("**Favorable Environmental Triggers:**")
                st.info(d_info.get("favorable_conditions", "Variable conditions."))

            with tab_treat:
                st.markdown("**Actionable Curative & Cultural Measures:**")
                treatments = d_info.get("treatment", [])
                if treatments:
                    for idx, step in enumerate(treatments, start=1):
                        st.markdown(f"**{idx}.** {step}")
                else:
                    st.write("No chemical treatment necessary for healthy specimens.")

            with tab_prev:
                st.markdown("**Best Agricultural Prevention Practices:**")
                preventions = d_info.get("prevention", [])
                if preventions:
                    for idx, prev in enumerate(preventions, start=1):
                        st.markdown(f"• {prev}")
                else:
                    st.write("Maintain standard balanced crop care.")

            # Download Diagnosis Summary
            st.divider()
            summary_text = (
                f"CROPCARE AI - DIAGNOSTIC REPORT\n"
                f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
                f"Target Image: {st.session_state.active_sample_name or 'Uploaded File'}\n"
                f"Primary Diagnosis: {top_pred['display_name']}\n"
                f"Confidence: {top_pred['percentage']}\n"
                f"Status: {'Healthy' if top_pred['is_healthy'] else 'Diseased'}\n"
                f"Pathogen: {d_info.get('pathogen_type', 'N/A')}\n"
                f"Severity: {d_info.get('severity', 'N/A')}\n\n"
                f"SYMPTOMS:\n{d_info.get('symptoms', '')}\n\n"
                f"RECOMMENDED TREATMENTS:\n" +
                "\n".join([f"- {t}" for t in d_info.get('treatment', [])]) + "\n\n"
                f"PREVENTION MEASURES:\n" +
                "\n".join([f"- {p}" for p in d_info.get('prevention', [])])
            )
            
            st.download_button(
                label="📄 Download Diagnostic Agronomy Slip",
                data=summary_text,
                file_name=f"CropCare_Report_{top_pred['plant']}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                mime="text/plain",
                use_container_width=True
            )

        else:
            st.markdown("""
            <div style="border: 1px dashed #CFD8DC; border-radius: 12px; padding: 48px 24px; text-align: center; color: #78909C;">
                <div style="font-size: 2.5rem; margin-bottom: 8px;">🔬</div>
                <div style="font-size: 1.1rem; font-weight: 700; color: #455A64;">Ready for Analysis</div>
                <p style="font-size: 0.9rem; margin-top: 6px;">
                    Select or upload an image on the left, then click <strong>"Run Plant Disease Diagnosis"</strong> to see predictions, confidence scores, and crop care suggestions.
                </p>
            </div>
            """, unsafe_allow_html=True)


# ==========================================
# TAB 2: ANALYTICS DASHBOARD
# ==========================================
elif nav_choice == "📊 Analytics Dashboard":
    st.markdown("""
    <div class="hero-banner">
        <div class="hero-title">📊 Crop Diagnostics Analytics & Prediction History</div>
        <div class="hero-subtitle">
            Review session metrics, monitor healthy versus diseased crop distributions, and trace past diagnostic queries.
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Top KPI Metrics Cards
    m1, m2, m3, m4 = st.columns(4)
    with m1:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">Total Diagnoses</div>
            <div class="metric-value">{st.session_state.total_scans}</div>
            <div class="metric-subtext">Total scans completed</div>
        </div>
        """, unsafe_allow_html=True)

    with m2:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">Healthy Detected</div>
            <div class="metric-value" style="color: #2E7D32;">{st.session_state.healthy_scans}</div>
            <div class="metric-subtext">Foliage free of pathology</div>
        </div>
        """, unsafe_allow_html=True)

    with m3:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">Disease Cases</div>
            <div class="metric-value" style="color: #C62828;">{st.session_state.diseased_scans}</div>
            <div class="metric-subtext">Requiring treatment action</div>
        </div>
        """, unsafe_allow_html=True)

    with m4:
        avg_conf = 0.0
        if st.session_state.history:
            avg_conf = sum(h["probability"] for h in st.session_state.history) / len(st.session_state.history) * 100
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">Average Confidence</div>
            <div class="metric-value" style="color: #1565C0;">{avg_conf:.1f}%</div>
            <div class="metric-subtext">Mean top-1 probability</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Prediction History Table
    st.markdown("### 🕒 **Recent Prediction History**")
    
    if st.session_state.history:
        h_col1, h_col2 = st.columns([4, 1])
        with h_col2:
            if st.button("🗑️ Clear History", use_container_width=True):
                st.session_state.history = []
                st.session_state.total_scans = 0
                st.session_state.healthy_scans = 0
                st.session_state.diseased_scans = 0
                st.rerun()

        df_history = pd.DataFrame(st.session_state.history)
        display_df = df_history[["timestamp", "plant", "condition", "status", "percentage"]].copy()
        display_df.columns = ["Timestamp", "Crop", "Diagnosis", "Health Status", "Confidence"]

        st.dataframe(
            display_df,
            use_container_width=True,
            hide_index=True
        )

        st.markdown("<br>", unsafe_allow_html=True)
        # Visual Distribution
        st.markdown("#### 📉 **Pathology Distribution**")
        d_col1, d_col2 = st.columns(2)
        with d_col1:
            st.markdown(f"**Healthy Crops:** {st.session_state.healthy_scans}")
            if st.session_state.total_scans > 0:
                st.progress(st.session_state.healthy_scans / st.session_state.total_scans)
        with d_col2:
            st.markdown(f"**Diseased Crops:** {st.session_state.diseased_scans}")
            if st.session_state.total_scans > 0:
                st.progress(st.session_state.diseased_scans / st.session_state.total_scans)

    else:
        st.info("No prediction history recorded yet. Perform diagnoses in the 'Plant Disease Diagnosis' tab to view records.")


# ==========================================
# TAB 3: DISEASE KNOWLEDGE BASE
# ==========================================
elif nav_choice == "📖 Disease Knowledge Base":
    st.markdown("""
    <div class="hero-banner">
        <div class="hero-title">📖 Comprehensive Plant Disease Knowledge Base</div>
        <div class="hero-subtitle">
            Explore 38 plant health conditions covered by the MobileNetV2 architecture, including symptoms,
            favorable microclimates, and organic and chemical treatment methods.
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Use cached crop list and disease database
    crops = get_cached_crops()
    all_diseases = get_cached_all_diseases()

    # Filter controls
    f1, f2 = st.columns([1, 2])
    with f1:
        selected_plant = st.selectbox("Filter by Host Plant:", ["All Plants"] + crops)
    with f2:
        search_query = st.text_input("Search Symptoms or Condition:", placeholder="e.g. Blight, Rust, Mildew, Spot...")

    # Filter database
    filtered_db = {}
    for k, v in all_diseases.items():
        if selected_plant != "All Plants" and v["plant"] != selected_plant:
            continue
        if search_query:
            query = search_query.lower()
            text_pool = f"{v['display_name']} {v['symptoms']} {v['pathogen_type']}".lower()
            if query not in text_pool:
                continue
        filtered_db[k] = v

    st.markdown(f"**Showing {len(filtered_db)} of {len(all_diseases)} agricultural disease profiles:**")
    st.divider()

    # Display Cards
    for k, info in filtered_db.items():
        with st.expander(f"{info['display_name']} — {info['status']}"):
            col_a, col_b = st.columns([1, 1])
            with col_a:
                st.markdown(f"**Pathogen:** `{info['pathogen_type']}`")
                st.markdown(f"**Severity Level:** `{info['severity']}`")
                st.markdown(f"**Favorable Environment:** {info['favorable_conditions']}")
                st.markdown("**Key Symptoms:**")
                st.write(info['symptoms'])
            with col_b:
                st.markdown("**Recommended Treatment:**")
                for t in info.get("treatment", []):
                    st.markdown(f"• {t}")
                st.markdown("**Prevention:**")
                for p in info.get("prevention", []):
                    st.markdown(f"• {p}")


# ==========================================
# TAB 4: MODEL & SYSTEM INFO
# ==========================================
elif nav_choice == "ℹ️ Model & System Info":
    st.markdown("""
    <div class="hero-banner">
        <div class="hero-title">ℹ️ Technical Architecture & System Specifications</div>
        <div class="hero-subtitle">
            Overview of the convolutional neural network backbone, inference pipeline, and operational guidelines.
        </div>
    </div>
    """, unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    with c1:
        st.markdown("""
        ### 🧠 **Deep Learning Architecture**
        - **Model Repository:** `neghani/plantvillage-mobilenetv2`
        - **Model Backbone:** MobileNetV2 with Inverted Residual Blocks
        - **Parameter Count:** ~3.4 Million Parameters (High efficiency for edge & web)
        - **Dataset:** PlantVillage (54,305 curated agricultural leaf images)
        - **Classes Covered:** 38 Classes spanning 14 crop species
        - **Input Resolution:** 224 × 224 RGB tensors
        - **Normalization Mean:** `[0.5, 0.5, 0.5]`, **Std:** `[0.5, 0.5, 0.5]`
        """)

    with c2:
        st.markdown("""
        ### 🔄 **Optimized Pipeline & Caching**
        1. **Resource Caching:** `@st.cache_resource` keeps neural network weights in-memory across the session.
        2. **Image Deduplication:** MD5 hash verification skips redundant CNN forward passes on identical images.
        3. **Data Caching:** Static disease records and agronomy guidelines are cached via `@st.cache_data`.
        4. **Fail-Fast Error Handling:** Network download failures do not repeatedly trigger failed download loops.
        5. **Genuine Probabilities:** Softmax distributions compute genuine confidence ratings.
        """)

    st.divider()

    st.markdown("### 🌿 **Supported Crop Types**")
    crops_supported = [
        "Apple (Malus domestica)", "Blueberry (Vaccinium corymbosum)", "Cherry (Prunus avium)",
        "Corn / Maize (Zea mays)", "Grape (Vitis vinifera)", "Orange / Citrus (Citrus sinensis)",
        "Peach (Prunus persica)", "Bell Pepper (Capsicum annuum)", "Potato (Solanum tuberosum)",
        "Raspberry (Rubus idaeus)", "Soybean (Glycine max)", "Squash (Cucurbita pepo)",
        "Strawberry (Fragaria × ananassa)", "Tomato (Solanum lycopersicum)"
    ]
    
    col_c1, col_c2 = st.columns(2)
    for i, crop in enumerate(crops_supported):
        target_col = col_c1 if i % 2 == 0 else col_c2
        target_col.markdown(f"✓ **{crop}**")
