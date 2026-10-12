---
media_id: "pdf_3867e2b60070d7dc3f413086d0b0036e_a1891f0b426477fb595747af3838feda001a693ee6c0644e"
source_file: "Thermoelectric_Phenomena_Materials_and_A.pdf.md"
original_path: "RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Thermoelectric_Phenomena_Materials_and_A.pdf.md"
extracted: "2026-09-27"
extract_method: "ima-mcp fetch_media_content"
extract_status: "ok"
clean_rules: "v2: dead-image-link->text(alt kept); repeat-digits->compressed"
processed: "2026-09-27"
---

# Thermoelectric_Phenomena_Materials_and_A.pdf.md

8
Annu. Rev. Mater. Res. 2011.41:433-448. Downloaded from www.annualreviews.org by Clemson University on 11/18/11. For personal use only.

# Thermoelectric Phenomena, Materials, and Applications

Terry M. Tritt

Department of Physics and Astronomy, Clemson University, Clemson, South Carolina
29634-0978; email: ttritt@clemson.edu

Annu. Rev. Mater. Res. 2011. 41:433–48

First published online as a Review in Advance on April 12, 2011

The Annual Review of Materials Research is online at matsci.annualreviews.org

This article's doi:
10.1146/annurev-matsci-062910-100453

Copyright © 2011 by Annual Reviews.
All rights reserved

1531-7331/11/0804-0433$20.00

## Keywords

thermoelectrics, thermopower, thermal conductivity, energy harvesting, power generation

## Abstract

Over the past 10-15 years, there have been significant advances in the scientific understanding as well as in the performance of thermoelectric (TE) materials. TE materials can be incorporated into power generation devices that are designed to convert waste heat into useful electrical energy. These TE materials can also be used in solid-state refrigeration devices for cooling applications. The conversion of waste heat into electrical energy will certainly play a role in our current challenge for alternative energy technologies to reduce our dependence on fossil fuels and to reduce greenhouse gas emissions. This article provides an overview of the various TE phenomena and discusses some of the primary TE materials that are currently being investigated. Several of the key parameters and terminology are defined and discussed along with an overview of some of the current and emerging technologies. The phonon glass-electron crystal approach to new TE materials for developing new materials is presented along with the role of solid-state crystal chemistry and the criteria for higher-performance TE materials. This article discusses TE phenomena, the selection criteria for higher-performance materials, and a few key materials.

Annu. Rev. Mater. Res. 2011.41:433-448. Downloaded from www.annualreviews.org by Clemson University on 11/18/11. For personal use only.

# 1. INTRODUCTION TO THERMOELECTRIC PHENOMENA AND APPLICATIONS

## 1.1. Background and Applications

Over the past 15 years or so, there has been a heightened interest in the field of thermoelectric (TE) materials research. Such interest has been driven by the need for more efficient materials and devices for electronic refrigeration and power generation. Various research groups are currently investigating a number of different systems of potential TE materials. These range from thin-film superlattice materials to large single-crystal or polycrystalline bulk materials and from semiconductors and semimetals to ceramic oxides. Several review articles written on the subject over the past few years capture much of the work done over the past decade or so [3–6; see also generally articles on the theme of "Harvesting Energy Through Thermoelectrics: Power Generation and Cooling" in the MRS Bulletin, Volume 31 (2006)]. Some of the research efforts focus on minimizing the lattice thermal conductivity, whereas other efforts focus on materials that exhibit high power factors, which are discussed below.

Proposed industrial and military applications of TE materials are generating increased activity in this field by demanding higher-performance, higher-temperature TE materials compared with those that are presently in use. The demand for alternative energy technologies to reduce our dependency on fossil fuels has led to various directions of research, including high-temperature energy harvesting via the direct recovery of waste heat and its conversion into useful electrical energy using TE devices. More recently, TEs have been investigated for their use in TE-solar hybrid systems to take advantage of the IR part of the solar spectrum and for TE-solar power generation (7). Thus, the development of higher-performance TE materials is becoming more important. Novel applications of TEs include aspects such as biothermal batteries to power heart pacemakers, enhanced performance of optoelectronics coupled with solid-state TE cooling, and power provision for deep-space probes via radioisotope TE generators. More recently, TE generators have been installed in automobiles to capture waste heat from exhaust and to transform it into useful electrical energy for automotive electrical systems and for increased fuel efficiency for use in next-generation vehicles. In addition, TE refrigeration applications include seat coolers for comfort and electronic component cooling. Of course, the deep-space applications of NASA's Voyager and Cassini missions using radioactive thermoelectric generators (RTGs) are well established (8).

TE refrigeration is an environmentally green method of small-scale, localized cooling in computers, infrared detectors, electronics and optoelectronics, and many other applications. However, most of the electronics and optoelectronics technologies typically require only small-scale or localized spot cooling of small components that do not impose a large heat load. If significant economical cooling can be achieved, the resulting cold computing could produce speed gains of 30% to 200% in some CMOS computer processors. Many researchers perceive cooling of the processors to be the fundamental limit to electronic system performance (9). Recent utilization of Peltier coolers in relation to refrigeration of biological specimens/samples is also an emerging TE application. Thus, the potential payoff for the development of low-temperature TE refrigeration devices, as well as for the development of high-temperature materials for waste heat recovery, is great. The requirement for compounds with high-performance properties optimized over wide temperature ranges has led to this much-expanded interest in new TE materials. The role of bulk materials applications and needs is demanding new breakthroughs in both materials engineering and device engineering, especially for automotive applications for cooling and power generation (8).

The development and potential of bulk materials for TE applications include high-temperature materials such as skutterudites, clathrates, half-Heusler alloys, and complex chalcogenides (10).

Annu. Rev. Mater. Res. 2011.41:433-448. Downloaded from www.annualreviews.org by Clemson University on 11/18/11. For personal use only.

Recently, ceramic oxide materials have also shown potential as high-temperature TE materials (11). The potential of nanomaterials and their role in TE research are emerging areas of interest (12). Another emerging area is one that utilizes materials termed TE nanocomposites, which incorporate nanomaterials that are then part of a matrix of a given TE material. These nanoparticles may be mixed into materials and solidified by some method such as hot pressing or spark plasma sintering. Such nanoparticles can also be nucleated within the material directly through either specific solid-state synthesis or more external methods such as high-energy ball milling or melt spinning (13–16). Thin-film properties, applications, and recent results are also very important (17).

A key factor in advancing many of these technologies is the development of higher-performance TE materials via either the emergence of completely new materials or a more ingenious materials engineering of some of the existing materials. Recent books and series provide a more complete overview of the state-of-the-art materials, a theoretical and experimental discussion of the basic principles, and an overview of some of the recent developments and materials (2, 18).

# 1.2. Seebeck and Peltier Effects

