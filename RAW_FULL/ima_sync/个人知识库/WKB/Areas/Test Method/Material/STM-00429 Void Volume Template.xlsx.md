---
media_id: "excel_3867e2b60070d7dc3f413086d0b0036e_88a4d4a13fdd88dfaf8cd367a924eb8a001a693ee6c0644e"
source_file: "STM-00429 Void Volume Template.xlsx.md"
original_path: "RAW/ima_sync/个人知识库/WKB/Areas/Test Method/Material/STM-00429 Void Volume Template.xlsx.md"
extracted: "2026-09-27"
extract_method: "ima-mcp fetch_media_content"
extract_status: "ok"
clean_rules: "v2: dead-image-link->text(alt kept); repeat-digits->compressed"
processed: "2026-09-27"
---

# STM-00429 Void Volume Template.xlsx.md

[INSTRUCTIONS]
|Void Volume vs Saturation ||||||||||LabVantage Data Import Instructions:|
|---|---|---|---|---|---|---|---|---|---|---|
|||||||||||1. Data tab must remain named &#34;Data&#34;|
|Objective:||||||||||2. Must have only one sample per file.|
|Quantify the void volume (via thickness at 0.05 psi) of a material at various levels of||||||||||3. Sample ID must be the LabVantage Sample ID Number SYY-000000|
|saturation and SAP swelling ||||||||||4. On Data tab, cell location must not be changed.|
|||||||||||5. In LabVantage, use designateddata file definition (import task) for STM-00429|
|Procedure:|||||||||||
|1.  Obtain 65mm Petri dish||||||||||Data tab cell protection password: STM-00429|
|2.  Die cut eighteen 2 3/8th&#34; diameter circle specimens per code|||||||||||
|3.  Tare empty petri dish on scale|||||||||||
|4.  Place specimen in petri dish and record weight of sample|||||||||||
|5.  Measure thickness of specimen + petri dish (0.05 psi) in mm|||||||||||
|6.  Place specimen and petri dish on scale and tare scale|||||||||||
|7.  Add and record actual weight of fluid added |||||||||||
|8.  Wait 20 minutes|||||||||||
|9.  Measure and record wet bulk of specimen + petri dish (0.05 psi) in mm|||||||||||
|10. Enter material composition and densities for each component|||||||||||
||||||||||||
|The void volume vs saturation curve will automatically be graphed|||||||||||
|Basis weight and density of the specimens are also calculated|||||||||||
||||||||||||
|Requestor can use these inputs for component densities to calculate void volume|||||||||||
|||||||||||Spreadsheet modification notes:|
|Typical component densities:||||g/cc||||||Rows 61-79 set at 0.2 height.  Change height to 13.2 to reveal cells.  Hiding these cells affects the R2 calculation.|
|SAM Density||||1.5||||||Hidden columns W-Z have the comparative data to calculate R2.|
|Pulp Density||||1.5|||||||
|PE/PET Bicomponent binder fiber||||1.15|||||||
|PE/PP Bicomponent binder fiber||||0.95|||||||
|Polypropylene||||0.93|||||||
||||||||||||
|Requestor should also consider loading levels to determine loading for codes to |||||||||||
|get complete saturation curves for the products.  Suggested values are|||||||||||
||||||||||||
|Huggies diapers with SAM/fluff core|||||2.5, 5, 7.5, 10, 15, 20|||g/g|||
|Pampers diapers - SAM/fluff or 100% SAM core|||||2.5, 5, 7.5, 10, 15, 20|||g/g|||
|Huggies diapers with ActivTech BLIZZARD core|||||5, 10, 15, 20, 25, 30|||g/g|||
||||||||||||
|Researcher can also consider if target gram loadings like 0, 12.5, 25, 37.5, 50, 75, and 100 g  |||||||||||
|would yield void volume for range of 0 to near 100% saturation.  In this case, the g/g loading would be  |||||||||||
|set from the actual loading.|||||||||||
||||||||||||
|||||||Spreadsheeet Rev.|11/22/2021 MJB/ATB||||

