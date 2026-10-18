# -*- coding: utf-8 -*-
import re
d = open('build_deck.js', encoding='utf-8').read()
# slide 7 source line
d = re.sub(r"Phosphor chemistry: Seeram; CR mechanism wording to be cross-checked with Bushberg et al\. \(2012\)\.",
           "Laser/emission details: Storage Phosphors for Medical Imaging, Materials 2011 (PMC5448636).", d)
# slide 8 source line
d = re.sub(r"Detector terms \(a-Si photodiode \+ TFT\) per Bushberg et al\. \(2012\)\.",
           "Terms (a-Si photodiode + TFT): see sources.md.", d)
# references slide
d = d.replace("    'Bushberg JT, Seibert JA, Leidholdt EM, Boone JM. The Essential Physics of Medical Imaging. 3rd ed. Lippincott Williams & Wilkins; 2012.',\n",
              "    'Seibert JA. Dose metrics: exposure index (summary of AAPM TG-116 / IEC 62494-1). IUPESM teaching slides, 2015.',\n")
d = d.replace("    'Bushong SC. Radiologic Science for Technologists. 11th ed. Elsevier; 2017.',\n",
              "    'Leblans P, et al. Storage phosphors for medical imaging. Materials 2011;4:1034-86 (PMC5448636).',\n")
open('build_deck.js', 'w', encoding='utf-8').write(d)

s = open('../sources.md', encoding='utf-8').read()
s = s.replace("- Bushberg JT, et al. *The Essential Physics of Medical Imaging*, 3rd ed., 2012 (supplementary; not read directly. Equivalent facts were verified in open sources, see Knowledge Guide §17).\n- Bushong SC. *Radiologic Science for Technologists*, 11th ed., 2017.\n",
              "- Seibert JA. Dose metrics: exposure index. IUPESM teaching slides, 2015: https://iupesm.org/wp-content/uploads/2015/08/Dose-metrics-New-_Exposure-Index_-_-J.-Anthony-Seibert.pdf (EI/DI, TG-116 action guidance).\n- Storage Phosphors for Medical Imaging, Materials 2011 (PMC5448636): https://pmc.ncbi.nlm.nih.gov/articles/PMC5448636/ (CR mechanism).\n- Axis Imaging News, \"Flat panel DR: what you need to know\" and howradiologyworks.com (direct vs indirect). Textbooks by Bushberg and Bushong were **not** consulted; the group may add them if available.\n")
open('../sources.md', 'w', encoding='utf-8').write(s)

k = open('../Knowledge_Guide.md', encoding='utf-8').read()
k = k.replace("| ⚠ standard physics, not re-checked | Seeram §1.3.6; Bushong |", "| ⚠ standard physics, not re-checked | Seeram §1.3.6 |")
open('../Knowledge_Guide.md', 'w', encoding='utf-8').write(k)

c = open('../Rehearsal_Checklist.md', encoding='utf-8').read()
c = c.replace("- [ ] Verify the ⚠ items in the Knowledge Guide (Bushberg) and confirm DI bands on slide 12.",
              "- [ ] Two ⚠ items remain in the Knowledge Guide (CR resolution reasons; kVp/mAs dose trade-off). Check them in Bushberg/Bushong if you have the book, or leave them out. DI bands on slide 12 were verified (Guide §17).")
open('../Rehearsal_Checklist.md', 'w', encoding='utf-8').write(c)
print('done')
