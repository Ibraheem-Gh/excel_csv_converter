import streamlit as st
import pandas as pd
import io

# إعداد الصفحة
st.set_page_config(
    page_title="محوّل Excel و CSV",
    page_icon="📝",
    layout="centered"
)

# --- الهيدر  ---
st.markdown("""
<div style="background-color:#34495E; padding:25px; border-radius:12px; box-shadow: 0 4px 8px rgba(0,0,0,0.3);">
    <h1 style="text-align:center; color:white;">📝 محوّل الملفات بين Excel و CSV</h1>
    <p style="text-align:center; color:#ecf0f1;">أداة تفاعلية لتحويل، تنظيف، وتصوّر بيانات ملفاتك بسهولة</p>
</div>
""", unsafe_allow_html=True)

df = None
file_type = None

# --- رفع الملف ---
with st.expander("📂 رفع الملف"):
    uploaded_file = st.file_uploader("اختر ملف بصيغة Excel أو CSV", type=["csv", "xlsx"])
    if uploaded_file:
        st.success("✅ تم رفع الملف بنجاح")
        try:
            df = pd.read_excel(uploaded_file)
            file_type = "Excel"
        except:
            df = pd.read_csv(uploaded_file)
            file_type = "CSV"
        st.info(f"📁 نوع الملف: {file_type}")

# --- تنظيف البيانات ---
if df is not None:
    with st.expander("🧹 تنظيف البيانات"):
        if st.checkbox("🧽 حذف الصفوف الفارغة"):
            df.dropna(inplace=True)
        if st.checkbox("🧼 إزالة القيم المكررة"):
            df.drop_duplicates(inplace=True)
        st.dataframe(df)

# --- التصور البياني ---
if df is not None:
    with st.expander("📊 معاينة البيانات"):
        st.write(f"📈 عدد الصفوف: {df.shape[0]} | عدد الأعمدة: {df.shape[1]}")
        if st.checkbox("📉 عرض مخطط بياني للبيانات الرقمية"):
            st.bar_chart(df.select_dtypes(include='number'))

# --- تحويل الملف وزر التحميل بعد المعالجة ---
if df is not None:
    st.markdown("---")
    st.write("📥 لتحميل الملف المحوّل بعد المعالجة:")

    output = io.BytesIO()# يقوم بإنشاء كائن في الذاكرة لتخزين البيانات بشكل مؤقت دون الحاجة لحفظها على القرص مباشرة.
    converted_type = "CSV" if file_type == "Excel" else "xlsx"

    if converted_type == "CSV":
        df.to_csv(output, index=False, encoding="utf-8-sig")

    else:
        with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
            df.to_excel(writer, index=False, sheet_name='Sheet1')

    st.download_button(
        label=f"💾 تحميل الملف بصيغة {converted_type}",
        data=output.getvalue(),
        file_name=f"converted.{converted_type}",
        mime="application/octet-stream"
    )

# --- الفوتر  ---
st.markdown("""
<div style="background-color:#EAECEE; padding:10px; border-radius:10px; margin-top:30px;">
    <p style="text-align:center; color:#2C3E50; font-weight:bold;">
        تم التصميم بواسطة إبراهيم 🚀 | جميع الحقوق محفوظة © 2025
    </p>
</div>
""", unsafe_allow_html=True)