[Saline Data]
||Void Volume as a Function of Saturation||||STM-00429|Rev. 1/25/2022 MJB||||||||||||||||||||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||||||||||||||||||||||||
||Sample ID|||Analyst||||||||||||||||||||||
||Date|||Instrument ID||||||||||||||||||||||
||Code Description|||||||||||||||||||||||
|||||||||||||||||||||||||
||Component|Percent Composition|Component Density (g/cc)|||||||Polynominal Curve Fit Outputs||||||||||||||||
||Superabsorbent|0|1.5||Composition Constant (cc/g)|0.736140350877193|||||||Fit 3rd Power|Fit 2nd Power|Fit 1st Power|Fit Intercept|Fit R2|||||||||
||Pulp|82|1.5||Specimen Area (cm2)|28.58146874284323||||Sat Level - VV by Weight|Sat Level - VV by Weight||#VALUE!||||#VALUE!|||||||||
||Binder|18|0.95|||||||Web Density -VV by Weight|Web Density -VV by Weight||#VALUE!||||#VALUE!|||||||||
||Intake Materials (Surge/Liner)|0|1.2|||||||Fluid Add - VV by Area|Fluid Add - VV by Area||#VALUE!||||#VALUE!|||||||||
|||0||||||||Sat Level - VV by Area|Sat Level - VV by Area||#VALUE!||||#VALUE!|||||||||
||Specimen Diameter (in)|2.375||||||||||||||||||||||||
|||||||||||||||||||||||||
|||||Avg|Stdev|||||||||||||||||||||
|||||0|0|BW (gsm)|||||||||||||||||||
|||||#DIV/0!|#DIV/0!|0.05 psi Density (g/cc)|||||||||||||||||||
|||||||||||||||||||||||||
|Saturation Set|Target Saturation Level|Dish Number|Dish Thickness|Specimen Dry Weight|Dry Thickness (Specimen and Dish)|Calculated Weight of Fluid to Add|Fluid Added Amount|Wet Thickness (Specimen and Dish)|Dry Thickness @ 0.05 psi|Wet Thickness @ 0.05 psi|Web Density|Specimen Wet Weight|Specimen Basis Weight|Void Volume Dry by Dry Weight|Void Volume Dry by Area|Web Density Dry|Actual Saturation Level|Void Volume Wet by Dry Weight|Void Volume Wet by Area|||Calc VV per unit dry wt from sat level|Calc VV per unit dry wt from web density|Calc VV per uint area from fluid added|Calc VV per uint area from sat level|
||g/g||mm|g|mm|g|g|mm|mm|mm|g/cm3|g|gsm|cm³/g|cm³/cm²|g/cm³|g/g|cm³/g|cm³/cm²|||cm³/g|cm³/g|cm³/cm²|cm³/cm²|
|||||||||||||||||||||||||
|1|1.25|1||||0|||0|0|#DIV/0!|0|0|#DIV/0!|#DIV/0!|#DIV/0!|#DIV/0!|#DIV/0!|0|||#VALUE!|#VALUE!|#VALUE!|#VALUE!|
|1|1.25|2||||0|||0|0|#DIV/0!|0|0|#DIV/0!|#DIV/0!|#DIV/0!|#DIV/0!|#DIV/0!|0|||#VALUE!|#VALUE!|#VALUE!|#VALUE!|
|1|1.25|3||||0|||0|0|#DIV/0!|0|0|#DIV/0!|#DIV/0!|#DIV/0!|#DIV/0!|#DIV/0!|0|||#VALUE!|#VALUE!|#VALUE!|#VALUE!|
|2|2.5|4||||0|||0|0|#DIV/0!|0|0|#DIV/0!|#DIV/0!|#DIV/0!|#DIV/0!|#DIV/0!|0|||#VALUE!|#VALUE!|#VALUE!|#VALUE!|
|2|2.5|5||||0|||0|0|#DIV/0!|0|0|#DIV/0!|#DIV/0!|#DIV/0!|#DIV/0!|#DIV/0!|0|||#VALUE!|#VALUE!|#VALUE!|#VALUE!|
|2|2.5|6||||0|||0|0|#DIV/0!|0|0|#DIV/0!|#DIV/0!|#DIV/0!|#DIV/0!|#DIV/0!|0|||#VALUE!|#VALUE!|#VALUE!|#VALUE!|
|3|3.75|7||||0|||0|0|#DIV/0!|0|0|#DIV/0!|#DIV/0!|#DIV/0!|#DIV/0!|#DIV/0!|0|||#VALUE!|#VALUE!|#VALUE!|#VALUE!|
|3|3.75|8||||0|||0|0|#DIV/0!|0|0|#DIV/0!|#DIV/0!|#DIV/0!|#DIV/0!|#DIV/0!|0|||#VALUE!|#VALUE!|#VALUE!|#VALUE!|
|3|3.75|9||||0|||0|0|#DIV/0!|0|0|#DIV/0!|#DIV/0!|#DIV/0!|#DIV/0!|#DIV/0!|0|||#VALUE!|#VALUE!|#VALUE!|#VALUE!|
|4|5|10||||0|||0|0|#DIV/0!|0|0|#DIV/0!|#DIV/0!|#DIV/0!|#DIV/0!|#DIV/0!|0|||#VALUE!|#VALUE!|#VALUE!|#VALUE!|
|4|5|11||||0|||0|0|#DIV/0!|0|0|#DIV/0!|#DIV/0!|#DIV/0!|#DIV/0!|#DIV/0!|0|||#VALUE!|#VALUE!|#VALUE!|#VALUE!|
|4|5|12||||0|||0|0|#DIV/0!|0|0|#DIV/0!|#DIV/0!|#DIV/0!|#DIV/0!|#DIV/0!|0|||#VALUE!|#VALUE!|#VALUE!|#VALUE!|
|5|7.5|13||||0|||0|0|#DIV/0!|0|0|#DIV/0!|#DIV/0!|#DIV/0!|#DIV/0!|#DIV/0!|0|||#VALUE!|#VALUE!|#VALUE!|#VALUE!|
|5|7.5|14||||0|||0|0|#DIV/0!|0|0|#DIV/0!|#DIV/0!|#DIV/0!|#DIV/0!|#DIV/0!|0|||#VALUE!|#VALUE!|#VALUE!|#VALUE!|
|5|7.5|15||||0|||0|0|#DIV/0!|0|0|#DIV/0!|#DIV/0!|#DIV/0!|#DIV/0!|#DIV/0!|0|||#VALUE!|#VALUE!|#VALUE!|#VALUE!|
|6|10|16||||0|||0|0|#DIV/0!|0|0|#DIV/0!|#DIV/0!|#DIV/0!|#DIV/0!|#DIV/0!|0|||#VALUE!|#VALUE!|#VALUE!|#VALUE!|
|6|10|17||||0|||0|0|#DIV/0!|0|0|#DIV/0!|#DIV/0!|#DIV/0!|#DIV/0!|#DIV/0!|0|||#VALUE!|#VALUE!|#VALUE!|#VALUE!|
|6|10|18||||0|||0|0|#DIV/0!|0|0|#DIV/0!|#DIV/0!|#DIV/0!|#DIV/0!|#DIV/0!|0|||#VALUE!|#VALUE!|#VALUE!|#VALUE!|
||1.25|1|||||0||||#DIV/0!||||||0|#DIV/0!|#DIV/0!|||#VALUE!|#VALUE!|#VALUE!|#VALUE!|
||1.25|2|||||0||||#DIV/0!||||||0|#DIV/0!|#DIV/0!|||#VALUE!|#VALUE!|#VALUE!|#VALUE!|
||1.25|3|||||0||||#DIV/0!||||||0|#DIV/0!|#DIV/0!|||#VALUE!|#VALUE!|#VALUE!|#VALUE!|
||2.5|4|||||0||||#DIV/0!||||||0|#DIV/0!|#DIV/0!|||#VALUE!|#VALUE!|#VALUE!|#VALUE!|
||2.5|5|||||0||||#DIV/0!||||||0|#DIV/0!|#DIV/0!|||#VALUE!|#VALUE!|#VALUE!|#VALUE!|
||2.5|6|||||0||||#DIV/0!||||||0|#DIV/0!|#DIV/0!|||#VALUE!|#VALUE!|#VALUE!|#VALUE!|
||3.75|7|||||0||||#DIV/0!||||||0|#DIV/0!|#DIV/0!|||#VALUE!|#VALUE!|#VALUE!|#VALUE!|
||3.75|8|||||0||||#DIV/0!||||||0|#DIV/0!|#DIV/0!|||#VALUE!|#VALUE!|#VALUE!|#VALUE!|
||3.75|9|||||0||||#DIV/0!||||||0|#DIV/0!|#DIV/0!|||#VALUE!|#VALUE!|#VALUE!|#VALUE!|
||5|10|||||0||||#DIV/0!||||||0|#DIV/0!|#DIV/0!|||#VALUE!|#VALUE!|#VALUE!|#VALUE!|
||5|11|||||0||||#DIV/0!||||||0|#DIV/0!|#DIV/0!|||#VALUE!|#VALUE!|#VALUE!|#VALUE!|
||5|12|||||0||||#DIV/0!||||||0|#DIV/0!|#DIV/0!|||#VALUE!|#VALUE!|#VALUE!|#VALUE!|
||7.5|13|||||0||||#DIV/0!||||||0|#DIV/0!|#DIV/0!|||#VALUE!|#VALUE!|#VALUE!|#VALUE!|
||7.5|14|||||0||||#DIV/0!||||||0|#DIV/0!|#DIV/0!|||#VALUE!|#VALUE!|#VALUE!|#VALUE!|
||7.5|15|||||0||||#DIV/0!||||||0|#DIV/0!|#DIV/0!|||#VALUE!|#VALUE!|#VALUE!|#VALUE!|
||10|16|||||0||||#DIV/0!||||||0|#DIV/0!|#DIV/0!|||#VALUE!|#VALUE!|#VALUE!|#VALUE!|
||10|17|||||0||||#DIV/0!||||||0|#DIV/0!|#DIV/0!|||#VALUE!|#VALUE!|#VALUE!|#VALUE!|
||10|18|||||0||||#DIV/0!||||||0|#DIV/0!|#DIV/0!|||#VALUE!|#VALUE!|#VALUE!|#VALUE!|
|||||||||||||||||||||||||
||Changed Cells|||||||||||||||||||||||||

