
import pandas as pd
from tkinter import Tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

# إنشاء نافذة tkinter واحدة
root = Tk()
root.withdraw()

# فتح نافذة اختيار ملف
file_path = askopenfilename(title="اختر ملف Excel", filetypes=[("Excel files", "*.xlsx *.xls")])
# قراءة ملف excel
df = pd.read_excel(file_path)

# فتح نافذة حفظ الملف
save_path = asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")], title="اختر مكان حفظ ملف csv")

# التحقق من أن المستخدم اختار مسارًا
if file_path and save_path:
    df = pd.read_excel(file_path)
    df.to_csv(save_path, encoding='utf-8-sig', index=False)
    print("تم الحفظ في:", save_path)
else:
    print("لم يتم اختيار ملف أو لم يتم تحديد مسار للحفظ.")




