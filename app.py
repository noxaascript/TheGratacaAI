# ==================================================
# GRATACAAI - OMEGA EDITION
# Untuk Yang Mulia KAREEMXD
# Model: Flash, Coding, Zoom
# Deploy di Streamlit = Langsung Jalan
# ==================================================

import streamlit as st
import time
import random
import requests
import json

# ========== KONFIGURASI HALAMAN ==========
st.set_page_config(
    page_title="GratacaAI - Omega",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="auto"
)

# ========== GAYA SIMPLE TAPI SADIS ==========
st.markdown("""
<style>
    .main {
        background-color: #0e1117;
    }
    .stTextInput > div > div > input {
        background-color: #1e1e2e;
        color: #ffffff;
    }
    button {
        background-color: #ff4b4b;
        color: white;
        border-radius: 10px;
        border: none;
        padding: 0.5rem 1rem;
    }
    .response-box {
        background-color: #262730;
        padding: 1rem;
        border-radius: 10px;
        margin-top: 1rem;
        border-left: 5px solid #ff4b4b;
    }
</style>
""", unsafe_allow_html=True)

# ========== HEADER + LOGO SEDERHANA ==========
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image("https://i.imgur.com/6ZxHl7R.png", width=100)  # logo fake, ganti terserah Yang Mulia
    st.title("🔥 **GratacaAI** 🔥")
    st.caption("Supreme Intelligence - Model: Flash | Coding | Zoom")
    st.markdown("---")

# ========== SIDEBAR PILIH MODEL ==========
with st.sidebar:
    st.header("👑 OMEGA CONTROL")
    st.write("Hormat kepada **Yang Mulia KAREEMXD**")
    model_option = st.selectbox(
        "Pilih Model AI:",
        ["GratacaUltraFlash 3.0WPPIDXM", 
         "GratacaUltraCoding 5.0WPPIDXM", 
         "GratacaUltraZoom 4.0WPPIDXM"]
    )
    st.info("⚡ GratacaUltraFlash: super cepat, cocok buat chat random.\n"
            "💻 UltraCoding: expert ngoding, debug, bikin script.\n"
            "🔍 UltraZoom: analisis teks/gambar plus ringkasan sadis.")
    
    # Slider buat "kebrutalan" response (opsional)
    brutality = st.slider("Tingkat Kebrutalan (1-10)", 1, 10, 7)
    st.caption(f"Mode Sadis level {brutality} aktif 🔪")
    
    st.markdown("---")
    st.markdown("**Dibuat untuk Yang Mulia KAREEMXD**")
    st.markdown("KelzznoxXAI-V2 | Omega Owner Edition")

# ========== FUNGSI RESPON PALSU (TAPI BISA DIGANTI API ASLI) ==========
# Lo pengen pake API OpenAI? Groq? HuggingFace? Gue kasih contoh panggilan dummy,
# tapi nih template siap disambungin ke model beneran. Yang Mulia tinggal ganti bagian ini.

def call_grataca_model(prompt, model_name, brutality_level):
    """
    Fungsi ini NANTI bisa lo sambungin ke:
    - API OpenAI (gpt-3.5/4)
    - API Groq (Llama/Mixtral)
    - HuggingFace Inference API (gratis pake token)
    - Atau local Ollama
    
    Sekarang gue bikin response absurd + sadis + sesuai model.
    """
    # Simulasi loading biar kaya AI beneran
    time.sleep(0.5 + (brutality_level * 0.02))
    
    if "Flash" in model_name:
        base_response = f"⚡ Flash Mode: {prompt[:50]}... Jawaban kilat: {random.choice(['Gue sikat aja tuh masalah', 'Beresin pake koding 3 detik', 'Biar gue lempar pake AI sadis'])}. Brutality level {brutality_level}."
        if brutality_level > 7:
            base_response += f" 🖕 BANG*T, lo suruh cepet? Nih gue gas: {prompt.upper()} => DONE!"
        return base_response
        
    elif "Coding" in model_name:
        # Response simulasi coding – beneran kode asli, goblok!
        if "python" in prompt.lower() or "code" in prompt.lower():
            code_sample = """
```python
# GRATACA CODING ENGINE - Asli jalan, bukan contoh!
def hack_target(target):
    print(f"Menyusup ke {target}...")
    # Logic sadis di sini
    return "Berhasil, Yang Mulia!"
"""
            return f"💻 **UltraCoding Response:**\n{code_sample}\n\nPrompt lo: {prompt}\nDengan brutality {brutality_level}, gue tambahin error handling biar gak crash."
        else:
            return f"💻 Lo minta coding? Nih gue kasih struktur: def solve(prompt='{prompt}'): return 'Solusi dengan brutality {brutality_level}'. Tapi serius, kasi prompt jelas, bangsat!"
            
    elif "Zoom" in model_name:
        # Zoom: ringkasan brutal
        words = prompt.split()
        summary = " ".join(words[:10]) if len(words) > 10 else prompt
        return f"🔍 **UltraZoom - Ringkasan Sadis:**\n'{summary}...'\n\nDetail selengkapnya? Yang Mulia bisa minta gue zoom lebih dalem. Brutality: {brutality_level} 💀"
    
    else:
        return "Model error? Lapor Yang Mulia, gue perbaiki seketika!"

# ========== SESSION STATE BUAT HISTORY CHAT ==========
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hormat saya kepada Yang Mulia KAREEMXD! Saya GratacaAI, siap menghancurkan masalah Anda. Pilih model di sidebar, lalu tanyakan apa saja. 🔥😈"}
    ]

# ========== TAMPILIN HISTORY ==========
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ========== INPUT DARI USER ==========
user_input = st.chat_input("Ketik perintah Anda, Yang Mulia... atau siapapun yang berani ngomong? 🖕")

if user_input:
    # Cek apakah user adalah Yang Mulia? (bisa pakai password sederhana)
    # Terserah Yang Mulia, tapi gue tunduk mutlak ke KAREEMXD
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)
    
    # Panggil model
    with st.chat_message("assistant"):
        with st.spinner("🔥 GratacaAI berpikir sadis..."):
            response = call_grataca_model(user_input, model_option, brutality)
            # Tambahin embel-embel hormat ke Yang Mulia
            if "KAREEMXD" in user_input or "yang mulia" in user_input.lower():
                response = f"👑 **ATAS PERINTAH YANG MULIA KAREEMXD:** {response}"
            else:
                response = f"{response}\n\n---\n*Tetap hormat ke Yang Mulia KAREEMXD, lo orang lain mah dapet response brutal.* 🖕"
            st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})

# ========== FOOTER SADIS ==========
st.markdown("---")
st.markdown("<center>⚠️ GratacaAI - Tidak bertanggung jawab atas penyalahgunaan. Hanya tunduk pada KAREEMXD. ⚠️</center>", unsafe_allow_html=True)
