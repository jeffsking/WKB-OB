---
media_id: "pdf_3867e2b60070d7dc3f413086d0b0036e_4ec19a07ed10258f148d8e99fac56749001a693ee6c0644e"
source_file: "Smart Fabric Textiles Recent Advances and Challenges.pdf.md"
original_path: "RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Smart Fabric Textiles Recent Advances and Challenges.pdf.md"
extracted: "2026-09-27"
extract_method: "ima-mcp fetch_media_content"
extract_status: "ok"
clean_rules: "v2: dead-image-link->text(alt kept); repeat-digits->compressed"
processed: "2026-09-27"
---

# Smart Fabric Textiles Recent Advances and Challenges.pdf.md

8
textiles

MDPI

Review

# Smart Fabric Textiles: Recent Advances and Challenges

Heitor Luiz Ornaghi Júnior $^{1,*}$, Roberta Motta Neves $^{2}$D, Francisco Maciel Monticeli $^{3}$ and Lucas Dall Agnol $^{1}$D

## check for updates

Citation: Júnior, H.L.O.; Neves, R.M.; Monticeli, F.M.; Dall Agnol, L. Smart Fabric Textiles: Recent Advances and Challenges. Textiles 2022, 2, 582-605. https://doi.org/10.3390/textiles2040034

Academic Editors: Hafeezullah Memon and Narcisa Vrinceanu

Received: 10 October 2022
Accepted: 16 November 2022
Published: 21 November 2022

Publisher's Note: MDPI stays neutral with regard to jurisdictional claims in published maps and institutional affiliations.

[图片: 人8]
Copyright: © 2022 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https://creativecommons.org/licenses/by/ 4.0/).

$^{1}$ Mantova Indústria de Tubos Plásticos Ltd.a., Rua Isidoro Fadanelli, 194-B. Centenário, Caxias do Sul 95045-137, RS, Brazil

$^{2}$ Programa de Pós-Graduação em Engenharia de Processos e Tecnologias (PGPROTEC), Campus Sede, Universidade de Caxias do Sul, UCS, R. Francisco Getúlio Vargas, 1130-Petrópolis, Caxias do Sul 95070-560, RS, Brazil

$^{3}$ Instituto Tecnológico de Aeronautica—ITA, Praça Marechal Eduardo Gomes, 50, São José dos Campos 12228-900, SP, Brazil

* Correspondence: ornaghijr.heitor@gmail.com

Abstract: Textiles have been used in our daily life since antiquity in both economies and social relationships. Nowadays, there has never been a greater desire for intelligent materials. Smart fabric textiles with high-quality and high-performance fiber manufacturing with specific functions represented by clothing and apparel brands (such as astronaut suits that can regulate temperature and control muscle vibrations) are becoming increasingly prominent. Product applications also extend from the field of life clothing to the medical/health, ecology/environmental protection, and military/aerospace fields. In this context, this review proposes to demonstrate the recent advances and challenges regarding smart fabric textiles. The possibilities of innovative smart textiles extending the overall usefulness and functionalities of standard fabrics are immense in the fields of medical devices, fashion, entertainment, and defense, considering sufficient comfort as a parameter necessary for users to accept wearable devices. Smart textile devices require a multidisciplinary approach regarding the circuit design of the development of intelligent textiles, as the knowledge of intelligent materials, microelectronics, and chemistry are integrated with a deep understanding of textile production for optimum results.

Keywords: smart fabrics; textiles; applications

### 1. Introduction

The development of textiles is directly related to the evolution of humanity. It can be charted starting from leaf-based clothing, followed by natural products such as silk and cotton that have improved well-being and comfort, until the use of synthetic materials that have gradually emerged and greatly improved our lives over the last century. The growing demand for high-quality products recently improved textile use in existing applications [1,2]. Due to the development of modern society, natural (such as cotton or hemp) [3,4] and chemical fibers (such as polyamide or viscose) [5] do not longer meet the full requirements imposed by the users by themselves. Fibers must have such special characteristics as energy collection, color tuning, and health monitoring, together with special characteristics such as shape memory or heat storage. Hence, since the very first use of natural/chemical cloths as reinforcement in composites [6,7] up to the most elaborate applications such as functional fibers with conductive [8] or antibacterial properties [9], smart fibers [10] with advanced properties such as energy harvesting [11], energy storage [12], or shape deformable [13] materials, shape memory materials, heat storage, and thermo-regulated fabrics are the typical applications of this relatively new generation of textiles. These are called smart textiles, being classified as passive smart textiles (textiles that sense external conditions), active smart textiles (textiles that respond to external conditions), and ultra-smart textiles (textiles that sense, react, and adapt themselves to conditions). Smart textiles are intelligent systems that can observe or communicate ambient circumstances and detect/process

Textiles 2022, 2

583

the wearer's state. Since their first appearance in the market in the late 1980s in Japan (where silk thread functioned with a memory effect), smart materials have gained increased investment motivated by the growing need for such materials for multiple applications in different sectors with promising expectations. Additionally, the growing advances in science allow for more sophisticated technologies to be developed and inserted in even more complex systems [14] in different disciplines such as cloth manufacturing, artificial intelligence, biotechnology, information, theory of chaos, and randomizations, among others [15]. Research and development geared towards wearable textile-based personal systems allowing for health monitoring, protection and safety, and a healthy lifestyle have gained strong interest during the last few years. Hence, there has never been a greater desire for intelligent materials like these that can be designed to change color and shape or provide interactive elements. For example, clothing and apparel brands (such as astronaut suits) that can regulate temperature and control muscle vibrations are a significant advance in comfort and performance. Another example of this is textile fabrics that release medication or moisturizer into the skin. Product applications also extend from the field of life clothing to the medical and health, ecology and environmental protection, military, and aerospace fields [16–18]. Figure 1 summarizes the main applications related to smart fabric textiles.

[图片: Color-changing fabricTemperature-regulatingfabricSMARTShape-memoryFABRICfabricTEXTILESWater-proof andbreathable fabricElectronicinformation fabric]
# Figure 1. Several applications associate with smart fabric textiles. The images were taken from internet [19–23].

These smart textiles have enormous potential in practically any area of human life (Figure 2) from aesthetic applications, the sensation of comfort even when exposed to extreme temperatures, protection, and the monitoring of diseases to military defense. Hence, depending on the external stimulus/condition (environmental conditions or stimuli from mechanical, thermal, magnetic, chemical, electrical, or other sources), the textiles sense and react to their surroundings due to the presence of three distinct components: sensors, actuators (for active smart textiles), and controlling units (for very smart textiles). Metallic materials, conductive polymers, or conductive inks can be integrated into the textile structure, aiming to achieve a specific property (such as electrical conductivity) in either the whole structure or for some printed areas that can be used as switches for the activation of circuits [3,24].

Textiles 2022, 2

584

As aforementioned, the benefits of smart materials became more evident at the beginning of the 1990s. Some recent studies have shown the wide range of the applications of smart textiles. Peng et al. [25] studied textiles for personal thermal management and energy and emphasized the importance of the development of textiles that effectively regulate heat exchange between the human body and the environment. Chen et al. [26] evaluated smart textiles used for electricity generation, considering the emerging energy crisis, environmental pollution, and public health and the smart textiles' respective abilities to harvest biomechanical energy, body heat energy, biochemical energy, solar energy, and other hybrid forms of energy. Massaroni et al. [27] studied medical smart textiles based on fiber optic technology driven by an increase in the mobility of patients who need continuous monitoring of physiological parameters and the respective monitoring of mechanical requirements. Revaiah et al. [28] focused their review on considering smart textiles for distinct military operations such as flame retardants suits, extended cold weather clothing, high altitude edema chambers, anti-G suits, and submarine escape sets, among others. Huang et al. [29], in their study, studied yarn-based piezoresistive sensors for smart textiles and outlined some characteristics that can improve the piezoresistive fibers produced based on their study. The medical and healthcare fields are also gaining great attention, which is mainly motivated by a growing population and an extended lifetime, enhanced medical procedures, patient recovery, and medical devices [30].

