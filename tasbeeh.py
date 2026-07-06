import streamlit as st
import base64

# إعدادات الصفحة - وضع الشاشة الكاملة
st.set_page_config(page_title="السبحة الإلكترونية", page_icon="📿", layout="wide", initial_sidebar_state="collapsed")

# الذاكرة لحفظ العداد
if 'tasbeeh_count' not in st.session_state:
    st.session_state.tasbeeh_count = 0

# دالة لتحويل الصورة المرفوعة إلى خلفية
def add_bg_from_upload(uploaded_file):
    if uploaded_file is not None:
        base64_img = base64.b64encode(uploaded_file.getvalue()).decode()
        bg_css = f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{base64_img}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        </style>
        """
        st.markdown(bg_css, unsafe_allow_html=True)

# تصميم الواجهة وإلغاء الهوامش
st.markdown("""
    <style>
    /* إخفاء الهوامش بالكامل لملء الشاشة */
    .appview-container .main .block-container {
        padding-top: 50px !important; /* مسافة للـ Dynamic Island بالآيفون */
        padding-bottom: 0px !important;
        padding-left: 10px !important;
        padding-right: 10px !important;
        max-width: 100%;
        background-color: transparent !important; /* إزالة اللون الأبيض نهائياً لبروز الخلفية */
    }
    
    header {display: none !important;} /* إخفاء الشريط العلوي */
    footer {display: none !important;} /* إخفاء الشريط السفلي */
    
    /* نصوص بخلفية ظل سوداء حتى تنقرئ على أي صورة واضحة */
    .title-font { font-size: 35px !important; font-weight: bold; text-align: center; color: white; text-shadow: 2px 2px 8px #000000; margin-bottom: 10px;}
    .number-display { font-size: 130px; font-weight: bold; color: white; text-align: center; text-shadow: 3px 3px 12px #000000; margin: 10px 0px;}
    
    /* زر التسبيح (يمين، لون سمائي) */
    div[data-testid="stHorizontalBlock"]:nth-of-type(1) div[data-testid="column"]:nth-of-type(2) div.stButton > button {
        height: 320px; /* دگمة عملاقة ومريحة */
        width: 100%;
        font-size: 70px !important;
        font-weight: bold;
        border-radius: 40px;
        background: linear-gradient(135deg, #00c6ff, #0072ff); /* سمائي وأزرق */
        color: white;
        border: 4px solid rgba(255,255,255,0.5);
        box-shadow: 0px 10px 20px rgba(0, 0, 0, 0.6);
        transition: all 0.1s ease-in-out;
    }
    div[data-testid="stHorizontalBlock"]:nth-of-type(1) div[data-testid="column"]:nth-of-type(2) div.stButton > button:active {
        transform: scale(0.95);
        background: linear-gradient(135deg, #0072ff, #00c6ff);
    }
    
    /* تخصيص زر التصفير (يسار) */
    div[data-testid="stHorizontalBlock"]:nth-of-type(2) div[data-testid="column"]:nth-of-type(1) div.stButton > button {
        height: 50px;
        font-size: 20px !important;
        background: rgba(231, 76, 60, 0.9);
        color: white;
        border: 2px solid white;
        border-radius: 15px;
        box-shadow: 0px 5px 10px rgba(0, 0, 0, 0.5);
    }

    /* تقليل وضوح مكان رفع الصورة (إخفاءه بأسفل الشاشة) */
    div[data-testid="stExpander"] {
        background-color: rgba(0, 0, 0, 0.1) !important;
        border: none !important;
        margin-top: 40px;
    }
    div[data-testid="stExpander"] * {
        color: rgba(255, 255, 255, 0.5) !important;
    }
    
    /* شفافية قائمة اختيار الذكر */
    .stSelectbox > div > div {
        background-color: rgba(0, 0, 0, 0.4) !important;
        color: white !important;
        border: none !important;
    }
    </style>
    """, unsafe_allow_html=True)

# العنوان
st.markdown('<p class="title-font">📿 السبحة الإلكترونية</p>', unsafe_allow_html=True)

# قائمة اختيار الذكر شفافة
zikr_option = st.selectbox("", ["سبحان الله", "الحمد لله", "لا إله إلا الله", "الله أكبر", "أستغفر الله", "اللهم صل على محمد وآل محمد"], label_visibility="collapsed")

# عرض العداد بخط عملاق
st.markdown(f'<div class="number-display">{st.session_state.tasbeeh_count}</div>', unsafe_allow_html=True)

# صف الأزرار الأول: مساحة فارغة باليسار (1) والدگمة الجبيرة باليمين (3)
col_left, col_right = st.columns([1, 3])
with col_right:
    if st.button("سبّح", key="main_btn"):
        st.session_state.tasbeeh_count += 1
        st.rerun()

st.write("")

# صف الأزرار الثاني: زر التصفير صغير على جهة اليسار حتى ما ينضغط بالغلط
col_reset, col_empty = st.columns([1, 3])
with col_reset:
    if st.button("🔄 تصفير", key="reset_btn"):
        st.session_state.tasbeeh_count = 0
        st.rerun()

# خيار رفع الصورة مخفي بأسفل الشاشة
with st.expander("⚙️ إضافة خلفية"):
    bg_img = st.file_uploader("اختر صورة من تلفونك:", type=['png', 'jpg', 'jpeg'])
add_bg_from_upload(bg_img)
