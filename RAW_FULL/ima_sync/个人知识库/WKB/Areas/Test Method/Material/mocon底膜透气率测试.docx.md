---
media_id: "word_3867e2b60070d7dc3f413086d0b0036e_56f26c0a3baf0d95192447ac3f03ba61001a693ee6c0644e"
source_file: "mocon底膜透气率测试.docx.md"
original_path: "RAW/ima_sync/个人知识库/WKB/Areas/Test Method/Material/mocon底膜透气率测试.docx.md"
extracted: "2026-09-27"
extract_method: "ima-mcp fetch_media_content"
extract_status: "ok"
clean_rules: "v2: dead-image-link->text(alt kept); repeat-digits->compressed"
processed: "2026-09-27"
---

# mocon底膜透气率测试.docx.md

8
WI-

Mocon底膜透气率试验

仪器编号：

最新版本号：第0版         修订日期：2024年1月18日

实验目的：

本试验用于测试底膜的透气性能。

校准：

当设备长期不使用或测试数据出现明显差异时需要进行校准。校准部分有Cal C校准和标准膜校准两部分。

Cal C校准：

# 1.设备开机，连接软件（连接步骤同下方测试步骤7）。

[图片]
# 2.点击菜单栏图标，将A-F依次修改（矩形框）。Test Mode选项选择“Continuous”；Exam Minutes选项修改为“5”；修改Material TD（校准日期）；Cal Mode选项选择“Active Cal C”；点击Stsrt All Tests开始校准A-F通气腔体。见下图：

[图片: 回 x MOCON PERMATRAN-W?101K Control Test B D E C Module 1 Module 2 Module 3 Module 4 Module 5 Module 6 Module 7 Module 8 Module 9 Module 10 00:00:00 Cell Parameters Test Control Parameters Sample Parameters Default Method Method Test Mode Continuous Tes 20240112-TEST-1 Material ID Number of Cycle Area/Cel cm2 Exam Minutes Test Numbe Convergence Thickness mi Period Enter Thickness List Cal C Mode Active Cal C Start All Tests Advance Test Abort Test Select Reporting Units Tes Star]
[图片]
# 3.点击菜单栏图标，分别依次缓慢旋转A-F旋钮同时查看Raw Counts数值，校准数值为60±2。Cal C校准开始后每个腔体旋钮只有5分钟调整时间，且调整过程设备与软件有延迟显示；此校准步骤依赖手法和经验，建议此项校准联系设备厂家或在设备厂家指导下进行校准调试。注：腔体水温尽量达到37.8℃，以减少对Raw Counts数值的影响。如温度不够可在水槽注水后待机1-2小时加温平衡一下。

# 4.校准完成后，分别依次选择	A-F图标，一直点击“Advance test”，直到A-F图标变成白色即可。

[图片: MOCON PERMATRAN-W?101K Diagnostics - Module 1 Module 5 Module 2 Module 3 Module 4 Module 6 Module 7 Module 8 Module 9 Module 10 2 0 Enabled Module Hour Sensor Hours B Senso Current Value Units Setpoint A Calibrate Temperature 37.77 . 37.8 -2.295794e+00 8.177570e-01 Auto ▼ Tune Barometer 773.15 2.756881e+01 mmHg 1.319084e+00 ▼ Auto Tune 115.49 SCCM Flow Rate -2.860018e-02 2.496872e+00 Auto Tune Permeant Sensor Parameters 60.12 Small Filter 16.00 0.50 Auto Tune Raw Counts Large Filter Note: All values are Read Only; The module is active Print Table Digital I/O Status Module Configuration System Setup Save Calibrations]
[图片]
标准膜校准：

# 1.捏住标准膜黑色标签部分从保护盒中取出（见右图），标签上“this side to carrier gas”标识一面向下水平放置到测试仓平台，拿取过程中手不能触碰标准膜表面，不能磕碰标准膜，然后按测试步骤1-9进行校准。

# 2.测试完成后把标准膜数据输入到Excel表格中（矩形框），标准膜数据偏差不能大于19%（椭圆框），否则需要重新校准。数据输入后Excel自动计算出校准因子（划线部分）。

[图片: Enter Ref film label valtEnter Ref film measured value% of deviation A 11006 11014.7 100.08% B 10498.37 93.46% 11233 C 11455.44 11581 98.92% D 10887.92 11987 90.83% E 11678 11105.62 95.10% F 11107 10434.79 93.95% Min % of deviation Spread Max% of deviation 100.08% 90.83% 9.25% A Calibrate to this value for cell 11539 4.76% All cells will be adjusted]
[图片]
# 3.点击软件菜单栏图标，把校准因子输入到“Expected TR”中，在“Comments“中输入校准日期编号，点击“Colibrate”完成校准。

[图片: x MOCON PERMATRAN-W?101K Calibrate Module D B C Module 1 Module 2 Module Module 4 Module 5 Module 6 Module 7 Module 8 Module 9 Module 10 00:00:00 Materia Values Factors Material ID Measured TR 1.152206 Current Gain Sample Type Expected TR Date/Time Last Calibrated Thickness SCCM Flow Rate 1/12/2024 10:43:34 AM Comments Clear Calibration Calibrate]
样品的准备：

# 取样：

[图片: 1]
# 取样底膜时，应避开破裂、褶皱、污染处。将底膜平整的铺在取样垫板上，用取样模快压住底膜后用篆刻刀按模快内外轮廓进行裁取，如下图：

[图片: 前]
测试前准备：