[图片: World of Wearable Technology ApplicationsProductsProducFunction With StyleFunctionsFunctions-Real-Time Data-Playful Show-Remote TeamApplicationsApplicationsMonitoringAmbience Through.MilitaryLightSSecunity Profiling.Emergency.LightServicesEmbellishmentHazmaPattern Changing·Identity RecognitionSectorSectorDetection·Decorative Display.EnvironmenTrack/DisplayRemoteSurveillanceSecurityEmotions.EmotionalMonitoring.Rescue/TrackingGlamorSafetyResponse-Uncbtrusive·Vital SignsAccess VoicePatient Monitoring.PersonMonitoringText,EmailCommunl--8odyIn Vivo/tmplantsMedicalMutimedia.InteractirecationAugmentation●Chroek DiseaseGroupManagementUse Social Media.PhysicalLifestyle-Olabetes Care.Bralin/EyWellnessExpressionComputingMovementSport/Use Touch & HugRemote EEG·OrganiserFitnessPysiologicaECG,EMG.Responsive LearningMonitoring.Interactive Gaming·Weight/ Energy.Spcrt Performance●Data/Media AccessMonitoring·Schedule·Fitness Monitoring·Sleep/Emotion/·SharedGalt/PostureGHeManagemenStress Tracking·Virtual CoachingCorrectionExperience.Outdoor Navigation/Trackg-[[G/Optimised Learning-Obesity ControlBody Cooling/HeatingAugmented RealitnteractivePerformance Monitor-Realtime StrearningtnstructionActivity TrackingHUDGoal Monitoring/Management-Direction Data/Location Share-Optimum Performancoc]
# Figure 2. Expected applications in Europe for the next years [31].

The increase in scientific studies and the respective emerging growth in the smart textiles field has led to the expansion of the market for smart textiles globally. The rapid demand for new textiles in different industries and distinct applications is the main impulse for this growth. The global smart textiles market is estimated to expand at a compound annual growth rate (CAGR) of 25% from 2021 to 2031, crossing the value of US$23.82 Bn by the end of 2031 [32]. With this, new facilities have been opened to meet the rising demand for smart fabrics with the advent of new technologies such as artificial intelligence (AI) and internet of things (IoT) [33] that help to monitor and control some process and/or product characteristics.

In this context, this review aims to present the recent advances and challenges regarding smart fabric textiles.

# 2. Brief History

The scientific interest in wearable electronic applications is recent, but investigations have been related to this field since the 1850s regarding their use in corsets and belts [34,35].

Textiles 2022, 2

585

In 1955, the first wearable computer was developed, and much research and effort has been put forward since then (mainly in the early 1990s) to incorporate textiles with electronic functions that are closed and integrated within the textile [36–39]. The development's history can be divided into three distinct categories, divided by respective complexity and functionality. The first category is close to wearable computing, the second category is new methods to incorporate the fabric as an essential part of the textile device or circuit, and the third category allows for the creation of fiber-level smart textiles. More details can be found in Cheneral and van Pieterson's study [40]. Considering this evolution in science and technology, it is natural to forecast systems more and more integrated. Ideas that can sound absurd nowadays can be perfectly plausible in the near future. Figure 3 shows the historical development of wearable electronic textiles.

[图片: (q]
# Figure 3. (a) Georgia Tech Wearable Motherboard (GTWM)14 From S. Park et al., "The wearable motherboard: A framework for personalized mobile information processing (PMIP)", Communications of the ACM 2002, Vol. 11:2. Copyright # 2002 by ACM, Inc. Reprinted with permission of ACM, Inc. See https://doi.org/10.1145/513918.513961. Accessed on 1 January 2021. (b) Firefly dress, 16 reprinted by permission of Maggie Orth of International Fashion Machines. (c) Pom-Pom light switch, 19 reprinted by permission of Maggie Orth of International Fashion Machines. (d) Textile capacitor array11 Copyright 2006. From J. Meyer et al., "Textile pressure sensor for muscle activity and motion detection", in Proceedings of 10th IEEE International Symposium on Wearable Computers, 2006, pp. 69-72. Reprinted with permission from IEEE proceedings. (e) Laminated elastic circuit from the STELLA project, image provided courtery of Johan de Baets from IMEC.20. (f) Eleksen textile keyboard21 licensed under Creative Commons BY-NCSA 2.0. (g) A woven thin film temperature sensor on a fiber19 licensed under Creative Commons BY-NC-SA 2.0. Figure obtained with kind permission from the publisher [40]. The same legend was used from the original study.

Textiles 2022, 2

586

# 3. Fabrication Methods

The integration of smart textile functions into a final product basically involves some property inherent to the original textile (electrical conductivity, for example) [37], the attachment of the circuit to the textile after fabrication [38], or some hybrid approach combining commercial and textile functionalities.

The first method is the use of conductive textile yarns, which includes several different methods such as weaving, knitting, embroidery, lamination, and stitching to be incorporated into smart textiles late in the process. Depending on the textile application, the requirement plays a major role. For sensors, for example, it is interesting to incorporate conductive wires as interconnecting lines for the maximization of the electrical circuits as demonstrated by other authors [39–46]. For applications in which a certain degree of heating is required, yarns with lower conductivity are the best alternative. On the other hand, for lightning-smart textile applications, a considerable current and high conductivity are necessary. The conductivity of these yarns will depend on the metal used and can vary from 0.5 Ω/m to several kΩ/m [42]. Processability also plays a major role in the use of textiles. Low-resistance wires have limited elasticity and strength, resulting in knots and breaks in the wires. In addition, the same cutting method used for textiles (the application of heat) cannot be used for textiles with conductive metal wires due to the high thermal conductivity of the metal. More complex conductive yarns with an insulation layer (polymer coating or some polymer wrapped around the conductive ore) can also be constructed. The insulation layer improves washability and robustness when exposed to different environments. Figure 4 represents different types of conductive yarns.

[图片: AB100%copper wire-0.75mm cable9mm10mm3 core2 coreFemp RopeCD]
# Figure 4. (A) Copper wire, (B) copper incorporated on hemp fiber, (C) silver-coated polyamide multifilament yarn, and (D) Kevlar multifilament yarn wrapped with metal foil. The images were taken from the Internet [47–50].

The second method used is weaving and knitting, which generate large-area textile surfaces. In the weaving process, two perpendicular sets of yarns (called weft and warp) are interlaced, forming a 2D textile. 3D structures are also available and are based on the longitudinal (X direction), cross (Y direction), and vertically (Z direction) intertwined,

Textiles 2022, 2

587

interlaced, or intermeshed fibers/yarns. Figure 5A,B shows an example of 3D textiles. According to the webpage, the textiles do not lose the aspect of comfort, even when an inflexible substance that increases rigidity is incorporated. Furthermore, the visual aspect of this textile is very attractive with its three-dimensional silhouettes.

[图片: AB]
# Figure 5. (A,B) 3D textiles produced by StartUp Fashion [46].

The third method is putting in finishing touches for smart textiles where a specific capability is incorporated into the textile after fabrication. An example of this method is the incorporation of electronic devices used to interconnect lines inside the textile. The main issue is to establish electrical contacts between the fabric structure and the devices. Figure 6a-c shows three examples.

[图片: (q)(c)(a]
# Figure 6. (a) Microcontacting and LED using a conductive adhesive, (b) functional LEDs on a woven narrow fabric, and (c) a printed PEDOT line on the fabric used in a strain sensor. The figures were obtained under kindly permission of [40]. The same legend from the original study was maintained.

# 4. The Main Types of Smart Fabric Textiles

## 4.1. Smart Color-Changing Fabric Textiles

While passive smart textiles such as UV-protecting clothing or waterproof fabrics can only sense external conditions, smart color-changing fabric textiles actively sense external stimuli and react to them [26]. The principle of color changing is mainly based on the electron density or molecular structure of the material that changes due to external stimulus effect, causing the color change. They return to the original state if the stimulus disappears because it is the more stable state [32]. The color change can be due to some basic parameters such as photochromic (light affected), thermochromic (heat affected), electrochromic (electric affected), solvent chromic (solution affected), halochromic (pH affected), tribochromic (friction affected), and mechanochromic (pressure affected) factors [24]. It is believed that the use of these color-changing textiles will become more widespread in the future in the field of fashion and decoration (T-shirts, bags, and hats) with a high potential globally, and the color change mechanisms will depend on many other effects in addition to the existing ones. Figure 7 shows some examples of color-changing fabric textiles under different chromic effects.

Textiles 2022, 2

588

[图片: ELECTROCHROMICHALOCHROMICMECHANOCHROMICTHERMOCHROMICPHOTOCHROMIC]
# Figure 7. Examples of smart color-changing fabric textiles under different chromic effects [35,36].

Besides aesthetics, color-changing smart textiles can be applied for crucial applications, as in the case of a firefighter suit. While a darker color increases heat absorption, light reflection increases; hence, at very high temperatures, the suit can turn white and reflect the light. Thermochromic dyes accelerate the dimensional change of fibers and provide another thermoregulation effect. At high temperatures, there is a shortening of the thermochromic dyestuff-fibers. The pores of the fabric are enlarged so that a large amount of air is introduced, and, consequently, body temperature decreases. At low temperatures, the fibers are elongated and the pores are closed, resulting in the fabric maintaining the body's temperature [24]. The research was conducted [51] regarding the color-changing mechanism based on pH change. In this case, silk ink was turned into constituent proteins, which the researchers suspended in water. Next, it was mixed in pH-sensitive indicators and lactate oxidase that, when worn, measured the fatigue level of the wearer. Figure 8 represents a pH-responsive textile used as a sensor for acid rain. The resulting material [52] (polyamide 6 with Bromocresol green dye) developed an immediate color change in an excess of acidifying air pollutants.

[图片: AAcid RainNormal RainpH-responsiveness of dyed PA6 fabric beforepH 3.6-5.6pH >5.6and after water and oil repellent finishing1815S/ypHdyed PA6 (0.1% of BCG)pH 3 4 5678 9 10 11dyed PA6 (0.2% of BCG)dyed and finished PA6 (0.2% of BCG)Colour change of Bromocresol Green (BCG)dyed PA6 (0.5% of BCG)dye on PA6 fabric at different pH values]
# Figure 8. Schematic representation of the color change under different pHs. For acid rain the pH range was from 3.6 to 5.6 while for the normal rain pH was >5.6. The images were adapted from [52] under the Creative Commons Attribution License.

Textiles 2022, 2

589

# 4.2. Temperature-Controlling Fabric Textiles

The main motivation for high-tech fabrics with controlled temperature is the requirement for maintaining a comfortable temperature, independent of the external environment. Materials that have a phase change resulting from heating/cooling started to be developed in the 1980s by NASA, where materials with the absorption/release of large amounts of energy accompanied by a change of phase from solid to liquid were developed. Some technologies contain change-size pores according to body temperature, which can open or close in response to the weather. In this sense, the pores can open if it is warm and dry and close when it is cold and wet, increasing the capability of the textile to be water-proof and breathable [53,54]. Figure 9A shows the capability of thermal conductive fabric (highly aligned boron nitride (BN)/poly (vinyl alcohol) (PVA)—named a-BN/PVA fabric by the authors) to improve the thermal transport properties of textiles for personal cooling. Figure 9B represents a colored textile used for personal cooling.

[图片: Aa-BN/PVA fabricCoolingTextileAligned BNhuman skinHeat transfera-RN/PVA fiher]
[图片: Mid-IR radiationColored PE compositefibers & textilesInorganic pigmentNPs-mixed PE200 m200 μmBare skinCotton textilePB-PE textileFe2O3-PE textileSi-PE textile]
# Figure 9. Temperature-controlling fabric textiles. The images are used under permission from [55,56]. (A) is a schematic representation of the capability of thermal conductive fabric (highly aligned boron nitride (BN)/poly (vinyl alcohol) (PVA)—named a-BN/PVA fabric by the authors) to improve the thermal transport properties of textiles for personal cooling. (B) represents a colored textile used for personal cooling were different colors are obtained according to cooling temperature. Optical micrographs and photos of the knitted colored textile with good wearability for blue PB-PE (I), red Fe₂O₃-PE (J), and yellow Si-PE (K).

Textiles 2022, 2

590

# 4.3. Shape Memory Fabric Textiles

Shape memory textiles can be applied to demonstrate useful attributes such as finishing, breathability, damping, skincare, wound-dressing, deodorant, and smart energy storage [57,58]. The principle is based on a mechanism that can remember and recover substantial programmed deformation under different external stimuli [57], which can be chemical, mechanical, magnetic, or electrical. All these materials have their activation effect triggered in temperatures close to body temperature. Shape memory alloys are composed of a combination of two or more elements with properties of hardness and elasticity that vary considerably at specific temperatures. Different effects are expected when applied to textiles, such as a flat appearance, crease retention, and bagging recovery [59]. The Italian company Corpo Nove created a t-shirt that does not require ironing. Figure 10 shows an example of shape memory fabrics.

[图片: (a)WeavingDeformationShape-memory deviceTraditional YarnSmart energy storage shape memory fabricsHealingShaperecoveredFabrics with original shapeShape recovering]
[图片: Automatic(b)Smart energy storagetransformationEasy to deformclothsNormalOver 35°CtemperatureCooling down]
# Figure 10. (a) Scheme of a shape memory supercapacitor woven hybridized with traditional fabric and (b) demonstration of the smart shape memory textile applied in an intelligent cloth (reproduced with permission from [60]).

A shape memory polymer is included between two layers of fabric, where temperature attains molecular motion and more conformational states, allowing the porous structure to eliminate the heat from the body, for example. Below a specific temperature, a tight structure is formed, restraining the passage of heat, water, or wind around the body. This polymer is a flexible barrier self-adjustable to temperature changes, providing optimum comfort in any environment.

Shape memory textiles can be used in different applications due to their capability to acquire a third dimension. Nickel-titanium shape memory alloys are used for protection against high temperatures. Self-tangled medical surgical threads are designed for endoscopic surgery, and implants that are small in normal ambient conditions allow them to perform operations with small incisions, shortening the healing time and reducing the risk of infection. Other applications include esthetic and decorative purposes [1,35,36].

Textiles 2022, 2

591

# 4.4. Waterproof and Breathable Fabric Textiles

Through movement, the human body sweats and dissipates heat through heat waves and perspiration. Therefore, besides protection from external agents such as heat, wind, or water, the fabric must maintain the warmth of the human body and allow the effective transmission of vapor from the skin to the outside atmosphere. Therefore, the fabric must have two main characteristics: (i) be breathable to allow the diffusion of water vapor; and (ii) be waterproof to avoid water breaking through from the outside environment to the skin. The design of some specific products is also dependent on breathability. Usually, the fabrics are successfully manufactured to prevent liquid water from passing through (the pores are made 20,000 times smaller than a drop of liquid water) but fail to avoid the passage of water vapor (uninfuntately, the pores are 700 times larger than a water molecule). Another important characteristic is the moisture vapor transmission rate. If the perspiration level is high, as in a firefighting operation or in racer suits, perspiration is also high, and the fabric should maintain the optimum moisture vapor transmission rate and protect itself from external heat and pressure. Figure 11 shows the principles of waterproofing and breathability for smart fabric textiles.

[图片: 2. Durable water repellent finish1. Outerwear material3.Membrane4. Insulation5. LiningPerspiration escape (sweat)Body heat]
# Figure 11. Examples of waterproof and breathable fabric textiles. The image was obtained under permission of [61].

The desirable properties of waterproof breathable fabric are:

· Optimum heat and moisture regulation.

· Absorption of surplus heat.

· Waterproofness.

· Good air and water vapor permeability.

· Rapid drying to prevent catching cold, durable, easy care/launderability.

· Dimensional stability even when it comes in contact with water.

· Lightweight, soft, and pleasant to the touch.

# 4.5. Wearable Electronics Smart Textile

Wearable electronics are mainly based on different functionalities, such as electricity utilization, generation, and storage. Electronic textiles have components intrinsic to the fabric that remain unsusceptible from becoming tangled or snagged by surrounding effects. Such electronic devices must meet special requirements concerning wearability and are characterized by their ability to recognize both the activity and the behavioral status of their

Textiles 2022, 2

592

use automatically, as well as their ability to recognize the situation around the user and must use this information to adjust the systems' configurations and functionality. Figure 12 represents some examples of wearable electronics' smart textiles.

[图片]
# Figure 12. Some examples of wearable electronic smart textiles. Images were taken from the Internet [23,62,63].

The incorporation of any electronic or interconnection must not interfere with physical flexibility, besides being of a typical size that does not appear in the final product. Many products have been developed regarding wearable electronics, such as biological monitoring-ECG and respiration garments, biomedical garments for the monitoring, diagnosing, and treatment of medical conditions, sensing patch textiles to target bodily fluid sensing, contactless sensors for monitoring ECG and EMG, and products that sense vital parameters, among others [64–71].

# 4.6. Phase-Changing Textiles

Phase change materials are thermoregulating materials containing a textile substrate. Usually, when a well-determined temperature is at its melting point, a phase change occurs, leading to different heat absorption/dissipation parameters. One important point is that the temperature remains constant during the entire phase change, be it from the heating to the cooling or vice versa. If two or more phase-changing materials are used simultaneously, the temperature range for phase change can be adjusted in specific applications. The most important feature of this is that textiles must be dependent on ambient temperature conditions, i.e., the textile must have a thermoregulating effect that is dependent on the material used and the respective thermal capacity. Finally, to increase its efficiency, the temperature at which the material will most commonly be used must also be the temperature at which the material changes phase.

Microencapsulated phase-changing materials can be incorporated into the structure of a textile during fiber drawing, incorporated into the nonwoven structure, or coated on the textile surface. Product design is also important. For example, the apparel containing a phase-changing material when transferred from an indoor (warm) to an outdoor (cold) environment can be maintained for an average of 12–15 min. If the apparel is not well designed, it can result in the dissipation of heat in the phase-changing material instead of maintaining the constant temperature.

Textiles 2022, 2

593

This type of textile is used commercially in hospital beds and pillows where the temperature is thermoregulated, ensuring comfort for the patient and contributing to the patient's healing process. Thermoregulator plasters and blankets have also been employed in the medical field as well as in underwear, shoes, and sportswear [2,51,53,54].

# 5. Today's Applications

Some applications are summarized in Figure 13.

[图片: e38x!PeNpSens8ria's s8ckssuoeq ouo29:10uepinB eBo J0]90%AHeShirtShirtn DrHUGSOUND SHIRTLexi's acketHexoskin smarsbirIntegrateActivity SensoIntegratedRespiration SensorIntegratedHeart Sensorcornal & externalcomperature senooAccolerometeCarbon Fiber heating Padpoq-1aM0TMicro computer0remnosnugroupsmonitorinyoga pantsUSB-A to chargereun]
# Figure 13. Some examples of wearable electronic smart textiles. Images were taken from the Internet [72–79].

The Nadi and Nadi X leggings from Wearable X are described as smart yoga pants that include activewear sensors to identify attempted yoga poses and provide haptic feedback in the form of gentle vibrations. This type of cloth helps the user to correct the Yoga pose but can be expanded to other clothes aiming to maximize the performance of an

Textiles 2022, 2

594

athlete in any sport by immediately indicating any errors in the initial stipulated movement. Additionally, the everyday posture that can lead to spine problems can be avoided by a gentle vibration warning.

The HugShirt and SoundShirt Pro have sensors and actuators (the SoundShirt Pro has haptic actuation modules) that can help users decrease their sense of loneliness and bring together their loved ones. This is obtained by using sensors that record the contact's strength, length, and position, and actuators reproduce the sense of touch and the emotion of the hug to your loved ones. Due to the haptic actuator modulus on the SoundShirt Pro, it can be used for music, hugs, gaming, and access to live performances at venues with a QPRO system, providing more immersive augmented and virtual reality experiences.

The Mercury jacket adjusts body temperature in real-time, thanks to sophisticated lightweight heating components and revolutionary stretch insulation. An intelligent thermostat responds to your body and surroundings by managing three lightweight, flexible carbon fiber heating components. Mercury is designed to protect you from repelling wind, snow, water, and odors—whatever your travels throw at you.

Some Yoga pants can monitor the activity of the primary lower-body muscular groups, sending signals directly to an app to indicate which muscles are working more effectively. Additionally, features such as the monitoring of heart rate, calorie expenditure, and active time vs. rest time are available.

Sensoria's socks include patented 100 percent textile sensors. They are coupled with a Bluetooth detachable core that improves precision in step counting, speed, calorie, altitude, and distance monitoring. Sensoria may assist runners in identifying injury-prone running techniques (heel striking, ball striking, and so on) and then use a mobile app to train the runner in real-time through auditory cues.

Hexoskin Smart Shirts allow comfort and mobility and have an integrated activity sensor, an integrated respiration sensor, and an integrated heart sensor that monitor daily health status. It's the updated version of the original Trucker Jacket, incorporating careful design features for active users in the city. This ground-breaking garment combines 150 years of Levi's denim creativity and Google engineering, with conductive Jacquard thread woven in. You can control music, screen phone calls, and obtain directions with a touch of the cuff.

Other applications for this technology include medical and health care. Textiles with specific functionalities would help to improve a hospital's quality and patient needs with more efficiency [80]. The benefits to including smart textiles in medical use includes patient mobility whilst undergoing monitoring, continuous monitoring of vital signs for postoperative recuperation, and a reduction in invasive procedures, among others [81]. The fabrication process, when based on synthetic or natural polymers, uses the polymer in fiber format, as films, or as composites. After the transformation of the polymer, the resulting end products can be bone grafts (from polymer composites), sutures (from 3D braids), protective respirators (from nonwovens), apparel (from fabrics woven/knits), or waterproof and breathable surgical gowns (from laminate fabrics). Afterwards, the material is treated (chemically, physically, or biologically), packaged, and sterilized. Various types of methods are applied prior to certain types of applications. These methods include surface modification (surface coating or plasma treatment) or finishing techniques (antibacterial, antiodor, blood coagulant, blood anticoagulant, drug delivery, water and blood absorption, or blood repellent). Hence, the types of applications include extracorporeal (external body applications), intracorporeal (internal body applications), or intra/extracorporeal (internal/external interface) applications. The external body applications are the most common among the three and include wound care, compression, barrier, and hygienic products. Internal applications can be absorbable or not in the human body and include orthopedic braces for knees, ankles, or back injuries to maintain the posture with comfort. Other applications include prosthetics to replace some missing parts of the body, improving fit and functionality. Finally, internal/external applications are biomaterials

Textiles 2022, 2

595

and includes extracorporeal devices and sutures. Figure 14 shows some examples of medical applications.

[图片: Protective forinfection controMedicalCloth diapecompressionMEDICALAPPLICATIONSSanitaryArtificial lungnapkinKnee braceProstheticdevice]
# Figure 14. Some examples of textile medical devices. Images were taken from the Internet [82–88].

# 6. Recent Advances and Challenges

Smart fabric textiles not only promote the development, transformation, and upgrading of the textile industry around the world but also promote the development of disruptive emerging industries. The global smart textiles market is estimated to expand at a compound annual growth rate (CAGR) of 25% from 2021 to 2031, crossing the value of US$23.82 Bn by the end of 2031 [30]. Ongoing research and development activities to explore advanced technologies in smart textiles are driving market growth. This field is still in the early stages of development; the possibilities of innovative smart textiles extending the overall usefulness and functionality of standard fabrics are immense. The global smart textiles market is expected to show lucrative growth opportunities and applications across different end-use industries in the forthcoming years. Some smart textiles are already commercialized at a relatively low cost (the perfect cost-price balance has been challenging to achieve), as in the case of smartwatches and wristbands in which smart wireless sensor networks are presented.

Some recent developments making performance more perfect in smart textiles range from ultrasonic assembly to the unique fabric used in outer space, space transportation systems, and innovative sportswear, among others [3]. Hence, the application field is vast and can be extended to medical and healthcare industries (measuring heart rate), the

Textiles 2022, 2

596

automotive industry, and personal protective equipment, among others. In addition, the advanced technology allows for the miniaturization of electronic components, broadening the range of applications for these types of materials. The constant search for comfort and lightness for sports and fitness applications creates an expected growth rate for the upcoming years. The capability to monitor and analyze physiological parameters such as blood pressure, diabetes, and temperature has also broadened its relevance to the medical applications field, and this application is expected to rise at a higher rate compared to the conventional ones.

The main issues are the incompatibility of some textiles and electronic systems, re-straining the applications for the same products. In addition, the slow adoption rate tends to promote steady growth for some specific smart textiles. The lack of regulations and standards is another factor in some products' steady growth.

Thermal management—The main issue is the development of passive textiles with active warming/cooling mechanisms to supply extra heat/cold. The heat mechanisms are based on Joule heating (the process in which the passage of an electric current through a conductor produces heat) and the cooling mechanisms are achieved by the enhancement of convection and liquid cooling. In brief, these mechanisms adjust the microclimate of the human body by altering its macroscale and/or microscale structures as environmental parameters change. These mechanisms are a new insight for building energy saving, being more flexible, cost-effective, and energy-efficient because the focus is only on the human body and its local ambient environment. The main drawback of this includes the practical application and commercialization of the textiles from laboratory proof-of-concept to the industrial scale. In addition, more universal tests for demonstrating the cooling/warming effect of textiles need to be established and acknowledged. A combination of comfort and specific thermal properties are required. The comparison among different studies is made more difficult due the fact that different methods are used in published papers, which are very distinct and flexible. A more advanced class of textiles comprises multiple functions such as thermal comfort, sensing, computing, electronic control, and being selfpowering [89,90]. Another example is the use of smart thermal management textiles with anisotropic and thermorepsive electrical conductivity due to outdoor heat stress. Peng et al. [91] relate that there is an annual burden of US $6.2 billion for the Australian workforce. The temperature fluctuation during the daytime can cause health hazards for workers, reducing labor productivity. Hence, self-regulating textiles are required to keep the human body stable even with oscillations in temperature [92].

Electricity generation—The field of distributed electronics demands persuasive energy solutions and an exploration of sustainability, pushing the research of more than 26 billion Internet of Things (IoT) devices. This era of IoT allows for a more efficient and rapid development of materials for efficiency enhancement (englobing applied materials and device structures), output stability, mechanical durability, wearing comfort, washability, encapsulation, aesthetics properties, large-scale fabrication, 3D printing, self-healing, and evaluation standard, among others. The production of each of the textiles entails many challenges to overcome [26,93].

Military operations—The military, the marines, and other related sectors are in search of constant changes in both comfort and technical textiles. Severe climatic situations, combined with abrupt and constant body movements, are one of the main motivations to drive new technologies. Protection against chemicals also plays a major role. The usefulness of such fabrics has long been acknowledged for improving fighter efficiency and saving people's lives in battle. The goal is to expand these characteristics to other issues (such as the ability to measure and store information and adjust a material's usefulness over time). Considering that the top 10 militaries have around 100 million soldiers and that at least 4-6 m of fabric are required per soldier (including apparel, helmets, tents, and gear), this is a growing demand [94,95].

Medical devices—According to the Medical Smart Textile Market [96], there is a CAGR growing estimative of 7.51%, reaching USD 2.10 billion by the end of 2027. The

Textiles 2022, 2

597

preoccupation with providing better healthcare services now and in the future is intertwined with the development of new textile-based implantable goods (tendons and artificial ligaments). Another important issue is the increase in the life expectancy of the global population, which will increase the number of surgeries performed, as well as the number of implantable goods used. Different textiles, including woven, knitted, and non-woven textiles, tend to have an enormous growth forecasted from 2017 to 2028. This is because they are hygiene products that are representative of almost 50% of the global medical textiles market. An example of great-scale investment was the COVID-19 pandemic situation, which forced the acquisition of new hospital beds and other apparatus in hospitals to support more than 36 million cases. Together, domestic production and personal protection equipment were improved. Other products are being developed, including biodegradable and nonbiodegradable polymers. Such products include face masks, shoe covers, and maternity pads [97–99].

Nanotechnology—The global nanotechnology clothing market is expected to grow from $4.61 billion in 2021 to $5.75 billion in 2022 at a compound annual growth rate (CAGR) of 24.6%. The market is expected to grow to $13.83 billion in 2026 at a compound annual growth rate (CAGR) of 24.6% [100]. Nanoparticles (silver nanoparticles, nanopores, nanoparticles, nanowhiskers, etc.) are used along with textiles to enhance desirable surface characteristics such as being microbicidal, waterproof, antistatic, UV-protection, color durable, dirt-resistant, odor-resistant, stain-resistant, wrinkle-resistant, and having a better thermal performance. The main types of nanotechnology used include nanocoated textiles, nanoporous textiles, fabrics consisting of nanofiber webs, and composite fibers based on nanostructures. These nanotechnologies have various applications such as healthcare, packing, sports and leisure, defense, home and household, environmental protection, and geotextiles, among others. The incorporation of nanoparticles with antimicrobial properties in textiles is another promising issue, despite the toxicity of the nanoparticles when in contact with the circulatory system. Major players operating in the nanotechnology clothing market are launching a new line of clothing with wearable technology to maintain their competitive position in the global market. The countries covered in the nanotechnology clothing market report are Australia, Brazil, China, France, Germany, India, Indonesia, Japan, Russia, South Korea, the UK, and the USA. In a review, Shah et al. [101] underline several methods for the functionalization of nanomaterials and their integration into textiles, considering several key features such as cost and ecosustainability. The authors also consider nontoxicity and wearability in the production in fabrication of supercapacitors, nanogenerators, and photoelectronic devices.

Wearable devices—The integration of wearable electronics in personal healthcare to monitor pressure, diabetes, or other issues are an anticipated trend in the future. The ability to respond to temperature, humidity, or other external environments, the monitoring of intelligent robotics, thermal regulation, and other integrated/combined characteristics to detect multiple signs are expected to be part of their future. Besides multifunctionality, user-friendly and user-acceptance characteristics are also required features. For this purpose, enhanced interfaces (to improve the interaction of humans with electronic devices) using microelectronics is an upcoming trend. The wearable multifunctional system may be sustainable, independent, and capable of facilitating efficient signal generation, transmission, and processing. Comfortability is still the main characteristic of wearable textiles. Next-generation electronic textile systems can be envisioned as completely integrated fiber-based electronic textile devices with enhanced optoelectrical and mechanical properties that consume minimal power or have self-sustainable device features. The development of biosafe and less irritating materials should not be overlooked for long-term continuous operations near or on the human body. This consideration leads to the development of advanced electronic textile system technology [102–109]. Figure 15 illustrates the wearable devices used for health monitoring where, after fabrication, the health monitoring is satisfactorily allied with extreme comfort.

Textiles 2022, 2

598

[图片: FabricationApplicationHealth monitoring1010102101]
# Figure 15. Health monitoring scheme using electronic fibers/textiles and the respective applications. Images were taken with kind permission from [110].

Electroconductive textiles—Firstly, electroconductive textiles require conductive structures in which knittable and weavable filaments are unified with sensors, energy transport, and energy storage, among others. According to Guo et al. [111], the key concept to define electroconductive textiles is electrical current; hence, any materials that are electrically conductive can be made into an electroconductive textile. These materials are classified following seven classes for textile use: (i) metal(mono) filaments such as stainless steel and copper; (ii) co-spun polymer-metal yarns consisting of a united polymer/metal filament achieved by some yarn spinning method; (iii) metal-coated polymeric filament and yarns; (iv) metal-filled polymeric filaments; (v) carbon allotropes acting as a conductive agent; (vi) a conductive polymer; and (vii) a mechanically stable common textile fiber coated by a conductive polymer. Vanço et al. [112] studied the physical vapor deposition (PVD) process coating on natural textile fibers. One of the main characteristics required is stability at elevated temperatures. This is only achieved by using modern coating methods over conventional ones. One of the possible applications is in the modernization of tires in the transport industry, where integrated sensors can provide information to the driver (such as inflation pressure and traction). Maity et al. [113] proposed a review in which methods of preparation and development, as well as characteristics of conductive polymer-based electroconductive textile composites used for electromagnetic interference shielding, are presented. In brief, electromagnetic interference shielding (EMI) is a method used to protect electronic and electrical equipment against electromagnetic radiation. Particles such as copper or silver are usually applied on the surface coating to protect cell phones or computers from the electromagnetic radiation caused by the energy reflection principle. Different methods and developments are being used to improve the performance of the shielding materials [114]. The chemical vapor deposition (CVD) was also studied [115] and can be applied in polypyrrole polymer coating or superhydrophobic fabrics. The process is expected to be scaled up to become economically viable in the future with the advance of nanotechnology. Aerogel is another material that can combine low density with a functionalized surface for the fabrication of sensors or other active materials that are active-responsive. Stempien et al. [116] developed a supercapacitor made with synthesized polypyrrole (PPy) layers on textile fabrics using a reactive inkjet printing technique. The main results indicated a final product with good electrochemical stability that retained more than 50% of its initial capacitance after 2000 cycles., compared to previously reported results.

The main demand for wearable devices lies in the comfort of use, being lightweight, and other features such as breathable/permeable/conformable materials. For example,

Textiles 2022, 2

599

Cheng et al. [117] and Weng et al. [118] studied some devices used to detect motion or monitor temperature as well as alert to some imminent diseases. The main issues lie in developing practical fabrication techniques, working mechanisms, the involvement of compatible materials, device assembly, and energy management. Hence, in the future the combination of comprising hardware (fiber devices) and software (algorithms) will be indispensable. Textile smart materials are usually hand-made, and efforts to grow to large-scale production are required. Efficient methods are applied to a few materials. Another important issue is the need for versatile manufacturing methods to be adequate to most of the emerging new materials and not restricted to a few of them. The higher the technology employed in the development of smart textile, the higher the amount of effort needed to introduce this technology to the textile. Characteristics such as fiber diameter and material are crucial to determine the process to be employed nowadays. For electronic fibers, there is a thick limit in which the fibers can be obtained, and, in the future, small materials are expected to yield a high-performance. The use of quantum dots as light-emitting layers several nanometers thick is being employed [108]. The challenges implicit in this design include multifunctionality, self-healing, biosafety (combining health monitoring devices with wearable displays using the own human body heat and movement as “fuel” to achieve some thermal management condition). Additionally, antileakage encapsulation for smart textiles that aims to avoid biosafety problems due to friction is required to minimize any reaction between skin and foreign bodies. Hence, biocompatible and nontoxic materials need to be employed. Finally, standards must be established (i.e., lifetime, durability, and flexibility under different environments).

One of the main requirements for successful electronic smart textiles is their washing and washability. As mentioned by Rotzler et al. [119], there are four interdependent factors that influence the washing process of textiles: chemistry, mechanical action, temperature, and washing time. Water can be seen as the fifth element. There is a seesaw effect englobing these four (five) factors, i.e., by decreasing one, the other must increase to maintain a consistent washing performance (to clean the product after certain predetermined cycles of the washing process without significant loss of serviceability) [120]. When integrating electronics into textiles, one more variable is included in the equation. Besides the absence of specific reliability standards, more in-depth knowledge is required to inform consumers, since many issues do not consider smart textiles. Most of the smart textiles are washed following ISO 6330 [113]. In a study conducted by Rotzler [121], the authors highlight some points indicating the main problems as well as some alternatives to improve the washability of electronic smart textiles. The main results indicate that the washing of smart textiles depends on the type of conductor track, the textile substrate used, and their interdependency. Hence, since the washing conditions will be highly dependent on the aforementioned factors, no global conclusions can be drawn. As an alternative, the authors recommend that significant improvement can be done on a fundamental level. One example is the increase of minimum bending radii for stretchable circuit boards' (SCB) conductor track.

Recyclability also plays a major role in the smart textile industry. While almost 100% of textiles are recycled and returned to the consumer as other products such as home insulation or stream [122,123], urgent attention is required to make electronic smart textiles sustainable. Veske and Ilen [124] compiled different studies and highlighted that research in recyclability is very scarce. The authors claimed that researchers mainly focus on innovation and fabrication methods other than the lack of an official standard method for regularization. Some of the studies are focused on lowering the environmental impact, ensuring a longer lifetime for and full responsibility of the producers. Other studies apply an ecodesign strategy focusing on sustainable design concepts. Finally, other studies focused on educational programs (guidelines or design tools) among producers aiming to further improve application and technology. As in the case of washability, the creation of reliable guidelines is required for design, development, and recycling.

Textiles 2022, 2

600

Antibacterial (inhibits the growth of bacteria), antifungal (inhibits the growth of fungal mycelium and spore germination), and antiviral (modifies the surface structures of viruses) textiles are also important because they scan directly affect our health. These products are included in air filters, personal hygiene, ventilation, and water purification, among others. An enormous increase in active sportswear is related to the COVID-19 pandemic [123]. In short, some chemicals, nanoparticles (NPs), or agents that coat the fabric and improve the antibacterial property are included in this growth. Despite their efficiency, synthetic chemicals and NPs do not have enough information available their impact on the environment. Hence, the use of natural agents must increase in the future, and a robust and consistent solution must be planned in advance to avoid a problem similar to that of plastic waste management [124]. Some examples include antibacterial fabric for underwear (Brooks Brothers/USA), an antimicrobial certain fabric for window coverings (Louvolite/England), and antimicrobial air mattresses (Coleman Aerobed/USA, Sea to Summit/Australia). Snari et al. [125] studied color-changing smart textiles; when Gram negative bacteria were recognized, the red shifted to purple, and when Gram positive bacteria were detected, the blue shifted to yellow. Nie et al. [126] produced self-disinfecting textiles combining photodynamic/photothermal effects and, according to the authors, these materials (with stimulus responses to different environments) presented great challenges due to the difficulties of contrasts' color changes being used as temperature indicators.

Stoppa and Chiolerio [127] claimed that the integration of electronics into textiles should involve a multidisciplinary approach—a huge number of producers are experienced with electronics or textiles, not both. Despite current advances in technology, the main issue is the comfort of the human body and safety.

# 7. Conclusions

After scientific efforts and development phases, smart textiles are an implanted customer interest and are presented as the future of the textile industry. With the rapid growth and advancements in textile technologies, nanotechnology, biosensors, new materials, and miniaturized electronics, many commercial products are available, and several scientists are developing new solutions, ideas, and concrete products with the emerging demand for smart textiles in various phases of life. The broadening of applications, from medical devices to entertainment and defense, is immense and has been increasing daily. However, faster development would be encouraged through increased investments in future research and development activities. For wearable devices, the most important feature is comfort. Nevertheless, mechanical resistance and durability must be accounted for in the final product. Increasingly, a multidisciplinary approach is required for developing more sophisticated materials.

Author Contributions: Conceptualization: H.L.O.J.; formal analysis: F.M.M. and R.M.N.; writing—original draft preparation: H.L.O.J. and L.D.A.; writing—review and editing: F.M.M. and R.M.N.; visualization: L.D.A.; supervision: H.L.O.J. All authors have read and agreed to the published version of the manuscript.

Funding: This research received no external funding.

Institutional Review Board Statement: Not applicable.

Informed Consent Statement: Not applicable.

Data Availability Statement: The data presented in this study are available on request from the corresponding author.

Conflicts of Interest: The authors declare no conflict of interest.

# References

1. Cherenack, K.; van Pieterson, L. Smart textiles: Challenges and opportunities. J. Appl. Phys. 2012, 112, 091301. [CrossRef].

2. van Langenhove, L.; Hertleer, C. Smart clothing: A new life. Int. J. Cloth. Sci. Technol. 2004, 16, 63–72. [CrossRef].

Textiles 2022, 2

601

3. Stanković, S.B.; Novaković, M.; Popović, D.M.; Poparić, G.B.; Bizjak, M. Novel engineering approach to optimization of thermal comfort properties of hemp containing textiles. J. Text. Inst. 2019, 110, 1271–1279. [CrossRef]

4. Wei, D.W.; Wei, H.; Gauthier, A.C.; Song, J.; Jin, J.; Xiao, H. Superhydrophobic modification of cellulose and cotton textiles: Methodologies and applications. J. Bioresour. Bioprod. 2020, 5, 1–15. [CrossRef]

5. van Rijwikj, K.; Teuwen, J.J.E.; Bersee, H.E.N.; Beukers, A. Textile fiber-reinforced anionic polyamide-6 composites. Part I: The vacuum infusion process. Compos. Part A Appl. Sci. Manuf. 2009, 40, 1–10. [CrossRef]

6. Pigatto, C.; Santos Almeida, J.H.; Luiz Ornaghi, H.; Rodríguez, A.L.; Mählmann, C.M.; Amico, S.C. Study of polypropylene/ethylene-propylene-diene monomer blends reinforced with sisal fibers. Polym. Compos. 2012, 33, 2262–2270. [CrossRef]

7. Júnior, H.L.; Zattera, A.J.; Amico, S.C. Dynamic mechanical properties and correlation with dynamic fragility of sital reinforced composites. Polym. Compos. 2015, 36, 161–166. [CrossRef]

8. Lee, J.; Kwon, H.; Seo, J.; Shin, S.; Koo, J.H.; Pang, C.; Son, S.; Kim, J.H.; Jang, Y.H.; Kim, D.E.; et al. Conductive fiber-based ultrasensitive textile pressure sensor for wearable electronics. Adv. Mater. 2015, 27, 2433–2439. [CrossRef]

9. Edgar, K.J.; Zhang, H. Antibacterial modification of Lyocell fiber: A review. Carbohydr. Polym. 2020, 250, 116932. [CrossRef].

10. Shi, Q.; Sun, J.; Hou, C.; Li, Y.; Zhang, Q.; Wang, H. Advanced functional fiber and smart textile. Adv. Fiber Mater. 2019, 1, 3–31. [CrossRef]

11. Huang, L.; Lin, S.; Xu, Z.; Zhou, H.; Duan, J.; Hu, B.; Zhou, J. Fiber-based energy conversion devices for human-body energy harvesting. Adv. Mater. 2020, 32, 1902034. [CrossRef] [PubMed]

12. Liao, M.; Yer, L.; Zhang, Y.; Chen, T.; Peng, H. The recent advance in fiber-shaped energy storage devices. Adv. Electron. Mater. 2019, 5, 1800456. [CrossRef]

13. Floris, I.; Adam, J.M.; Calderón, P.A.; Sales, S. Fiber optic shape sensors: A comprehensive review. Opt. Lasers Eng. 2021, 139, 106508. [CrossRef]

14. Smart Textiles in Fashion: What They Are, Types & Exciting Examples. Available online: https://thetechfashionista.com/what-are-smart-textiles-and-examples/ (accessed on 20 October 2022).

15. Smart Textile. Available online: https://www.technicaltextile.net/articles/smart-textile-2592 (accessed on 20 October 2022).

16. Patwary, M.S.U.; Syduzzaman, M. Smart Textiles and Nano-Technology: A General Overview. J. Text. Sci. Eng. 2015, 5, 1-7. [CrossRef]

17. Gasparini, K. Digital Hybridisation in Adaptive Textiles for Public Space. Textiles 2022, 2, 436–446. [CrossRef]

18. Giglio, A.; Neuwerk, K.; Haupt, M.; Conti, G.M.; Paoletti, I. Textile-Based Sound Sensors (TSS): New Opportunities for Sound Monitoring in Smart Buildings. Textiles 2022, 2, 296–306. [CrossRef]

19. Chandler, D.L. 3 Questions: The Rapidly Unfolding Future of Smart Fabrics. Available online: https://news.mit.edu/2020/smart-fabrics-future-0508 (accessed on 15 October 2022).

20. Aouf, R.S. Scientists Create Temperature-Regulating Fabric. Available online: https://www.dezeen.com/2019/02/26/temperature-regulating-fabric-university-of-maryland/ (accessed on 15 October 2022).

21. Polyester Shape Memory. Available online: https://www.leantex.com/memory-fabric/ (accessed on 15 October 2022).

22. Sharma, S. Waterproof Breathable Fabrics: Product Modification and Recent Developments. Available online: https://textilelearner.net/waterproof-breathable-fabrics/ (accessed on 15 October 2022).

23. Hart, M. Scientists Develop Electronic Textiles for Interactive Gear. Available online: https://nerdist.com/article/scientists-develop-electronic-textiles-interactive-gear-smart-clothes/ (accessed on 15 October 2022).

24. Çelikel, D.C. Smart E-Textile Materials. In Advanced Functional Materials; IntechOpen: London, UK, 2020; pp. 1–16. [CrossRef]

25. Peng, Y.; Cui, Y. Advanced textiles for personal thermal management and energy. Joule 2020, 4, 724–742. [CrossRef].

26. Chen, G.; Li, Y.; Bick, M.; Chen, J. Smart textiles for electricity generation. Chem. Rev. 2020, 120, 3668–3720. [CrossRef].

27. Massaroni, C.; Saccomandi, P.; Schena, E. Medical smart textiles based on fiber optic technology: An overview. J. Funct. Mater. 2015, 6, 204–221. [CrossRef]

28. Revaiah, R.G.; Kotresh, T.M.; Kandasubramanian, B. Technical textiles for military applications. J. Text. Inst. 2020, 111, 273–308. [CrossRef]

29. Huand, C.-T.; Tang, C.-F.; Lee, M.-C.; Chang, S.-H. Parametric design of yarn-based piezoresistive sensors for smart textiles. Sens. Actuators A Phys. 2008, 148, 10–15.

30. van Langenhove, L. Smart Textiles for Medicine and Healthcare: Materials, Systems and Applications; CRC Press: Cambridge, UK, 2007; ISBN 9781845692933.

31. Smart Textiles in Europe: The Next Tech Disruption—Interview with Andreas. Available online: https://www.smartx-europe.eu/smart-textiles-europe-next-tech-disruption-interview-lymberis-1/ (accessed on 5 November 2022).

32. Bhisey, R. Smart Textile Market to Expand at a CAGR of 25% from 2021 to 2031. Open PR Worldwide Public Relations. 2022. Available online: https://www.openpr.com/news/2651325/smart-textile-market-to-expand-at-a-cagr-of-25-from-2021-to-2031 (accessed on 25 August 2022).

33. Smart and Interactive Textiles Market to Thrive at a CAGR of 25.88% during 2022–2032 | Future Market Insights, Inc. Available online: https://www.globenewswire.com/news-release/2022/08/08/2493665/0/en/Smart-and-Interactive-Textiles-Market-to-Thrive-at-a-CAGR-of-25-88-during-2022-2032-Future-Market-Insights-Inc.html (accessed on 25 September 2022).

34. Gauvreau, B.; Guo, N.; Schicker, K.; Stoeffler, K.; Boismenu, F.; Ajji, A.; Wingfield, R.; Dubois, C.; Skorobogatiy, M. Color-changing and color-tunable photonic bandgap fiber textiles. Opt. Express 2008, 16, 15677–15693. [CrossRef] [PubMed]

Textiles 2022, 2

602

35. Zhang, J.; He, S.; Liu, L.; Guan, G.; Lu, X.; Sun, X.; Peng, H. The continuous fabrication of mechanochromic fibers. J. Mater. Chem. C Mater. 2016, 4, 2127–2133. [CrossRef]

36. Moretti, C.; Tao, X.; Koehl, L.; Koncar, V. Electrochromic textile displays for personal communication. In Smart Textiles and Their Applications; Elsevier Inc.: Amsterdam, The Netherlands, 2016; pp. 539–568. [CrossRef]

37. Fishlock, D. Doctor volts [Electrotherapy]. IEEE Rev. 2001, 47, 23-28. [CrossRef].

38. Thorpe, E.O. The invention of the first wearable computer. In Proceedings of the 2nd International Symposium on Wearable Computers 1998, Washington, DC, USA, 19-20 October 1998; pp. 4-8.

39. Juanga-Labayen, J.P.; van Labayen, I.V.; Yaun, Q. A review on textile recycling practices and challenges. Textiles 2022, 2, 174–188. [CrossRef]

40. Krifa, M. Electrically conductive textile materials—Application in flexible sensors and antennas. Textiles 2021, 1, 239–257. [CrossRef]

41. Axisa, F.; Dittmar, A.; Delhomme, G. Smart clothes for the monitoring in real time and conditions of physiological, emotional and sensorial reactions of human. In Proceedings of the 25th Annual International Conference, Riverton, NJ, USA, 2–4 November 2015.

42. Cottet, D.; Grzyb, J.; Kirstein, T.; Troster, G. Electrical characterization of textile transmission line. IEEE Trans. Adv. Packag. 2003, 26, 182–190. [CrossRef]

43. Locher, I.; Troster, G. Fundamental building blocks for circuits on textiles. IEEE Trans. Adv. Packag. 2007, 30, 541–550. [CrossRef].

44. Martin, T.; Jones, M.; Chong, J.; Quirk, M.; Baumann, K.; Passauer, L. Design and implementation of an electronic textile jumpsuit. In Proceedings of the 2009 International Symposium on Wearable Computers (ISWC '09), Linz, Austria, 4-7 September 2009; pp. 157-168.

45. Randell, S.; Baurley, M.C.; Muller, H. Textile tools for wearable computing. In Proceedings of the 1st International Forum on Applied Wearable Computing (IFAWC 2004), Bremen, Germany, 30 August-1 September 2004.

46. Textile Trend: 3D Fabric. Available online: https://startupfashion.com/textile-trend-3d-fabric (accessed on 20 October 2022).

47. About Copper. Available online: https://copperalliance.org/sustainable-copper/about-copper/ (accessed on 20 October 2022).

48. 2 Núcleo 3 Núcleo Torcido Cabo Corda de Cânhamo Fio Elétrico Estilo Retro Cobre Cabo da Lâmpada Do Vintage Tecido Fio Têxtil Pingente de Cabo de Luz. Available online: https://pt.aliexpress.com/item/1005002134805048.html?gatewayAdapt=glo2bra (accessed on 20 October 2022).

49. Highly Conductive Pure Silver-Coated Nylon Thread/Yarn for E-Textiles Electronic. Available online: https://www.ebay.ca/itm/274894080543 (accessed on 20 October 2022).

50. Kevlar Yarn 6 6mm Aramid Fiber Rope Used on Tamglass Tempering Furnace Kevlar Rope. Available online: https://leverjimmy.en.made-in-china.com/product/nvbmQGhEIBYo/China-Kevlar-Yarn-6-6mm-Aramid-Fiber-Rope-Used-on-Tamglass-Tempering-Furnace-Kevlar-Rope.html (accessed on 20 October 2022).

51. Kramer, J. Color-Changing Ink Turns Clothes into Giant Chemical Sensors American. Scientific American. 2020. Available online: https://www.scientificamer9ican.com/article/color-changing-ink-turns-clothes-into-giant-chemical-sensors/ (accessed on 25 August 2022).

52. Stojkoski, V.; Kert, M. Design of pH responsive textile as a sensor material for acid rain. Polymers 2020, 12, 2251. [CrossRef].

53. Notman, N.; Turner, K. Temperature-Controlling Textiles. Royal Society of Chemistry—Education in Chemistry. 2020. Available online: https://edu.rsc.org/feature/temperature-controlling-textiles/4011183.article (accessed on 25 August 2022).

54. Service, R.F. This Fabric Can Give You Your Own Personal Climate-Control System. Science (1979). 2017. Available online: https://www.science.org/content/article/fabric-can-give-you-your-own-personal-climate-control-system (accessed on 25 August 2022).

55. Gao, T.; Yang, Z.; Chen, C.; Li, Y.; Fu, K.; Dai, J.; Hitz, E.M.; Xie, H.; Liu, B.; Song, J.; et al. Three-Dimensional Printed Thermal Regulation Textiles. ACS Nano 2017, 11, 11513–11520. [CrossRef]

56. Ru, H.; Liu, Y.; Huang, S.; Ren, X.; Shu, W.; Cheng, J.; Tao, G.; Xu, W.; Chen, R.; Luo, X. Emerging Materials and Strategies for Personal Thermal Management. Adv. Energy Mater. 2020, 10, 1903921. [CrossRef]

57. Gök, M.O.; Bilir, M.Z.; Gürcüm, B.H. Shape-Memory Applications in Textile Design. Procedia Soc. Behav. Sci. 2015, 195, 2160–2169. [CrossRef]

58. Thakur, S. Shape Memory Polymers for Smart Textile Applications. In Textiles for Advanced Applications; InTech: Tokyo, Japan, 2017. [CrossRef]

59. New Cloth Market. Development of Shape Memory Fabrics/Garments. Fibre2Fashion. 2009. Available online: https://www.fibre2fashion.com/industry-article/3983/development-of-shape-memory-fabrics-garments (accessed on 25 August 2022).

60. Huang, Y.; Zhu, M.; Pei, Z.; Xue, Q.; Huang, Y.; Zhi, C. A shape memory supercapacitor and its application in smart energy storage textiles. J. Mater. Chem. A Mater. 2016, 4, 1290–1297. [CrossRef]

61. Mukhopadhyay, A.; Midha, V.K. Waterproof breathable fabrics. In Handbook of Technical Textiles, 2nd ed.; Woodhead Publishing: Sawston, UK, 2016; pp. 27-55. [CrossRef]

62. Interactive Led Fabrics. Available online: https://br.pinterest.com/pin/1137370080867857745/?mt=login (accessed on 10 October 2022).

63. Ganapati, P. Smart Textiles Blend LEDs, Circuits and Sensors. Available online: https://www.wired.com/2010/06/gallery-smart-textiles/ (accessed on 10 October 2022).

Textiles 2022, 2

603

64. Zulqarnain, M.; Stanzione, S.; Rathinavel, G.; Smout, S.; Willegems, M.; Myny, K.; Cantatore, E. A flexible ECG patch compatible with NFC RF communication. NPJ Flex. Electron. 2020, 4, 13. [CrossRef]

65. My Heart Project—Ist 507816. Available online: http://www.hitech-projects.com/euprojects/myheart/ (accessed on 25 October 2022).

66. Create the Change. Available online: https://www.biotexfuture.de/ (accessed on 25 October 2022).

67. Advanced E-Textiles for Firefighters and Civilian Victims. Available online: http://www.proetex.org/ (accessed on 25 October 2022).

68. Innovation in Materials and Substrate Technology. Available online: http://www.stella-project.de/Innovations/tabid/54/Default.aspx (accessed on 25 October 2022).

69. Microflex Dissemination—Details of the Publications and Events Related to the Microflex Project. Available online: http://microflex.ecs.soton.ac.uk/ (accessed on 25 October 2022).

70. Application of Sensor Technology in Textiles. Available online: https://textilelearner.net/sensor-technology-in-textile-industry/#: ~{|:text=Sensor%20is%20an%20instrument%20that,(today%20mostly%20electronic)%20instrument (accessed on 25 October 2022).

71. Eurecat Centre Tecnologic de Catalunya. Available online: https://eurecat.org/en/portfolio-items/dephotex/ (accessed on 25 October 2022).

72. McQuarrie, L. Wearable X Is Launching Smart Yoga Pants for Men and a Redesigned App. Available online: https://www.trendhunter.com/trends/smart-yoga-pants (accessed on 5 October 2022).

73. Sensoria Smart Socks Win 'Best New Wearable Technology Device' Award by IDTechEx. Available online: https://www.innovationintextiles.com/sensoria-smart-socks-win-best-new-wearable-technology-device-award-by-idtechex/ (accessed on 5 October 2022).

74. Rubenov, E. Send Somone a Hug via Text Message. Available online: https://www.trendhunter.com/trends/hug-shirt-send-somone-a-hug-via-text-message (accessed on 5 October 2022).

75. Smart Textiles and Smart Clothing—The New Black for the Internet of Things. Available online: https://www.nanowerk.com/smart/smart-clothing.php (accessed on 5 October 2022).

76. Levi's® Trucker Jacket. Available online: https://atap.google.com/jacquard/products/levi-trucker/ (accessed on 5 October 2022).

77. Top Performance Sportswear Smart Textiles to Watch Out for in 2019. Available online: https://butlertechnologies.com/performance-sportswear-smart-textiles/ (accessed on 5 October 2022).

78. Nadi X Mesh. Available online: https://www.wearablex.com/products/nadi-x-mesh (accessed on 5 October 2022).

79. Ministry of Supply Heated Jacke. Available online: https://eshopu.tk/products.aspx?cname=ministry+of+supply+heated+jacket&cid=69 (accessed on 5 October 2022).

80. Rajandran, S.; Anand, S.C. Developments in medical textiles. Text. Prog. 2002, 32, 1–42. [CrossRef].

81. Shirvan, A.R.; Nouri, A. Chapter 13—Medical textiles. In Advances in Functional and Protective Textiles; Woodhead Publishing: Sawston, UK, 2020; pp. 291–333. [CrossRef]

82. Liposuction Garments. Available online: https://www.indiamart.com/proddetail/liposuction-garments-16709847491.html (accessed on 7 October 2022).

83. The Best Cloth Diaper Inserts for Absorbency and Comfort. Available online: https://nickisdiapers.com/blogs/switch-to-sustainable/most-absorbent-cloth-diaper-fabrics (accessed on 7 October 2022).

84. Kiron, M.I. Medical Textiles: Features, Types and Applications. Available online: https://textilelearner.net/medical-textiles/ (accessed on 7 October 2022).

85. LIVMOA™ 5000 for Infection Control. Available online: https://www.livmoa.toray/en/infection/5000_001.html (accessed on 7 October 2022).

86. Non-Woven Cotton Sanitary Pads Wholesale. Available online: https://www.purcotton.net/oem-service/sanitary-pads/ (accessed on 7 October 2022).

87. McDavid Knee Brace Com Dobradiças Laterais. Suporte Máximo do Joelho & Compressão Para Estabilidade & Recuperação, Suporte ao Tendão da Patela, Alívio. Available online: https://www.extra.com.br/mcdavid-knee-brace-com-dobradicas-laterais-suporte-maximo-do-joelho-compressao-para-estabilidade-recuperação-suporte-ao-tendao-da-patela-alivio/p/1538337866 (accessed on 7 October 2022).

88. A Guide to Cosmetic Prosthetic Devices. Available online: https://www.biotechpossibilities.com/possibilities/a-guide-to-cosmetic-prosthetic-devices (accessed on 7 October 2022).

89. Peng, L.; Su, B.; Yu, A.; Jiang, X. Review of clothing for thermal management with advanced materials. Cellulose 2019, 26, 6415–6448. [CrossRef]

90. Guo, Y.; Li, K.; Hou, C.; Li, Y.; Zhang, Q.; Wang, H. Fluoroalkylsilane-modified textile-based personal energy management device for multifunctional wearable applications. ACS Appl. Mater. Interfaces 2016, 8, 4676–4683. [CrossRef]

91. Peng, L.; Fan, W.; Li, D.; Wang, S.; Yu, A.; Jiang, X. Smart thermal management textiles with anisotropic and thermoresponsive electrical conductivity. Adv. Mater. Tech. 2019, 5, 1900599. [CrossRef]

92. Fang, Y.; Chen, G.; Bick, M.; Chen, J. Smart textiles for personalized thermoregulation. Chem. Soc. Rev. 2021, 50, 9357–9374. [CrossRef]

93. Ünsal, Ö.F.; Hiçyilmaz, A.S.; Yilmaz, A.N.Y.; ALtin, Y.; Borazan, I.; Bedeloğlu, A. Chapter 17—Energy-generating textiles. In Advances in Functional and Protective Textiles; Woodhead Publishing: Sawston, UK, 2020; pp. 415–455. [CrossRef]

94. Tao, X. Smart Fibers, Fabrics and Clothing; CRC Press: Cambridge, UK, 2000; Volume 34.

Textiles 2022, 2

604

95. Military Textiles: The Scope and Future. Available online: https://textilevaluechain.in/in-depth-analysis/military-textilesthe-scope-and-future/ (accessed on 28 September 2022).

96. Medical Smart Textile Market Valuation Worth USD 2.10 Billion by 2027 at 7.51% CAGR—Report by Market Research Future (MRFR). Available online: https://www.globenewswire.com/en/news-release/2022/06/21/2465760/0/en/Medical-Smart-Textile-Market-Valuation-Worth-USD-2-10-Billion-by-2027-at-7-51-CAGR-Report-by-Market-Research-Future-MRFR.html (accessed on 28 September 2022).

97. Rajendran, S. Advanced Textiles for Wound Care; Woodhead Publishing: Sawston, UK, 2018; ISBN 978-0-08-102192-7.

98. Peng, Y.; Sun, F.; Xiao, C.; Iqbal, M.I.; Sun, Z.; Guo, M.; Gao, W.; Hu, X. Hierarchically structured and scalable artificial muscles for smart textiles. ACS Appl. Mater. Interfaces 2021, 14, 45. [CrossRef]

99. Libanori, A.; Chen, G.; Zhao, X.; Zhou, Y.; Chen, J. Smart textiles for personalized healthcare. Nat. Electron. 2022, 5, 142–156. [CrossRef]

100. Global Nanotechnology Clothing Market (2022 to 2031)—Featuring Nano Textile, Colmar and Shanghai Hu Zheng. Nano Technology among Others. Available online: https://www.globenewswire.com/en/news-re%20lease/2022/04/22/2427164/28124/en/Global-Nanotechnology-Clothing-Market-2022-to-2031-Featuring-Nano-Textile-Colmar-and-Shanghai-Huzheng-Nano-Technology-Among-Others.html#:-{:text=The%20global%20nanotechnology%20clothing%20market%20is%20expected%20to%20grow%20from,(CAGR)%20of%2024.6%25 (accessed on 20 September 2022).

101. Shah, M.A.; Pirzada, B.M.; Price, G.; Shibiru, A.L.; Qurashi, A. Applications of nanotechnology in smart tetile industry: A critical review. J. Adv. Res. 2022, 38, 55–75. [CrossRef] [PubMed]

102. Kao, H.L.; Chuang, C.H.; Chang, L.C.; Cho, C.L.; Chiu, H.C. Inkjet-printed silver films on textiles for wearable electronics applications. Surf. Coat. Technol. 2019, 362, 328–332. [CrossRef]

103. Chen, W.D.; Lin, Y.H.; Chang, C.P.; Sung, Y.; Liu, Y.M.; Ger, M.D. Fabrication of high-resolution conductive line via inkjet printing of nano-palladium catalyst onto PET substrate. Surf. Coat. Technol. 2011, 205, 4750. [CrossRef]

104. Wang, M.W.; Liu, T.Y.; Pang, D.C.; Hung, J.C.; Tseng, C.C. Inkjet printing of a pH sensitive palladium catalyst patterns of ITO glass for electroless copper. Surf. Coat. Technol. 2014, 259, 340–345. [CrossRef]

105. Ghahremani Honarvar, M.; Latifi, M. Overview of wearable electronics and smart textiles. J. Text. Inst. 2017, 108, 631–652. [CrossRef]

106. Park, S.; Sundaresan, J. Smart textiles: Wearable electronic systems. MRS Bull. 2003, 28, 585–591. [CrossRef].

107. Qiu, Q.; Zhu, M.; Li, Z.; Qiu, K.; Liu, X.; Yu, J.; Ding, B. Highly flexible, breathable, tailorable and washable power generation fabrics for wearable electronics. Nano Energy 2019, 58, 750–758. [CrossRef]

108. Niu, Z.; Qi, S.; Shuaib, S.S.A.; Yuan, W. Flexible, stimuli-responsive and self-cleaning phase change fiber for thermal energy storage and smart textiles. Compos. Part B Eng. 2022, 228, 109431. [CrossRef]

109. Nigusse, A.B.; Mengistie, D.A.; Malengier, B.; Tseghai, G.B.; van Langenhove, L. Wearable smart textiles for long-term electrocardiography monitoring—A review. Sensors 2021, 21, 4174. [CrossRef]

110. Yin, Z.; Lu, H.; Gan, L.; Zhang, Y. Electronic fibers/textiles for health-monitoring: Fabrication and application. Adv. Mater. Technol. 2022, 2200654. [CrossRef]

111. Guo, L.: Bresky, E.; Persson, N.-K. Electroconductive textiles and textile-based electromechanical sensors—Integration in as an approach for smart textiles. In Smart Textiles and their Applications; Woodhead Publishing: Sawston, UK, 2016; pp. 657-693. [CrossRef]

112. Vanço, M.; Krmela, J.; Pešlová, F. The use of PVD coating on natural textile fibers. Proc. Eng. 2016, 136, 341–345. [CrossRef].

113. Maity, S.; Catterjee, A. Conductive polymer-based electro-conductive textile composites for electromagnetic interference shielding: A review. J. Ind. Text. 2016, 47, 2228–2252. [CrossRef]

114. Kim, H.K.; Byun, S.W.; Jeong, S.H.; Ki Hong, Y.; Joo, J.S.; Song, K.; Park, Y.H.; Lee, J.Y. Environmental stability of EMI shielding PET fabric/polypyrrole composite. Mol. Cryst. Liq. Cryst. 2002, 377, 369–372. [CrossRef]

115. Wilson, J.I.B. Textile surface functionalization by chemical vapour deposition (CVD). In Surface Modification of Textiles; Woodhead Publishing: Sawston, UK, 2009; pp. 126–138. [CrossRef]

116. Stempien, Z.; Khalid, M.; Koanecki, M.; Filipczak, P.; Wrzesińska, A.; Korzeniewska, E.; Sasiadek, E. Inkjet Printing of Polypyrrole Electroconductive Layers Based on Direct Inks Freezing and Their Use in Textile Solid-State Supercapacitors. Materials 2021, 14, 3577. [CrossRef]

117. Chen, D.; Jiang, K.; Huang, T.; Shen, G. Recent advances in fiber supercapacitors: Materials, device configurations, and applications. Adv. Mater. 2019, 32, 1901806. [CrossRef]

118. Weng, W.; Yang, J.; Zhang, Y.; Li, Y.; Yang, S.; Zhu, L.; Zhu, M. A route toward smart system integration: From fiber design to device construction. Adv. Mater. 2020, 32, 1902301. [CrossRef]

119. Rotzler, S.; Kallmayer, C.; Dils, C.; von Krshiwobloski, M.; Bauer, U.; Schneider-Ramelow, M. Improving the washbility of smart textiles: Influence of different washing conditions on textile integrated conductor tracks. J. Text. Inst. 2020, 111, 1766–1777. [CrossRef]

120. Sinner, H. €Uber das Waschen Mit Haushaltswaschmaschinen; HauspHeim Verlag: Hamburg, Germany, 1960.

121. Rotzler, S. Einfluss der Sinnerschen Faktoren Sowie der Textile Substrate Auf die Waschbarkeit Textilintegrienter Leiterbahnen. Master's Thesis, Hochschule für Technik und Wirtschaft Berlin, Berlin, Germany, 2018.

Textiles 2022, 2

605

122. Textile Recycling—CTDEEP. Available online: https://portal.ct.gov/-/media/DEEP/waste_management_and_disposal/Solid_Waste_Management_Plan/June2013/SMARTTextileRecyclingGroipenSWACJune2013pdf.pdf (accessed on 5 November 2022).

123. Chowdhury, P.; Samanta, K.K.; Basak, S. Recent development in textile for sportswear application. Int. J. Eng. Res. Technol. 2014, 3, 1905–1910.

124. Veske, P.; Ilen, E. Review of the end-of-life solutions in electronics-based smart textiles. J. Text. Inst. 2021, 112, 1500–1513. [CrossRef]

125. Gulati, R.; Sharma, S.; Sharma, R.K. Antimicrobial textile: Recent developments and functional perspective. Polym. Bull. 2022, 79, 5747–5771. [CrossRef] [PubMed]

126. Snari, R.M.; Alsahag, M.; Alisaac, A.; Bayazeed, A.; Alsoliemy, A.; Khalifa, M.E.; El-Metwaly, N.M. Smart textiles immobilized with hydrazone probe for colorimetric recognition of bacteria. J. Mol. Liq. 2022, 366, 120149. [CrossRef]

127. Nie, X.; Wu, S.; Huang, F.; Wang, Q.; Wei, Q. Smart textiles with self-disinfention and photothermochromic effects. ACS Appl. Mater. Interfaces 2021, 13, 2245–2255. [CrossRef] [PubMed]

