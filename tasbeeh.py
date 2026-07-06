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
    
    /* زر التسبيح - مستطيل عمودي (كبسولة) على اليمين */
    button[kind="primary"] {
        position: fixed !important;
        bottom: 50px !important;
        right: 20px !important;
        width: 90px !important;  
        height: 400px !important; 
        font-size: 30px !important;
        font-weight: bold !important;
        border-radius: 50px !important; 
        background: linear-gradient(135deg, #00c6ff, #0072ff) !important;
        color: white !important;
        border: 3px solid rgba(255,255,255,0.6) !important;
        box-shadow: 0px 8px 15px rgba(0, 0, 0, 0.5) !important;
        z-index: 1000 !important;
    }
    button[kind="primary"]:active {
        transform: scale(0.95) !important;
    }
    
    /* زر التصفير - صغير ومربع على اليسار */
    button[kind="secondary"] {
        position: fixed !important;
        bottom: 50px !important;
        left: 20px !important;
        width: 90px !important;
        height: 90px !important;
        font-size: 22px !important;
        background: rgba(231, 76, 60, 0.9) !important;
        color: white !important;
        border: 2px solid white !important;
        border-radius: 20px !important;
        box-shadow: 0px 5px 10px rgba(0, 0, 0, 0.5) !important;
        z-index: 1000 !important;
    }

    /* تصغير مستطيل اختيار الصورة وتوسيطه حتى لا يتعارض مع الأزرار */
    div[data-testid="stExpander"] {
        background-color: rgba(255, 255, 255, 0.95) !important;
        border-radius: 15px !important;
        margin-top: 40px !important;
        width: 220px !important; /* حجم المستطيل صار صغير وملموم */
        margin-left: auto !important; /* توسيط */
        margin-right: auto !important; /* توسيط */
        border: 1px solid #ccc !important;
        position: relative;
        z-index: 500;
    }
    div[data-testid="stExpander"] * { 
        color: black !important; 
    }
    
    /* القائمة المنسدلة للأذكار */
    .stSelectbox {
        position: relative;
        z-index: 500;
    }
    .stSelectbox > div > div {
        background-color: rgba(0, 0, 0, 0.6) !important;
        color: white !important;
        border: none !important;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<p class="title-font">📿 السبحة الإلكترونية</p>', unsafe_allow_html=True)
zikr_option = st.selectbox("", ["سبحان الله", "الحمد لله", "لا إله إلا الله", "الله أكبر", "أستغفر الله", "اللهم صل على محمد وآل محمد"], label_visibility="collapsed")
st.markdown(f'<div class="number-display">{st.session_state.tasbeeh_count}</div>', unsafe_allow_html=True)

# أزرار التسبيح والتصفير
if st.button("سبّح", type="primary"):
    st.session_state.tasbeeh_count += 1
    st.rerun()

if st.button("تصفير", type="secondary"):
    st.session_state.tasbeeh_count = 0
    st.rerun()

# الإعدادات لرفع الصورة بحجم صغير ومتوسط
with st.expander("⚙️ لتغيير الصورة اضغط هنا"):
    uploaded_file = st.file_uploader("اختر صورة:", type=['png', 'jpg', 'jpeg'])
    if uploaded_file is not None:
        st.session_state.bg_image = base64.b64encode(uploaded_file.getvalue()).decode()
        st.rerun()

# تطبيق الخلفية
apply_bg()
