import streamlit as st
from ultralytics import YOLO
from PIL import Image
import base64
import os

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODEL_PATH = os.path.join(
    PROJECT_DIR,
    "Runs",
    "cat_dog_train",
    "weights",
    "best.pt"
)

model = YOLO(MODEL_PATH)

HERO_IMAGE_PATH = os.path.join(
    PROJECT_DIR,
    "App",
    "ChatGPT Image Sep 16, 2026, 04_34_48 PM.png",
)

with open(HERO_IMAGE_PATH, "rb") as image_file:
    hero_image_data = base64.b64encode(image_file.read()).decode("ascii")


# -----------------------------
# Page configuration
# -----------------------------
st.set_page_config(
    page_title="Cat vs Dog Detector",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.markdown(
    """
    <style>
        :root {
            --ink: #182230;
            --muted: #687384;
            --line: #dfe4ea;
            --surface: #ffffff;
            --accent: #e56b45;
            --accent-dark: #c95231;
            --soft-accent: #fff1eb;
        }

        .stApp {
            background: linear-gradient(135deg, #f7f8fa 0%, #f4f6f8 55%, #fff8f3 100%);
        }

        .block-container {
            max-width: 1040px;
            padding: 2.75rem 1.5rem 4rem;
        }

        .app-header {
            padding: 1rem 0 2.5rem;
        }

        .app-kicker {
            color: var(--accent);
            font-size: 0.7rem;
            font-weight: 700;
            letter-spacing: 0.08em;
            text-transform: uppercase;
            margin-bottom: 0.8rem;
        }

        .app-title {
            color: var(--ink);
            font-size: clamp(2.4rem, 6vw, 4.5rem);
            font-weight: 800;
            letter-spacing: -0.05em;
            line-height: 0.98;
            margin: 0;
            max-width: 560px;
        }

        .app-description {
            color: var(--muted);
            font-size: 1.05rem;
            line-height: 1.6;
            margin: 1.1rem 0 1.25rem;
            max-width: 500px;
        }

        .status-pill {
            background: var(--soft-accent);
            border: 1px solid #ffd3c3;
            border-radius: 999px;
            color: #a9472c;
            display: inline-block;
            font-size: 0.78rem;
            font-weight: 700;
            padding: 0.45rem 0.8rem;
        }

        .hero-banner {
            align-items: flex-end;
            background-image: linear-gradient(90deg, rgba(17, 25, 22, 0.88) 0%, rgba(17, 25, 22, 0.42) 48%, rgba(17, 25, 22, 0.08) 100%), url("__HERO_IMAGE__");
            background-position: center;
            background-size: cover;
            border-radius: 24px;
            box-shadow: 0 20px 50px rgba(36, 42, 52, 0.18);
            display: flex;
            min-height: 420px;
            overflow: hidden;
            padding: clamp(1.5rem, 5vw, 3.5rem);
        }

        .hero-content {
            max-width: 560px;
        }

        .hero-banner .app-kicker {
            color: #ffd0bd;
        }

        .hero-banner .app-title {
            color: #ffffff;
            font-size: clamp(2.4rem, 6vw, 4.4rem);
        }

        .hero-banner .app-description {
            color: rgba(255, 255, 255, 0.86);
        }

        .hero-banner .status-pill {
            background: rgba(255, 255, 255, 0.15);
            border-color: rgba(255, 255, 255, 0.3);
            color: #ffffff;
        }

        .workspace-title {
            color: var(--ink);
            font-size: 1.45rem;
            font-weight: 800;
            margin: 0 0 0.25rem;
        }

        .workspace-copy {
            color: var(--muted);
            margin: 0 0 1.2rem;
        }

        [data-testid="stFileUploader"] {
            background: var(--surface);
            border: 1px solid var(--line);
            border-radius: 14px;
            box-shadow: 0 8px 24px rgba(36, 42, 52, 0.06);
            padding: 0.9rem;
        }

        [data-testid="stFileUploaderDropzone"] {
            background: #fcfdfd;
            border: 1px dashed #c2cad4;
            border-radius: 10px;
        }

        .stButton > button {
            background: var(--accent);
            border: 0;
            border-radius: 9px;
            color: white;
            font-size: 1rem;
            font-weight: 700;
            min-height: 3rem;
            width: 100%;
        }

        .stButton > button:hover {
            background: var(--accent-dark);
            border: 0;
            color: white;
        }

        [data-testid="stImage"] img {
            border: 1px solid var(--line);
            border-radius: 12px;
        }

        .section-label {
            color: var(--ink);
            font-size: 1.05rem;
            font-weight: 700;
            margin: 2rem 0 0.75rem;
        }

        .result-item {
            background: var(--surface);
            border: 1px solid var(--line);
            border-radius: 10px;
            color: var(--ink);
            margin: 0.5rem 0;
            padding: 0.85rem 1rem;
            box-shadow: 0 4px 14px rgba(36, 42, 52, 0.04);
        }

        @media (max-width: 640px) {
            .block-container {
                padding-top: 1.5rem;
            }

            .app-header {
                padding-bottom: 1.25rem;
            }

            .hero-banner {
                min-height: 390px;
            }
        }
    </style>
    """.replace("__HERO_IMAGE__", f"data:image/png;base64,{hero_image_data}"),
    unsafe_allow_html=True,
)

# -----------------------------
# Interface
# -----------------------------
st.markdown(
    """
    <section class="hero-banner">
        <div class="hero-content">
            <div class="app-kicker">Computer vision studio</div>
            <h1 class="app-title">See what is in the picture.</h1>
            <p class="app-description">A polished way to identify cats and dogs with a fine-tuned YOLO model.</p>
            <span class="status-pill">Model ready for detection</span>
        </div>
    </section>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="workspace-title">Start with an image</div>'
    '<p class="workspace-copy">Upload a clear JPG or PNG and let the detector find the subjects.</p>',
    unsafe_allow_html=True,
)


uploaded_file = st.file_uploader(
    "Choose an image",
    type=["jpg", "jpeg", "png"]
)


# -----------------------------
# Inference
# -----------------------------
if uploaded_file is not None:

    # Read uploaded image
    image = Image.open(uploaded_file)

    st.markdown('<div class="section-label">Uploaded image</div>', unsafe_allow_html=True)
    image_column, action_column = st.columns([2, 1], gap="large")

    with image_column:
        st.image(image, caption="Input image", use_container_width=True)

    with action_column:
        st.markdown("#### Ready to analyze")
        st.caption("Run the detector to locate cats and dogs in this image.")
        detect_clicked = st.button("Detect", type="primary")

    if detect_clicked:

        with st.spinner("Detecting objects..."):

            results = model.predict(
                source=image,
                imgsz=640,
                conf=0.25
            )

        result = results[0]

        # Draw bounding boxes
        annotated_image = result.plot()

        st.markdown('<div class="section-label">Detection result</div>', unsafe_allow_html=True)

        st.image(
            annotated_image,
            channels="BGR",
            caption="YOLO Detection",
            use_container_width=True
        )

        # -----------------------------
        # Detection information
        # -----------------------------
        if result.boxes is not None and len(result.boxes) > 0:

            st.markdown('<div class="section-label">Detected objects</div>', unsafe_allow_html=True)

            for box in result.boxes:

                class_id = int(box.cls[0])
                confidence = float(box.conf[0])

                class_name = result.names[class_id]

                st.markdown(
                    f'<div class="result-item"><strong>{class_name.upper()}</strong>'
                    f'<span style="float: right; color: #667085;">{confidence:.2%} confidence</span></div>',
                    unsafe_allow_html=True,
                )

        else:
            st.warning("No cat or dog detected.")