import streamlit as st
import base64

# إعدادات الصفحة
st.set_page_config(page_title="السبحة الإلكترونية", page_icon="📿", layout="wide", initial_sidebar_state="collapsed")

# 1. حفظ العداد في الذاكرة
if 'tasbeeh_count' not in st.session_state:
    st.session_state.tasbeeh_count = 0

# 2. حفظ الخلفية في الذاكرة حتى ما تختفي أبداً
if 'bg_image' not in st.session_state:
    st.session_state.bg_image = None

# دالة تطبيق الخلفية
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

# تصميم الواجهة والألوان
st.markdown("""
    <style>
    /* إخفاء الهوامش */
    .appview-container .main .block-container {
        padding-top: 40px !important;
        padding-bottom: 0px !important;
        padding-left: 10px !important;
        padding-right: 10px !important;
        max-width: 100%;
        background-color: transparent !important;
    }
    header {display: none !important;}
    
    /* إجبار التطبيق على ترتيب الأعمدة من اليسار لليمين حتى الدگمة تبقى باليمين دائماً */
    [data-testid="stHorizontalBlock"] {
        direction: ltr !important;
    }
    
    /* نصوص العداد */
    .title-font { font-size: 35px !important; font-weight: bold; text-align: center; color: white; text-shadow: 2px 2px 8px #000000; margin-bottom: 10px;}
    .number-display { font-size: 140px; font-weight: bold; color: white; text-align: center; text-shadow: 3px 3px 12px #000000; margin: 10px 0px;}
    
    /* دگمة التسبيح الرئيسية (لون سمائي وحجم عملاق) */
    button[kind="primary"] {
        height: 380px !important; /* حجم عملاق */
        width: 100% !important;
        font-size: 70px !important;
        font-weight: bold !important;
        border-radius: 40px !important;
        background: linear-gradient(135deg, #00c6ff, #0072ff) !important; /* تدرج سمائي وأزرق */
        color: white !important;
        border: 4px solid rgba(255,255,255,0.4) !important;
        box-shadow: 0px 10px 20px rgba(0, 0, 0, 0.6) !important;
    }
    button[kind="primary"]:active {
        transform: scale(0.95) !important;
    }
    
    /* زر التصفير صغير على اليسار */
    button[kind="secondary"] {
        height: 60px !important;
        width: 100% !important;
        font-size: 20px !important;
        background: rgba(231, 76, 60, 0.8) !important;
        color: white !important;
        border: 2px solid white !important;
        border-radius: 15px !important;
    }

    /* إعدادات الخلفية مخفية وشفافة */
    div[data-testid="stExpander"] {
        background-color: rgba(0, 0, 0, 0.3) !important;
        border: none !important;
        margin-top: 30px !important;
    }
    div[data-testid="stExpander"] * {
        color: white !important;
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

# ترتيب الأزرار: اليسار (1) للتصفير، واليمين (2.5) للتسبيح
col_left, col_right = st.columns([1, 2.5])

with col_right:
    # الزر الرئيسي (Primary) لليمين
    if st.button("سبّح", type="primary"):
        st.session_state.tasbeeh_count += 1
        st.rerun()

with col_left:
    # زر التصفير (Secondary) لليسار
    st.write("") 
    st.write("") 
    st.write("") 
    if st.button("🔄 تصفير", type="secondary"):
        st.session_state.tasbeeh_count = 0
        st.rerun()

# رفع الصورة وتحديث الذاكرة
with st.expander("⚙️ لتغيير الصورة الخلفية اضغط هنا"):
    uploaded_file = st.file_uploader("اختر صورة من تلفونك:", type=['png', 'jpg', 'jpeg'])
    if uploaded_file is not None:
        st.session_state.bg_image = base64.b64encode(uploaded_file.getvalue()).decode()
        st.rerun()

# تفعيل الصورة الخلفية
apply_bg()
