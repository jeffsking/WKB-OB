---
media_id: "word_3867e2b60070d7dc3f413086d0b0036e_bbfc6413661cfc1d71875180494c3282001a693ee6c0644e"
source_file: "WI-63849 Motion mannequin.docx.md"
original_path: "RAW/ima_sync/个人知识库/WKB/Areas/Test Method/成品/TJ/WI-63849 Motion mannequin.docx.md"
extracted: "2026-09-27"
extract_method: "ima-mcp fetch_media_content"
extract_status: "ok"
clean_rules: "v2: dead-image-link->text(alt kept); repeat-digits->compressed"
processed: "2026-09-27"
---

# WI-63849 Motion mannequin.docx.md

8
WI-63849

Motion mannequin

仪器编号：

最新版本号：第0版         修订日期：2024年2月20日

实验目的：

本试验用于模拟尿裤产品使用状态下，基于人体湿态和干态整体产品漏尿性和合身性两部分的研究。

配制溶液：

0.1g牛黄酸胆酸钠粉末加入1L生理盐水中用磁力搅拌器搅拌5-10min后加入液体贮存容器中，并将水浴锅打开加热液体至37±1℃。

校准：

每次测试开始前都要润洗管路和校准液体。

润洗管路：

# 1.在Mannequin下方放置液体收集容器，收集流出的液体。

