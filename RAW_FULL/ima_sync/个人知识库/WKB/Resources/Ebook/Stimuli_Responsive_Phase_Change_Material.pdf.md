---
media_id: "pdf_3867e2b60070d7dc3f413086d0b0036e_e2b86e1216024993270cbd7e67f9df5d001a693ee6c0644e"
source_file: "Stimuli_Responsive_Phase_Change_Material.pdf.md"
original_path: "RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Stimuli_Responsive_Phase_Change_Material.pdf.md"
extracted: "2026-09-27"
extract_method: "ima-mcp fetch_media_content"
extract_status: "ok"
clean_rules: "v2: dead-image-link->text(alt kept); repeat-digits->compressed"
processed: "2026-09-27"
---

# Stimuli_Responsive_Phase_Change_Material.pdf.md

8
materials

MDPI

Review

# Stimuli-Responsive Phase Change Materials: Optical and Optoelectronic Applications

Irene Vassalini $^{1,2,3,*}$ ID, Ivano Alessandri $^{1,2,3}$ ID and Domenico de Ceglia $^{3,4,*}$ ID

## check for updates

Citation: Vassalini, I.; Alessandri, I.; de Ceglia, D. Stimuli-Responsive Phase Change Materials: Optical and Optoelectronic Applications. Materials 2021, 14, 3396. https://doi.org/10.3390/ma14123396

Academic Editor: Guido Panzarasa

Received: 21 May 2021Accepted: 17 June 2021Published: 19 June 2021

Publisher's Note: MDPI stays neutral with regard to jurisdictional claims in published maps and institutional affiliations.

[图片: ④人日]
Copyright: © 2021 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https://creativecommons.org/licenses/by/ 4.0/).

1 INSTM, Research Unit of Brescia, Via Branze 38, 25123 Brescia, Italy; ivano.alessandri@unibs.it

2 Department of Information Engineering, University of Brescia, Via Branze 38, 25123 Brescia, Italy

$^{3}$ CNR-INO, Research Unit of Brescia, Via Branze 38, 25123 Brescia, Italy

$^{4}$ Department of Information Engineering, University of Padova, Via Gradenigo 6/a, 35131 Padova, Italy

* Correspondence: irene.vassalini@unibs.it (I.V.); domenico.deceglia@unipd.it (D.d.C.)

Abstract: Stimuli-responsive materials offer a large variety of possibilities in fabrication of solid-state devices. Phase change materials (PCMs) undergo rapid and drastic changes of their optical properties upon switching from one crystallographic phase to another one. This peculiarity makes PCMs ideal candidates for a number of applications including sensors, active displays, photonic volatile and non-volatile memories for information storage and computer science and optoelectronic devices. This review analyzes different examples of PCMs, in particular germanium-antimonium tellurides and vanadium dioxide ($VO_2$) and their applications in the above-mentioned fields, with a detailed discussion on potential, limitations and challenges.

Keywords: phase change materials; GST; $VO_2$; thin films; metasurfaces; active photonics; displays; optical switches; memories

## 1. Introduction

The optical properties of photonic devices are usually fixed at the time in which the devices are designed and then fabricated. A stimulating challenge in optics and photonics is to go beyond this static, passive behavior, and to gain some degree of control over the optical response, with the ultimate goal to achieve dynamically tunable, or even reconfigurable, optical functionalities [1,2]. The complication in achieving this goal derives from the fact that the most common materials used in photonics, such as glass for fiber optics and silicon for integrated photonics, hardly change their optical properties, even under intense optical or electrical stimuli. For this reason, optical modulation and switching, and more generally tunability, are usually reached by means of free-carrier injection, chemical and mechanical activation, or by deploying materials with large electro-optic or optical nonlinear coefficients [3-7]. All these mechanisms are inherently weak and require intense control signals and long interaction lengths in order to produce significant optical modulation. For this reason, researchers have devoted a great deal of attention to finding new, "smart" materials, in which the change of the refractive index can be large and, at the same time, accessible with relatively low-intensity stimuli.

In this context, Phase Change Materials (PCMs) represent a specific class of solid-state materials that undergo a transition from a given crystallographic phase to another one in response to an increase of temperature. This transition is combined with a significant variation of material optical and electrical properties [8,9]. They can be considered as a particular type of stimuli-responsive materials, since they modulate their electrical and optical behaviors in response to the application of an external stimulus, which leads to a variation of temperature. This stimulus can be delivered by direct heating, application of an electrical potential (the enhancement of temperature is a consequence of Joule heating) or laser pulses (laser heating). In particular, in response to the external stimulus PCMs pass from a phase characterized by low reflectivity, low refractive index, low dielectric optical

Materials 2021, 14, 3396

2 of 36

constant and high resistivity (they behave as semiconductors) to a phase characterized by high reflectivity, high refractive index, high dielectric optical constant and low resistivity (they behave as metals) [1,10]. From this general description, it is evident that they can be employed in the preparation of photonic devices (that guide, manipulate and detect light), which are able to modify their function in response to external stimuli, behaving in a dynamic way. This possibility opens the way to the development of new competitive photonic systems, characterized by adjustable optical properties and on-demand functionalities.

The main aim of this work is to analyze and discuss recent and selected examples that can be found in the literature of photonic systems obtained by using phase change materials which find applications in three particular fields: colored dynamic displays, optical switching and memory/logic devices.

# 2. Types of Phase-Change Materials and Their Properties

In general, in PCMs the two phases exhibit high contrast of the optical constants ($\Delta n > 1$) over a broad wavelength range, from the visible to the infrared (IR) range [11]. The most studied and most frequently applied class of materials is that of chalcogenides, which are composites of elements of the XVI group of the periodic table (S, Se, Te) with Ge, As, Sb or Ga. In particular, the group of composites located on the GeTe-Sb₂Te₃ tie line in the ternary phase diagram for Ge, Sb and Te, such as GeSb₂Te₄ (GST124) and Ge₂Sb₂Te₅ (GST225) (Figure 1a). Their phase change transition has been widely studied and it has been pointed out that their significant variation of electrical and optical properties is ascribed to a variety of types of bonds between the different atoms passing from amorphous (covalent bond) to crystalline phase (resonant bonding) [12]. The presence in the crystalline phase of resonant bonding (i.e., a single, half-filled p-band forms two bonds to the left and right (more than allowed by the 8-N rule)) has been identified as a unique fingerprint of this type of PCMs, that is obtained when the bond between the atoms in the crystalline phase are characterized by small ionicity and a limited degree of hybridization [13]. The materials are characterized by low reflectivity and low values of refractive index and extinction coefficient in the amorphous state, while the refractive index and extinction coefficient values significantly increase upon crystallization, leading to high reflectivity. In Figure 1b–d, the case of Ge₂Sb₂Te₅ is reported as an example.

[图片: 未能识别到文本内容]
[图片: |Wavelength (nm)|n (aGST)|n (cGST)|κ (aGST)|κ (cGST)| |:---:|:---:|:---:|:---:|:---:| |200|1|1|3|1| |700|4|5|1|4| |1200|4|6|0|3| |1700|4|6|0|1|]
[图片: |Wavelength (μm)|aGST|cGST| |:---:|:---:|:---:| |3.0|4.0|6.0| |3.4|3.98|5.9| |3.8|3.97|5.85| |4.2|3.96|5.8| |4.6|3.95|5.75| |5.0|3.95|5.7| |5.4|3.94|5.67| |5.8|3.94|5.65|]
[图片: |Wavelength (μm)|aGST|cGST| |:---:|:---:|:---:| |3|0|0.5| |3.4|0|0.6| |3.8|0|0.7| |4.2|0|0.8| |4.6|0|0.9| |5|0|1.0| |5.4|0|1.1| |5.8|0|1.2|]
# Figure 1. (a) Ternary phase diagram for Ge, Sb and Te showing most common chalcogenide phase change materials; (b) variation in the visible range of the real (n) and imaginary (k) part of the refractive index of $Ge_2Sb_{2}Te_5$ ($GST225$) upon phase transition [14]; (c) variation in the IR range of the real (n) part of the refractive index of GST225 upon phase transition [15]; (d) variation in the IR range of the imaginary (k) part of the refractive index of GST225 upon phase transition [15]. Reproduced from Refs. [14,15] with permission from Optical Society and MDPI.

Materials 2021, 14, 3396

3 of 36

For this class of PCMs, crystallization occurs with heating in the range between 100 and

180 ◦C (with an increase of the transition temperature Tc moving from Sb2Te3 towards GeTe, and an increasing of Tc upon reducing the thickness of the material ﬁlm or enhancing the residual stress to which it is subjected), while the melting point is around 600 ◦C (also,in this case, the glass transition temperature increases, moving from Sb2Te3 towards GeTe).

Other interesting features are that the phase transition is very quick (in the order of ps-ns for amorphization and in the order of sub-nanoseconds and nanoseconds for crystallization)and not-volatile. The high rate of switching between the two different phases is justiﬁed by the fact that they are characterized by similar atomic arrangements [12]. For example,Ge2Sb2Te5 has an f.c.c structure when crystalline, which is characterized by high- grade lattice symmetry, similar to that of the amorphous state. Thus, upon crystallization, the atoms have to move only a little to achieve the right position inside the crystal structure.

The key point to underscore is that the phase transition and related change of properties are permanent and non-volatile. This means that they are retained also after the removal of the inducing stimulus (i.e., temperature increase). This feature is highly suitable in many applications, because it enables us to create devices and functionalities that require a very low amount of energy to operate, just the one needed to induce the phase transition.

Once crystallization is obtained, it is possible to revert the material back to the amorphous phase by heating it to a temperature higher than its melting point and making cooling happen quickly. In this case, it is possible to exploit both direct heating, or electric or laser pulses. In this case, after the removal of the external stimulus the chilling of the material has to be fast, so that the material atoms have no time to arrange themselves in the ordered crystalline structure. Switching between the amorphous and crystalline phases can be repeated various times, adjusting temperature properly. For example, different devices have been prepared with the capability of 105 switching cycles for optical storage applications, or 106−17 switching cycles for memory applications (106−8 cycling capability is required for replacing ﬂash memories, 1012 cycling capability is required for embedded memories and up to 1015−17 cycling capability is required for replacing standalone or embedded Dynamic RAM) [16,17].

Other materials included in this review are GeTe [18], Ge2Sb2Se4Te1 [19], Sb2Te3 [20],Ag3In4Sb76Te17 [21] and InSb [22]. All of them exhibit properties and responses that are similar to Ge2Sb2Te5.

On the other hand, special attention will be dedicated to vanadium oxide, VO2. Despite it is an oxide, it shares with the above-mentioned chalcogenide a crystallographic phase transition which leads to a signiﬁcant change of refractive index and increases in conductivity. In this case, the material passes from monoclinic (insulating) to tetragonal (metallic) rutile structure (at T~68 ◦C). Above Tc, the electrical resistance lowers by 3–5 order of magnitude and there is a dramatic change of the optical properties in the Vis-IR region (Figure 2). Below Tc, VO2 is in the monoclinic phase and the V atoms pair with a high localization of d-electrons which leads to the formation of an energy gap of

0.6 eV, permitting high IR transmission. On the contrary, at temperatures higher than the transition temperature, there is an overlap between the Fermi level and the V 3d band which eliminates the aforementioned band gap, causing the material to be highly reﬂective or opaque in the near-infrared (NIR) region.

Unlike the GSTs and, more generally, chalcogenides, in VO2 the phase transition is volatile. This means that, once direct or indirect heating is stopped and temperature comes back to a value lower than transition temperature, the newly acquired properties are lost.

Materials 2021, 14, 3396

4 of 36

# a)

[图片: monoclinicrutileT>TT<Tc6metainsulatora0]
# b)

[图片: |Wavelength (nm)|VO₂ S (n)|VO₂ M (n)|ITO (n)| |:---:|:---:|:---:|:---:| |400|2.7|2.3|2.2| |500|2.6|2.4|2.1| |600|2.3|2.1|2.0| |700|2.2|1.9|1.9| |800|2.2|1.7|1.8| |900|2.2|1.5|1.7| |1000|2.3|1.3|1.6|]
# c)

[图片: |Wavelength (nm)|VO₂ S|VO₂ M|ITO| |:---:|:---:|:---:|:---:| |300|1.8|1.5|0| |400|1.0|1.5|0| |500|0.5|0.8|0| |600|0.3|0.6|0| |700|0.4|0.7|0| |800|0.5|0.8|0| |900|0.6|1.0|0| |1000|0.7|1.3|0|]
# Figure 2. (a) Insulator to metal phase-change transition in $VO_2$ [23]; (b) variation in the visible range of the real part of the refractive index of $VO_2$ upon phase transition [24]; (c) variation in the visible range of the imaginary (k) part of the refractive index of $VO_2$ upon phase transition [24]. Reproduced from Refs. [23,24] with permission from Nature Springer and IOP publishing.

# 3. Variably Colored and Writable Displays

Phase change materials have been widely exploited for the preparation of both variably colored displays, where the color of the final device is determined by the morphological properties of the structure (such as PCM thickness, shape, spacing, phase, etc.), and writable displays, where the capability of the material of changing optical properties in response to external stimuli is exploited to store optical information (writings) with precise spatial and temporal control. In the following, different strategies will be illustrated according to the different types of involved materials. In general terms, the employment of PCMs represents an efficient alternative possibility to store optical information, which enriches the palette of strategies that can be found in the literature [25–31]. In particular, it entails some advantages: the possibility of achieving not only binary systems but multicolor devices with precise color depth modulation, the possibility of exploiting different stimuli (especially, laser and voltage), precise spatial control and very quick actuation. In addition, in the proposed devices, PCMs are especially in the form of thin films, requiring only a small amount of materials, and enabling the obtainment also of flexible devices.

## 3.1. Colored and Dynamic Displays Based on Interference Effect with Chalcogenides

One of the first demonstrations of the use of a phase change material for the preparation of colored display that can be found in literature is the work of Hossein et al. [32], which is based on the employment of a Fabry–Pérot cavity made of two layers of Indium Tin Oxide (ITO), filled with Ge₂Sb₂Te₅, which serves as a highly absorptive medium (Figure 3a). According to the type of substrate on which this stacked structure is deposited, it is possible to obtain a reflective (deposition on a refractive surface made of Pt) or a semi-transparent (deposition on a transparent material, such as quartz) display. Similarly, they demonstrated that it is possible to achieve both flexible (deposition on transparent boPET or Pt-covered boPET) and not-flexible devices. The final color of the display depends on the thickness of the bottom layer of ITO (since it determines the resonance condition of the whole cavity) and on the thickness of the Ge₂Sb₂Te₅ layer. The same research group developed a theoretical model that enables us to simulate and predict the reflective spectrum of the multilayered system and convert it, by means of an algorithm, into the corresponding final color [33]. Thanks to these simulations it has been possible to determine the maximum thickness of the GST225 layer, which has to be lower than 25 nm, otherwise, the final display tends to a constant grey color, typical of bulk GST225. In addition, according to this model, it is possible to achieve a maximum value of contrast between the reflective spectrum of the whole system with GST225 in the amorphous or in the crystalline state, when the GST225 layer

Materials 2021, 14, 3396

5 of 36

has a thickness lower than 10 nm. The most striking feature of the proposed system, in fact, is that by changing the crystallographic state of the GST225 layer it is possible to induce a variation of its refractive index, which is converted into a modification of the reflectivity (or transmission) spectrum of the whole stack, as visible in Figure 3b. Practically, this means a dynamic variation of the display color, in response to the phase change of the GST225 layer. For example, when the bottom ITO layer is 180-nm thick, and the GST225 layer has a thickness of 7 nm, the display is pink-purple if GST is in the amorphous state, and orange if GST is in the crystallin state, indicating a significant blueshift of the cavity resonance upon crystallization (Figure 3c). The authors demonstrated that it is possible to achieve this color modification by heating the whole structure or by applying a sufficient difference of potential (electrical stimulation) between the upper and the bottom layers of ITO thanks to the employment of a conductive tip. In particular, they created a pixelated display, in which each pixel can be independently accessed through the interaction with a conductive tip of an atomic force microscope (CAFM) in order to apply the sufficient difference of potential and make the GST225 phase transition occur. This strategy has been employed to reproduce photography in a bimodal color scale (Figure 3d).

# a)

[图片: ITOGST225ITO (t)substratet=50nmt=120nmt=50nmcrystallinec)crystallineamornbous]
# b)

[图片: |Wavelength (nm)|Amorphous, measured t = 50 nm|Amorphous, measured t = 70 nm|Amorphous, measured t = 120 nm|Amorphous, measured t = 180 nm|Crystalline, measured t = 50 nm|Crystalline, measured t = 70 nm|Crystalline, measured t = 120 nm|Crystalline, measured t = 180 nm| |:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:| |350|0.4|0.6|0.6|0.0|0.4|0.6|0.6|0.0| |400|0.3|0.5|0.2|0.0|0.3|0.5|0.2|0.0| |450|0.2|0.3|0.5|0.0|0.2|0.3|0.5|0.0| |500|0.1|0.2|0.8|0.0|0.1|0.2|0.8|0.0| |550|0.0|0.1|0.8|0.0|0.0|0.1|0.8|0.0| |600|0.0|0.1|0.7|0.4|0.0|0.1|0.7|0.4| |650|0.0|0.0|0.7|0.8|0.0|0.0|0.7|0.8| |700|0.0|0.0|0.6|0.9|0.0|0.0|0.6|0.9| |750|0.0|0.0|0.5|1.0|0.0|0.0|0.5|1.0|]
[图片: t=50nmt=120nmc)crystallinecrystallineamorphousamorphot=70nmt=180nmcrystallinecrystallinet=180nmt=70nmamorphousamorphou]
[图片]
# Figure 3. (a) Scheme of the structure proposed by Hosseini et al. [32] to obtain a colored display; (b) variation of the Reflectivity spectrum of a device consisting of 10 nm ITO/7 nm GST225/t ITO/Pt mirror, with different thickness t, upon phase transition; (c) optical pictures of different devices consisting of 10 nm ITO/7 nm GST225/t ITO/Pt mirror, with different t, in different phases; (d) employment of a 10 nm ITO/7 nm GST225/70 nm ITO/Pt mirror device for the reproduction and storage of a greyscale picture of the Oxford Radcliff Camera (original picture shown in the left). Clear regions correspond to amorphous GST225, dark blue regions correspond to crystalline GST225. The scale bar is 10 µm. Reproduced from Ref. [32] with permission from Nature Springer.

