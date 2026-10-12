# -*- coding: utf-8 -*-
import io
import os

BASE = 'E:/WKB-OB'
files = [
    'RAW_FULL/ima_sync/WKB/Resources/Ebook/29_Principles_of_polymerization.pdf.md',
    'RAW_FULL/ima_sync/WKB/Resources/Ebook/Barel_Paye_Maibach_Handbook_of_Cosmetic.pdf.md',
    'RAW_FULL/ima_sync/WKB/Resources/Ebook/Cosmetic_Formulation_of_Skin_Care_Produc.pdf.md',
    'RAW_FULL/ima_sync/WKB/Resources/Ebook/Ebook Extract/Absorbent Technology (Chatterjee & Gupta)/chapters/Absorbent Technology_ch10_report.md.md',
    'RAW_FULL/ima_sync/WKB/Resources/Ebook/Ebook Extract/Biodegradable Thermoplastic/Biodegradable Thermoplastic_concepts.md.md',
    'RAW_FULL/ima_sync/WKB/Resources/Ebook/Ebook Extract/Cosmetic Science and Technology/ch07_Percutaneous_Absorption_report.md.md',
    'RAW_FULL/ima_sync/WKB/Resources/Ebook/Ebook Extract/Cosmetic Science and Technology/ch37_Classification_of_Surfactants_report.md.md',
    'RAW_FULL/ima_sync/WKB/Resources/Ebook/Ebook Extract/ES纤维亲水_深度拆书报告_academic_20260813.md.md',
    'RAW_FULL/ima_sync/WKB/Resources/Ebook/Ebook Extract/Ebewole Polymer Science Technology/chapters/Ebewole Polymer Science Technology_ch04.md.md',
    'RAW_FULL/ima_sync/WKB/Resources/Ebook/Ebook Extract/Ebewole Polymer Science Technology/chapters/Ebewole Polymer Science Technology_ch13.md.md',
]

for f in files:
    p = os.path.join(BASE, f.replace('/', os.sep))
    name = os.path.basename(f)
    if not os.path.exists(p):
        print('MISSING\t%s' % name)
        continue
    s = io.open(p, encoding='utf-8').read()
    try:
        content = s.split('\n\n# ', 1)[1].split('\n\n', 1)[1]
    except Exception:
        content = None
    if content is None:
        print('PARSE_FAIL\t%s' % name)
    else:
        print('%d\t%s' % (len(content), name))