[图片: BMG-FactoryTalk View SE Client April 11, 2024 Kimberly-Clark 3:56:15 PM Mannequin Lab BMG1 BMG1 BMG1 BMG1 Motion LAB Test Interface Study Manager Configuration Manager Configuration Stopped Pressure Switch BMG1 Saline Pump Station 1 0.00 mLM Closed Fluid Delivery BMG1_SV1201 BM01 LLS1100 -0.02% BM01_LLS1101 -0.02% BM01_LLS1102 -0.02 % Stopped BM01 Drive 0.00 RPM Stand Mannequin Position Current Step Total Run 0 Min Sec Elapsed Time Time Remaining Request Number Test Select Run Current Run Current Step Wait Wait Time (S)5 Inactive Notes Code Gender Position Leaked Size Location Dry Wt Wet Wt Insult Walk Station # Speed 30.0 Inactive 0.00 0.00 N/A N/A Station 1 Wait Wait Time (S)30 Inactive Stand Station # Inactive Walk Station # Speed 30.0 Inactive Wait Wait Time (S)120 Inactive Current User: Waiting for Alarm Events.. V= MOSAICICNTMAP05M Clear Clear Al AThe automatic renewal of activations is enabled but will not be performed due to the inability to connect to the Rockwell Web Service. Please verify your connection to the internet and contact technical support if the problem persists]
图1

# 2.打开软件，进入测试界面（图1）。

# 3.打开软件点击左上角“Fluid Delivery” （图2）进入参数调整页面（图3）。

[图片]
# 4.Station Delay设置为10s；Flow Rate设置为15ml/S；Volume设置为300ml；点击白色激活窗口按钮勾选工作站；（图3矩形处）点击按钮开始润洗。

# 5.为减少测试误差，润洗后的液体不能再次使用。

[图片: AMG1 Saline Delivery 5 Start Dela Sec Se Station Delay:10 Flow Rate 15.0 mL/Sec 70.0 Volume mL Enable Station 1 Calibration 1.00 0.8-1.2]
[图片: Stopped Pressure Switch BSG1 Saline Pump Fluid Delivery 0.00 mLM]
图2

液体校准：

# 1.在Mannequin下方放置液体收集容器，收集流出的液体。

# 2.天平上放置烧杯清零备用。

# 3.点击左上角“Fluid Delivery” （图2）进入参数调整页面（图3）。

# 4.Station Delay设置为10s；Flow Rate设置为15ml/S；Volume设置为70ml；点击白色激活窗口按钮勾选工作站；点击按钮开始校准。

# 5.将工作站流出的液体倒入天平称重记录。

# 6.液体校准波动控制在±3%以内。

# 7.如液体波动范围在±3%以外，调整界面底部的液体传输参数Calibration（图3椭圆处）。

# 根据公式 \frac{\mathrm{T}\mathrm{a}\mathrm{r}\mathrm{g}\mathrm{e}\mathrm{t}\mathrm{ }\mathrm{W}\mathrm{T}-\mathrm{A}\mathrm{c}\mathrm{t}\mathrm{u}\mathrm{a}\mathrm{l}\mathrm{ }\mathrm{W}\mathrm{T}}{\mathrm{T}\mathrm{a}\mathrm{r}\mathrm{g}\mathrm{e}\mathrm{t}\mathrm{ }\mathrm{W}\mathrm{T}} 计算出结果，从校准区域数值中增加或扣除结算结果。如果校准数值接近0.8或1.2，则需手动校准蠕动泵。

# 8.点击软件界面顶端的“BSG1 Configuration”（图4）进入界面点击“Remote PLC Control”（图5）将蠕动泵改为手动模式。

[图片: Pump Control Mode Remote PLC Control]
[图片: Mannequin Lab BSG1 BSG1 BSG1 Test Interface Study Manage Configuration]
# 9.点击“BSG1 Test Interface”按钮（图4）返回软件主界面。

[图片]
[图片]
[图片]
# 10.点击Station 1 Valve按钮（图6）转入设置界面（图7），点击Operator Mode按钮，再点击Open Valve，当开启时可以听到设备相关提示音；然后点击关闭界面。

[图片: BSG1_SV1201 Closed]
[图片: Station 1 Closed BSG1_SV1201 BSG1_LLS1400 -0.03 %]
# 11.在Mannequin工作站下方放置液体收集容器，收集流出的液体。

# 12.检查蠕动泵设置，选择管路尺寸查看是否为17（图8），确认后选择管路校准点击启动进行液体校准（图9）。

[图片: MASTERflEx® L/S® 管路校准 启动 200.000mL 900.0 mL/min 清除 退出 17 5 13]
[图片: MASTERFLEX® L/S® 管路尺寸 最大 尺寸 流量 mL/min 1650.2 15]
# 13.从工作站1收集液体进行称重，并把实际注液量输入到管路校准中，重复步骤直到误差达到±1%以内（图9）。

# 14.将要测试产品所需的注液量输入到容积中（图10）手动校验完成。

[图片: MASTERFLEX® L/S® Remote IP 10.21.222.90 MAC E8:EB:1B:8B:64:CD 900.0 mL/min Tube 17 c]
[图片: MASTERFLEX® L/S® 容积 mL 0.0 退出]
[图片]
# 15.点击Station 1 Valve按钮（图6）转入设置界面（图7），点击Operator Mode按钮，点击Close Valve按钮，当关闭时可以听到设备相关提示音。

[图片: 吕2]
# 16.点击Program Mode按钮；然后点击关闭界面。

# 17.点击软件界面顶端的“BSG1 Configuration”（图4）进入界面点击“Remote PLC Control”（图3）将蠕动泵改为自动模式（图11）。

# 18.校准流出的液体可以倒回液体贮存容器继续使用。

漏尿性测试：

测试前的准备：

# 1.在测试界面点击“BSG1 Study Manager”，进入设置界面（图12）。

[图片: Clear Study Select Run Current Run Save Select Phase Code Gender Position Recirculate Flow Rate (mL/s)15.00 Wait Time (s) 0 N/A NIA Station 1 2 Select Phase Crawl Station # Speed 30.0 0 N/A NIA Station 2 Select Phase Insul Station Flow Rate (mL/s) 15.00 On Volume (mL)70.00 Wait Time (s) 1 Leak Detector 0 N/A N/A Station 3 Select Phase Crawl Station # Speed 30.0 0 N/A N/A Station 4 5 Select Phase Insul On Station Flow Rate (mL/s)15.00 Volume (mL) 70.00 Wait Time (s)2 Leak Detecto 0 N/A Station 5 N/A 6 Select Phase 1 Craw Station # Speed 30.0 0 N/A Station 6 N/A 7 Select Phase Insult Station Flow Rate (mL/s) 15.00 On Volume (mL)70.00 Wait Time (s)2 Leak Detector Station 7 0 N/A N/A Select Phase Loop Step Number 2 0 N/A N/A Loop Count Station 8 0 9 N/A N/A Select Phase Insult Flow Rate (mL/s) 15.00 On Station 9 Station Volume (mL)70.00 Wait Time (s) 30 Leak Detector 0 N/A N/A Station 10 Select Phase 10 Run Complete 0 N/A N/A Station 11 0 Station 12 N/A N/A]
图12

# 2.点击“Select Phase”选项在转入界面（图13）中依次选择所需测试的动作组合。

[图片: Select Phase Cancel Select Phase Wait Walk Message Crawl Insult Sit Loop Motion Start Lay Recirculate Motion Stop Stand Complete Delete Phase]
# 3.选择完成后点击“Cancel”关闭。

# 4.点击“BSG1 Test Interface”按钮返回软件主界面。

样品的准备：

# 1.产品称重记录在“Dry Wt”中（图14）。

[图片: Current Step Total Run 0 Sec 0 Min Time Remaining Elapsed Time Request Number Test_ Select Run Current Run Current Step Recirculate Flow Rate (mL/s) 15.00 Wait Time (s) Inactive Code Size Notes Gender Position Leaked Location Dry Wt Wet Wt Insult Craw Station # Speed 30.0 Inactive 0.0 N/A N/A 0.0 Station 1 On Insult Station Flow Rate (mL/s)15.00 Volume (mL)70.00 Wait Time (s)1 Leak Detector Inactive Craw Station # Speed 30.0 Inactive Insult Station On Flow Rate (mL/s)15.00 Volume (mL) 70.00 Wait Time (s)2 Leak Detector Inactive Craw Station # Speed 30.0 Inactive On Insult Station Flow Rate (mL/s)15.00 Volume (mL)70.00 Wait Time (s)2 Leak Detector Inactive Loop Step Number 2 Loop Count 2 Inactive Insult Station Flow Rate (mL/s)15.00 On Volume (mL)70.00 Wait Time (s)30 Leak Detector Inactive 10 Run Complete Inactive]
# 1.将产品穿戴在Mannequin上。

# 2.穿戴完成后用一根手指划过腿部皮筋和折页皮筋位置，确保产品服帖Mannequin。

测试步骤：

# 1.在测试软件界面上按下运行按钮（图15）。

[图片: BCC Leak Locations 16 15 Close Station 1 14 13 12 11 O 10 9 7 8 6 5 3 4 2 1 17 (Outer Cover 2 Crotch Right Leg 1 Crotch Left Leg 4 3 Front Right Leg Front Left Leg ← s Back Right Leg Back Left Leg 7 8 Lower Right Side Lower Left Side 10 15 Upper Rlght Side Front Center Waist Upper Left Side 12 11 Front Right Waist 16 Rear Center Waist Front Left Waist 14 13 Back Right Wais 17 Outer Cover Back Left Wais]
# 2.观察Mannequin上产品的漏尿，当漏尿发生时，在“Data Entry Section”中的“Location”栏记录漏尿位置（图16）。

# 3.完成后，点击“Close”按钮（图16）。

# 4.脱下产品称重并在“Wet Wt”中记录产品湿重（图14），

[图片: 个]
# 5.运行结束时，点击按钮保存数据和切换下一轮测试。

导出报告：

# 1.打开桌面“Study Builder&Report”文件夹，选择“Mannequin Report.xlsm”文件打开。

# 2.Excel底部选择“Main”工作表（图17）。

[图片: Version 2.5 HMI: CNTM323ICW2 Run Report BSG1 Systems Request Number Trypockrt-240218-LYH Report Generic Connections Ref]
# 3.点击“Refresh Data Connections”刷新后，在“Request Number”中选择相对应的报告编号，点击“Run Report”(图17)。

# 4.Excel底部选择“Report”工作表，查看或导出数据。

合身性测试：

测试前的准备：根据测试者需求进行参数设置，此部分与漏尿性测试前准备的部分一致，请查看上文。

样品的准备：

# 1.产品称重记录在“Dry Wt”中（图18）。

# 2.用马克笔标标识出产品两侧耳贴外轮廓线（图19；在产品前部中心位置划线，在中心线左右两侧划出耳贴需要贴的位置（图20），不同产品型号耳贴粘合建议值见下表，Pants产品跳过此步骤。

|Mannequin Name|Mannequin Size|Tab Spacing|
|---|---|---|
|Koopa|Step 2|20 mm|
|Yoshi|Step 3, Low end of step 4|19 mm|
|Mario|Step 4|22 mm|
|Luigi|High end of step 4, Step 5|30 mm|
|Kirby|High end of step 4|38 mm|

[图片]
[图片]
# 3.将产品穿戴在Mannequin上。在Mannequin上划线标识处前后腰围位置；如果产品前后 腰围超出了Mannequin顶部，则不用划线。

# 4.穿戴完成后用一根手指划过腿部皮筋和折页皮筋位置，确保产品服帖Mannequin。

# 5.拍照记录Mannequin前部、后部、左侧，使用黑色背景板，将Mannequin扭转到相对应位置拍照。

[图片: 6 8 9 U 7 mm]
# 6.标识Ear Roping：在产品两侧耳贴最容易成束的位置垂直划线（目前建议在耳贴基部CD中心位置划线），该线需和耳贴边缘平行，该线用于运动前后的Ear Roping指标测量（图21）。

[图片]
# 7.标识Panel shift：先辨识出Inner Cover side panel的位置，顶部的Outcover panel可能需要翻折下来以便标识；用马克笔在产品外侧上Inside panel顶部和底部标识处一条10mm垂直的线，如产品外侧不能完全覆盖，可标记在Mannequin上（图2红色部分）；测试完成后，用马克笔追踪标记Inside panel顶部和底部新的位置，测量两条线之间的距离（图2绿色部分），测量时保持直尺水平。

# 8.测量前部下坠尺寸：产品前部腰围顶端到Mannequin顶端的距离（图23）该尺寸需在测试前后都进行测量。

[图片]
[图片]
# 9.测量候补下坠尺寸：产品后部腰围顶端到Mannequin顶端的距离（图24）该尺寸需在测试前后都进行测量。

[图片]
[图片]
# 10.测量裆部下坠尺寸：从Mannequin腿部底部位置到尿裤最低点的距离，需要两把直尺，一把平行贴在腿部底部，另一把测量第一把支持界定的水平线到尿裤最低点的距离（图25）该尺寸需在测试前后都进行测量。

# 11.评估LegGap：测试完成后，将Mannequin的两腿撇开并锁定，观察Mannequin下部左侧和右侧腿部位置，如果两侧中任意一侧可观察到间隙，记录“存在腿部间隙”（图26）。

[图片: 020 o 5 RM Hu]
# 12.测量Tab-to-Tab:使用马克笔标识出耳贴中部边缘位置，使用直尺测量两个耳贴中间中心边缘的距离（Hook中心到Hook中心），该尺寸需在测试前后都进行测量（图27）。

测试步骤：

# 1.在测试界面点击“BSG1 Study Manager”进入设置界面（图28）, 点击“Select Phase”选项在转入界面（图29）。

# 2.根据测试者的需求在图29中进行运动组合设定，选择完成后点击“Cancel”关闭；在图28中进行注液量、运动时长、运动间隔的设定。

# 3.设置完成后点击“BSG1 Test Interface”按钮返回软件主界面。

# 4.在测试软件界面上按下运行按钮开始测试。

# 备注：此测试主要针对Diaper产品，如需测试pants产品请与测试提出者进行讨论。

# 此测试不涉及到FIA；如涉及到FIA的进一步测试，请与测试提出者进行讨论。

图28

导出报告：根据测试者需求，手动记录运动后位置，提供运动前后位置和距离尺寸。

注意事项：

# 1.穿戴产品到mannequin时，操作锁定腿关节时注意夹手。

# 2.拿取mannequin假体时注意避免砸伤。

# 3.测试开始后离开mannequin工作范围，避免磕碰。

参考文稿：

TTM-00313-8 Mannequin Wet and Dry Motion Fit Test

Urine Analog,  # WI-33165

Operation of Mannequin Lab Rockwell System Platform,  # WI-38044

Fit Image Analysis (FIA) Mannequin Procedure, # WI-45237

Motion Mannequin Full System Calibration, # WI-45322

Mannequin Wet and Dry Motion Fit Test Data Sheet,  # FORM-51078

Mannequin Lab Study Builder Tool,  # WI-38046

FIA Mannequin Procedure, WI-45237

External Reference(s) (if applicable):

Mannequin Fit Measurment Overview:

https://kimberlyclark.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=dcde1110-695c-45ab- b69a-ac05010b0286

Standard Motion Script Building:

https://kimberlyclark.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=67686567-c8ce-4db2- 8adb-abf1015f4cab

Custom Motion Script Building:

https://kimberlyclark.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=a7673ead-2e88-4f64- bf08-abff012ce0f4

