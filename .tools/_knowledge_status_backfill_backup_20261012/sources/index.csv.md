---
type: source
title: "index.csv"
source_type: 报价单
source_path: RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Mathematics of Diffusion/index.csv.md
original_link: ""
date_published: 2026-10-11
date_processed: 2026-10-11
credibility: 中
key_claims: []
pages_linked: []
compile_mode: extractive
---

# index.csv

## Positioning 定位

本文为 IMA 知识库条目的抽取式源摘要页（`source_type: 报价单`）。
正文直接摘录自镜像层 `RAW_FULL/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Mathematics of Diffusion/index.csv.md`，未做语义改写；
待后续深度编译时补全 `key_claims` 与实体链接。

## Extracted Content 原文摘录

# index.csv.md

|章节|页码|原句|引用目的|
|---|---|---|---|
|Ch1|1|DIFFUSION is the process by which matter is transported from one part of a system to another as a result of random molecular motions.|扩散物理定义|
|Ch1|2|the rate of transfer of diffusing substance through unit area of a section is proportional to the concentration gradient measured normal to the section, i.e. F = -D dC/dx|Fick 第一定律数学表述|
|Ch1|2|In some cases, e.g. diffusion in dilute solutions, D can reasonably be taken as constant, while in others, e.g. diffusion in high polymers, it depends very markedly on concentration.|D 的浓度依赖性|
|Ch1|3|the statement expressed mathematically by (1.1) is in general consistent only for an isotropic medium|各向同性假设|
|Ch1|4|dC/dt = D d²C/dx²|扩散 PDE（Fick 第二定律）|
|Ch2|12|Either it is comprised of a series of error functions or related integrals, in which case it is most suitable for numerical evaluation at small times… or it is in the form of a trigonometrical series which converges most satisfactorily for large values of time.|两类标准解|
|Ch2|12|C = (M/2(πDt)^½) exp(-x²/4Dt), and this is therefore the solution which describes the spreading by diffusion of an amount of substance M deposited at time t = 0 in the plane x = 0.|瞬时平面源格林函数|
|Ch2|13|Since this equation is linear the sum of the two solutions is itself a solution|反射法数学依据|
|Ch2|13|the condition to be satisfied at the impermeable boundary is dC/dx = 0, x = 0|不透边界条件|
|Ch3|29|all problems in which an amount of diffusing substance is deposited within a certain restricted region at time t = 0 and left to diffuse throughout the surrounding medium.|瞬时源定义|
|Ch3|30|the integral in (3.10) has to be evaluated numerically except on the axis r = 0, where (3.10) becomes C = C₀{1-exp(-a²/4Dt)}.|球源轴心简化|
|Ch4|45|F = -D dC/dx = D(C₁ - C₂)/l|片层稳态通量|
|Ch4|46|P = DS|渗透常数定义|
|Ch4|47|the resistance to diffusion of the whole membrane is simply the sum of the resistances of the separate layers|复合膜串联|
|Ch4|48|M_t/M_∞ = 1 - (8/π²) Σ [1/(2n+1)²] exp{-D(2n+1)²π²t/4l²}|非稳态通量级数|
|Ch4|52|L = l²/6D … Following Daynes (1920), Barrer (1951) has used (4.26) as the basis of a method for obtaining the diffusion constant|时间滞后法|
|Ch4|52|To within the accuracy of plotting the steady state is achieved when Dt/l² = 0.45 approximately|稳态判据|
|Ch5|70|The concentration distribution defined by (5.4) is not linear, as it is for the plane sheet.|柱几何对数分布|
|Ch5|71|if ah < 1 the rate first increases and later decreases, passing through a maximum when b = 1/h.|最优壁厚判据|
|Ch5|77|M_t/M_∞ = 4a(1+a) Σ [exp(-Dqₙ²t/a²)/(qₙ(4a²+qₙ²))]|有限体积柱解|
|Ch6|90|On putting u = Cr, (6.1) becomes ∂u/∂t = D ∂²u/∂r². Since this is the equation for linear flow in one dimension|u=Cr 变换|
|Ch6|91|(C-C₁)/(C₀-C₁) at r=0 = 1 + 2 Σ(-1)ⁿ exp(-Dn²π²t/a²)|球心浓度简化|
|Ch6|92|M_t/M_∞ = 1 - (6/π²) Σ [1/n² · (1+3α)/(1+3αn²) · exp(-Dn²π²t/a²)]|有限体积球解|
|Ch7|106|Boltzmann (1894) showed that for certain boundary conditions, provided D is a function of C only, C may be expressed in terms of a single variable x/2√t|Boltzmann 变换|
|Ch7|107|It is only when the initial and boundary conditions are expressible in terms of η alone|Boltzmann 适用条件|
|Ch7|107|Crank and Henry (1949a,b) gave a method of solving (7.10)… based on iterative quadrature.|Crank-Henry 迭代法|
|Ch8|138|there are a number of advantages in using non-dimensional variables in numerical work|无量纲化|
|Ch8|144|this condition is r ≤ ½, i.e. δT ≤ ½(δX)²|显式格式稳定性|
|Ch8|145|The Crank-Nicolson method has the strong advantage of remaining stable for all values of r|Crank-Nicolson 稳定性|
|Ch8|147|A more accurate replacement of (8.21) is possible by introducing a 'fictitious' concentration c₋₁ʲ at the external grid point|虚拟点法|
|Ch9|161|D₀∫{1+f(C)}dC = Ax + B|D(C) 稳态解|
|Ch9|162|when D increases as C increases the concentration-distance curves in the steady state are convex away from the distance axis|D(C) 定性判据|
|Ch9|168|the rate of transfer of B will be, to a first approximation, dependent on A·C_A only|双组分扩散结论|
|Ch10|203|the diffusion coefficient is defined as the rate of transfer of the diffusing substance across unit area of a section, divided by the space gradient of concentration at the section|D 定义|
|Ch10|204|In order that (10.4) and (10.6) shall both be satisfied it follows that D_A^V = D_B^V|互扩散系数|
|Ch10|225|Frisch (1958) showed that from measurements of L and the steady-state flow F at different pressures, both the parameters in the D(C) functional relationship and the solubility coefficient can be found|Frisch D(C) 反演|
|Ch10|227|L(l) can be written as the sum of a 'Fickian' time lag L_F(l) and a 'non-Fickian' or 'time-dependent' contribution L_T which is independent of l|Frisch 分解|
|Ch10|227|D_T is the 'thermodynamic diffusion coefficient', and D_0 the corresponding kinetic coefficient|热力学/动力学 D 分离|
|Ch11|255|THE diffusion behaviour of many polymers cannot be described adequately by a concentration-dependent form of Fick's law… In rubbery polymers, on the other hand, diffusion is generally Fickian.|非菲克现象|
|Ch11|256|(i) Case I or Fickian diffusion in which the rate of diffusion is much less than that of relaxation; (ii) Case II diffusion, the other extreme in which diffusion is very rapid compared with the relaxation processes; (iii) Non-Fickian or anomalous diffusion which occurs when the diffusion and relaxation rates are comparable.|Alfrey-Gurnee-Lloyd 三分类|
|Ch11|256|Case II systems are characterized by n = 1 and Case I systems by n = ½. Non-Fickian systems lie between Case I and Case II in that n takes an intermediate value between ½ and 1.|Mt ∝ tⁿ 判据|
|Ch11|256|the parameter is the constant velocity of an advancing front which marks the innermost limit of penetration of the diffusant and is the boundary between swollen gel and glassy core|Case II 匀速前沿|
|Ch11|256|The sorption curves are sigmoid in shape with a single point of inflexion often at about 50 per cent equilibrium sorption.|Sigmoid 曲线|
|Ch12|267|1/R_L = 1/R_L1 + 1/R_L2 + ⋯ + 1/R_Ln = Σ Pᵢ = Δp|层状串联阻力|
|Ch12|268|D̄ᵢ = (1/(C₂ᵢ - C₂ᵢ₋₁)) ∫Dᵢ dC|积分

*（正文超过 6000 字，此处截断；完整内容见镜像层）*

## Original 原文

- 本地路径：`RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Mathematics of Diffusion/index.csv.md`
- 镜像正文：`RAW_FULL/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Mathematics of Diffusion/index.csv.md`