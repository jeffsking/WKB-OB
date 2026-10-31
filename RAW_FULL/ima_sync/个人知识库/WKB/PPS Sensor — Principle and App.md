---
media_id: "note_3867e2b60070d7dc3f413086d0b0036e_7516855958794537"
extract_status: "ok"
extract_channel: "A"
synced_at: "2026-10-17T18:16:44+08:00"
source_path: "RAW/ima_sync/个人知识库/WKB/PPS Sensor — Principle and App.md"
media_type: 11
extract_method: "RAW-side full body (IMA plugin synced)"
---

# PPS Sensor — Principle and App...

# PPS Sensor — Principle and Application Introduction

以下是英文版会议纪要（已加入会议日期）。

***

**Meeting Minutes**

**Subject:** PPS Sensor — Principle and Application Introduction

**Date:** October 16, 2026 (the recording itself does not state the meeting date; date shown is the record date)

**Duration of recording:** approx. 24 minutes

**Attendees:** PPS China representative (presenter) and buyer team (incl. 王总 and colleagues)

**Purpose:** Technical introduction of PPS capacitive pressure sensors, application cases, and discussion on customization suitability

_(Note: the uploaded transcript is titled "PBS"; the brand is consistently referred to as PPS throughout the discussion.)_

***

**1. Company Background & Partnership**

* Robotics today is still at the application/design-market stage; no closed commercial loop has been achieved .
* PPS's founder started with academic research on tactile sensing for robot hands; the business later evolved into pressure sensors and customized solutions for corporate applications .
* The company began in 1996 and has roughly 30 years of history by this year .
* The earliest product was a single-point sensor used to record surgical operation procedures; many variants were derived from it, including multi-point/array sensors .
* PPS is a small but long-established company. The overseas R\&D team numbers about 20–30 people, based in the UK; many are professors affiliated with universities or research institutes .
* The Chinese entity is **not** a wholly-owned subsidiary — it acts as the local representative/agent: it interfaces with customers, collects requirements, and feeds them back to the UK team, whose response efficiency is low (an email may go unanswered for a month or never) .
* Customer references shown include Kimberly-Clark (金佰利) and P\&G (宝洁); which specific departments use the sensors is not yet clear and would need to be checked with the UK team. Customers do not allow public disclosure of the relationship ("you can't say I'm your customer"), so these are marketing references only .
* Domestic business is conducted under the local Chinese company's name; with authorization, invoicing can be issued by the local entity if trade occurs .

**2. Application Cases**

* **Medical device — endoscope tube:** sensors are embedded segment-by-segment inside a gastrointestinal endoscope tube. The segmented design with gaps is deliberate: when the tube bends, adjacent sensors would otherwise come too close and cause short-circuit or damage. The sensing is used to detect where the tube is bending, stuck, or subjected to excessive force (e.g., during insertion) .
* **Non-invasive breast screening:** the device screens by softness/hardness differences between normal and abnormal tissue. It is not a direct tumor diagnosis but a preliminary screening; abnormal findings would then lead to invasive biopsy .
* Overseas collaboration exists with a medical device company on this. A domestic (Chinese) company recently approached PPS wanting to do non-invasive screening: they first tried temperature-based monitoring (temperature difference between normal and abnormal tissue), but the effect was insufficient because the difference was too small. They are now considering combining their temperature approach with PPS pressure sensing — follow-up is still in progress .

**3. Sensor Principle & Structure**

* The sensor is a thin film: upper and lower electrode layers with a dielectric layer in between (the dielectric behaves like a sponge — it can be pressed and rebound) .
* Under pressure, the microscopic gaps change, which changes capacitance (C) — it is a **capacitive sensor**. The formula links pressure (psi) and gap change to capacitance output .
* Both vertical pressing and bending cause deformation → force → signal output. So the sensor is not exactly like a human hand; it responds to any force that deforms it .
* **Bending limit:** large bending angles are not allowed because of the three-layer structure — bending stretches the outer layer and compresses the inner layer (different arc lengths), creating a risk of delamination or localized damage; the sensor then becomes unusable .
* **Layer bonding:** the layers are joined by adhesive or soldering. The electrode layers are conductive; exact materials vary by sensor type and are part of PPS's internal selection criteria (conductive or non-conductive materials depending on desired characteristics) .
* Slight bending is fine, or external packaging/protection can be added; some material variants can be folded at large angles but at the cost of reduced sensitivity .

**4. Layout & Specifications**

