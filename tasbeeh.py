import streamlit as st
import base64

# إعدادات الصفحة
st.set_page_config(page_title="السبحة الإلكترونية", page_icon="📿", layout="wide", initial_sidebar_state="collapsed")

# حفظ العداد
if 'tasbeeh_count' not in st.session_state:
    st.session_state.tasbeeh_count = 0

# حفظ الخلفية
if 'bg_image' not in st.session_state:
    st.session_state.bg_image = None

def apply_bg():
    if st.session_state.bg_image:
        bg_css = f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{st.session_state.bg_image}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        </style>
        """
        st.markdown(bg_css, unsafe_allow_html=True)

# CSS لضبط التصميم وتثبيت الأزرار
st.markdown("""
    <style>
    /* إخفاء الهوامش */
    .appview-container .main .block-container {
        padding-top: 40px !important;
        padding-bottom: 0px !important;
        background-color: transparent !important;
    }
    header {display: none !important;}
    
    .title-font { font-size: 35px !important; font-weight: bold; text-align: center; color: white; text-shadow: 2px 2px 8px #000000; margin-bottom: 10px;}
    .number-display { font-size: 140px; font-weight: bold; color: white; text-align: center; text-shadow: 3px 3px 12px #000000; margin-top: 20px;}
    
    /* تثبيت زر التسبيح في أسفل اليمين بشكل إجباري */
    button[kind="primary"] {
        position: fixed !important;
        bottom: 40px !important;
        right: 20px !important;
        width: 65vw !important; /* يأخذ 65% من عرض الشاشة */
        height: 250px !important;
        font-size: 60px !important;
        font-weight: bold !important;
        border-radius: 35px !important;
        background: linear-gradient(135deg, #00c6ff, #0072ff) !important;
        color: white !important;
        border: 4px solid rgba(255,255,255,0.4) !important;
        box-shadow: 0px 10px 20px rgba(0, 0, 0, 0.6) !important;
        z-index: 1000 !important;
    }
    button[kind="primary"]:active {
        transform: scale(0.95) !important;
    }
    
    /* تثبيت زر التصفير في أسفل اليسار */
    button[kind="secondary"] {
        position: fixed !important;
        bottom: 40px !important;
        left: 20px !important;
        width: 25vw !important;
        height: 60px !important;
        font-size: 20px !important;
        background: rgba(231, 76, 60, 0.8) !important;
        color: white !important;
        border: 2px solid white !important;
        border-radius: 15px !important;
        z-index: 1000 !important;
    }

    /* شفافية وترتيب باقي العناصر */
    div[data-testid="stExpander"] {
        background-color: rgba(0, 0, 0, 0.3) !important;
        border: none !important;
        position: relative;
        z-index: 500;
    }
    div[data-testid="stExpander"] * { color: white !important; }
    
    .stSelectbox {
        position: relative;
        z-index: 500;
    }
    .stSelectbox > div > div {
        background-color: rgba(0, 0, 0, 0.5) !important;
        color: white !important;
        border: none !important;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<p class="title-font">📿 السبحة الإلكترونية</p>', unsafe_allow_html=True)
zikr_option = st.selectbox("", ["سبحان الله", "الحمد لله", "لا إله إلا الله", "الله أكبر", "أستغفر الله", "اللهم صل على محمد وآل محمد"], label_visibility="collapsed")
st.markdown(f'<div class="number-display">{st.session_state.tasbeeh_count}</div>', unsafe_allow_html=True)

# أزرار بدون ترتيب أعمدة (سيتم وضعها حسب إحداثيات الـ CSS أعلاه)
if st.button("سبّح", type="primary"):
    st.session_state.tasbeeh_count += 1
    st.rerun()

if st.button("تصفير", type="secondary"):
    st.session_state.tasbeeh_count = 0
    st.rerun()

# الإعدادات لرفع الصورة
with st.expander("⚙️ لتغيير الصورة الخلفية اضغط هنا"):
    uploaded_file = st.file_uploader("اختر صورة من تلفونك:", type=['png', 'jpg', 'jpeg'])
    if uploaded_file is not None:
        st.session_state.bg_image = base64.b64encode(uploaded_file.getvalue()).decode()
        st.rerun()

apply_bg()