[Blood data1]
||Void Volume as a Function of Saturation||||STM-00429|Rev. 1/25/2022 MJB||||||||||||||||||||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||||||||||||||||||||||||
||Sample ID|||Analyst||||||||||||||||||||||
||Date|||Instrument ID||||||||||||||||||||||
||Code Description|||||||||||||||||||||||
|||||||||||||||||||||||||
||Component|Percent Composition|Component Density (g/cc)|||||||Polynominal Curve Fit Outputs||||||||||||||||
||Superabsorbent|0|1.5||Composition Constant (cc/g)|0.736140350877193|||||||Fit 3rd Power|Fit 2nd Power|Fit 1st Power|Fit Intercept|Fit R2|||||||||
||Pulp|82|1.5||Specimen Area (cm2)|28.58146874284323||||Sat Level - VV by Weight|Sat Level - VV by Weight||#VALUE!||||#VALUE!|||||||||
||Binder|18|0.95|||||||Web Density -VV by Weight|Web Density -VV by Weight||#VALUE!||||#VALUE!|||||||||
||Intake Materials (Surge/Liner)|0|1.2|||||||Fluid Add - VV by Area|Fluid Add - VV by Area||#VALUE!||||#VALUE!|||||||||
|||0||||||||Sat Level - VV by Area|Sat Level - VV by Area||#VALUE!||||#VALUE!|||||||||
||Specimen Diameter (in)|2.375||||||||||||||||||||||||
|||||||||||||||||||||||||
|||||Avg|Stdev|||||||||||||||||||||
|||||0|0|BW (gsm)|||||||||||||||||||
|||||#DIV/0!|#DIV/0!|0.05 psi Density (g/cc)|||||||||||||||||||
|||||||||||||||||||||||||
|Saturation Set|Target Saturation Level|Dish Number|Dish Thickness|Specimen Dry Weight|Dry Thickness (Specimen and Dish)|Calculated Weight of Fluid to Add|Fluid Added Amount|Wet Thickness (Specimen and Dish)|Dry Thickness @ 0.05 psi|Wet Thickness @ 0.05 psi|Web Density|Specimen Wet Weight|Specimen Basis Weight|Void Volume Dry by Dry Weight|Void Volume Dry by Area|Web Density Dry|Actual Saturation Level|Void Volume Wet by Dry Weight|Void Volume Wet by Area|||Calc VV per unit dry wt from sat level|Calc VV per unit dry wt from web density|Calc VV per uint area from fluid added|Calc VV per uint area from sat level|
||g/g||mm|g|mm|g|g|mm|mm|mm|g/cm3|g|gsm|cm³/g|cm³/cm²|g/cm³|g/g|cm³/g|cm³/cm²|||cm³/g|cm³/g|cm³/cm²|cm³/cm²|
|||||||||||||||||||||||||
|1|1.25|1||||0|||0|0|#DIV/0!|0|0|#DIV/0!|#DIV/0!|#DIV/0!|#DIV/0!|#DIV/0!|0|||#VALUE!|#VALUE!|#VALUE!|#VALUE!|
|1|1.25|2||||0|||0|0|#DIV/0!|0|0|#DIV/0!|#DIV/0!|#DIV/0!|#DIV/0!|#DIV/0!|0|||#VALUE!|#VALUE!|#VALUE!|#VALUE!|
|1|1.25|3||||0|||0|0|#DIV/0!|0|0|#DIV/0!|#DIV/0!|#DIV/0!|#DIV/0!|#DIV/0!|0|||#VALUE!|#VALUE!|#VALUE!|#VALUE!|
|2|2.5|4||||0|||0|0|#DIV/0!|0|0|#DIV/0!|#DIV/0!|#DIV/0!|#DIV/0!|#DIV/0!|0|||#VALUE!|#VALUE!|#VALUE!|#VALUE!|
|2|2.5|5||||0|||0|0|#DIV/0!|0|0|#DIV/0!|#DIV/0!|#DIV/0!|#DIV/0!|#DIV/0!|0|||#VALUE!|#VALUE!|#VALUE!|#VALUE!|
|2|2.5|6||||0|||0|0|#DIV/0!|0|0|#DIV/0!|#DIV/0!|#DIV/0!|#DIV/0!|#DIV/0!|0|||#VALUE!|#VALUE!|#VALUE!|#VALUE!|
|3|3.75|7||||0|||0|0|#DIV/0!|0|0|#DIV/0!|#DIV/0!|#DIV/0!|#DIV/0!|#DIV/0!|0|||#VALUE!|#VALUE!|#VALUE!|#VALUE!|
|3|3.75|8||||0|||0|0|#DIV/0!|0|0|#DIV/0!|#DIV/0!|#DIV/0!|#DIV/0!|#DIV/0!|0|||#VALUE!|#VALUE!|#VALUE!|#VALUE!|
|3|3.75|9||||0|||0|0|#DIV/0!|0|0|#DIV/0!|#DIV/0!|#DIV/0!|#DIV/0!|#DIV/0!|0|||#VALUE!|#VALUE!|#VALUE!|#VALUE!|
|4|5|10||||0|||0|0|#DIV/0!|0|0|#DIV/0!|#DIV/0!|#DIV/0!|#DIV/0!|#DIV/0!|0|||#VALUE!|#VALUE!|#VALUE!|#VALUE!|
|4|5|11||||0|||0|0|#DIV/0!|0|0|#DIV/0!|#DIV/0!|#DIV/0!|#DIV/0!|#DIV/0!|0|||#VALUE!|#VALUE!|#VALUE!|#VALUE!|
|4|5|12||||0|||0|0|#DIV/0!|0|0|#DIV/0!|#DIV/0!|#DIV/0!|#DIV/0!|#DIV/0!|0|||#VALUE!|#VALUE!|#VALUE!|#VALUE!|
|5|7.5|13||||0|||0|0|#DIV/0!|0|0|#DIV/0!|#DIV/0!|#DIV/0!|#DIV/0!|#DIV/0!|0|||#VALUE!|#VALUE!|#VALUE!|#VALUE!|
|5|7.5|14||||0|||0|0|#DIV/0!|0|0|#DIV/0!|#DIV/0!|#DIV/0!|#DIV/0!|#DIV/0!|0|||#VALUE!|#VALUE!|#VALUE!|#VALUE!|
|5|7.5|15||||0|||0|0|#DIV/0!|0|0|#DIV/0!|#DIV/0!|#DIV/0!|#DIV/0!|#DIV/0!|0|||#VALUE!|#VALUE!|#VALUE!|#VALUE!|
|6|10|16||||0|||0|0|#DIV/0!|0|0|#DIV/0!|#DIV/0!|#DIV/0!|#DIV/0!|#DIV/0!|0|||#VALUE!|#VALUE!|#VALUE!|#VALUE!|
|6|10|17||||0|||0|0|#DIV/0!|0|0|#DIV/0!|#DIV/0!|#DIV/0!|#DIV/0!|#DIV/0!|0|||#VALUE!|#VALUE!|#VALUE!|#VALUE!|
|6|10|18||||0|||0|0|#DIV/0!|0|0|#DIV/0!|#DIV/0!|#DIV/0!|#DIV/0!|#DIV/0!|0|||#VALUE!|#VALUE!|#VALUE!|#VALUE!|
||1.25|1|||||0||||#DIV/0!||||||0|#DIV/0!|#DIV/0!|||#VALUE!|#VALUE!|#VALUE!|#VALUE!|
||1.25|2|||||0||||#DIV/0!||||||0|#DIV/0!|#DIV/0!|||#VALUE!|#VALUE!|#VALUE!|#VALUE!|
||1.25|3|||||0||||#DIV/0!||||||0|#DIV/0!|#DIV/0!|||#VALUE!|#VALUE!|#VALUE!|#VALUE!|
||2.5|4|||||0||||#DIV/0!||||||0|#DIV/0!|#DIV/0!|||#VALUE!|#VALUE!|#VALUE!|#VALUE!|
||2.5|5|||||0||||#DIV/0!||||||0|#DIV/0!|#DIV/0!|||#VALUE!|#VALUE!|#VALUE!|#VALUE!|
||2.5|6|||||0||||#DIV/0!||||||0|#DIV/0!|#DIV/0!|||#VALUE!|#VALUE!|#VALUE!|#VALUE!|
||3.75|7|||||0||||#DIV/0!||||||0|#DIV/0!|#DIV/0!|||#VALUE!|#VALUE!|#VALUE!|#VALUE!|
||3.75|8|||||0||||#DIV/0!||||||0|#DIV/0!|#DIV/0!|||#VALUE!|#VALUE!|#VALUE!|#VALUE!|
||3.75|9|||||0||||#DIV/0!||||||0|#DIV/0!|#DIV/0!|||#VALUE!|#VALUE!|#VALUE!|#VALUE!|
||5|10|||||0||||#DIV/0!||||||0|#DIV/0!|#DIV/0!|||#VALUE!|#VALUE!|#VALUE!|#VALUE!|
||5|11|||||0||||#DIV/0!||||||0|#DIV/0!|#DIV/0!|||#VALUE!|#VALUE!|#VALUE!|#VALUE!|
||5|12|||||0||||#DIV/0!||||||0|#DIV/0!|#DIV/0!|||#VALUE!|#VALUE!|#VALUE!|#VALUE!|
||7.5|13|||||0||||#DIV/0!||||||0|#DIV/0!|#DIV/0!|||#VALUE!|#VALUE!|#VALUE!|#VALUE!|
||7.5|14|||||0||||#DIV/0!||||||0|#DIV/0!|#DIV/0!|||#VALUE!|#VALUE!|#VALUE!|#VALUE!|
||7.5|15|||||0||||#DIV/0!||||||0|#DIV/0!|#DIV/0!|||#VALUE!|#VALUE!|#VALUE!|#VALUE!|
||10|16|||||0||||#DIV/0!||||||0|#DIV/0!|#DIV/0!|||#VALUE!|#VALUE!|#VALUE!|#VALUE!|
||10|17|||||0||||#DIV/0!||||||0|#DIV/0!|#DIV/0!|||#VALUE!|#VALUE!|#VALUE!|#VALUE!|
||10|18|||||0||||#DIV/0!||||||0|#DIV/0!|#DIV/0!|||#VALUE!|#VALUE!|#VALUE!|#VALUE!|
|||||||||||||||||||||||||
||Changed Cells|||||||||||||||||||||||||

