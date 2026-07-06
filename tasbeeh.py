import streamlit as st
import base64

# إعدادات الصفحة
st.set_page_config(page_title="السبحة الإلكترونية", page_icon="📿", layout="centered")

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
        /* إضافة طبقة شفافة فوق الخلفية حتى تبين الكتابة واضحة */
        .stApp > header {{
            background-color: transparent;
        }}
        .block-container {{
            background-color: rgba(255, 255, 255, 0.85);
            padding: 2rem;
            border-radius: 20px;
            margin-top: 20px;
        }}
        </style>
        """
        st.markdown(bg_css, unsafe_allow_html=True)

# تصميم الواجهة والأزرار
st.markdown("""
    <style>
    .title-font { font-size: 40px !important; font-weight: bold; text-align: center; color: #1f618d; text-shadow: 1px 1px 2px rgba(0,0,0,0.1); margin-bottom: 0px;}
    .number-display { font-size: 90px; font-weight: bold; color: #145a32; text-align: center; text-shadow: 2px 2px 4px rgba(0,0,0,0.2); margin: 10px 0px;}
    
    /* تكبير الزر الرئيسي للسبحة وجعله بارز */
    div.stButton > button {
        height: 200px;
        width: 100%;
        font-size: 50px !important;
        font-weight: bold;
        border-radius: 25px;
        background: linear-gradient(135deg, #27ae60, #2ecc71);
        color: white;
        border: 3px solid #1e8449;
        box-shadow: 0px 8px 15px rgba(0, 0, 0, 0.2);
        transition: all 0.2s ease-in-out;
    }
    
    /* تأثير عند الضغط على الزر الكبير */
    div.stButton > button:active {
        transform: scale(0.95);
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
        background: linear-gradient(135deg, #1e8449, #27ae60);
    }
    
    /* تخصيص زر التصفير ليكون أصغر ولونه مختلف */
    div[data-testid="column"]:nth-of-type(2) div.stButton > button {
        height: 60px;
        font-size: 22px !important;
        background: linear-gradient(135deg, #e74c3c, #c0392b);
        border: none;
        border-radius: 10px;
        box-shadow: none;
    }
    </style>
    """, unsafe_allow_html=True)

# العنوان
st.markdown('<p class="title-font">📿 السبحة الإلكترونية</p>', unsafe_allow_html=True)

# قائمة رفع صورة الخلفية (مخفية داخل قائمة قابلة للطي لترتيب الواجهة)
with st.expander("🖼️ إعدادات الخلفية (اضغط لتغيير الصورة)"):
    bg_img = st.file_uploader("ارفع صورة دينية من هاتفك لتكون خلفية للتطبيق:", type=['png', 'jpg', 'jpeg'])
add_bg_from_upload(bg_img)

# اختيار الذكر
zikr_option = st.selectbox("اختر الذكر:", ["سبحان الله", "الحمد لله", "لا إله إلا الله", "الله أكبر", "أستغفر الله", "اللهم صل على محمد وآل محمد"])

# عرض العداد بخط عملاق
st.markdown(f'<div class="number-display">{st.session_state.tasbeeh_count}</div>', unsafe_allow_html=True)

# الزر الكبير للتسبيح
if st.button(f"اضغط هنا للتسبيح", key="main_btn"):
    st.session_state.tasbeeh_count += 1
    st.rerun()

st.write("---")

# زر التصفير بحجم معقول في الأسفل
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("🔄 تصفير العداد", key="reset_btn"):
        st.session_state.tasbeeh_count = 0
        st.rerun()
