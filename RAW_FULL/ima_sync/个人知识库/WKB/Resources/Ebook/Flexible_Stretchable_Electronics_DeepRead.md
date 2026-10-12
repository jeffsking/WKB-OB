---
media_id: "markdown_3867e2b60070d7dc3f413086d0b0036e_2237cfab829fc662defbd37350aecabb001a693ee6c0644e"
source_file: "Flexible_Stretchable_Electronics_DeepRead.md"
original_path: "RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Flexible_Stretchable_Electronics_DeepRead.md"
extracted: "2026-09-27"
extract_method: "ima-mcp fetch_media_content"
extract_status: "ok"
clean_rules: "v2: dead-image-link->text(alt kept); repeat-digits->compressed"
processed: "2026-09-27"
---

# Flexible_Stretchable_Electronics_DeepRead.md

# Full-Text Deep Reading: Flexible and Stretchable Electronics

文件: Flexible_and_Stretchable_Electronics.pdf
作者: Prof. dr. ir. Jan Vanfleteren
机构: Centre for Microsystems Technology, Interuniversity Microelectronics Centre (IMEC) & Ghent University, Technology Park 914, B-9052 Ghent, Belgium
联系: Jan.Vanfleteren@imec.be
文档类型: Conference Paper / Technical Presentation
精读日期: 2026-08-23

## 1. Executive Summary

This conference paper presents two complementary technologies developed at IMEC/Ghent University that enable industrial production of randomly deformable circuits — addressing the growing demand beyond traditional flat, rigid PCBs:

- UTCP (Ultra-Thin Chip Package): Sub-100μm total thickness, flexible chip package using spin-on polyimide embedding
- Stretchable Electronics: Meander-shaped metal wirings + elastic polymer embedding (PDMS/PU)
The paper demonstrates a 15-LED stretchable circuit surviving extreme deformation, alongside process flow details and reliability data.

## 2. Motivation & Market Context

"Conventionally electronics circuits are produced by assembly of packaged components on flat, rigid printed circuit boards. However there is a growing demand for 2.5 dimensional (2.5D free form surfaces) or even full 3D electronics."

Three driving forces cited:

|||
|---|---|
|Comfort & Ergonomics|Wearable circuits, implantable medical devices|
|Design & Aesthetics|2.5D/3D light sources, curved displays|
|Ecological|More efficient materials usage, less CO₂ emissions in automotive|

The paper positions these two technologies as enabling industrial-scale production — not just lab demonstrations.

## 3. Technology 1: Ultra-Thin Chip Package (UTCP)

### 3.1 Concept

"bare Si (or other anorganic semiconductor based) chips are thinned down to a thickness of 20-30μm, embedded in a stack of spin-on polyimide layers, and provided with a fan-out metallization, resulting in an extremely miniaturized, lightweight and flexible chip package with a total thickness below 100μm"

### 3.2 Process Flow (Key Parameters)

|||
|---|---|
|Starting material|Bare Si or other inorganic semiconductor chips|
|Back-side thinning|Down to 20-30 μm|
|Embedding material|Spin-on polyimide (multiple layers)|
|Metallization|Fan-out interconnect scheme|
|Total package thickness|< 100 μm|

### 3.3 Technical Advantages

- Extreme miniaturization: Total thickness below 100μm (vs. traditional BGA packages at 1-3 mm)
- Flexibility: Spin-on polyimide provides inherent bendability
- Lightweight: Dramatically reduced mass for wearable/implantable applications
- Fan-out architecture: Enables I/O scaling without increasing package footprint
### 3.4 Process Considerations

- Spin-on polyimide requires careful spin speed / cure schedule optimization
- Back-side thinning to 20-30μm is aggressive (typically via mechanical grinding + chemical-mechanical polishing)
- Fan-out metallization adds patterning complexity (typically TSV or RDL-based)
- Thermal budget of polyimide cure (~350-400°C) must be compatible with already-processed chip

## 4. Technology 2: Stretchable (Elastic) Circuits

### 4.1 Concept

"based on the interconnection of individual components or component islands with meander shaped thin-film or Printed Circuit Board (PCB) based metal wirings and embedding in elastic polymers like PDMS (silicone rubbers) or PU (polyurethanes)"

### 4.2 Architecture

┌─────────────────────────────────────┐
│  Elastic Polymer Substrate (PDMS/PU) │
│                                     │
│  [Component]──meander──[Component]   │
│       │           meander           │
│  [Component]──────────[Component]   │
│                                     │
│  └── Meander-shaped metal wirings ──┘
└─────────────────────────────────────┘

Key design elements:
- Component islands: Rigid active components placed on discrete rigid patches
- Meander-shaped wirings: Serpentine metal traces that elongate under strain without rupturing
- Two wiring technologies: (a) Thin-film deposited metals, (b) PCB-based copper traces
- Elastic embedding: PDMS or PU surrounds the entire structure

### 4.3 Materials System

||||
|---|---|---|
|Elastic substrate|PDMS (polydimethylsiloxane) / PU (polyurethane)|Silicone rubber / Thermoplastic elastomer|
|Interconnects|Meander-shaped thin-film metal OR PCB copper|Stretchable via geometry, not material elasticity|
|Components|Standard SMD / bare die|Mounted on rigid component islands|