[Example]
||Void Volume as a Function of Saturation||||STM-00429|Rev. 1/25/2022 MJB||||||||||||||||||||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||||||||||||||||||||||||
||Sample ID|S20-002071||Analyst|W.R.Baumann|||||||||||||||||||||
||Date|2019/09/17||Instrument ID|IC-1121, IC-205, IPS-1591, IPS-0181, IPS-1124, IPS-1505, IPS-0124, IPS-0352, IPS-1610|IC-1121, IC-205, IPS-1591, IPS-0181, IPS-1124, IPS-1505, IPS-0124, IPS-0352, IPS-1610|IC-1121, IC-205, IPS-1591, IPS-0181, IPS-1124, IPS-1505, IPS-0124, IPS-0352, IPS-1610|||||||||||||||||||
||Code Description|Little Movers Control|Little Movers Control|||||||||||||||||||||||
|||||||||||||||||||||||||
||Component|Percent Composition|Component Density (g/cc)|||||||Polynominal Curve Fit Outputs||||||||||||||||
||Superabsorbent|60|1.5||Composition Constant (cc/g)|0.6666666666666667|||||||Fit 3rd Power|Fit 2nd Power|Fit 1st Power|Fit Intercept|Fit R2|||||||||
||Pulp|40|1.5||Specimen Area (cm2)|45.60367311877479||||Sat Level - VV by Weight|Sat Level - VV by Weight||0.003146678794591015|-0.1362722807612937|1.1986459360561|6.061396046141011|0.9510161817919952|||||||||
||Binder|0|1.2|||||||Web Density -VV by Weight|Web Density -VV by Weight||14.286421719171333|-51.122980655614235|34.9904940672878|1.9867261510708727|0.9245382082409032|||||||||
||Intake Materials (Surge/Liner)|0|1.2|||||||Fluid Add - VV by Area|Fluid Add - VV by Area||0.0000027013323281072562|-0.0005674576222492444|0.024100638956856157|0.6342823976284719|0.9113399176323979|||||||||
|||0||||||||Sat Level - VV by Area|Sat Level - VV by Area||0.0003024826621052742|-0.013390685510330652|0.11891026322973457|0.6336151512829757|0.9394194148826952|||||||||
||Specimen Diameter (in)|3||||||||||||||||||||||||
|||||||||||||||||||||||||
|||||Avg|Stdev|||||||||||||||||||||
|||||1046.5774906655163|55.655840311888404|BW (gsm)|||||||||||||||||||
|||||0.14962852672201812|0.01144855909660569|0.05 psi Density (g/cc)|||||||||||||||||||
|||||||||||||||||||||||||
|Saturation Set|Target Saturation Level|Dish Number|Dish Thickness|Specimen Dry Weight|Dry Thickness (Specimen and Dish)|Calculated Weight of Fluid to Add|Fluid Added Amount|Wet Thickness (Specimen and Dish)|Dry Thickness @ 0.05 psi|Wet Thickness @ 0.05 psi|Web Density|Specimen Wet Weight|Specimen Basis Weight|Void Volume Dry by Dry Weight|Void Volume Dry by Area|Web Density Dry|Actual Saturation Level|Void Volume Wet by Dry Weight|Void Volume Wet by Area|||Calc VV per unit dry wt from sat level|Calc VV per unit dry wt from web density|Calc VV per uint area from fluid added|Calc VV per uint area from sat level|
||g/g||mm|g|mm|g|g|mm|mm|mm|g/cm3|g|gsm|cm³/g|cm³/cm²|g/cm³|g/g|cm³/g|cm³/cm²|||cm³/g|cm³/g|cm³/cm²|cm³/cm²|
|||||||||||||||||||||||||
|1|2.5|1|1.39|4.74|9.1|11.850000000000001|11.96|13.47|7.71|12.08|0.3031445137160849|16.700000000000003|1039.3899604653923|6.751145986197335|0.7017073359689739|0.13481063041055674|2.5232067510548526|8.432328507907163|0.8764477594464825|||8.268789043990921|8.293864957291351|0.8459773719979405|0.8532566980666892|
|1|2.5|2|1.37|4.74|9.28|11.850000000000001|12.05|14.13|7.909999999999999|12.760000000000002|0.28853612681067436|16.79|1039.3899604653923|6.943566547879928|0.7217073359689739|0.13140201775795096|2.542194092827004|9.067571075855831|0.9424742342050926|||8.279591441738257|8.169782994632069|0.8470253261627753|0.8543371156122531|
|1|2.5|3|1.38|4.72|7.79|11.799999999999999|11.93|12.82|6.41|11.440000000000001|0.319145253196807|16.65|1035.004348817859|5.526544025946606|0.5719997100788096|0.16146713710107002|2.527542372881356|7.858884614663498|0.8133979753034483|||8.271262832039458|8.411108056080208|0.8456263606047375|0.8535041083153936|
|2|5|4|1.35|5.25|8.41|26.25|26.32|17.56|7.0600000000000005|16.209999999999997|0.42706279985387513|31.57|1151.2230574774912|5.465941566067621|0.6292517961681674|0.1630627560166418|5.013333333333334|8.40067697629218|0.9671053033527849|||9.042096716305878|8.718673391403438|0.9247625980629816|0.9313106173114477|
|2|5|5|1.35|4.31|7.6|21.549999999999997|21.56|15.54|6.25|14.19|0.39977369035125604|25.869999999999997|945.099310043426|5.946394980487452|0.5619933793304382|0.15121588960694818|5.002320185614849|9.345308311417194|0.8832244437263483|||9.041319954372383|8.717361220839894|0.9171910500063019|0.9312274560972738|
|2|5|6|1.41|4.79|8.23|23.95|24.07|16.52|6.82|15.11|0.41882446111122124|28.86|1050.3539895842255|5.826382407864526|0.6119764006943851|0.15401084891264302|5.025052192066806|8.693907463285049|0.9131680389137523|||9.042899558256359|8.72350781263177|0.9232906739700932|0.9313967521920424|
|3|7.5|7|1.41|4.43|8.1|33.224999999999994|33.33|17.36|6.6899999999999995|15.95|0.5191244382785499|37.76|971.412979928626|6.220208574069301|0.6042391346714249|0.1452037339205719|7.523702031602709|8.229012481063762|0.7993769536100004|||8.705940373397915|8.372660594958633|0.9071936539665977|0.8990897067359416|
|3|7.5|8|1.34|4.79|7.94|35.925|35.99|18.83|6.6000000000000005|17.49|0.5112785677141453|40.78|1050.3539895842255|5.6169292119119065|0.5899764006943851|0.15914454387639776|7.51356993736952|8.471292474197032|0.8897855847207674|||8.709150961913778|8.422170496454491|0.8925761904639048|0.8994053333936508|
|3|7.5|9|1.36|4.38|8.54|32.85|32.89|17.89|7.179999999999999|16.53|0.4944093953525896|37.27|960.4489508097928|6.809003949607375|0.6539700699460138|0.1337672633439823|7.5091324200913245|9.034902206697431|0.8677562345091628|||8.710552868433378|8.516388230694947|0.9092141727973052|0.8995431424578654|
|4|10|10|1.35|4.77|8.77|47.699999999999996|47.74|20.32|7.42|18.97|0.6069806737268677|52.510000000000005|1045.968377936692|6.427238040698302|0.6722687748042205|0.14096608867071322|10.008385744234802|7.461251133399537|0.7804232745380217|||7.562416004017308|7.585100369604437|0.7854672967299501|0.7856438877622065|
|4|10|11|1.39|4.75|8.24|47.5|47.59|20.3|6.8500000000000005|18.91|0.6069352555047407|52.34|1041.5827662891588|5.909863035725068|0.6155611489140562|0.1520558782903881|10.018947368421053|7.469448252828731|0.7780048573835074|||7.556248663134474|7.58561265264029|0.7872047747795372|0.785028393843213|
|4|10|12|1.34|5.03|9.33|50.300000000000004|50.36|22.75|7.99|21.41|0.5673027303990414|55.39|1102.9813293546251|6.577336280033345|0.7254679113763584|0.13804522269770025|10.011928429423458|8.732431573352585|0.9631708985274735|||7.560348331216156|7.99226136930824|0.7538572811969368|0.7854375396919708|
|5|15|13|1.36|4.87|8.06|73.05|73.06|22.01|6.7|20.650000000000002|0.8275319992548912|77.93|1067.8964361743585|5.607349963637053|0.5988069042550429|0.1593875277872177|15.00205338809035|3.668361052074598|0.39174296941112846|||3.998290971981957|4.029128787141939|0.41957793982477876|0.42508237828810214|
|5|15|14|1.35|4.41|8.17|66.15|66.15|19.92|6.82|18.57|0.8331953630854865|70.56|967.0273682810927|6.385874164853608|0.6175315087812605|0.14179286924942708|15|3.5365126942323784|0.34199045635962133|||3.9998628474361073|3.9138278183100224|0.5273752675733603|0.42524384450989827|
|5|15|15|1.36|5.11|8.44|76.65|76.71|23.78|7.079999999999999|22.42|0.8002469781471333|81.82|1120.5237759447582|5.65180702571935|0.633298414937016|0.1582660700486947|15.011741682974558|4.330091676247835|0.48519706752561925|||3.990875160894289|4.5702751449438|0.3632467753802122|0.42432057404247514|
|6|20|16|1.34|4.79|8.97|95.8|95.88|24.07|7.630000000000001|22.73|0.9711824121363337|100.67|1050.3539895842255|6.597550992962806|0.6929764006943852|0.1376610733400033|20.01670146137787|0.9569552537874297|0.10051417686692117|||0.6908937370297554|0.836496450865138|0.10944305098259544|0.07451133475628513|
|6|20|17|1.37|4.99|7.9|99.80000000000001|99.89|24.68|6.53|23.31|0.986621513499126|104.88|1094.2101060595585|5.301108593164985|0.5800526595960295|0.16756663186210696|20.018036072144287|0.6183357461317387|0.0676589222355226|||0.6902605934341235|0.46553226084624955|0.07202393565402399|0.07443983645705332|
|6|20|18|1.46|5.04|8.22|100.8|101|24.99|6.760000000000001|23.529999999999998|0.9882070954195308|106.04|1105.1741351783917|5.4500164738674135|0.6023217243214407|0.16348729810331236|20.039682539682538|0.5844132635867232|0.06458784231712383|||0.6800176875839785|0.427190678129723|0.0629971266876368|0.07328256152684087|
||2.5|1|||||0||||0.13481063041055674||||||0|6.751145986197335|0.7017073359689739|||6.061396046141011|5.809714709849519|0.6342823976284719|0.6336151512829757|
||2.5|2|||||0||||0.13140201775795096||||||0|6.943566547879928|0.7217073359689739|||6.061396046141011|5.734246997402522|0.6342823976284719|0.6336151512829757|
||2.5|3|||||0||||0.16146713710107002||||||0|5.526544025946606|0.5719997100788096|||6.061396046141011|6.363823020241544|0.6342823976284719|0.6336151512829757|
||5|4|||||0||||0.1630627560166418||||||0|5.465941566067621|0.6292517961681674|||6.061396046141011|6.3949823437012|0.6342823976284719|0.6336151512829757|
||5|5|||||0||||0.15121588960694818||||||0|5.946394980487452|0.5619933793304382|||6.061396046141011|6.158252951069443|0.6342823976284719|0.6336151512829757|
||5|6|||||0||||0.15401084891264302||||||0|5.826382407864526|0.6119764006943851|||6.061396046141011|6.215227217237116|0.6342823976284719|0.6336151512829757|
||7.5|7|||||0||||0.1452037339205719||||||0|6.220208574069301|0.6042391346714249|||6.061396046141011|6.033331048755924|0.6342823976284719|0.6336151512829757|
||7.5|8|||||0||||0.15914454387639776||||||0|5.6169292119119065|0.5899764006943851|||6.061396046141011|6.318064950674094|0.6342823976284719|0.6336151512829757|
||7.5|9|||||0||||0.1337672633439823||||||0|6.809003949607375|0.6539700699460138|||6.061396046141011|5.786726308696023|0.6342823976284719|0.6336151512829757|
||10|10|||||0||||0.14096608867071322||||||0|6.427238040698302|0.6722687748042205|||6.061396046141011|5.943331200979074|0.6342823976284719|0.6336151512829757|
||10|11|||||0||||0.1520558782903881||||||0|5.909863035725068|0.6155611489140562|||6.061396046141011|6.175449049762362|0.6342823976284719|0.6336151512829757|
||10|12|||||0||||0.13804522269770025||||||0|6.577336280033345|0.7254679113763584|||6.061396046141011|5.880355127362998|0.6342823976284719|0.6336151512829757|
||15|13|||||0||||0.1593875277872177||||||0|5.607349963637053|0.5988069042550429|||6.061396046141011|6.322874413671228|0.6342823976284719|0.6336151512829757|
||15|14|||||0||||0.14179286924942708||||||0|6.385874164853608|0.6175315087812605|||6.061396046141011|5.961017437707929|0.6342823976284719|0.6336151512829757|
||15|15|||||0||||0.1582660700486947||||||0|5.65180702571935|0.633298414937016|||6.061396046141011|6.30063336595312|0.6342823976284719|0.6336151512829757|
||20|16|||||0||||0.1376610733400033||||||0|6.597550992962806|0.6929764006943852|||6.061396046141011|5.872015228446415|0.6342823976284719|0.6336151512829757|
||20|17|||||0||||0.16756663186210696||||||0|5.301108593164985|0.5800526595960295|||6.061396046141011|6.481722963076239|0.6342823976284719|0.6336151512829757|
||20|18|||||0||||0.16348729810331236||||||0|5.4500164738674135|0.6023217243214407|||6.061396046141011|6.403234956351341|0.6342823976284719|0.6336151512829757|

