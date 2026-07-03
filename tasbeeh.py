import streamlit as st
import time

# إعدادات الصفحة
st.set_page_config(page_title="مُنجز | MCQs & Tasbeeh", page_icon="🎯", layout="centered")

# تصميم مخصص متناسق مع الموبايل
st.markdown("""
    <style>
    .big-font { font-size:30px !important; font-weight: bold; text-align: center; color: #4A90E2; }
    .counter-box { background-color: #f0f2f6; padding: 20px; border-radius: 15px; text-align: center; margin-bottom: 20px; }
    .number-display { font-size: 50px; font-weight: bold; color: #2C3E50; }
    div.stButton > button:first-child { width: 100%; font-size: 20px; padding: 10px; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<p class="big-font">🎯 عداد الإنجاز والتسبيح</p>', unsafe_allow_html=True)

# استخدام الـ Session State لحفظ العدادات
if 'mcq_count' not in st.session_state:
    st.session_state.mcq_count = 0
if 'tasbeeh_count' not in st.session_state:
    st.session_state.tasbeeh_count = 0

# --- القسم الأول: عداد الـ MCQs ---
st.markdown("### 📚 أسئلة الـ MCQ (الهدف: 19)")
col1, col2 = st.columns([2, 1])

with col1:
    if st.button("➕ خلصت سؤال"):
        if st.session_state.mcq_count < 19:
            st.session_state.mcq_count += 1
        else:
            st.balloons() # احتفال إذا عبر الـ 19
            st.success("عاشت إيدك! خلصت الـ 19 سؤال")

with col2:
    if st.button("🔄 تصفير الأسئلة"):
        st.session_state.mcq_count = 0

# عرض عداد الـ MCQ
progress = st.session_state.mcq_count / 19
st.progress(progress)
st.markdown(f'<div class="counter-box"><div class="number-display">{st.session_state.mcq_count} / 19</div></div>', unsafe_allow_html=True)

st.write("---")

# --- القسم الثاني: عداد السبحة ---
st.markdown("### 📿 السبحة الإلكترونية")

# خيارات الأذكار
zikr_option = st.selectbox("اختر الذكر:", ["سبحان الله", "الحمد لله", "لا إله إلا الله", "اللهم صلي وسلم على سيدنا محمد وعلى اله وصحبه وسلم", "أستغفر الله"])

col3, col4 = st.columns([2, 1])

with col3:
    if st.button(f"📿 {zikr_option}"):
        st.session_state.tasbeeh_count += 1

with col4:
    if st.button("🔄 تصفير السبحة"):
        st.session_state.tasbeeh_count = 0

# عرض عداد السبحة
st.markdown(f'<div class="counter-box"><div class="number-display">{st.session_state.tasbeeh_count}</div></div>', unsafe_allow_html=True)