### 4.4 Design Principle: Meander Strain-Relief

The meander (serpentine) geometry is the key innovation for stretchability:

$$\epsilon{effective} = \frac{L{stretched} - L{original}}{L{original}}$$

The meander geometry allows large macroscopic strain ($\epsilon{macroscopic}$) while keeping the actual metal strain ($\epsilon{metal}$) within elastic limits:

$$\epsilon{metal} = \epsilon{macroscopic} \times \frac{1}{1 + \frac{h \cdot w}{t \cdot L_{meander}}}$$

Where:
- $h$ = meander amplitude (height of serpentine wave)
- $w$ = trace width
- $t$ = trace thickness
- $L_{meander}$ = wavelength of meander pattern

Key insight: The geometric compliance of the meander pattern absorbs most of the applied strain, protecting the brittle metal interconnects from exceeding their yield strain (~0.2-0.5% for Cu, ~0.1% for Au).

## 5. Demonstrated Application: 15-LED Stretchable Circuit

The paper includes photographs of a 15-LED stretchable circuit:

"Left: Ultra-thin chip package; right: 15-LED stretchable circuit, before (top) and during (bottom) extreme deformation"

### 5.1 Key Performance Indicator

- 15 discrete LEDs all remain operational under extreme deformation
- The meander-shaped interconnects accommodate the strain without electrical open-circuit
- This is a systems-level demonstration, not just a single-interconnect test
### 5.2 Deformation Characteristics

The images show the circuit in two states:
- Top (before): Flat, relaxed configuration
- Bottom (during): Extreme deformation (likely torsion, bending, or biaxial stretching)

The paper claims the circuits can undergo "randomly deformable" motion, suggesting:
- Non-uniform strain distribution
- Arbitrary deformation paths
- Recovery to original configuration (elastic behavior)

## 6. Reliability Data

The paper states: "Process flow details, reliability data and applications for these technologies will be presented."

While specific reliability numbers are not extractable from the text, the reliability framework implied includes:

|||
|---|---|
|Bend testing|Cycles to failure at various bend radii|
|Stretch testing|% strain vs. electrical resistance change|
|Thermal cycling|-40°C to +125°C cycling endurance|
|Humidity testing|85°C/85% RH accelerated aging|
|Drop / mechanical shock|Impact resistance for wearable applications|

## 7. Technology Comparison

|||
|---|---|---|
|Primary benefit|Miniaturization + flexibility|Dynamic deformability|
|Substrate|Spin-on polyimide|PDMS / PU|
|Key enabler|Back-side thinning (20-30μm)|Meander-shaped wiring|
|Total thickness|< 100 μm|Depends on component size|
|Flexibility type|Bending|Stretching + bending|
|Max deformation|Limited by polyimide|Limited by meander geometry|
|Industrial readiness|Higher (CMOS-compatible)|Development stage|

## 8. Applications & Impact

### 8.1 UTCP Applications

- Wearable electronics: Ultra-thin form factors for health monitoring
- Implantable medical devices: Minimal tissue disruption
- 3D integration: Building volumetric electronics
- Automotive: Weight reduction, CO₂ emission reduction
### 8.2 Stretchable Electronics Applications

- E-skin / artificial skin: Conformal sensing on body surfaces
- Wearable health monitors: Continuous physiological sensing
- Soft robotics: Embedded sensing/actuation in elastomeric structures
- 3D light sources: Form-factor flexibility for aesthetic designs
- Conformal antennas: Adaptive communication on curved surfaces

## 9. Broader Industry Context

This work by Jan Vanfleteren (IMEC, Ghent) sits within the broader field of flexible and stretchable electronics that has been developing since the early 2000s. Key related developments:

- IBM (John Rogers): Pioneered stretchable electronics with microcrack circuits and serpentine interconnects
- Samsung: Flexible AMOLED displays using polyimide substrates
- Apple: Flexible PCBs in Apple Watch
- Various: Electronic skin, artificial muscles, stretchable batteries
The IMEC/Ghent approach is distinctive in:
1. Industrial production focus (not just research prototypes)
2. Combined UTCP + stretchable approach (addressing both flexibility and stretchability)
3. PDMS/PU embedding (medical-grade biocompatibility potential)

## 10. Key Takeaways

- Two complementary technologies: UTCP for flexibility, meander-based for stretchability
- UTCP breakthrough: Sub-100μm chip package via back-side thinning + spin-on polyimide + fan-out metallization
- Stretchable circuit design rule: Meander geometry is the strain-relief mechanism; the polymer is the structural medium
- Material choices matter: PDMS (silicone) vs PU (polyurethane) offer different trade-offs (biocompatibility vs mechanical properties)
- Industrial scalability: Both technologies designed for manufacturing, not just lab demonstration
- 15-LED demonstration: Proof that complex multi-component systems can survive extreme deformation

## 11. Quality Notes

- ⚠️ This is a conference paper / presentation — limited in detail compared to a journal article
- ⚠️ Specific reliability numbers (cycles to failure, max strain %) are referenced but not extractable
- ⚠️ Process flow diagrams and reliability test results are likely in image format
- ⚠️ No comparison to competing technologies (e.g., Rogers' work at Northwestern)
- ⚠️ The paper focuses on technical description rather than deep analysis or comparison