* Layout: upper layer, lower layer, middle dielectric/electrode layer — shown both in plan view and cross-section; discussion noted the upper and lower layers are not quite the same material .
* Range: from highly sensitive versions (e.g., detecting spray/mist) up to a large range of 5 psi. psi (pressure unit) is used because force is applied over an area, not a single point .
* **Spray demo discussion:** the buyer team asked whether the sensor detects the dynamic impact at the moment of spraying or the static load of droplets attached to the surface. The presenter clarified it is mainly the load/pressure from droplets attaching to the surface; the demo shows a sustained reading after spraying stops. In principle, any force that causes deformation outputs data in real time .
* **Sampling frequency:** typically 40–50 Hz per second; higher versions reach 100–200 Hz; smaller/single-point sensors can sample faster; the demo unit is around 100 Hz .

**5. Linearity, Calibration, Drift & Repeatability**

* Ideally, capacitance should increase proportionally (linear) with pressure; in reality the capacitance curve is curved, so a **compensation algorithm** is required — all products of this type use algorithm compensation .
* Different materials (different softness) produce different curves, so algorithms must match each curve; **every sensor has its own dedicated calibration file** .
* **Drift:** all sensors drift; the error is bounded within a spec (e.g., FSR accuracy of less than ±3% full-scale for some products). Example: holding a constant 2 N force, the reading creeps slowly upward, but the drift cycle is very slow — readings remain credible for 1, 2, or 5 minutes of measurement; even pressing for a day and night it won't drift to zero. This is a common issue for all sensors, not just PPS .
* **Creep:** pressing 10 N for 10 minutes, then releasing — after release the sensor returns near zero but may still show \~0.19 before slowly settling back to zero. Industry tolerance values apply .
* **Repeatability (key criterion):** performing the same action at the same location (e.g., pressing 2 N) may output 1.5 N, but if it outputs the same value every time — 99 out of 100 presses within the specified error band — the sensor is judged accurate. Fixed deviations can be compensated by algorithm; if the output varies each time, algorithm compensation becomes very difficult .
* **Why readings differ from electronic scales:** scales use an S-type metal block that concentrates gravity onto a single point, causing microscopic deformation and electrical change; it is single-point, extremely stable, with negligible drift. PPS sensors contain many sensing points averaged via algorithm — a different calibration philosophy. Neither is "inaccurate"; they simply use different reference standards. At customer sites, on-site comparison of the two methods often shows large absolute differences — this is exactly why: the user should always compare within one consistent reference frame (PPS vs. PPS), not against load-cell/electronic devices .

**6. Open Items / Unfinished Discussion**

* The explanation of the **FSR** (full-scale range) accuracy figure was cut off — the transcript ends mid-sentence at approximately 24:00 while discussing the FSR error percentage .
* Which department(s) at Kimberly-Clark (and P\&G) use PPS sensors — to be checked with the UK team if possible .

**Action Items**

1. PPS China to ask the UK team which specific department(s) of Kimberly-Clark use the sensors .
2. Continue follow-up with the domestic non-invasive screening prospect on the combined temperature + pressure approach .

***

如需调整（例如改为中文版、补全与会人姓名或日期）随时说。

以下为会议纪要英文版，已按要求补充会议日期（2026-10-16），并尽量保留讨论细节。

***

**Meeting Minutes: Pressure Sensor Technology & Application Discussion**

**Date:** October 16, 2026

**Topic:** Pressure sensor technology, applications (diaper/rubber band testing, consumer electronics), pricing and customization

**Attendees:** Mr. Wang (customer, hygiene product R\&D/procurement); Supplier representatives (Weida Hong Kong / Weide Suzhou; PPS distributor)

***

**1. Company & Distribution Background**

* The Hong Kong headquarters is called **Weida (伟达)**, and the Suzhou company is **Weide (维易德)**, a wholly owned subsidiary of the Hong Kong parent .
* Asked whether they are the exclusive PPS agent: there is **no other agent in China, only dealers**; their group's branches form a dealer network .
* They are currently building a **dedicated PPS China website** for better external business communication (the current Chinese-language site is hosted in the UK, loads slowly, and relies on auto-translation) .

**2. Product Technology & Features**