The GST225 phase transition is not-volatile, leading to permanent storage of optical information, with reduced energy consumption. In fact, it is necessary just to supply to the system the energy necessary to cause the first (amorphous → crystalline) transition. Nevertheless, it is possible to erase the stored optical information on demand, by inducing a subsequent re-amorphization of the "drawn" pixel, thanks to the application of a higher-energy stimulus. The authors estimated that in the optimized display (with a very thin GST225 layer of 7 nm) the voltage threshold for the "writing" of one pixel is 2.2 V, while a

Materials 2021, 14, 3396

6 of 36

pulse of 5 ns and 5 V is necessary for the erasing process (with a total energy consumption of only 15 pJ).

The first possibility of achieving a not-binary color rendering of an image is reported by Rios et al. [21] The exploited system is analogous to the one just described, but in this case, the entity of the variation of color is linked to the amount of crystalized PCM in a certain CAFM scanned area. If the separation between two nuclei of crystallization is larger than the size they grow after the voltage pulse, some amorphous material remains in between, and the obtained final color is intermediate between those of the whole-amorphous and whole-crystalline state. Interestingly, they demonstrated that the nuclei size depends on the applied voltage, while the entity of separation relies on the scanning speed. So, by increasing the applied voltage (from 2 to 10 V) they were able to achieve a perceptible color depth modulation, which is linked to a different crystallization degree of the PCM layer (Figure 4a). In this case, the final color of the display dynamically depends on the crystallographic state of the PCM material, while statically depends on the thickness of both the PCM and the upper ITO reflective layer. In this work, the authors investigated as PCM both Ge₂Sb₂Te₅ and Ag₃In₄Sb₇₆Te₁₇ (AIST). Figure 4b gives as an example the possibility of a storage a greyscale image on a 10 nm ITO/7 nm AIST/70 nm ITO with perceptible color depth modulation. Despite the two materials are characterized by different crystallization dynamics (GST225 undergoes nucleation dominated crystallization, while AIST a growth dominated crystallization) they enable us to obtain displays with very similar properties and performances, with a slightly better depth modulation capability and broader color gamut in the case of AIST.

[图片: 未能识别到文本内容]
# Figure 4. Non-binary grayscale image rendering. (a) different colors in reflection mode obtained by scanning voltage varying between 0 and 10 V and inducing different grades of crystallization by means of CAMS; (b) reproduction and storage of a greyscale picture of the boat picture shown in the left. The used device is a stacked 10 nm ITO/7 nm AIST/70 nm ITO/Pt sample. Reproduced from Ref. [21] with permission from Wiley.

The possibility of achieving a multilevel optical tuning thanks to a gradual crystallization of the PCM layer inside a Fabry–Pérot cavity has been reported also by Meng et al. [34], who employed as PCM C-doped Sb₂Te₃, which is characterized by a very fast growth-dominated crystallization process, and, thanks to C-doping, by a continuous variation of crystallization degree as a function of temperature (not ON/OFF switching behavior). They demonstrated that by means of single-shot ultrafast (ps) laser pulses characterized by different laser fluence (14–32 mJ/cm $^{2}$) it is possible to control the extent of the crystallized area and obtain 6 different reflectivity levels.

Another strategy that can be employed to achieve multiple color switching is that of preparing multilayered structures, which contain more than one layer made of a PCM characterized by different thicknesses, separated by thermal/diffusion barriers. As anticipated in the previous paragraph, in the case of thin (<10 nm) film, the crystallization temperature of Ge₂Sb₂Te₅ is significantly affected by thickness (Tᵉ significantly increases with decreasing film thickness). For example, Yoo et al. proposed a multilayered structure

Materials 2021, 14, 3396

7 of 36

composed of an 8 nm-thick GST225 layer, 6 nm-thick $Ta_2O_5$ thermal barrier layer, 5 nm-thick GST225 layer, ITO layer (whose thickness influences the final display colors) and Pt layer [35]. Since the upper GST225 layer is characterized by a major thickness, it crystalizes at a lower temperature than the underlying thinner GST225 layer. So, when the whole system is subjected to a moderate stimulus (annealing at 210 °C) only the thicker upper layer of GST225 undergoes the phase transition, while when the system is subjected to a more intense stimulus (annealing at 260 °C) both the GST225 layers crystallize (Figure 5a). Gradual crystallization leads to a progressive shift of the reflectance curves towards a shorter wavelength, enabling to obtain three different colors (Figure 5b). The authors theoretically demonstrated that, in general, it is possible to achieve a display that can switch between $(n+1)$ different colors, by stacking n PCM layers. The upper limit for n turns out to be 4. They demonstrated that it is possible to obtain color-switching also electrically, by applying different voltage biases: when a 2 V bias is imposed, only the thicker GST225 layer crystalizes, while at 4 V applied, both layers undergo a phase transition. The result is that three different colors can be dynamically visualized in the display (Figure 5c).

[图片: graph TD A1[thicker GST225 Ta2O5 thinner GST225 ITO/Pt substrate] -->|moderate stimulus| A2[crystalline GST225 Ta2O5 amorphous GST225 ITO/Pt substrate] A1 -->|intense stimulus| A3[crystalline GST225 Ta2O5 crystalline GST225 ITO/Pt substrate]]
# Figure 5. Examples of displays that can dynamically switch between more colors based on multilayered structures, which contain more than one layer made of a PCM. (a) Different PCM layers are characterized by different thicknesses and, as a consequence, different crystallization temperatures, so it is possible to achieve a selective crystallization of GST225 according to the intensity of the applied stimulus. Upon moderate heating or applied potential, only the thicker layer crystallizes, upon intense heating or applied potential both the GST225 layers crystallize; (b) measured reflectance spectra for 8 nm GST225/6 nm $Ta_2O_5$/5 nm GST225/150 nm ITO/Pt device upon different grades of stimulus and crystallization [35]; (c) optical microscope image (scale bar: 10 µm) of the phase and color transition induced by applying different potentials [35]. Reproduced from Ref. [35] with permission from the American Chemical Society.

Similarly, Jafary et al. recently proposed a reconfigurable color reflector by means of a selective phase transition in a multilayered structure obtained by staking GeTe layers of different thickness [36]. In this work, the employed PCM is GeTe (whose crystallization temperature varies according to the material thickness, similarly to GST225) and the employed stimulus for the occurrence of the phase transition and the color variation is Joule heating, by means of heaters integrated inside the structure. They demonstrated the appearance of four (2n) different colors, when two (n) layers of GeTe are involved: red when both GeTe layers are in the amorphous state, orange when only the bottom thinner layer is crystalline, green when only the upper thicker layer is crystalline and dark blue when both the layers are crystalline.

A reconfigurable color reflector based on selective phase change in different layers has been proposed also by Meng et al., but by employing different phase change materials characterized by different phase change transition temperatures: GST225 (transition at ~160 °C) and $VO_2$ (transition at ~70 °C) [37]. The optimized nanostructure is a multilayer device, in which the layers are deposited in the following order from the bottom to the top: $SiO_2/VO_2$ (70 nm)/GST225 (50 nm)/Al(100 nm). According to the phase-type of $VO_2$ and GST225, four different reflectivity levels can be reached at four different temperatures, with a total reflectivity change of 44% over the whole visible spectrum. At room temperature, the structure is 87% reflective (this corresponds to the first reflective state); by heating the whole system up to 72 °C the reflectivity decreases to ~68%, indicating the metal-

Materials 2021, 14, 3396

8 of 36

to-insulator transition of the $VO_2$ layer, thus producing the second reflective state; by increasing furtherly the temperature up to 158 °C, the GST225 layer undergoes a structural phase transition, thus decreasing the overall reflectivity to the third reflective state of ~56%. Upon cooling from 200 °C to ambient temperature, a fourth reflective state of ~100% is achieved at 44 °C, which is due to the $VO_2$ reversible transition back to an insulator behavior. Upon cooling, only one transition occurs, because the GST225 layer remains in its metastable, f.c.c. phase.

Similar switchable and writable colored displays based on strong interference phenomenon are the systems reported by Schlich et al. based on a GST225 layer deposited on Au film and separated by a Ti/TiN layer, which acts as a diffusion barrier, and whose color switch has been obtained by means of fs-laser pulses [38], or the work by Shi et al., employing a GST225 thin layer deposited on a SiO₂ dielectric layer and an Al mirror thick film [39].

# 3.2. Colored and Dynamic Displays Based on Structured Metasurfaces Containing Chalcogenides

Another strategy is based on the exploitation of analogous multilayered structures, where at least the upper layer is a structured metasurface. An example is the work of Gholipour et al., reporting a multilayered structure of subwavelength nanograting arrays made of ZnS/SiO₂, GST225, ZnS/SiO₂ deposited on a quartz substrate [40]. The presence of subwavelength period nanograting introduces resonances for TM-polarized light (which is incident perpendicularly to the grating lines) in the visible range. The precise value of the wavelengths of these resonances depends on the grating period, the line depth of the grating and the crystallographic state of the GST225 layer. When GST225 is in the amorphous state, resonances are due to displacement currents associated with the high refractive index contrast between dielectric GST225 and the surrounding medium; on the contrary, when GST225 is in the crystalline state, they are plasmonic resonances based upon the opposite sign of the real part of the relative permittivity at the interface between GST225 and the surrounding medium. Since different values of resonance wavelength mean different color, changing the grating period or the line depth enables to obtain a static variation of display color. In addition, the modification of the GST state enables to achieve a dynamic modulation of color display, in response to the application of an external stimulus, such as annealing or laser fs-pulses.

Carrillo et al., instead, proposed a layered structure made of a top aluminum layer patterned into circles deposited on a stack of ITO, GeTe and Al layers [41] (Figure 6a). Al has been chosen because it supports a plasmonic behavior in the visible range and it is easily manipulable, ITO has been chosen because it provides environmental protection from oxidation of GeTe and because it is transparent, while GeTe has been chosen for its phase change properties. In particular, when GeTe is in its crystalline form, it is characterized by a metallic-like behavior with a negative value of the real part of permittivity, which enables us to support and confine a resonant mode in the ITO layer for a specific spectral band. In this way, light with a particular wavelength (equal to the $\lambda$ of the resonance) is absorbed by the system. This resonant absorption enables the generation of a particular color, which depends on the properties of the structured metasurface (diameter of the Al circles in the top layer, periodicity of the metasurface) and thickness of the ITO layer. By varying these parameters, it is possible to obtain displays characterized by a different color: cyan (strong resonant absorption in red waveband), magenta (strong resonant absorption in green waveband) or yellow (strong resonant absorption in blue waveband) (Figure 6b–d). On the contrary, when GeTe is in the amorphous state, no resonances are supported, no light absorption at a particular wavelength occurs and the whole system is characterized by an essentially flat reflectance spectrum, which leads to a white-like color. So, the phase switching of GeTe enables us to obtain an on/off control of resonance. Experimentally, the authors use these structures for the preparation of fixed bi-color displays, by combining different pixels, obtained from structures with a different thickness/circle dimension, all in the crystalline state (Figure 6e); or dynamic bi-color displays, obtained by combining

Materials 2021, 14, 3396

9 of 36

identical pixels, some of which are maintained in the amorphous (white) state, while some others are converted into the crystalline (colored) state (Figure 6f). In this case, switching and writing are obtained by means of laser scanning.

# a)

[图片: ITOGaleAI]
[图片: (q6EwuI]
[图片: c)278nm181nm]
[图片: (P240nmwugst]
[图片]
[图片: 未能识别到文本内容]
[图片: |wavelength (nm)|amorphous|crystalline| |:---:|:---:|:---:| |400|0.4|0.4| |500|0.2|0.1| |600|0.3|0.2| |700|0.3|0.3|]
[图片: |wavelength (nm)|amorphous|crystalline| |:---:|:---:|:---:| |400|0.1|0.1| |500|0.2|0.2| |600|0.3|0.3| |700|0.3|0.3|]
# Figure 6. (a) Scheme of the structure proposed by Carillo et al. [41] for the obtainment of a colored display, employing a structured metasurface; (b-d) SEM images and corresponding Reflectance spectra of cyan (b), magenta (c) and yellow (d) pixels. Color variation is obtained by changing morphological parameter of the metasurface (disk diameter and periodicity), as reported in the SEM images; (e) optical picture of fixed bi-color displays, obtained by combining different cyan and magenta pixels in the crystalline state; (f) optical picture of dynamic bi-color displays, obtained by combining same cyan pixels, some in the amorphous and some in the crystalline state. Reproduced from Ref. [41] with permission from Wiley.

# 3.3. Colored and Dynamic Displays Based on $VO_2$

As it can be seen, the incorporation of chalcogenide within thin-film stacks is a strategy that has been widely explored in recent years to obtain dynamic color tunability in response to phase change transitions. However, some concerns related to the use of GST225, AIST and other chalcogenides can arise: they are quite toxic; they are characterized by a high light absorption capability, especially when in the conductive state, which limits their employment only in the form of very thin film (<10 nm), with a consequent enhancement of difficulties during the fabrication procedure; and the phase transition occurs at high temperature, leading to significant power consumption. More recently, researchers have begun to investigate $VO_2$ as a viable alternative, also for applications in the field of dynamically tunable colored displays, that can be exploited also for the storage of graphical information. The main limitations are related to the fact that, in this case, the phase transition is volatile, so images and writings can be stored just for a limited period of time and undergo a spontaneous self-erasing process in few seconds, and that the refractive index variation is greatest in the infrared and microwave spectral range, rather than in the visible. This fact has initially led to the development of displays for the visualization of tunable images with encoded infrared data [42,43]. However, at $\lambda < 700$ nm the phase transition produces a maximum change of 60% in n and of 20% in k, enabling the production of tunable colored displays based on $VO_2$ also in the visible range, with the advantages of low toxicity, limited power consumption and easy fabrication (for $VO_2$ film deposition different techniques are available, ranging from sputtering, molecular beam epitaxy to plasma laser deposition).

## 3.3.1. Applications in the IR Range

As regards applications in the IR range, an interesting work is that of Chandra et al. related to a multi-stack structure composed of a complementary gold hole/disk array, a

Materials 2021, 14, 3396

10 of 36

tri-layered cavity spacer (which is composed of a layer of photoresist polymer SU-8, a layer of $VO_2$ and a layer of $SiO_2$) and a reflective back mirror [42] (Figure 7a).

[图片: a)AuRDSU8VO2LSSiO2Mirror]
[图片: b3.252.731.642.18]
[图片: |Wavelength (µm)|Semiconductor Reflectance (%)|Metal Reflectance (%)| |:---:|:---:|:---:| |6|~100|~0| |8|~95|~95| |10|~99|~99| |12|~99|~99| |14|~98|~99| |16|~0|~99|]
[图片: 未能识别到文本内容]
# Figure 7. (a) Scheme of the structure proposed by Chandra et al. [42] for the encoding of IR images. $L_M$ stands for the cavity length when $VO_2$ is metallic, $L_S$ stands for the cavity length when $VO_2$ is in the semiconductor phase and $R_D$ stands for the relief depth of the Au-SU8 metasurface; (b) SEM images and corresponding Reflectance spectra of different structures with Au holes characterized by different diameters, bot for metallic and semiconductor $VO_2$. Scale bar corresponds to 2 µm; (c) FTIR scan generated images of the plasmonic surface acquired for (from the left to the right) semiconducting ($T = 295$ K), phase-separated ($T = 320$ K), and metallic ($T = 360$ K) states of $VO_2$. Albert Einstein image is $1.3 \times 1.7$ mm$^2$. Reproduced from Ref. [42] with permission of the American Chemical Society.

It is a multilayered cavity-coupled plasmonic system, whose tunability is based on the fact that cavity length changes according to the $VO_2$ phase (it increases when $VO_2$ is a semiconductor), and, as a consequence, the resonance wavelength of the whole structure is altered. In particular, when $VO_2$ is metallic, it behaves like a mirror and the effective cavity length is remarkably shortened, no Fabry-Pérot modes are sustained, and the device reflects about 80% light almost uniformly across the IR band. So, absorption peaks can be observed at low temperatures, but they vanish upon heating. According to the thickness of $SiO_2$, $VO_2$, and SU-8 layers, as well as periodicity and diameter of the hole/disk array, the position of the Fabry-Pérot assisted localized surface plasmon resonance changes, introducing further tunability. In fact, the design parameters can be optimized to achieve at low-temperature infrared absorption at any desired wavelength. The possibility of using this type of system for the infrared-coded image has been demonstrated by preparing a device with the surface characterized by differently sized holes, which enables us to introduce different resonance wavelengths inside the same structure and different reflectance spectra (Figure 7b). Each hole corresponds to a pixel, and the greyscale values of the desired image can be mapped to hole diameters. Therefore, it is possible to convey information from the visible to the infrared domain. Hyperspectral imaging of this infrared encoded image is then performed: the FTIR spectrum for a single pixel is acquired at room temperature and it is analyzed to obtain the infrared coded image. By heating up the device, the image quality deteriorates until completely disappearing, when the temperature reaches values higher than $VO_2$ phase transition, since the reflection of all the pixels simultaneously flattens to 80% (Figure 7c).

An opposite behavior (image appearance in the IR range upon heating, and disappearance upon cooling) is reported by Nagasaki et al., who propose a metasurface composed of cylindrical $VO_2$ nanostructures periodically arranged on a sapphire substrate [43]. In this case, the switching between the semiconductor and the metallic phase leads to a modification of the phenomenon at the basis of the observed resonances, with a considerable variation of the reflection spectrum. In the case of the low-temperature phase, the antenna is composed of a dielectric and Mie resonances are excited inside the nanostructure; in the case of the high-temperature phase, the antenna consists of a metal and surface plasmon resonances are excited on the surface of the $VO_2$ nanostructures. The main effect obtained upon switching is that at high temperature the reflection peak disappears, and a reflection dip is generated. In this case, by modifying structure parameters, such as cylinder diameter or height, it is possible to obtain different resonance wavelengths. Using this metasurface as a pixel, the authors demonstrate the possibility of obtaining the storage of graphical information by means of a tunable invisible ink. In the final device, they combine pixels

Materials 2021, 14, 3396

11 of 36

obtained from metasurface characterized by disks with different diameters and different reflectance: when $d = 560$ nm pixels have high reflectance, when $d = 520$ nm pixels show high reflectance at low temperatures and low reflectance at high temperatures. The first type of pixels has been used for the background, while the second type for the letters that have to be displayed upon heating. So, the desired message is shown upon heating, while, upon cooling, the image vanishes.