A discussion of TE effects and devices should start with one of the most fundamental phenomena, the Seebeck coefficient, or the thermopower (19, 20). In the early 1800s, Seebeck observed that if two dissimilar materials were joined together and the junctions were held at different temperatures ($T$ and $T + \Delta T$), then a voltage difference ($\Delta V$) that was proportional to the temperature difference ($\Delta T$) developed. The ratio of the voltage developed to the temperature difference ($\Delta V/\Delta T$) is related to an intrinsic property of the materials termed the Seebeck coefficient ($\alpha$), or the thermopower. This effect can be understood by establishing a temperature gradient across a material; the more energetic electrons migrate to a lower potential until an electric field is established to impede the further flow of electrons. This effect is illustrated in Figure 1, which shows the establishment of an electric field that is the opposite of that of the temperature gradient, $\bar{\nabla}T$, given that the sign of $\alpha_n$ is negative for electrons:

$$ \vec{E} = \alpha_n \vec{\nabla} T. \qquad 1. $$

The Seebeck coefficient is very low for metals (only a few microvolts per degree Kelvin) and is much higher for semiconductors (typically a few hundred microvolts per degree Kelvin) (21). A few years after Seebeck's observation, Peltier discovered a related effect (the Peltier effect). If an electrical current is passed through the junction of two dissimilar materials, heat is either absorbed or rejected at the junction, depending on the current's direction. This effect is due largely to the difference in the Fermi energies of the two materials. These two effects are related to each other, as shown in the definition of the Peltier coefficient, $\Pi = \alpha T$. The rate that the Peltier heat is liberated or rejected at the junction ($\dot{Q}_p$) is given by $\dot{Q}_p = \alpha IT$, where $I$ is the current through the junction and $T$ is the temperature in degrees Kelvin. Thermomagnetic effects such as the Hall, Ettingshausen, and Nernst effects are beyond the scope of this article (see Nolas et al. 18 for a more complete discussion of these effects).

# 1.3. Definition and Description of the Figure of Merit and Thermoelectric Performance

The potential of a material for TE applications is determined in large part by a measure of the material's dimensionless figure of merit,

$$ ZT = \frac{\alpha^2 \sigma T}{\kappa} = \frac{\alpha^2 T}{\rho \kappa}, \qquad 2. $$

Annu. Rev. Mater. Res. 2011.41:433-448. Downloaded from www.annualreviews.org by Clemson University on 11/18/11. For personal use only.

[图片: 、aTCb+++++XX++++++++++++E]
# Figure 1

A depiction of the thermoelectric effect when a material is subjected to an external temperature gradient and the system is in equilibrium. (a) The more energetic electrons have a longer mean free path. (b) These more energetic electrons (denoted by blue dots) then diffuse to the cold side until an electric field (E) is developed to oppose any further diffusion. We define $x$ as increasing from the cold-side temperature $T_C$ to the hot-side temperature $T_H$, therefore defining the temperature gradient $\vec{\nabla}T$ as shown. Because the electrons are negatively charged (and therefore $\alpha_n$ is negative), an electric field is established that is the opposite of that the temperature gradient to oppose further diffusion when the system is in equilibrium.