* **Multi-level triggering:** unlike ordinary switches that output only a single on/off signal, their capacitive sensor outputs a **dynamic, continuously varying signal**. A trigger threshold can be set (e.g., light turns on only when force reaches a set value), or output can scale with force (e.g., 1–6 LEDs lighting progressively as pressure increases) .
* **Capacitive, solid-state sensor:** claimed higher precision than piezo-resistive types (which have lower sensitivity regardless of manufacturer) .
* **Software demo highlights:**
  * Real-time force mapping with color depth indicating force magnitude (single-point sensor; displayed precision ratio 500:1; example range 220 psi) .
  * Bar/column view and 2D planar view; region selection for analysis .
  * Sample analysis: max pressure in selected region **10.7 psi** with its location, total force, and average pressure; units switchable between **psi, kPa, and Newton (e.g., 5 N / 43.9 kPa)** .
  * **Playback/caching** of time-series recordings of pressing actions .
  * Data export: full **time-axis CSV export with every sampling point**; large data volumes are normally processed with their software rather than by customers doing raw data mining .

**3. P\&G (宝洁) Application Cases**

* **Diapers:** sensors are used to measure pressure at the **leg elastics and waist elastics** (which differ in amount and possibly thickness/size); average and maximum pressure values help judge whether elastic choice/configuration is comfortable for the child. The model they tested is a plain plastic dummy wearing the diaper .
* **Electric toothbrushes:** used to measure peak vibration/impact force during brushing .
* P\&G may use the equipment beyond diaper testing — other R\&D colleagues also use it, so flexibility was important to them .

**4. Power, Size & Physical Limits**

* Direct USB connection; power consumption very low (\~5 V / \~2 A, roughly a few watts; small box size) .
* Standard version is **not wireless**; an integrated **Bluetooth version with a coin battery (5 V, 250 mAh)** exists .
* Sensor **cannot be folded dead-flat; only simple bending** (three-layer structure). The higher-sensitivity element sits inside; the outer layer is just a protective/anti-slip indicator material .

**5. Customization, Development & Production**

* **Basic application-level support is handled locally; any custom development requires coordination with the UK team** — local team can do preliminary evaluation, but detailed design/implementation is finalized by the UK side .
* **Production is in Korea** (moved from UK/US due to labor costs); signal-collection boards can be made in China, partly because their group operates contract-manufacturing factories — currently kept in-house for confidentiality .

**6. Pricing & Business Model**

* Full sensor kit (watch-type/board setup): about **RMB 100k per set; software is free and shared across multiple units** (same software for all hardware purchases) .
* **Gloves: \~RMB 60–70k each; a Bluetooth pair \~RMB 100k+**. The glove is cheaper because it is a **standardized, mature product**, whereas the watch/board unit is a low-volume engineering component with custom calibration, hence more expensive .
* They prefer custom calibration for high-volume standardized goods .

**7. Customer Cases (Electronics & Aerospace)**

* **Shenyang Aircraft (沈飞):** measuring **aircraft cabin door trigger-force thresholds** — too high and crew can't pull the door; too low and it's unsafe; repeated pull tests after integration .
* **Xiaomi, Lenovo:** keyboard typing-force optimization for laptops/mobile devices to improve comfort (hardware is already saturated; companies are seeking new differentiators) .
* **Goertek (歌尔):** smartwatch OEM (supplier to Google); purchased after Google required such testing and for their own research .
* **Head-mounted wearables:** their sensor (model number **6383** mentioned) is embedded in such devices .

**8. Feasibility of Stretchable-Material Application (Key Technical Discussion)**

* Mr. Wang asked whether the sensor could be attached to elastic materials (e.g., PDMS) to convert vertical pressure sensing into a **stretch/tension sensor with positive correlation** to elongation .
* Supplier response:
  * Physically possible **only if the stretchable material also meets the capacitive requirements** — not just the dielectric layer, but the **wiring/electrodes must stretch too**; otherwise only the middle stretches and the sensor doesn't .
  * Analogy: sticking a sticker on a balloon and inflating it — the sticker doesn't grow with the balloon; no signal, or the sensor tears apart .
  * With existing three-layer materials, direct attachment to PDMS-type elastomers is **not feasible** .
  * A fundamental issue: the sensor cannot distinguish whether output comes from **stretching or pressing** (stretching would turn the whole region red / raise the bar chart), so the data becomes ambiguous .
  * Stretchable/tension sensors on the market are mostly **resistive or liquid-electronics based and suffer from unstable data** .

**9. Follow-up Items**

* Launch the **PPS China official website** for better domestic promotion .
* Supplier to further evaluate the stretch-sensing concept; any such development would still route through the UK team .

***

需要调整结构、补充遗漏细节或改成中英对照版，随时说。