[图片: 注]
[图片: 02 压力表 0.1耐 03 10 10E P Wa 20 04 5 司 2211816]
# 1.查看气瓶剩余容量，容量小于3kg（图一右）不能进行测试，分压阀压力调至25PSI （图一左），设备阀门压力为15PSI（图二），且所有气体铜管接口处不可弯曲（如图二标红处）。

# 2.设备启动顺序为：气瓶总开阀门→分压阀门→设备阀门→设备电源开关→电脑软件。

# 3.操作平台A-F共6个通气腔体旋钮不可随意旋转扭动（见图八标红处）。

测试步骤：

# 1.打开设备保护壳，逆时针旋转松测试仓固定紧螺栓打开上锁卡扣，将测试仓固定螺栓取下（图三、图四）。

# 2.捏住水槽两侧小耳朵，将水槽轻轻取下（图五标红处），轻轻水平放置桌面，不能磕碰、挤压、触碰水槽底部薄膜（图六）。

[图片]
[图片]
[图片]
[图片: -]
[图片]
[图片: - 0]
图三

图四

图五

图八

# 3.将采取好的底膜样品平铺到测试仓平台的黑色垫片上，测试面向上，均匀的盖住垫片（图七）。

# 4.把水槽水平放到测试仓平台上，操作者需与测试仓平台水平平视，不能磕碰水槽底部薄膜。水槽箭头标识面向操作者，在测试仓平台上不能旋转扭动水槽。

# 5.用注射器补加37℃纯水至距水槽平面5mm处。

# 6.盖上测试仓固定螺栓（固定螺栓上箭头标识面向操作者）并锁好卡扣。顺时针旋拧螺栓锁紧，旋拧螺栓时为保护注水槽底部薄膜，不要大力旋拧。在螺栓向下拧不动时稍微带一点点力度即可。

[图片: MOCON PERMATRAN-W?101K Diagnostics 0 - Module 1 Module 2 Module 3 Module 4 Module 5 Module 6 Module 7 Module 8 Module 9 Module 10 0 0 Module Hours Sensor Hours ☑Enabled B Sensor Units Setpoin A Calibrate Current Value 37.71 37.8 Temperature -2.295794e+00 8.177570e-01 Auto Tune ▼ 773.58 Barometer mmHg 2.756881e+01 1.319084e+00 ▼ Auto Tune -0.25 SCCM Flow Rate -2.860018e-02 2.496872e+00 Auto Tune Permeant Sensor Parameters 0.50 Auto Tune Raw Counts 12.44 Small Filter 16.00 Large Filter Digital I /O Status Module Configuration Print Table Save Calibrations System Setup]
# 7.打开设备电源，打开电脑软件，点击菜单栏图标，输入密码：password，点击🆗，弹窗后再次点击🆗；勾选Enabled选项连接设备（见下图）。

# 8.点击菜单栏图标，修改窗口右侧Material TD，（例：20240118-产品编码）；查看Cal C Mode选项是否为Use Last Cal C，此选项选错，只能重新校验Cal C后再进行测试！（见下图椭圆部分）

# 9.如需测试6个以下的数据，依次点击与样品所在腔体同编号的按钮，然后点击Start Test开始单个测试（见下图矩形部分）；

# 如需测试全部6个数据，则需点击Start All Test开始全部测试（见下图箭头标识）。

[图片: 回 x MOCON PERMATRAN-W?101K Control Test 0 B D E F C Module 1 Module 2 Module 3 Module 4 Module 5 Module 6 Module 7 Module 8 Module 9 Mo dule 10 00:00:00 Cell Parameters Test Control Parameters Sample Parameter Default Method Method Test Mode Convergence By Cydes Test 20240112-TEST-1 Material ID Number of Cycle Area/Cel cm2 Exam Minutes 10 Test Numbe Convergence Thickness mi ▼ Period Enter Thickness List Cal C Mode Use Last Cal C Start Test Start All Tests Advance Test Abort Test Select Reporting Units]
# 10.测试完成后，关闭顺序为：先断开设备与软件连接→关闭软件→关闭设备电源→设备阀门→分压阀门→气瓶总阀门。

导出报告：

[图片]
点击菜单栏图标，将“Report Options”选项中两项全选，点击Print Report保存报告。

[图片: x MOCON PERMATRAN-W?101K Single Test Report D Module 1 Module 2 Module 3 Module 4 Module 5 Module 6 Module 7 Module 8 Module Module 10 00:00:00 Material Id:20240112-TEST-1 Test Number:<unspecifed> Using Method: Default Method,Calibrated: 1/12/2024 10:43:34 AM MODULE INFORMATION CELL A INFORMATION Module 1,Serial Number: Sample Type Film:10 cm2,1mi MK_00002 Setup Name: Default Setup Test Mode: Convergence By Cycles Temp Setpoint/Actual Auto: 37.8/37.7℃ Control Params Min 4 Cycles 10 Barometric Pressure: Auto:771.45 mmHg ExamMinutes: Cal C Mode: Use Last: 15455.35 Flow Rate Auto:0.00 SCCM Conditioning Disabled Cal C Flow Rate: 109.11SCCM Cycles Complete: Not Available Ambient Temp: Manual:23.0 ℃ Current Status: Idle Started Testing: Not Started Elapsed Time: Not Available TEST RESULTS IN SELECTED UNITS Transmission Rate Not Available gm/[m2-day Permeation: Not Available gm-mil/[m2-day OPERATOR COMMENTS: (Press Ctrl+Enter to start a new line Save Comment Report Options: Print what? Export Repor Select Report Parameters Indude Chart in Report Print this test Incude Data Points in Report Print all completed tests for this module Print Report Save Options Setting]