Xu et al. recently reported about another device able to convert a visible image into an IR image through localized optical heating and thermal emission [44]. The device is composed of stacked multilayers made of (from the top to the bottom) 50 nm $VO_2$, 30 nm $TiO_2$, 850 nm ZnS, 30 nm $TiO_2$, 100 nm Au and Si substrate. The top $VO_2$ layer confers dynamicity to the whole system, the $TiO_2/ZnS/TiO_2$ trilayer works as a lossless layer, while the bottom Au works as a highly reflective mirror. The absorptance and emissivity spectra of the device have been measured for both the insulating $VO_2$ and metallic $VO_2$ phases, and, during the insulator-to-metal (IMT) transition, the average emissivity of the device in the 8–14 µm range increases drastically from 0.19 to 0.91, reaching its maximum value ~1 at $\lambda = 10$ µm for metallic $VO_2$. The $VO_2$ phase transition can be triggered by laser illumination, which can be exploited for the recording of thermal patterns, with spatially resolved thermal emissions. The authors demonstrated the writing of both binary patterns (bilevel thermal emission, with a difference of 7 °C) or greyscale patterns (multilevel thermal emission). This multilevel behavior can be obtained by exploiting the hysteresis of $VO_2$ phase transition, which means that it occurs at different temperatures during heating and cooling. Due to this hysteresis, two phases and two emissivity levels are allowed at a particular temperature (inside the hysteresis regions, between 53 and 80 °C), according to the fact that it is reached upon heating or cooling. Interestingly, the authors observed that the precise value of emissivity can be controlled by changing the peak temperature during the heating process. During the recording of greyscale patterns, each pixel of the device is written by laser pulses with different durations which enable to obtain different peak temperatures during heating and different emissivity levels.

# 3.3.2. Applications in the Visible Range

In regard to applications in the visible range, Shu et al. demonstrated the possibility of dynamic color generation in a $VO_2$ based device, by integrating plasmonic nanostructures (periodic array of Ag nanodisks) with $VO_2$ thin film [45]. A silicon dioxide film is used to separate the $VO_2$ film from the silver-nanodisk array in order to reduce the electromagnetic loss and glass is used as substrate (Figure 8a). By tuning the spatial periodicity of the arrays and diameter of the silver nanodisks and thickness of the $SiO_2$ layer, various colors can be achieved across the entire visible spectrum. In addition, by exploiting insulator-metal transition of vanadium dioxide, the colors can be actively tuned by varying the temperature. For example, when the disk diameter is 120 nm and the spatial periodicity is 300 nm, the device is greenish at room temperature, and yellow for temperatures higher than 80 °C. Alternatively, when the disk diameter is 100 nm and spatial periodicity is 200 nm, the device is deep green at room temperature, and blue for temperatures higher than 80 °C. In general, when the temperature is raised to 80 °C, the peak shifts to shorter wavelengths and the peak width increases, which leads to the color change. In this work, the authors demonstrated the possibility of constructing temperature-dependent multicolor image (i.e., tulips image) also in the visible range, by combining structures characterized by different geometrical parameters (different nanodisk diameter and periodicity). By increasing temperature to 80 °C, the colors of the image change simultaneously due to the insulator-metal transition of $VO_2$, and new colors are generated. Thereafter, when the sample is cooled down to room temperature, the sample resumes its original colors, thanks to the reversibility of the phase transition (Figure 8b-e).

Materials 2021, 14, 3396

12 of 36

[图片: cb)ed2SiOdVO2-SubstrateTemperature-controlled stage]
# Figure 8. (a) Scheme of the structure proposed by Shu et al.; (b) SEM image of the pattern prepared for the visualization of tulips image by combining five different structures. Bar = 40 µm; (c) SEM images of the four arrays contained in structures I-IV reported in (b). Scale bars correspond to 400 nm; (d) reflection image of tulips pattern, recorded at 20 °C. Scale bar corresponds to 40 µm; (e) reflection image of tulips pattern, recorded at 80 °C. The scale bar corresponds to 40 µm. Reproduced from Ref. [45] with permission from Wiley.

Another proposed structure is the one recently reported by He et al: a 5 nm thick silver periodic porous layer on the top, a 50 nm thick $VO_2$ layer in the middle and a 200 nm thick silver layer at the bottom [46].