where $\alpha$ is the Seebeck coefficient, $\sigma$ the electrical conductivity, $\rho$ the electrical resistivity, and $\kappa$ the total thermal conductivity ($\kappa = \kappa_L + \kappa_E$, where $\kappa_L$ and $\kappa_E$ are the lattice and electronic contributions, respectively). The power factor, $\alpha^2\sigma T$ (or $\alpha^2T/\rho$), is typically optimized through doping in narrow-gap semiconducting materials as a function of carrier concentration (typically approximately $10^{19}$ carriers cm$^{-3}$) to give the highest ZT (18). High-mobility carriers are most desirable to have the highest electrical conductivity for a given carrier concentration. The ZT for a single material is somewhat meaningless because an array of TE couples is utilized in a device or module. There are two materials in a TE couple (shown in Figure 2): an n type and a p type (see, for example, http://www.marlow.com for a look at several TE module designs). If one ignores parasitic contributions that reduce device performance such as contact resistance and radiation effects, then the resulting ZT for the couple (based solely on the TE materials) is given by

$$ ZT = \frac{(\alpha_p - \alpha_n)^2 T}{[(\rho_n \kappa_n)^{1/2} + (\rho_p \kappa_p)^{1/2}]^2}. \quad 3. $$

The thermopower of $n$-type carriers ($\alpha_n$) is negative, and that of the holes ($\alpha_p$) is positive. The coefficient of performance ($\phi$) (refrigeration mode) and the TE efficiency ($\eta_{TE}$) (power generation mode) of the TE couple are directly related to the ZT, as shown in Equation 3 for the efficiency. The efficiency ($\eta_{TE}$) of the TE couple is given by the power input to the load ($W$) over the net

Annu. Rev. Mater. Res.2011.41:433-448. Downloaded from www.annualreviews.org by Clemson University on 11/18/11. For personal use only.

[图片: Active coolingHeat sourcennHeat sinkHeat rejectionRefrigeration modePower generation mode]
# Figure 2

A generic diagram of a thermoelectric couple made of $n$-type and $p$-type thermoelectric materials. Power generation or refrigeration modes are possible, depending on the configuration. Red denotes hotter temperatures, and blue denotes colder temperatures.

heat flow rate ($Q_H$), where $Q_H$ is positive for heat flow from the source to the sink:

$$ \eta_{TE} = \frac{W}{Q_H} = \frac{T_H - T_C}{T_H} \left( \frac{(1 + ZT_M)^{1/2} - 1}{(1 + ZT_M)^{1/2} + T_C / T_H} \right), \qquad 4. $$

where $T_H$ is the hot-side temperature, $T_C$ is the cold-side temperature, and $T_M$ is the average temperature. Thus, $\eta_{TE}$ is proportional to the Carnot efficiency ($\eta_C$):

$$ \eta_C = \frac{T_H - T_C}{T_H}, \qquad 5. $$

which we know from thermodynamics is the maximum efficiency of a heat engine operating between two temperatures, $T_H$ and $T_C$. Figure 3 shows the ratio of $\eta_{TE}$ and $\eta_C$ plotted as a function of ZT for a heat engine operating between the temperatures of $T_H = 800$ K and $T_C = 300$ K, which would yield a Carnot efficiency of 62%. This plot assumes that the devices are operating with no parasitic losses such as contact resistance or radiation effects and that ZT is constant between these two temperatures. Of course, these are not realistic assumptions, and the plot is used only as a gauge to ascertain where the greatest return in efficiency gain would be achieved per unit increase in ZT. The biggest return is for a ZT between 2 and 3, and in my opinion, the ultimate goal of TE materials research is ZT ≈ 2–3 in stable, bulk TE n-type and p-type materials with low parasitic losses that can operate between these two temperatures with high ZT values.

# 1.4. Thermoelectric Modules: Devices

The Peltier effect is the basis for many modern-day TE refrigeration devices, and the Seebeek effect is the basis for TE power generation devices. The versatility of TE materials is illustrated in Figure 2, which shows a diagram of a TE couple that is composed of $n$-type (negative thermopower and electron carriers) and $p$-type (positive thermopower and hole carriers) semiconductor materials connected through metallic electrical contact pads. Both refrigeration and power generation may be accomplished using the same module as shown in Figure 2. A TE module or device comprises an array of these couples, which are arranged electrically in series and thermally in parallel. TE energy conversion utilizes the Seebeek effect, wherein a temperature gradient is imposed across

Annu. Rev. Mater. Res. 2011.41:433-448. Downloaded from www.annualreviews.org by Clemson University on 11/18/11. For personal use only.

[图片: |ZT|ηTE/ηC| |:---:|:---:| |0|0| |1|0.28| |2|0.4| |3|0.49| |4|0.54|]
# Figure 3

The ratio of thermoelectric efficiency to the Carnot efficiency ($\eta_{TE}/\eta_C$) as a function of the figure of merit, ZT. The maximum efficiency or Carnot efficiency is given by $\eta_C = (T_H - T_C)/T_H = (800 \text{ K} - 300 \text{ K})/800 \text{ K} = 63\%$, where $T_H$ is the hot-side temperature and $T_C$ is the cold-side temperature. This plot assumes no parasitic losses such as contact resistance or radiation effects and that ZT is essentially constant between these two temperatures. Red denotes hotter temperatures, and blue denotes colder temperatures.

the device, resulting in a voltage that can be used to drive a current through a load resistance or device. This process reflects the direct conversion of heat into electricity. Conversely, Peltier heat is generated when an electric current is passed through a TE material to provide a temperature gradient (with heat being absorbed on the cold side), is transferred through (or pumped by) the charge carriers in the TE materials, and is then rejected at the heat sink, thus providing refrigeration capability. The advantages of TE solid-state energy conversion are compactness, quietness (no moving parts), and localized heating or cooling. In addition, energy in the form of waste heat (0% efficiency) that would be normally lost may be converted into useful electrical energy (with 7–8%-and-greater efficiency) using a TE power generation device.

The best TE materials that are currently used in devices have a value of $ZT \approx 1$. Previous to the mid-1990s, this value had been a practical upper limit for more than 30 years, yet there were no theoretical or thermodynamic reasons for $ZT \approx 1$ as an upper barrier. As is apparent from Equation 2, the $ZT$ may be increased either by decreasing $\kappa_L$ or by increasing either $\alpha$ or $\sigma$, where $\alpha^2\sigma T$ is defined as the power factor, which is related primarily to the electronic properties. However, $\sigma$ is tied to $\kappa_E$ through the Wiedemann-Franz relationship, and the ratio of $\kappa_E/\sigma$ is essentially constant at a given temperature for the majority of TE materials.

$$ \kappa_E = L_0 \sigma T. \qquad 6. $$

The value of the Lorenz number ($L_0$) is $L_0 = 2.48 \times 10^{-8} \text{ V}^2 \text{ K}^{-2}$ for metals and is usually taken as $L = 2.0 \times 10^{-8} \text{ V}^2 \text{ K}^{-2}$ for degenerate, i.e., highly doped, semiconductors. Some of the goals of current research efforts are to find new materials that either increase the current efficiency of TE devices (e.g., increase ZT) or have the capability of operating in new and broader temperature regimes, especially at lower temperatures ($T < 250$ K) and at higher temperatures ($T > 400$ K). Over the past 30 years, alloys based on the Bi$_2$Te$_3$ system [($\text{Bi}_{1-x}\text{Sb}_x$)$_2$($\text{Te}_{1-x}\text{Se}_x$)$_3$] as well as on

Annu. Rev. Mater. Res. 2011.41:433-448. Downloaded from www.annualreviews.org by Clemson University on 11/18/11. For personal use only.

[图片: |材料|年份|(ZT)max| |:---:|:---:|:---:| |Bi2Te3 alloys|1960|1.0| |PbTe|1965|0.6| |n-SiGe|1970|1.0| |Filled skutterudites (RECoSb3)|1995|1.3| |Zn4Sb3|2000|1.2| |CsBi4Te3|2005|0.8| |LAST-AgPb18SbTe20|2005|2.2| |PbTe-QDSL|2000|1.7| |Bi2Te3-Sb2Te3-SL|2005|2.5| |Nano-p-Bi2Te3 and Pb0.98Tl0.02Te|2010|1.5|]
# Figure 4

The figure of merit, ZT, as a function of the time frame of several key TE materials relative to their discovery year, thus showing many of the recent advancements in both thin-film and bulk thermoelectric materials. Abbreviations: LAST, PbAgSbTe compounds; QDSL, quantum dot superlattice; SL, superlattice.

the Si₁-yGe, system have been extensively studied and optimized for their use as TE materials to perform a variety of solid-state TE refrigeration and power generation applications (22, 23). These traditional TE materials have undergone extensive investigation, and only a few years ago there appeared to be little room for future improvement in these common bulk structures. However, recent results on nanostructures of traditional TE materials have shown a promising new direction for these materials. In addition, entirely new classes of compounds have been recently investigated. Figure 4 shows the ZT values of the Bi₂Te₃ and Si₁-yGe, materials and their more recent nanocomposite forms in the year they were discovered, as well as the ZT values of many of the more recent bulk and thin-film materials that have been developed over the past several years.

# 1.5. Transport Properties

The thermopower or Seebeck coefficient ($\alpha$) can be thought of as the heat per carrier over temperature or more simply the entropy per carrier, $\alpha \approx C/q$, where $C$ is the specific heat and $q$ is the charge of the carrier (20). In the case of a classical gas, each particle has an energy of $E = \frac{3}{2}k_B T$, where $k_B$, the Boltzmann constant, is $1.38 \times 10^{-23} \text{ J K}^{-1}$. The thermopower of a classical electron gas is then approximately $k_B/e \approx 87 \ \mu\text{V K}^{-1}$, where $e$ is the absolute value of the charge of the electron. For metals, the heat per carrier is essentially a product of the electronic specific heat and the temperature divided by the number of carriers ($N$), and then

$$ \alpha \approx \frac{C_{el}}{q} \approx \left(\frac{k_B}{e}\right) \frac{k_B T}{E_F}, \quad 7. $$

where $E_F$ is the Fermi energy (related to the chemical potential of the material). Only that fraction of the electrons ($k_B T / E_F$) participate in the conduction process and thus also contribute to the thermopower of a metal. At $T \approx 0$, all states above the Fermi energy are vacant, and all the states below the Fermi energy are occupied. The quantity $k_B/e \approx 87 \mu\text{V K}^{-1}$ is a constant and represents the thermopower of a classical electron gas. Metals have thermopower values that are much lower than $87 \mu\text{V K}^{-1}$ (on the order of $1-10 \mu\text{V K}^{-1}$) and that decrease with decreasing temperature, i.e., $E_F \gg k_B T$. The Mott equation describes the behavior of metals as a function of temperature

Annu. Rev. Mater. Res. 2011.41:433-448. Downloaded from www.annualreviews.org by Clemson University on 11/18/11. For personal use only.

and is the diffusion thermopower.

$$ \alpha_D = \frac{\pi^2 k_B^2 T}{3e} \left[ \frac{1}{\sigma(E)} \frac{d\sigma}{dE} \right]_{E=E_F} . \quad 8. $$

In a semiconductor a charged particle must first be excited across an energy gap $E_G$. In this case the thermopower is approximated by

$$ \alpha \approx \frac{C_{el}}{q} \approx \left(\frac{k_B}{e}\right) \frac{E_G}{k_B T}. \qquad 9. $$

Thus, the thermopower is much higher than the characteristic value $k_B/e \approx 87 \ \mu\text{V K}^{-1}$ and increases with decreasing temperature. Semiconductors can exhibit either electron conduction (negative thermopower) or hole conduction (positive thermopower). The thermopower for different carrier types is given by a weighted average of their electrical conductivity values ($\sigma_e$ and $\sigma_p$),

$$ \alpha \approx \frac{(\alpha_e \sigma_e + \alpha_p \sigma_p)}{(\sigma_e + \sigma_p)}. \qquad 10. $$

It is necessary to dope the semiconductors with either donor or acceptor states to allow extrinsic conduction of the appropriate carrier type, electrons or holes, respectively. The overall objective is to have either a predominantly n-type material or a predominantly p-type material. The total thermopower will be lower than that of either of the individual contributions unless the direct band gap is large enough (typically on the order of $10 k_B T_0$, where $T_0$ is the operating temperature of the material) to effectively minimize minority carrier contributions. Typical values of the thermopower that are needed for good TE performance are on the order of $150-250 \mu V K^{-1}$ or greater.

For high-temperature applications, the contribution of minority carriers should be minimized to maintain a high thermopower value. In addition, the thermal stability of the materials is an essential aspect. Atomic diffusion within the materials and interdiffusion of contacts can seriously deteriorate the properties of a given material at high temperatures. Aspects of this are discussed elsewhere (2, 18). These materials and devices are expected to operate at elevated temperatures for long periods of time without deterioration of the materials' properties or the devices' performance. Diffusion and thermal annealing are important effects to thoroughly investigate and understand in any set of materials.

Electrical conductivity of metals and semiconductors has been discussed extensively in many texts on solid-state physics. Many carriers and states, typically $n \approx 10^{22}$ carriers cm $^{-3}$, are available for conduction in metals. The electrical conductivity is then very high for metals, on the order of $10^6 (\Omega \cdot \text{cm})^{-1}$. Again for semiconductors, the carriers must be thermally excited across a gap for conduction to occur, as shown from the activated behavior that is derived for the temperature dependency of electrical conductivity:

$$ \sigma \approx \sigma_0 \exp \left[ - \frac{E_G}{2k_B T} \right]. \qquad 11. $$

Here, $\sigma = n e \mu$. The carrier concentration typically dominates the conductivity, but the mobility $\mu$ and the temperature dependency of the mobility are also very important in relation to the behavior of electrical conductivity. Many textbooks on solid-state and semiconductor physics describe this behavior well. Thus, the two primary ways to achieve high conductivity in a semiconductor are either by having a very small gap to excite across $E_G \ll 10 K_B T$ or by having very high mobility carriers. Typical values of the electrical conductivity of a good TE material are on the order of approximately $10^3 (\Omega \cdot \text{cm})^{-1}$.

The thermal conductivity, $\kappa$, is related to the transfer of heat through a material by electrons and by phonons (quantized vibrations of the lattice) such that $\kappa = \kappa_L + \kappa_E$. The electrical and

Annu. Rev. Mater. Res. 2011.41:433-448. Downloaded from www.annualreviews.org by Clemson University on 11/18/11. For personal use only.

thermal conductivities $\sigma$ and $\kappa$ are interrelated: $\sigma$ is tied to $\kappa_E$ through the Wiedemann-Franz relationship given in Equation 6, and $\kappa_E = L_0\sigma T$. The lattice thermal conductivity is discussed below under Section 2.2. Typical values of thermal conductivity for a good TE material are $\kappa < 2$ W m$^{-1}$ K$^{-1}$, and typically $\kappa_L \approx \kappa_E$.

# 2. INVESTIGATING NEW THERMOELECTRIC MATERIALS

## 2.1. The Phonon Glass-Electron Crystal Approach

Several years ago Slack (24) described the chemical characteristics of materials that might prove to be candidates for a good TE material; namely, the candidate materials should be narrow-band-gap semiconductors with high-mobility carriers. Mahan and colleagues (25, 26) also described characteristics of good TE materials. The candidate material is typically a narrow-band-gap semiconductor (e.g., $E_G \approx 10 k_BT_0$ or $\approx 0.25 \text{ eV}$ at 300 K). Also, the mobility of the carriers must remain high ($\mu \approx 2,000 \text{ cm}^2$ ($V \cdot \text{s})^{-1}$), whereas the lattice thermal conductivity must be minimized. In semiconductors, the Seebeck coefficient and the electrical conductivity (both in the numerator of ZT) are strong functions of the doping level and chemical composition. Therefore, these quantities must be optimized by band gap engineering for good TE performance. The thermal conductivity of complex materials can often be modified by chemical substitutions, and the lattice thermal conductivity needs to be as low as possible. Understanding these various effects and selecting optimization strategies can be exceedingly difficult problems because in complex materials there are often many possible degrees of freedom. Slack suggested that the best TE material would behave as a phonon glass-electron crystal (PGEC) material; that is, it would have the electrical properties of a crystalline material and the thermal properties of an amorphous or glass-like material. Therefore, a material's engineering or designer materials approach must be pursued either to improve more established materials or to discover completely new classes of materials to investigate.

## 2.2. Minimum Thermal Conductivity

In many areas of research related to new TE materials, attempts are being made to reduce the lattice part of the thermal conductivity to essentially its minimum value, at which minimum lattice thermal conductivity is achieved (that is, when all the phonons have a mean free path that is essentially equal to the interatomic spacing of the constituent atoms). Such attempts involve scattering phonons in different frequency ranges through a variety of methods such as mass fluctuation scattering in a mixed crystal of ternary and quaternary compounds, rattling scattering, grain boundary scattering due to grain size, and interface scattering in thin films or multilayer systems. In addition, the advent of TE nanocomposites has proven to be a very viable approach in lowering the lattice thermal conductivity (3–7).

The lattice thermal conductivity is given by

$$ \kappa_L = \frac{1}{3} v_S C_V L_{pb}, \qquad 12. $$

where $v_s$ is the velocity of sound, $C_V$ is the heat capacity at constant volume, and $L_{pb}$ is the mean free path of the phonons. At high temperatures ($T > \approx 300$ K), the sound velocity and the heat capacity are essentially temperature independent in typical materials. Therefore, the magnitude and the temperature dependency of $\kappa_L$ are determined basically by the mean free path of the phonons at higher temperatures, $T > \theta_D$ (where $\theta_D$ is the Debye temperature). Slack (27) defined

Annu. Rev. Mater. Res. 2011.41:433-448. Downloaded from www.annualreviews.org by Clemson University on 11/18/11. For personal use only.

the minimum thermal conductivity ($\kappa_{min}$) as the thermal conductivity when the mean free path is limited essentially by the interatomic distance between the atoms within the crystal. A typical analysis of $\kappa_{min}$ results in values of $\kappa_{min} \approx 0.25-0.5$ W m $^{-1}$ K $^{-1}$ (25, 27).

# 2.3. Minimum Thermopower

There are certain practical limits for each of the parameters used to calculate ZT. These practical limits must be possible to achieve a material viable for TE applications. For example, in Bi₂Te, to achieve a ZT ≈ 1 at T = 320 K, σ ≈ 1 mΩ-cm, α ≈ 225 µV K $^{-1}$, and α ≈ 1.5 W m $^{-1}$ K $^{-1}$. I discuss above the ZT barrier, which in effect is given by minimizing the thermal conductivity. It is practical to investigate materials in which the electronic and lattice terms are comparable, on the order of 0.75 to 1 W m $^{-1}$ K $^{-1}$. Let us look at the hypothetical situation of a material in which the lattice thermal conductivity is zero (κL = 0). We also assume the scattering in this system is elastic and that the Wiedemann-Franz relationship, slightly rearranged (κE/σ = L₀T), is well behaved in this material. Then we can rewrite Equation 1 as ZT = α $^{2}$T/ρκE = α $^{2}$/L₀. Therefore, to be a viable TE material, a material must possess a minimum thermopower that is directly related to the values of ZT and L₀. Given this description, to achieve a certain value of ZT, the material would require that α = (L₀) $^{0.5}$ = 157 µV K $^{-1}$ for ZT = 1 and α = (2L₀) $^{0.5}$ = 225 µV K $^{-1}$ for ZT = 2. Of course, any real material will possess a finite κL, so these thermopower values will have to be higher to achieve the projected ZT values!

# 3. DESIGNER MATERIALS APPROACHES TO ADVANCED THERMOELECTRIC MATERIALS

TE materials research has always been a materials design problem involving intricate tuning of structure/property relationships in complex solids through principles of solid-state chemistry materials science and solid-state physics. The discussion thus far indicates that new materials must be able to eventually achieve certain minimum values of important parameters to be considered as a potential TE material. Whether a material has a $\kappa_L \approx \kappa_{\min}$ does not matter. If a material cannot be tuned or doped to attain a minimum thermopower (150 µV K $^{-1}$), then it cannot achieve ZT $\approx 1$.

# 3.1. The Classical Approach: Bulk Binary Semiconductors

Within the framework of the simple electronic band structure of solids, in general metals are poor TE materials. Hence, most of the early TE work emphasized semiconductors (28). As stated above, to have a maximum ratio of electrical to thermal conductivity, the material should have relatively few carriers ($\approx 10^{19} \text{ cm}^{-3}$) with very high mobilities. Crystal structure and bonding strongly influence mobility. Materials with either diamond or zinc blend structures with a high degree of covalent bonding frequently have high mobilities (e.g., Si, Ge, or InSb) and high thermal conductivity values. In contrast, low lattice thermal conductivities are found in conjunction with low Debye temperatures and high anharmonic lattice vibrations. These conditions are best satisfied by highly covalent intermetallic compounds and alloys of the heavy elements such as (Pb, Hg, Bi, Tl, or Sb) and (S, Se, or Te). Once a material system has been selected with a favorable electrical-to-thermal-conductivity ratio, one optimizes the composition to further enhance the ZT by doping the material to maximize the density of states at the Fermi level and hence the high Seebeck coefficients.

The most-studied TE materials are probably Bi₂Te₃ alloys that crystallize in a layered structure with rhombohedral-hexagonal symmetry with a space group R3m (D₅₃d). The hexagonal unit cell

Annu. Rev. Mater. Res. 2011.41:433-448. Downloaded from www.annualreviews.org by Clemson University on 11/18/11. For personal use only.

dimensions at room temperature are $a = 3.8$ Å and $c = 30.5$ Å. The layers are stacked along the $c$ axis in the following sequence:

... Te – Bi – Te – Bi – Te... Te – Bi – Te – Bi – Te...

The Bi and Te layers are held together by strong covalent bonds, whereas the adjacent Te layers exhibit van der Waals bonding. This weak binding between the Te layers accounts for the ease of cleavage along the plane perpendicular to the c axis and the anisotropic thermal and electrical transport properties of Bi₂Te₃. For example, the thermal conductivity along the plane perpendicular to the c axis (1.5 W m⁻$^{1}$ K⁻$^{1}$) is nearly twice that of the value along the c-axis direction (0.7 W m⁻$^{1}$ K⁻$^{1}$). When grown from a melt or by zone refining, Bi₂Te₃ crystals are always non-stoichiometric and show p-type behavior. In contrast, n-type materials can be grown from melt containing excess Te, I, or Br. The thermal conductivity values of both p-type and n-type Bi₂Te₃ are ~1.9 W m⁻$^{1}$ K⁻$^{1}$, giving a ZT of ~0.6 near room temperature. Ioffe (21) suggested that alloying could further reduce the lattice thermal conductivity of Bi₂Te₃ through the scattering of short-wavelength acoustic phonons. The optimum compositions for TE cooling devices are normally Bi₂Te₃.₂.₅.₆.₀.₅ (for n type) and Bi₀.₅Sb₁.₅.₆.₃ (for p type) with ZT ≈ 1 near room temperature. As stated above, the incorporation of in situ nanostructures that are nucleated by either high-energy ball milling or melt spinning in these materials has proven beneficial in reducing the lattice thermal conductivity and in achieving ZT ≈ 1.4 between 300 K and 400 K (14–16).

In contrast to Bi₂Te₃, PbTe crystallizes in a cubic NaCl-type crystal structure, and the TE properties are isotropic. Both p-type and n-type thermoelements can be produced by doping of acceptors (e.g., Na₂Te or K₂Te) or donors (PbI₂, PbBr₂, or Ge₂Te₃). In analogy to Bi₂Te₃, solid-solution compositions (e.g., PbTe-SnTe) have been made to lower the lattice thermal conductivity (29). The ZT value is low near room temperature but increases to ZT ≈ 0.7 at 700 K, making this a prime candidate for power generation in the higher-temperature range. High ZT values (ZT ≈ 1.5) were recently achieved in Tl-doped PbTe materials by using the concept of energy filtering to enhance ZT. Such values can be achieved by inducing a large variation in the density of states near the Fermi level, thus significantly enhancing the thermopower (30). This energy-filtering effect can be understood through a modified Mott diffusion equation for the thermopower by manipulating the chemical potential term with an addition of only 2% Tl.

$$ \alpha = \frac{\pi^2 k_B^2 T}{3e} \left[ \frac{1}{n} \frac{dn(E)}{dE} + \frac{1}{\mu} \frac{d\mu(E)}{dE} \right]_{E=E_F}. \quad 13. $$

It is possible to achieve ZT in excess of unity at 700 K in a structurally related solid-solution composition, AgSbTe₂ (80%)–GeTe (20%) (termed TAGS, which denotes alloys containing Te, Ag, Ge, and Sb). However, due to high-temperature stability issues, these compositions are not currently favored in TE devices.

Neither Si nor Ge is a good TE material because both have a very high lattice thermal conductivity (150 W m $^{-1}$ K $^{-1}$ and 63 W m $^{-1}$ K $^{-1}$ for Si and Ge, respectively). However, the lattice thermal conductivity can be substantially reduced by alloy formation between the two elements. The best alloy composition is Si₀.₇Ge₀.₃, which possesses a thermal conductivity that is ~10 W m $^{-1}$ K $^{-1}$, and the reduction is apparently due to increased phonon-phonon and phonon-electron scattering (18). Remarkably, such a large reduction does not unduly reduce the carrier mobility, and ZT ≈ 0.6–0.7 can be realized at elevated temperatures. Due to their exceptional stability at high temperature (~1,200 K), these alloys are of interest to NASA for use in RTGs in deep-space probes. Nano-structuring in these materials has also led to a further reduction in the lattice thermal conductivity and to higher ZT values; such nanostructures are stable at high temperatures (31).

Annu. Rev. Mater. Res. 2011.41:433-448. Downloaded from www.annualreviews.org by Clemson University on 11/18/11. For personal use only.

# 3.2. Complex Inorganic Structures

Most of the above-mentioned investigations focused on binary intermetallic semiconductor systems. Recent approaches to high-performance bulk TE materials focus on ternary and quaternary chalcogenides containing heavy atoms with low-dimensional or isotropic complex structures to take advantage of the high carrier effective masses and low lattice thermal conductivities associated with such systems (32). Along these lines, CsBi₄Te₆ possessing a layered structure has been identified as a material showing a ZT of 0.8 at 225 K; this ZT value is 40% greater than that of the Bi₂-xSbₓTe₃-ySe₇ alloys (33). Other potential low-temperature TE materials currently under investigation are low-dimensional semiconducting or semimetallic doped layered pentatellurides (e.g., ZrTe₅ and HfTe₅) (34). These compounds have a structure similar to that of Bi₂Te₃, with a van der Waals gap between the individual layers. Although doped pentatellurides exhibit very high power factors (exceeding the optimally doped Bi₂Te₃ solid solutions) in the low-temperature range (<250 K), the thermal conductivity is relatively high (κ ≈ 4–8 W m $^{-1}$ K $^{-1}$). These materials need to be compositionally tuned further to be useful TEs.

Cubic quaternary compounds with a complex formula $Ag_nPb_mM_nTe_{m+2n}$ ($M = Sb, Bi$) and that crystallize in a PbTe structure were recently reported (35). The composition $AgPb_{10}SbTe_{12}$ shows exceptionally high ZT values (>2) at elevated temperatures (shown in Figure 4). Such values are due to the very low total thermal conductivity of the bulk materials, which possibly arises from compositional modulations (seen as a nanodot) similar to the kinds of nanostructures that are found in superlattices. These materials have ZT values of >1.7.

Another group of materials under investigation is half-Heusler alloys with a general formula $MNiSn$, where $M = Zr$, Hf, Ti. A complex composition of the type $Zr_{0.5}Hf_{0.5}Ni_{0.5}Pd_{0.5}Sn_{0.99}Sb_{0.01}$ shows a ZT of 0.7 at $T \approx 800$ K, highlighting the intricate balance in structure/composition/property relationships in these compounds (36). The $\beta-Zn_4Sb_3$ system has been reinvestigated for TE power generation applications at the Jet Propulsion Laboratory (37).

# 3.3. Crystal Structures with Rattlers

The method of lowering the lattice thermal conductivity through a mixed-crystal or solid-solution formation does not always produce enough phonon scattering to lower the lattice thermal conductivity to $\kappa_{\min}$. Slack's PGEC concept, described above, avoids this limitation. The concept of $\kappa_{\min}$ is successfully verified in crystal structures with large empty cages or voids, where atoms can be partially or completely filled in such a way that they rattle, resulting in the scattering of the acoustic phonons. This approach works especially well in highly covalent semiconductor materials based on clathrates (Si, Ge, or Sn) and void structures formed by heavy elements of low electrone-gativity differences, e.g., CoSb₃-based skutterudites. Some doped skutterudites show exceptionally high ZT values at elevated temperatures (ZT ≈ 1.2 at 600–800 K). More recently, multiple filler atoms (e.g., Ce, Yb, and Ba) and In doping along with nanostructuring have resulted in significant improvements in these materials (38–41).

# 3.4. Oxide Thermoelectrics

Numerous oxides with metal atoms in their common oxidation states are stable at elevated temperatures and show electrical properties ranging from insulating to superconducting. Nevertheless, oxides have received very little attention for TE applications because of their strong ionic character: They have narrow conduction bandwidths arising from weak orbital overlap, which leads

Annu. Rev. Mater. Res. 2011.41:433-448. Downloaded from www.annualreviews.org by Clemson University on 11/18/11. For personal use only.

to localized electrons with low carrier mobilities. This situation changed with the unexpected discovery of good TE properties in a strongly correlated layered oxide, $NaCO_2O_4$ (42). This oxide attains $ZT \approx 0.7-0.8$ at 1,000 K. Inspired by the striking TE performance of $NaCO_2O_4$, most of the current research is currently focused on Co-based layered oxides such as $Ca_3CO_4O_9$ and $Bi_2Sr_3Co_2O_3$ that crystallize in misfit layered structures (24). Among the n-type oxides, Al-doped ZnO ($Al_{0.02}Zn_{0.98}O$) exhibits reasonably good TE performance ($ZT \approx 0.3$ at 1,000 K) (43).

# 3.5. Thin-Film and Superlattice Materials

The approaches in bulk materials research rely heavily on the thermodynamic stability of phases at a given condition, whereas thin-film deposition can yield metastable designer phases with novel properties. Quantum well (0-D, 1-D, and 2-D) systems take advantage of a low-dimensional character through physical confinements in quantum dots, nanowires, and thin-film structures to enhance the electronic properties of a given material (44). In addition, nanostructured semiconductor materials may scatter mid- to long-wavelength phonons and thereby reduce the lattice thermal conductivity to $\kappa_{\min}$. Researchers at the Research Triangle Institute have demonstrated a significant enhancement in ZT through the construction of $\text{Bi}_2\text{Te}_3/\text{Sb}_2\text{Te}_3$ superlattices (17, 45). These materials exhibit $ZT \approx 2.4$. The enhancement is attributed to creating a nanoengineered material that is efficient in thermal insulation while remaining a good electrical conductor. The thermal insulation arises from a complex localization-like behavior for phonons, whereas electron transmission is facilitated by the optimal choice of band offsets in these semiconductor heterostructures. Also, there have been reports on PbTe/PbTeSe quantum dot structures that yield $ZT \sim 1.3-1.6$ (46). These materials have been grown as thick films. Such films have been floated off the substrate to yield freestanding films, which were measured to yield these results.

# 4. CONCLUSIONS

Currently, there are no theoretical or thermodynamic limits to the possible values of ZT. The current need for alternative energy technologies and materials to replace the depleting supplies of fossil fuels is becoming more urgent. Energy-related research will grow rapidly over the next few years, and higher-performance TE materials and devices are directly needed. Slack (24) estimated that an optimized PGEC material could exhibit values of ZT ≈ 4. Such projections give encouragement that such materials may be possible. However, as is evident from Figure 3, if we could find TE materials with ZT ≈ 2–3 and that were stable over a broad temperature range with low parasitic losses, then the problem would be almost entirely solved. Thus, a systematic search and subsequent thorough investigation of promising materials may eventually yield these much-needed materials for next-generation TE devices. Although many strategies are being employed in hopes of identifying the next generation of TE materials, the PGEC approach appears to be the best, especially for bulk materials. One has to decide whether holey semiconductors (materials with cages such as skutterudites or clathrates) or unholey semiconductors such as SiGe or PbTe are the best to pursue and which tuning parameters are available to improve these materials (47). To date, none of the new materials have displaced the current state-of-the-art materials (Bi₂Te, PbTe, and SiGe) in a commercial TE device. These materials have held that distinction for more than 30 years. Nanostructuring and in situ growth of stable nanostructures, thus yielding TE nanocomposites, have further improved the TE properties of these materials. Although the thin-film results are very exciting, they may be most appropriate for small-scale electronic and optoelectronics applications in which small heat loads or low levels of power generation are more appropriate. To address large-scale refrigeration (home refrigerators) or power generation

Annu. Rev. Mater. Res. 2011.41:433-448. Downloaded from www.annualreviews.org by Clemson University on 11/18/11. For personal use only.

(automotive or industrial applications) requirements, higher-performance bulk materials will have to be developed. Theoretical guidance in terms of band structure calculations and modeling will be essential to identify the most promising TE materials. In addition, rapid yet accurate characterization of materials and verification of results are also necessary to effectively advance this field of research. A multidisciplinary approach will be required to develop higher-efficiency TE materials and devices. The techniques used to develop designer materials for thermoelectrics will most likely prove important in other areas of materials research.

# SUMMARY POINTS

1. Thermoelectric materials can be incorporated into devices that can be used for solid-state refrigeration or power generation.

2. The interrelationship of the properties of these materials makes it very difficult to find materials that can achieve high ZT values, i.e., $ZT > 1$.

3. The broad range of properties that must be investigated in the search for high-efficiency thermoelectric materials make them some of the most interesting materials to study. One must appreciate the intricate role of both electrons and phonons in a given material and further understand how to manipulate their properties in a favorable manner to achieve a high ZT, i.e., designer or phonon glass-electron crystal (PGEC) materials.

4. In the past the low efficiency (<10%) of current materials has limited them to mainly niche applications.

5. However, over the past 10 years there has been significant improvement in several thermoelectric materials, and these are opening up new markets.

6. Several automotive applications are beginning to use thermoelectric materials either for climate-controlled cooling in automotive cabins or for waste heat recovery from automobile exhaust systems.

7. Slack's (24) PGEC methodology and the advent of TE nanocomposites hold promising potential for achieving materials that possess ZT values of the order of 2–3 and that are thermally stable over the range of temperatures in which they are to be used.

8. Future world energy demands will certainly make us look at all types of alternative energy sources as opposed to fossil fuels. Hopefully, thermoelectric materials and devices can play a small but contributing role in meeting those demands.

# DISCLOSURE STATEMENT

The author is not aware of any affiliations, memberships, funding, or financial holdings that might be perceived as affecting the objectivity of this review.

# LITERATURE CITED

1. Tritt TM, ed. 2000. Recent Trends in Thermoelectric Materials Research, Vol. 71: Semiconductors and Semimetals. New York: Academic

2. Kanatzidis MG. 2010. Nanostructured thermoelectrics, the new paradigm. Chem. Mater. 22(3):648–59

3. Heremans J. 2009. Nanometer-scale thermoelectric materials. In Springer Handbook on Nanotechnology. Part A. Nanostructures, Micro/Nanofabrication and Materials, ed. B Bhushan, pp. 345-73. Heidelberg: Springer. 2nd ed.

Annu. Rev. Mater. Res. 2011.41:433-448. Downloaded from www.annualreviews.org by Clemson University on 11/18/11. For personal use only.

4. Dresselhaus MS, Chen G, Tang MY, Yang R, Lee H, et al. 2007. New directions for low-dimensional thermoelectric materials. Adv. Mater. 19:1043–53

5. Lan Y, Minnich AJ, Chen G, Ren Z. 2010. Enhancement of thermoelectric figure-of-merit by a bulk nanostructuring approach. Adv. Funct. Mater. 20:357–76

6. He J, Tritt TM. 2010. Thermal-to-electrical energy conversion from the nanotechnology perspective. In Nanotechnology for the Energy Challenge, ed. Javier Garcia Martinez, pp. 47–77. Weinheim, Ger.: Wiley-VCH

7. Tritt TM, Bottner H, Chen LD. 2008. Thermoelectrics: direct solar thermal energy conversion. MRS Bull. 33:366-68

8. Yang J, Caillat T. 2006. Thermoelectric materials for space and automotive power generation. MRS Bull. 31:224–29

9. Allen AW. 1997. Thermoelectrically cooled IR detectors beat the heat. Laser Focus World 33:S15

10. Nolas GS, Poon SJ, Kanatzidis M. 2006. Recent developments in bulk thermoelectric materials. MRS Bull. 31:99–205

11. Koumoto K, Terasaki I, Funahashi R. 2006. Complex oxide materials for potential thermoelectric applications. MRS Bull. 31:206–210

12. Rao A, Ji X, Tritt TM. 2006. Properties of nanostructured one-dimensional and composite thermoelectric materials. MRS Bull. 31:218–23

13. Sootsman JR, Chung DY, Kanatzidis MG. 2009. New and old concepts in thermoelectric materials. Angew. Chem. Int. Ed. 48:8616–39

14. Xie W, Tang X, Yan Y, Zhang Q, Tritt TM. 2009. Unique low-dimensional structure and enhanced thermoelectric performance for $p$-type $Bi_{0.52}Sb_{1.48}Te_3$ bulk material. Appl. Phys. Lett. 94:102111

15. Poudel B, Hao Q, Ma Y, Lan Y, Minnich A, et al.2008. High-thermoelectric performance of nanostructured bismuth antimony telluride bulk alloys. Science 320:634–38

16. Xie W, He J, Kang HJ, Tang X, Zhu S, et al. 2010. Identification of the specific nanostructures responsible for the high thermoelectric performance of (Bi,Sb)$_{2}$Te$_{3}$ nanocomposite. Nano Lett. 10(9):3283–89

17. Boettner H, Chen G, Venkatasubramanian R. 2006. Aspects of thin-film superlattice thermoelectric materials, devices, and applications. MRS Bull. 31:211–17

18. Nolas GS, Sharp J, Goldsmid HJ. 2001. Thermoelectrics: Basic Principles and New Materials Developments. New York: Springer

19. Morelli DT. 1997. Thermoelectric devices. Encycl. Appl. Phys. 21:339–54

20. Chaiken PM. 1990. An introduction to thermopower for those who might want to use it to study organic conductors and superconductors. In Organic Superconductors, ed. VZ Kresin, WA Little, pp. 101–15. New York: Plenum

21. Ioffe AF. 1957. Semiconductor Thermoelements and Thermoelectric Cooling. London: Infosearch

22. Goldsmid HJ. 1986. Electronic Refrigeration. London: Pion

23. Rowe DM, ed. 1995. CRC Handbook of Thermoelectrics. Boca Raton, FL: CRC

24. Slack GA. 1995. New materials and performance limits for thermoelectric cooling. See Reference 23, pp. 407-40

25. Mahan GD, Sofo JO. 1996. The best thermoelectric. Proc. Natl. Acad. Sci. USA 93:7436-39

26. Mahan GD, Sales B, Sharp J. 1997. Thermoelectric materials: new approaches to an old problem. Phys. Today 50(3):42–47

27. Slack GA. 1979. The thermal conductivity of non-metallic crystals. In Solid State Physics, Vol. 34, ed. F Seitz, D Turnbull, H Ehrenreich, pp. 1–71. New York: Academic

28. Heikes RR, Ure RW Jr. 1961. Thermoelectricity: Science and Engineering. New York: Intersci.

29. Wood C. 1988. Materials for thermoelectric energy conversion. Rep. Prog. Phys. 51:459-539

30. Heremans JP, Jovovic V, Toberer ES, Saramat A, Kurosaki K, et al. 2008. Enhancement of thermoelectric efficiency in PbTe by distortion of the electronic density of states. Science 321:554–57

31. Joshi G, Lee H, Lan Y, Wang X, Zhu G, et al. 2008. Enhanced thermoelectric figure-of-merit in nanostructured p-type silicon germanium bulk alloys. Nano Lett. 8(12):4670-74

32. Kanatzidis MG, Mahanti SD, Hogan TP, eds. 2003. Chemistry, Physics and Materials Science of Thermoelectric Materials: Beyond Bismuth Telluride. New York: Plenum

Annu. Rev. Mater. Res. 2011.41:433-448. Downloaded from www.annualreviews.org by Clemson University on 11/18/11. For personal use only.

33. Chung DY, Hogan T, Brazis P, Rocci-Lane M, Kannewurf C, et al. 2000. CsBi₄Te₆: a high-performance thermoelectric material for low-temperature applications. Science 287:1024–28

34. Littleton RT, Tritt TM, Kolis JW, Ketchum DR, Lowhorn ND, Korzenski MB. 2001. Suppression of the resistivity anomaly and corresponding thermopower behavior in the pentatelluride system by the addition of Sb: Hf1-XZTrXTe5-Y Sby. Pbys. Rev. B 64:121104

35. Hsu KF, Loo S, Gao F, Chen W, Dyck JS, et al. 2004. Cubic AgPb$_{m}$SbTe$_{2+m}$: bulk thermoelectric materials with high figure of merit. Science 303:818–21

36. Shen Q, Chen L, Goto T, Hirai T, Yang J, et al. 2001. Effects of partial substitution of Ni by Pd on the thermoelectric properties of ZrNiSn-based half-Heusler compounds. Appl. Phys. Lett. 79:4165-67

37. Caillat T, Fleurial JP, Borshchevsky A. 1997. Preparation and thermoelectric properties of semiconducting $Zn_4Sb_3$. J. Phys. Chem. Solids 58:1119–25

38. He T, Chen J, Rosenfeld HD, Subramanian MA. 2006. Thermoelectric properties of indium-filled skutterudites. Chem. Mater. 18(3):759-62

39. Peng JY, He J, Su Z, Alboni PN, Zhu S, Tritt TM. 2009. High temperature thermoelectric properties of double-filled $In_x Yb_y Co_4 Sb_{12}$ skutterudites. J. Appl. Phys. 105:084907

40. Li H, Tang X, Zhang Q, Uher C. 2009. High performance $In_xCe_yCo_4Sb_{12}$ thermoelectric materials with in situ forming nanostructured InSb phase. Appl. Phys. Lett. 94:102114

41. Shi X, Kong H, Li C-P, Uher C, Yang J, et al. 2008. Low thermal conductivity and high thermoelectric figure of merit in n-type Ba_xYb_yCo_4Sb_{12}$ double-filled skutterudites. Appl. Phys. Lett. 92:182101

42. Terasaki I, Murayama N, eds. 2002. Oxide Thermoelectrics. Trivandrum, India: Res. Signpost

43. Ohtaki M, Tsubota T, Eguchi K, Arai H. 1996. High-temperature thermoelectric properties of $(Zn_{12-x}Al_x)O. \mathcal{J}. Appl. Pbys. 79(3):1816-18$

44. Hicks LD, Dresselhaus MS. 1993. Effect of quantum-well structures on the thermoelectric figure of merit. Phys. Rev. B 47:12727-31

45. Venkatasubramanian R, Siivola E, Colpitts T, O'Quinn B. 2001. Thin-film thermoelectric devices with high room-temperature figures of merit. Nature 13:597-602

46. Harman TC, Taylor PJ, Walsh MP, LaForge BE. 2002. Quantum dot superlattice thermoelectric materials and devices. Science 297:2229–32

47. Tritt TM. 1999. Holey and unholey semiconductors. Science 283:804-5

Annu. Rev. Mater. Res. 2011.41:433-448. Downloaded from www.annualreviews.org by Clemson University on 11/18/11. For personal use only.

R

Annual Review of
Materials Research

Volume 41, 2011

# Contents

## Materials Science of Biological Systems

Advances in Drug Delivery

Brian P. Timko, Kathryn Whitehead, Weiwei Gao, Daniel S. Kohane,
Omid Farokbzad, Daniel Anderson, and Robert Langer
1

Crystallization Pathways in Biomineralization
Steve Weiner and Lia Addadi

Deformation and Fracture Mechanisms of Bone and Nacre
Rizbi Wang and Himadri S. Gupta ..............................................................................................................................................................................................................................................................................................................................................................................................................................

Linear and Nonlinear Rheology of Living Cells
Philip Kollmannsberger and Ben Fabry .................................................................................................................................. 75

Mussel-Inspired Adhesives and Coatings
Bruce P. Lee, P.B. Messersmith, J.N. Israelachvili, and J.H. Waite 99

Nanomechanics of the Cartilage Extracellular Matrix
Lin Han, Alan J. Grodzinsky, and Christine Ortiz 133

Plant Stems: Functional Design and Mechanics
Thomas Speck and Ingo Burgert 169

## Current Interest

Elastic and Mechanical Properties of the MAX Phases
Michel W. Barsoum and Miladin Radovic 195

Electrocaloric Materials
J.F. Scott 229

Electrochromic Materials
Roger J. Mortimer 241

Nanowire Solar Cells
## Erik C. Garnett, Mark L. Brongersma, Yi Cui, and Michael D. McGebee 269

Nonconventional (Non-Silicon-Based) Photovoltaic Materials
T. Unold and H.W. Schock 297

Annu. Rev. Mater. Res. 2011.41:433-448. Downloaded from www.annualreviews.org by Clemson University on 11/18/11. For personal use only.

On the Future Availability of the Energy Metals

T.E. Graedel $\ldots$ 323

Oxide Electronics Utilizing Ultrafast Metal-Insulator Transitions
Zheng Yang, Changbyun Ko, and Sbriram Ramanathan $\ldots$ 337

Point Defects in Oxides: Tailoring Materials Through Defect Engineering Harry L. Tuller and Sean R. Bishop $\ldots$ 369

Recent Developments in Semiconductor Thermoelectric Physics and Materials
Ali Shakouri $\ldots$ 399

Thermoelectric Phenomena, Materials, and Applications Terry M. Tritt $\ldots$ 433

# Index

Cumulative Index of Contributing Authors, Volumes 37-41 $\ldots$ 449

# Errata

An online log of corrections to Annual Review of Materials Research articles may be found at http://matsci.annualreviews.org/errata.shtml
