import pandas as pd
from tkinter import Tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

# إنشاء نافذة tkinter واحدة
root = Tk()
root.withdraw()

# فتح نافذة اختيار ملف
file_path = askopenfilename(title="اختر ملف")

# قراءة ملف CSV
df = pd.read_csv(file_path)

# فتح نافذة حفظ الملف
save_path = asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")], title="اختر مكان حفظ الملف")

# التحقق من أن المستخدم اختار مسارًا
if save_path:
    df.to_excel(save_path, index=False)
    print("تم الحفظ في:", save_path)
else:
    print("لم يتم اختيار مسار للحفظ.")