Duan et al. reported the possibility of producing a reconfigurable multistate optical system, by controlling the phase-transition characteristics of $VO_2$ with simultaneous stimuli: temperature, hydrogen doping and electron doping [47]. In fact, limited hydrogenation of $VO_2$ can result in a metallic phase at room temperature, $H-VO_2(M)$, while heavy hydrogenation can result in a different insulating phase, $H-VO_2(I)$, characterized by different reflectance and resistivity, compared to common insulating monoclinic $VO_2$. $H-VO_2(M)$ is characterized by lower reflectance (in the visible range, at 600 nm) and resistance than all the other types of $VO_2$ (monoclinic, rutile or $H-VO_2(I)$); while $H-VO_2(I)$ is characterized by a reflectance that is intermediate to those of monoclinic and rutile $VO_2$ and higher resistance (Figure 9a). Interestingly, also rutile $VO_2$ can be converted into $H-VO_2(M)$, at a slightly higher temperature in comparison to monoclinic $VO_2$, upon moderate hydrogenation, and into $H-VO_2(I)$, upon further exposure to $H_2$. Phase dehydrogenase can also be obtained by exposure to $O_2$, converting $H-VO_2(I)$ into monoclinic or rutile $VO_2$, according to the operation temperature and bypassing the $H-VO_2(M)$ phase (Figure 9b). The authors demonstrate a quadruple-state dynamic plasmonic display by exploiting the $VO_2$ tunability in response to a combination of temperature and $H$-doping. The proposed device is made of stacked $Al/Al_2O_3$ nanodisks, which reside on a substrate composed of Pd nanodots distributed on a 60 nm film of $VO_2$ deposited on an Au (100 nm)/Si substrate. The Pd nanodots serve to catalyze the hydrogenation of $VO_2$ at low (20–100 °C) temperatures. The height of Al and $Al_2O_3$ disks is fixed at 30 nm, while their diameter and their periodicity can be modified in order to develop structures with different colors. For each structure, 4 different $VO_2$ states, with 4 different colors, can be obtained. For example, when monoclinic $VO_2$ is blue, $H-VO_2(I)$ is pink, rutile $VO_2$ is red and $H-VO_2(M)$ is green. This type of structure can be used to prepare a dynamic color display (as an example, reproducing Vincent van Gogh's The Starry Night) which can be switched at the four different states, showing vivid color tuning. By depositing thin layers of metals on the surface of $VO_2$, it is possible to further control its transition temperature by means of electron doping: when metal with a lower work function (and higher Fermi level) in comparison to $VO_2$ is used (for example, Cr, Al, Ti, Ni and Cu), it can donate electrons to $VO_2$, facilitating its transition to the metallic phase; on the contrary, when metal with a higher work function (and lower Fermi level) in comparison to $VO_2$ is used (for example, Pt and Au), it can accept electrons from $VO_2$, preventing its transition to the metallic phase. In the first case, the monoclinic to rutile transition occurs at a lower temperature, in the second case, it occurs at a higher temperature (Figure 9c). The authors demonstrate the possibility of producing dynamic displays encrypted with two-level optical information, with two merged patterns, consisting of a QR code and writing. The display is obtained by combining four different structures: the background is made of structures containing

Materials 2021, 14, 3396

13 of 36

only $VO_2$ thin film, the QR code is obtained with $VO_2/Ti$ systems, while the writing is constructed by $VO_2/Pd$ nanodots structures (when the writing is overlapped to the background) or $VO_2/Ti/Pd$ nanodots structures (when the writing is overlapped to the QR code). At the initial state, all the device is made of monoclinic $VO_2$ and the display shows a yellowish color with blank information. To read out the QR code pattern, the temperature is utilized as the first decryption key. With increasing temperature, the areas covered by Ti start to become greenish in the temperature range of 64 ± 3 °C, indicating that they underwent a phase transition. With a further temperature increase above 80 °C, all the device cells are converted into the rutile phase, so the QR code disappears and the display shows a uniform greenish color, with blank information. To read out the writing, hydrogen is employed as a second decryption key. Upon loading $H_2$, the areas with Pd coverage are converted into $H-VO_2(M)$ phase and the writing becomes clearly visible (Figure 9c).

[图片: |温度 (°C)|Reflectance @ 600 nm| |:---:|:---:| |20|0.6 (m-VO₂), 0.2 (H-VO₂(M))| |40|0.6 (m-VO₂), 0.2 (H-VO₂(M))| |60|0.55 (m-VO₂), 0.2 (H-VO₂(M))| |80|0.3 (r-VO₂), 0.2 (H-VO₂(M))| |100|0.3 (r-VO₂), 0.2 (H-VO₂(M))|]
[图片: graph TD A1[m-VO₂(Insulator)] -->|T < Tc| A2[H-VO₂(M)] A1 -->|Fire| A4[m/r-VO₂(Mixed)] A2 -->|O₂| A1 A2 -->|H₂| A3[H-VO₂(I)] A3 -->|O₂| A2 A3 -->|H₂| A4 A4 -->|T ≈ Tc| A5[r-VO₂(Metal)] A4 -->|Snowflake| A1 A4 -->|O₂| A2 A4 -->|H₂| A3 A5 -->|T > Tc| A6[H-VO₂(M)] A5 -->|Fire| A4 A6 -->|O₂| A5 A6 -->|H₂| A7[H-VO₂(I)] A7 -->|O₂| A6 A7 -->|H₂| A4]
[图片: |催化剂|Tc1 (°C)|Tc (°C)|Tc'i (°C)| |:---:|:---:|:---:|:---:| |Pt|72|65|59| |Au|71|64|58| |VOx|70|64|58| |Pd|69|64|57| |Cu|68|63|57| |Ni|67|62|56| |Ti|65|61|56| |Al|64|60|56| |Cr|64|59|56|]
[图片: 未能识别到文本内容]
# Figure 9. (a) Reflectance of the structure proposed by Duan et al. measured at 600 nm and at different temperatures and H-doping levels. H-doping introduces two hydrogenated phases, H-VO₂(M) (green curve) and H-VO₂(I) (pink curve); (b) possible paths of phase transition of VO₂ by modifying temperature and H-doping; (c) variation of the transition temperature of VO₂ upon electron-doping. The gray-dotted line indicates the transition temperature of VO₂ without any surface metal; (d) example of dual-key information encryption. Variations of reflectance at 600 nm corresponding to the four states (i, ii, iii, and iv) of the optical double-encrypted display. The two decryption keys are temperature and hydrogenation, respectively. Reproduced from Ref. [47] with permission from the American Chemical Society.

Dong et al. reported the possibility of using a VO₂ thin film (~200 nm) deposited on a Si substrate as rewritable metacanvas not only for displaying graphical images, but also for writing photonic operators, in order to use the device for light manipulation [48]. For the storage of graphical information, initially, the device is heated up to a temperature near to the phase transition (all VO₂ is still in the insulating phase), a laser (λ = 532 nm, 1–11.5 mW, d = 1–3 µm) is focused onto the film to locally heat VO₂ to the metallic phase and storage can occur. It is maintained until the temperature reaches a value low enough to enable it to return to the insulating phase (the VO₂ phase transition is characterized by hysteresis, so there are different transition temperatures upon heating and cooling, which

Materials 2021, 14, 3396

14 of 36

guarantee a sort of non-volatility) and erasing occurs. The device functionality has been demonstrated for displaying images and, more interestingly, for the writing and storage of photonic operators (Figure 10). In this way, it is possible to obtain a device that is able to manipulate light, for example, beam steering or hologram generation. More complex light manipulation processes can be obtained by combining different devices, storing different photonic operators. For example, the first metacavas can be programmed as a linear polarizer, which can transform circularly polarized light into linear polarized light, and the second metacavas can be programmed as a concentric ring grating, which can further transform a light beam into a two-lobe pattern (Figure 10b).

# a)

[图片: 6]
# b)

[图片: F2F1I312]
# Figure 10. Examples of the employment of VO₂ based metacavvas used for the writing and storage of optical operators and interaction with light. (a) beam steering; (b) combination of two VO₂ based metacavvas, the first programmed and used as a linear polarizer, the second programmed and used as concentric ring grating. Reproduced from Ref. [48] with permission from Wiley.

Other stacked non-structured multilayers, among which one is made of $VO_2$, can generate different and variable colors, as reported by Wilson et al. [24].

# 4. Optical Switching

PCMs offer a unique set of properties to realize active, tunable and reconfigurable photonic devices. Some of these materials, such as the chalcogenides (GST), owing to their non-volatile phase transition, are suitable for reconfigurable photonic devices in which post-fabrication tunability is desired. Other materials with a volatile phase transition are more indicated for low-intensity optical modulation and dynamic tuning. In particular, $VO_2$ is attracting attention for low-power tunable devices because it exhibits an abrupt and reversible change of its complex refractive index at a relatively low temperature of 68 °C. The opportunities for PCM-based optical switches and modulators are endless although many challenges lie ahead. Future research will most likely require a multi-disciplinary effort: material science, chemistry and nanotechnologies will offer solutions to tackle the complex problems of integrating PCMs within commercially-available photonic platforms (e.g., silicon photonics), improving the quality of PCMs with proper alloying and doping, and efficiently introduce the stimuli needed to switch PCMs; fundamental research on hysteresis effects and the dynamics of the phase transition will be key to understand the ultimate limits of PCM-based devices in terms of modulation speed as well as the peculiar behavior of nanostructured PCMs (nanoparticles or nanocrystals); research efforts to develop accurate and fast multiphysics models, which include simultaneously thermal and optical effects, will be key to engineer ultra-compact devices for both photonic-integrated circuits and free-space operation with high modulation depth, low losses, low-intensity stimuli and reduced fabrication complexity.

Materials 2021, 14, 3396

15 of 36

Various strategies have been so far proposed in order to attain tunability, modulation and switching with photonic devices including PCMs. The operational wavelength in which PCM-enabled tunability has been demonstrated covers the entire spectrum, ranging from visible to THz frequencies. For the sake of clarity, we have classified the design strategies of the literature in three groups: (I) integration of PCMs with silicon-photonics devices, such as waveguides and resonators; (II) planar structures made of multilayer thin films of PCMs combined with films of metals and other dielectrics; (III) photonic nanostructures, such as nanoantennas, plasmonic and dielectric metasurfaces, as well as resonant gratings.

# 4.1. Integration of PCMs within Waveguides and Integrated Resonators

Optical modulation in silicon devices, such as waveguides and resonators, is a long-standing goal of the photonics research community. The ultimate objective is to realize all-optical signal processing for fast interchip and intrachip communications. So far, the best performances in terms of modulation efficiency have been obtained by embedding plasmonic resonators, polymers, two-dimensional materials, germanium and, more recently, PCMs in silicon-based devices. The typical strategy to achieve tunability and switching in integrated photonics with PCMs is to introduce the PCM in the proximity of a resonator, as illustrated in Figure 11.

[图片: DROP40-nm Etch180-nm SVO,TabWriteHONOHL3-um SiOSProbe10 μm]
# Figure 11. Integrated PCM-based photonic switches. (a) Reproduced from [49] with permission from OSA. (b) Reproduced from [50] with permission from Wiley.

An optical modulator was demonstrated by Briggs et al., in which a 2-micrometer long section of a silicon ring resonator was partially covered with $VO_2$ by pulsed-laser deposition, as depicted in Figure 11a [49]. In this work, direct substrate heating was applied as an external stimulus in order to induce the insulator to metal transition in $VO_2$ and to trigger the absorption modulation at wavelengths tuned near the resonances of the ring (~1550 nm). This modulation strategy was exploited by Ryckman et al. in a silicon ring resonator partially covered with a PCM patch deposited by electron-beam vaporization of $VO_2$ powder [51]. A 10-dB modulation of a cw signal at 1550 nm was activated by a pump laser at 532 nm, which was able to shift the ring cavity resonance by 1.26 nm. Similar modulation efficiency was observed by Rude et al. in a non-volatile optical switch for telecom wavelengths (1550 nm) realized with a silicon ring resonator with an RF-sputtered over-cladding layer of GST225 [52]. Here the phase transition was driven by a pulsed laser diode at 975 nm and the observed switching time for crystallization and amorphization of GST225 was on the order of a few micro-seconds. All-optical switching at 1.55 micron, driven by 25 ns pulses at 1064 nm, was demonstrated by Ryckman et al. in 2013 [53]. The switching mechanism was absorption modulation, with an efficiency of 4 dB/micron, in a non-resonant configuration with a $VO_2$ patch covering a section of an Si ridge waveguide, and intracavity phase modulation ~$\pi/5$ rad/micron. An electrically driven absorption modulator was proposed in 2015 by Joushaghani et al., in which a $VO_2$ film covered a micrometer-long section of a silicon waveguide and it was electrically excited with gold contacts [54]. A modulation efficiency with an extinction ratio of 12 dB was demonstrated with electro-optic bandwidth of ~1.3 MHz, corresponding to a switching time of less than a

Materials 2021, 14, 3396

16 of 36

microsecond. A similar electro-absorption modulation effect was demonstrated by Markov et al. with a significant improvement of the switching time, which was brought down to a few nanoseconds [55]. A non-volatile optical switch, reported in Figure 11b was presented by Stegmaier et al., by depositing a GST225 micro-sized patch on top of a ring cavity [50]. In this configuration, a switching time of ~200 ps with a 1 ps laser pulsed source was demonstrated without optical power bias to keep the device stable at the two states. The on-off switching contrast was of ~5 dB with an insertion loss of ~5 dB. A highly-compact, thermally-activated switch based on $VO_2$ embedded in a 500-nm long section of a silicon waveguide was presented by Miller et al., with a modulation depth of ~10 dB [56]. According to Zhang et al., a broadband nonvolatile switching at telecom wavelengths can be obtained with an optimized design that exploits GST225, reaching modulation efficiencies of 15 dB and insertion losses as low as 0.1 dB [57].

# 4.2. Integration of PCMs within Planar Multilayer Films

Optical thin-film filters have a rich history, which dates back to Newton's measurements of film thicknesses (Newton's rings), the theory of light as a wave and the first experiments on interference by Young. Although design strategies and fabrication technologies for interference films are quite mature, the ability to endow the optical response of these planar structures with tunability remains an open goal. GST225 and VO₂ have both been extensively investigated as possible game-changers to reach this goal. Figure 12 reports a literature selection of some of the switching and modulator concepts based on thin planar films.

[图片: FTIR source297KTo MCT detector(b343K0.8346K347K“"Transmission-Insulating VO2348Kobjective0351KMetallic VO2359KForward20.2h<<VOBackward15Sapphire100Wavelength (um1.0μm3.5μmTemp.controlled plate0.2μm2μm(d)(c)GST #532nm5mMid-RSiO2200nm-GSTGSTGSTGST #465nmTamSiO2200nmGST #3ns laser65nmSO2200nmSGST #265nm-GSTSIO2200nmGST #132nmQuartzFused Silica Substrate]
# Figure 12. Integration of PCMs within planar multilayer films. (a) Reproduced from [58] with permission from AIP. (b) Reproduced from [59] with permission from the American Chemical Society. (c) Reproduced from [60] with permission from IEEE. (d) Reproduced from [61] with permission from Nature Springer.

Early works on optical switching abilities of $VO_2$ thin films date back to the late 90s. Beteille and Livage measured thermal-induced switching in vanadium dioxide thin films deposited from vanadium alkoxides [57]. In this work, it was also shown the typical hysteresis of the transition, as well as the possibility to control the transition temperature by properly doping $VO_2$ during deposition. Mid- and far-infrared switching was then optimized in films of $VO_2$ sputtered on amorphous silica substrates in [57,62]. The optimization was performed by varying sputtering parameters, such as film thickness, gas ratio and substrate temperature. The best performances were observed with film thicknesses of about 120 nm. Transmittance modulation of 75% between the insulator and the metallic state of $VO_2$ was measured at 3.5 micron, while reflectance and emissivity variations of ~50% were observed between 8 and 12 micron.

Materials 2021, 14, 3396

17 of 36

Similar planar structures, based on thin films of $VO_2$ and $VO_2O_5$, were also investigated as dynamic optical limiters in the infrared [63]. In these experiments, the IMT transition was induced by a cw infrared laser irradiating the surface of the samples with an irradiance of ~250 W/cm $^{2}$. The limiter performance, with a transmittance decrease from 47% to 28% in the $VO_2$ sample, was mainly restricted by the slow response time (~100 ms).

The thermochromic response of $VO_2$ is quite sensitive to the deposition process and to the choice of substrate. In [64], substrates of aluminum, silicon and quartz were compared in the sputtering deposition of $VO_2$ for tunable emissivity in space applications. It was found that $VO_2$ films deposited on an Al display an emissivity dependence on temperature that is opposite to that of $VO_2$ deposited on transparent substrates (quartz and Si). In [65] optimized tunability of thermal emission was designed in thin-film multilayer structures made by alternated layers of $VO_2$ and metal for applications in smart windows and infrared signature reduction. A very promising application was demonstrated in [58] by Kats et al., in which perfect absorption by critical coupling was achieved in the proximity of the IMT in an ultra-thin film of $VO_2$ deposited on top of a sapphire substrate (the structure and the temperature-dependent reflectivity spectra are reported in Figure 12a). This work has shown that a $VO_2$ ultra-thin film near the IMT behaves like a metamaterial mixture in which the insulator and metallic phases coexist. The mixture optical response can be easily regulated by applying an external stimulus (thermal, electrical or optical). A large tuning range for reflectance, from 80% to 0.25%, was measured, thus paving the way for applications in bolometers, modulators and controlled thermal emission. Recent work by Wan et al. [59] has demonstrated an optical diode for near-infrared light with broadband asymmetric transmission triggered at high input intensities. The device has been realized with a $VO_2$ thin film sputtered on top of a sapphire substrate and covered with a metallic semi-transparent layer (Figure 12b).

Optical switching has been also investigated in GST films (see [12,66] for a recent review). GST225 can be deposited on virtually any substrate or film at low temperatures, and it therefore can be integrated in multilayer structures [60]. The phase transition from amorphous to crystalline induces a significant change of the optical properties, and this modulation occurs on fast timescales, on the order of pico- to nanoseconds. Unlike VO₂, GST phase change is non-volatile. Crystallization is relatively easy to trigger, while the opposite process, amorphization, requires heating to a significantly higher temperature and it must be followed by a fast quenching.

In [60], a reflective optical limiter was experimentally demonstrated with a multilayer hosting GST films alternated with SiO₂ films in a photonic-band-edge filter configuration, as schematized in Figure 12c. Recently, an all-optical switch based on layered epitaxial trigonal GST124 was demonstrated for telecom wavelengths with film thicknesses on the order of 100 nm [67]. Reversible optical switching of highly confined phonon-polaritons in quartz was obtained with an ultrathin (~7 nm) planar film of GST326 [61]. The film was activated with laser pulses (see Figure 12d). This demonstration has indicated a novel practical way to realize all-dielectric, rewritable phonon-polariton resonators.

# 4.3. Integration of PCMs within Photonic Nanostructures

Photonic nanostructures may display a variety of resonances, whose properties, such as quality factor and modal volume, depending on the shape and size of the structure, on the optical properties of the materials inside the resonator and on the optical properties of the materials surrounding the resonator. For example, in a very simple, but the representative scenario, in which the nanostructure is made by an isolated or an ensemble of very small spherical nanoparticles, the optical properties of the nanostructure, such as near-field enhancement, scattering and absorption spectra, will be ruled by the polarizability of the single nanoparticle. In the dipole or quasistatic approximation, the polarizability can be written as $\alpha = 3\epsilon_{bg} V \frac{\epsilon_{np}-\epsilon_{bg}}{\epsilon_{np}+2\epsilon_{bg}}$, where $V$ is the volume occupied by the nanoparticle, $\epsilon_{bg}$ is the permittivity of the background material and $\epsilon_{np}$ the permittivity of the nanoparticle. Any permittivity change either in the nanoparticle ($\epsilon_{np}$) or in the environment ($\epsilon_{bg}$) will

Materials 2021, 14, 3396

18 of 36

induce a change in the optical properties of the nanostructure. The relative change will be larger especially when photonic resonances are excited. This can be realized by introducing PCMs either in the volume of the resonator or in the environment surrounding the resonator. This concept can be applied even to the simplest manifestation of nanophotonic resonance, i.e., the Fröhlich resonance of a very small metallic nanoparticle, which occurs when $\epsilon_{np} = -2\epsilon_{bg}$. In 2005, Maaza et al. demonstrated reversible tunability of the surface-plasmon polariton resonance of Au nanoparticles embedded in a VO₂ matrix [68]. The mixture was able to thermally switch, showing a resonance shift from 645 to 598 nm. Similar blueshift effects were observed in mixtures of silver nanoparticles embedded in VO₂. [69]. In [70], circular and elliptical gold nanoparticles were lithographically fabricated and then covered with crystalline grains of a VO₂ film. Albeit more complex, the lithographic approach has the advantage to avoid the resonance broadening associated with the dispersion of the particle size that one typically has in self-assembled mixtures of nanoparticles. The thermally induced blueshift of the surface plasmon resonance was measured to be on the order of 80 nm for circular nanoparticles and 200 nm for elliptical nanoparticles. Plasmonic resonance can be also supported by VO₂ nanoparticles, when the VO₂ is in its metallic phase. In [71], VO₂ nanoparticles were obtained by ion-implantation and self-assembly in a silica matrix. The onset of the nanoparticle plasmonic resonance at telecom wavelengths was photoinduced using a pulsed laser at 800 nm (Ti: Sapphire) with pulses having a time duration of ~50 fs and energy of 1–3 μJ. In this work, the dynamics of the phase transition were measured with a pump-probe setup and it was found that the IMT transition occurs on a time scale of about 150 fs. This result paved the way for the development of ultrafast photonic devices based on PCMs. VO₂ nanoparticles have been extensively studied for energy-efficient thermochromic fenestration, in which solar energy is transmitted below a comfortable temperature and otherwise rejected in order to reduce the use of space heating and cooling [72]. In comparison with VO₂ films, VO₂ nanoparticles have been proved to show larger luminous transmittance and deeper modulation of solar energy. The only limitation of VO₂ for this kind of application is the relatively high temperature for transition, which can be drastically reduced to a comfortable temperature by replacing some vanadium with tungsten [73] or by adding magnesium dopant [74]. The amorphous to crystalline change of GST has been also explored to dynamically control plasmonic resonances [75].

Besides very small nanoparticles, a plethora of resonant configurations have been investigated, including plasmonic antennas operating in the near and mid-infrared, metallic antennas in far-infrared and in the THz range, dielectric Mie-type resonators, plasmonic and dielectric metasurfaces, metamaterials, as well as resonant gratings. Figure 13 reports a literature selection of representative concepts for PCM-based switches and modulators that have been realized with photonic nanostructures.

Materials 2021, 14, 3396

19 of 36

# (a)

[图片: (b)Read chacneZnS-SiOGe2Sb2TesZnS-SiO2Glass substrate-4联42Phase change canvas0.59mWrite channe]
# (c)

[图片: hvGST switchingby light pulse]
# (d)

[图片: VO2(30℃C)VO2(90°C)]
# (e)

[图片: amorphouscrystallineReflectanceqbueM]
# (f)

[图片: 200nm(f)50fs pulse960HzGST-326C-GSTa-GSTc-GST]
# Figure 13. Integration of PCMs within photonic nanostructures. (a) Reconfigurable planar thin-film metasurface. Reproduced from [76] with permission from Nature Springer. (b) Reconfigurable metasurface based on GST rods. Reproduced from [77] with permission from Wiley. (c) Reconfigurable metasurface based on Ge-GST meta-atoms. Reproduced from [78] with permission from Wiley. (d) VO₂-based nanoantennas for metasurfaces in the visible. Reproduced from [79] with permission from the American Chemical Society. (e) Tunable perfect absorber based on metal-GST-metal resonances. Reproduced from [80] with permission from Wiley. (f) Plasmonic antennas switched with a PCM. Reproduced from [81] with permission from the American Chemical Society.

The pioneering work of Sun et al. in 2006 [82] has been probably the first demonstration of tunable response in resonant, periodic nanostructures based on PCMs. In that work, modulation of extraordinary optical transmission was experimentally observed in structures obtained with periodic hole arrays on a metal-VO₂ double-layer thin film structure. Thermal tuning of metamaterial/metasurface resonances were observed at THz frequencies by Driscoll et al. in 2009 inter-twining metallic split-ring resonators with vanadium dioxide [83]. A similar structure was investigated in [84], but in this case, the switching was induced by a combination of thermal and electrical stimuli near the resonance frequency of the split ring resonator (approximately at 1.5 THz), and the measured resonance red-shift was about 20%. By exploiting the hysteretic nature of the VO₂ phase transition, it was possible to demonstrate persistent frequency tuning of the array using a transient electrical stimulus. Extension of this concept to near-infrared wavelengths was demonstrated by Dicken et al. in 2009 [85].

Electro-optical switching of a Fano-type resonance of a plasmonic metasurface was observed experimentally by Samson et al. [86]. In this work, a PCM film of gallium lanthanum sulphide (GLS) was sputtered on top of a resonant plasmonic nanostructure made of asymmetrically-split ring resonators. The electrically-driven transition in GLS provided about a 150 nm shift in the near-infrared resonance, with a transmission modulation contrast ratio of 4:1. This design was then improved by exploiting the more common GST225 PCM in a similar configuration, in which a GST225 film, sandwiched between ZnS/SiO₂ cap and buffer ultrathin layers, covered the surface of a gold metasurface [87]. In this structure, switching the infrared resonance of the metasurface was obtained by optically stimulating the GST225 phase transition with laser pulses having a time duration of 50 ns and peak intensities of about 0.25 mW/μm $^{2}$. The reversible nature of the switch was also tested with the repeated optical operation, revealing an endurance of 50 cycles before degradation. Infrared tunable resonances were demonstrated in a plasmonic crystal made of gold nanoantennas fabricated on top of a GST225 thin film [88]. The peculiarity of this structure was the sharp nature of the switched resonances, which was associated

Materials 2021, 14, 3396

20 of 36

with a lattice mode of the plasmonic crystal rather than to a localized surface plasmon resonance. A remarkable non-volatile shift of 500 nm was measured.

Modulation in the THz was proven in 2010 by Liu et al. using a metallic split-ring resonator on top of a $VO_2$ film [89]. The modulation efficiency was associated with strong field enhancement provided by the resonators in the gap regions, which become shorted when the $VO_2$ switched to the metallic phase. An interesting pump-probe experiment on this structure, in which both the pump and the probe were tuned at TH frequencies, revealed the dynamics of the transmission modulation, which showed a characteristic switching time on the picosecond scale. Proof of principle for tunability of aluminum nanorod antennas was provided in the mid-infrared (~5 µm) using both GST and InSb [90]. The resonance shifting was measured to be 19.3% with a figure of merit, i.e., resonance shift divided by resonance bandwidth, of the order of one. In this work, different configurations were considered, with the PCM on top of the antennas, in the same plane of the antennas and on the bottom. The PCM was selected for its low absorption losses at the resonance frequency of the antenna. In this work, the crystallization of GST and InSb was achieved via annealing on a hot plate. Optical switching was demonstrated by the same authors and in the same type of structure, i.e., aluminum nanorods surrounded by GST326 (see Figure 13f), in [81] by using fs laser source at 800 nm to induce the phase change. Thermal tuning in the mid-infrared was also demonstrated using $VO_2$ as PCM in close proximity of a resonant plasmonic antenna array [91]. The Y-shape antennas were fabricated on top of a $VO_2$ film of 180 nm using sapphire as substrate, and the volatile modulation was induced thermally. The measured relative shift was about 10% at a wavelength of ~10 µm.

Complete control over the radiation pattern of nanoantennas can be achieved by judiciously leveraging the refractive index changes of PCMS. In [92] a metasurface of patch antennas was proposed, in which a GST layer is sandwiched between two metallic patches. Exploiting the Kerker condition, in which induced magnetic and electric dipoles interfere either destructively or constructively in the forward/backward directions, and under the application of a stimulus that changes the phase of GST from amorphous to crystalline, the radiation pattern switches dramatically from unidirectional to dipole-like. An alternative way to tune the radiation properties of PCM-based optical antennas in the near-infrared was indicated by Savalyia et al. [93]. The idea is to replace a portion of the volume of plasmonic antennas with a PCM (in the proposed configuration, $VO_2$) in stark contrast with the most common approach in which $VO_2$ is in proximity, but in the outside body of the nanoantenna.

Selective absorption and dynamic control of absorption bandwidth in the mid-infrared is of paramount importance for thermal imaging and for efficient microbolometer in many applications, including astronomy, military and surveillance. A perfect absorber based on a patch-antenna array deposited on top of a grounded film of PCM (GST) was proposed by Tittl et al. [80]. The structure, as well as its principle of operation, are reported in Figure 13e. By exploiting the metal–semiconductor–metal plasmonic magnetic resonances in this system, peaks of absorption larger than 90% and with a selective bandwidth of ~1 µm were redshifted by 0.7 µm while maintaining high absorbance. Moreover, 20 µm by 20 µm pixels of the metasurface tuned at different wavelengths in the mid-IR were fabricated, showing the potential application of this technology for multispectral thermal imaging. A similar concept device was proposed by Wang et al. in a $VO_2$-based metamaterial absorber, in which the plasmonic magnetic resonance is supported in a one-dimensional gold grating separated by a gold mirror by a thin $VO_2$ film [94]. The perfect absorption for TM-polarized light at 5 µm is completely suppressed when $VO_2$ switches to the metal phase. A similar configuration, i.e., a resonant array of plasmonic antennas separated from a metallic mirror by a PCM film, was proposed by Cao et al. to realize broadband, polarization- and angular-independent perfect absorption in the visible range [95]. In their work, they indicated GST as the absorbing material for the large imaginary part of its dielectric constant in the visible, and it was predicted that a modest intensity signal of ~95 nW/µm $^{2}$ would be sufficient to switch the GST at the nanosecond scale.

Materials 2021, 14, 3396

21 of 36

A different approach to obtain tunable perfect absorption in the near-infrared was proposed by Zhu et al., where $VO_2$ was only present in the gap of bow-tie antennas [96]. The antenna array was separated from a metallic mirror by a dielectric spacer of $Al_2O_3$. The advantage of this configuration is the power and time required to switch the PCM are quite reduced, since the PCM only occupies the tiny volume inside the gap of a nanoantenna, in which the field enhancement is very large. The switch was electrically driven by exploiting the antennas, connected to larger electrodes, as heating elements. The measured modulation depth was 33% with a recovery time on the order of a millisecond. A theoretical study on $VO_2$-loaded dipole antennas was presented by Tognazzi et al. [97]. It was shown that the switching capabilities of this type of hybrid antenna are ruled by the antenna's arm length, and that smaller $VO_2$ volumes in the gap yield larger extinction-efficiency contrast as well as larger intensities of the resonant peaks. Furthermore, these structures are weakly sensitive with respect to changes of position and size of the gap, revealing good robustness against small fabrication defects.

Arrays of metal–PCM–metal resonators were also proposed as low-power and fast mid-infrared beam steering devices using GST as PCM [98]. A steering range of 11 degrees in transmission and 22 degrees in reflection was numerically predicted with a steering response on the nanosecond scale and power density of a few µW/µm $^{2}$. Reversible beam steering was experimentally demonstrated in the near-infrared (1.55 µm) with plasmonic 1D antennas fabricated on top of a GST film [99]. The array reflection switched with a 44% efficiency from anomalous to specular, in response to the phase switch induced on the GST film.

PCMs are also able to control the polarization state of electromagnetic waves. A switchable THz quarte-wave plate, thermally driven, was presented by Wang et al. [100]. The structure was a metasurface obtained with a periodic array of asymmetric cross-shaped resonators, with $VO_2$ pads fabricated at the terminals of the crosses. The operational bandwidth, in which the metasurface acted as a quarter-wave plate was able to transform linearly polarized light into circularly-polarized light, blue-shifted by ~10% upon the application of a thermal stimulus.

Proof-of-principle transmissive tunable metasurfaces were presented by Dong et al., using an array of gold square pillars on top of a GST film and an indium-tin-oxide layer [101]. A 10% shift of the antennas' resonance was experimentally demonstrated by thermally annealing the sample and the possibility to tune electrically was demonstrated to be feasible, since the ITO layer has a negligible effect on the transmission properties of the metasurface.

A significant breakthrough for reconfigurable and tunable nanophotonics and, more generally, for the dynamic control of free-space propagating optical fields, was introduced by Wang et al. in 2015 [76]. It was proven that a single film of GST, properly stimulated by engineered trains of optical pulses, can be tailored to function as a metasurface with an almost arbitrary optical response and functionality (see the artistic rendition of the concept in Figure 13a). A variety of devices were demonstrated with this technique: visible-range reconfigurable plates, a lens with subwavelength focus, a greyscale hologram and an all-dielectric metamaterial with on-demand reflection and transmission resonances.

Owing to their large refractive index, PCMs, and GST in particular, lend themselves naturally to the design of Mie-type resonators and all-dielectric metasurfaces based on Mie resonances. An all-dielectric reconfigurable metasurface was demonstrated by Karvounis et al. with visible/near-infrared switching contrast of ~7 dB in reflection and transmission [102]. The metasurface consisted of a high-contrast, subwavelength grating with sharp leaky-mode resonances and the 10% measured resonance shift was laser-induced. An active metasurface concept was proposed by Chu et al. [77]. The idea is to engineer PCM metamolecules (based on GST rods, as reported in Figure 13b) with a tailored optical response and functionality, including the tuning of anomalous reflection in gradient metasurface for beam steering and the tuning of the electromagnetically-induced-transparency resonance. A full-phase control in all-dielectric metasurface was achieved by Leitis et al. using hybrid

Materials 2021, 14, 3396

22 of 36

Ge-GST Mie resonators as building blocks for the active metasurface, as illustrated in Figure 13c [78]. In particular, a tunable infrared Huygens' metasurface was presented with dynamic, programmable phase control and large transmission in the infrared. The phase control was achieved via ultrashort laser pulses at 660 nm. Reconfigurable metasurfaces with very large switching contrast (~30 dB) in the mid-infrared have been recently presented by Shalaginov et al. [103]. In this work, varifocal lens design has been demonstrated in which a variable focal plane can be obtained by selectively excite different meta-atoms of the meta-surface. The Huygens' GST meta-atoms have been engineered with various regular shapes, such as 'I', 'H', and "+" shapes. PCMs have also been used to tune the Mie resonances in semiconductor metasurfaces. For example, recently, a tunable Mie-resonant dielectric metasurfaces was proposed for infrared light, in which a VO₂ film underneath an array of Mie-resonant silicon nanocylinders was able to switch transmission by two orders of magnitude [104]. It has been also shown that such a metasurface can be tailored to produce spectrally tunable near-perfect absorption.

PCM-based dielectric metasurfaces have been also investigated for applications involving visible light. Recently, it has been theoretically predicted that modulation of visible light may be possible with $VO_2$-based metasurfaces, exploiting a diverse number of design strategies to increase light interaction through hybrid resonances in which both lattice effects and localized resonances conspire to boost the light-matter interaction [105]. An experimental demonstration of tunable Mie-resonances has been recently provided by Kepič et al., with tunable $VO_2$ nanoantennas supporting Mie-resonances in the visible and near-infrared range (Figure 13d) [79]. Moreover, plasmonic resonances were also observed when the $VO_2$ was switched to its metallic phase. Scattering and extinction modulation depths were measured on the order of a few dBs, and they were induced both thermally, with a temperature-controlled stage, and optically, by using a cw laser.

# 5. Photonic Memory Devices for Information Storage and Computing

Initial applications of chalcogenide PCMs were focused on data storage, leading to the development of rewritable optical discs (DVD or blue-rays) or non-volatile phase-change electronic memories (phase-change random access memories, PCRAMs). Data storage is achieved thanks to variations of material reflectivity in the first case, and thanks to electrical conductivity changes (the resistance value of a PCM memory cell is typically around $10^3$ ohms for crystalline state and $10^6$ for amorphous state) in the second case. These applications are at an advanced development stage: PCM-based rewritable optical discs are already commercialized and excellent reviews can be found in the literature regarding PCRAMs [106–110]. They are very promising alternatives to more common Flash memories, thanks to their ultrafast operation (on the time scale of nanoseconds, that is orders of magnitude fasters than Flash memories), high reproducibility, high cycling endurance (the possibility of reaching $10^{12}$ switching cycles by means of electrical pulses has been demonstrated), low power consumption, especially thanks to the non-volatility of the phase transition, and good scalability of the material to the nanoscale. However, PCRAMs are characterized by some drawbacks, such as resistance drift over aging (due to long term instability of the amorphous state) and difficulty of reaching with precision the desired resistance level (often it is necessary to check and verifying if a target value has been reached, following a “program and verify” method, which enhances the whole process complexity). In addition, PCRAMs are still linked to von Neumann architecture inside computers, which separate, in time and space, the operations of processing and memory.

More recently different research groups have begun to study the possibility of using PCMs, in particular GST225, for obtaining photonic memories, in which data are stored thanks to the variation of light transmission along a photonic circuit. In this case, the obtained devices are characterized by non-volatility, high cyclability ($10^6$ cycles) and high operation speed, which is further increased by the fact that both information storage and transfer can be performed by optical means. For example, PCRAMs typically require a writing pulse of 50–100 ns and reading pulse of 10 ns, while for PCM photonic memories

Materials 2021, 14, 3396

23 of 36

10 ns and 500 ps are enough for writing and reading, respectively [111]. PCMs have the advantage of being easily manipulable at the nanoscale and they can guarantee good compatibility with semiconductor processing and on-chip optical interconnects typical of photonic circuits, leading to high-speed information transfer, large bandwidth and low loss residual crosstalk.

The first proposal of using Ge₂Sb₂Te₅ for obtaining a photonic memory comes from Pernice et al. in 2012 [112]. The proposed architecture is made of a microring resonator coupled to a nanophotonic bus feeding waveguide, a control waveguide and a drop waveguide. The waveguides are made of SiN and on the top of the microring resonator is a patch made of GST225, which introduces dynamicity into the system (Figure 14a). In fact, light that passes through the control waveguide can evanescently couple to the ring resonator, interacting with the GST225 patch. In this way, it causes a temperature enhancement of the GST225 layer and induces a transition phase. For this tuning, high-intensity laser pulses are used, with $\lambda = 700$ nm and a duration of 600 fs. The architecture can be optimized in a number of ways: by varying the gap between the control waveguide and the ring resonator it is possible to regulate the degree of the heat transfer and, so, the degree of the phase change, and by suspending this portion of the ring resonator it is possible to improve thermal isolation of the GST225 layer, enabling to reach a temperature high enough to undergo quickly crystallization or amorphization processes. When GST225 is in the crystalline state, it is characterized by high light absorption capability, on the contrary, when it is in the amorphous state, it is characterized by low absorption. When some probe light (of the proper wavelength, in resonance with the ring resonator) flows through the feeding bus waveguide, it evanescently couples to the ring resonator, which absorbs it in a different way, according to the GST225 phase. So, by controlling the GST225 phase it is possible to control the modal profile of the propagating wave in the ring resonator. When GST225 is amorphous, light is largely confined into the SiN portion of the ring waveguide and it propagates without significant loss. On the contrary, when GST225 is crystalline, it becomes more absorptive, and light is confined close to the GST225 portion of the ring waveguide, increasing the optical loss through the ring resonator. As a result, the transmission that can be detected at the readout port of the drop waveguide undergoes significant variations according to the GST225 state. Upon crystallization of the GST225, the transmission at the drop port reaches lower values. Transmission variations can be detected also at the through port, with an opposite behavior after GST225 crystallization, i.e., higher transmission values at the through port for crystalline GST225. By switching between amorphous and crystalline phases, it is possible to vary continuously the light transmission through the ring resonator between 0 to 90%. Therefore, by assessing memory levels to select levels of transmission, it is possible to obtain multilevel memory device. Writing and storage of information are performed thanks to GST225 crystallization, while erasing is performed by means of amorphization. Reading out, instead, is performed without altering the GST225 state, by means of weak probe laser pulses from the input bus waveguide, and it can be performed both at the through or at the drop port.

The same architecture, i.e., one ring resonator coupled to 2 parallel bus waveguides, is used also by Stegmaier et al. [50]. In particular, it was demonstrated that by controlling the crystallographic state of the GST225 patch on the ring resonator it is possible to control the flow of the on-resonance light inside the device: when GST225 is the crystalline state light is directed to the through port, while it is directed to the drop port when it is in the amorphous state (Figure 14b). In this case, amorphization is achieved by using 2 pulses at high energy (but low enough to not damage the material), while crystallization is obtained stepwise, using a train of pulses with decreasing energy (from 38 to 19 pJ), which enable a slow cooling of the material and guarantee a sufficient time to achieve an ordered arrangement of GST225 atoms. In addition, by modulating the power of the pulses inside the train used for crystallization, it is possible to access intermediate crystallization levels, leading to gradual variation of transmission and intermediate memory levels.

Materials 2021, 14, 3396

24 of 36

# a)

[图片: dropportdrop waveguidecontrowaveguideGST225feeding waveguide]
# b)

[图片: |Wavelength (nm)|cGST THROUGH|aGST THROUGH|cGST DROP|aGST DROP| |:---:|:---:|:---:|:---:|:---:| |1560|0.98|0.99|0.01|0.02| |1561|0.98|0.99|0.02|0.04| |1562|0.63|0.99|0.07|0.10| |1563|0.98|0.99|0.07|0.12| |1564|0.98|0.99|0.03|0.05| |1565|0.98|0.99|0.01|0.02|]
# c)

[图片: |Wavelength (nm)|Amorphous w=20 μm|Amorphous w=10 μm|Amorphous w=5 μm|Amorphous w=1 μm|Amorphous w=0.5 μm|Crystalline w=20 μm|Crystalline w=10 μm|Crystalline w=5 μm|Crystalline w=1 μm|Crystalline w=0.5 μm| |:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:| |1592|40|40|40|35|35|0|0|0|-10|-10| |1594|40|40|40|30|30|0|0|0|-20|-20| |1596|40|40|40|35|35|0|0|0|-10|-10| |1598|40|40|40|35|35|0|0|0|-20|-20| |1600|40|40|40|35|35|0|0|0|-10|-10|]
# Figure 14. (a) Examples of a commonly employed architecture for the preparation of memory cell, composed of a ring resonator containing a switchable GST225 unit, a feeding waveguide and a drop waveguide. In the work of Pernice et al. a control waveguide is used to induce phase transition [112]; (b) variation of transmission recorded at the through port (up) and at the drop port (bottom) upon GST225 switching. Laser pulses are used to induce phase transition [50]; (c) variation of transmission at the through port upon GST225 switching, according to different width values of the GST225 patch. It is possible to modify the ring resonator parameters (radius and gap with the feeding waveguide) in order to obtain “direct switching”, as highlighted in the green region, and “inverse switching”, as highlighted in yellow regions [113]. Reproduced from Refs. [50,113] with permission from Wiley.

Similar results are obtained using similar devices, based on different architectures (one [14] or more ring resonators [111] coupled to only one bus waveguide, double-ring resonators in series coupled to three waveguides [114], etc.). The operational principle of all these devices is based on the fact the attenuation coefficient of the GST225 in the crystalline state is higher than that obtained for the amorphous state. In fact, as demonstrated by Rios et al., this behavior is independent of the employed architecture [114]. Here the authors tested three different architectures: a ring resonator (with a GST225 switching portion) coupled to one bus waveguide, a micro Mach–Zehnder interferometer (it is composed of two beam splitters and two mirrors, along one of the two possible paths a GST225 patch is deposited on the top surface of the waveguide) and a balanced splitter (one of extremity contains a GST225 switching portion). For all the three structures, transmission measurements have been performed under three different conditions: (i) before deposition of the GST225 on the surface of Si₃N₄ waveguides in order to estimate losses due to the waveguides, (ii) when GST225 is in the amorphous state and (iii) when GST225 is in the crystalline state. The variation of the amount of light transmitted in different conditions is linked to the losses recorded inside the structure, and it is proportional to an attenuation coefficient. The attenuation coefficient obtained in the case of crystalline GST225 is higher than the one obtained for amorphous GST225, confirming its more absorptive behavior. It was also demonstrated that the attenuation coefficient is higher for the wider GST225 patch (linear correlation with GST225 width). Furthermore, in this work, the authors proved that it is possible to build a memory device by exploiting a ring resonator coupled to only one bus waveguide, which works both as input and read-out through a port. Interestingly, the authors noticed that when the attenuation inside the ring resonator changes, also the resonance condition changes. In other words, also the position of the resonance peak can be used to retrieve the GST225 state. In addition, the results of this research indicated that it is possible to engineer the ring resonator (modifying its radius, the width of the GST225 patch and the gap between the ring resonator and the bus waveguide) in a way that it is possible to obtain both transmission decrease (direct switching) or increase (inverse switching) upon GST225 crystallization (Figure 14c). This fact is particularly interesting because, not only does it enable to perform data storage by assessing different memory levels to different transmission levels, but it also allows us to implement logic operations by combining direct and inverse switching arrays inside the same device.

Rios et al. in another work demonstrated the possibility of achieving multilevel and multi-bit data storage, using a device composed of three memory cells (three ring resonators

Materials 2021, 14, 3396

25 of 36

with a GST225 patch) coupled to one bus waveguide [111]. The three-ring resonators are characterized by three different radii, so three different resonance wavelengths. Their different dimensions enable independent access to different cells, both for writing (performed through amorphization, using a high intensity 15 ns laser pulse), erasing (performed through crystallization, using a train of 50 ns pulses of decreasing power) and reading out (performed using lower power 500 ps pulse, which does not modify the GST225 state). Data storage is encoded in the amount of light transmitted along the bus waveguide and read at the through port. When GST225 is in its amorphous state, low values of optical loss are recorded inside the ring resonator (excited at a particular wavelength), and it is possible to record at the through port lower values of transmission in comparison with the same structure with GST225 in the crystalline state. In addition, by properly modulating the energy of the pulses for writing/erasing it is possible to reach intermediate levels characterized by a mixture of crystalline and amorphous regions, which exhibit transmission properties lying between fully-crystalline (level 0) and fully-amorphous (level 1) ones. The authors experimentally demonstrated the possibility of obtaining up to 7 different levels, which can be reached both serially and randomly (Figure 15). However, the number of levels that can be achieved in one device is determined by the difference in transmission between the highest and the lowest level and by the signal-to-noise ratio of the read-out process: it can be increased by using larger memory cells and readout pulse with higher energy.

# a)

[图片: .]
# b)

[图片: 10Transmission (norm)o80.0155415561560156215641558Wavelenght (nm]
# c)

[图片: normase39STEE9STSE9ST E9ST(wu)1y8uajaneM]
# d)

[图片: LevelPPPPR7.3RR32R3.1]
# Figure 15. (a) SEM image of the architecture of the system used by Rios et al. as a memory device, composed of three differently-sized ring resonators containing a switchable GST225 unit, combined with a feeding waveguide; (b) measured transmission at the through port: a group of three distinct resonances, corresponding to the respectively colored rings, are observed; (c) variation of transmission at the through port upon GST225 switching, for one individual element. Writing is obtained through amorphization, erasing is obtained through crystallization; (d) multilevel operation: 7 different levels can be reached inside the device, by applying laser pulses $P_1$ characterized by different power ($E_{P1} = 372 \pm 12$ pJ, $E_{P2} = 415 \pm 13$ pJ, $E_{P3} = 465 \pm 13$ pJ, $E_{P4} = 524 \pm 14$ pJ, $E_{P5} = 561 \pm 14$ pJ, $E_{P6} = 585 \pm 14$ pJ and $E_{P7} = 601 \pm 15$ pJ). Each level is accessible in consecutive (both ascending or descending) or arbitrary order. $R_{n-m}$ indicates a partial erasing process. Reproduced from Ref. [111] with permission from Nature Springer.

Li et al. proposed an alternative method to obtain multilevel switching, which enables to achieve inside a single cell 34 levels and to prepare memory device of more than 5 bits [115]. The exploited architecture is very simple: A Si₃N₄ waveguide on which a patch of GST225 has been deposited, together with an ITO protective layer. As usual, by controlling the GST225 phase, it is possible to control the amount of light transmitted along the waveguide, considering that GST225 is more absorptive when crystalline. The main advantages of this method are that it enables to reach a high number of non-volatile levels, it is very fast (operation last less than 250 s) and a low amount of energy is consumed. It is based on a double-step single optical pulse, which allows us to control the final level of the cell independently of the previous state. In this case, writing is obtained by means of gradual amorphization, while erasing is achieved by means of crystallization. The writing programming pulse is a 20–50 ns rectangular pulse of variable energy, which controls the % of amorphous material and the transmission along the waveguide. Higher power corresponds to higher amorphization and higher transmission. The erasing pulse, instead, is divided into two steps: a first, high amplitude, 50 ns pulse, which serves

Materials 2021, 14, 3396

26 of 36

for heating GST225 above crystallization temperature, followed by longer (200 ns) and lower-amplitude (37% of previous amplitude) pulse, which serves to induce crystallization. Actually, this double-step pulse can be exploited alone to reach different levels inside the single cell, eliminating the first programming pulse, reducing further time operation. In fact, the first high amplitude step is able to erase any previous GST225 state, while the second longer and lower amplitude pulse can control the amount of crystallized fraction, according to its duration. Higher duration corresponds to a higher amount of crystalline phase and lower transmission. The preparation of a device with a furtherly increased memory capacity of 512 bits has been recently demonstrated by Feldmann et al. [114]. The device is a memory in the array format, composed of 16 × 16 cells (16 rows, each containing 16 cells). Each cell is formed by two microring resonators in series coupled to three bus waveguides (made of Si₃N₄ on SiO₂, deposited on silicon carrier wafer): one input waveguide, one perpendicular connection waveguide, and one output waveguide. The input waveguide is the same for the whole device, passing all the cells along all the rows. Each row, instead, has a proper output waveguide, leading to 16 output waveguides in the whole device. The connection waveguides contain a GST225 patch on their top, one for each cell (Figure 16a). Each cell is characterized by a two-bit capacity, since by controlling the phase transition of the GST225 patch, it is possible to achieve 4 levels. The two resonators inside a single cell are characterized by the same radius and therefore the same resonance wavelength, but it is different for all the cells inside one row. In this way, an individual cell can be addressed by selecting light wavelength, both during the programming (changing the GST225 phase) and the reading process. The reading step proceeds as follows: low-intensity light traveling along the input waveguide is evanescently coupled (according to its wavelength resonator radius) to the lower resonator and the connection waveguide of a single cell; after passing the connection waveguide, light is coupled to the output waveguide of the proper row through the upper resonator of the same cell and it is finally read out at the output port of the corresponding line (selecting the appropriate wavelength). According to the crystallographic state of the GST225 patch on the connection waveguide, which is the real memory element of the cell, the amount of light transmitted at the output drop waveguide can be controlled. The programming step is linked to GST225 phase transition and it is obtained by letting high-intensity light flow through the output waveguide (selecting the desired row and wavelength) and coupling it to the upper resonator and the connection waveguide. Depending on the intensity of the laser pulse, four different crystallization levels can be reached (full crystallization for 550 pJ) (Figure 16b). Specifically, crystallization is achieved by means of multistep pulses (similar to the method proposed by Li et al. [115]) composed of one pulse of 50 ns and about 200 pJ, which is responsible for material melting at a temperature higher than crystallization temperature, plus two pulses of lower energy and variable duration (from 0 to 300 ns), which enable to control the degree of crystallization. Higher duration corresponds to a higher crystallization, which leads to lower transmission of light at the output port during the read-out process. The functionality of the proposed device has been successfully demonstrated for the memorization and reproduction of a colored image in 4 colors (2 bits), with high precision.

Materials 2021, 14, 3396

27 of 36

[图片: a)increasing resonance wavelength...NNRow NPCMchanging input gapRow 2Row 1inputoutpuoutputand writeand write(S2)(S1,SN]
[图片: |Time (s)|Transmission (norm)| |:---:|:---:| |0|0.05| |5|0.95| |10|0.45| |15|0.05| |20|0.95| |25|0.45| |30|0.05| |35|0.95| |40|0.45| |45|0.05| |50|0.95| |55|0.45| |60|0.05|]
# Figure 16. (a) Sketch describing the operation principle of the photonic memory proposed by Feldmann et al. [114]. Several PCM-cells are combined into rows and can be addressed individually; (b) Multilevel operation of a single memory cell. The phase-change material can be reversibly switched between four clearly distinguishable levels, characterized by different transmissions.

Until now it has been exploited the non-volatility of the GST225 phase transition, to store information in a permanent way inside a non-volatile memory device. In order to induce erasing of the stored information, it is necessary to actively operate on the device, by making light flow along with the device and making occur the GST225 phase transition in the opposite sense. Indeed, in this way, it is possible to mimic only the long-term memory, but not the short-term memory behavior, typical of biological neurons and synapses. Obtaining artificial memory devices that are able to sustain, on-demand, both behaviors will be a further step towards the development of neuromorphic computers. In this contest, Youngblood et al. demonstrated that it is possible to control the duration of retention of phase change inside GST225, by applying a high-energy writing pulse and another high (variable) energy probe pulse [116]. In this case, the probe pulse can also modify the GST225 phase, and it is possible to control the retention time of the previously stored information, by changing its energy. The prosed device is a $Si_3N_4$ waveguide on which 2 µm-long and 10 nm-thick GST225 patches are deposited, covered by a 10 nm ITO protecting layer. The device has been annealed, so at the beginning, the GST225 is in the crystalline phase. By applying a high-intensity writing pulse it is possible to induce gradual amorphization. In order to reach a volatile behavior, the applied probe pulse has to be characterized by energy high enough to perturb GST225 and modify its phase, inducing recrystallization (higher crystallization for higher power). A new value of transmission, which gradually lowers, is obtained at the read-out port, which depends both on the GST225 state after the first writing pulse (i.e., power of the writing pulse) and the power of the probe pulse. In particular, the higher the power of the probe pulse, the faster the recrystallization process, and transmission variation is more pronounced (Figure 17a). The same effect is obtained in the case of low writing power. Thus, by controlling these two parameters, it is possible to optically control data retention time, controlling volatility from years (low probe pulse and high writing pulse) to milliseconds (high probe pulse and moderate writing pulse). This strategy has been exploited to implement inside a photonic device also an example of data computing process:

Materials 2021, 14, 3396

28 of 36

the detection of coincident events between multiple inputs. Coincidence detection is based on the fact that GST225 amorphization can be pursued only when a sufficiently high temperature is obtained. So, when low-energy pulses are used for writing, two pulses must be simultaneously applied (coincidence pulse) (Figure 17b). By monitoring transmission at the read-out port, according to the delay between the two writing laser pulses, it is possible to record some variations: in the case of coincidence (0 ns delay) transmission remains constant at a high value, with small spikes; as delay increases lower values of transmission are obtained (indicating that amorphization has been only partially obtained) and duration and amplitude of transmission spikes decrease. In the case of not correlated pulses, amorphization is not even reached and transmission remains zero (Figure 17c).

# a)

[图片: |时间 (ps)|Normalized ΔTransmission| |:---:|:---:| |0.0|1.0| |0.5|0.9| |1.0|0.7| |1.5|0.5| |2.0|0.3| |2.5|0.1| |3.0|0.0|]
# b)

[图片: 未能识别到文本内容]
# c)

[图片: |Time (ms)|Delay Time 0 ns|Delay Time 5 ns|Delay Time 10 ns|Delay Time 20 ns|Delay Time 50 ns| |:---:|:---:|:---:|:---:|:---:|:---:| |0|4|2|0|0|0| |5|4|1.5|0.5|0|0| |10|4|1|0.2|-0.5|0| |15|4|0.5|0|-0.2|0| |20|4|0|0|-0.5|0| |25|2|0|0|-0.2|0| |30|0|0|0|-0.2|0|]
# Figure 17. (a) Variation of the optical transmission with increasing optical probe power. At low probe powers (black line), the device remains in the amorphous state for nonvolatile operation, while increasing the probe power causes recrystallization of the GST225; (b) detection of coincident events between two signals using volatile phase-change memory. Only when two pulses overlap in time, the combined optical power surpass the threshold required to reach an amorphous state (higher transmission level) and can be detected by the device; (c) multipulse device dynamics using two pulse trains with varying time delays between them. When the two pulse trains are overlapped in time, the transmission is at a maximum, indicating the two signals are correlated. Reproduced from Ref. [116] with permission from Wiley.

The possibility to achieve a non-volatile regime for data storage has been demonstrated by the same authors also inside a device made of a ring resonator (containing a GST225 switching patch) and coupled to two waveguides.

The capability of simultaneously store and process information by means of a photonic device based on PCMs has been demonstrated also by Feldmann et al., who reported an all-optical abacus-like calculating unit [117]. Abacus provides two of the most basic functions of a computer, processing (calculation) and memory (storage), simultaneously and in a single device, enabling to overcome time limitations of modern computers based on von-Neumann architectures, which separate, in time and space, these operations and require further data transfer and connections. The proposed device is a rectangular waveguide array with a PCM cell at every waveguide crossing point. Each PCM cell with a straight waveguide corresponds to a single processing unit, which can be independently switched thanks to a two-step method (Figure 18a). The pulses of the two steps are launched into the photonic array via two orthogonal waveguides, superimposing at the crossing incorporating the PCM-cell that has to be switched, and they are characterized by energy such that only when they arrive together, the PCM heats up sufficiently to induce a phase transition, similarly to what reported in the case of coincidence detection. In the case of multiple rows and multiple columns array, a simple transmission measurement is no longer appropriate for reading, since the optical transmission along any row or column in the waveguide array is influenced by all the phase-change cells lying on the same row or column. In this case, a two-step pulse scheme is used also for the read-out process: after a PCM-cell has been set to a specific level after the writing process (data processing and memorization), a reset operation consisting of two overlapping pulses is applied. The

Materials 2021, 14, 3396

29 of 36

change in transmission depends on the initial state of the PCM; thus, by sending a reset two-step pulse to the crossing of interest and detecting how much the transmission changes, we can selectively read the state of each PCM-cell in the array in a destructive manner. As PCMs the authors tested both GST225 and AIST, without noticing significant differences.

# a)

[图片: PhotonicPCMwaveguidesFocusing gratingcouplers]
# b)

[图片: |Time (s)|Change in optical transmission (%)| |:---:|:---:| |0|20| |5|10| |10|5| |15|2| |20|0|]
# c)

[图片: |Time (s)|Value| |:---:|:---:| |0|12| |5|4| |10|4| |15|2| |20|12| |25|6| |30|6|]
# Figure 18. (a) Optical micrograph of a crossed-waveguide photonic array used as a memory device for the implementation of arithmetic calculation. Scale bar is 100 µm; (b) level definition in a base-ten device; (c) example of addition: with the transmission levels defined in b), '6 + 6 = 12' is calculated. By analogy to the operation of an abacus, a carryover is performed when the tenth level is reached, and the cell is reset to its initial state. The result '12' is obtained from one carryover, which can be read in another cell (the corresponding to "tens"), and the final state of the illustrated PCM-cell, which is at level 2. Reproduced from Ref. [117] with permission from Nature Springer.

In this configuration, each PCM cell represents a single place value, corresponding to the different rows of the abacus, while the abacus beads are represented by ‘quanta’ of crystallization in the PCM (in the form of transmission variation). If we work in base 10, the first cell represents ones, the second tens, the third hundreds, and so on. The number of the base, instead, is linked to the number of crystallization levels that can be reached, and depends on the energy of the laser pulses used until complete crystallization (in the case of base 10, the PCM can be fully crystallized by applying 10 pulses, as shown in Figure 18b). The sliding of a bead to the right (increasing value)/left (decreasing value) is thus represented by stepwise crystallization/amorphization. With this device, the authors demonstrate the possibility to perform all the arithmetic operations: addition, multiplication (in the form of successive addition), subtraction (exploiting numbers complements approach) and division (in the form of repeated subtractions). In Figure 18c, the case of 6 + 6 addition in base ten is reported. Starting from state 0, pulse sequences equivalent to the first summand are sent into the waveguide which sets the first PCM-cell to level six. Then the second summand is added by sending the corresponding (six) pulses. When reaching the tenth level (after four pulses), the first PCM-cell is reset to level 0 (by inducing amorphization) before the rest of the input sequence (two pulses) is applied, by inducing new crystallization. While resetting the cell, one crystallization pulse is sent to a second PCM-cell representing the next highest order multiple of the base to store the carryover information, in this case, “tens” (not shown in the graph). At the end of the calculation, the shown PCM-cell is at level 2 while the second PCM-cell is at level 1, revealing the expected answer of 12.

A similar device composed of multiple phase-change cells can be used also to perform direct multiplication, by encoding the information related to the first multiplicand into the transmittance level of the cell after the first writing pulse, and the value of the second multiplier into the value of the power used for the “reading” ($P_{in}$) pulse. In this way, the power of the pulse of $P_{in}$ at the output port, $P_{out}$, depends on the value of transmittance of the waveguide and represents the result of the multiplication, $P_{out} = T((P_{Write}) \times P_{in})$. A similar device composed of multiple phase-change cells can be used also to perform matrix-vector multiplication (using memory cells in series and combining the output

Materials 2021, 14, 3396

30 of 36

signals containing the result of each multiplication, carried out in different cells, by means of beam splitter), which is a basis of many operations of artificial intelligence [118].

Cheng et al. demonstrated that photonic phase-change cells can be used also for the preparation of programmable optical logic devices, based on both “OR” and “NAND” logics [119].

Cheng et al. take a further step forward in the development of photonic neuromorphic computing, demonstrating that photonic synapses obtained by incorporating multiple, small, and discrete GST225 islands on tapered Si₃N₄ waveguides can mimic the behavior of biological synapses [120]. The employment of multiple islands instead of a unique patch enables better control of the interaction between the optical pulse and GST225 and better control of its phase transition. In biological brains, a neuron (called pre-neuron) generates action potentials (spikes, fire time $t_{pre}$) that propagate along the axon and are transmitted through a junction to the next neuron (called post-neuron) that generates the postsynaptic action potentials (fire time $t_{post}$). The junction is the synapse, which is characterized by a synaptic weight (w) determining the communication strength between the two neurons. At the basis of memory and learning in the human and animal brain, there is “synaptic plasticity”, that is the capability of changing dynamically synaptic weight, defined as $\Delta w = f(t_{post} - t_{pre}) = Ae^{-\Delta t/\tau}$, where A and $\tau$ are constants and $\Delta t$ is the time delay between pre- and post-synaptic signals. In the proposed photonic synapse, the synaptic weight is determined by the level of transmission of the waveguide. In particular, the authors demonstrated that the proposed photonic synapses are effectively able to modify the synaptic weight with an exponential dependence on the time delay between pre- and post-synaptic signals, mimic efficiently biological systems.

The possibility of developing and exploit photonic non-volatile synapses has been explored also by Chakraborty et al., who demonstrated that the proposed computing platform can be used to emulate a Spiking Neural Network inferencing engine for complex operations, such as image classification [121,122]. Wu et al. have recently demonstrated that a programmable waveguide mode converter based on GST225 can be programmed at 64 distinguishable levels, which are used to represent the weight parameters in matrix-vector multiplication computation with neuronal networks. They demonstrate the capability of the obtained system of performing image processing tasks, such as edge detection and pattern recognition, paving the way for the development of efficient optical computing [123].

# 6. Conclusions and Outlook

PCMs are a special subset of stimuli-responsive materials that offer a wide gamut of applications in optics and electronics. The rapid and drastic variation of their optical properties, in particular refractive index and extinction coefficient, opens the door to the burgeoning field of active photonics and optoelectronics. This work reviewed some relevant examples in the fields of optics, photonics and optoelectronics. In this context, $VO_2$ and different types of GSTs are the most investigated materials and several architectures have been explored. A very important sector is represented by dynamic displays. GSTs thin films enable to fully exploit interference effects with other oxide layers that serve either as substrates (e.g., ITO) or thermal (e.g., $Ta_2O_5$) and diffusion (Ti/TiN) barriers. The fine-tuning of the degree of crystallization/amorphization of the PCMs is a key factor for the development of multicolored dynamic displays that can be controlled by direct or indirect (i.e., electrically- or light-driven) thermal stimuli. The use of PCM-based metasurfaces that take advantage of dynamic optical resonances is a very useful strategy for fabricating ON/OFF bicolor displays. $VO_2$ thin films and metasurfaces represent a promising evolution of PCM-based displays that can operate either in IR or Visible. In particular, the research on rewritable metacanvas is not limited to displays but can be extended to the fabrication of optical devices embedding multiple functions, such as beam steering and hologram generation. In addition to dynamic optical displays, PCMs can offer a variety of applications in optical switching that is at the basis of reconfigurable photonic devices requiring either non-volatile (obtained by GSTs) or volatile (obtained by

Materials 2021, 14, 3396

31 of 36

VO2) phase transitions. In particular, VO2 is suitable for low-power devices, asking for low-intensity optical modulation. PCMs have been extensively integrated into photonic

waveguides and resonators, planar thin ﬁlms and patterned photonic structures operating

in different ranges of the electromagnetic spectrum, from Visible to Terahertz. PCMs can also be coupled to nanoantennas and nanoresonators, allowing us to control their optical resonances. Metamaterials and metasurfaces can take full advantage of such a

very exciting opportunity, which could be transformed into a real breakthrough for active nanophotonics and sensing. Moreover, examples of the applications of PCMS in computing

and information storage have been reviewed, showing the impressive progress in the development of photonic memory devices. Nucleation-dominated crystallization still

represents a major bottleneck for phase-change memories, however huge advancement has

been made in the last years, making PCM thin ﬁlms attractive for large-scale production.

In fact, the possibility to deposit PCM thin ﬁlms at low temperature on ﬂexibles substrates is promising for roll-to-roll fabrication of large-area devices.

In addition to pioneering works on all-dielectric reconﬁgurable optical devices and metamaterials, many other ﬁelds of applications remain unexplored. In particular, ultrasensitive vibrational spectroscopies (e.g., Raman and IR) can be a proﬁtable next frontier

for all-dielectric PCMs, in view of leading the development of portable, ultra-compact sensors that overcome the low reproducibility and stability issues of current high-sensitivity devices [124–128]. Another broad ﬁeld of possible applications for PCM-based thin ﬁlms and nanostructures is nonlinear optics. While nonlinear optical effects in chalcogenides’have been extensively investigated (see, e.g., [129]), little to no attention has been so far devoted to change of nonlinear optical interactions driven by the phase transition in PCM chalcogenides and VO2, such as modulation of harmonic generation and variations of self-phase modulation.

Further promising ﬁelds of applications of PCMs encompass smart catalysts for environmental remediation [130–133] and system chemistry applied to solid-state devices [134].

Broadening the horizons of research could stimulate the discovery and development of new materials and architectures, with major, yet unpredictable beneﬁts for different areas of application. Intense efforts and giant steps forward can be expected in the next years, as not only the “times”, but also “phases” need to rapidly change.

Author Contributions: Conceptualization, I.V., I.A. and D.d.C.; writing—original draft preparation,I.V. and D.d.C.; writing—review and editing, I.V., D.d.C., I.A.; supervision, I.A. All authors have read and agreed to the published version of the manuscript.

Funding: This research was partially funded by the Italian Ministry of University and Research(MUR) through the PRIN project NOMEN (2017MP7F8F). Research of D.d.C. was partly performed within Project “Internet of Things: Sviluppi Metodologici, Tecnologici E Applicativi”, cofunded(2018–2022) by the Italian Ministry of Education, Universities and Research (MIUR) under the aegis of the “Fondo per il ﬁnanziamento dei dipartimenti universitari di eccellenza” initiative (Law 232/2016).

Institutional Review Board Statement: Not applicable.

Informed Consent Statement: Not applicable.

Data Availability Statement: The data underlying this article will be shared on reasonable request from the corresponding author.

Conﬂicts of Interest: The authors declare no conﬂict of interest. The funders had no role in the design of the study; in the collection, analyses, or interpretation of data; in the writing of the manuscript, or in the decision to publish the results.

References

1. Gong, Z.; Yang, F.; Wang, L.; Chen, R.; Wu, J.; Grigoropoulos, C.P.; Yao, J. Phase change materials in photonic devices. J. Appl.

Phys. 2021, 129, 030902. [CrossRef]

2. Peccianti, M. Grand Challanges in Photonics: Route to Light. Front. Photonics 2021, 1, 626728. [CrossRef]

Materials 2021, 14, 3396

32 of 36

3. Jha, A.; Huang, C.; Prucnal, P.R. Reconfigurable all-optical nonlinear activation functions. Opt. Lett. 2020, 45, 4819–4822. [CrossRef]

4. De Angelis, C. Non Linear Optics. Front. Photonics 2021, 1, 628215. [CrossRef]

5. Nedelijkovic, M.; Littlejohns, C.G.; Khokhar, A.Z.; Banakar, M.; Cao, W.; Penades, J.S.; Tran, D.T.; Gardes, F.Y.; Thomson, D.J.; Reed, G.T.; et al. Silicon-on-insulator free-carrier injection modulators for the mid-infrared. Opt. Lett. 2019, 44, 915–918. [CrossRef] [PubMed]

6. Szukalski, A.; Korbut, A.; Ortyl, E. Structural and light driven molecular engineering in photochromic polymers. Polymer 2020, 192, 122311. [CrossRef]

7. Maire, J.; Arregui, G.; Capuj, N.E.; Colombano, M.F.; Griol, A.; Martinez, A.; Sotomayor-Torres, C.M.; Navarro-Urrios, D. Optical modulation of coherent phonon emission in optomechanical cavities. APL Photonics 2018, 3, 126102. [CrossRef]

8. Cao, T.; Wang, R.; Simpson, R.E.; Li, G. Photonic Ge-Sb-Te phase change metamaterials and their applications. Prog. Quantum Electron. 2020, 74, 100299. [CrossRef]

9. Raeis-Hosseini, N.; Rho, J. Metasurfaces based on phase-change material as a reconfigurable platform for multifunctional devices. Materials 2017, 10, 1046. [CrossRef]

10. Hale, D.V.; Hoover, M.J.; O'Neill, M.J. Phase Change Materials Handbook; National Technical Information Service U.S. Department of Commerce: Huntsville, AL, USA, 1971.

11. Zhang, Y.; Chou, J.B.; Li, J.; Li, H.; Du, Q.; Yadav, A.; Zhou, S.; Shalaginov, M.Y.; Fang, Z.; Zhong, H.; et al. Broadband transparent optical phase change materials for high-performance nonvolatile photonics. Nat. Commun. 2019, 10, 4279. [CrossRef] [PubMed]

12. Wuttig, M.; Bhaskaran, H.; Taubner, T. Phase-change materials for non-volatile photonic applications. Nat. Photonics 2017, 11, 465–476. [CrossRef]

13. Lencer, D.; Salinga, M.; Grabowski, B.; Hickel, T.; Neugebauer, J.; Wuttig, M. A map for phase-change materials. Nat. Mater. 2008, 7, 972–977. [CrossRef] [PubMed]

14. Zheng, J.; Khanolkar, A.; Xu, P.; Colburn, S.; Deshmukh, S.; Myers, J.; Frantz, J.; Pop, E.; Hendrickson, J.; Doylend, J.; et al. GST-on-silicon hybrid nanophotonic integrated circuits: A non-volatile quasi-continuously reprogrammable platform. Opt. Mater. Express 2018, 8, 1551–1561. [CrossRef]

15. Shi, X.; Chen, C.; Liu, S.; Li, G. Nonvolatile, reconfigurable and narrowband mid-infrared filter based on surface lattice resonance in phase-change ge2sb2te5. Nanomaterials 2020, 10, 2530. [CrossRef] [PubMed]

16. Raoux, S. Phase change materials. Annu. Rev. Mater. Res. 2009, 39, 25-48. [CrossRef]

17. Raoux, S.; Xiong, F.; Wuttig, M.; Pop, E. Phase change materials and phase change memory. MRS Bull. 2014, 39, 703–710. [CrossRef]

18. Michel, A.K.U.; Sousa, M.; Yarema, M.; Yarema, O.; Ovuka, V.; Lassaline, N.; Wood, V.; Norris, D.J. Optical Properties of Amorphous and Crystalline GeTe Nanoparticle Thin Films: A Phase-Change Material for Tunable Photonics. ACS Appl. Nano Mater. 2020, 3, 4314–4320. [CrossRef]

19. De Leonardis, F.; Soref, R.; Passaro, V.M.N.; Zhang, Y.; Hu, J. Broadband Electro-Optical Crossbar Switches Using Low-Loss Ge2Sb2Se4Te1 Phase Change Material. J. Light. Technol. 2019, 37, 3183–3191. [CrossRef]

20. Martinez, J.C.; Lu, L.; Ning, J.; Dong, W.; Cao, T.; Simpson, R.E. The Origin of Optical Contrast in $Sb_2Te_3$-Based Phase-Change Materials. Phys. Status Solidi Basic Res. 2020, 257, 1900289. [CrossRef]

21. Ríos, C.; Hosseini, P.; Taylor, R.A.; Bhaskaran, H. Color Depth Modulation and Resolution in Phase-Change Material Nanodisplays. Adv. Mater. 2016, 28, 4720–4726. [CrossRef]

22. Kim, Y.T.; Kim, E.T.; Kim, C.S.; Lee, J.Y. Phase transformation mechanism of In-Sb-Te through the boundary reaction between InSb and InTe. Phys. Status Solidi Rapid Res. Lett. 2011, 5, 98–100. [CrossRef]

23. Shao, Z.; Cao, X.; Luo, H.; Jin, P. Recent progress in the phase-transition mechanism and modulation of vanadium dioxide materials. NPG Asia Mater. 2018, 10, 581-605. [CrossRef]

24. Wilson, K.; Marocico, C.A.; Bradley, A.L. Dynamic structural colour using vanadium dioxide thin films. J. Phys. D Appl. Phys. 2018, 51, 255101. [CrossRef]

25. Vassalini, I.; Alessandri, I. Spatial and Temporal Control of Information Storage in Cellulose by Chemically Activated Oscillations. ACS Appl. Mater. Interfaces 2015, 7, 28708–28713. [CrossRef]

26. Bontempi, N.; Vassalini, I.; Danesi, S.; Ferroni, M.; Donarelli, M.; Colombi, P.; Alessandri, I. Non-Plasmonic SERS with Silicon: Is It Really Safe? New Insights into the Optothermal Properties of Core/Shell Microbeads. J. Phys. Chem. Lett. 2018, 9, 2127–2132. [CrossRef]

27. Sun, H.; Liu, S.; Lin, W.; Zhang, K.Y.; Lv, W.; Huang, X.; Huo, F.; Yang, H.; Jenkins, G.; Zhao, Q.; et al. Smart responsive phosphorescent materials for data recording and security protection. Nat. Commun. 2014, 5, 2–10. [CrossRef] [PubMed]

28. Klajn, R.; Wesson, P.J.; Bishop, K.J.M.; Grzybowski, B.A. Writing self-erasing images using metastable nanoparticle "inks". Angew. Chem. Int. Ed. 2009, 48, 7035–7039. [CrossRef]

29. Alessandri, I.; Ferroni, M.; Depero, L.E. Plasmonic Heating-Assisted Transformation of SiO₂/ Au Core/Shell Nanospheres (Au Nanoshells): Caveats and Opportunities for SERS and Direct Laser Writing. Plasmonics 2013, 8, 129–132. [CrossRef]

30. Alessandri, I; Depero, L.E. Laser-induced modification of polymeric beads coated with gold nanoparticles. Nanotechnology 2008, 19. [CrossRef]

Materials 2021, 14, 3396

33 of 36

31. Häckel, M.; Kador, L.; Kropp, D.; Schmidt, H.W. Polymer blends with azobenzene-containing block copolymers as stable rewritable volume holographic media. Adv. Mater. 2007, 19, 227–231. [CrossRef]

32. Hosseini, P.; Wright, C.D.; Bhaskaran, H. An optoelectronic framework enabled by low-dimensional phase-change films. Nature 2014, 511, 206–211. [CrossRef] [PubMed]

33. Hosseini, P.; Bhaskaran, H. Colour performance and stack optimisation in phase change material based nano-displays. Integr. Photonics Mater. Devices Appl. III 2015, 9520, 95200M. [CrossRef]

34. Meng, Y.; Behera, J.K.; Wen, S.; Simpson, R.E.; Shi, J.; Wu, L.; Song, Z.; Wei, J.; Wang, Y. Ultrafast Multilevel Optical Tuning with CSb₂Te₃ Thin Films. Adv. Opt. Mater. 2018, 6, 1800360. [CrossRef]

35. Yoo, S.; Gwon, T.; Eom, T.; Kim, S.; Hwang, C.S. Multicolor Changeable Optical Coating by Adopting Multiple Layers of Ultrathin Phase Change Material Film. ACS Photonics 2016, 3, 1265–1270. [CrossRef]

36. Jafari, M.; Guo, L.J.; Rais-Zadeh, M. A Reconfigurable Color Reflector by Selective Phase Change of GeTe in a Multilayer Structure. Adv. Opt. Mater. 2019, 7, 1801214. [CrossRef]

37. Meng, Y.; Behera, J.K.; Ke, Y.; Chew, L.; Wang, Y.; Long, Y.; Simpson, R.E. Design of a 4-level active photonics phase change switch using VO₂ and Ge₂Sb₂Te₅. Appl. Phys. Lett. 2018, 113, 071901. [CrossRef]

38. Schlich, F.F.; Zalden, P.; Lindenberg, A.M.; Spolenak, R. Color switching with enhanced optical contrast in ultrathin phase-change materials and semiconductors induced by femtosecond laser pulses. ACS Photonics 2015, 2, 178–182. [CrossRef]

39. Liu, F.; Shi, H.; Zhu, X.; Dai, P.; Lin, Z.; Long, Y.; Xie, Z.; Zhou, Y.; Duan, H. Tunable reflective color filters based on asymmetric Fabry-Perot cavities employing ultrathin $Ge_2Sb_2Te_5$ as a broadband absorber. Appl. Opt. 2018, 57, 9040–9045. [CrossRef]

40. Gholipour, B.; Karvounis, A.; Yin, J.; Soci, C.; MacDonald, K.F.; Zheludev, N.I. Phase-change-driven dielectric-plasmonic transitions in chalcogenide metasurfaces. NPG Asia Mater. 2018, 10, 533–539. [CrossRef]

41. Carrillo, S.G.C.; Trimby, L.; Au, Y.Y.; Nagareddy, V.K.; Rodriguez-Hernandez, G.; Hosseini, P.; Ríos, C.; Bhaskaran, H.; Wright, C.D. A Nonvolatile Phase-Change Metamaterial Color Display. Adv. Opt. Mater. 2019, 7, 18017782. [CrossRef]

42. Chandra, S.; Franklin, D.; Cozart, J.; Safaei, A.; Chanda, D. Adaptive Multispectral Infrared Camouflage. ACS Photonics 2018, 5, 4513–4519. [CrossRef]

43. Nagasaki, Y.; Kohno, T.; Bando, K.; Takase, H.; Fujita, K.; Takahara, J. Adaptive printing using VO₂ optical antennas with subwavelength resolution. Appl. Phys. Lett. 2019, 115, 161105. [CrossRef]

44. Xu, Z.; Li, Q.; Du, K.; Long, S.; Yang, Y.; Cao, X.; Luo, H.; Zhu, H.; Ghosh, P.; Shen, W.; et al. Spatially Resolved Dynamically Reconfigurable Multilevel Control of Thermal Emission. Laser Photonics Rev. 2020, 14, 1900162. [CrossRef]

45. Shu, F.Z.; Yu, F.F.; Peng, R.W.; Zhu, Y.Y.; Xiong, B.; Fan, R.H.; Wang, Z.H.; Liu, Y.; Wang, M. Dynamic Plasmonic Color Generation Based on Phase Transition of Vanadium Dioxide. Adv. Opt. Mater. 2018, 6, 1700939. [CrossRef]

46. He, J.; Zhang, M.; Shu, S.; Yan, Y.; Wang, M. VO₂ based dynamic tunable absorber and its application in switchable control and real-time color display in the visible region. Opt. Express 2020, 28, 37590–37599. [CrossRef]

47. Duan, X.; White, S.T.; Cui, Y.; Neubrech, F.; Gao, Y.; Haglund, R.F.; Liu, N. Reconfigurable Multistate Optical Systems Enabled by VO2Phase Transitions. ACS Photonics 2020, 7, 2958–2965. [CrossRef] [PubMed]

48. Dong, K.; Hong, S.; Deng, Y.; Ma, H.; Li, J.; Wang, X.; Yeo, J.; Wang, L.; Lou, S.; Tom, K.B.; et al. A Lithography-Free and Field-Programmable Photonic Metacanvas. Adv. Mater. 2018, 30, 1703878. [CrossRef]

49. Briggs, R.M.; Pryce, I.M.; Atwater, H.A. Compact silicon photonic waveguide modulator based on the vanadium dioxide metal-insulator phase transition. Opt. Express 2010, 18, 11192–11201. [CrossRef] [PubMed]

50. Stegmaier, M.; Ríos, C.; Bhaskaran, H.; Wright, C.D.; Pernice, W.H.P. Nonvolatile All-Optical 1 × 2 Switch for Chipscale Photonic Networks. Adv. Opt. Mater. 2017, 5, 1600346. [CrossRef]

51. Ryckman, J.D.; Diez-Blanco, V.; Nag, J.; Marvel, R.E.; Choi, B.K.; Haglund, R.F.; Weiss, S.M. Photothermal optical modulation of ultra-compact hybrid Si-VO₂ ring resonators. Opt. Express 2012, 20, 13215–13225. [CrossRef] [PubMed]

52. Rudé, M.; Pello, J.; Simpson, R.E.; Osmond, J.; Roelkens, G.; Van Der Tol, J.J.G.M.; Pruneri, V. Optical switching at 1.55 µm in silicon racetrack resonators using phase change materials. Appl. Phys. Lett. 2013, 103, 141119. [CrossRef]

53. Ryckman, J.D.; Hallman, K.A.; Marvel, R.E.; Haglund, R.F.; Weiss, S.M. Ultra-compact silicon photonic devices reconfigured by an optically induced semiconductor-to-metal transition. Opt. Express 2013, 21, 10753–10763. [CrossRef]

54. Joushaghani, A.; Jeong, J.; Paradis, S.; Alain, D.; Stewart Aitchison, J.; Poon, J.K.S. Wavelength-size hybrid Si-VO₂ waveguide electroabsorption optical switches and photodetectors. Opt. Express 2015, 23, 3657–3668. [CrossRef]

55. Markov, P.; Marvel, R.E.; Conley, H.J.; Miller, K.J.; Haglund, R.F.; Weiss, S.M. Optically Monitored Electrical Switching in VO₂. ACS Photonics 2015, 2, 1175–1182. [CrossRef]

56. Miller, K.J.; Hallman, K.A.; Haglund, R.F.; Weiss, S.M. Silicon waveguide modulator with embedded phase change material. Opt. Express 2017, 25, 26527–26536. [CrossRef]

57. Zhang, Q.; Zhang, Y.; Li, J.; Sref, R.; Gu, T.; Hu, J. Broadband nonvolatile photonic switching based on optical phase change materials: Beyond the classical figure-of-merit. Opt. Lett. 2018, 43, 94–97. [CrossRef]

58. Kats, M.A.; Sharma, D.; Lin, J.; Genevet, P.; Blanchard, R.; Yang, Z.; Qazilbash, M.M.; Basov, D.N.; Ramanathan, S.; Capasso, F. Ultra-thin perfect absorber employing a tunable phase change material. Appl. Phys. Lett. 2012, 101, 221101. [CrossRef]

59. Wan, C.; Horak, E.H.; King, J.; Salman, J.; Zhang, Z.; Zhou, Y.; Roney, P.; Gundlach, B.; Ramanathan, S.; Goldsmith, R.H.; et al. Limiting Optical Diodes Enabled by the Phase Transition of Vanadium Dioxide. ACS Photonics 2018, 5, 2688–2692. [CrossRef]

Materials 2021, 14, 3396

34 of 36

60. Sarangan, A.; Duran, J.; Vasilyev, V.; Limberopoulos, N.; Vitebskiy, I.; Anisimov, I. Broadband Reflective Optical Limiter Using GST Phase Change Material. IEEE Photonics J. 2018, 10, 2200409. [CrossRef]

61. Li, P.; Yang, X.; Maß, T.W.W.; Hanss, J.; Lewin, M.; Michel, A.K.U.; Wuttig, M.; Taubner, T. Reversible optical switching of highly confined phonon-polaritons with an ultrathin phase-change material. Nat. Mater. 2016, 15, 870–875. [CrossRef]

62. Guinneton, F.; Sauques, L.; Valmalette, J.C.; Cros, F.; Gavarri, J.R. Optimized infrared switching properties in thermochromic vanadium dioxide thin films: Role of deposition process and microstructure. Thin Solid Films 2004, 446, 287–295. [CrossRef]

63. Wang, W.; Luo, Y.; Zhang, D.; Luo, F. Dynamic optical limiting experiments on vanadium dioxide and vanadium pentoxide thin films irradiated by a laser beam. Appl. Opt. 2006, 45, 3378–3381. [CrossRef]

64. Benkahoul, M.; Chaker, M.; Margot, J.; Haddad, E.; Kruzelecky, R.; Wong, B.; Jamroz, W.; Poinas, P. Thermochromic $VO_2$ film deposited on Al with tunable thermal emissivity for space applications. Sol. Energy Mater. Sol. Cells 2011, 95, 3504–3508. [CrossRef]

65. Voti, R.L.; Larciprete, M.C.; Leahu, G.L.; Sibilia, C.; Bertolotti, M. Optimization of thermochromic $VO_2$ based structures with tunable thermal emissivity. J. Appl. Phys. 2012, 112, 034305. [CrossRef]

66. Abdollahramezani, S.; Hemmatyar, O.; Taghinejad, H.; Krasnok, A.; Kiarashinejad, Y.; Zandehshahvar, M.; Alù, A.; Adibi, A. Tunable Nanophotonics Enabled by Chalcogenide Phase-Change Materials. Nanophotonics 2020, 9, 1189–1241. [CrossRef]

67. Mikulics, M.; Hardtdegen, H.H. Fully photon operated transmistor/all-optical switch based on a layered Ge1Sb₂Te₄ phase change medium. FlatChem 2020, 23, 100186. [CrossRef]

68. Maaza, M.; Nemraoui, O.; Sella, C.; Beye, A.C.; Baruch-Barak, B. Thermal induced tunability of surface plasmon resonance in Au-VO₂ nano-photonics. Opt. Commun. 2005, 254, 188–195. [CrossRef]

69. Xu, G.; Chen, Y.; Tazawa, M.; Jin, P. Surface plasmon resonance of silver nanoparticles on vanadium dioxide. J. Phys. Chem. B 2006, 110, 2051–2056. [CrossRef] [PubMed]

70. Suh, J.Y.; Donev, E.U.; Ferrara, D.W.; Tetz, K.A.; Feldman, L.C.; Haglund, R.F. Modulation of the gold particle-plasmon resonance by the metal-semiconductor transition of vanadium dioxide. J. Opt. A Pure Appl. Opt. 2008, 10, 055202. [CrossRef]

71. Rini, M.; Cavalleri, A.; Schoenlein, R.W.; López, R.; Feldman, L.C.; Haglund, R.F.; Boatner, L.A.; Haynes, T.E. Photoinduced phase transition in $VO_2$ nanocrystals: Ultrafast control of surface-plasmon resonance. Opt. Lett. 2005, 30, 558–560. [CrossRef] [PubMed].

72. Li, S.Y.; Niklasson, G.A.; Granqvist, C.G. Nanothermochromics: Calculations for VO₂ nanoparticles in dielectric hosts show much improved luminous transmittance and solar energy transmittance modulation. J. Appl. Phys. 2010, 108, 063525. [CrossRef]

73. Zhu, J.; Zhou, Y.; Wang, B.; Zheng, J.; Ji, S.; Yao, H.; Luo, H.; Jin, P. Vanadium Dioxide Nanoparticle-based Thermochromic Smart Coating: High Luminous Transmittance, Excellent Solar Regulation Efficiency, and Near Room Temperature Phase Transition. ACS Appl. Mater. Interfaces 2015, 7, 27796–27803. [CrossRef] [PubMed]

74. Mlyuka, N.R.; Niklasson, G.A.; Granqvist, C.G. Mg doping of thermochromic VO₂ films enhances the optical transmittance and decreases the metal-insulator transition temperature. Appl. Phys. Lett. 2009, 95, 171909. [CrossRef]

75. Polking, M.J.; Jain, P.K.; Bekenstein, Y.; Banin, U.; Millo, O.; Ramesh, R.; Alivisatos, A.P. Controlling localized surface plasmon resonances in GeTe nanoparticles using an amorphous-to-crystalline phase transition. Phys. Rev. Lett. 2013, 111, 037401. [CrossRef] [PubMed]

76. Wang, Q.; Rogers, E.T.F.; Gholipour, B.; Wang, C.M.; Yuan, G.; Teng, J.; Zheludev, N.I. Optically reconfigurable metasurfaces and photonic devices based on phase change materials. Nat. Photonics 2016, 10, 60–65. [CrossRef]

77. Chu, C.H.; Tseng, M.L.; Chen, J.; Wu, P.C.; Chen, Y.H.; Wang, H.C.; Chen, T.Y.; Hsieh, W.T.; Wu, H.J.; Sun, G.; et al. Active dielectric metasurface based on phase-change medium. Laser Photonics Rev. 2016, 10, 986–994. [CrossRef]

78. Leitis, A.; Heßler, A.; Wahl, S.; Wuttig, M.; Taubner, T.; Tittl, A.; Altug, H. All-Dielectric Programmable Huygens' Metasurfaces. Adv. Funct. Mater. 2020, 30, 1910259. [CrossRef]

79. Kepič, P.; Ligmajer, F.; Hrtoň, M.; Ren, H.; Menezes, L.D.S.; Maier, S.A.; Šikola, T. Optically tunable Mie-resonance VO₂ nanoantennas for metasurfaces in the visible. ACS Photonics 2021, 8, 1048–1057. [CrossRef]

80. Tittl, A.; Michel, A.K.U.; Schäferling, M.; Yin, X.; Gholipour, B.; Cui, L.; Wuttig, M.; Taubner, T.; Neubrech, F.; Giessen, H. A. Switchable Mid-Infrared Plasmonic Perfect Absorber with Multispectral Thermal Imaging Capability. Adv. Mater. 2015, 27, 4597–4603. [CrossRef] [PubMed]

81. Michel, A.K.U.; Zalden, P.; Chigrin, D.N.; Wuttig, M.; Lindenberg, A.M.; Taubner, T. Reversible Optical Switching of Infrared Antenna Resonances with Ultrathin Phase-Change Layers Using Femtosecond Laser Pulses. ACS Photonics 2014, 1, 833–839. [CrossRef]

82. Suh, J.Y.; Donev, E.U.; Lopez, R.; Feldman, L.C.; Haglund, R.F. Modulated optical transmission of subwavelength hole arrays in metal-VO₂ films. Appl. Phys. Lett. 2006, 88, 133115. [CrossRef]

83. Driscoll, T.; Palit, S.; Qazilbash, M.M.; Brehm, M.; Keilmann, F.; Chae, B.G.; Yun, S.J.; Kim, H.T.; Cho, S.Y.; Jokerst, N.M.; et al. Dynamic tuning of an infrared hybrid-metamaterial resonance using vanadium dioxide. Appl. Phys. Lett. 2008, 93, 024101. [CrossRef]

84. Driscoll, T.; Kim, H.T.; Chae, B.G.; Kim, B.J.; Lee, Y.W.; Jokerst, N.M.; Palit, S.; Smith, D.R.; Di Ventra, M.; Basov, D.N. Memory metamaterials. Science 2009, 325, 1518–1521. [CrossRef]

85. Dicken, M.J.; Aydin, K.; Pryce, I.M.; Sweatlock, L.A.; Boyd, E.M.; Walavalkar, S.; Ma, J.; Atwater, H.A. Frequency tunable near-infrared metamaterials based on VO₂ phase transition. Opt. Express 2009, 17, 18330–18339. [CrossRef] [PubMed]

Materials 2021, 14, 3396

35 of 36

86. Sámson, Z.L.; MacDonald, K.F.; De Angelis, F.; Gholipour, B.; Knight, K.; Huang, C.C.; Di Fabrizio, E.; Hewak, D.W.; Zheludev, N.I. Metamaterial electro-optic switch of nanoscale thickness. Appl. Phys. Lett. 2010, 96, 143105. [CrossRef]

87. Gholipour, B.; Zhang, J.; MacDonald, K.F.; Hewak, D.W.; Zheludev, N.I. An all-optical, non-volatile, bidirectional, phase-change meta-switch. Adv. Mater. 2013, 25, 3050–3054. [CrossRef] [PubMed]

88. Chen, Y.G.; Kao, T.S.; Ng, B.; Li, X.; Luo, X.G.; Luk'yanchuk, B.; Maier, S.A.; Hong, M.H. Hybrid phase-change plasmonic crystals for active tuning of lattice resonances. Opt. Express 2013, 21, 13691–13698. [CrossRef] [PubMed]

89. Liu, M.; Hwang, H.Y.; Tao, H.; Strikwerda, A.C.; Fan, K.; Keiser, G.R.; Sternbach, A.J.; West, K.G.; Kittiwatanakul, S.; Lu, J.; et al. Terahertz-field-induced insulator-to-metal transition in vanadium dioxide metamaterial. Nature 2012, 487, 345–348. [CrossRef] [PubMed]

90. Michel, A.K.U.; Chigrin, D.N.; Maß, T.W.W.; Schönauer, K.; Salinga, M.; Wuttig, M.; Taubner, T. Using low-loss phase-change materials for mid-infrared antenna resonance tuning. Nano Lett. 2013, 13, 3470–3475. [CrossRef]

91. Kats, M.A.; Blanchard, R.; Genevet, P.; Yang, Z.; Qazilbash, M.M.; Basov, D.N.; Ramanathan, S.; Capasso, F. Thermal tuning of mid-infrared plasmonic antenna arrays using a phase change material. Opt. Lett. 2013, 38, 368–370. [CrossRef] [PubMed]

92. Alaee, R.; Albooyeh, M.; Tretyakov, S.; Rockstuhl, C. Phase-change material-based nanoantennas with tunable radiation patterns. Opt. Lett. 2016, 41, 4099–4102. [CrossRef] [PubMed]

93. Savaliya, P.B.; Thomas, A.; Dua, R.; Dhawan, A. Tunable optical switching in the near-infrared spectral regime by employing plasmonic nanoantennas containing phase change materials. Opt. Express 2017, 25, 23755–23772. [CrossRef] [PubMed]

94. Wang, H.; Yang, Y.; Wang, L. Switchable wavelength-selective and diffuse metamaterial absorber/emitter with a phase transition spacer layer. Appl. Phys. Lett. 2014, 105, 071907. [CrossRef]

95. Cao, T.; Wei, C.W.; Simpson, R.E.; Zhang, L.; Cryan, M.J. Broadband polarization-independent perfect absorber using a phase-change metamaterial at visible frequencies. Sci. Rep. 2014, 4, 3955. [CrossRef] [PubMed]

96. Zhu, Z.; Evans, P.G.; Haglund, R.F.; Valentine, J.G. Dynamically Reconfigurable Metadevice Employing Nanostructured Phase-Change Materials. Nano Lett. 2017, 17, 4881–4885. [CrossRef]

97. Tognazzi, A.; Locatelli, A.; Vincenti, M.A.; Giannetti, C.; De Angelis, C. Tunable Optical Antennas Using Vanadium Dioxide. Metal-Insulator Phase Transitions. Plasmonics 2019, 14, 1283–1288. [CrossRef]

98. Cao, T.; Zheng, G.; Wang, S.; Wei, C. Ultrafast beam steering using gradient Au-Ge₂Sb₂Te₅-Au plasmonic resonators. Opt. Express 2015, 23, 18029-18039. [CrossRef]

99. de Galarreta, C.R.; Alexeev, A.M.; Au, Y.Y.; Lopez-Garcia, M.; Klemm, M.; Cryan, M.; Bertolotti, J.; Wright, C.D. Nonvolatile Reconfigurable Phase-Change Metadevices for Beam Steering in the Near Infrared. Adv. Funct. Mater. 2018, 28, 1704993. [CrossRef]

100. Wang, D.; Zhang, L.; Gu, Y.; Mehmood, M.Q.; Gong, Y.; Srivastava, A.; Jian, L.; Venkatesan, T.; Qiu, C.W.; Hong, M. Switchable. Ultrathin Quarter-wave Plate in Terahertz Using Active Phase-change Metasurface. Sci. Rep. 2015, 5, 15020. [CrossRef] [PubMed].

101. Dong, W.; Qiu, Y.; Zhou, X.; Banas, A.; Banas, K.; Breese, M.B.H.; Cao, T.; Simpson, R.E. Tunable Mid-Infrared Phase-Change Metasurface. Adv. Opt. Mater. 2018, 6, 1701346. [CrossRef]

102. Karvounis, A.; Gholipour, B.; MacDonald, K.F.; Zheludev, N.I. All-dielectric phase-change reconfigurable metasurface. Appl. Phys. Lett. 2016, 109, 051103. [CrossRef]

103. Shalaginov, M.Y.; An, S.; Zhang, Y.; Yang, F.; Su, P.; Liberman, V.; Chou, J.B.; Roberts, C.M.; Kang, M.; Rios, C.; et al. Reconfigurable all-dielectric metalens with diffraction-limited performance. Nat. Commun. 2021, 12, 1225. [CrossRef]

104. Tripathi, A.; John, J.; Kruk, S.; Zhang, Z.; Nguyen, H.S.; Berguiga, L.; Romeo, P.R.; Orobtchouk, R.; Ramanathan, S.; Kivshar, Y.; et al. Tunable Mie-resonant dielectric metasurfaces based on $VO_2$ phase-transition materials. ACS Photonics 2021, 8, 1206–1213. [CrossRef]

105. Kim, S.J.; Kim, I.; Choi, S.; Yoon, H.; Kim, C.; Lee, Y.; Choi, C.; Son, J.; Lee, Y.W.; Rho, J.; et al. Reconfigurable all-dielectric Fano metasurfaces for strong full-space intensity modulation of visible light. Nanoscale Horiz. 2020, 5, 1088–1095. [CrossRef]

106. Lencer, D.; Salinga, M.; Wuttig, M. Design rules for phase-change materials in data storage applications. Adv. Mater. 2011, 23, 2030–2058. [CrossRef]

107. Bez, R.; Pirovano, A. Non-volatile memory technologies: Emerging concepts and new materials. Mater. Sci. Semicond. Process. 2004, 7, 349–355. [CrossRef]

108. Wong, H.S.P.; Raoux, S.; Kim, S.; Liang, J.; Reifenberg, J.P.; Rajendran, B.; Asheghi, M.; Goodson, K.E. Phase change memory. Proc. IEEE 2010, 98, 2201-2227. [CrossRef]

109. Noé, P.; Vallée, C.; Hippert, F.; Fillot, F.; Raty, J.Y. Phase-change materials for non-volatile memory devices: From technological challenges to materials science issues. Semicond. Sci. Technol. 2018, 33, 13002. [CrossRef]

110. Guo, P.; Sarangan, A.M.; Agha, I. A review of germanium-antimony-telluride phase change materials for non-volatile memories and optical modulators. Appl. Sci. 2019, 9, 530. [CrossRef]

111. Rios, C.; Stegmaier, M.; Hosseini, P.; Wang, D.; Scherer, T.; Wright, C.D.; Bhaskaran, H.; Pernice, W.H.P. Integrated all-photonic non-volatile multi-level memory. Nat. Photonics 2015, 9, 725–732. [CrossRef]

112. Pernice, W.H.P.; Bhaskaran, H. Photonic non-volatile memories using phase change materials. Appl. Phys. Lett. 2012, 101, 171101. [CrossRef]

113. Rios, C.; Hosseini, P.; Wright, C.D.; Bhaskaran, H.; Pernice, W.H.P. On-chip photonic memory elements employing phase-change materials. Adv. Mater. 2014, 26, 1372–1377. [CrossRef] [PubMed]

Materials 2021, 14, 3396

36 of 36

114. Feldmann, J.; Youngblood, N.; Li, X.; Wright, C.D.; Bhaskaran, H.; Pernice, W.H.P. Integrated 256 Cell Photonic Phase-Change Memory with 512-Bit Capacity. IEEE J. Sel. Top. Quantum Electron. 2020, 26, 8301807. [CrossRef]

115. Li, X.; Youngblood, N.; Ríos, C.; Cheng, Z.; Wright, C.D.; Pernice, W.H.; Bhaskaran, H. Fast and reliable storage using a 5 bit, nonvolatile photonic memory cell. Optica 2019, 6, 1–6. [CrossRef]

116. Youngblood, N.; Ríos, C.; Gemo, E.; Feldmann, J.; Cheng, Z.; Baldycheva, A.; Pernice, W.H.P.; Wright, C.D.; Bhaskaran, H. Tunable. Volatility of Ge₂Sb₂Te₅ in Integrated Photonics. Adv. Funct. Mater. 2019, 29, 1807571. [CrossRef]

117. Feldmann, J.; Stegmaier, M.; Gruhler, N.; Riós, C.; Bhaskaran, H.; Wright, C.D.; Pernice, W.H.P. Calculating with light using a chip-scale all-optical abacus. Nat. Commun. 2017, 8, 1256. [CrossRef]

118. Ríos, C.; Youngblood, N.; Cheng, Z.; Le Gallo, M.; Pernice, W.H.P.; David Wright, C.; Sebastian, A.; Bhaskaran, H. In-memory computing on a photonic platform. Sci. Adv. 2019, 5, eau5759. [CrossRef]

119. Cheng, Z.; Ríos, C.; Youngblood, N.; Wright, C.D.; Pernice, W.H.P.; Bhaskaran, H. Device-Level Photonic Memories and Logic Applications Using Phase-Change Materials. Adv. Mater. 2018, 30, 1802435. [CrossRef]

120. Cheng, Z.; Ríos, C.; Pernice, W.H.P.; David Wright, C.; Bhaskaran, H. On-chip photonic synapse. Sci. Adv. 2017, 3, e1700160. [CrossRef]

121. Chakraborty, I.; Saha, G.; Roy, K. A Photonic In-Memory Computing Primitive for Spiking Neural Networks Using Phase-Change Materials. Phys. Rev. Appl. 2019, 11, 014063. [CrossRef]

122. Chakraborty, I.; Saha, G.; Sengupta, A.; Roy, K. Toward Fast Neural Computing using All-Photonic Phase Change Spiking Neurons. Sci. Rep. 2018, 8, 12980. [CrossRef]

123. Wu, C.; Yu, H.; Lee, S.; Peng, R.; Takeuchi, I.; Li, M. Programmable phase-change metasurfaces on waveguides for multimode photonic convolutional neural network. Nat. Commun. 2021, 12, 96. [CrossRef] [PubMed]

124. Alessandri, I.; Lombardi, J.R. Enhanced Raman Scattering with Dielectrics. Chem. Rev. 2016, 116, 14921–14981. [CrossRef] [PubMed]

125. Bontempi, N.; Vassalini, I.; Alessandri, I. All-dielectric core/shell resonators: From plasmon-free SERS to multimodal analysis. J. Raman Spectrosc. 2018, 49, 943–953. [CrossRef]

126. Vassalini, I.; Bontempi, N.; Federici, S.; Ferroni, M.; Gianoncelli, A.; Alessandri, I. Cyclodextrins enable indirect ultrasensitive Raman detection of polychlorinated biphenyls captured by plasmonic bubbles. Chem. Phys. Lett. 2021, 775, 138674. [CrossRef]

127. Bontempi, N.; Vassalini, I.; Danesi, S.; Alessandri, I. ZORRO: Zirconium oxide resonators for all-in-one Raman and whispering-gallery-mode optical sensing. Chem. Commun. 2017, 53, 10382–10385. [CrossRef]

128. Alessandri, I.; Vassalini, I.; Bertuzzi, M.; Bontempi, N.; Memo, M.; Gianoncelli, A. “RaMassays”: Synergistic Enhancement of Plasmon-Free Raman Scattering and Mass Spectrometry for Multimodal Analysis of Small Molecules. Sci. Rep. 2016, 6, 34521. [CrossRef]

129. Zakery, A.; Elliott, S.R. Optical Nonlinearities in Chalcogenide Glasses and Their Applications; Springer: Berlin/Heidelberg, Germany, 2007; ISBN 10 3-540-71066-3.

130. Vassalini, I.; Ribaudo, G.; Gianoncelli, A.; Casula, M.F.; Alessandri, I. Plasmonic hydrogels for capture, detection and removal of organic pollutants. Environ. Sci. Nano 2020, 7, 3888–3900. [CrossRef]

131. Vassalini, I.; Gjipalaj, J.; Crespi, S.; Gianoncelli, A.; Mella, M.; Ferroni, M.; Alessandri, I. Alginate-Derived Active Blend Enhances Adsorption and Photocatalytic Removal of Organic Pollutants in Water. Adv. Sustain. Syst. 2020, 4, 1900112. [CrossRef]

132. Vassalini, I.; Alessandri, I. Switchable stimuli-responsive heterogeneous catalysis. Catalysts 2018, 8, 569. [CrossRef]

133. Vassalini, I.; Alessandri, I. “The phactalysts”: Carbon nanotube/TiO₂ composites as phototropic actuators for wireless remote triggering of chemical reactions and catalysis. Nanoscale 2017, 9, 11446–11451. [CrossRef] [PubMed]

134. Alessandri, I.; Vassalini, I. System chemistry in catalysis: Facing the next challenges in production of energy vectors and environmental remediation. Catalysts 2021, 11, 64. [CrossRef]
