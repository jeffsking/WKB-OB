---
media_id: "pdf_3867e2b60070d7dc3f413086d0b0036e_d7f6edb8a86491caca2d81de168c3834001a693ee6c0644e"
source_file: "THE_MATHEMATICS_OF_DIFFUSION_CLARENDON_P.pdf.md"
original_path: "RAW/ima_sync/个人知识库/WKB/Resources/Ebook/THE_MATHEMATICS_OF_DIFFUSION_CLARENDON_P.pdf.md"
extracted: "2026-09-27"
extract_method: "ima-mcp fetch_media_content"
extract_status: "ok"
clean_rules: "v2: dead-image-link->text(alt kept); repeat-digits->compressed"
processed: "2026-09-27"
---

# THE_MATHEMATICS_OF_DIFFUSION_CLARENDON_P.pdf.md

8
# THE MATHEMATICS
OF DIFFUSION

BY

J. CRANK

BRUNEL UNIVERSITY
UXBRIDGE

SECOND EDITION

CLARENDON PRESS · OXFORD

Oxford University Press, Ely House, London W.I.

GLASGOW NEW YORK TORONTO MELBOURNE WELLINGTON
CAPE TOWN IBADAN NAIROBI DAR ES SALAAM LUSAKA ADDIS ABABA
DELHI BOMBAY CALCUTTA MADRAS KARACHI LAHORF DACCA
KUALA LUMPUR SINGAPORE HONG KONG TOKYO

ISBN 0-19-853344-6

© OXFORD UNIVERSITY PRESS 1975

All rights reserved. No part of this publication may be reproduced, stored in a retrieval system, or transmitted, in any form or by any means, electronic, mechanical, photocopying, recording or otherwise, without the prior permission of Oxford University Press

FIRST EDITION 1956
SECOND EDITION 1975

# PREFACE TO SECOND EDITION

IN preparing this second edition I have tried to incorporate as much new material as possible but to preserve the character of the original volume. The book contains a collection of mathematical solutions of the differential equations of diffusion and methods of obtaining them. They are discussed against a background of some of the experimental and practical situations to which they are relevant. Little mention is made of molecular mechanisms, and I have made only fleeting excursions into the realms of irreversible thermodynamics. These I hope are self-explanatory. A number of general accounts of the subject are already available, but very few mathematical solutions of the equations of non-equilibrium thermodynamics have been obtained for practical systems.

During the last 15-20 years the widespread occurrence of concentration-dependent diffusion has stimulated the development of new analytical and numerical solutions. The time-lag method of measuring diffusion coefficients has also been intensively investigated and extended. Similarly, a lot of attention has been devoted to moving-boundary problems since the first edition was published. These and other matters have now been included by extensive revision of several chapters. Also, the chapter dealing with the numerical solution of the diffusion equations has been completely rewritten and brought up to date. It seems unbelievable now that most of the calculations in the first edition were carried out on desk calculating machines.

Two entirely new chapters have been added. In one are assembled some of the mathematical models of non-Fickian or anomalous diffusion occurring mainly in solvent-polymer systems in the glassy state. The other attempts a systematic review of diffusion in heterogeneous media, both laminates and particulates. A succession of improved solutions are described to the problem of diffusion in a medium in which are embedded discrete particles with different diffusion properties.

I have resisted the temptation to lengthen appreciably the earlier chapters. The enlarged edition of Carslaw and Jaeger's book Conduction of heat in solids contains a wealth of solutions of the heat-flow equations for constant heat parameters. Many of them are directly applicable to diffusion problems, though it seems that some non-mathematicians have difficulty in making the necessary conversions. For them I have included a brief ' translator 's guide'. A few new solutions have been added, however, some of them in the context in which they arose, that is the measurement of diffusion coefficients.

I should like to express my appreciation to the Vice Chancellor and Council of Brunel University for so readily agreeing to my application for extended leave without which I could not have undertaken the preparation of

vi

PREFACE TO THE SECOND EDITION

a second edition. I am deeply grateful to my academic colleagues who shared my administrative responsibilities and particularly to Professor Peter Macdonald who so willingly and effectively assumed the role of Acting Head of the School of Mathematical Studies.

I am most grateful to Mrs. Joyce Smith for all the help she gave me, not least by typing the manuscript and checking the proofs. Mr. Alan Moyse kept me well supplied with the seemingly innumerable books, journals, and photostat copies which I requested.

I owe a great deal to friendly readers who have pointed out mistakes in the first edition and made helpful suggestions for the second. In particular I have benefited from discussions with my friend and former colleague, Dr. Geoffrey Park. I had an invaluable introduction to the literature on which Chapter 12 is based from Mr. W. M. Woodcock, who came to me for help but, in fact, gave far more than he received. Finally, I have appreciated the understanding help and guidance afforded me by members of staff of the Clarendon Press.

Uxbridge
October 1973

J.C.

# ACKNOWLEDGEMENTS

I wish to acknowledge the permission of the authors or publishers of the following journals or books to reproduce the figures and tables specified: Fig. 4.9, Barr, R. M. Trans. Faraday Soc.; Fig. 10.8, Frensdorff, H. K. J. Poly. Sci.; Fig. 11.1, Rogers, C. E. 'Physics and Chemistry of the Organic Solid State'. J. Wiley & Sons Inc.; Fig. 11.2, J. Poly. Sci.; Fig. 12.1, Jefferson, T. B. Ind. & Eng. Chem.; Fig. 12.2, Tsoa, G. Ind. & Eng. Chem.; Fig. 12.3, Cheng, S. C. & Vachon, R. I. J. Heat & Mass Transfer; Fig. 13.11, J. Inst. Maths. Applic.; Table 7.1, Lee, C. F. J. Inst. Maths. Applic.; Table 7.6, Wilkins, J. E. J. Soc. Ind. Appl. Maths.; Table 7.7, Philip, J. R. Aust. J. Phys.; Table 9.1, Wilkins, J. E. J. Soc. Ind. Appl. Maths.; and Table 10.2, Hansen, C. M. I. & E. C. Fundamentals.

# PREFACE

A MORE precise title for this book would be 'Mathematical solutions of the diffusion equation', for it is with this aspect of the mathematics of diffusion that the book is mainly concerned. It deals with the description of diffusion processes in terms of solutions of the differential equation for diffusion. Little mention is made of the alternative, but less well developed, description in terms of what is commonly called 'the random walk', nor are theories of the mechanism of diffusion in particular systems included.

The mathematical theory of diffusion is founded on that of heat conduction and correspondingly the early part of this book has developed from 'Conduction of heat in solids' by Carslaw and Jaeger. These authors present many solutions of the equation of heat conduction and some of them can be applied to diffusion problems for which the diffusion coefficient is constant. I have selected some of the solutions which seem most likely to be of interest in diffusion and they have been evaluated numerically and presented in graphical form so as to be readily usable. Several problems in which diffusion is complicated by the effects of an immobilizing reaction of some sort are also included. Convenient ways of deriving the mathematical solutions are described.

When we come to systems in which the diffusion coefficient is not constant but variable, and for the most part this means concentration dependent, we find that strictly formal mathematical solutions no longer exist. I have tried to indicate the various methods by which numerical and graphical solutions have been obtained, mostly within the last ten years, and to present, again in graphical form, some solutions for various concentration-dependent diffusion coefficients. As well as being useful in themselves these solutions illustrate the characteristic features of a concentration-dependent system. Consideration is also given to the closely allied problem of determining the diffusion coefficient and its dependence on concentration from experimental measurements. The diffusion coefficients measured by different types of experiment are shown to be simply related. The final chapter deals with the temperature changes which sometimes accompany diffusion.

In several instances I have thought it better to refer to an easily accessible book or paper rather than to the first published account, which the reader might find difficult to obtain. Ease of reference usually seemed of primary importance, particularly with regard to mathematical solutions.

I should like to express my thanks to my friend and colleague, Mr. A. C. Newns, who read the typescript and made many valuable comments and suggestions, and also to Mrs. D. D. Whitmore, who did most of the calculations and helped to correct the proofs and compile the index. I am grateful

viii

PREFACE

to Miss D. Eldridge who, by patient and skilful typing, transformed an almost illegible manuscript into a very clear typescript for the printer. I should also like to thank the following who readily gave permission to use material from various publications: Professor R. M. Barrer, Mr. M. B. Coyle, Dr. P. V. Danckwerts, Dr. L. D. Hall, Dr. P. S. H. Henry, Professor J. C. Jaeger, Dr. G. S. Park, Dr. R. H. Stokes, Dr. C. Wagner, and the publishers of the following journals, British Journal of Applied Physics, Journal of Chemical Physics, Journal of Metals, Journal of Scientific Instruments, Philosophical Magazine, Proceedings of the Physical Society, Transactions of the Faraday Society. Finally, it is a pleasure to thank those members of the staff of the Clarendon Press who have been concerned with the production of this book for the kindness and consideration they have shown to me.

Maidenhead

J. C.

December 1955

# CONTENTS

1. The diffusion equations 1

2. Methods of solution when the diffusion coefficient is constant 11

3. Infinite and sem-infinite media 28

4. Diffusion in a plane sheet 44

5. Diffusion in a cylinder 69

6. Diffusion in a sphere 89

7. Concentration-dependent diffusion: methods of solution 104

8. Numerical methods 137

9. Some calculated results for variable diffusion coefficients 160

10. The definition and measurement of diffusion coefficients 203

11. Non-Fickian diffusion 254

12. Diffusion in heterogeneous media 266

13. Moving boundaries 286

14. Diffusion and chemical reaction 326

15. Simultaneous diffusion of heat and moisture 352

Tables 375

References 399

Author index 407

Subject index 411

# 1

## THE DIFFUSION EQUATIONS

### 1.1. The diffusion process

DIFFUSION is the process by which matter is transported from one part of a system to another as a result of random molecular motions. It is usually illustrated by the classical experiment in which a tall cylindrical vessel has its lower part filled with iodine solution, for example, and a column of clear water is poured on top, carefully and slowly, so that no convection currents are set up. At first the coloured part is separated from the clear by a sharp, well-defined boundary. Later it is found that the upper part becomes coloured, the colour getting fainter towards the top, while the lower part becomes correspondingly less intensely coloured. After sufficient time the whole solution appears uniformly coloured. There is evidently therefore a transfer of iodine molecules from the lower to the upper part of the vessel taking place in the absence of convection currents. The iodine is said to have diffused into the water.

If it were possible to watch individual molecules of iodine, and this can be done effectively by replacing them by particles small enough to share the molecular motions but just large enough to be visible under the microscope, it would be found that the motion of each molecule is a random one. In a dilute solution each molecule of iodine behaves independently of the others, which it seldom meets, and each is constantly undergoing collision with solvent molecules, as a result of which collisions it moves sometimes towards a region of higher, sometimes of lower, concentration, having no preferred direction of motion towards one or the other. The motion of a single molecule can be described in terms of the familiar 'random walk' picture, and whilst it is possible to calculate the mean-square distance travelled in a given interval of time it is not possible to say in what direction a given molecule will move in that time.

This picture of random molecular motions, in which no molecule has a preferred direction of motion, has to be reconciled with the fact that a transfer of iodine molecules from the region of higher to that of lower concentration is nevertheless observed. Consider any horizontal section in the solution and two thin, equal, elements of volume one just below and one just above the section. Though it is not possible to say which way any particular iodine molecule will move in a given interval of time, it can be said that on the average a definite fraction of the molecules in the lower element of volume will cross the section from below, and the same fraction of molecules in the

2

THE DIFFUSION EQUATIONS

upper element will cross the section from above, in a given time. Thus, simply because there are more iodine molecules in the lower element than in the upper one, there is a net transfer from the lower to the upper side of the section as a result of random molecular motions.

# 1.2. Basic hypothesis of mathematical theory

Transfer of heat by conduction is also due to random molecular motions, and there is an obvious analogy between the two processes. This was recognized by Fick (1855), who first put diffusion on a quantitative basis by adopting the mathematical equation of heat conduction derived some years earlier by Fourier (1822). The mathematical theory of diffusion in isotropic substances is therefore based on the hypothesis that the rate of transfer of diffusing substance through unit area of a section is proportional to the concentration gradient measured normal to the section, i.e.

$$F = -D \frac{\partial C}{\partial x}, \qquad (1.1)$$

where $F$ is the rate of transfer per unit area of section, $C$ the concentration of diffusing substance, $x$ the space coordinate measured normal to the section, and $D$ is called the diffusion coefficient. In some cases, e.g. diffusion in dilute solutions, $D$ can reasonably be taken as constant, while in others, e.g. diffusion in high polymers, it depends very markedly on concentration. If $F$, the amount of material diffusing, and $C$, the concentration, are both expressed in terms of the same unit of quantity, e.g. gram or gram molecules, then it is clear from (1.1) that $D$ is independent of this unit and has dimensions (length)$^{2}$ (time)$^{-1}$, e.g. cm$^{2}$ s$^{-1}$. The negative sign in eqn (1.1) arises because diffusion occurs in the direction opposite to that of increasing concentration.

It must be emphasized that the statement expressed mathematically by (1.1) is in general consistent only for an isotropic medium, whose structure and diffusion properties in the neighbourhood of any point are the same relative to all directions. Because of this symmetry, the flow of diffusing substance at any point is along the normal to the surface of constant concentration through the point. As will be seen later in § 1.4 (p. 5), this need not be true in an anisotropic medium for which the diffusion properties depend on the direction in which they are measured.

# 1.3. Differential equation of diffusion

The fundamental differential equation of diffusion in an isotropic medium is derived from eqn (1.1) as follows.

Consider an element of volume in the form of a rectangular parallelepiped whose sides are parallel to the axes of coordinates and are of lengths 2 dx, 2 dy, 2 dz. Let the centre of the element be at $P(x, y, z)$, where the

THE DIFFUSION EQUATIONS

3

concentration of diffusing substance is C. Let ABCD and A'B'C'D' be the faces perpendicular to the axis of x as in Fig. 1.1. Then the rate at which diffusing substance enters the element through the face ABCD in the plane x - dx is given by

$$ 4 dy dz \left( F_x - \frac{\partial F_x}{\partial x} dx \right), $$

where $F_x$ is the rate of transfer through unit area of the corresponding plane through P. Similarly the rate of loss of diffusing substance through the face A'B'C'D' is given by

$$ 4 dy dz \left( F_x + \frac{\partial F_x}{\partial x} dx \right). $$

[图片: CC2dzDDPOFx0Fxdx)dx)4dydz(Fx-B4dydz(Fx+2x2dy0xBA2dxA]
# FIG. 1.1. Element of volume.

The contribution to the rate of increase of diffusing substance in the element from these two faces is thus equal to

$$ -8 \ dx \ dy \ dz \frac{\partial F_x}{\partial x} $$

Similarly from the other faces we obtain

$$ -8 \, dx \, dy \, dz \frac{\partial F_y}{\partial y} \quad \text{and} \quad -8 \, dx \, dy \, dz \frac{\partial F_z}{\partial z}. $$

But the rate at which the amount of diffusing substance in the element increases is also given by

$$ 8 \text{ dx dy dz} \frac{\partial C}{\partial t}, $$

and hence we have immediately

$$ \frac{\partial C}{\partial t} + \frac{\partial F_x}{\partial x} + \frac{\partial F_y}{\partial y} + \frac{\partial F_z}{\partial z} = 0. \quad (1.2) $$

4

THE DIFFUSION EQUATIONS

If the diffusion coefficient is constant, $F_x$, $F_y$, $F_z$ are given by (1.1), and (1.2) becomes

$$ \frac{\partial C}{\partial t} = D\left(\frac{\partial^2 C}{\partial x^2} + \frac{\partial^2 C}{\partial y^2} + \frac{\partial^2 C}{\partial z^2}\right), \qquad (1.3) $$

reducing simply to

$$ \frac{\partial C}{\partial t} = D \frac{\partial^2 C}{\partial x^2} \qquad (1.4) $$

if diffusion is one-dimensional i.e. if there is a gradient of concentration only along the x-axis. Expressions (1.1) and (1.4) are usually referred to as Fick's first and second laws of diffusion, since they were first formulated by Fick (1855) by direct analogy with the equations of heat conduction.

In many systems, e.g. the interdiffusion of metals or the diffusion of organic vapours in high-polymer substances, $D$ depends on the concentration of diffusing substance $C$. In this case, and also when the medium is not homogeneous so that $D$ varies from point to point, eqn (1.2) becomes

$$ \frac{\partial C}{\partial t} = \frac{\partial}{\partial x} \left( D \frac{\partial C}{\partial x} \right) + \frac{\partial}{\partial y} \left( D \frac{\partial C}{\partial y} \right) + \frac{\partial}{\partial z} \left( D \frac{\partial C}{\partial z} \right), \qquad (1.5) $$

where $D$ may be a function of $x, y, z$, and $C$.

If $D$ depends on the time during which diffusion has been taking place but not on any of the other variables, i.e.

$$D = f(t),$$

then on introducing a new time-scale $T$ such that

$$dT = f(t) dt,$$

the diffusion equation becomes

$$ \frac{\partial C}{\partial T} = \frac{\partial^2 C}{\partial x^2} + \frac{\partial^2 C}{\partial y^2} + \frac{\partial^2 C}{\partial z^2}, \qquad (1.6) $$

which is the same as (1.3) for a constant diffusion coefficient equal to unity.

# 1.3.1. Diffusion in a cylinder and sphere

Other forms of the above equations follow by transformation of coordinates, or by considering elements of volume of different shape. Thus by putting

$$ \begin{aligned} x &= r \cos \theta, \\ y &= r \sin \theta, \end{aligned} $$

or by considering an element of volume of a cylinder of sides dr, $r$ dθ, dz,

THE DIFFUSION EQUATIONS

5

we obtain the equation for diffusion in a cylinder,

$$ \frac{\partial C}{\partial t} = \frac{1}{r} \left\{ \frac{\partial}{\partial r} \left( rD \frac{\partial C}{\partial r} \right) + \frac{\partial}{\partial \theta} \left( \frac{D}{r} \frac{\partial C}{\partial \theta} \right) + \frac{\partial}{\partial z} \left( rD \frac{\partial C}{\partial z} \right) \right\}, \quad (1.7) $$

in terms of the cylindrical coordinates $r, \theta, z$. The corresponding equation for a sphere in terms of spherical polar coordinates $r, \theta, \phi$ is obtained by writing

$$ \begin{aligned} x &= r \sin \theta \cos \phi, \\ y &= r \sin \theta \sin \phi, \\ z &= r \cos \theta, \end{aligned} $$

or by considering an element of volume of a sphere of sides $dr$, $r d\theta$, $r \sin \theta d\phi$. It is

$$ \frac{\partial C}{\partial t} = \frac{1}{r^2} \left\{ \frac{\partial}{\partial r} \left( Dr^2 \frac{\partial C}{\partial r} \right) + \frac{1}{\sin \theta} \frac{\partial}{\partial \theta} \left( D \sin \theta \frac{\partial C}{\partial \theta} \right) + \frac{D}{\sin^2 \theta} \frac{\partial^2 C}{\partial \phi^2} \right\}. \quad (1.8) $$

The simplified forms of (1.7) and (1.8) for purely radial diffusion, e.g. in a long cylinder where end effects are negligible or in a spherically symmetrical system, are given in Chapters 5 and 6, where some solutions of the differential equations are to be found. All these diffusion equations can be expressed in terms of the nomenclature of vector analysis as

$$ \frac{\partial C}{\partial t} = \operatorname{div} (D \operatorname{grad} C). $$

# 1.4. Anisotropic media

Anisotropic media have different diffusion properties in different directions. Some common examples are crystals, textile fibres, and polymer films in which the molecules have a preferential direction of orientation. For such media it is not always true, as was stated in § 1.2 (p. 2) for isotropic media, that the direction of flow of diffusing substance at any point is normal to the surface of constant concentration through the point. This means that (1.1) must be replaced in general by the assumptions

$$ \left. \begin{aligned} -F_x &= D_{11} \frac{\partial C}{\partial x} + D_{12} \frac{\partial C}{\partial y} + D_{13} \frac{\partial C}{\partial z} \\ -F_y &= D_{21} \frac{\partial C}{\partial x} + D_{22} \frac{\partial C}{\partial y} + D_{23} \frac{\partial C}{\partial z} \\ -F_z &= D_{31} \frac{\partial C}{\partial x} + D_{32} \frac{\partial C}{\partial y} + D_{33} \frac{\partial C}{\partial z} \end{aligned} \right\}, \quad (1.9) $$

6

THE DIFFUSION EQUATIONS

so that $F_x$, for example, depends not only on $\partial C/\partial x$ but also on $\partial C/\partial y$ and $\partial C/\partial z$. The $D_s$ have the significance that $D_{13} \ \partial C/\partial z$, for example, is the contribution to the rate of transfer in the $x$-direction due to the component of concentration gradient in the $z$-direction. Substituting from (1.9) for the $F_s$ in (1.2) we obtain

$$ \frac{\partial C}{\partial t} = D_{11} \frac{\partial^2 C}{\partial x^2} + D_{22} \frac{\partial^2 C}{\partial y^2} + D_{33} \frac{\partial^2 C}{\partial z^2} + (D_{23} + D_{32}) \frac{\partial^2 C}{\partial y \partial z} \\ + (D_{31} + D_{13}) \frac{\partial^2 C}{\partial z \partial x} + (D_{12} + D_{21}) \frac{\partial^2 C}{\partial x \partial y}, \quad (1.10) $$

if the $Ds$ are taken as constant. The extension to non-constant $Ds$ is obvious from (1.5). A transformation to rectangular coordinates $\xi, \eta, \zeta$ can be found which reduces (1.10) to

$$ \frac{\partial C}{\partial t} = D_1 \frac{\partial^2 C}{\partial \xi^2} + D_2 \frac{\partial^2 C}{\partial \eta^2} + D_3 \frac{\partial^2 C}{\partial \zeta^2}. \quad (1.11) $$

This is the same transformation as that by which the ellipsoid

$$ D_{11}x^2 + D_{22}y^2 + D_{33}z^2 + (D_{23} + D_{32})yz + (D_{31} + D_{13})zx + (D_{12} + D_{21})xy = \text{constant} \quad (1.12) $$

is reduced to

$$ D_1 \xi^2 + D_2 \eta^2 + D_3 \zeta^2 = \text{constant.} \quad (1.13) $$

The new axes may be called the principal axes of diffusion and $D_1, D_2, D_3$ the principal diffusion coefficients. If we make the further transformation

$$ \xi_1 = \xi\sqrt{D/D_1}, \quad \eta_1 = \eta\sqrt{D/D_2}, \quad \zeta_1 = \zeta\sqrt{D/D_3}, \quad (1.14) $$

where $D$ may be chosen arbitrarily, (1.11) becomes:

$$ \frac{\partial C}{\partial t} = D \left( \frac{\partial^2 C}{\partial \xi_1^2} + \frac{\partial^2 C}{\partial \eta_1^2} + \frac{\partial^2 C}{\partial \zeta_1^2} \right). \quad (1.15) $$

This has the same form as eqn (1.3) for isotropic media, and hence certain problems in anisotropic media can be reduced to corresponding problems in isotropic media. Whether or not this can be done in a given case depends on the boundary conditions. Thus it is possible when the medium is infinite, or when it is bounded by planes perpendicular to the principal axes of diffusion so that the boundary conditions are of the familiar form $C = \text{constant}$, $\xi = 0$, $\xi = l$, $t > 0$, for example, and similarly for $\eta$ and $\zeta$. The problem of diffusion into an anisotropic cylinder which has its axis along $\xi$ and is bounded by planes perpendicular to $\xi$ reduces to the corresponding problem in an isotropic cylinder provided $D_2 = D_3$.

THE DIFFUSION EQUATIONS

7

Certain properties deduced by Carswal and Jaeger (1959, p. 46) indicate the physical significance of the ellipsoid and also of the principal axes of diffusion. Thus it can be shown that the square of the radius vector of the ellipsoid in any direction is inversely proportional to the diffusion coefficient normal to the surfaces of constant concentration at points where their normals are in that direction. Hence the diffusion coefficient $D_n$ at right angles to surfaces whose normals have direction cosines $l, m, n$ relative to the principal axes of diffusion is given by

$$ D_n = l^2 D_1 + m^2 D_2 + n^2 D_3. \quad (1.16) $$

Carsw and Jaeger further show that if there is symmetry about the planes $\xi = 0$ and $\eta = 0$, then the general relationships (1.9) for the Fs reduce to

$$-F_{\xi} = D_1 \partial C / \partial \xi, \quad -F_{\eta} = D_2 \partial C / \partial \eta, \quad -F_{\zeta} = D_3 \partial C / \partial \zeta. \quad (1.17)$$

This simplification also occurs for other types of crystallographic symmetry. It means that the flow through a surface perpendicular to a principal axis of diffusion is proportional simply to the concentration gradient normal to the surface as is the case for isotropic media.

# 1.4.1. Significance of measurements in anisotropic media

Since in the majority of experiments designed to measure a diffusion coefficient the flow is arranged to be one-dimensional, it is worth while to see how such measurements are affected by anisotropy. If the diffusion is one-dimensional in the sense that a concentration gradient exists only along the direction of $x$, it is clear from (1.10), since both $C$ and $\partial C/\partial x$ are everywhere independent of $y$ and $z$, that the diffusion is governed by the simple equation

$$ \frac{\partial C}{\partial t} = D_{11} \frac{\partial^2 C}{\partial x^2}, \qquad (1.18) $$

and $D_{11}$ is the diffusion coefficient measured. If the direction of diffusion is chosen to be that of a principal axis, then $D_{11}$ is equal to one or other of the principal diffusion coefficients $D_1, D_2$, or $D_3$. Otherwise the coefficient $D_{11} = D_n$, related to $D_1, D_2, D_3$, by (1.16) is measured. This would be measured, for example, by an observation of the rate of flow through a plane sheet of a crystal cut so that its normal has direction cosines ($l, m, n$) relative to the principal axes of diffusion of the crystal. Similar remarks apply to a high polymer sheet in which there is both uniplanar and undirectional orientation, i.e., the molecules are arranged with their long axes lying mainly parallel to the plane of the sheet and all parallel to one direction in that plane. The principal axes of diffusion of such a sheet will be normal to the plane sheet, and along and perpendicular to the preferred direction of orientation in that plane. Even if a concentration gradient exists in one direction only,

8

THE DIFFUSION EQUATIONS

it is clear from (1.9) and (1.15) that the diffusion flow is not along this direction unless it coincides with a principal axis of diffusion.

# 1.4.2. Conversion of heat flow to diffusion solutions

Carslaw and Jaeger (1959) and other books contain a wealth of solutions of the heat-conduction equation. There is general awareness among scientists and engineers that the phenomena of heat flow and diffusion are basically the same. Nevertheless, many non-mathematics experience difficulty in making the changes of notation needed to transcribe from one set of solutions to the other. In this section we examine in detail the correspondence between the physical parameters, the variables, and the equations and boundary conditions which occur in heat-flow and diffusion problems. We take the one-dimensional case with constant properties as an illustration.

(i) The equations. Diffusion theory is based on Fick's two equations (1.1) and (1.4), where C is the concentration of diffusant expressed, say, in mass per unit volume, and D is the diffusion coefficient. The two corresponding equations in heat flow are

$$ F = -K \frac{\partial \theta}{\partial x}, \qquad (1.19) $$

$$ \frac{\partial \theta}{\partial t} = \left( \frac{K}{c\rho} \right) \frac{\partial^2 \theta}{\partial x^2}, \qquad (1.20) $$

where $\theta$ is temperature, $K$ is the heat conductivity, $\rho$ is density, and $c$ specific heat, so that $\rho c$ is the heat capacity per unit volume. The space coordinate is $x$ and $t$ is time. In (1.19), $F$ is the amount of heat flowing in the direction of $x$ increasing per unit time through unit area of a section which is normal to the direction of $x$.

(ii) Variables and parameters. In order that the two sets of equations should correspond we may identify concentration $C$ with temperature $\theta$, and take $D = K$ in (1.1) and (1.19) and $D = K/(cp)$ in (1.4) and (1.20). The two together mean $cp = 1$. This is a consequence of our having identified $C$ with $\theta$. The 'diffusing substance' in heat flow is heat not temperature. The factor $cp$ is needed to convert temperature to the amount of heat per unit volume; but concentration is, by definition, the amount of diffusing substance per unit volume and so no conversion factor is needed, i.e. $cp = 1$. It is usual to write $K/(cp) = k$, the heat diffusivity. All three of $K$, $k$, $cp$ appear in heat-flow equations, and to convert to diffusion terms we take

$$ D = K = k \quad \text{and} \quad c\rho = 1. \qquad (1.21) $$

(iii) Boundary conditions. (a) Prescribed surface temperature corresponds to prescribed concentration just within the surface, say of a plane sheet. If the surface is in contact with a vapour at pressure $p$, there is some relation

THE DIFFUSION EQUATIONS

9

between $p$ and $C$ such as $C = Sp$, where $S$ is the solubility. There is no analogue to $S$ in heat flow.

(b) Prescribed heat flux corresponds to flux of diffusant and we have

$$ -K \frac{\partial \theta}{\partial x} = F(t), \quad \text{in heat,} \qquad (1.22a) $$

$$ -D \partial C/\partial x = F(t), \quad \text{in diffusion,} \qquad (1.22b) $$

where $F$ is in general a known function of time but may be constant.

(c) A heat-insulated surface corresponds to an impermeable surface and is the special case of (1.22a, b) with $F = 0$, i.e.

$$ \partial C / \partial x = \partial \theta / \partial x = 0. $$

(d) What is referred to as a 'radiation boundary condition' in heat flow usually means that the heat flux across unit area of the surface is proportional to the difference between the surface temperature $\theta_s$ and the temperature $\theta_0$ of the outside medium, i.e. is given by $H(\theta_s - \theta_0)$. But the rate of heat loss from unit area of a surface is $-K \partial\theta/\partial n$ in the direction of the normal $\mathbf{n}$, measured away from the surface, so that the boundary condition is

$$ K \frac{\partial \theta}{\partial n} + H(\theta_s - \theta_0) = 0, $$

i.e.

$$ \partial\theta/\partial n + h(\theta_s - \theta_0) = 0, $$

where $h = H/K$. Sometimes this is referred to as Newton's law of cooling. It corresponds to surface evaporation in diffusion, and we have

$$ \partial C / \partial n + \alpha (C_s - C_0) = 0 $$

where $\alpha = h = H/D$.

If the surface is perpendicular to the x-direction, as an example, $\partial C/\partial n = \partial C/\partial x$ if $n$ is along the direction of $x$ increasing but $\partial C/\partial n = -\partial C/\partial x$ if along $x$ decreasing. Thus for a slab between $x = 0$ and $x = 1$ we have

$$ \partial c / \partial x + \alpha (C_s - C_0) = 0, \quad x = 1, $$

but

$$ -\partial c / \partial x + \alpha (C_s - C_0) = 0, \quad x = 0. $$

(e) A perfect conductor of heat is always at a uniform temperature and so is equivalent in this respect to a well-stirred fluid. Thus, a boundary condition describing thermal contact with a perfect conductor also describes diffusion of solute from a well-stirred solution or vapour. Conservation of heat from a well-stirred fluid of fixed volume $V$ and uniform temperature $\theta_s$, a function of time, gives as a boundary condition on the surface $x = 0$ of a medium, $x > 0$, in contact with the fluid

$$c\rho V \frac{\partial \theta_s}{\partial t} = K \frac{\partial \theta}{\partial x}, \quad x = 0,$$

10

THE DIFFUSION EQUATIONS

where $c, \rho$ have their usual meaning for the fluid. Correspondingly for diffusion we have

$$V \partial C_s / \partial t = D \partial C / \partial x, \quad x = 0.$$

In addition, $\theta_s$ will be the temperature just within the surface but the two concentrations may be related by some isotherm equation. Care is needed with algebraic signs as in the previous section.

(f) The conservation principle applied at the interface between two media of different properties leads immediately to boundary conditions

$$ \theta_1 = \theta_2, \quad K_1 \partial\theta_1/\partial x = K_2 \partial\theta_2/\partial x $$

in heat flow and

$$C_1 = PC_2 + Q, \qquad D_1 \partial C_1 / \partial x = D_2 \partial C_2 / \partial x,$$

in diffusion, where the suffices 1 and 2 denote the two media and P and Q are constant.

(g) If heat is produced in a medium, e.g. as a result of an exothermic reaction, at a rate $A$ per unit volume, this must be added to the right side of eqn. (1.20), which can be written

$$c\rho\frac{\partial\theta}{\partial t}=K\frac{\partial^2\theta}{\partial x^2}+A.$$

The diffusion equation (1.4) must be similarly modified if the diffusing substance is created or removed as diffusion proceeds. We identify $A$ as the rate of creation per unit volume and put $c\rho = 1$, $K = D$ as usual.

(h) Problems in heat flow may involve moving boundaries on which phase changes occur, accompanied by the absorption or liberation of latent heat. In the first case, the relevant feature is that latent heat is removed instantaneously from the heat-conduction process, in which it takes no further part. The diffusion counterpart is the immobilizing of diffusing molecules on fixed sites or in holes. The velocity of the transformation boundary at $X(t)$ is related to the difference between the rate of heat arriving and leaving it by conduction by a condition

$$-K_1 \partial \theta_1 / \partial x + K_2 \partial \theta_2 / \partial x = L\rho \, dX / dt,$$

where $L$ is the latent heat per unit mass and $\rho$ the density, assuming no volume changes accompany the transformation. The condition in a diffusion problem follows by writing $\theta = C, D = K, \rho = 1$ as usual, and $L$ becomes the capacity of the immobilizing sites in unit volume for trapped diffusing molecules.

Useful collections of mathematical solutions of the diffusion equations are to be found in books by Barrer (1951), Jost (1952), and Jacobs (1967). Jacob's solutions are of particular interest to biologists and biophysicists.

# 2

## METHODS OF SOLUTION WHEN THE DIFFUSION COEFFICIENT IS CONSTANT

### 2.1. Types of solution

GENERAL solutions of the diffusion equation can be obtained for a variety of initial and boundary conditions provided the diffusion coefficient is constant. Such a solution usually has one of two standard forms. Either it is comprised of a series of error functions or related integrals, in which case it is most suitable for numerical evaluation at small times, i.e. in the early stages of diffusion, or it is in the form of a trigonometrical series which converges most satisfactorily for large values of time. When diffusion occurs in a cylinder the trigonometrical series is replaced by a series of Bessel functions. Of the three methods of solution described in this chapter, the first two illustrate the physical significance of the two standard types of solution. The third, employing the Laplace transform, is essentially an operator method by which both types of solution may be obtained. It is the most powerful of the three, particularly for more complicated problems. The methods are presented here as simply as possible. The fuller treatments necessary to make the discussion mathematically rigorous are to be found in works on heat conduction, e.g. Carslaw and Jaeger (1959).

### 2.2. Method of reflection and superposition

#### 2.2.1. Plane source

It is easy to see by differentiation that

$$C = \frac{A}{t^{\frac{1}{2}}} \exp(-x^2/4Dt), \qquad (2.1)$$

where $A$ is an arbitrary constant, is a solution of

$$ \frac{\partial C}{\partial t} = D \frac{\partial^2 C}{\partial x^2}, \qquad (2.2) $$

which is the equation for diffusion in one dimension when $D$ is constant. The expression (2.1) is symmetrical with respect to $x = 0$, tends to zero as $x$ approaches infinity positively or negatively for $t > 0$, and for $t = 0$ it vanishes everywhere except at $x = 0$, where it becomes infinite. The total amount of substance $M$ diffusing in a cylinder of infinite length and unit

12

METHODS OF SOLUTION WHEN THE

cross-section is given by

$$M = \int_{-\infty}^{\infty} C \, dx, \qquad (2.3)$$

and if the concentration distribution is that of expression (2.1) we see, on writing

$$x^2/4Dt = \xi^2, \quad dx = 2(Dt)^{\frac{1}{2}} d\xi, \qquad (2.4)$$

that

$$M = 2AD^{\frac{1}{2}} \int_{-\infty}^{\infty} \exp(-\xi^2) d\xi = 2A(\pi D)^{\frac{1}{2}}. \qquad (2.5)$$

Expression (2.5) shows that the amount of substance diffusing remains constant and equal to the amount originally deposited in the plane $x = 0$. Thus, on substituting for $A$ from (2.5) in eqn (2.1), we obtain

$$C = \frac{M}{2(\pi Dt)^{\frac{1}{2}}} \exp(-x^2/4Dt), \qquad (2.6)$$

and this is therefore the solution which describes the spreading by diffusion of an amount of substance $M$ deposited at time $t = 0$ in the plane $x = 0$. Fig. 2.1 shows typical distributions at three successive times.

[图片: |x|C/M (1/16)|C/M (1/2)|C/M (1)| |:---:|:---:|:---:|:---:| |-4|0.0|0.0|0.0| |-3|0.0|0.0|0.0| |-2|0.0|0.0|0.125| |-1|0.0|0.25|0.25| |0|1.125|0.5|0.25| |1|0.0|0.25|0.25| |2|0.0|0.0|0.125| |3|0.0|0.0|0.0| |4|0.0|0.0|0.0| |5|0.0|0.0|0.0|]
# FIG. 2.1. Concentration-distance curves for an instantaneous plane source. Numbers on curves are values of Dt.

# 2.2.2. Reflection at a boundary

Expression (2.6) can be used to build up solutions of other problems in linear flow by introducing the concept of reflection at a boundary. Thus, in

DIFFUSION COEFFICIENT IS CONSTANT

13

the problem just considered, half the diffusing substance moves in the direction of positive x and the other half along negative x. If, however, we have a semi-infinite cylinder extending over the region x > 0 and with an impermeable boundary at x = 0, all the diffusion occurs in the direction of positive x. We can consider the solution for negative x to be reflected in the plane x = 0 and superposed on the original distribution in the region x > 0. Since the original solution was symmetrical about x = 0 the concentration distribution for the semi-infinite cylinder is given by

$$C = \frac{M}{(\pi Dt)^{\frac{1}{2}}} \exp(-x^2/4Dt). \qquad (2.7)$$

This procedure of reflection and superposition is mathematically sound, for reflection at $x = 0$ means the adding of two solutions of the diffusion equation. Since this equation is linear the sum of the two solutions is itself a solution, and we see that (2.7) satisfies the condition that the total amount of diffusing substance remains constant at $M$. Furthermore, the condition to be satisfied at the impermeable boundary is

$$ \partial C/\partial x = 0, \qquad x = 0, \qquad (2.8) $$

since this is the mathematical condition for zero flow across a boundary. As $\partial C/\partial x$ is zero at $x = 0$ in the original solution (2.6), it is clearly still zero after reflection and superposition.

# 2.2.3. Extended initial distributions

So far we have considered only cases in which all the diffusing substance is concentrated initially in a plane. More frequently in practice, however, the initial distribution occupies a finite region and we have an initial state such as that defined by

$$C = C_0, \quad x < 0, \quad C = 0, \quad x > 0, \quad t = 0. \quad (2.9)$$

This is the initial distribution, for example, when a long column of clear water rests on a long column of solution, or when two long metal bars are placed in contact end to end. The solution to such a problem is readily deduced by considering the extended distribution to be composed of an infinite number of line sources and by superposing the corresponding infinite number of elementary solutions. With reference to Fig. 2.2, consider the diffusing substance in an element of width $\delta\xi$ to be a line source of strength $C_0\delta\xi$. Then, from (2.6) the concentration at point P, distance $\xi$ from the element, at time t is

$$ \frac{C_0\delta\xi}{2(\pi Dt)^{\frac{1}{2}}}\exp(-\xi^2/4Dt), $$

and the complete solution due to the initial distribution (2.9) is given by

14

METHODS OF SOLUTION WHEN THE

summing over successive elements $\delta\xi$, i.e. by

$$ C(x, t) = \frac{C_0}{2(\pi Dt)^{\frac{1}{2}}} \int_x^\infty \exp(-\xi^2/4Dt) d\xi = \frac{C_0}{\pi^{\frac{1}{2}}} \int_{x/2\sqrt{Dt}}^\infty \exp(-\eta^2) d\eta, \quad (2.10) $$

where $\eta = \xi/2\sqrt{Dt}$.

[图片: 1CC85Px=0]
# FIG. 2.2. Extended initial distribution.

A standard mathematical function, of which extensive tables are available, is the error function, usually written as erf z, where

$$ \operatorname{erf} z = \frac{2}{\pi^{\frac{1}{2}}} \int_{0}^{z} \exp(-\eta^2) d\eta. \qquad (2.11) $$

This function has the properties

$$ \operatorname{erf}(-z) = -\operatorname{erf}z, \quad \operatorname{erf}(0) = 0, \quad \operatorname{erf}(\infty) = 1, \qquad (2.12) $$

and hence, since

$$ \begin{aligned} \frac{2}{\pi^{\frac{1}{2}}} \int_{z}^{\infty} \exp(-\eta^2) d\eta &= \frac{2}{\pi^{\frac{1}{2}}} \int_{0}^{\infty} \exp(-\eta^2) d\eta - \frac{2}{\pi^{\frac{1}{2}}} \int_{0}^{z} \exp(-\eta^2) d\eta \\ &= 1 - \operatorname{erf} z = \operatorname{erfc} z, \end{aligned} \quad (2.13) $$

where erfc is referred to as the error-function complement, the solution (2.10) of the diffusion problem is usually written in the form

$$ C(x, t) = \frac{1}{2} C_0 \operatorname{erfc} \frac{x}{2\sqrt{ (Dt)}} . \qquad (2.14) $$

Convenient tables of the error function are those of the Works Project Association (1941) and shorter tables are to be found, for example, in Milne-Thomson and Comrie (1944). Table 2.1, taken from Carswal and Jaeger (1959), is sufficient for many practical purposes. The form of the concentration distribution is shown in Fig. 2.3. It is clear from (2.14) that $C = \frac{1}{2}C_0$ at $x = 0$ for all $t > 0$.

The error function therefore enters into the solution of a diffusion problem as a consequence of summing the effect of a series of line sources, each yielding an exponential type of distribution.

DIFFUSION COEFFICIENT IS CONSTANT

15

[图片: |x/(4Dt)^(1/2)|C/C₀| |:---:|:---:| |-2|1.0| |-1|0.95| |0|0.5| |1|0.16| |2|0.0|]
# FIG. 2.3. Concentration-distance curve for an extended source of infinite extent.

In the same way, we can study the diffusion of a substance initially confined in the region $-h < x < +h$ as in Fig. 2.4. Here the integration is from $x-h$ to $x+h$ instead of from $x$ to ∞ as in (2.10), leading immediately to the result

$$ C = \frac{1}{2} C_0 \left\{ \operatorname{erf} \frac{h-x}{2\sqrt{(Dt)}} + \operatorname{erf} \frac{h+x}{2\sqrt{(Dt)}} \right\}. \quad (2.15) $$

The concentration distribution at successive times is shown in Fig. 2.4. It is clear that the system can be cut in half by a plane at $x = 0$ without affecting

[图片: |x/h|C/C₀ (曲线1)|C/C₀ (曲线2)| |:---:|:---:|:---:| |-4|0.1|0.1| |-3|0.05|0.15| |-2|0.01|0.2| |-1|0.5|0.25| |0|1.0|0.25| |1|0.5|0.25| |2|0.01|0.2| |3|0.05|0.15| |4|0.1|0.1|]
# FIG. 2.4. Concentration-distance curves for an extended source of limited extent. Numbers on curves are values of $(Dt/h^2)^\ddagger$.

16

METHODS OF SOLUTION WHEN THE

the distribution, which is symmetrical about $x = 0$. Therefore expression (2.15) also gives the distribution in a semi-infinite system. Such a system is realized in practice in the classical experiment in which a cylinder contains a layer of solution having on top of it an infinitely-long column of water, initially clear. In practice, this means that concentration changes do not reach the top of the column during the time of the experiment.

# 2.2.4. Finite systems

If the column of water, referred to above, is of finite length $l$, the condition that the concentration tends to zero as $x$ approaches infinity is to be replaced by the condition that there is no flow of diffusing substance through the top surface, i.e.

$$ \partial C/\partial x = 0, \quad x = l. \qquad (2.16) $$

We have seen that this condition is satisfied if the concentration curve is considered to be reflected at the boundary and the reflected curve superposed on the original one. In the finite system we are considering now, the curve reflected at $x = l$ is reflected again at $x = 0$, and then at $x = l$, and so on, the result of each successive reflection being superposed on the original curve (2.15). Since the original solution is the sum of two error functions, the complete expression for the concentration in the finite system is an infinite series of error functions or error-function complements so that

$$ \begin{aligned}C={}&\frac{1}{2} C_0\left\{\operatorname{erfc}\frac{x-h}{2\sqrt{(Dt)}}-\operatorname{erfc}\frac{x+h}{2\sqrt{(Dt)}}+\operatorname{erfc}\frac{2l-h-x}{2\sqrt{(Dt)}}\right.\\&\left.-\operatorname{erfc}\frac{2l+h-x}{2\sqrt{(Dt)}}+\operatorname{erfc}\frac{2l-h+x}{2\sqrt{(Dt)}}-\operatorname{erfc}\frac{2l+h+x}{2\sqrt{(Dt)}}\right.\\&\left.+\operatorname{erfc}\frac{4l-h-x}{2\sqrt{(Dt)}}-\operatorname{erfc}\frac{4l-x+h}{2\sqrt{(Dt)}}+\dots\right\}\\={}&\frac{1}{2} C_0\sum_{n=-\infty}^{\infty}\left\{\operatorname{erf}\frac{h+2nl-x}{2\sqrt{(Dt)}}+\operatorname{erf}\frac{h-2nl+x}{2\sqrt{(Dt)}}\right\}.\end{aligned}\qquad(2.17) $$

A solution of this kind can be obtained for most problems in diffusion by use of the Laplace transform, to be discussed in § 2.4 (p. 19), or otherwise. Such solutions are most useful for calculating the concentration distribution in the early stages of diffusion, for then the series converges rapidly and two or three terms give sufficient accuracy for most practical purposes.

In all cases the successive terms in the series can be regarded as arising from successive reflections at the boundaries. The nature of the reflection depends on the condition to be satisfied. For the impermeable boundary already considered a simple reflection ensures that $\partial C/\partial x = 0$ as required. Another boundary condition which occurs frequently is of the type $C = 0$,

DIFFUSION COEFFICIENT IS CONSTANT

17

in which case it is necessary to change the sign of the concentration when it is reflected at the boundary. A further example of the use of this method is given by Jost (1952). For more complicated problems, however, the reflection and superposition method soon becomes unwieldy and results are more readily obtained by other methods.

# 2.3. Method of separation of variables

A standard method of obtaining a solution of a partial differential equation is to assume that the variables are separable. Thus we may attempt to find a solution of (2.2) by putting

$$C = X(x)T(t), \quad (2.18)$$

where $X$ and $T$ are functions of $x$ and $t$ respectively. Substitution in (2.2) yields

$$ X \frac{dT}{dt} = DT \frac{d^2 X}{dx^2}, $$

which may be rewritten

$$ \frac{1}{T} \frac{dT}{dt} = \frac{D}{X} \frac{d^2 X}{dx^2}, \qquad (2.19) $$

so that we have on the left-hand side an expression depending on $t$ only, while the right-hand side depends on $x$ only. Both sides therefore must be equal to the same constant which, for the sake of the subsequent algebra, is conveniently taken as $-\lambda^2 D$. We have, therefore, two ordinary differential equations

$$ \frac{1}{T} \frac{dT}{dt} = -\lambda^2 D, \qquad (2.20) $$

and

$$ \frac{1}{X} \frac{d^2 X}{dx^2} = -\lambda^2, \qquad (2.21) $$

of which solutions are

$$ T = e^{-\lambda^2 Dt}, \qquad (2.22) $$

and

$$ X = A \sin \lambda x + B \cos \lambda x, \qquad (2.23) $$

leading to a solution of (2.2) of the form

$$ C = (A \sin \lambda x + B \cos \lambda x) \exp(-\lambda^2 Dt), \quad (2.24) $$

18

METHODS OF SOLUTION WHEN THE

where $A$ and $B$ are constants of integration. Since (2.2) is a linear equation, the most general solution is obtained by summing solutions of type (2.24), so that we have

$$ C = \sum_{m=1}^{\infty} (A_m \sin \lambda_m x + B_m \cos \lambda_m x) \exp(-\lambda_m^2 Dt), \quad (2.25) $$

where $A_m$, $B_m$, and $\lambda_m$ are determined by the initial and boundary conditions for any particular problem. Thus if we are interested in diffusion out of a plane sheet of thickness $l$, through which the diffusing substance is initially uniformly distributed and the surfaces of which are kept at zero concentration, the conditions are

$$ C = C_0, \quad 0 < x < l, \quad t = 0 \quad (2.26) $$

$$C = 0, \quad x = 0, \quad x = l, \quad t > 0. \qquad (2.27)$$

The boundary conditions (2.27) demand that.

$$ B_m = 0, \quad \lambda_m = m\pi/l, \qquad (2.28) $$

and hence the initial condition (2.26) becomes

$$ C_0 = \sum_{1}^{\infty} A_m \sin(m\pi x/l), \quad 0 < x < l. \qquad (2.29) $$

By multiplying both sides of (2.29) by $\sin (p\pi x/l)$ and integrating from 0 to $l$ using the relationships

$$ \int_{0}^{l} \sin \frac{p\pi x}{l} \sin \frac{m\pi x}{l} dx = \begin{cases} 0, & m \neq p, \\ \frac{1}{2}l, & m = p, \end{cases} \quad (2.30) $$

we find that terms for which $m$ is even vanish, and

$$ A_m = 4C_0/m\pi, \quad m = 1, 3, 5, \dots $$

The final solution is therefore

$$ C = \frac{4C_0}{\pi} \sum_{n=0}^{\infty} \frac{1}{2n+1} \exp \left\{ -D(2n+1)^2 \pi^2 t/l^2 \right\} \sin \frac{(2n+1)\pi x}{l}, \quad (2.31) $$

where $2n + 1$ has been substituted for $m$ for convenience so that $n$ takes values 0, 1, 2, ... . This trigonometrical-series type of solution converges satisfactorily for moderate and large times, and it is then used for numerical evaluation in preference to the error-function type of solution discussed earlier in § 2.2.4 (p. 16).

In (2.29) the initial distribution is expressed as a sum of sine functions. This reveals the physical significance of the trigonometrical series in (2.31), each term of which corresponds to a term in the Fourier series (2.29) by which the initial distribution can be represented.

DIFFUSION COEFFICIENT IS CONSTANT

19

# 2.4. Method of the Laplace transform

The Laplace transformation is a mathematical device which is useful for the solution of various problems in mathematical physics. Application of the Laplace transform to the diffusion equation removes the time variable, leaving an ordinary differential equation the solution of which yields the transform of the concentration as a function of the space variables $x, y, z$. This is then interpreted, according to certain rules, to give an expression for the concentration in terms of $x, y, z$ and time, satisfying the initial and boundary condition. Historically the method may be regarded as derived from the operational methods introduced by Heaviside. Full accounts of the Laplace transform and its application have been given by Carslaw and Jaeger (1941), Churchill (1944), and others. Shorter accounts by Jaeger (1949) and Tranter (1951) are also available. Here we shall deal only with its application to the diffusion equation, the aim being to describe rather than to justify the procedure.

The solution of many problems in diffusion by this method calls for no mathematics beyond ordinary caiculus. No attempt is made here to explain its application to the more difficult problems for which the theory of functions of a complex variable must be used, though solutions to problems of this kind are quoted in later chapters. The fuller accounts should be consulted for the derivation of such solutions.

## 2.4.1. Definition of the Laplace transform

Suppose $f(t)$ to be a known function of $t$ for positive values of $t$. Then the Laplace transform $\bar{f}(p)$ of $f(t)$ is defined as

$$ \bar{f}(p) = \int_{0}^{\infty} e^{-pt} f(t) dt, \qquad (2.32) $$

where $p$ is a number sufficiently large to make the integral (2.32) converge. It may be a complex number whose real part is sufficiently large, but in the present discussion it suffices to think of it simply as a real positive number. For example, if $f(t) = e^{2t}$, $p$ must exceed 2. Unless it is necessary to emphasize that $\tilde{f}$ is a function of $p$, just as $f$ is a function of $t$, we shall usually denote the Laplace transform of $f$ by $\tilde{f}$.

Laplace transforms of common functions are readily constructed by carrying out the integration in (2.32) as in the following examples:

$$ f(t) = 1, \quad \bar{f}(p) = \int_{0}^{\infty} e^{-pt} dt = 1/p, \qquad (2.33) $$

$$ f(t) = e^{at}, \quad \bar{f}(p) = \int_{0}^{\infty} e^{-pt} e^{at} dt = \int_{0}^{\infty} e^{-(p-a)t} dt = \frac{1}{p-a}, \quad (2.34) $$

$$f(t) = \sin \omega t, \quad \bar{f}(p) = \int_{0}^{\infty} e^{-pt} \sin \omega t dt = \frac{\omega}{p^2 + \omega^2}. \qquad (2.35)$$

20

METHODS OF SOLUTION WHEN THE

Extensive tables or dictionaries of Laplace transforms are available, some in the works referred to above. A short table of transforms occurring frequently in diffusion problems is reproduced from Carslaw and Jaeger's book (1959) in Table 2.2.

# 2.4.2. Semi-infinite medium

As an example of the application of the Laplace transform, consider the problem of diffusion in a semi-infinite medium, $x > 0$, when the boundary is kept at a constant concentration $C_0$, the initial concentration being zero throughout the medium. We need a solution of

$$ \frac{\partial C}{\partial t} = D \frac{\partial^2 C}{\partial x^2}, \qquad (2.36) $$

satisfying the boundary condition

$$ C = C_0, \quad x = 0, \quad t > 0, \quad (2.37) $$

and the initial condition

$$C = 0, \quad x > 0, \quad t = 0. \qquad (2.38)$$

On multiplying both sides of (2.36) by $e^{-pt}$ and integrating with respect to $t$ from 0 to ∞ we obtain

$$ \int_{0}^{\infty} e^{-pt} \frac{\partial^2 C}{\partial x^2} dt - \frac{1}{D} \int_{0}^{\infty} e^{-pt} \frac{\partial C}{\partial t} dt = 0. \quad (2.39) $$

If we assume that the orders of differentiation and integration can be interchanged, and this can be justified for the functions in which we are interested, then

$$ \int_0^\infty e^{-pt} \frac{\partial^2 C}{\partial x^2} dt = \frac{\partial^2 C}{\partial x^2} \int_0^\infty C e^{-pt} dt = \frac{\partial^2 \bar{C}}{\partial x^2}. \quad (2.40) $$

Also, integrating by parts, we have

$$ \int_0^\infty e^{-pt} \frac{\partial C}{\partial t} dt = [C e^{-pt}]_0^\infty + p \int_0^\infty C e^{-pt} dt = p \bar{C}, \quad (2.41) $$

since the term in the square bracket vanishes at $t = 0$ by virtue of the initial condition (2.38) and at $t = \infty$ through the exponential factor. Thus (2.36) reduces to

$$ D \frac{\partial^2 \bar{C}}{\partial x^2} = p \bar{C}. \qquad (2.42) $$

By treating the boundary condition (2.37) in the same way we obtain:

$$ \bar{C} = \int_{0}^{\infty} C_{0} e^{-pt} dt = \frac{C_{0}}{p}, \quad x = 0. \qquad (2.43) $$

DIFFUSION COEFFICIENT IS CONSTANT

21

Thus the Laplace transform reduces the partial differential equation (2.36) to the ordinary differential equation (2.42). The solution of (2.42) satisfying (2.43), and for which $\bar{C}$ remains finite as $x$ approaches infinity is

$$ \bar{C} = \frac{C_0}{p} e^{-qx}, \quad (2.44) $$

where $q^2 = p/D$. Reference to Table 2.2, item 8, shows that the function whose transform is given by (2.44) is

$$ C = C_0 \operatorname{erfc} \frac{x}{2\sqrt{(Dt)}}, \qquad (2.45) $$

where, as before,

$$ \operatorname{erfc} z = 1 - \operatorname{erf} z. \qquad (2.46) $$

It is easy to verify that (2.45) satisfies (2.36), (2.37), and (2.38) and that it is therefore the required solution of the diffusion problem.

# 2.4.3. Plane sheet

In the problem just considered the transform solution could be interpreted immediately by reference to the table of transforms. Consider now, as an example of a slightly more difficult problem in which this is not so, a plane sheet of thickness $2l$, whose surface are maintained at constant concentration $C_0$, and with zero concentration of diffusing substance throughout the sheet initially. Let the sheet occupy the region $-l \le x \le l$, so that there is symmetry about $x = 0$ and the boundary conditions may be written

$$ C = C_0, \quad x = l, \quad t \ge 0, \qquad (2.47) $$

$$ \partial C/\partial x = 0, \quad x = 0, \quad t \ge 0. \qquad (2.48) $$

Eqn (2.48) expresses the condition that there is no diffusion across the central plane of the sheet. It is often more convenient to use this condition and to consider only half the sheet, $0 \le x \le l$, instead of using the condition $C = C_0$, $x = -l$.

The equations for the Laplace transform $\bar{C}$ are

$$ \frac{d^2 \bar{C}}{dx^2} - q^2 \bar{C} = 0, \quad 0 < x < l, \qquad (2.49) $$

with

$$ d\bar{C}/dx = 0, \quad x = 0, \qquad (2.50) $$

and

$$ \bar{C} = C_0/p, \quad x = l, \qquad (2.51) $$

22

METHODS OF SOLUTION WHEN THE

where $q^2 = p/D$ as before. The solution of these is

$$ \bar{C} = \frac{C_0 \cosh qx}{p \cosh ql}. \qquad (2.52) $$

There are two methods of dealing with this transform solution, leading to the two standard types of solution we have already met. We shall first obtain a solution useful for small values of the time.

(i) Expansion in negative exponentials. We express the hyperbolic functions in (2.52) in terms of negative exponentials and expand in a series by the binomial theorem. Thus we obtain from (2.52),

$$ \begin{aligned} \bar{C} &= \frac{C_0(e^{qx} + e^{-qx})}{p e^{ql}(1 + e^{-2ql})} = \frac{C_0}{p} \{ e^{-q(l-x)} + e^{-q(l+x)} \} \sum_{n=0}^{\infty} (-1)^n e^{-2nql} \\ &= \frac{C_0}{p} \sum_{n=0}^{\infty} (-1)^n e^{-q((2n+1)l-x)} + \frac{C_0}{p} \sum_{n=0}^{\infty} (-1)^n e^{-q((2n+1)l+x)}. \end{aligned} \quad (2.53) $$

Thus, using item 8 of the table of transforms (Table 2.2), we obtain:

$$ C = C_0 \sum_{n=0}^{\infty} (-1)^n \operatorname{erfc} \frac{(2n+1)l-x}{2\sqrt{(Dt)}} + C_0 \sum_{n=0}^{\infty} (-1)^n \operatorname{erfc} \frac{(2n+1)l+x}{2\sqrt{(Dt)}}. \quad (2.54) $$

This is a series of error functions such as we obtained by the method of reflection and superposition. Successive terms are in fact the concentrations at depths $l-x$, $l+x$, $3l-x$, $3l+x$, ... in the semi-infinite medium. The series converges quite rapidly for all except large values of $Dt/l^2$. For example, we have for the concentration at the centre of the sheet ($x = 0$) when $Dt/l^2 = 1$

$$ C/C_0 = 0.9590 - 0.0678 + 0.0008 = 0.8920, \quad (2.55) $$

and when $Dt/l^2 = 0.25$

$$ C/C_0 = 0.3146 - 0.0001 = 0.3145. \qquad (2.56) $$

(ii) Expression in partial fractions. It can be shown that if a transform $\bar{y}$ has the form

$$ \bar{y} = \frac{f(p)}{g(p)}, \quad (2.57) $$

where $f(p)$ and $g(p)$ are polynomials in $p$ which have no common factor, the degree of $f(p)$ being lower than that of $g(p)$, and if

$$ g(p) = (p - a_1)(p - a_2) \dots (p - a_n), \quad (2.58) $$

where $a_1, a_2, \dots, a_n$ are constants which may be real or complex but must all

DIFFUSION COEFFICIENT IS CONSTANT

23

be different, then the function $y(t)$ whose transform is $\bar{y}(p)$ is given by

$$ y(t) = \sum_{r=1}^{n} \frac{f(a_r)}{g'(a_r)} e^{a_r t}. \quad (2.59) $$

Here $g'(a_r)$ denotes the value of $dg(p)/dp$ when $p = a_r$. A proof of this by Jaeger (1949) is reproduced in the Appendix to this chapter. It is derived by expressing (2.57) in partial fractions. Since the hyperbolic functions $\cosh z$ and $\sinh z$ can be represented by the following infinite products (see, e.g. Carslaw (1909, p. 275))

$$ \cosh z = \left(1 + \frac{4z^2}{\pi^2}\right) \left(1 + \frac{4z^2}{3^2\pi^2}\right) \left(1 + \frac{4z^2}{5^2\pi^2}\right) \dots, \quad (2.60) $$

$$ \sinh z = z \left(1 + \frac{z^2}{\pi^2}\right) \left(1 + \frac{z^2}{2^2\pi^2}\right) \left(1 + \frac{z^2}{3^2\pi^2}\right) \dots \quad (2.61) $$

a quotient of these functions such as in (2.52) may still be regarded as being of the type (2.57) except that now $f(p)$ and $g(p)$ have an infinite number of factors. The $a_1, a_2, \dots$ are the zeros of $g(p)$, i.e. solutions of the equation, $g(p) = 0$, and if these are all different it is plausible to assume that (2.59) still holds with $n = \infty$. The justification of this assumption involves the theory of functions of a complex variable in order to carry out a contour integration and is to be found in the fuller accounts of the subject. There is, in fact, a rigorous mathematical argument by which the use of (2.59) with $n = \infty$, can be justified in diffusion problems in a finite region only. It must not be applied to (2.44), for example, for the semi-infinite region. The above refers to $a_1, a_2, \dots$ all different. The extension of (2.59) to cases in which $g(p)$ has repeated zeros, e.g. one of its factors is square, is given in the Appendix. Its application to an infinite number of factors is still justifiable.

We may now consider the application of (2.59) to (2.52). First the zeros of the denominator must be found. Clearly, $p = 0$ is a zero, and the other zeros are given by the values of $q$ for which $\cosh q = 0$, i.e.

$$ q = \pm \frac{(2n+1)\pi i}{2l}, \quad n = 0, 1, 2, \dots \qquad (2.62) $$

and hence

$$ p = - \frac{D(2n + 1)^2 \pi^2}{4l^2}, \quad n = 0, 1, 2, \dots. \quad (2.63) $$

To apply (2.59) to (2.52) we need

$$g'(p) = \frac{d}{dp}(p \cosh ql) = \cosh ql + \frac{1}{2}ql \sinh ql. \quad (2.64)$$

24

METHODS OF SOLUTION WHEN THE

For the zero $p = 0$, $g'(p) = 1$. For the other zeros, given by (2.62) and (2.63), $\cosh ql = 0$, and

$$\sinh ql = \sinh \frac{(2n+1)\pi i}{2} = i \sin \frac{(2n+1)\pi}{2} = i(-1)^n, \quad (2.65)$$

so that for these zeros, by substituting in (2.64) we obtain

$$ g'(p) = \frac{(2n+1)\pi(-1)^{n+1}}{4}. \quad (2.66) $$

Hence finally by inserting the zeros into (2.59) we obtain:

$$ C = C_0 - \frac{4C_0}{\pi} \sum_{n=0}^{\infty} \frac{(-1)^n}{2n+1} \exp\{-D(2n+1)^2\pi^2t/4l^2\} \cos\frac{(2n+1)\pi x}{2l}. \quad (2.67) $$

This is the trigonometrical-series type of solution obtained previously by the method of separation of the variables. The series converges rapidly for large values of $t$. Thus for the concentration at the centre of the sheet ($x = 0$) when $Dt/l^2 = 1$,

$$ C/C_0 = 1 - 0.1080 = 0.8920, \quad (2.68) $$

and when $Dt/l^2 = 0.25$

$$ C/C_0 = 1 - 0.6872 + 0.0017 = 0.3145. \quad (2.69) $$

# 2.5. Solutions in two and three dimensions

2.5.1. Solutions expressed as the product of the solutions of simpler problems

Consider the equation of diffusion

$$ \frac{\partial^2 c}{\partial x_1^2} + \frac{\partial^2 c}{\partial x_2^2} + \frac{\partial^2 c}{\partial x_3^2} = \frac{1}{D} \frac{\partial c}{\partial t}, \quad (2.70) $$

in the rectangular parallelepiped.

$$ a_1 < x_1 < b_1, \quad a_2 < x_2 < b_2, \quad a_3 < x_3 < b_3. \qquad (2.71) $$

For certain types of initial and boundary conditions, the solution of (2.70) is the product of the solutions of the three one-variable problems, and thus can be written down immediately if these are known. The following proof is given by Carslaw and Jaeger (1959, p. 33).

Suppose $c_r(x_r, t)$, $r = 1, 2, 3$, is the solution of

$$ \frac{\partial^2 c_r}{\partial x_r^2} = \frac{1}{D} \frac{\partial c_r}{\partial t}, \quad a_r < x_r < b_r, \qquad (2.72) $$

DIFFUSION COEFFICIENT IS CONSTANT

25

with boundary conditions

$$ \alpha_r \frac{\hat{c} c_r}{\hat{c} x_r} - \beta_r c_r = 0, \quad x_r = a_r, \quad t > 0, \qquad (2.73) $$

$$ \alpha'_{r} \frac{\partial c_{r}}{\partial x_{r}} + \beta'_{r} c_{r} = 0, \quad x_{r} = b_{r}, \quad t > 0, \quad (2.74) $$

where the $\alpha_r$ and $\beta_r$ are constants, either of which may be zero (so that the cases of zero surface concentration and no flow of heat at the surface are included) and with initial conditions

$$ c_r(x_r, t) = C_r(x_r), \quad t = 0, \quad a_r < x_r < b_r. \quad (2.75) $$

Then the solution of (2.70) in the region defined by (2.71) with

$$ c = C_1(x_1)C_2(x_2)C_3(x_3), \quad t = 0, \quad (2.76) $$

and with boundary conditions

$$ \alpha_r \frac{\partial c}{\partial x_r} - \beta_r c = 0, \quad x_r = a_r, \quad t > 0, \ r = 1, 2, 3, \quad (2.77) $$

$$ \alpha'_{r} \frac{\partial c}{\partial x_{r}} - \beta'_{r} c = 0, \quad x_{r} = b_{r}, \quad t > 0, \quad r = 1, 2, 3, \dots \quad (2.78) $$

is

$$ c = c_1(x_1, t)c_2(x_2, t)c_3(x_3, t). \quad (2.79) $$

For substituting (2.79) in (2.70) gives

$$ c_2 c_3 \frac{\partial^2 c_1}{\partial x_1^2} + c_3 c_1 \frac{\partial^2 c_2}{\partial x_2^2} + c_1 c_2 \frac{\partial^2 c_3}{\partial x_3^2} - \frac{1}{D} \left( c_2 c_3 \frac{\partial c_1}{\partial t} + c_3 c_1 \frac{\partial c_2}{\partial t} + c_1 c_2 \frac{\partial c_3}{\partial t} \right) = 0, \qquad (2.80) $$

using (2.72). Clearly the initial and boundary conditions (2.76), (2.77), and (2.78) are satisfied.

An essential condition is (2.76), namely that the initial condition must be expressible as a product of the initial conditions for the one-variable problems taken separately. Carslaw and Jaeger (1959) give solutions for a rectangular corner, rectangles, parallelepipeds, cylinders and some examples of isotherms are shown graphically.

# 2.5.2. A general relationship

Goldenberg (1963) derived a much more general relationship between the transient solutions of two-dimensional problems for an infinite cylinder of arbitrary cross-section, and the transient solutions of the corresponding three-dimensional problems in finite cylinders. The boundary conditions

26

METHODS OF SOLUTION WHEN THE

on the end faces of the cylinder may be of the type describing constant concentration, constant flux, or evaporation, and heat may be generated at a rate independent of time and the axial coordinate.

An example of Goldenberg's relationships is afforded by the homogeneous slab, bounded by the planes $z = 0$ and $z = l$, with heat produced in the cylindrical region $R$ of arbitrary cross-section for time $t > 0$, at the constant rate $A$ per unit time per unit volume.

The slab is initially at zero temperature with its faces maintained at zero temperature for $t > 0$. The corresponding two-dimensional problem is obtained when the thickness $l$ of the slab is infinite and the solution is independent of $z$. Goldenberg (1963) shows that the solution $V(x, y, z, t)$ for the finite slab is related to $f(x, y, t)$ for the infinite slab by the expression

$$V = \frac{4}{\pi} \sum_{n=0}^{\infty} \frac{\sin \{(2n+1)\pi z/l\}}{2n+1} \left\{ e^{-\delta t} f + \delta \int_{0}^{t} e^{-\delta t} f \, dt \right\}, \quad (2.81)$$

where $\delta = D\pi^2(2n+1)^2/l^2$ and $D$ is the diffusion coefficient.

The same relationship is valid for a hollow cylinder of arbitrary cross-section and for the region external to a cylinder of arbitrary cross-section. Similar relationships hold in other situations discussed by Goldenberg.

## 2.6. Other solutions

Langford (1967) obtained new solutions of the one-dimensional heat equation for temperature and heat flux both prescribed at the same fixed boundary. They take the form of series of polynomial and quasi-polynomial solutions for plane sheets, cylinders, and spheres. They include as special cases some of the old or classical solutions. They also have applications to phase change problems with boundaries moving at a constant velocity.

# APPENDIX TO CHAPTER 2

To deduce the function $y(t)$ whose Laplace transform $\bar{y}(p)$ is given by

$$ \bar{y}(p) = \frac{f(p)}{g(p)}, \quad (1) $$

we first put $\bar{y}(p)$ into partial fractions in the usual way by assuming

$$ \frac{f(p)}{g(p)} = \sum_{r=1}^{n} \frac{A_r}{p-a_r} = \frac{A_1}{p-a_1} + \frac{A_2}{p-a_2} + \frac{A_3}{p-a_3} + \dots + \frac{A_n}{p-a_n}. \quad (2) $$

Then

$$ f(p) \equiv \sum_{r=1}^{n} A_r(p-a_1) \dots (p-a_{r-1})(p-a_{r+1}) \dots (p-a_n), \quad (3) $$

DIFFUSION COEFFICIENT IS CONSTANT

27

and putting $p = a_r$ in this gives

$$ f(a_r) = A_r(a_r - a_1) \dots (a_r - a_{r-1})(a_r - a_{r+1}) \dots (a_r - a_n) \quad (r = 1, 2, \dots, n). \quad (4) $$

Substituting for $A_r$ from (4) in (2) gives

$$ \bar{y}(p) = \sum_{r=1}^{n} \frac{1}{p-a_r} \frac{f(a_r)}{(a_r-a_1)\dots(a_r-a_{r-1})(a_r-a_{r+1})\dots(a_r-a_n)}. \quad (5) $$

Now since

$$ g(p) = (p - a_1)(p - a_2) \dots (p - a_n), \quad (6) $$

we have, on differentiating by the ordinary rule for differentiation of a product,

$$g'(p) = \sum_{r=1}^{n} (p - a_1) \dots (p - a_{r-1})(p - a_{r+1}) \dots (p - a_n). \quad (7)$$

Putting $p = a_r$ in this, gives

$$ g'(a_r) = (a_r - a_1) \dots (a_r - a_{r-1})(a_r - a_{r+1}) \dots (a_r - a_n), \quad (8) $$

and using (8) in (5) gives a further form for $\bar{y}(p)$ namely:

$$ \bar{y}(p) = \sum_{r=1}^{n} \frac{f(a_r)}{(p - a_r)g'(a_r)}. \quad (9) $$

On applying item 3 of Table 2.2 to successive terms of (9) we obtain immediately

$$ y(t) = \sum_{r=1}^{n} \frac{f(a_r)}{g'(a_r)} e^{a_r t}. \quad (10) $$

This result applies only to the case in which $g(p)$ has no repeated zeros, but it can readily be generalized for the case of repeated factors. Thus (10) implies that to each linear factor $p - a$, of the denominator of $\bar{y}(p)$ there corresponds a term

$$ \frac{f(a_r)}{g'(a_r)} e^{a_r t} \quad (11) $$

in the solution. The generalization is that, to each squared factor $(p-b)^2$ of the denominator of $\bar{y}(p)$ there corresponds a term

$$ \left[ \frac{(p-b)^2 f(p)}{g(p)} \right]_{p=b} t e^{bt} + \left[ \frac{d}{dp} \left\{ \frac{(p-b)^2 f(p)}{g(p)} \right\} \right]_{p=b} e^{bt} \quad (12) $$

in the solution. To each multiple factor $(p-c)^m$ of the denominator of $\bar{y}(p)$ there corresponds a term

$$ \sum_{s=0}^{m-1} \left[ \frac{d^s}{dp^s} \left\{ \frac{(p-c)^m f(p)}{g(p)} \right\} \right]_{p=c} \frac{t^{m-s-1}}{s!(m-s-1)!} e^{ct} \quad (13) $$

in the solution.

# 3

## INFINITE AND SEMI-INFINITE MEDIA

## 3.1. Introduction

In this and the following three chapters solutions of the diffusion equation are presented for different initial and boundary conditions. In nearly all cases the diffusion coefficient is taken as constant. In many cases the solutions are readily evaluated numerically with the help of tables of standard mathematical functions. Where this is not so, and where numerical evaluation is tedious, as many graphical and tabulated solutions as space permits are given.

### 3.2. Instantaneous sources

Under this heading are included all problems in which an amount of diffusing substance is deposited within a certain restricted region at time $t = 0$ and left to diffuse throughout the surrounding medium. For example, it may be located initially at a point, or in a plane, or within a sphere, when we have an instantaneous point, plane, or spherical source as the case may be.

The solution for an instantaneous plane source in an infinite medium has already been given in Chapter 2, eqn (2.6). The corresponding solution for an instantaneous point source on an infinite plane surface is obtained in the same way by recognizing that

$$ C = \frac{A}{t} \exp \left\{ -(x^2 + y^2)/4Dt \right\} \quad (3.1) $$

is a solution of

$$ \frac{\partial^2 C}{\partial x^2} + \frac{\partial^2 C}{\partial y^2} = \frac{1}{D} \frac{\partial C}{\partial t}, \qquad (3.2) $$

which is the equation for diffusion in two dimensions when the diffusion coefficient is constant. The arbitrary constant $A$ is expressed in terms of $M$, the total amount of substance diffusing, by performing the integration

$$ M = \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} C \, dx \, dy = 4\pi DA, \quad (3.3) $$

the concentration C being expressed in this problem as the amount of diffusing substance per unit area of surface. The concentration at a distance

INFINITE AND SEMI-INFINITE MEDIA

29

r from a point source on an infinite plane surface is thus given by

$$ C = \frac{M}{4\pi Dt} \exp(-r^2/4Dt). \quad (3.4) $$

The corresponding expression for a point source in an infinite volume is

$$ C = \frac{M}{8(\pi Dt)^{\frac{1}{2}}} \exp(-r^2/4Dt). \quad (3.5) $$

By integrating the appropriate solution for a point source with respect to the relevant space variables, solutions may be obtained for line, surface, and volume sources. Thus for surface diffusion in the x, y plane due to a line source along the y-axis we have

$$ C = \int_{-\infty}^{\infty} \frac{M}{4\pi Dt} \exp \left\{ -(x^2 + y^2)/4Dt \right\} dy = \frac{M}{2(\pi Dt)^{\frac{1}{2}}} \exp(-x^2/4Dt), \quad (3.6) $$

where now $M$ is the amount of diffusing substance deposited initially per unit length of the line source. This is the same as expression (2.6) of Chapter 2 for a plane source of strength $M$ per unit area in an infinite volume. The corresponding result for a line source of strength $M$ per unit length in an infinite volume, obtained by integrating (3.5), is

$$ C = \frac{M}{4\pi Dt} \exp(-r^2/4Dt), \quad (3.7) $$

which is the same expression as (3.4) for a point source on an infinite plane surface, though $M$ has a different significance in the two cases. Results for a variety of sources are derived by Carslaw and Jaeger (1959, p. 255). The spherical and cylindrical sources are likely to be of practical interest. If the diffusing substance is initially distributed uniformly through a sphere of radius $a$, the concentration $C$ at radius $r$, and time $t$ is given by

$$C = \frac{1}{2} C_0 \left\{ \text{erf} \frac{a+r}{2\sqrt{(Dt)}} + \text{erf} \frac{a+r}{2\sqrt{(Dt)}} \right\} \\ - \frac{C_0}{r} \sqrt{\left(\frac{Dt}{\pi}\right)} [\exp\{-(a-r)^2/4Dt\} - \exp\{-(a+r)^2/4Dt\}], \quad (3.8)$$

where $C_0$ is the uniform concentration in the sphere initially. Expression (3.8) may easily be written in terms of the total amount of diffusing substance $M$, since

$$ M = \frac{4}{3}\pi a^3 C_0. \quad (3.9) $$

The corresponding result for a cylinder of radius $a$ may be written in the form

$$ C = \frac{C_0}{2Dt} \exp(-r^2/4Dt) \int_0^a \exp(-r'^2/4Dt) I_0\left(\frac{rr'}{2Dt}\right) r' dr', \quad (3.10) $$

30

INFINITE AND SEMI-INFINITE MEDIA

where $I_0$ is the modified Bessel function of the first kind of order zero. Tables of $I_0$ are available. The integral in (3.10) has to be evaluated numerically except on the axis $r = 0$, where (3.10) becomes

$$ C = C_0\{1 - \exp(-a^2/4Dt)\}. \qquad (3.11) $$

These expressions may be applied, for example, to the diffusion of a sphere or cylinder of solute into a large volume of solvent. Curves showing the concentration distribution at successive times are given in Figs. 3.1 and 3.2.

[图片: |r/a|C/C₀ (曲线 0)|C/C₀ (曲线 1)|C/C₀ (曲线 2)| |:---:|:---:|:---:|:---:| |0|1.0|0.4|0.1| |1|0.3|0.2|0.05| |2|0.0|0.0|0.0| |3|0.0|0.0|0.0| |4|0.0|0.0|0.0|]
# FIG. 3.1. Concentration distributions for a spherical source. Numbers on curves are values of $(Dt/a^2)^‡$.

[图片: |r/a|C/C₀ (曲线 0)|C/C₀ (曲线 ½)|C/C₀ (曲线 1)| |:---:|:---:|:---:|:---:| |0|1.0|0.6|0.2| |1|0.5|0.35|0.2| |2|0.0|0.1|0.05| |3|0.0|0.0|0.0| |4|0.0|0.0|0.0|]
# FIG. 3.2. Concentration distributions for a cylindrical source. Numbers on curves are values of $(Dt/a^2)^‡$.

INFINITE AND SEMI-INFINITE MEDIA

31

The expression (3.10) and the curves of Fig. 3.2 also apply to a circular disc source, of radius $a$, on an infinite plane surface, if $C_0$ denotes the uniform concentration of the diffusing substance over the region $0 < r < a$ initially. An alternative solution given by Rideal and Tadayon (1954) is

$$ C = aC_0 \int_0^\infty J_1(ua)J_0(ur) \exp(-Dtu^2) du, \quad (3.10a) $$

where $J_0$ and $J_1$ are Bessel functions of the first kind and of order zero and one respectively. Tables of $J_0$ and $J_1$ are available. Rideal and Tadayon also give an expression for the total amount of diffusing substance $Q$ remaining on the disc after time $t$, which is

$$ Q = 2\pi a^2 C_0 \int_0^\infty \frac{J_1^2(ua)}{u} \exp(-Dtu^2) du. \quad (3.10b) $$

For small values of $t$, (3.10b) becomes

$$ Q = \pi a^2 C_0 \left\{ 1 - \frac{2}{a} \left( \frac{Dt}{2\pi} \right)^{\frac{1}{2}} \right\}, \quad (3.10c) $$

and when $t$ is large we have

$$ Q = \pi a^4 C_0 / (4Dt). \quad (3.10d) $$

Cases of an extended source in an infinite medium, where the diffusing substance initially occupies the semi-infinite region $x < 0$ or is confined to the region $-h < x < h$, have been considered (see eqns (2.14) and (2.15) in Chapter 2). The solution to the corresponding problem in which the region $-h < x < h$ is at zero concentration and $|x| > h$ at a uniform concentration $C_0$ initially is

$$ C = \frac{1}{2} C_0 \left\{ \operatorname{erfc} \frac{h-x}{2\sqrt{(Dt)}} + \operatorname{erfc} \frac{h+x}{2\sqrt{(Dt)}} \right\}. \quad (3.12) $$

Knight and Philip (1973) have obtained an exact explicit solution for $D = a(1 - b^{-1}C)^{-2}$ with $a$ and $b$ positive constants and for an instantaneous distributed source at concentration $b$ and the initial concentration uniform but arbitrary away from the source. The analysis holds for infinite and semi-infinite media, and physical applications are discussed.

# 3.2.1. Continuous sources

A solution for a continuous source, from which diffusing substance is liberated continuously at a certain rate, is deduced from the solution for the corresponding instantaneous source by integrating with respect to time $t$. Thus if diffusing substance is liberated continuously from a point in an infinite volume at the rate $\phi$ per second, the concentration at a point distant $r$

32

INFINITE AND SEMI-INFINITE MEDIA

from the source at time $t$ is obtained by integrating (3.5) and is

$$C = \frac{1}{8(\pi D)^{\frac{3}{2}}} \int_{0}^{t} \phi(t') \exp\{-r^2/4D(t-t')\} \frac{dt'}{(t-t')^{\frac{3}{2}}}. \qquad (3.5a)$$

If $\phi$ is constant and equal to $q$, then

$$C = \frac{q}{4\pi Dr} \operatorname{erfc} \frac{r}{2\sqrt{(Dt)}}. \qquad (3.5b)$$

Solutions for other continuous sources are obtained similarly and examples are given by Carslaw and Jaeger (1959, p. 261).

# 3.3. Semi-infinite media

The solution for a plane source deposited initially at the surface, $x = 0$, of a semi-infinite medium was given in Chapter 2, eqn (2.7), and that for the initial distribution $C = C_0$, $0 < x < h$, $C = 0$, $x > h$, was seen to be given by eqn (2.15) for x positive.

The problem of the semi-infinite medium whose surface is maintained at a constant concentration $C_0$, and throughout which the concentration is initially zero, was handled by the method of the Laplace transform in Chapter 2, p. 21 (see eqn (2.45)). Other results of practical importance which may be obtained in the same way are given below.

(i) The concentration is $C_0$ throughout, initially, and the surface is maintained at a constant concentration $C_1$.

$$ \frac{C - C_1}{C_0 - C_1} = \operatorname{erf} \frac{x}{2\sqrt{(Dt)}} \qquad (3.13) $$

The special case of zero surface concentration is immediately obvious. The rate of loss of diffusing substance from the semi-infinite medium when the surface concentration is zero, is given by

$$ \left( D \frac{\partial C}{\partial x} \right)_{x=0} = \frac{DC_0}{\sqrt{(\pi Dt)}}, \qquad (3.14) $$

so that the total amount $M_t$ of diffusing substance which has left the medium at time $t$ is given by integrating (3.14) with respect to $t$ and is

$$M_t = 2C_0 \left( \frac{Dt}{\pi} \right)^{\frac{1}{2}} \qquad (3.15)$$

The same expression with $C_0$ replaced by $C_1$ gives the total amount taken up by the medium in time $t$ if the initial concentration $C_0$ is zero. If the initial concentration is zero throughout the semi-infinite medium, and the surface concentration varies with time, solutions are still obtainable by the Laplace

INFINITE AND SEMI-INFINITE MEDIA

33

transform. Cases of practical interest are given below. Here $M_t$ is used throughout to denote the total amount of diffusing substance which has entered the medium at time $t$.

(ii) $C_{x=0} = kt$, where $k$ is a constant.

$$ \begin{aligned} C &= kt \left[ \left( 1 + \frac{x^2}{2Dt} \right) \operatorname{erfc} \frac{x}{2\sqrt{/(Dt)}} - \frac{x}{\sqrt{(\pi Dt)}} \exp \left\{ -x^2/4Dt \right\} \right] \\ &= 4kt i^2 \operatorname{erfc} \frac{x}{2\sqrt{/(Dt)}}. \end{aligned} \quad (3.16) $$

$$ M_t = \frac{4}{3}kt \left( \frac{Dt}{\pi} \right)^{\frac{1}{2}}. \qquad (3.17) $$

The function $i^2$erfc is defined and tabulated in Table 2.1, so that values of $C$ may be written down immediately. The effect of an increasing surface concentration is shown in Fig. 3.3.

[图片: |(Dt)¹/²|MₜD¹/²/k or Mₜ/C₀| |:---:|:---:| |0.4|0.1| |0.8|0.4| |1.2|1.0| |1.6|1.8| |2.0|2.3|]
# FIG. 3.3. Sorption curves for variable and constant surface concentrations in a semi-infinite medium.

34

INFINITE AND SEMI-INFINITE MEDIA

(iii) $C_{x=0} = kt^{\frac{1}{2}}$, where $k$ is a constant.

$$ \begin{aligned} C &= kt^{\frac{1}{2}} \left\{ \exp(-x^2/4Dt) - \frac{x\pi^{\frac{1}{2}}}{2\sqrt{(Dt)}} \operatorname{erfc} \frac{x}{2\sqrt{(Dt)}} \right\} \\ &= k(\pi t)^{\frac{1}{2}} \operatorname{ierfc} \frac{x}{2\sqrt{(Dt)}}. \end{aligned} \quad (3.18) $$

$$ M_t = \frac{1}{2}kt(\pi D)^{\frac{1}{2}}. \quad (3.19) $$

The function ierfc is defined and tabulated in Table 2.1. In this case $M$ is directly proportional to $t$ and so the rate of uptake of diffusing substance is constant.

(iv) $C_{x=0} = kt^{\frac{1}{2}n}$, where $k$ is a constant and $n$ is any positive integer, even or odd.

$$ C = k\Gamma(\frac{1}{2}n + 1)(4t)^{\frac{1}{2}n} i^n \operatorname{erfc} \frac{x}{2\sqrt{ (Dt)}}. \quad (3.20) $$

$$ M^t = \frac{k}{2^n} \sqrt{(Dt)(4t)^{\frac{1}{2}n}} \frac{\Gamma(\frac{1}{2}n + 1)}{\Gamma(\frac{1}{2}n + \frac{3}{2})}. \quad (3.21) $$

The function $i^n$erfc is defined and tabulated up to $n = 6$ in Table 2.1. $\Gamma(n)$ is the gamma function defined and tabulated, for example, by Milne-Thomson and Comrie (1944). If $n$ is even, so that $\frac{1}{2}n = N$, an integer, then

$$ \Gamma(\frac{1}{2}n + 1) = \Gamma(N + 1) = N!. \qquad (3.22) $$

If $n$ is odd, so that $\frac{1}{2}n = M - \frac{1}{2}$, then

$$ \Gamma(\frac{1}{2}n + 1) = \Gamma(M + \frac{1}{2}) = 1.3.5 \dots (2M - 3)(2M - 1)\pi^{\frac{1}{2}}/2^M. \quad (3.23) $$

Other properties of gamma functions are :

$$ \Gamma(n+1) = n\Gamma(n); \quad \Gamma(\frac{1}{2}) = \pi^{\frac{1}{2}}. \qquad (3.24) $$

A polynomial in $t^{\frac{1}{2}}$ may sometimes be a useful way of representing a given surface concentration empirically. In such a case the complete expression for the concentration at any point is the sum of a number of terms of type (3.20) corresponding to successive terms in the polynomial.

(v) These solutions can be extended to cover other initial and boundary conditions by using the fact that for a linear differential equation the sum of two solutions is itself a solution. For example, if

$$ C_{x=0} = C_0 + kt \quad (3.25) $$

and the semi-infinite medium is initially at zero concentration throughout, the solution is given by

$$ C = C_0 \operatorname{erfc} \frac{x}{2\sqrt{(Dt)}} + 4kt i^2 \operatorname{erfc} \frac{x}{2\sqrt{(Dt)}}, \quad (3.26) $$

INFINITE AND SEMI-INFINITE MEDIA

35

since the first term on the right-hand side of (3.26) is the solution satisfying the conditions

$$ \left. \begin{array}{l} C = C_0, \\ C = 0, \end{array} \right. \quad x = 0 \left. \right\} \qquad (3.27) $$

and the second term satisfies

$$ \left. \begin{array}{l} C = kt, \\ C = 0, \end{array} \right. \quad x = 0 \left. \right\} \qquad (3.28) $$

In general the solution to the problem of the semi-infinite medium in which the surface concentration is given by $F(t)$ and in which the initial distribution is $f(x)$, is given by

$$ C = c_1 + c_2, \quad (3.29) $$

where $c_1$ is a solution of the diffusion equation which satisfies

$$ \left. \begin{array}{l} c_1 = 0, \\ c_1 = F(t), \end{array} \right. \quad t = 0 \left. \right\} \qquad (3.30) $$

and $c_2$ is another solution satisfying

$$ \left. \begin{array}{l} c_2 = f(x), & t = 0 \\ c_2 = 0, & x = 0 \end{array} \right\} \qquad (3.31) $$

Clearly, with $c_1$ and $c_2$ so defined, the diffusion equation and the initial and boundary conditions are satisfied. Consider, as an example, the problem of desorption from a semi-infinite medium having a uniform initial concentration $C_0$, and a surface concentration decreasing according to (3.25), with $k$ negative. The solution is

$$ C = C_0 + 4kt i^2 \operatorname{erfc} \frac{x}{2\sqrt{(Dt)}}. \qquad (3.32) $$

which is obtained by adding to (3.26) the solution satisfying:

$$ \left. \begin{array}{l} C = C_0, \\ C = 0, \end{array} \right. \quad x > 0, \quad t = 0 \left. \right\} (3.33) $$

i.e. by adding $C_0$ erf $\{x/2\sqrt{}(Dt)\}$.

# 3.3.1. Surface evaporation condition

In some cases the boundary condition relates to the rate of transfer of diffusing substance across the surface of the medium. Thus, if a stream of dry air passes over the surface of a solid containing moisture, loss of moisture occurs by surface evaporation. Similarly if the solid is initially dry and the

36

INFINITE AND SEMI-INFINITE MEDIA.

air contains water vapour, the solid takes up moisture. In each case the rate of exchange of moisture at any instant depends on the relative humidity of the air and the moisture concentration in the surface of the solid. The simplest reasonable assumption is that the rate of exchange is directly proportional to the difference between the actual concentration $C_s$ in the surface at any time and the concentration $C_0$ which would be in equilibrium with the vapour pressure in the atmosphere remote from the surface. Mathematically this means that the boundary condition at the surface is

$$ -D \frac{\partial C}{\partial x} = \alpha (C_0 - C_s), \quad x = 0, \quad (3.34) $$

where $\alpha$ is a constant of proportionality.

If the concentration in a semi-infinite medium is initially $C_2$ throughout, and the surface exchange is determined by (3.34), the solution is

$$ \frac{C - C_2}{C_0 - C_2} = \operatorname{erfc} \frac{x}{2\sqrt{(Dt)}} - \exp(hx + h^2Dt) \operatorname{erfc} \left\{ \frac{x}{2\sqrt{(Dt)}} + h\sqrt{(Dt)} \right\}, \quad (3.35) $$

where $h = \alpha/D$. The special cases of zero concentration in the medium initially ($C_2 = 0$), and evaporation into an atmosphere of zero relative humidity ($C_0 = 0$), are immediately obvious from (3.35). The rate at which the total amount $M_t$ of diffusing substance in the semi-infinite medium per unit cross-sectional area changes is given by

$$ \frac{dM_t}{dt} = - \left( D \frac{\partial C}{\partial x} \right)_{x=0} = \alpha(C_0 - C_s), \quad (3.36) $$

and, on substituting for $C_s$ the value obtained from (3.35) by putting $x = 0$, after integration with respect to $t$ we obtain for the total quantity of diffusing substance having crossed unit area of the surface,

$$ M_t = \left( \frac{C_0 - C_2}{h} \right) \left\{ \exp(h^2 Dt) \operatorname{erfc} h \sqrt{ (Dt) - 1} + \frac{2}{\pi^{\frac{1}{2}}} h \sqrt{ (Dt)} \right\} \quad (3.37) $$

If $C_0$ is greater than $C_2$ this amount is taken up by the medium; if $C_0$ is less than $C_2$ this amount is lost by evaporation from the surface. The expression (3.35) can be written in terms of any two of the dimensionless parameters

$$ \frac{x}{2\sqrt{(Dt)}}, \quad h\sqrt{(Dt)}, \quad \text{or} \quad hx. \qquad (3.38) $$

In Fig. 3.4 the ratio $(C-C_2)/(C_0-C_2)$ is plotted as a function of $x/2\sqrt{/(Dt)}$ for various values of $h\sqrt{/(Dt)}$. In order to evaluate $hM_t/(C_0-C_2)$ from (3.37), only one dimensionless parameter $h\sqrt{/(Dt)}$ is needed. The relationship is readily evaluated from standard functions and is shown graphically in

INFINITE AND SEMI-INFINITE MEDIA

37

[图片: |x/(4Dt)¹/²| (C-C₂)/(C₀-C₂) for ∞ | (C-C₂)/(C₀-C₂) for 4 | (C-C₂)/(C₀-C₂) for 2 | (C-C₂)/(C₀-C₂) for 1 | (C-C₂)/(C₀-C₂) for 1/2 | (C-C₂)/(C₀-C₂) for 1/4 | |:---:|:---:|:---:|:---:|:---:|:---:|:---:| |0.0|1.0|0.9|0.8|0.6|0.4|0.2| |0.4|0.6|0.55|0.48|0.38|0.28|0.16| |0.8|0.35|0.32|0.28|0.22|0.14|0.07| |1.2|0.18|0.16|0.14|0.11|0.07|0.04| |1.6|0.08|0.07|0.06|0.05|0.03|0.02| |2.0|0.03|0.03|0.02|0.02|0.01|0.01| |2.4|0.01|0.01|0.01|0.01|0.01|0.01|]
# FIG. 3.4. Concentration distribution for a surface evaporation condition in a semi-infinite medium. Numbers on curves are values of $h(Dt)^{\ddagger}$.

# Fig. 3.5. The evaluation for large $h\sqrt{/(Dt)}$ is made easier by using the asymptotic formula

$$ \exp(z^2) \operatorname{erfc} z = \frac{1}{\pi^{\frac{1}{2}}} \left( \frac{1}{z} - \frac{1}{2z^3} + \frac{1.3}{2^2.z^5} \cdots \right). \quad (3.39) $$

# 3.3.2. Square-root relationship

Expression (2.45) shows that the solution of the problem of diffusion into a semi-infinite medium having zero initial concentration and the surface of which is maintained constant, involves only the single dimensionless parameter

$$ \frac{x}{2\sqrt{(Dt)}} \qquad (3.40) $$

It follows from this that

(i) the distance of penetration of any given concentration is proportional to the square root of time;

(ii) the time required for any point to reach a given concentration is proportional to the square of its distance from the surface and varies inversely as the diffusion coefficient;

(iii) the amount of diffusing substance entering the medium through unit area of its surface varies as the square root of time.

38

INFINITE AND SEMI-INFINITE MEDIA

[图片: |h(Dt)¹|Mₜh(C₀-C₂)| |:---:|:---:| |0|0| |1|0.5| |2|1.5| |3|2.8| |4|4.0| |5|5.0| |6|5.8|]
# FIG. 3.5. Sorption curve for a surface evaporation condition in a semi-infinite medium.

These fundamental properties hold in general in semi-infinite media, provided the initial concentration is uniform and the surface concentration remains constant. They also hold for point and line sources on infinite surfaces or in infinite media, and also for the case of diffusion in an infinite medium where the diffusing substance is initially confined to the region $x < 0$. Clearly they do not apply to cases where parameters other than $x/2\sqrt{ (Dt)}$ are involved, such as the width of an extended source or the rate of change of surface concentration, etc.

# 3.4. The infinite composite medium

Here we consider diffusion in systems in which two media are present. Suppose the region $x > 0$ is of one substance in which the diffusion coefficient is $D_1$, and in the region $x < 0$ the diffusion coefficient is $D_2$. In the simplest case, the initial conditions are that the region $x > 0$ is at a uniform concentration $C_0$, and in $x < 0$ the concentration is zero initially. If we write $c_1$ for the concentration in $x > 0$ and $c_2$ in $x < 0$ the boundary conditions at the interface $x = 0$ may be written

$$ c_2/c_1 = k, \quad x = 0, \quad (3.41) $$

$$ D_1 \partial c_1 / \partial x = D_2 \partial c_2 / \partial x, \quad x = 0, \quad (3.42) $$

INFINITE AND SEMI-INFINITE MEDIA

39

where $k$ is the ratio of the uniform concentration in the region $x < 0$ to that in $x > 0$ when final equilibrium is attained. The condition (3.42) expresses the fact that there is no accumulation of diffusing substance at the boundary. A solution to this problem is easily obtained by combining solutions for the semi-infinite medium so as to satisfy the initial and boundary conditions. We seek solutions of the type

$$ c_1 = A_1 + B_1 \operatorname{erf} \frac{x}{2\sqrt{(D_1 t)}}, \quad x > 0, \qquad (3.43) $$

$$ c_2 = A_2 + B_2 \operatorname{erf} \frac{|x|}{2\sqrt{(D_2 t)}}, \quad x < 0, \quad (3.44) $$

which are known to satisfy the diffusion equations in the two regions. By choosing the constants $A_1, B_1, A_2, B_2$ to satisfy the initial conditions and (3.41), (3.42) we obtain

$$ c_1 = \frac{C_0}{1 + k(D_2/D_1)^{\frac{1}{2}}} \left\{ 1 + k(D_2/D_1)^{\frac{1}{2}} \operatorname{erf} \frac{x}{2\sqrt{D_1 t}} \right\}, \quad (3.45) $$

$$ c_2 = \frac{kC_0}{1 + k(D_2/D_1)^{\frac{1}{2}}} \text{erfc} \frac{|x|}{2\sqrt{(D_2 t)}}. \quad (3.46) $$

Fig. 3.6 shows a typical concentration distribution for the case where $D_2 = 4D_1$ and $k = \frac{1}{2}$. Graphs for other cases are shown by Jost (1952) and by Barrer (1951). We may note that, as diffusion proceeds, the concentrations at the interface, $x = 0$, remain constant at the values

$$ c_1 = \frac{C_0}{1 + k(D_2/D_1)^{\frac{1}{2}}}, \quad c_2 = \frac{kC_0}{1 + k(D_2/D_1)^{\frac{1}{2}}}. \qquad (3.47) $$

[图片: |x|C/C₀| |:---:|:---:| |-8|0| |-6|0| |-4|0.05| |-2|0.1| |0|0.25| |2|0.9| |4|1.0| |6|1.0|]
# FIG. 3.6. Concentration distribution in a composite medium. $D_1t = 1$, $D_2 = 4D_1$, $k = \frac{1}{2}$.

40

INFINITE AND SEMI-INFINITE MEDIA

# 3.4.1. Interface resistance

If we have the same problem as on p. 38 except that there is a contact resistance at $x = 0$, then (3.41) is to be replaced by

$$ D_1 \partial c_1 / \partial x + h(c_2 - c_1) = 0, \quad x = 0, \quad (3.48) $$

while (3.42) still holds. The expressions for the concentrations in this case are

$$ c_1 = \frac{C_0}{1 + (D_2/D_1)^{\frac{1}{2}}} \left[ 1 + \left( \frac{D_2}{D_1} \right)^{\frac{1}{2}} \left\{ \operatorname{erf} \frac{x}{2\sqrt{(D_1 t)}} + \exp(h_1 x + h_1^2 D_1 t) \operatorname{erfc} \left( \frac{x}{2\sqrt{(D_1 t)}} + h_1 \sqrt{(D_1 t)} \right) \right\} \right], \quad (3.49) $$

$$ c_2 = \frac{C_0}{1 + (D_2/D_1)^{\frac{1}{2}}} \left\{ \text{erfc} \frac{|x|}{2\sqrt{(D_2 t)}} - \exp (h_2 x + h_2^2 D_2 t) \text{erfc} \left( \frac{|x|}{2\sqrt{(D_2 t)}} + h_2 \sqrt{(D_2 t)} \right) \right\}, \quad (3.50) $$

where

$$ h_1 = \frac{h}{D_1} \{1 + (D_1/D_2)^{\frac{1}{2}}\}, \quad h_2 = \frac{h}{D_2} \{1 + (D_2/D_1)^{\frac{1}{2}}\}. \quad (3.51) $$

The concentrations on either side of the interface are no longer constant but each approaches the equilibrium value $\frac{1}{2}C_0$ relatively slowly. This, and the general distribution at successive times, is illustrated in Fig. 3.7 for the case in which $D_1 = D_2$ and $h = \frac{1}{10}D_1$.

[图片: |x|0|9|25|100| |:---:|:---:|:---:|:---:|:---:| |-40|0|0|0|0| |-30|0|0|0|0| |-20|0|0|0|0.01| |-10|0|0|0.01|0.05| |0|0.63|0.84|0.92|0.96| |10|1.0|0.98|0.96|0.84| |20|1.0|1.0|0.99|0.96| |30|1.0|1.0|1.0|0.99| |40|1.0|1.0|1.0|1.0|]
# FIG. 3.7. Concentration distribution in a composite medium with a resistance at the interface. Numbers on curves are values of $D_1t$; $D_1 = D_2$; $h = \frac{1}{10}D_1$.

INFINITE AND SEMI-INFINITE MEDIA

41

# 3.5. The semi-infinite composite medium

This is the case of a semi-infinite medium which has a skin or surface layer having diffusion properties different from those of the rest of the medium. Thus, suppose in the semi-infinite region $-1 < x < \infty$, the diffusion coefficient is $D_1$ in the region $-1 < x < 0$, and that the concentration is denoted by $c_1$ there, while the corresponding quantities in $x > 0$ are $D_2$ and $c_2$. If we assume the conditions at the interface to be

$$ c_1 = c_2, \quad x = 0, \qquad (3.52) $$

$$ D_1 \partial c_1 / \partial x = D_2 \partial c_2 / \partial x, \quad x = 0, \quad (3.53) $$

the solution to the problem of zero initial concentration and the surface $x = -l$ maintained at constant concentration $C_0$ is given by Carswak and Jaeger (1959, p. 321), and is

$$ c_1 = C_0 \sum_{n=0}^{\infty} \alpha^n \left\{ \text{erfc} \frac{(2n+1)l+x}{2\sqrt{(D_1 t)}} - \alpha \text{erfc} \frac{(2n+1)l-x}{2\sqrt{(D_1 t)}} \right\}, \quad (3.54) $$

$$ c_2 = \frac{2kC_0}{k+1} \sum_{n=0}^{\infty} \alpha^n \operatorname{erfc} \frac{(2n+1)l + kx}{2\sqrt{D_1 t}}, \quad (3.55) $$

where

$$ k = (D_1/D_2)^{\frac{1}{2}}, \quad \alpha = \frac{1-k}{1+k}. \qquad (3.56) $$

The total quantity entering the medium through unit area of the surface $x = -l$ in time $t$ is $M_t$, where $M_t$ is given by

$$ \frac{M_t}{lC_0} = 2 \left( \frac{D_1 t}{\pi l^2} \right)^{\frac{1}{2}} \left\{ 1 + 2 \sum_{n=1}^{\infty} \alpha^n \exp(-n^2 l^2 / D_1 t) \right\} - 4 \sum_{n=1}^{\infty} n \alpha^n \operatorname{erfc} \frac{nl}{\sqrt{(D_1 t)}}. \quad (3.57) $$

Following Carslaw and Jaeger (1959, p. 322), for very large times the exponentials in (3.57) may all be replaced by unity. This is true also of the error-function complements in (3.57) and so for large times we have approximately

$$ \frac{M_t}{lC_0} = 2 \left( \frac{D_1 t}{\pi l^2} \right)^{\frac{1}{2}} \left( 1 + \frac{2\alpha}{1-\alpha} \right) - \frac{4\alpha}{(1-\alpha)^2}, \quad (3.58) $$

provided $\alpha^2 < 1$. Fig. 3.8 shows $M_t/lC_0$ as a function of $(D_1t/l^2)^{\frac{1}{2}}$.

Whipple (1954) has given formulae for the concentration in a semi-infinite region of low diffusion coefficient bisected by a thin well-diffusing slab, at different times after the boundary of the semi-infinite region has been raised suddenly from zero to unit concentration. This is of interest in grain-boundary diffusion.

42

INFINITE AND SEMI-INFINITE MEDIA

[图片: |(D₁t/l²)¹/²|M₁/C₀ (D₂=0)|M₁/C₀ (D₂=4)|M₁/C₀ (D₂=1)|M₁/C₀ (D₂=4)|M₁/C₀ (D₂=∞)| |:---:|:---:|:---:|:---:|:---:|:---:| |0.5|0.5|0.6|0.6|0.7|0.8| |1.0|1.0|1.0|1.0|1.0|1.0| |1.5|1.0|1.4|1.7|1.9|2.5| |2.0|1.0|1.9|2.4|2.4|3.5| |2.5|1.0|2.3|3.1|3.0|4.5| |3.0|1.0|2.5|3.5|3.3|5.5|]
# FIG. 3.8. Sorption curves for a composite semi-infinite medium. Numbers on curves are values of $D_1/D_2$.

# 3.6. Weber's disc

This is a classical problem of the field due to an electrified disc. More recent interest relates to the diffusion current at a circular electrode. Several authors (Tranter 1951; Grigull 1961; Saito 1968) have developed the same solution in different ways. When the diameter of the electrode is $2a$ we require solutions of

$$ \frac{\partial^2 C}{\partial r^2} + \frac{1}{r} \frac{\partial C}{\partial r} + \frac{\partial^2 C}{\partial z^2} = 0, \qquad (3.59) $$

where C is the concentration say of oxygen in the solution, the axis of z passes perpendicularly through the centre of the disc and r is the radial distance from the z-axis. The boundary conditions are

$$ \begin{aligned} C &= 0, & z &= 0, & r &\leqslant a, \\ \partial C/\partial z &= 0, & z &= 0, & r &> a, \\ C &= C_0, & r &\geqslant 0, & z &= \infty, \\ C &= C_0, & z &\geqslant 0, & r &= \infty, \end{aligned} \qquad (3.60) $$

where $C_0$ is the concentration in the bulk of the solution. The concentration is

INFINITE AND SEMI-INFINITE MEDIA

43

given by

$$ \begin{aligned} C_0 - C &= \frac{2C_0}{\pi} \int_0^\infty \frac{\sin(ma)}{m} J_0(mr) e^{-mz} dm \\ &= \frac{2C_0}{\pi} \tan^{-1} \frac{a}{\sqrt{\left(\frac{1}{2}[(r^2 + z^2 - a^2) + \sqrt{\{(r^2 + z^2 - a^2) + 4z^2 a^2\}]\right)}}. \end{aligned} \quad (3.61) $$

The concentration gradient at the disc surface is

$$ \left( \frac{\partial C}{\partial z} \right)_{z=0} = - \frac{2C_0}{\pi} \int_0^\infty \sin(ma) J_0(mr) \, dm \\ \stackrel{\text{=}}{=} \frac{2C_0}{\pi} \frac{1}{\sqrt{(a^2 - r^2)}}. \quad (3.62) $$

Saito (1963) gives an approximate analytical solution for a narrow band electrode and sketches the concentration distribution for each electrode.

# 4

## DIFFUSION IN A PLANE SHEET

## 4.1. Introduction

IN this chapter we consider various cases of one-dimensional diffusion in a medium bounded by two parallel planes, e.g. the planes at $x = 0$, $x = l$. These will apply in practice to diffusion into a plane sheet of material so thin that effectively all the diffusing substance enters through the plane faces and a negligible amount through the edges.

### 4.2. Steady state

Consider the case of diffusion through a plane sheet or membrane of thickness $l$ and diffusion coefficient $D$, whose surfaces, $x = 0$, $x = l$, are maintained at constant concentrations $C_1$, $C_2$ respectively. After a time, a steady state is reached in which the concentration remains constant at all points of the sheet. The diffusion equation in one dimension then reduces to

$$ d^2C/dx^2 = 0, \qquad (4.1) $$

provided the diffusion coefficient $D$ is constant. On integrating with respect to $x$ we have

$$ dC/dx = \text{constant}, \quad (4.2) $$

and by a further integration we have, on introducing the conditions at $x = 0$, $x = l$,

$$ \frac{C - C_1}{C_2 - C_1} = \frac{x}{l}. \qquad (4.3) $$

Both (4.2) and (4.3) show that the concentration changes linearly from $C_1$ to $C_2$ through the sheet. Also, the rate of transfer of diffusing substance is the same across all sections of the membrane and is given by

$$ F = -D \frac{dC}{dx} = D(C_1 - C_2)/l. \quad (4.4) $$

If the thickness $l$ and the surface concentrations $C_1, C_2$ are known, $D$ can be deduced from an observed value of $F$ by using (4.4). Experimental arrangements for measuring $D$ in this and other ways have been reviewed by Newns (1950).

If the surface $x = 0$ is maintained at a constant concentration $C_1$ and at $x = l$ there is evaporationation into an atmosphere for which the equilibrium

DIFFUSION IN A PLANE SHEET

45

concentration just within the surface is $C_2$, so that

$$ \partial C/\partial x + h(C - C_2) = 0, \quad x = l, $$

then we find

$$ \frac{C - C_1}{C_2 - C_1} = \frac{hx}{1 + hl}, \quad (4.3a) $$

and

$$ F = \frac{Dh(C_1 - C_2)}{1 + hl}. \quad (4.4a) $$

If the surface conditions are:

$$ \partial C/\partial x + h_1(C_1 - C) = 0, \quad x = 0; \quad \partial C/\partial x + h_2(C - C_2) = 0, \quad x = l, $$

then

$$ C = \frac{h_1 C_1 \{1 + h_2(l-x)\} + h_2 C_2 (1 + h_1 x)}{h_1 + h_2 + h_1 h_2 l}, \quad (4.3b) $$

and

$$F = \frac{Dh_1h_2(C_1 - C_2)}{h_1 + h_2 + h_1h_2l} \quad (4.4b)$$

Corresponding solutions for a funnel-shaped region are easily obtained (Jacobs 1967).

# 4.2.1. Permeability constant

In some practical systems, the surface concentrations $C_1, C_2$ may not be known but only the gas or vapour pressures $p_1, p_2$ on the two sides of the membrane. The rate of transfer in the steady state is then sometimes written

$$ F = P(p_1 - p_2)/l, \quad (4.5) $$

and the constant $P$ is referred to as the permeability constant. Here $P$ is expressed, for example, as cm $^{3}$ gas at some standard temperature and pressure passing per second through 1 cm $^{2}$ of the surface of a membrane 1 cm thick when the pressure difference across the membrane is 1 cm of mercury. The permeability constant is a much less fundamental constant than the diffusion coefficient which is expressed in units such as cm $^{2}$ s $^{-1}$, particularly as different investigators use different units and even different definitions of $P$.

If the diffusion coefficient is constant, and if the sorption isotherm is linear, i.e. if there is a linear relationship between the external vapour pressure and the corresponding equilibrium concentration within the

46

DIFFUSION IN A PLANE SHEET

membrane, then eqns (4.4) and (4.5) are equivalent, but not otherwise. The linear isotherm may be written

$$ C = Sp, \quad (4.6) $$

where $C$ is the concentration within the material of the membrane in equilibrium with an external vapour pressure $p$, and $S$ is the solubility. Since $C_1$, $p_1$ and $C_2$, $p_2$ in (4.4) and (4.5) are connected by (4.6) it follows that, with due regard to units,

$$ P = DS. \quad (4.7) $$

## 4.2.2. Concentration-dependent diffusion coefficient

If the diffusion coefficient varies with concentration it is clear that the simple value of $D$ deduced from a measurement of the steady rate of flow is some kind of mean value over the range of concentration involved. Thus, if $D$ is a function of $C$ (4.1) is to be replaced by

$$ \frac{d}{dx} \left( D \frac{dC}{dx} \right) = 0, \qquad (4.8) $$

and hence the relationship

$$ F = -D \text{ dC/dx} = \text{constant} \quad (4.9) $$

still holds, as of course it must in the steady state. Integrating between $C_1$ and $C_2$, the two surface concentrations, we have

$$ F = -\frac{1}{l} \int_{C_1}^{C_2} D \, dC = D_I(C_1 - C_2)/l, \quad (4.10) $$

where

$$ D_I = \frac{1}{C_1 - C_2} \int_{C_2}^{C_1} D \, dC, \qquad (4.11) $$

and this is the mean value deduced from a measurement of F. It follows from (4.9) that if D depends on C the concentration no longer depends linearly on distance through the membrane. Concentration distributions for D depending on C in a number of ways are given in Chapter 9.

# 4.2.3. Composite membrane

If we have a composite membrane composed of $n$ sheets of thicknesses $l_1, l_2, \dots, l_n$, and diffusion coefficients $D_1, D_2, \dots, D_n$, the fall in concentration through the whole membrane is the sum of the falls through the component sheets. Since the rate of transfer $F$ is the same across each section, the total

DIFFUSION IN A PLANE SHEET

47

drop in concentration is

$$ \frac{Fl_1}{D_1} + \frac{Fl_2}{D_2} + \dots + \frac{Fl_n}{D_n} = (R_1 + R_2 + \dots + R_n)F, \quad (4.12) $$

where $R_1 = l_1/D_1$, etc. may be termed formally the resistance to diffusion of each sheet. Thus the resistance to diffusion of the whole membrane is simply the sum of the resistances of the separate layers, assuming that there are no barriers to diffusion between them. This subject is treated more generally in § 12.2(i) (p. 266).

# 4.3. Non-steady state

All the solutions presented here can be obtained either by the method of separation of the variables or by the Laplace transform as described in § 2.4. Many of the results are quoted by Barrer (1951), Carswal and Jaeger (1959), Jacobs (1967), Jost (1952) and others. The emphasis here is on numerical evaluation.

## 4.3.1. Surface concentrations constant. Initial distribution $f(x)$

If

$$ C = C_1, \quad x = 0, \quad t \ge 0, \quad (4.13) $$

$$ C = C_2, \quad x = l, \quad t \ge 0, \quad (4.14) $$

$$C = f(x), \quad 0 < x < l, \quad t = 0, \qquad (4.15)$$

the solution in the form of a trigonometrical series is

$$C = C_1 + (C_2 - C_1) \frac{x}{l} + \frac{2}{\pi} \sum_{1}^{\infty} \frac{C_2 \cos n\pi - C_1}{n} \sin \frac{n\pi x}{l} \exp(-Dn^2\pi^2t/l^2) + \frac{2}{l} \sum_{1}^{\infty} \sin \frac{n\pi x}{\pi} \exp(-Dn^2n^2t/l^2) \int_{0}^{l} f(x') \sin \frac{n\pi x'}{l} dx'. \quad (4.16)$$

In the cases of most common occurrence $f(x)$ is either zero or constant so that the integral in (4.16) is readily evaluated. Very often the problem is symmetrical about the central plane of the sheet, and the formulae are then most convenient if this is taken as $x = 0$ and the surfaces at $x = \pm l$.

## 4.3.2. Uniform initial distribution. Surface concentrations equal

This is the case of sorption and desorption by a membrane. If the region $-l < x < l$ is initially at a uniform concentration $C_0$, and the surfaces are kept at a constant concentration $C_1$, the solution (4.16) becomes

$$ \frac{C - C_0}{C_1 - C_0} = 1 - \frac{4}{\pi} \sum_{n=0}^{\infty} \frac{(-1)^n}{2n+1} \exp \left\{ -D(2n+1)^2 \pi^2 t/4l^2 \right\} \cos \frac{(2n+1)\pi x}{2l} \quad (4.17) $$

If $M_t$ denotes the total amount of diffusing substance which has entered the

48

DIFFUSION IN A PLANE SHEET

sheet at time $t$, and $M_\infty$ the corresponding quantity after infinite time, then

$$ \frac{M_t}{M_\infty} = 1 - \sum_{n=0}^{\infty} \frac{8}{(2n+1)^2 \pi^2} \exp \left\{ -D(2n+1)^2 \pi^2 t/4l^2 \right\}. \qquad (4.18) $$

The corresponding solutions useful for small times are

$$ \frac{C-C_0}{C_1-C_0} = \sum_{n=0}^{\infty} (-1)^n \operatorname{erfc} \frac{(2n+1)l-x}{2\sqrt{(Dt)}} + \sum_{n=0}^{\infty} (-1)^n \operatorname{erfc} \frac{(2n+1)l+x}{2\sqrt{(Dt)}}, \quad (4.19) $$

and

$$ \frac{M_t}{M_\infty} = 2 \left( \frac{Dt}{l^2} \right)^{\frac{1}{2}} \left\{ \pi^{-\frac{1}{2}} + 2 \sum_{n=1}^{\infty} (-1)^n \text{ ierfc} \frac{nl}{\sqrt{(Dt)}} \right\}. \qquad (4.20) $$

The modifications to these expressions for $C_0 = 0$ or $C_1 = 0$ are obvious.

Jason and Peters (1973) analyse the bimodal diffusion of water in fish muscle by combining two expressions of the type (4.18), one for each mode and each having its own diffusion coefficient.

Eqn (4.18) can be solved graphically for $Dt/l^2$ and hence $D$ obtained from measured sorption or desorption time curves. An alternative suggested by Talbot and Kitchener (1956) is the approximate formula

$$\theta = -\ln x + \frac{q}{p} + \frac{rq^2}{2p^3}$$

where $\theta=\pi^2Dt/4l^2$, $x=\frac{1}{8}\pi^2M_t/M_\infty$ and $p=1+x^8+x^{24}$, $q=\frac{1}{9}x^8+\frac{1}{25}x^{24}$, and, $r=1+9x^8+25x^{24}$.

The solution is correct to four significant figures when $M_l/M_\infty < \frac{2}{3}$ for desorption. The solution (4.18) also applies to diffusion along a cylindrical rod or tube of length $l$, with one end and its surface sealed and the other end maintained at a constant concentration.

Talbot and Kitchener also obtained a solution for a slightly tapering tube. If $d_1$ and $d_2$ are the diameters of the two ends, the degree of taper is specified by $\mu = (d_2-d_1)/d_1$, where $d_1$ is the closed end, and may be positive or negative. For small $\mu$, e.g. around 0-01, we have effectively radial diffusion and a solution is

$$\frac{M_t}{M_\infty} = \frac{6(1+\mu)^2}{3+3\mu+\mu^2} \sum_{n=1}^{\infty} \frac{\alpha_n^2+\mu^2}{\alpha_n^2(\alpha_n^2+\mu^2+\mu)} \exp(-D\alpha_n^2 t/l^2),$$

where the $\alpha_n$ are the roots of $\tan \alpha = -\alpha/\mu$, and, to the first order in $\mu$, $\alpha_n^2 = (n - \frac{1}{2})^2\pi^2 + 2\mu$. The solution becomes, with this approximation,

$$ \frac{M_t}{M_\infty}=\sum_{n=1}^\infty\frac{8}{(2n-1)^2\pi^2}\{ 1+(k_n-\lambda\theta)\mu\exp\left(-(2n-1)^2\theta\right)\}, $$

DIFFUSION IN A PLANE SHEET

49

where $\theta = \pi^2 Dt/4l^2$, $\lambda = 8/\pi^2$, $k_n = 1 - \frac{3}{2}\lambda/(2n-1)^2$, i.e.

$$ \lambda = 0.81057, \quad k_1 = -0.21585, \quad k_2 = 0.86491, \quad k_3 = 0.95137. $$

Thus putting $x = \frac{1}{8}\pi^2 M_t/M_\infty$ as before, $\theta$ must satisfy

$$x = \{1 + (k_1 - \lambda\theta)\mu\} e^{-\theta} + \frac{1}{9}\{1 + (k_2 - \lambda\theta)\mu\} e^{-9\theta} \\ + \frac{1}{25}\{1 + (k_3 - \lambda\theta)\mu\} e^{-25\theta} + \dots$$

If the solution (4.18) is applied to the tapered tube to calculate $\theta$, the approximate value, say $\theta_0$, obtained can be corrected by using

$$\theta = \theta_0 \left\{ 1 - \mu \frac{\lambda(1+q) - s/\theta_0}{p} \right\} = \theta_0(1 - \kappa\mu)$$

where $s = k_1 + \frac{1}{9}k_2x^8 + \frac{1}{25}k_3x^{24}$, $p$ and $q$ are defined above, and $\kappa\mu$ is the correction term. Talbot and Kitchener (1956) quote

$$ \kappa = 0.807 - 0.60x^8 + (0.212 - 0.25x^8)/\theta_0 $$

approximately and discuss in more detail the capillary tube method (Anderson and Saddington 1949) for measuring diffusion coefficients.

It is clear that expressions (4.17), (4.18), (4.19), (4.20) can be written in terms of the dimensionless parameters

$$T = Dt/l^2, \qquad X = x/l, \qquad (4.21)$$

so that the solutions for all values of $D, l, t$, and $x$ can be obtained from graphs or tabulated values covering these two parameters. Graphs of $(C-C_0)/(C_1-C_0)$ are shown for various times in Fig. 4.1. These are reproduced with change of nomenclature from Carslaw and Jaeger's book (1959, p. 101). Tabulated values of $(C-C_0)/(C_1-C_0)$ and of $M_t/M_\infty$ are given by Henry (1939). Values of $M_t/M_\infty$ have also been tabulated by McKay (1930) and extensive numerical values for the concentration at the centre of the sheet, $x = 0$, are given by Olson and Schulz (1942). The curve labelled zero fractional uptake in Fig. 4.6 shows how $M_t/M_\infty$ varies with the square root of time in a sheet of thickness $2a$ when the concentration at each surface remains constant.

# 4.3.3. Uniform initial distribution. Surface concentrations different

This is the case of flow through a membrane. If one face $x = 0$ of a membrane is kept at a constant concentration $C_1$ and the other $x = l$ at $C_2$, and the membrane is initially at a uniform concentration $C_0$, there is a finite interval of time during which the steady-state condition previously discussed

50

DIFFUSION IN A PLANE SHEET

[图片: |(C-C₀)/(C₁-C₀)|x/l| |:---:|:---:| |1.5|0.0| |1.0|0.0| |0.8|0.0| |0.6|0.0| |0.4|0.0| |0.3|0.0| |0.2|0.0| |0.15|0.0| |0.1|0.0| |0.08|0.17| |0.06|0.25| |0.04|0.35| |0.03|0.4| |0.02|0.5| |0.01|0.67| |0.005|0.83|]
# FIG. 4.1. Concentration distributions at various times in the sheet $-l < x < l$ with initial uniform concentration $C_0$ and surface concentration $C_1$. Numbers on curves are values of $Dt/l^2$.

in § 4.2 (p. 44) is set up. During this time the concentration changes according to

$$C = C_1 + (C_2 - C_1) \frac{x}{l} + \frac{2}{\pi} \sum_{n=1}^{\infty} \frac{C_2 \cos n\pi - C_1}{n} \sin \frac{n\pi x}{l} \exp(-Dn^2\pi^2t/l^2) + \frac{4C_0}{\pi} \sum_{m=0}^{\infty} \frac{1}{2m+1} \sin \frac{(2m+1)\pi x}{l} \exp\{-D(2m+1)^2\pi^2t/l^2\}. \quad (4.22)$$

As $t$ approaches infinity the terms involving the exponentials vanish and we have simply the linear concentration distribution obtained in § 4.2. Barnes (1934) examined the errors introduced by assuming a linear gradient to exist across the membrane during the whole course of diffusion.

If $M_t$ denotes the total amount of diffusing substance which enters the sheet during time $t$, and $M_\infty$ the corresponding amount during infinite time, then

$$ \frac{M_t}{M_\infty} = 1 - \frac{8}{\pi^2} \sum_{n=0}^{\infty} \frac{1}{(2n+1)^2} \exp \{-D(2n+1)^2 \pi^2 t/l^2\}. \quad (4.23) $$

In this case $M_\infty = l\{\frac{1}{2}(C_1 + C_2) - C_0\}$ and the total content of the membrane.

DIFFUSION IN A PLANE SHEET

51

at time $t$ is given by $M_t + lC_0$. The expression (4.23) is similar to (4.18) and is readily evaluated from the curve labelled zero fractional uptake in Fig. 4.6, with the proviso that in (4.23) $l$ signifies the whole thickness of the membrane but in (4.18) it denotes the half-thickness.

The rate at which the gas or other diffusing substance emerges from unit area of the face $x = l$ of the membrane is given by $-D(\partial C/\partial x)_{x=l}$ which is easily deduced from (4.22). By integrating then with respect to $t$, we obtain the total amount of diffusing substance $Q_t$ which has passed through the membrane in time $t$.

$$ Q_t = D(C_1 - C_2) \frac{t}{l} + \frac{2l}{\pi^2} \sum_1^\infty \frac{C_1 \cos n\pi - C_2}{n^2} \{1 - \exp(-Dn^2\pi^2t/l^2)\} + \frac{4C_0 l}{\pi^2} \sum_{m=0}^\infty \frac{1}{(2m+1)^2} \{1 - \exp(-D(2m+1)^2\pi^2t/l^2)\}. \quad (4.24) $$

In the commonest experimental arrangement both $C_0$ and $C_2$ are zero, i.e. the membrane is initially at zero concentration and the concentration at the face through which diffusing substance emerges is maintained effectively at zero concentration. In this case we find

$$ \frac{Q_t}{lC_1} = \frac{Dt}{l^2} - \frac{1}{6} - \frac{2}{\pi^2} \sum_1^\infty \frac{(-1)^n}{n^2} \exp(-Dn^2\pi^2t/l^2), \quad (4.24a) $$

which, as $t \to \infty$, approaches the line

$$Q_t = \frac{DC_1}{l} \left( t - \frac{l^2}{6D} \right). \qquad (4.25)$$

This has an intercept $L$ on the $t$-axis given by

$$L = l^2/6D \quad (4.26)$$

Following Daynes (1920), Barrer (1951) has used (4.26) as the basis of a method for obtaining the diffusion constant, the permeability constant, and the solubility of a gas by analysing stationary and non-stationary flow through a membrane. Thus from an observation of the intercept, $L$, $D$ is deduced by (4.26); from the steady-state flow rate the permeability constant $P$ is deduced by using (4.5), and $S$ follows from (4.7). The intercept $L$ is referred to as the 'time lag'.

A graph of $Q_t/lC_1$ as a function $Dt/l^2$ is shown for the case $C_0 = C_2 = 0$ in Fig. 4.2. To within the accuracy of plotting the steady state is achieved when $Dt/l^2 = 0.45$ approximately

An alternative form of solution useful for small times, usually attributed to Holstein (Rogers, Buritz, and Alpert 1954) is easily derived by using Laplace transforms as in § 2.4.3(i). Still keeping $C_0 = C_2 = 0$, we find the rate of

52

DIFFUSION IN A PLANE SHEET

[图片: |Dt/l^2|Q_t/C_1| |:---:|:---:| |0.1|0.0| |0.2|0.0| |0.3|0.1| |0.4|0.2| |0.5|0.3|]
# FIG. 4.2. Approach to steady-state flow through a plane sheet.

flow $F(t)$ per unit area of the surface $x = l$ to be

$$F(t) = -\left(\frac{D\partial C}{\partial x}\right)_{x=l} = 2C_1 \sum_{1}^{\infty} \left(\frac{D}{\pi t}\right)^{\frac{1}{2}} \exp\left\{-(2m+1)^2 l^2/(4Dt)\right\} \quad (4.27)$$

This series converges most rapidly for small $t$. Rogers et $al$. take only the leading term and obtain essentially

$$ \ln(t^{\frac{1}{2}}F) = \ln \left\{ 2C_1 \left( \frac{D}{\pi} \right)^{\frac{1}{2}} \right\} - \frac{l^2}{4Dt}. \qquad (4.27a) $$

From the slope and intercept of this line experimental data yield $D$ and $C_1$, and hence solubility. They discuss the advantages of their method compared with the use of the time lag given by eqn (4.26).

Other applications of Holstein's solution are discussed in § 10.6 and § 10.6.2 (pp. 216 and 224). Jenkins, Nelson, and Spirer (1970) examined the more general problems of deducing both the diffusion coefficient and the solubility coefficient from experimental data and mathematical solutions when the outflow volume is finite so that the concentration varies with time at the outgoing face. The necessary solution is given by Carslaw and Jaeger (1959). Jenkins et al. tabulate some useful calculated data and also consider varying concentrations at the ingoing face. In particular, they examined the assumption, frequently made in time-lag measurements of the Daynes type, that

DIFFUSION IN A PLANE SHEET

53

steady flow is established after a period of about 3 times the time lag. They concluded that the time lag is underestimated by about 4 per cent by making this assumption.

Paul and Dibenedetto (1965) also obtained solutions for finite outflow volumes. Špaček and Kubin (1967) allowed the concentrations on both sides of the membrane to vary with time.

# 4.3.4. Variable surface concentration

The solution to the general problem of diffusion in the region $0 < x < l$ with the surfaces at concentrations $\phi_1(t)$ and $\phi_2(t)$ and the initial concentration $f(x)$ is given by Carslaw and Jaeger (1959, p. 102). For empirical values of $\phi_1(t)$, $\phi_2(t)$, and $f(x)$, three integrals arise which have to be evaluated graphically or numerically. In certain cases, however, where the surface concentration can be represented by a mathematical expression, the solution can be considerably simplified.

(i) One case of practical interest is that of a sheet in which the concentration is initially zero and each surface of which approaches an equilibrium concentration $C_0$, exponentially, i.e.

$$ \phi_1(t) = \phi_2(t) = C_0\{1 - \exp(-\beta t)\}. \qquad (4.28) $$

This can represent a surface concentration which is changed rapidly but not instantaneously, a situation which usually arises when an instantaneous change is attempted in an experiment. For the sheet whose surfaces are at $\pm l$ the solution is

$$ \begin{aligned}\frac{C}{C_0}&=1-\exp(-\beta t)\frac{\cos x(\beta/D)^{\ddagger}}{\cos l(\beta/D)^{\ddagger}}\\&\quad-\frac{16\beta l^2}{\pi}\sum_{n=0}^{\infty}\frac{(-1)^n\exp(-D(2n+1)^2\pi^2t/4l^2)}{(2n+1)\{ 4\beta l^2-D\pi^2(2n+1)^2\}}\cos\frac{(2n+1)\pi x}{2l},(4.29)\end{aligned} $$

provided $\beta$ is not equal to any of the values $D(2n+1)^2\pi^2/4l^2$. The sorption-time curve, i.e. the curve showing the total amount $M_t$ of diffusing substance in the sheet as a function of time $t$, is obtained by integrating (4.29) with respect to $x$ between the limits $-l$ and $+l$ and is

$$ \begin{aligned}\frac{M_t}{2lC_0}&=1-\exp(-\beta t)(D/\beta l^2)^{\ddagger}\tan(\beta l^2/D)^{\ddagger}\\&\quad-\frac{8}{\pi^2}\sum_{n=0}^{\infty}\frac{\exp\{-(2n+1)^2\pi^2Dt/4l^2\}}{(2n+1)^2[1-(2n+1)^2\{ D\pi^2/(4\beta l^2)\}]}.\end{aligned}\qquad(4.30) $$

# Fig. 4.3 shows uptake curves for different values of the parameter $\beta l^2/D$ plotted against $(Dt/l^2)^{\frac{1}{2}}$. When $\beta = \infty$, the surface concentration rises instantaneously to $C_0$ and the curve of Fig. 4.3 has the characteristic initial

54

DIFFUSION IN A PLANE SHEET

[图片: |(Dt/P)¹/²|M₁/2/C₀| |:---:|:---:| |0.0|0.0| |0.5|0.0| |1.0|0.0| |1.5|0.02| |2.0|0.08| |2.5|0.2| |3.0|0.4| |3.5|0.62| |4.0|0.78| |4.5|0.85| |5.0|0.92|]
# FIG. 4.3. Calculated sorption curves for surface concentration given by $C_0(1 - e^{-\beta t})$. Numbers on curves are values of $\beta l^2/D$.

linear portion followed by the approach to the equilibrium value $M_t = 2lC_0$. The uptake curves for finite values of $\beta l^2/D$, for which the surface concentration rises at a finite rate, all show points of inflexion. At first the rate of uptake increases as sorption proceeds but later decreases as the final equilibrium is approached. Curves of this kind are often referred to as sigmoid sorption curves. They may arise in practice because surface equilibrium conditions are not established instantaneously, but they may result from other causes (see § 11.2, p. 255; § 14.4.6, p. 347).

(ii) If the surface concentrations vary linearly with time, i.e.

$$ \phi_1(t) = \phi_2(t) = kt, \quad (4.31) $$

the solution is

$$ \frac{DC}{kl^2} = \frac{Dt}{l^2} + \frac{1}{2} \left( \frac{x^2}{l^2} - 1 \right) + \frac{16}{\pi^3} \sum_{n=0}^{\infty} \frac{(-1)^n}{(2n+1)^3} \exp \left\{ -D(2n+1)^2 \pi^2 t/4l^2 \right\} \cos \frac{(2n+1)\pi x}{2l} \quad (4.32) $$

DIFFUSION IN A PLANE SHEET

55

[图片: |x/l|D/kp (曲线1)|D/kp (曲线2)|D/kp (曲线0.5)|D/kp (曲线0.25)|D/kp (曲线0.1)| |:---:|:---:|:---:|:---:|:---:|:---:| |0|0.6|1.4|0.2|0.1|0.05| |0.2|0.65|1.45|0.22|0.12|0.06| |0.4|0.7|1.5|0.25|0.15|0.07| |0.6|0.75|1.6|0.3|0.18|0.08| |0.8|0.85|1.7|0.4|0.2|0.09| |1.0|1.0|2.0|0.5|0.25|0.1|]
# FIG. 4.4. Concentration distributions in a plane sheet for surface concentration $kt$. Numbers on curves are values of $Dt/l^2$.

The corresponding expression for $M_t$ is

$$ \frac{DM_t}{kl^3} = \frac{2Dt}{l^2} - \frac{2}{3} + \frac{64}{\pi^4} \sum_{n=0}^{\infty} \frac{\exp\{-D(2n+1)^2\pi^2t/4l^2\}}{(2n+1)^4}. \quad (4.33) $$

Some numerical results are given by Williamson and Adams (1919) and Gurney and Lurie (1923). Fig. 4.4 shows $DC/kl^2$ plotted as a function of $x/l$ for various values of $Dt/l^2$. Fig. 4.5 shows $DM_t/kl^3$ as a function of the single variable $Dt/l^2$.

[图片: |Dt/l²|DM₀/kP| |:---:|:---:| |0.0|0.0| |0.5|0.5| |1.0|1.0| |1.5|2.0| |2.0|3.5|]
# FIG. 4.5. Sorption curve for plane sheet with surface concentration $kt$.

56

DIFFUSION IN A PLANE SHEET

These solutions can be extended to cover modified surface conditions such as $\phi_1(t) = \phi_2(t) = C_0 + kt$, and a non-zero initial concentration by superposing solutions as in § 3.3(v).

Sinusoidally varying surface concentrations are considered in § 10.6 (p. 217).

# 4.3.5. Diffusion from a stirred solution of limited volume

If a plane sheet is suspended in a volume of solution so large that the amount of solute taken up by the sheet is a negligible fraction of the whole, and the solution is well stirred, then the concentration in the solution remains constant. If, however, there is only a limited volume of solution, the concentration of solute in the solution falls as solute enters the sheet. If the solution is well stirred the concentration in the solution depends only on time, and is determined essentially by the condition that the total amount of solute in the solution and in the sheet remains constant as diffusion proceeds. It is useful from an experimental point of view to have only a limited amount of solution since the rate of uptake of solute by the sheet can be deduced from observations of the uniform concentration in the solution. It is often simpler to do this than to observe directly the amount in the sheet. This has been stressed by Carman and Haul (1954), who have written mathematical solutions in forms most appropriate for the measurement of diffusion coefficients by this method.

The general problem can be stated mathematically in terms of a solute diffusing from a well-stirred solution. The modifications necessary for corresponding alternative problems, such as that of a sheet suspended in a vapour, are obvious.

Suppose that an infinite sheet of uniform material of thickness $2l$ is placed in a solution and that the solute is allowed to diffuse into the sheet. The sheet occupies the space $-l \le x \le l$, while the solution is of limited extent and occupies the spaces $-l-a \le x \le -l$, $l \le x \le l+a$. The concentration of the solute in the solution is always uniform and is initially $C_0$, while initially the sheet is free from solute.

We require a solution of the diffusion equation:

$$ \frac{\partial C}{\partial t} = D \frac{\partial^2 C}{\partial x^2}, \qquad (4.34) $$

with the initial condition

$$ C = 0, \quad -l < x < l, \quad t = 0, \quad (4.35) $$

and with a boundary condition expressing the fact that the rate at which solute leaves the solution is always equal to that at which it enters the sheet over the surfaces $x = \pm l$. This condition is

$$ a\partial C/\partial t = \mp D\partial C/\partial x, \quad x = \pm l, \quad t > 0. \quad (4.36) $$

DIFFUSION IN A PLANE SHEET

57

We assume here that the concentration of solute just within the surface of the sheet is the same as that in the solution. This may not be so but there may be a partition factor $K$ which is not unity, such that the concentration just within the sheet is $K$ times that in the solution. This can clearly be allowed for by using a modified length of solution $a/K$ in place of $a$ in (4.36) and elsewhere.

A solution of this problem by March and Weaver (1928), based on the use of an integral equation, was cumbersome for numerical evaluation. More convenient forms of solution have been obtained by Carslaw and Jaeger (1959, p. 128), Wilson (1948), Berthier (1952), while Crank (1948c) has developed solutions particularly suitable for small values of the time. The solution is most readily obtained by the use of the Laplace transform. In a form expressing the total amount of solute $M_t$ in the sheet at time $t$ as a fraction of $M_\infty$, the corresponding quantity after infinite time, the solution is

$$ \frac{M_t}{M_\infty} = 1 - \sum_{n=1}^{\infty} \frac{2\alpha(1+\alpha)}{1+\alpha+\alpha^2 q_n^2} \exp(-Dq_n^2 t/l^2), \quad (4.37) $$

where the $q_n$s are the non-zero positive roots of

$$ \tan q_n = -\alpha q_n, \quad (4.38) $$

and $\alpha = a/l$, the ratio of the volumes of solution and sheet, or if there is a partition factor $K$ then $\alpha = a/Kl$. Some roots of (4.38) are given in Table 4.1 for values of $\alpha$ corresponding to several values of final fractional uptake. Roots for other values of $\alpha$ are given by Carslaw and Jaeger (1959, p. 492) and by Carman and Haul (1954). It is sometimes convenient to express $\alpha$ in terms of the fraction of total solute finally taken up by the sheet. Thus, in the final equilibrium state, since the total amount of solute in solution and sheet was originally contained in the solution of concentration $C_0$, we have

$$ \frac{aC_{\infty}}{K} + lC_{\infty} = aC_{0}, \quad (4.39) $$

where $C_{\infty}$ is the uniform concentration in the sheet finally. The content $M_{\infty}$ of the sheet finally is given by

$$M_{\infty} = 2lC_{\infty} = \frac{2aC_{0}}{1+a/(lK)} = \frac{2aC_{0}}{1+\alpha}. \quad (4.40)$$

The fractional uptake of the sheet finally is therefore given by

$$ \frac{M_{\infty}}{2aC_0} = \frac{1}{1+\alpha}. \quad (4.41) $$

If, for example, 50 per cent of the solute initially in the solution is finally in the sheet, $\alpha = 1$. In the particular case of an infinite amount of solute ($\alpha = \infty$)

58

DIFFUSION IN A PLANE SHEET

the roots of (4.38) are $q_n = (n + \frac{1}{2})\pi$, and we have

$$ \frac{M_t}{M_\infty} = 1 - \sum_{n=0}^{\infty} \frac{8}{(2n+1)^2 \pi^2} \exp \{-D(n + \frac{1}{2})^2 \pi^2 t/l^2\}, \quad (4.42) $$

which is expression (4.18) for the case of a constant concentration $C_0$ at the surface of a sheet. The smaller $Dt/l^2$ is, the more terms in the series in (4.37) are needed for a given accuracy. When more than three or four terms are needed it is better to use an alternative form of solution. For most values of $\alpha$ the simplest expression is

$$ \frac{M_t}{M_\infty} = (1 + \alpha) \{1 - \exp(T/\alpha^2) \text{erfc}(T/\alpha^2)^{\frac{1}{2}}\}, \quad (4.43) $$

where $T = Dt/l^2$. If very small values of $\alpha$ are required, corresponding to very high fractional uptakes of solute by the sheet, there may be a range of $Dt/l^2$ in which neither (4.37) nor (4.43) is convenient but where the following is useful:

$$ \frac{M_t}{M_\infty} = (1 + \alpha) \left\{ 1 - \frac{\alpha}{\pi^{\frac{1}{2}} T^{\frac{1}{2}}} + \frac{\alpha^3}{2\pi^{\frac{1}{2}} T^{\frac{3}{2}}} - \frac{3\alpha^5}{4\pi^{\frac{1}{2}} T^{\frac{5}{2}}} + \dots \right\} . \quad (4.44) $$

This is obtained from (4.43) by substituting the asymptotic expansion for $\exp(T/\alpha^2)$ erfc $(T/\alpha^2)^{\frac{1}{2}}$ when $T/\alpha^2$ is large.

Fig. 4.6 gives curves showing $M_t/M_\infty$ against $(Dt/l^2)^\dagger$ for five values of final fractional uptake. Fig. 4.6 shows that the greater the final fractional uptake of the sheet the faster is the solute removed from the solution. Clearly by comparing the rate of fall of concentration in the solution observed experimentally, with the corresponding calculated curve showing $M_t/M_\infty$ as a function of $Dt/l^2$, the diffusion coefficient $D$ can be deduced. This has been suggested by Berthier (1952) as a method for measuring self-diffusion using radioactive isotopes. He gives a table of $M_t/M_\infty$ for values of $1/\alpha$ between 0 and 1.0 at intervals of 0.1. For precision measurements it is advisable to check Berthier's values as in some instances not enough terms of the series solutions have been retained to obtain the accuracy quoted. The concentration within the sheet is given by the expression

$$ C = C_{\infty} \left\{ 1 + \sum_{n=1}^{\infty} \frac{2(1+\alpha) \exp(-Dq_n^2 t/l^2)}{1+\alpha+\alpha^2 q_n^2} \frac{\cos(q_n x/l)}{\cos q_n} \right\}. \quad (4.45) $$

We have considered diffusion into a plane sheet initially free of solute. There is the complementary problem in which all the solute is initially uniformly distributed through the sheet and subsequently diffuses out into a well-stirred solution. It is easily seen that the mathematical solutions presented above for sorption by the sheet also describe desorption, provided $M_t$ is taken to mean the amount of solute leaving the sheet up to time $t$.

DIFFUSION IN A PLANE SHEET

59

[图片: |(Dt/l²)¹/²|Mₜ/M∞ (90)|Mₜ/M∞ (70)|Mₜ/M∞ (50)|Mₜ/M∞ (30)|Mₜ/M∞ (0)| |:---:|:---:|:---:|:---:|:---:|:---:| |0.1|0.76|0.5|0.36|0.24|0.08| |0.2|0.88|0.72|0.58|0.4|0.16| |0.3|0.94|0.84|0.74|0.58|0.24| |0.4|0.97|0.91|0.84|0.7|0.32| |0.5|0.99|0.95|0.9|0.8|0.4| |0.6|1.0|0.97|0.95|0.88|0.48| |0.7|1.0|0.99|0.97|0.93|0.55| |0.8|1.0|1.0|0.98|0.96|0.62| |0.9|1.0|1.0|0.99|0.98|0.69| |1.0|1.0|1.0|0.99|0.99|0.75| |1.1|1.0|1.0|1.0|1.0|0.81|]
# FIG. 4.6. Uptake by a plane sheet from a stirred solution of limited volume. Numbers on curves show the percentage of total solute finally taken up by the sheet.

and $M_{\infty}$ the corresponding amount after infinite time. For the problem of desorption from the sheet we require a solution of (4.34) satisfying (4.36) but with the initial condition (4.35) replaced by

$$ C = C_0, \quad -l < x < l, \quad t = 0. \quad (4.46) $$

On writing

$$ C_1 = C_0 - C, \quad (4.47) $$

(4.46) and the other equations for desorption are identical with (4.34), (4.35), (4.36), with $C_1$ written for C. Hence the equations and solutions for desorption are identical with those for sorption provided $M_t, M_\infty$ are suitably interpreted and $C_1, (C_1)_\infty$ replace $C, C_\infty$ in expression (4.45). The parameter $\alpha$ is equal to $a/K_l$ as before, but its relation to the final uptake of the sheet expressed by (4.40) and (4.41) no longer holds. Instead we have that the fractional uptake of the solution is given by

$$ \frac{M_{\infty}}{2lC_0} = \frac{1}{1+1/\alpha}. \quad (4.48) $$

Jaeger and Clarke (1947) have presented solutions of a number of other problems in diffusion from a well-stirred solution in terms of certain fundamental functions. Accurately drawn graphs of these functions, from which

60

DIFFUSION IN A PLANE SHEET

solutions of limited accuracy are readily constructed, are given in their paper. Permeation into finite volumes is discussed in § 4.3.3 (pp. 52, 53).

# 4.3.6. Surface evaporation

In § 3.3.1 (p. 35) the rate of loss of diffusing substance by evaporation from the surface of a sheet was represented by

$$ -D \partial C / \partial x = \alpha (C_0 - C_s), \quad (4.49) $$

where $C_s$ is the actual concentration just within the sheet and $C_0$ is the concentration required to maintain equilibrium with the surrounding atmosphere. If the sheet $-l < x < l$ is initially at a uniform concentration $C_2$, and the law of exchange of the type (4.49) holds on both surfaces, the solution is

$$ \frac{C - C_2}{C_0 - C_2} = 1 - \sum_{n=1}^{\infty} \frac{2L \cos(\beta_n x/l) \exp(-\beta_n^2 Dt/l^2)}{(\beta_n^2 + L^2 + L) \cos \beta_n}, \quad (4.50) $$

where the $\beta_n$s are the positive roots of

$$ \beta \tan \beta = L \qquad (4.51) $$

and

$$ L = l\alpha/D, \quad (4.52) $$

a dimensionless parameter. Roots of (4.51) are given in Table 4.2 for several values of $L$. Roots for other values of $L$ are given by Carslaw and Jaeger (1959, p. 491). The total amount of diffusing substance $M_t$ entering or leaving the sheet up to time $t$, depending on whether $C_0$ is greater or less than $C_2$, is expressed as a fraction of $M_\infty$, the corresponding quantity after infinite time, by

$$ \frac{M_t}{M_\infty} = 1 - \sum_{n=1}^{\infty} \frac{2L^2 \exp(-\beta_n^2 Dt/l^2)}{\beta_n^2(\beta_n^2 + L^2 + L)}. \quad (4.53) $$

A solution suitable for small values of time may be obtained in the usual way by expanding the expression for the Laplace transform in a series of negative exponentials (Carslaw and Jaeger 1959, p. 310). The terms in the series expression for concentration very soon become cumbersome for numerical evaluation, however. In practice, it is usually sufficient to use only the leading terms corresponding to the interval during which the sheet is effectively semi-infinite, when the concentration is given by expression (3.35), and (3.37) gives the value of $M_t$ for half the sheet.

Graphs showing $M_t/M_\infty$ for several values of $L$ are plotted in Fig. 4.7 from numerical values given by Newman (1931). Carslaw and Jaeger (1959, p. 123) give corresponding curves as well as others showing how the concentrations at the surfaces and the centre of the sheet vary with time. Newman

DIFFUSION IN A PLANE SHEET

61

[图片: |(Dt/l²)¹/²|M₁/M∞| |:---:|:---:| |0.1|0.0| |0.5|0.0| |1|0.0| |2|0.0| |10|0.0| |∞|0.0|]
# FIG. 4.7. Sorption or desorption curves for the surface condition (4.49). Numbers on curves are values of $L = l\alpha/D$.

also gives a table of values from which $M_t/M_\infty$ can easily be deduced for a parabolic initial distribution instead of a uniform initial concentration. All these equations and solutions have a practical application in the drying of porous solids.

Carslaw and Jaeger (1959, p. 114) give solutions of more general problems in which there is an initial, non-uniform concentration distribution, or in which the vapour pressure is different on the two surfaces of the sheet, or in which evaporation occurs from one surface only, the other being maintained at a constant concentration. Jaeger and Clarke (1947) have also given in graphical form the solutions of a number of problems with an evaporation type of boundary condition.

The more complicated case in which the rate of transfer on the surface is proportional to some power of the surface concentration was discussed by Jaeger (1950a).

# 4.3.7. Constant flux $F_0$ at the surfaces

If the sheet $-l < x < l$ is initially at a constant concentration $C_0$, and diffusing substance enters at a constant rate $F_0$ over unit area of each surface, i.e.

$$D \partial C/\partial x = F_0, \quad x = l, \qquad (4.54)$$

then

$$C-C_0 = \frac{F_0 l}{D} \left\{ \frac{Dt}{l^2} + \frac{3x^2 - l^2}{6l^2} - \frac{2}{\pi^2} \sum_{n=1}^{\infty} \frac{(-1)^n}{n^2} \exp(-Dn^2 \pi^2 t / l^2) \cos \frac{n\pi x}{l} \right\}. \quad (4.55)$$

62

DIFFUSION IN A PLANE SHEET

Obviously the total amount of diffusing substance taken up by unit area of the sheet in time $t$ is $2F_0t$. Concentration-distance curves for various times are shown in Fig. 4.8. An alternative form of solution suitable for small times is given by Macey (1940).

[图片: |x/l|D(C-C0)/Fl = 0.1|D(C-C0)/Fl = 0.25|D(C-C0)/Fl = 0.5|D(C-C0)/Fl = 1.0| |:---:|:---:|:---:|:---:|:---:| |0.0|0.0|0.1|0.3|0.8| |0.2|0.0|0.1|0.3|0.8| |0.4|0.0|0.2|0.4|0.9| |0.6|0.1|0.3|0.5|1.0| |0.8|0.2|0.4|0.7|1.1| |1.0|0.4|0.6|0.9|1.3|]
# FIG. 4.8. Concentration distributions in a plane sheet for constant flux $F_0$ at the surface. Numbers on curves are values of $Dt/l^2$.

# 4.3.8. Impermeable surfaces

An impermeable surface is one at which the concentration gradient is zero. This condition holds at the central plane of a sheet provided the initial and boundary conditions are symmetrical about that plane. It follows therefore that the symmetrical solutions already given for the plane sheet occupying the region $-l < x < l$ apply also to the sheet $0 < x < l$ when the face $x = 0$ is impermeable. If, on the other hand, both surfaces $x = 0$ and

DIFFUSION IN A PLANE SHEET

63

$x = l$ are impermeable and the initial distribution is $f(x)$, the solution is

$$ C = \frac{1}{l} \int_{0}^{l} f(x') dx' + \frac{2}{l} \sum_{n=1}^{\infty} \exp(-Dn^2\pi^2t/l^2) \cos \frac{n\pi x}{l} \int_{0}^{l} f(x') \cos \frac{n\pi x'}{l} dx'. \quad (4.56) $$

Barrer (1951) suggests that diffusion from one layer to another as discussed in § 2.2.4 may be treated by regarding the system as a single layer with impermeable boundaries and applying (4.56), where the initial distribution is

$$ \left. \begin{array}{l} f(x) = C_0, \\ f(x) = 0, \end{array} \right. \qquad 0 < x < h \}. \qquad (4.57) $$

The solution (4.56) becomes

$$ C = C_0 \left\{ \frac{h}{l} + \frac{2}{\pi} \sum_{n=1}^{\infty} \frac{1}{n} \sin \frac{n\pi h}{l} \exp(-Dn^2\pi^2t/l^2) \cos \frac{n\pi x}{l} \right\}. \quad (4.58) $$

Jackson, Oldland, and Pajaczkowski (1968) made a similar use of (4.56) in a radiotracer method of measuring diffusion coefficients (§ 10.8, p. 252). The solution (4.58) is complementary to expression (2.17) which is convenient for small times. Numerical values based on (2.17) and (4.58) are available in the well-known tables by Stefan (1879) and Kawalki (1894), some of which are reproduced by Jost (1952).

Another special case of (4.56) has been evaluated by Crank and Henry (1949c) in an investigation of different methods of conditioning a sheet to a required uniform concentration. They consider the problem in which a sheet, initially at zero concentration throughout, has its surfaces maintained at a constant concentration $C_0$ for a time $t_0$, after which they are rendered impermeable. The subsequent change in concentration is described by (4.56) with $f(x)$ given by

$$ f(x) = C_0 \left[ 1 - \frac{4}{\pi} \sum_{m=0}^{\infty} \frac{1}{2m+1} \sin \frac{(2m+1)\pi x}{l} \exp \left\{ -D(2m+1)^2 \pi^2 t_0 / l^2 \right\} \right]. \quad (4.59) $$

In this case the two integrals in (4.56) reduce to

$$ \int_0^l f(x) dx = C_0 l \left[ 1 - \frac{8}{\pi^2} \sum_{m=0}^{\infty} \frac{1}{(2m+1)^2} \exp \left\{ -D(2m+1)^2 \pi^2 t_0 / l^2 \right\} \right], \quad (4.60) $$

and

$$ \int_0^l f(x) \cos \frac{2p\pi x}{l} dx = \frac{8C_0 l}{\pi^2} \sum_{m=0}^{\infty} \frac{1}{4p^2 - (2m+1)^2} \exp \{-D(2m+1)^2\pi^2 t_0 / l^2\}, \quad (4.61) $$

64

DIFFUSION IN A PLANE SHEET

where $2p$ is substituted for $n$ since only the terms involving even $n$ are non-zero.

# 4.3.9. Composite sheet

Various problems of diffusion into a composite sheet comprised of two layers for which the diffusion coefficients are different have been solved (see, for example, Carslaw and Jaeger (1959, p. 319)). The solutions are similar in form to those presented in this chapter but obviously more complicated. In view of the additional number of parameters involved, no attempt is made to give numerical results here. Studies of the time-lag involved in establishing the steady-state flow through a composite sheet of several layers are discussed in § 12.2(ii) (p. 268).

# 4.4. Edge effects in membranes

We have treated flow through a membrane as a one-dimensional phenomenon. In the usual experimental arrangements an appreciable portion of the membrane is clamped between impermeable annular plates of outer radius b. At the ingoing and outgoing faces, flow only occurs through the circular aperture, radius a, where a < b. But inside the membrane the flow lines spread into the clamped region. This 'edge effect' means that the usual assumption of one-dimensional diffusion is not strictly correct. Barrer, Barrie, and Rogers (1962), using a solution developed by Jaeger and Beck (1955), examined the importance of the edge effect. They replaced the usual experimental condition of constant concentrations maintained on the two faces of the membrane by conditions of uniform constant flux. The mathematical solution yields a mean concentration difference between the two faces of the membrane which can be equated to the prescribed uniform difference in the original experiment. Barrer et al. (1962) obtain the relationship

$$F_0/F = 1 - 16S/\pi^2, \qquad (4.62)$$

with

$$S = \sum_{q=1}^{\infty} \frac{1}{q^2} \frac{I_1(q\alpha)}{I_1(q\beta)} \{I_1(q\beta)K_1(q\alpha) - K_1(q\beta)I_1(q\alpha)\}, \quad (4.63)$$

where $F$ is the steady-state flux per unit area with edge effect, $F_0$ without edge effect, $\beta = \pi b/l$, $\alpha = \pi a/l$, with $l$ the membrane thickness, and $I_1, K_1$ are modified Bessel functions. Fig. 4.9, taken from Barrer et al.'s paper, shows that the relative difference in the flux ($F-F_0)/F_0$ for a given overlap ($b-a/a$ is greater the thicker the membrane and for an $l/a$ ratio of 0.2 or less is approaching the limits of experimental error.

The conclusion is that with thin membranes ($l/a \le 0.2$) edge effects may safely be neglected but otherwise appreciable errors creep in. Barrer et al.

DIFFUSION IN A PLANE SHEET

65

[图片: |100(b-a)/a|0.2|0.4|0.6|0.8| |:---:|:---:|:---:|:---:|:---:| |5|2|4|6|8| |10|4|7|10|14| |15|5|9|13|19| |20|5|10|15|23| |25|5|11|16|28|]
# FIG. 4.9. Relative difference in flux ($F-F_0)/F_0$ as a function of the overlap ($b-a)/a$ for fixed $l/a$ ratios. (From Barrer et al. 1962).

show that the errors can lead to apparent differences between diffusion coefficients deduced from steady-state and time-lag measurements.

# 4.5. Approximate two-dimensional solutions

Problems in which the diffusion is predominantly in one direction occur frequently, perhaps because of the boundary conditions or the shape of the medium. Crank and Parker (1966) obtained approximate solutions to two-dimensional problems in biased heat flow. Previously it was widely accepted that for a thin sheet a good, one-dimensional approximation is obtained by assuming the temperature to be uniform across the thickness of the sheet. It appears, however, that a 'quadratic profile' provides a better approximation than the usual 'constant profile'. Crank and Parker considered the problem defined by the equations

$$v_{xx}+v_{yy}=v_t \qquad (4.64)$$

$$v_x = 0, \quad x = 0; \quad v_x = -hv, \quad x = b; \quad t \ge 0, \quad (4.65)$$

$$ \begin{aligned} v &= 0, & y &= 0; & v &= 1, & y &= 1, & t &\ge 0, \\ v &= 0, & 0 &\le y < 1, & 0 &\le x \le b, & t &= 0. \end{aligned} \quad (4.66) $$

66

DIFFUSION IN A PLANE SHEET

These equations describe the temperature in a sheet of thickness b and unit length, whose ends are maintained at fixed temperatures and from the surfaces of which heat is lost according to Newton's law of cooling. In diffusion terms, we have ends at constant concentration and evaporation from the surface x = b.

(i) Constant profile. If diffusion is small in the x-direction compared with that in the y-direction, then the concentration $v$ should vary slowly with x. Thus the mean concentration $u$ defined by

$$u = \frac{1}{b} \int_{0}^{b} v \, dx \qquad (4.67)$$

should be a good approximation to $v$. On integrating (4.64) with respect to $x$ from 0 to $b$ and using (4.67) we obtain

$$u_t-u_{yy}=\frac{1}{b}[v_x]_0^b=\frac{-h}{b}(v)_{x=b},$$

i.e.

$$u_t - u_{yy} = -pu, \qquad (4.68)$$

where

$$p = \{h(v)_{x=b}\}/bu. \qquad (4.69)$$

The 'constant profile' solution (Fox 1934) assumes $v \equiv u$, i.e. $p = h/b$. Crank and Parker discuss two ways of improving this crude approximation.

(ii) Partial separation of variables. We replace the assumption $v \equiv u$ by $v = Xu$, where $X$ is a function of $x$ only and $u$ is defined by (4.68) for some value of $p$. Then from (4.64)

$$uX_{xx} = X(u_t - u_{yy}) = -Xpu$$

from (4.68), so that $X_{xx} = -pX$ and finally

$$X = A \sin(x\sqrt{p}) + B \cos(x\sqrt{p}),$$

where A, B are arbitrary constants. In order to satisfy (4.65) with $v = Xu$ we have A = 0 and

$$ \sqrt{p} \tan(b\sqrt{p}) = h. \qquad (4.70) $$

If $hb$ is small enough we get a good approximation from the first root only $p_1$ of (4.70). Then (4.68) becomes

$$u_t - u_{vv} = -p_1 u. \qquad (4.71)$$

The boundary conditions on $u$ are found from (4.66) and (4.67) and are

$$u=0, y=0; \quad u=1, y=1; \quad u=0, t=0, 0 \le y<1. \quad (4.72)$$

DIFFUSION IN A PLANE SHEET

67

The solution of (4.71) subject to (4.72) is

$$u_1 = \frac{\sinh(y\sqrt{p_1})}{\sinh\sqrt{p_1}} + 2\pi \exp(-p_1 t) \sum_{r=1}^{\infty} \frac{(-1)^r r}{p_1 + r^2 \pi^2} \exp(-r^2 \pi^2 t) \sin r\pi y. \quad (4.73)$$

Thus, an approximation to the solution of (4.64), (4.65), and (4.66) is

$$ v_1 = Bu_1 \cos x \sqrt{p_1}. \quad (4.74) $$

The arbitrary constant $B$ may be chosen so that $v_1$ is as close as possible to $v$ at $t = 0$. Since $u_1$ is identically zero at $t = 0$ except when $y = 1$, the only deviation of $v_1$ from $v$ to be minimized is along $y = 1$. A least-squares fitting of $v_1$ gives

$$B = 2h/[\{h+b(h^2+p_1)\} \cos(b\sqrt{p_1})]. \quad (4.75)$$

A Chebyshev criterion (Fox and Parker 1968) leads to

$$ B = 2/\{1 + \cos(b\sqrt{p})\}. \quad (4.76) $$

Crank and Parker quote error bounds on $v - v_1$.

(iii) Quadratic profile. An alternative approach starts again from (4.68) but with $p$ regarded simply as a parameter, for the time being unknown. We define an approximation $w(x, y, t)$ to $v$ such that

$$ w_{xx} = u_t - u_{yy} = -pu. \quad (4.77) $$

Since $u$ and $p$ are independent of $x$ we can integrate (4.77) to give:

$$ w = (A + Bx - \frac{1}{2}px^2)u, \quad (4.78) $$

where $A$ and $B$ are arbitrary functions of $y$ and $t$. They are obtained by making $w$ obey the conditions (4.65) on $v$ and we have

$$ B = 0, \quad A = pb(1 + \frac{1}{2}hb)/h, $$

so that

$$ w = (1 + \frac{1}{2}hb - \frac{1}{2}hx^2/b) \frac{pbu}{h}. \quad (4.79) $$

We can easily see that $w$ satisfies eqns (4.64)–(4.66) to within $O(hb)$ if $p = h\{1+O(hb)\}/b$. Thus by using $w$ for $v$ in (4.69) to obtain $p$, we have finally

$$ w = \frac{k(1 + \frac{1}{2}hb - \frac{1}{2}hx^2/b)u}{1 + \frac{1}{3}hb}, \quad (4.80) $$

68

DIFFUSION IN A PLANE SHEET

referred to as the 'quadratic-profile' solution. The constant $k$ is arbitrary but must not differ from unity by more than $O(hb)$. Least-squares or Chebyshev criteria can again be used but we choose $k = 1$. Crank and Parker (1966) tabulated their approximate solutions and compared them with the full analytical solution which is

$$ v = \sum_{s=1}^{\infty} \frac{2h}{h + b(h^2 + \alpha_s^2)} \frac{\cos \alpha_s x}{\cos \alpha_s b} \\ \times \left\{ \frac{\sinh \alpha_s y}{\sinh \alpha_s} + 2\pi \exp(-\alpha_s^2 t) \sum_{r=1}^{\infty} \frac{(-1)^r r \exp(-r^2 \pi^2 t)}{r^2 \pi^2 + \alpha_s^2} \sin r \pi y \right\}, \quad (4.81) $$

where $\alpha_s$, ($s = 1, 2, \dots$) are the positive roots of

$$ \alpha \tan \alpha b = h, \qquad (4.82) $$

for a range of values of $h$ and $b$. They concluded that the 'constant-profile' solution which is usually used as an approximation for a thin sheet or rod is, in fact, poor for a thin sheet with a high surface evaporation. But it provides a good approximation for a thick sheet with low surface loss. Both the quadratic profile' and the 'partial separation of variables' yield much better approximations over all. Concentration profiles across the sheet support these general conclusions.

As hb → 0, the roots of (4.82) approach

$$ b\alpha_1 \sim \sqrt{h b}, b\alpha_{n+1} \sim n\pi, n \ge 1. $$

Also the constant terms outside the curly brackets in (4.81) tend towards unity for $s = 1$ and the other terms either stay of the same order of magnitude or decrease, as $s$ increases. It is easy to see that as $hb \to 0$ the analytical solution (4.81) approaches the approximate solution given by (4.73), (4.74), and (4.79). Crank and Parker show, however, that the approximate methods can readily be extended to cover some non-linear situations.

5

# DIFFUSION IN A CYLINDER

## 5.1. Introduction

WE consider a long circular cylinder in which diffusion is everywhere radial. Concentration is then a function of radius $r$ and time $t$ only, and the diffusion equation (1.7) becomes

$$ \frac{\partial C}{\partial t} = \frac{1}{r} \frac{\partial}{\partial r} \left( r D \frac{\partial C}{\partial r} \right). \qquad (5.1) $$

## 5.2. Steady state

If the medium is a hollow cylinder whose inner and outer radii are $a$ and $b$ respectively, and if the diffusion coefficient is constant, the equation describing the steady-state condition is

$$ \frac{d}{dr} \left( r \frac{dC}{dr} \right) = 0, \quad a < r < b. \qquad (5.2) $$

The general solution of this is

$$ C = A + B \ln r, \qquad (5.3) $$

where $A$ and $B$ are constants to be determined from the boundary conditions at $r = a$, $r = b$. If the surface $r = a$ is kept at a constant concentration $C_1$, and $r = b$ at $C_2$, then

$$ C = \frac{C_1 \ln (b/r) + C_2 \ln (r/a)}{\ln (b/a)}. \quad (5.4) $$

The quantity of diffusing substance $Q_t$ which diffuses through unit length of the cylinder in time $t$ is given by

$$Q_t = \frac{2\pi Dt(C_2 - C_1)}{\ln(b/a)} \quad (5.5)$$

If $Q_t$ is measured in a concentration-dependent system, the mean value of the diffusion coefficient obtained from (5.5) is $(\int_{C_1}^{C_2} D dC)/(C_2 - C_1)$ as for the plane sheet (see (4.11)). The concentration distribution defined by (5.4) is not linear, as it is for the plane sheet. Typical distributions are shown in Fig. 5.1 for the cases $C_2 = 0, b/a = 2, 5, 10$.

70

DIFFUSION IN A CYLINDER

[图片: |r/a|C/C₁ (曲线2)|C/C₁ (曲线5)|C/C₁ (曲线10)| |:---:|:---:|:---:|:---:| |1|1.0|1.0|1.0| |2|0.0|0.6|0.8| |3||0.4|0.7| |4||0.3|0.6| |5|0.0|0.0|0.5| |6|||0.4| |7|||0.3| |8|||0.2| |9|||0.1| |10|0.0|0.0|0.0|]
# FIG. 5.1. Steady-state concentration distributions through cylinder wall. Numbers on curves are values of $b/a$.

Another steady-state problem leading to an interesting result is that of the hollow cylinder whose surface $r = a$ is kept at a constant concentration $C_1$, and at $r = b$ there is evaporation into an atmosphere for which the equilibrium concentration just within the surface is $C_2$. The boundary condition, with the constant of proportionality denoted by $h$, is

$$ \frac{dC}{dr} + h(C - C_2) = 0, \quad r = b, \qquad (5.6) $$

and we find

$$C = \frac{C_1\{1+hb \ln(b/r)\} + hbC_2 \ln(r/a)}{1+hb \ln(r/a)} \quad (5.7)$$

The outward rate of diffusion per unit length of the cylinder is $Q_t$, where

$$Q_t = 2\pi D(C_1 - C_2) \frac{hb}{1 + hb \ln (b/a)}. \qquad (5.8)$$

By differentiating this expression with respect to $b$, it is easily seen that if $ah > 1$ the rate of diffusion decreases steadily as $b$ increases from $a$, but if $ah < 1$ the rate first increases and later decreases, passing through a maximum when $b = 1/h$. This is due to the two opposing changes associated with an increase in $b$. On the one hand, the rate of evaporation is increased because of the increase in area of the surface, $r = b$, as $b$ increases, but on the other hand, the gradient of concentration through the cylinder decreases as $b$ is increased. In certain circumstances, therefore, the rate of diffusion through the wall of a pipe may be increased by making the wall thicker (Porter and Martin 1910). This is illustrated in Fig. 5.2 for $ah = \frac{1}{2}$.

DIFFUSION IN A CYLINDER

71

[图片: |b/a|Q₁/2πD(C₁-C₂)| |:---:|:---:| |1.0|0.50| |1.5|0.56| |2.0|0.59| |2.5|0.58| |3.0|0.56| |3.5|0.55|]
# FIG. 5.2. Effect of thickness of cylinder wall on steady-state rate of flow.

If the surface conditions are

$$ \partial C/\partial r + h_1(C_1 - C) = 0; \quad \partial C/\partial r + h_2(C - C_2) = 0, \quad (5.6a) $$

we find

$$C = \frac{ah_1C_1\{1+bh_2 \ln(b/r)\} + bh_2C_2\{1+ah_1 \ln(r/a)\}}{ah_1 + bh_2 + abh_1h_2 \ln(b/a)}, \quad (5.7a)$$

and

$$Q_t = \frac{2\pi Dtabh_1h_2(C_2 - C_1)}{ah_1 + bh_2 + abh_1h_2 \ln (b/a)} \quad (5.8a)$$

Other problems on diffusion in regions bounded by surfaces of the cylindrical coordinate system and in which the flow is not necessarily radial are treated by Carslaw and Jaeger (1959, p. 214).

# 5.3. Non-steady state: solid cylinder

Following essentially the method of separating the variables described in § 2.3 (p. 17), we see that

$$ C = u \exp(-D\alpha^2 t) \quad (5.9) $$

72

DIFFUSION IN A CYLINDER

is a solution of (5.1) for $D$ constant provided $u$ is a function of $r$ only, satisfying

$$ \frac{d^2 u}{dr^2} + \frac{1}{r} \frac{du}{dr} + \alpha^2 u = 0, \quad (5.10) $$

which is Bessel's equation of order zero. Solutions of (5.10) may be obtained in terms of Bessel functions, suitably chosen so that the initial and boundary conditions are satisfied. Thus if the initial concentration distribution is $f(r)$ and the surface $r = a$ is maintained at zero concentration, a solution of (5.1) is wanted satisfying

$$ C = 0, \quad r = a, \quad t \ge 0, \qquad (5.11) $$

$$ C = f(r), \quad 0 < r < a, \quad t = 0. \qquad (5.12) $$

The boundary condition (5.11) is satisfied by

$$ C = \sum_{n=1}^{\infty} A_n J_0(\alpha_n r) \exp(-D\alpha_n^2 t), \quad (5.13) $$

provided the $\alpha_n$s are roots of

$$ J_0(a\alpha_n) = 0, \quad (5.14) $$

where $J_0(x)$ is the Bessel function of the first kind of order zero. Roots of (5.14) are tabulated in tables of Bessel functions. For this function $C$ is finite at $r = 0$. The initial condition (5.12) becomes

$$ f(r) = \sum_{n=1}^{\infty} A_n J_0(r\alpha_n), \quad (5.15) $$

it being assumed that $f(r)$ can be expanded in a series of Bessel functions of order zero. The $A_n$s are determined by multiplying both sides of (5.15) by $rJ_0(\alpha_n r)$ and integrating from 0 to $a$ using the results,

$$ \int_0^a r J_0(\alpha r) J_0(\beta r) dr = 0, \qquad (5.16) $$

when $\alpha$ and $\beta$ are different roots of (5.14), and

$$ \int_0^a r \{J_0(\alpha r)\}^2 dr = \frac{1}{2} a^2 J_1^2(a\alpha_n), \quad (5.17) $$

where $J_1(x)$ is the Bessel function of the first order and $\alpha$ is a root of (5.14). The derivation of the relationships (5.16) and (5.17), and of corresponding expressions which hold when $\alpha$ is a root not of (5.14) but of alternative equations which commonly arise in diffusion problems, is given by Carslaw

DIFFUSION IN A CYLINDER

73

and Jaeger (1959, p. 196). Finally the solution satisfying (5.11) and (5.12) is

$$ C = \frac{2}{a^2} \sum_{n=1}^{\infty} \exp(-D\alpha_n^2 t) \frac{J_0(r\alpha_n)}{J_1^2(a\alpha_n)} \int_0^a rf(r) J_0(r\alpha_n) dr. \quad (5.18) $$

Alternatively, solutions for both large and small times can be obtained by use of the Laplace transform.

# 5.3.1. Surface concentration constant : initial distribution $f(r)$

If in the cylinder of radius $a$ the conditions are

$$ C = C_0, \quad r = a, \quad t \ge 0, \qquad (5.19) $$

$$ C = f(r), \quad 0 < r < a, \quad t = 0, \qquad (5.20) $$

the solution is

$$C = C_0 \left\{ 1 - \frac{2}{a} \sum_{n=1}^{\infty} \frac{1}{\alpha_n} \frac{J_0(r\alpha_n)}{J_1(a\alpha_n)} \exp(-D\alpha_n^2 t) \right\} + \frac{2}{a^2} \sum_{n=1}^{\infty} \exp(-D\alpha_n^2 t) \frac{J_0(r\alpha_n)}{J_1^2(a\alpha_n)} \int rf(r) J_0(r\alpha_n) dr, \quad (5.21)$$

where the $\alpha_n$s are the positive roots of (5.14).

If the concentration is initially uniform throughout the cylinder $f(r) = C_1$ and (5.21) reduces to

$$ \frac{C - C_1}{C_0 - C_1} = 1 - \frac{2}{a} \sum_{n=1}^{\infty} \frac{\exp(-D\alpha_n^2 t) J_0(r\alpha_n)}{\alpha_n J_1(a\alpha_n)}. \quad (5.22) $$

If $M_t$ denotes the quantity of diffusing substance which has entered or left the cylinder in time $t$ and $M_\infty$ the corresponding quantity after infinite time, then

$$ \frac{M_t}{M_\infty} = 1 - \sum_{n=1}^{\infty} \frac{4}{a^2 \alpha_n^2} \exp(-D\alpha_n^2 t). \quad (5.23) $$

The corresponding solution useful for small times is:

$$ \frac{C - C_1}{C_0 - C_1} = \frac{a^{\frac{1}{2}}}{r^{\frac{1}{2}}} \operatorname{erfc} \frac{a-r}{2\sqrt{(Dt)}} + \frac{(a-r)(Dta)^{\frac{1}{2}}}{4ar^{\frac{1}{2}}} \operatorname{ierfc} \frac{a-r}{2\sqrt{(Dt)}} + \frac{(9a^2 - 7r^2 - 2ar)Dt}{32a^{\frac{1}{2}}r^{\frac{1}{2}}} i^2 \operatorname{erfc} \frac{a-r}{2\sqrt{(Dt)}} + \dots, \quad (5.24) $$

which holds provided $r/a$ is not small. The case of $r/a$ small is discussed by Carsten and McKerrow (1944). They give a series solution involving modified Bessel functions of order $n \pm \frac{1}{4}$. The necessary functions are tabulated in their paper and numerical calculation is straightforward.

74

DIFFUSION IN A CYLINDER

Also for small times we have

$$ \frac{M_t}{M_\infty} = \frac{4}{\pi^{\frac{1}{2}}} \left( \frac{Dt}{a^2} \right)^{\frac{1}{2}} - \frac{Dt}{a^2} - \frac{1}{3\pi^{\frac{1}{2}}} \left( \frac{Dt}{a^2} \right)^{\frac{3}{2}} + \dots \quad (5.25) $$

Clearly these solutions are not as valuable as the corresponding ones for the plane sheet. In practice the range in $t$ over which they are convenient for evaluation is less than in the plane case.

[图片: |(C-C₁)/(C₀-C₁)|r/a| |:---:|:---:| |0.005|0.78| |0.01|0.7| |0.02|0.62| |0.03|0.55| |0.04|0.48| |0.06|0.39| |0.08|0.32| |0.1|0.26| |0.15|0.2| |0.2|0.15| |0.3|0.1| |0.4|0.07| |0.6|0.04| |0.8|0.02| |1.0|0.0|]
# FIG. 5.3. Concentration distributions at various times with initial concentration $C_1$ and surface concentration $C_0$. Numbers on curves are values of $Dt/a^2$.

The solutions for the cylinder can be written in terms of the two dimensionless parameters $Dt/a^2$ and $r/a$. Curves showing $(C-C_1)/(C_0-C_1)$ as a function of $r/a$ for different values of $Dt/a^2$ drawn by Carswal and Jaeger (1959, p. 200) are reproduced in Fig. 5.3. The curve of Fig. 5.7 for zero fractional uptake shows how $M_t/M_\infty$ depends on $Dt/a^2$ when the concentration at the surface of the cylinder remains constant.

DIFFUSION IN A CYLINDER

75

# 5.3.2. Variable surface concentration

If the initial concentration in the cylinder is zero and that at the surface is $\phi(t)$, the solution is

$$ C = \frac{2D}{a} \sum_{n=1}^{\infty} \exp(-D\alpha_n^2 t) \frac{\alpha_n J_0(r\alpha_n)}{J_1(a\alpha_n)} \int_0^t \exp(D\alpha_n^2 \lambda)\phi(\lambda) d\lambda, \quad (5.26) $$

where the $\alpha_n$s are the roots of (5.14).

(i) As for the plane sheet, a case of practical interest is when.

$$ \phi(t) = C_0\{1 - \exp(-\beta t)\}, \quad (5.27) $$

representing a surface concentration which approaches a steady value $C_0$, but not instantaneously. The solution (5.26) then becomes

$$ \frac{C}{C_0} = 1 - \frac{J_0\{(\beta r^2/D)^{\frac{1}{2}}\}}{J_0\{(\beta a^2/D)^{\frac{1}{2}}\}} \exp(-\beta t) + \frac{2\beta}{aD} \sum_{n=1}^{\infty} \frac{J_0(r\alpha_n)}{\alpha_n J_1(a\alpha_n)} \frac{\exp(-D\alpha_n^2 t)}{(\alpha_n^2 - \beta/D)}, \quad (5.28) $$

and the sorption-time curve is given by:

$$ \frac{M_t}{\pi a^2 C_0} = 1 - \frac{2J_1\{(\beta a^2/D)^{\frac{1}{2}}\} \exp(-\beta t)}{(\beta a^2/D)^{\frac{1}{2}}J_0\{(\beta a^2/D)^{\frac{1}{2}}\}} + \frac{4}{a^2} \sum_{n=1}^{\infty} \frac{\exp(-D\alpha_n^2 t)}{\alpha_n^2\{\alpha_n^2/(\beta/D)-1\}}. \quad (5.29) $$

# Fig. 5.4 shows uptake curves for different values of the parameter $\beta a^2/D$.

[图片: |(Dt/a²)¹/²|M/πa²C₀| |:---:|:---:| |∞|1.0| |5|1.0| |1|1.0| |0.5|0.98| |0.1|0.76| |0.01|0.22|]
# FIG. 5.4. Calculated sorption curves for surface concentration given by $C_0(1 - e^{-\beta t})$. Numbers on curves are values of $\beta a^2/D$.

76

DIFFUSION IN A CYLINDER

(ii) If the surface concentration varies linearly with time, i.e.

$$ \phi(t) = kt, \qquad (5.30) $$

the solution is

$$C = k \left( t - \frac{a^2 - r^2}{4D} \right) + \frac{2k}{aD} \sum_{n=1}^{\infty} \exp(-D\alpha_n^2 t) \frac{J_0(r\alpha_n)}{\alpha_n^3 J_1(a\alpha_n)}. \quad (5.31)$$

[图片: |r/a|0.08|0.16|0.32|0.48|0.80| |:---:|:---:|:---:|:---:|:---:|:---:| |0.0|0.0|0.0|0.12|0.25|0.55| |0.1|0.0|0.0|0.13|0.26|0.56| |0.2|0.0|0.0|0.14|0.27|0.57| |0.3|0.0|0.0|0.15|0.28|0.58| |0.4|0.0|0.0|0.16|0.29|0.59| |0.5|0.0|0.01|0.18|0.31|0.61| |0.6|0.0|0.02|0.2|0.33|0.63| |0.7|0.01|0.04|0.23|0.36|0.66| |0.8|0.02|0.06|0.26|0.39|0.69| |0.9|0.04|0.09|0.3|0.43|0.73| |1.0|0.07|0.12|0.34|0.48|0.8|]
# FIG. 5.5. Concentration distributions through a cylinder with surface concentration $kt$. Numbers on curves are values of $Dt/a^2$.

In Fig. 5.5, curves showing $DC/(ka^2)$ are drawn against $r/a$ for different values of $Dt/a^2$. Numerical values are given by Williamson and Adams (1919). The corresponding expression for $M_t$ is

$$M_t = \pi ka^2 t - \frac{\pi ka^4}{8D} + \frac{4\pi k}{D} \sum_{n=1}^{\infty} \frac{\exp(-D\alpha_n^2 t)}{\alpha_n^4}, \qquad (5.32)$$

and $M_tD/(\pi ka^4)$ is plotted against $Dt/a^2$ on Fig. 5.6. These solutions can be extended by superposition as in § 3.3(v), to cover modified surface conditions such as $\phi(t) = C_0 + kt$ and a non-zero initial concentration.

DIFFUSION IN A CYLINDER

77

[图片: |Dt/a²|M₁/πka⁴| |:---:|:---:| |0.0|0.0| |0.1|0.03| |0.2|0.08| |0.3|0.14| |0.4|0.21| |0.5|0.29| |0.6|0.37| |0.7|0.46| |0.8|0.55|]
# FIG. 5.6. Sorption curve for cylinder with surface concentration $kt$.

# 5.3.3. Diffusion from a stirred solution of limited volume

The problem differs only in detail from the corresponding problem considered for the plane sheet in § 4.3.5 (p. 56) and the results can be written down without explanation.

Suppose that the cylinder occupies the space $r < a$ while the cross-section of the bath of solution in which it is immersed is $A$ (excluding the space occupied by the cylinder). The concentration of solute in the solution is always uniform and is initially $C_0$. The cylinder is initially free from solute. The total amount of solute $M_t$ in the cylinder after time $t$ is expressed as a fraction of the corresponding amount $M_\infty$ after infinite time by the relation (Wilson 1948).

$$ \frac{M_t}{M_\infty} = 1 - \sum_{n=1}^{\infty} \frac{4\alpha(1+\alpha)}{4+4\alpha+\alpha^2 q_n^2} \exp(-Dq_n^2 t/a^2), \quad (5.33) $$

where the $q_n$s are the positive, non-zero roots of

$$\alpha q_n J_0(q_n) + 2J_1(q_n) = 0, \qquad (5.34)$$

and $\alpha = A/\pi a^2$, the ratio of the volumes of solution and eyinder. If there is a partition factor $K$ between solute in equilibrium in the cylinder and in the solution, $\alpha = A/(\pi a^2 K)$. The parameter $\alpha$ is expressed in terms of the final fractional uptake of solute by the cylinder by the expression

$$ \frac{M_{\infty}}{AC_0} = \frac{1}{1+\alpha}. \qquad (5.35) $$

The roots of (5.34) are given in Table 5.1 for several values of $\alpha$ in order to assist the evaluation of (5.33). The convergence of the series in (5.33) becomes inconveniently slow for numerical evaluation when $Dt/a^2$ is small. An

78

DIFFUSION IN A CYLINDER

alternative solution suitable for small $Dt/a^2$ when $\alpha$ is moderate is (Crank 1948c).

$$ \frac{M_t}{M_\infty} = \frac{1+\alpha}{1+\frac{1}{4}\alpha} \left[ 1 - \exp \left\{ 4(1+\frac{1}{4}\alpha)^2 Dt/(a^2\alpha^2) \right\} \operatorname{erfc} \left\{ 2(1+\frac{1}{4}\alpha)\frac{(Dt/a^2)^{\frac{1}{2}}}{\alpha} \right\} \right]. \quad (5.36) $$

Carman and Haul (1954) have derived an alternative equation which is less easy to use but which is accurate up to considerably higher values of $M_t/M_\infty$. Their equation is

$$ \begin{aligned}\frac{M_t}{M_\infty}=\frac{\gamma_3}{\gamma_3+\gamma_4}\exp\left\{ 4\gamma_3^2Dt/(a^2\alpha^2)\right\}\operatorname{erfc}\left\{\frac{2\gamma_3}{\alpha}\left(\frac{Dt}{a^2}\right)^{\frac{1}{2}}\right\}\\+\frac{\gamma_4}{\gamma_3+\gamma_4}\exp\left\{ 4\gamma_4^2Dt/(a^2\alpha^2)\right\}\operatorname{erfc}\left\{-\frac{2\gamma_4}{\alpha}\left(\frac{Dt}{a^2}\right)^{\frac{1}{2}}\right\},\end{aligned}\qquad(5.37) $$

where

$$ \gamma_3 = \frac{1}{2}\{(1 + \alpha)^{\frac{1}{2}} + 1\}, \quad \gamma_4 = \gamma_3 - 1. \qquad (5.38) $$

For $\alpha$ very small it is convenient to use the asymptotic expansion for erfc in (5.36) and hence to write

$$ \frac{M_t}{M_\infty}=\frac{1+\alpha}{1+\frac{1}{4}\alpha}\left\{ 1-\frac{\alpha(Dt/a^2)^{-\frac{1}{2}}}{2\pi^{\frac{1}{2}}(1+\frac{1}{4}\alpha)}+\frac{\alpha^3(Dt/a^2)^{-\frac{1}{2}}}{16\pi^{\frac{1}{2}}(1+\frac{1}{4}\alpha)^3}-\frac{3\alpha^5(Dt/a^2)^{-\frac{1}{2}}}{128\pi^{\frac{1}{2}}(1+\frac{1}{4}\alpha)^5}+\dots\right\}.\quad(5.39) $$

If $\alpha$ is very large, the following expression is more convenient,

$$ \frac{M_t}{M_\infty}=\frac{2}{\alpha}(1+\alpha)\left\{\frac{2}{\pi^{\ddagger}}\left(\frac{Dt}{a^2}\right)^{\frac{1}{2}}-\left(\frac{1}{2}+\frac{2}{\alpha}\right)\frac{Dt}{a^2}-\frac{4}{3\pi^{\ddagger}}\left(\frac{1}{8}-\frac{2}{\alpha}-\frac{4}{\alpha^2}\right)\left(\frac{Dt}{a^2}\right)^{\frac{1}{2}}+\dots\right\},\quad(5.40) $$

which for the special case of $\alpha = \infty$, becomes

$$ \frac{M_t}{M_\infty} = 2 \left\{ \frac{2}{\pi^{\frac{1}{2}}} \left( \frac{Dt}{a^2} \right)^{\frac{1}{2}} - \frac{1}{2} \frac{Dt}{a^2} - \frac{1}{6\pi^{\frac{1}{2}}} \left( \frac{Dt}{a^2} \right)^{\frac{1}{2}} + \dots \right\}. \qquad (5.41) $$

The derivation of these solutions for small times is given by Crank (1948c). Fig. 5.7 shows curves of $M_t/M_\infty$ against $(Dt/a^2)^\ddagger$ for five values of the final fractional uptake. Berthier (1952) gives a table of $M_t/M_\infty$ for values of $1/\alpha$ between 0 and 1 at intervals of 0.1. As in the plane case his values are not always reliable to three decimal places.

The concentration of solute $C$ within the cylinder is given by

$$C = C_{\infty} \left\{ 1 + \sum_{n=1}^{\infty} \frac{4(\alpha+1) \exp(-Dq_n^2 t/a^2)}{(4+4\alpha+\alpha^2 q_n^2)} \frac{J_0(q_n r/a)}{J_0(q_n)} \right\}. \qquad (5.42)$$

As for the plane sheet (§ 4.3.5, p. 58) the above equations also describe the course of desorption into a well-stirred solution, initially free from solute,

DIFFUSION IN A CYLINDER

79

[图片: |(Dt/a²)¹/²|M₁/Mₘₐₓ (0)|M₁/Mₘₐₓ (30)|M₁/Mₘₐₓ (50)|M₁/Mₘₐₓ (70)|M₁/Mₘₐₓ (90)| |:---:|:---:|:---:|:---:|:---:|:---:| |0.0|0.0|0.0|0.0|0.0|0.0| |0.1|0.2|0.3|0.4|0.5|0.7| |0.2|0.4|0.5|0.6|0.7|0.9| |0.3|0.5|0.7|0.8|0.85|0.98| |0.4|0.6|0.8|0.9|0.95|1.0| |0.5|0.7|0.9|0.95|0.98|1.0| |0.6|0.8|0.95|0.98|0.99|1.0| |0.7|0.9|0.98|0.99|1.0|1.0| |0.8|0.95|0.99|1.0|1.0|1.0| |0.9|0.98|0.995|1.0|1.0|1.0| |1.0|1.0|1.0|1.0|1.0|1.0|]
# FIG. 5.7. Uptake by a cylinder from a stirred solution of limited volume. Numbers on curves show percentages of total solute finally taken up by cylinder.

from a cylinder in which the concentration is initially uniform and equal to $C_0$. The only modifications are that (5.35) is to be replaced by

$$ \frac{M_{\infty}}{\pi a^2 C_0} = \frac{1}{1 + 1/\alpha}, \quad (5.43) $$

and $C_1, (C_1)_{\infty}$ replace $C, C_{\infty}$ in (5.42), where

$$ C_1 = C_0 - C, \quad (C_1)_{\infty} = C_0 - C_{\infty}. \qquad (5.44) $$

# 5.3.4. Surface evaporation

If the cylinder is initially at a uniform concentration $C_2$, and there is a surface condition

$$ -D \partial C / \partial r = \alpha (C_s - C_0), \quad (5.45) $$

where $C_s$ is the actual concentration just within the cylinder and $C_0$ is the concentration required to maintain equilibrium with the surrounding atmosphere, the required solution is

$$ \frac{C - C_2}{C_0 - C_2} = 1 - \sum_{n=1}^{\infty} \frac{2LJ_0(r\beta_n/a)}{(\beta_n^2 + L^2)J_0(\beta_n)} \exp(-\beta_n^2 Dt/a^2). \quad (5.46) $$

80

DIFFUSION IN A CYLINDER

The $\beta_n$s are the roots of

$$ \beta J_1(\beta) - L J_0(\beta) = 0, \quad (5.47) $$

and

$$ L = a\alpha/D, \quad (5.48) $$

a dimensionless parameter. Roots of (5.47) are given in Table 5.2 for several values of $L$. The total amount of diffusing substance $M_t$ entering or leaving the cylinder, depending on whether $C_0$ is greater or less than $C_2$, is expressed as a fraction of $M_\infty$, the corresponding quantity after infinite time, by

$$ \frac{M_t}{M_\infty} = 1 - \sum_{n=1}^{\infty} \frac{4L^2 \exp(-\beta_n^2 Dt/a^2)}{\beta_n^2 (\beta_n^2 + L^2)}. \quad (5.49) $$

The solutions suitable for small values of time, provided $r/a$ is not small, are

$$ \frac{C - C_2}{C_0 - C_2} = \frac{2h(Dta)^{\frac{1}{2}}}{r^{\frac{1}{2}}} \text{ierfc} \frac{a-r}{2\sqrt{(Dt)}} + \frac{4ha^{\frac{1}{2}}Dt}{r^{\frac{1}{2}}} \left\{ \frac{1}{8r} + \frac{3}{8a} - h \right\} i^2 \text{erfc} \frac{a-r}{2\sqrt{(Dt)}} + \dots \quad (5.50) $$

where $h = \alpha/D$, and

$$ \frac{M_t}{M_\infty} = \frac{2DtL}{a^2} - \frac{8L^2}{3\pi^{\frac{1}{2}}}\left(\frac{Dt}{a^2}\right)^{\frac{3}{2}} - L^2\left(\frac{Dt}{a^2}\right)^2 \left(\frac{1}{2}-L\right) - \dots \quad (5.51) $$

Tabulated values of $M_t/M_\infty$ are given by Newman (1931) from which the graphs of Fig. 5.8 are drawn. Newman also gives values of a second function from which $M_t/M_\infty$ can easily be deduced for a parabolic initial distribution.

[图片: |(Dt/a²)¹/²|Mₜ/M∞ (D=0.1)|Mₜ/M∞ (D=0.2)|Mₜ/M∞ (D=0.5)|Mₜ/M∞ (D=1)|Mₜ/M∞ (D=2)|Mₜ/M∞ (D=5)|Mₜ/M∞ (D=10)|Mₜ/M∞ (D=∞)| |:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:| |0|0|0|0|0|0|0|0|0| |1|0.3|0.5|0.8|0.9|0.98|1.0|1.0|1.0| |2|0.6|0.8|0.95|0.98|1.0|1.0|1.0|1.0| |3|0.8|0.95|0.98|1.0|1.0|1.0|1.0|1.0| |4|0.9|0.98|1.0|1.0|1.0|1.0|1.0|1.0| |5|0.95|0.99|1.0|1.0|1.0|1.0|1.0|1.0|]
# FIG. 5.8. Sorption and desorption curves for the surface condition (5.45). Numbers on curves are values of $L = a\alpha/D$.

DIFFUSION IN A CYLINDER

81

# 5.3.5. Constant flux $F_0$ at the surface

If the cylinder is initially at a uniform concentration $C_0$, and there is a constant rate of transfer of diffusing substance $F_0$ per unit area of the surface, i.e.

$$-D \partial C/\partial r = F_0, \quad r = a, \qquad (5.52)$$

then we have

$$C - C_0 = -\frac{F_0 a}{D} \left\{ \frac{2Dt}{a^2} + \frac{r^2}{2a^2} - \frac{1}{4} \right. \\ \left. -2 \sum_{n=1}^{\infty} \exp\left(-D\alpha_n^2 t/a^2\right) \frac{J_0(r\alpha_n/a)}{\alpha_n^2 J_0(\alpha_n)}\right\}, \quad (5.53)$$

where the $\alpha_n$s are the positive roots of

$$J_1(\alpha) = 0. \qquad (5.54)$$

Roots of (5.54) are given in tables of Bessel functions, and the first five roots are to be found in Table 5.2 when $L = 0$. Obviously the amount of diffusing substance lost by unit length of the cylinder in time $t$ is $2\pi aF_0t$. This is a problem which has been discussed in connexion with the drying of clay by Macey (1940, 1942), Jaeger (1944), and others. A solution useful for small values of time is

$$C - C_0 = -\frac{F_0}{D} \left\{ 2\left(\frac{Dat}{r}\right)^{\frac{1}{2}} \text{ierfc} \frac{a-r}{2\sqrt{(Dt)}} \right. \\ \left. + \frac{Dt(a+3r)}{2a^{\frac{1}{2}}r^{\frac{1}{2}}} i^2 \text{erfc} \frac{a-r}{2\sqrt{(Dt)}} + \dots \right\}. \qquad (5.55)$$

Concentration-distance curves, plotted from (5.53) are shown in Fig. 5.9.

# 5.3.6. Impermeable surface

If the surface of the cylinder is impermeable and there is an initial concentration distribution $f(r)$ then

$$C = \frac{2}{a^2} \left\{ \int_0^a r'f(r') dr' + \sum_{n=1}^{\infty} \exp(-D\alpha_n^2 t) \right. \\ \left. \times \frac{J_0(r\alpha_n)}{J_0^2(a\alpha_n)} \int_0^a r'f(r') J_0(\alpha_n r') dr' \right\}, \qquad (5.56)$$

where the $\alpha_n$s are roots of

$$J_1(a\alpha_n) = 0, \qquad (5.57)$$

which are given in standard tables.

82

DIFFUSION IN A CYLINDER

[图片: |r/a|0.01|0.05|0.1|0.2| |:---:|:---:|:---:|:---:|:---:| |0.0|0.02|0.0|0.0|0.18| |0.1|0.03|0.01|0.02|0.19| |0.2|0.04|0.02|0.04|0.2| |0.3|0.05|0.03|0.06|0.21| |0.4|0.06|0.04|0.08|0.23| |0.5|0.07|0.05|0.1|0.25| |0.6|0.08|0.07|0.12|0.28| |0.7|0.09|0.09|0.15|0.31| |0.8|0.1|0.11|0.18|0.35| |0.9|0.11|0.14|0.22|0.4| |1.0|0.12|0.17|0.26|0.45|]
# FIG. 5.9. Concentration distributions in a cylinder for constant flux $F_0$ at the surface. Numbers on curves are values of $Dt/a^2$.

# 5.3.7. Composite cylinder

Various problems of radial diffusion into a composite cylinder comprised of two coaxial cylinders having different diffusion coefficients have been solved (see e.g. Carslaw and Jaeger (1959, p. 345). The extra parameters involved make any attempt at general numerical evaluation too formidable to be attempted here. Some solutions relating to diffusion accompanied by non-linear absorption are discussed in Chapter 9.

Ölcer (1968) summarized the available solutions and solved the composite hollow cylinder problem in a very general form for combined radial and axial diffusion with internal sources included. Stevenson (1974) obtains a solution and gives numerical values typical of a small tubular membrane related to permeability measurements.

# 5.4. The hollow cylinder

Carslaw and Jaeger (1959, p. 207) give the general solution to the problem of the hollow cylinder with the surface $r = a$ maintained at a constant concentration $C_1$, and $r = b$ at $C_2$, when the initial distribution is $f(r)$, in the region $a \le r \le b$. In the special case of a constant initial concentration, $f(r) = C_0$, and when $C_1 = C_2$, the solution is

$$ \frac{C - C_0}{C_1 - C_0} = 1 - \pi \sum_{n=1}^{\infty} \frac{J_0(a\alpha_n)U_0(r\alpha_n)}{J_0(a\alpha_n) + J_0(b\alpha_n)} \exp(-D\alpha_n^2 t). \quad (5.58) $$

where

$$ U_0(r\alpha_n) = J_0(r\alpha_n) Y_0(b\alpha_n) - J_0(b\alpha_n) Y_0(r\alpha_n), \quad (5.59) $$

DIFFUSION IN A CYLINDER

83

and the $\alpha_n$s are the positive roots of

$$U_0(a\alpha_n) = 0. \qquad (5.60)$$

Roots of (5.60) are given in Table 5.3 for different values of b/a. This table is reproduced from Carslaw and Jaeger's book (1959, p. 493). In (5.58) and (5.59) $J_0$ and $Y_0$ are Bessel functions of the first and second kind respectively, of order zero. They are both listed in standard tables. The expression for the amount of diffusing substance entering or leaving the region $a \le r \le b$ in time $t$ is given by

$$ \frac{M_t}{M_\infty} = 1 - \frac{4}{b^2 - a^2} \sum_{n=1}^{\infty} \frac{J_0(a\alpha_n) - J_0(b\alpha_n)}{\alpha_n^2\{ J_0(a\alpha_n) + J_0(b\alpha_n)\}} \exp(-D\alpha_n^2 t). \quad (5.61) $$

In Fig. 5.10, curves of $M_t/M_\infty$ are plotted against $\{Dt/(b-a)^2\}^{\frac{1}{2}}$ for different values of $b/a$.

[图片: |{Dt(b-a)²}¹/²|M₁/M∞ (Plane sheet, b/a=1)|M₁/M∞ (b/a=10)|M₁/M∞ (Solid cylinder, a=0)| |:---:|:---:|:---:|:---:| |0.0|0.0|0.0|0.0| |0.1|0.1|0.1|0.1| |0.2|0.2|0.2|0.2| |0.3|0.3|0.3|0.3| |0.4|0.4|0.4|0.4| |0.5|0.5|0.5|0.5| |0.6|0.6|0.6|0.6| |0.7|0.7|0.7|0.7| |0.8|0.8|0.8|0.8|]
# FIG. 5.10. Uptake curves for hollow cylinder.

84

DIFFUSION IN A CYLINDER

# 5.4.1. Flow through cylinder wall

If the surface $r = a$ is maintained at $C_1$, $r = b$ at $C_2$, and the region $a \le r \le b$ is initially at $C_0$, the concentration approaches the steady-state distribution discussed in § 5.2 (p. 69) according to the expression

$$C = \frac{C_1 \ln(b/r) + C_2 \ln(r/a)}{\ln(b/a)} + \pi C_0 \sum_{n=1}^{\infty} \frac{J_0(a\alpha_n)U_0(r\alpha_n) \exp(-D\alpha_n^2t)}{J_0(a\alpha_n) + J_0(b\alpha_n)} \\ - \pi \sum_{n=1}^{\infty} \frac{\{C_2 J_0(a\alpha_n) - C_1 J_0(b\alpha_n)\} J_0(a\alpha_n)U_0(r\alpha_n)}{J_0^2(a\alpha_n) - J_0^2(b\alpha_n)} \exp(-D\alpha_n^2t), \quad (5.62)$$

where the $\alpha_n$s are roots of (5.60). The amount of diffusing substance entering or leaving the cylinder wall in time $t$ is given by $M_t$, where

$$ \begin{aligned}M_t={}&\frac{1}{2}\pi\frac{(C_2-C_1)(a^2-b^2)}{\ln(b/a)}+\pi\{ b^2(C_2-C_0)-a^2(C_1-C_0)\}\\&+4\pi\sum_{n=1}^{\infty}\frac{\{(C_1-C_0)J_0(b\alpha_n)-(C_2-C_0)J_0(a\alpha_n)\}}{\alpha_n^2\{ J_0(a\alpha_n)+J_0(b\alpha_n)\}}\exp(-D\alpha_n^2t).\quad(5.63)\end{aligned} $$

Normally a quantity of greater practical interest is the amount $Q_t$ escaping from unit length of the outer surface $r = b$. This is readily deduced from (5.62) and is given by obtaining $-2\pi D(r \ \partial c/\partial r)_{r=b}$ and integrating with respect to time $t$. In the most commonly occurring case $C_0 = C_2 = 0$, and we then find

$$ \frac{Q_t}{\pi C_1} = \frac{2(Dt-L)}{\ln(b/a)} - 4 \sum_{n=1}^{\infty} \frac{J_0(a\alpha_n)J_0(b\alpha_n) \exp(-D\alpha_n^2t)}{\alpha_n^2\{J_0^2(a\alpha_n) - J_0^2(b\alpha_n)\}}. \quad (5.64) $$

For a given $b/a$ the graph of $Q_t/(\pi b^2 C_1)$ against $t$ approaches, at large $t$, a straight line which makes an intercept $L$ on the $t$-axis given by

$$ \frac{a^2 - b^2 + (a^2 + b^2) \ln (b/a)}{4 \ln (b/a)}. \qquad (5.65) $$

As Barrer (1951) suggests, this intercept provides a means of measuring the diffusion coefficient $D$ for a material in the form of a hollow cylinder. Fig. 5.11 shows graphs of $Q_t/(\pi b^2 C_1)$, the amount evaporated from unit area of the outer surface $r = b$, as a function of $Dt/(b-a)^2$ for different values of $b/a$.

# 5.4.2. A general boundary condition

Jaeger (1940) has given the solution to the problem of diffusion into a hollow cylinder in which the concentration is initially zero and the boundary conditions on the two surfaces are

$$k_1 \frac{\partial C}{\partial t} + k_2 \frac{\partial C}{\partial r} + k_3 C = k_4, \quad r = a, \qquad (5.66)$$

DIFFUSION IN A CYLINDER

85

[图片: |Dt/(b-a)²|Q/πb²C₁ (曲线4)|Q/πb²C₁ (曲线2)|Q/πb²C₁ (曲线1.5)|Q/πb²C₁ (曲线1.2)| |:---:|:---:|:---:|:---:|:---:| |0.1|0.0|0.0|0.0|0.0| |0.2|0.02|0.02|0.02|0.01| |0.3|0.07|0.06|0.05|0.02| |0.4|0.14|0.12|0.1|0.04| |0.5|0.22|0.18|0.15|0.07| |0.6|0.3|0.25|0.21|0.1| |0.7|0.37|0.32|0.27|0.14| |0.8|0.4|0.37|0.33|0.18|]
# FIG. 5.11. Approach to steady-state flow through wall of cylinder. Numbers on curves are values of $b/a$.

$$ k'_1 \frac{\partial C}{\partial t} + k'_2 \frac{\partial C}{\partial r} + k'_3 C = k'_4, \quad r = b. \qquad (5.67) $$

These conditions include as special cases.

(i) Constant concentrations, $C_1$ on $r = a$ and $C_2$ on $r = b$, when $k_1 = k_2 = k'_1 = k'_2 = 0$, $k_4/k_3 = C_1$, $k'_4/k'_3 = C_2$.

(ii) Evaporation conditions on the surfaces:

$$ -D \partial C / \partial r = \gamma_1 (C_1 - C), \quad r = a, \qquad (5.68) $$

$$ -D \partial C / \partial r = \gamma_2 (C - C_2), \quad r = b, \qquad (5.69) $$

when $k_1 = k'_1 = 0$, $k_2 = k'_2 = D$, $k_3 = -\gamma_1$, $k_4 = -\gamma_1C_1$, $k'_3 = \gamma_2$, $k'_4 = \gamma_2C_2$. This includes the obvious modification for an impermeable surface.

(iii) Diffusion proceeding from a well-stirred solution occurring in the region $0 \le r \le a$, the concentration at $r = a$ being always the same as that throughout the solution; the surface $r = b$ impermeable. At $r = a$ the condition is

$$\pi a^2 \partial C / \partial t = 2\pi a D \frac{\partial C}{\partial r}, \quad r = a,$$

86

DIFFUSION IN A CYLINDER

i.e.

$$ \frac{\partial C}{\partial t} - \frac{2D}{a} \frac{\partial C}{\partial r} = 0, \quad r = a, \qquad (5.70) $$

and we have also

$$ \partial C/\partial r = 0, \qquad r = b, \qquad (5.71) $$

so that $k_1 = k'_2 = 1$, $k_2 = -2D/a$, $k'_1 = k'_3 = k'_4 = k_3 = k_4 = 0$. Other cases, such as that of diffusion from a well-stirred solution in the region $0 \le r \le a$ with the surface $r = b$ maintained at a constant concentration, or the surface $r = a$ maintained at a constant concentration while there is loss by evaporation from the surface $r = b$, and other combinations of these boundary conditions are all deducible from the general solution. The derivation of the solution by the use of Laplace transforms is given by Jaeger (1940) (Carslaw and Jaeger 1959, p. 332). The final result is

$$ C=\frac{ak_4\{ k^{\prime}_2-bk^{\prime}_1\ln(r/b)\}-bk^{\prime}_4\{ k_2-ak_3\ln(r/a)\}}{ak_3k^{\prime}_2-bk_2k^{\prime}_3-abk_3k^{\prime}_3\ln(a/b)}}{-\pi\sum_{n=1}^{\infty}\exp(-D\alpha_n^2t)F(\alpha_n)C_0(r;\alpha_n)[k_4\{ A^{\prime}_nJ_0(b\alpha_n)-k^{\prime}_2\alpha_nJ_1(b\alpha_n)\}}\\-k^{\prime}_4\{ A_nJ_0(a\alpha_n)-k_2\alpha_nJ_1(a\alpha_n)\}],\qquad(5.72) $$

where

$$ \left. \begin{array}{l} A_n = k_3 - Dk_1 \alpha_n^2; \\ B = k_2 + 2Dk_1/a; \end{array} \right. \quad \begin{aligned} A_n' &= k_3' - Dk_1' \alpha_n^2 \\ B' &= k_2' + 2Dk_1'/b \end{aligned} \right\}, \qquad (5.73) $$

$$C_0(r; \alpha_n) = J_0(r\alpha_n) \{ A_n Y_0(a\alpha_n) - k_2\alpha_n Y_1(a\alpha_n)\} \\ - Y_0(r\alpha_n) \{ A_n J_0(a\alpha_n) - k_2\alpha_n J_1(a\alpha_n)\}, \qquad (5.74)$$

$$ F(\alpha_n)=\frac{A_n^{\prime}J_0(b\alpha_n)-k_2^{\prime}\alpha_nJ_1(b\alpha_n)}{\{ A_n^{\prime}J_0(b\alpha_n)-k_2^{\prime}\alpha_nJ_1(b\alpha_n)\}^2(A_n^2+k_2B\alpha_n^2)},\quad(5.75) $$

and where the $\alpha_n$s are the positive roots of

$$ \begin{aligned}&\{(k_3-k_1D\alpha^2)J_0(a\alpha)-k_2\alpha J_1(a\alpha)\}\{(k^{\prime}_3-k^{\prime}_1D\alpha^2)Y_0(b\alpha)-k^{\prime}_2\alpha Y_1(b\alpha)\}\\&\qquad-\{(k^{\prime}_3-k^{\prime}_1D\alpha^2)J_0(b\alpha)-k^{\prime}_2\alpha J_1(b\alpha)][(k_3-k_1D\alpha^2)Y_0(a\alpha)-k_2\alpha Y_1(a\alpha)\}=0.\\&\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qqua

DIFFUSION IN A CYLINDER

87

# 5.5. The region bounded internally by the cylinder $r = a$

(i) If the initial concentration throughout the region $r > a$ is $C_0$, and the surface $r = a$ is maintained at $C_1$, then

$$ \frac{C - C_0}{C_1 - C_0} = 1 + \frac{2}{\pi} \int_0^\infty \exp(-Du^2t) \frac{J_0(ur)Y_0(ua) - Y_0(ur)J_0(ua)}{J_0^2(ua) + Y_0^2(ua)} \frac{du}{u}. \quad (5.77) $$

A solution useful for small times is

$$ \frac{C - C_0}{C_1 - C_0} = \left(\frac{a}{r}\right)^{\frac{1}{2}} \text{erfc } \frac{r-a}{2\sqrt{(Dt)}} + \frac{(r-a)(Dt)^{\frac{1}{2}}}{4a^{\frac{1}{2}}r^{\frac{3}{2}}} \text{ierfc } \frac{r-a}{2\sqrt{(Dt)}} + \frac{Dt(9a^2 - 2ar - 7r^2)}{32a^{\frac{3}{2}}r^{\frac{3}{2}}} i^2 \text{erfc } \frac{r-a}{2\sqrt{(Dt)}} + \dots \quad (5.78) $$

Fig. 5.12 shows how concentration depends on radius at successive times. The expression for the amount of diffusing substance F crossing unit area of the surface r = a in unit time is

$$ F = -D \left( \frac{\partial C}{\partial r} \right)_{r=a} = \frac{4(C_1 - C_0)D}{\pi^2 a} \int_0^\infty \exp(-Du^2t) \frac{du}{u\{J_0^2(au) + Y_0^2(au)\}}. \quad (5.79) $$

Numerical values of the integral in (5.79) have been tabulated by Jaeger and Clarke (1942) and are shown graphically by Carswal and Jaeger (1959, p. 388). For small times we have

$$ F = \frac{D(C_1 - C_0)}{a} \{ (\pi T)^{-\frac{1}{2}} + \frac{1}{2} - \frac{1}{4} (T/\pi)^{\frac{1}{2}} + \frac{1}{8} T - \dots \}, \quad (5.80) $$

[图片: |(C-C₀)/(C₁-C₀)|r/a (曲线 4)|r/a (曲线 1)|r/a (曲线 1/4)| |:---:|:---:|:---:|:---:| |0.6|1.4|1.7|1.9| |0.4|1.7|2.1|2.3| |0.2|2.3|2.7|2.8| |0.1|3.0|3.4|3.5|]
# FIG. 5.12. Concentration-distance curves in the region $r > a$. Numbers on curves are values of $Dt/a^2$.

88

DIFFUSION IN A CYLINDER

and for large times

$$ F = \frac{2D}{a} (C_1 - C_0) \left[ \frac{1}{\ln(4T) - 2\gamma} - \frac{\gamma}{\{\ln(4T) - 2\gamma\}^2} - \dots \right], \quad (5.81) $$

where $T = Dt/a^2$ and $\gamma = 0.57722$ is Euler's constant.

(ii) If the region $r > a$ is initially at a uniform concentration $C_0$, and there is transfer of diffusing substance across $r = a$ according to

$$ -D \partial C / \partial r = \alpha(C - C_1), \quad r = a, \qquad (5.82) $$

then we have

$$ \begin{aligned}\frac{C-C_1}{C_0-C_1}={}&-\frac{2h}{\pi}\int_0^\infty\exp(-Du^2t)\\&\times\frac{J_0(ur)\{ uY_1(ua)+hY_0(ua)\}-Y_0(ur)\{ uJ_1(ua)+hJ_0(ua)\}}{\{ uJ_1(ua)+hJ_0(ua)\}^2+\{ uY_1(ua)+hY_0(ua)\}^2}\frac{\mathrm{d} u}{u},(5.83)\end{aligned} $$

where $h = \alpha/D$. Graphs showing how $(C-C_1)/(C_0-C_1)$ at the surface $r = a$ varies with time have been drawn by Carslaw and Jaeger, (1959 p. 338), for several values of $ah$. Clearly because of (5.82) these curves also show the rate of transfer across unit area of the surface $r = a$. Carslaw and Jaeger (1959, p. 338) also give the solution of the corresponding problem when there is a constant rate of flow of diffusing substance across the surface $r = a$.

# 6

## DIFFUSION IN A SPHERE

## 6.1. Introduction

IF we restrict ourselves to cases in which the diffusion is radial, the diffusion equation for a constant diffusion coefficient takes the form

$$ \frac{\partial C}{\partial t} = D \left( \frac{\partial^2 C}{\partial r^2} + \frac{2}{r} \frac{\partial C}{\partial r} \right). \qquad (6.1) $$

On putting

$$ u = Cr, \qquad (6.2) $$

(6.1) becomes

$$ \frac{\partial u}{\partial t} = D \frac{\partial^2 u}{\partial r^2}. \qquad (6.3) $$

Since this is the equation for linear flow in one dimension, the solutions of many problems in radial flow in a sphere can be deduced immediately from those of the corresponding linear problems.

### 6.2. Steady state

In this case the equation is

$$ \frac{d}{dr} \left( r^2 \frac{dC}{dr} \right) = 0, \qquad (6.4) $$

of which the general solution is

$$ C = B + A/r, \quad (6.5) $$

where $A$ and $B$ are constants to be determined from the boundary conditions. If in the hollow sphere, $a \le r \le b$, the surface $r = a$ is kept at a constant concentration $C_1$, and $r = b$ at $C_2$, then

$$ C = \frac{aC_1(b-r) + bC_2(r-a)}{r(b-a)}. \quad (6.6) $$

The quantity of diffusing substance $Q_t$ which passes through the spherical wall in time $t$ is given by

$$ Q_t = 4\pi Dt \frac{ab}{b-a} (C_2 - C_1). \quad (6.7) $$

90

DIFFUSION IN A SPHERE

If $Q_t$ is measured in a concentration-dependent system, the mean value of the diffusion coefficient obtained from (6.7) is

$$ \left( \int_{C_2}^{C_1} D dC \right) / (C_1 - C_2) $$

as for the plane sheet (see eqn. (4.11)).

If the surface $r = a$ is maintained at a concentration $C_1$ and at $r = b$ there is evaporation according to the condition

$$ \frac{dC}{dr} + h(C - C_2) = 0, \quad r = b, \qquad (6.8) $$

we find

$$ C = \frac{aC_1\{hb^2 + r(1-hb)\} + hb^2C_2(r-a)}{r\{hb^2 + a(1-hb)\}}. \quad (6.9) $$

The amount $Q_t$ passing through the spherical wall in time $t$ is now given by

$$ Q_t = \frac{4\pi Dthab^2(C_1 - C_2)}{hb^2 + a(1 - hb)}. \quad (6.10) $$

If $ah > 2$, the rate of diffusion decreases steadily as $b$ increases, but if $ah < 2$ the rate first increases and later decreases, passing through a maximum when $b = 2/h$. As in the case of the cylinder, this maximum is due to the combination of a decreasing gradient and an increasing surface area as $b$ is increased.

If the surface conditions are

$$ \partial C / \partial r + h_1(C_1 - C) = 0, \quad r = a; \quad \partial C / \partial r + h_2(C - C_2) = 0, \quad r = b, \qquad (6.11) $$

the solutions are:

$$ C = \frac{C_1 a^2 h_1 \{b^2 h_2 - r(bh_2 - 1)\} + C_2 b^2 h_2 \{r(ah_1 + 1) - a^2 h_1\}}{r \{b^2 h_2(ah_1 + 1) - a^2 h_1(bh_2 - 1)\}}, \quad (6.12) $$

and

$$Q_t = \frac{4\pi a^2 b^2 h_1 h_2 Dt(C_1 - C_2)}{b^2 h_2 (ah_1 + 1) - a^2 h_1 (bh_2 - 1)}. \quad (6.13)$$

# 6.3. Non-steady state

## 6.3.1. Surface concentration constant: initial distribution $f(r)$

If we make the substitution $u = Cr$, suggested above, the equations for $u$ are

$$ \frac{\partial u}{\partial t} = D \frac{\partial^2 u}{\partial r^2}, \qquad (6.14) $$

DIFFUSION IN A SPHERE

91

$$ u = 0, \quad r = 0, \quad t > 0, \quad (6.15) $$

$$ u = aC_0, \quad r = a, \quad t > 0, \quad (6.16) $$

$$ u = rf(r), \quad t = 0, \quad 0 < r < a, \qquad (6.17) $$

where $C_0$ is the constant concentration at the surface of the sphere. These are the equations of diffusion in a plane sheet of thickness $a$, with its ends, $r = 0$ and $r = a$, kept at zero and $aC_0$ respectively, and with the initial distribution $rf(r)$. This problem has been considered in § 4.3.1 (p. 47) and the solution follows immediately by making the appropriate substitutions in eqn (4.16). If the sphere is initially at a uniform concentration $C_1$ and the surface concentration is maintained constant at $C_0$, the solution becomes

$$ \frac{C - C_1}{C_0 - C_1} = 1 + \frac{2a}{\pi r} \sum_{n=1}^{\infty} \frac{(-1)^n}{n} \sin \frac{n\pi r}{a} \exp(-Dn^2\pi^2t/a^2). \quad (6.18) $$

The concentration at the centre is given by the limit as $r \to 0$, that is by

$$ \frac{C - C_1}{C_0 - C_1} = 1 + 2 \sum_{n=1}^{\infty} (-1)^n \exp(-Dn^2\pi^2t/a^2). \quad (6.19) $$

The total amount of diffusing substance entering or leaving the sphere is given by

$$ \frac{M_t}{M_\infty} = 1 - \frac{6}{\pi^2} \sum_{n=1}^{\infty} \frac{1}{n^2} \exp(-Dn^2\pi^2t/a^2). \quad (6.20) $$

The corresponding solutions for small times are:

$$ \frac{C - C_1}{C_0 - C_1} = \frac{a}{r} \sum_{n=0}^{\infty} \left\{ \text{erfc} \frac{(2n+1)a - r}{2\sqrt{(Dt)}} - \text{erfc} \frac{(2n+1)a + r}{2\sqrt{(Dt)}} \right\}, \quad (6.21) $$

and

$$ \frac{M_t}{M_\infty} = 6 \left( \frac{Dt}{a^2} \right)^{\frac{1}{2}} \left\{ \pi^{-\frac{1}{2}} + 2 \sum_{n=1}^{\infty} \text{ierfc} \frac{na}{\sqrt{ (Dt)}} \right\} - 3 \frac{Dt}{a^2}. \quad (6.22) $$

These solutions can be written in terms of the two dimensionless parameters $Dt/a^2$ and $r/a$. Curves showing $(C-C_1)/(C_0-C_1)$ as a function of $r/a$ for different values of $Dt/a^2$, drawn by Carswal and Jaeger (1959, p. 235) are reproduced in Fig. 6.1. The curve for zero fractional exhaustion on Fig. 6.4 shows $M_1/M_\infty$ as a function of $Dt/a^2$.

# 6.3.2. Variable surface concentration

If the initial concentration in the sphere is zero and that at the surface is $\phi(t)$ the solution is

$$ C = -\frac{2D}{ra} \sum_{n=1}^{\infty} (-1)^n \exp(-Dn^2\pi^2t/a^2)n\pi \sin \frac{n\pi r}{a} \int_0^t \exp(Dn^2\pi^2\lambda/a^2)\phi(\lambda) \, \mathrm{d}\lambda. \quad (6.23) $$

92

DIFFUSION IN A SPHERE

[图片: |r/a|(C-C∞)/(C₀-C∞)| |:---:|:---:| |0|0.4| |0|0.3| |0|0.2| |0|0.15| |0|0.1| |0|0.08| |0|0.06| |0|0.04| |0|0.03| |0|0.02| |0|0.01| |0|0.005|]
# FIG. 6.1. Concentration distributions at various times in a sphere with initial concentration $C_1$ and surface concentration $C_0$. Numbers on curves are values of $Dt/a^2$.

(i) When

$$ \phi(t) = C_0\{1 - \exp(-\beta t)\}, \quad (6.24) $$

(6.23) becomes

$$ \frac{C}{C_0} = 1 - \frac{a}{r} \exp(-\beta t) \frac{\sin\{(\beta a^2/D)^\frac{1}{2}r/a\}}{\sin\{\beta a^2/D\}^{\frac{1}{2}}} - \frac{2\beta a^3}{\pi Dr} \sum_{n=1}^{\infty} (-1)^n \frac{\exp(-Dn^2\pi^2t/a^2)}{n(n^2\pi^2 - \beta a^2/D)} \sin \frac{n\pi r}{a}, \quad (6.25) $$

and the sorption-time curve is given by

$$ \frac{3M_t}{4\pi a^3 C_0} = 1 - \frac{3D}{\beta a^2} \exp(-\beta t) \left\{ 1 - \left(\frac{\beta a^2}{D}\right)^{\frac{1}{2}} \cot\left(\frac{\beta a^2}{D}\right)^{\frac{1}{2}} \right\} \\ + \frac{6\beta a^2}{\pi^2 D} \sum_{n=1}^{\infty} \frac{\exp(-Dn^2\pi^2t/a^2)}{n^2(n^2\pi^2 - \beta a^2/D)}. \quad (6.26) $$

# Fig. 6.2 shows uptake curves for different values of the parameter $\beta a^2/D$.

DIFFUSION IN A SPHERE

93

[图片: |(Dt/a²)¹/²|3Mₜ/4πa²C₀ (t=0.01)|3Mₜ/4πa²C₀ (t=0.1)|3Mₜ/4πa²C₀ (t=0.5)|3Mₜ/4πa²C0 (t=1.0)|3Mₜ/4πa²C₀ (t=5.0)|3Mₜ/4πa²C₀ (t=∞)| |:---:|:---:|:---:|:---:|:---:|:---:|:---:| |0.0|0.0|0.0|0.0|0.0|0.0|0.0| |1.0|0.01|0.16|0.7|0.96|1.0|1.0| |2.0|0.04|0.4|0.88|0.99|1.0|1.0| |3.0|0.07|0.6|0.96|1.0|1.0|1.0| |4.0|0.1|0.76|0.98|1.0|1.0|1.0| |5.0|0.2|0.9|0.99|1.0|1.0|1.0|]
# FIG. 6.2. Calculated sorption curves for surface concentration given by $C_0\{1-\exp(-\beta t)\}$. Numbers on curves are values of $\beta a^2/D$.

(ii) If the surface concentration varies linearly with time, i.e.

$$ \phi(t) = kt. \qquad (6.27) $$

the solutions are:

$$ C = k \left( t - \frac{a^2 - r^2}{6D} \right) - \frac{2ka^3}{D\pi^3 r} \sum_{n=1}^{\infty} \frac{(-1)^n}{n^3} \exp(-Dn^2\pi^2t/a^2) \sin \frac{n\pi r}{a}, \quad (6.28) $$

and

$$ \frac{M_t}{\frac{4}{3}\pi a^3 k} = \left( t - \frac{a^2}{15D} \right) + \frac{6a^2}{\pi^4 D} \sum_{n=1}^{\infty} \frac{1}{n^4} \exp(-Dn^2\pi^2 t/a^2). \quad (6.29) $$

$M_t D/(\frac{4}{3}\pi a^5 k)$ is plotted against $Dt/a^2$ in Fig. 6.3.

# 6.3.3. Diffusion from a well-stirred solution of limited volume

The problem and method of solution are very similar to those of the plane sheet and the results can be given without explanation. Suppose that the sphere occupies the space $r < a$, while the volume of the bath of solution (excluding the space occupied by the sphere) is $V$. The concentration of solute in the solution is always uniform and is initially $C_0$. The sphere is initially

94

DIFFUSIO N IN A SPHERE

o-5 r

0-4

0-3

0-2

01

00

01

0-2

0-3

0-4

0-5

Dt/a2

FIG. 6.3. Sorption curve for  sphere with surface concentration kt.

free from solute. The total amount of solute Mt in the sphere after time t is expressed as a fraction of the corresponding quantity after infinite time by the relation

- - i - I

where the qns are the non-zero roots of

(6.30)

(6.31)

and a = 3V/(4na3), the ratio of the volumes of solution and sphere, or if there is a partition factor K between solute in equilibrium in the sphere and the solution, a = 3V/(4na3K). The parameter a is expressed in terms of the final fractional uptake of solute by the sphere by the relation

1

1+a

(6.32)The roots of (6.31) are given in Table 6.1 for several values of a. An alternative solution suitable for smal times given by Carman and Haul (1954) is

7i+}' 2

I a \a-+ higher terms,

yi+y2

(6.33)

DIFFUSIO N IN A SPHERE

95

where in their notation

and

1},

(6.34)

e erfc z = exp z2 erfc z.

(6.35)

In Fig. 6.4, MJM  ̂ against (Dt/a2)*  is plotted for five final fractional uptakes.

Berthier (1952) gives a table of MJM  ̂ for values of I/a between 0 and 1 at intervals of 0-1. His values are not always reliable to three decimal places.

1 0 r

0-0 01

0-2 0-3 0-4 0-5 0-6 0-7 0-8

FIG . 6.4. Uptake by a sphere from a stirred solution of limited volume. Numbers on curves show percentage of solute finally taken up by sphere.

The concentration of solute C within the sphere is given by 6(1 + a) exp ( - Dg2t/a2) a sin (qnr/a):2

r sin qn

(6.36)

96

DIFFUSIO N IN A SPHERE

The above equations also describe the course of desorption into a wellstirred solution, initially free from solute, from a sphere in which the concentration is uniform and equal to Co. The only modifications are that (6.32)is to be replaced by

and Cj, (Cj)^ replace C, Cm in (6.36), where

C^Co-C, (Cl)o0 = C0-Cx.

(6.38)

6.3.4. Surface evaporation

If the sphere is initially at a uniform concentration Cl, and there is a surface condition

= (x(Cs-C0\

(6.39)where Cs is the actual concentration just within the sphere, and Co is the concentration required to maintain equilibrium with the surrounding atmosphere, the required solution is

C - Co =2La « exp (-Dtft/a2) sin j^r/a

C i - Co r ^ {/?n2 + L(L- l ) }  sin/?, "

The fins are the roots of

- l = 0,

(6.41)

and

L = a*/D.

(6.42)Some roots of (6.41) are given in Table 6.2. The expression for the total amount of diffusing substance entering or leaving the sphere is

M, , £ 6L2exp(-/?n2Pt/a2)

Fig. 6.5 shows curves of MJM  ̂ plotted as functions of (Dt/a2)  ̂ for several values of L for which Newman (1931) gives tabulated solutions.

6.3.5. Constant flux F0 at the surface

If the sphere is initially at a uniform concentration Co, and there is a constant rate of transfer Fo per unit area of surface, i.e.

-DdC/dr = Fo, r = a,

(6.44)

then we have

1 r2 3 a " sin (anr)

,

]

DIFFUSION IN A SPHERE

97

FIG. 6.5. Sorption or desorption curves for the surface condition (6.39). Numbers on curves are values of L = aa/D.

where the aocns are the positive roots of

aaMcot aoLn =

(6.46)

The amount of diffusing substance lost by the sphere in time t is 4na2Fot.

Some roots of (6.46) are given in Table 6.2 when L = 0. Fig. 6.6 shows curves of D(C0 — C)/(Foa) plotted against r/a for different values of Dt/a2.

6.3.6. Impermeable surface

If the surface of the sphere is impermeable and there is an initial concentration f(r) then

3 Ca

2 °°

C = ^ \ r2/(r)dr + - Xa Jo arn=l

where the ans are the positive roots of (6.46).

sin ci r Ca

^ -

r'/(r')sinanr'dr',

in ocnaj0)-si

(6.47)

6.3.7. Composite sphere

Problems of diffusion into a composite sphere comprised of an inner core and an outer shel for which the diffusion coefficients are different have been considered by Carslaw and Jaeger (1959, p. 351), Bromwich(1921), Carslaw (1921), Carslaw and Jaeger (1939), Bell (1945), and others.

The extra parameters involved make any attempt at general numerical evaluation too formidable to be attempted here.

98

DIFFUSIO N I N A SPHERE

00

FIG . 6.6. Concentration distribution s in a sphere for  constant flux Fo at the surface. Numbers on curves are values of Dt/a2.

6.4. Hollow sphere

Carslaw and Jaeger (1959, p. 246) give the general solution to the problem of the hollow sphere with the surface r = a maintained at a constant concentration C1? and r = b at C2, when the initial distribution is f(r) in the region a ^ r ^ b. Some special cases have been considered by Barrer (1944)who also suggests a number of practical systems to which his solutions might be applied. In the special case of a constant initial concentration, f(r) = Co,and when Cx = C2, the solution is

c-c 0

b c os nn — a\ . nnir — a) ,

->->„,

-,,

1 s in - ^

exp {  - Dn2n2t/(b - a)2}

b-a

(6.48)The total amount of diffusing substance entering or leaving the hollow sphere a ^ r ^ b in time t is given by

M, =

M

b cos nn — a

(6.49)

DIFFUSION IN A SPHERE

99

1-0

0-9

0-8

0-7

8 0-6 s

0-4

0-3

0-2

01

00

01

0-2 0-3 0-4 0-5 0-6 0-7 0-8

FIG. 6.7. Uptake curves for hollow sphere.

Graphs of MJM  ̂ against {Dt/(b — a)2}*  are shown in Fig. 6.7 for different values of b/a.

6.4.1. Flow through spherical wall

If the surface r = a is maintained at Cx, and r = b at C2, and the region a ^ r ^ b is initially at Co, the concentration approaches the steady-state distribution discussed in § 6.2, according to the expression

aC, (bC2-aCl){r-a)

2

r

r(b — a)

rn,

b(C2-C0) cos nn-aiC  ̂ Co)

x sinM " ( r

ahxp{-Dn27i2t/(b-a)2}.

b — a

(6.50)

100

DIFFUSION IN A SPHERE

The total amount which accumulates in the spherical wall in time t is M f ,where

ab

(\ 4- h* 4-

2

M, - >-*)[(s 2

— v

Qxp{-Dn2n2t/(b-a)2}

, — lab cos nn

- - C o

(6.51)

The quantity which is usually of greater practical importance is Qn the amount escaping say from the outer surface r = b. In the simplest case,when Co = C2 = 0, we find

n

i 9

-7-4 Z

6 n z n = l

(6.52)

As r -> oo, the graph of (6.52) when plotted against Dt/(b — a)2 approaches a straight line which has an intercept on the time axis given by

Dt

1

(6.53)

(b -a )2 6'

As in the case of the plane sheet and the cylinder, this intercept can be used

osr

01 0-2 0-3 0-4 0-5 0-6

FIG. 6.8. Approach to steady-state flow through the wall of a sphere.

DIFFUSIO N IN A SPHERE

101

to determine the diffusion coefficient D experimentally (Barrer 1951).

Fig. 6.8 shows the way in which the graph of (6.52) approaches the straight line.

6.4.2. Surface evaporation

Carslaw and Jaeger (1959, p. 246) give a solution to the problem in which evaporation into an atmosphere of zero vapour pressure occurs at r = a and r = b according to the expressions

k1—-h1C = 0, r = a,

(6.54)

k2-— + h2C = 0, r = b.

(6.55)

If the initial concentration distribution in the spherical wall is /(r), the solution is

C = - f exp {-Da2ntRn{r)} f r'Rn(r')f(r')  dr' ,

(6.56)

where

G = ahi+k^, H = bh2-k2,

(6.57)

(H2 + b2k22cx.2f{G sin(r-a)<xn + ak  ̂ cos (r- a)an{{b-a){a2k\oL2n+G2){b2k22a2n+H2) + {Hakx^

(6.58)

and +an, n = 1,2,.. are the roots of 2

)cos(fo-a)a = 0. (6.59)

By putting either or both /cx and k2 zero we obtain the solutions for one or both surfaces maintained at zero concentration, and similarly hl or h2 zero corresponds to an impermeable surface. If both hx and h2 are zero, so that both surfaces are impermeable, a term

is to be added to (6.56).

If evaporation takes place into atmospheres of different vapour pressures the solution can be deduced from the above by following the method used by Carslaw and Jaeger (1959, p. 118) for the plane sheet. Thus we write

102

DIFFUSIO N IN A SPHERE

C = u + w, where w is a function of r only, satisfying d

dr du

= 0, a < r < b,

= ft,

so that

u =

and w is a function of r and t such that

dw D d I  2dw

dw

dw

2-—

a < r < b,

i— /iivv = 0,

r = a,

or

r = ft,

and hence w is given by (6.56) on using f{r)  — u for f(r).

6.5. The region bounded internally by the sphere r = a

Solutions of this problem follow readily from those of the corresponding problems of the semi-infinite sheet by using the transformation u = Cr.

(i) If the region r > a is initially at a uniform concentration Co, and the surface r = a is maintained at Cx, the solution is

C-Co a

r-a

= - erfc -2y/(Dty

(6.60)

which is readily evaluated using Table 2.1.

(ii) If the initial concentration is Co, and there is a boundary condition

= h{Cl-C\

r = a9

(6.61)

DIFFUSIO N IN A SPHERE

103

then we find

C—Co

ha2 r n r — a

,

- , ,

[ r — a

\ e r f c e x P {h'(ra) + h'2Dt\ erfc ^^-77—:- e xP {h'(r-a) + h'2 t\ erfc ̂

(6.62)

where /?' = /z + (l/a). The ratio (C — C^KC  ̂ — Co) on the surface, r = a, is y O - exp(/2/2Dt)erfc/zV(Dr)},

(6.63)

which again is readily evaluated from Table 2.1.

CONCENTRATION-DEPENDENT DIFFUSION:METHODS OF SOLUTION

7.1. Time-dependent diffusion coefficients

I  N Chapters 2-6 mathematical solutions were presented for various problems in which the diffusion coefficient was taken to be constant. These solutions can also be used if the diffusion coefficient D depends on the time t for which diffusion has been proceeding but is independent of other variables, i.e. if D is a function of t only. In this case the equation for diffusion in one dimension becomes

- -5,

(7.1)

and on writing

dT=D(t)dt,

(7.2)

i.e.

T= f D(t')dt\

(7.3)

equation (7.1) reduces to

^ - ^

(7 4)

The solutions for constant D can therefore be used to give C as a function of x and T, and T is then converted into t using the relationship (7.3). If the integral in (7.3) cannot be evaluated formally, the relationship between T and t has to be obtained by graphical or numerical integration. If the boundary conditions involve time explicitly, e.g. if the surface concentration is a given function of t, this function must be rewritten in terms of T in order to obtain the appropriate solution of (7.4) in x and T. The transformation (7.2)of course, can be used for all forms of the diffusion equation, e.g. for diffusion in a plane sheet, cylinder, or sphere.

Dodson (1973) used (7.3) in a problem of diffusion in a cooling solid presented by the calculation of the age of a rock or mineral from its accumulated products of radioactive decay. His equation takes the form

dc/dt =

METHOD S OF SOLUTIO N

105

which in terms of the variables q = l - e ~a ' - c ,

M = j D(0)e~'df = D(0)(l-e~')

becomes

dq/du = V2q.

Solutions for a time-dependent surface condition on q are deduced by Dodson from general forms by Carslaw and Jaeger (1959).

7.2. Concentration-dependent diffusion: infinit e and semi-infinite media

A case of great practical interest is that in which the diffusion coefficient depends only on the concentration of diffusing substance. Such a concentration-dependence exists in most systems, but often, e.g. in dilute solutions, the dependence is slight and the diffusion coefficient can be assumed constant for practical purposes. In other cases, however, such as the diffusion of vapours in high-polymer substances, the concentration dependence is a very marked,characteristic feature. A number of methods have been used to obtain numerical solutions, some applicable to any type of concentration-dependent diffusion coefficient, and others restricted to particular types, e.g.

exponential or linear dependence. In other cases, algebraic solutions have been expressed in terms of a single integral and these will be referred to as formal solutions even though the integral has to be evaluated numerically.

7.2.1. Boltzmann s transformation

The equation for one-dimensional diffusion when the diffusion coefficient D is a function of concentration C is

cC _ d

dt ~ dx ox

(7.5)

Boltzmann (1894) showed that for certain boundary conditions, provided D is a function of C only, C may be expressed in terms of a single variable x/2t* and that (7.5) may therefore be reduced to an ordinary differential equation by the introduction of a new variable rj, where

r\ = \x/t*.

(7.6)

Thus we have

dC 1 dC

( 7 ?)

and

dC

x dC

(7>8)

106

CONCENTRATION-DEPENDEN T DIFFUSION :

and hence

dxDd_C_~dx

D

4r dry

so that finally (7.5) becomes

dC

dC

(7.9)

(7.10)an ordinary differential equation in C and rj. The transformation (7.6)can be used when diffusion takes place in infinite or semi-infinite media provided the concentration is initially constant in the regions x ^ 0 or x > 0 as the case may be. For the problem defined by

eqn (7.10)

Similarly,

become

C

c

is to be solved

the conditions

C

c

=

cl

= c2

x < 0,x > 0,

t = 0,

r  = 0,

for the boundary conditions

C =

for a

= C0

= cx c c

C i ,

7̂ —

C2, */ =semi-infinite x = 0,x > 0,

= Q, 17= Cl 5 7̂

- 0 0 ,

+ OO.

medium

t >0,

t = 0,

= 0,

= 00.

(7.11)(7.12)

(7.13)(7.14)

(7.15)(7.16)

(7.17)(7.18)It is only when the initial and boundary conditions are expressible in terms of t]  alone, and x and t are not involved separately, that the transformation(7.6) and the eqn (7.10) can be used. They cannot be used, for example, when diffusion occurs in a finite sheet of thicknes /, and the boundary conditions are

C = Co, x = 0,

because the second condition becomes

x = /,

(7.19)

(7.20)

which is not expressible in terms of rj  only but involves t explicitly. In general the transformation can be used for diffusion and semi-infinite media when the initial concentrations are uniform and may be zero.

METHODS OF SOLUTION

107

7.2.2. Numerical iterative methods

(i) Crank and Henry (1949a,b) gave a method of solving (7.10) subject to(7.17) and (7.18) based on iterative quadrature. Eqn (7.10) can be written

(7-21)

D dr] drj\ drj

where c = C/Co, a dimensionles concentration, and c = 1 on rj  = 0. We illustrate the method for the case c = 0, Y\ = oo. By integrating (7.21) twice,we obtain

where A is a constant of integration to be chosen such that

= 1 '

( 7-23)

in order that (7.18) shal be satisfied. The condition (7.17) is automatically satisfied by (7.22). The diffusion coefficient D is a known function f(c) of c,e.g. D = exp (kc). If we have a first approximation to the function c(rj) we deduce the function D(rj)  using D = f(c) and carry out the integrations in(7.22) numerically using (7.23) to obtain a second approximation, and so on.

The convergence of this iteration is poor when D varies markedly with c.

Crank and Henry obtained some improvement by rewriting the procedure in terms of the variable s defined by

s= \ Ddc \ Ddct

(7.24)

(ii) Philip (1969a) reviewed his extensive contributions to the theory of infiltration which include one-dimensional diffusion as a special case. One method (Philip 1955) which has better convergence and accuracy than the one just described starts by rewriting (7.10) as

t This transformation seems to have been used first by Kirchhoff(1894) and more recently by Eyres, Hartree, Ingham, Jackson, Sarjant, and Wagstaff (1946). Philip (1973a) has shown that for periodic non-linear diffusion, the time average of s satisfies Laplace's equation and is therefore readily evaluated for appropriate boundary conditions.

108

CONCENTRAT ION-DEPENDEN T D IFFUSION :

which on integration yields

2 I rjdc = -Ddc/drj,

(7.25)

subject to the condition (7.17). The lower limit of the integral is 0 because(7.18) implies dc/dt] -• Oasc -> O.Philip's method uses a finite-difference form of (7.25) in an iterative procedure starting from an estimate of J*  r\ dc. An analytical solution is used in the region of c -» 0. He compares his numerical solutions with the analytical solutions obtained by Neumann's method§ 13.2.4 (p. 296) for two examples in which D is a two-step function of c.

(iii ) Lee (1969) put the problem on a sounder mathematical footing by examining the analytical properties of the initial-value system comprising eqn (7.10) written in terms of the variable s defined in (7.24), i.e.

^ 2

^-

(7.26)

dr\

dr]

subject to the conditions

s = 1, Y\ = 0

(7.27)

and

ds/drj = - g, n = 0,

(7.28)

where F(s) = l/D(s) and the parameter g > 0. He showed that the unique solutions are monotonic decreasing, and either reach s = 0 at a finite value of Y\ or tend asymptotically as r\ -> oo, to s = s ,̂ 1 > s  ̂ > 0. He refers to the former solutions as Class I type and the latter of Class oo. He established that a solution of (7.26) subject to (7.28) and

s = 0, t]  = + oo

(7.29)

exists, which is the solution of the initial-value system with s  ̂ = 0. Subsequently, Lee (1971a, 1972) developed iterative methods for obtaining numerical solutions of the initial-value problem for successive approximations to the parameter g in (7.28) until the solution for which ŝ  = 0 is obtained within prescribed error estimates. The methods can conveniently be programmed for a digital computer and one solution takes only two or three minutes of computer time.

First, Lee considers a solution s = s{rj, g) of the initial-value system. From(7.26) it is evident that for rj  « I, d2s/drj2 « 1. Thus ds/drj changes very slowly for r\ « 1, and its value at a point is very close to the slope of the chord joining that point and the initial point rj  = 0, s = 1.

METHOD S OF SOLUTIO N

109

The term ds/drj in (7.26) may be replaced by (1 —s)/(l —77), and so we approximate to (7.26) for rj  « 1 by

^ = 2(1-s)F(s).

(7.30)

drj2

Lee (1971a) used the solution of (7.30) as a first approximation in his iterative process. The solution is easily obtained and can be of some intrinsic interest as an approximate solution which may be accurate enough for some purposes. The reader is referred to Lee's paper (1971a) for iterations based on the solution of (7.30).

We turn instead to the method described in the later paper (1972) which,by avoiding the use of (7.30), is simpler and requires less computing time.

Lee established some relevant theorems so that we can consider two positive numbers gv and gL

*  and gv = %U/n)*,

(7.31)

where

U = sup F(s)

(7.32)

and

L = inf F(s)

(7.33)

such that

(i) for all g > gv the solutions s(r], g) are of Class I;

(ii) for all g < gL the solutions s(f/, g) are of Class oo with ŝ  > 0.

The gradient G we require to give the solution of (7.26) lies in the range&L < G < 8uWe now take as a first approximation of G an interpolated value gt , where Si =i(gi/ + gL)-

(7-34)

Depending on s(rj, gx) being of Class I or Class oo, the second approximation is obtained by a similar interpolation between the derivative at r\ = 0 of sfo, gi) and that of sfo, gL) or s(rj, gv).

In general, if the last iterative solution is of Class oo with an asymptotic value other than zero, the next approximation is obtained by interpolating between the derivative at rj  = 0 of the last solution and that of the last Class I solution; if, on the other hand, the last iteration is of Class I then the next approximation follows by interpolating between the derivative of the last solution and that of the last Class oo solution. Lee used a fourth-order Runge-Kutta method of numerical integration to obtain the successive approximate solutions.

110

CONCENTRATION-DEPENDEN T DIFFUSION :

Since the derivatives of these solutions are negative and monotonic increasing to zero, an error estimate 0 < ed « 1 can always be prescribed so that the asymptotic value of a solution can be assumed as soon as the absolute value of the derivative becomes less than ed, and hence the solution is asymptotic. Otherwise, the value of the solution reaches zero before the value of its derivative exceeds — ed, and the solution is of Class I.

For a solution of Class oo the asymptotic value assumed above indicates the degree of approximation of the solution to the required one which approaches zero asymptotically. Thus, for a prescribed error estimate 0 < ea « 1, iteration stops as soon as the assumed asymptotic value of the last iterative solution is less than ea. The last solution is taken as the required

solution s(rj, s'o).

Lee (1969) showed that the derivatives are monotonic increasing to zero approximately at an exponential rate exp ( — rj2m), where

m = inf F(s).

0<s< 1

It follows that the increment of the asymptotic value due to ed ^ 0 is always less than

-ed Qxp(-rj2m)dr] = -ed(n/4m)*,

which can be made very much less than ea if we choose ed « m^ea. Thus we can choose consistent error estimates.

Lee (1971a) tabulated results for a practical example relating to the uptake of exces calcium by calcium chloride (Wagner 1968). The diffusion coefficient D takes the form

D = D0/(l+Ac).

The variable s defined by (7.24) becomes

s(c) =

and in the eqn (7.26) we have

F(s) = exp{sln(l

Lee evaluated numerical solutions satisfying (7.27) and (7.29) which are reproduced in Table 7.1 for a wide range of values of A. The prescribed error estimate ea is 001 and ed is 10"4. The table shows the integration step sizes and the number of iterations required. A GE-225 digital computer took two to three minutes from data input to print final results for one solution.

By his second method Lee (1972) tabulated solutions of the equation

d^p_

f

1 }dp

METHOD S OF SOLUTIO N

111

subject to the conditions

p = 1, n = 0; p = 0, rj  = cc,

where >y ^ 0, 1 ^ p ^ 0, a0, b0 are constants.

7.2.3. Two- and three-dimensional series solutions

Philip (1966) developed series solutions for radially symmetrical diffusion in infinite media surrounding cylinders and spheres. The equation is

subject to the conditions

C = Co, p > 1, T = 0,

(7.36)

C = Cl 9 p = 1, T ^ 0 ,

(7.37)

where

p = r/r0, i = r/rg

(7.38)and r = r0 is the surface of the cylindrical (m = 2) or spherical (m = 3) cavity from which diffusant is supplied. We seek solutions of (7.35) of the form

P(C,T) = l + 01T i + 02T + (/>3T* + - '

(7'39)where each </> is a function of C. Philip (1957) gave an a priori  justification of this form of series in a related study of infiltration. By using

(dC/dT)p(dP/dC)r = -(dp/dT)c

(7.40)

we convert (7.35) into

1 d p m d I _ , d

(7.41)

09

and integration with respect to C yields

= D9m~1^.

(7.42)

1 d rc

mdiJc/

We have assumed that limc^Co Dpm -1 dC/d9 = 0, i.e. the flux is zero at infinity for all finite T. By substituting (7.39) in (7.42) and assuming that the expansion on each side is convergent we obtain the following set of relations on equating coefficients:

f </>1dC= -2(D/<t>\\

(7.43)

JC0

f 4>2dC = {D(j>' 2/(ct)\)2}-(m-l) f DdC,

(7.44)

and so on. Here $' signifies differentiation with respect to C, and because of (7.37) we have the conditions

C = C l9

4 >  n = 0, n = 1,2,3,....  (7.46) The first equation (7.43) is clearly of the same form as (7.25). Detailed comparison allowing for the different symbolism shows them to be identical. Thus, the leading term in the series for m-dimensional diffusion is the solution for one-dimensional diffusion. This is to be anticipated as long as the depth of penetration is small compared with r 0 .

Once equation (7.43) has been solved, say by the methods of § 7.2.2 (i), (ii), (p. 107), then (7.44), (7.45) etc. may be solved in turn. They are all linear equations and are amenable to numerical solution. One workable procedure is analogous that that outlined in §7.2.2 (ii) (p. 107). Philip (1969a)  gives a sample set of moisture profiles in soil, computed from the first three terms of the series solutions for the cylindrical and spherical cases.

7.2.4. Some special numerical solutions

7.2.4. Some special numerical solutions

Wagner (1952) for exponential and Stokes (1952) for linear concentration dependent diffusion each transformed eqn (7.10), so that the relationship between D and C is removed from the differential equation and appears instead in one of the boundary conditions. Methods of numerical forward integration are used to build up families of solutions for different exponential and linear relationships.

(i) Exponential diffusion coefficients. Infinite medium. Wagner (1952)  has given the following method of dealing with a diffusion coefficient which varies exponentially with concentration, according to the expression

D = D u exp[P{C-%C x + C 2 )}l (7.47)

where D a is the diffusion coefficient for the average concentration C a = ^C\ + C 2 ), and /? is a constant given by

P = d

References

METHOD S OF SOLUTIO N

113

For purposes of tabulating the final results it is convenient to take new variables

y = $x/(Dot)* 9

(7.52)where Do is the diffusion coefficient for the concentration Co at x = 0 and

so that

C1)^

(7.54)

To compute numerical values of the function i//, we introduce another dimensionles variable

C0)9

(7.55)

whereupon (7.47) becomes

D = Doe\

(7.56)

with Do as diffusion coefficient for C = Co. Substitution of (7.52), (7.55),and (7.56) in (7.49) gives

- = 0.

(7.57)

//

try

Introducing the auxiliary variable

u = ey

(7.58)

into (7.57), we have

Solutions of (7.59) from y = — oo to y = + oo for the initial conditions y = 0, u = 1, y = 0,

(7.60)

were obtained for different values of the parameter g given by g EE (dy/d>Oy = 0 = (Au/Ay)y = 0 = 0-2,04,..., 24.

(7.61)

For each value of g there are two limiting values of y, yl at y = — oo and y2 at y = + oo, with opposite signs. In view of (7.55) these values are related to the initial concentrations C1 and C2 by

y, = / ? « : , - C o ) ,

(7.62)

y2 = /?(C2-C0) .

(7.63)

114

CONCENTRATION-DEPENDEN T DIFFUSION :

On subtracting corresponding sides of (7.62) and (7.63) we have 72-71 =P(C2-CX\

(7.64)

which according to (7.48) is the natural logarithm of the ratio of the diffusion coefficients for the concentrations C2 and Cx. Fig. 7.1 shows the relation between y2 — yl and the parameter g.

2-4

20

1-6

1-2

0-8

0-4

0

i

i

i

|

|

L

0-5 10 1-5 2 0 2-5 3 0 3-5 4 0 4-5 5 0

±(y2—7i) =±p(c2-c{)

FIG . 7.1. Auxiliar y parameter  g as a function of(y2 — yl) = /?(C2 —Ct).

Moreover, it follows from (7.62) and (7.63) that

Co = %C1 + C2)-%

Substitution of (7.65) in (7.47) gives

(7.65)

(7.66)

To facilitate the computation of Do, a graph of ^{yl + y2) as a function of g is shown in Fig. 7.2.

According to (7.55) and (7.53) we obtain the values of \j/ from the relationship

(7.67)

Numerical values of the function \jf(yy g) are compiled in Table 7.2. For negative values of the parameter g the relationship

can be used and the sign of y must be reversed.

(7.68)

METHOD S OF SOLUTIO N

115

- 0 - 4 -

- 0 - 6 -

00

0-4 0-8 1-2 1-6

20

FIG. 7.2. %yl+y2) as a function of g.

2-4

In view of the regularity of the differences between the ij/  values for different g values but equal y values, it is believed that the error in \j/ is in general not greater than one figure in the last decimal place, except for g = —1-6 to g = —24 for which the accuracy is less because of rather sudden changes in the values of the first derivative of ^ as a function of y.

In order to obtain the concentration distribution for a diffusion coefficient with given initial concentrations Cx and C2 and known values of Da and jS,we proceed as follows:

(1) read the value of the auxiliary parameter g for the known value of

(y2-yi) = P(C2-Cl) from Fig. 7.1;

(2) read the value of ^y1 + y2) for the auxiliary parameter g from Fig. 7.2;

(3) calculate the value of Do from (7.66);

(4) plot \\f for the auxiliary parameter g as a function of y with the aid of

Table 7.2.

In view of (7.52) and (7.54) the plot of \\f versus y gives the concentration C at any point x at time t.

Instead of using Figs. 7.1 and 7.2, the values of g and ^yx +y2) may be calculated from the empirical interpolation formulae

5(y2-y1)310-3 + 64(y2-y1)510-5,

(7.69)

= -(M44g2-0-0038g4

(7.70)

Thus far it has been assumed that the diffusion coefficient is an exponential function of the concentration in accordance with (7.47). If this assumption does not hold strictly, we may use the foregoing analysis as an approximation.

Wagner (1952) recommends that the analysis be based on the diffusion

coefficients for the concentrations C_ i = i(C 1 -C 2 )-i(C 2 -C 1 ) and C* = ^C, + C 2 ) + i(C 2 -C 1 ) as the most representative values, corresponding to the average concentration ^{C 1 + C 2 )±25 per cent of the total concentration difference {C 2 -C l ). Thus

References

M E T H O D S OF S O L U T I O N

117

2-4

1-6

0-8

01 0

- 0 -8

- 1 - 6

- 2 - 4

- 3 -5 - 3 - 0 - 2 -5 - 2 - 0 - 1 -5 - 1 0 - 0 -5 0 0-5 10 1-5

r = p(C0-Cs)

FIG . 7.3. Auxiliar y parameter  g as a function of r = P{CO — CS).

In order to obtain the concentration distribution for diffusion from the surface to the interior of a sample (or vice versa) one therefore proceeds as follows:

(1) read the value of the parameter g for the value of r = jS(C0 — Cs) from Fig.

7.3;

(2) Plot c for this value of g as a function of ys using Table 7.3.

The concentration C at any distance x and any time t follows, since from(7.77)

C=CSHCO-Cs)c9

(7.81)

and ys is given by (7.76)

Instead of using Fig. 7.3 one may calculate the values of g with the aid of the empirical interpolation formula

g =

M28r

(7.82)

1—0-177r

Using (7.76) and (7.81), the flux acros the surface x = 0 becomes-Ds(dC/dx)x = 0 = -UDJt)HC0-Cs)(dc/dys)ys

= 0

(7.83)

and from (7.61), (7.80), and (7.82) it follows that dc\ 2 1-128

l-0-177r'

(7.84)

If P is positive (i.e. the diffusion coefficient increases with concentration)and if the substance diffuses from the surface into the interior of a sample with zero initial concentration, i.e. C0 — Cs < 0, the value of g is negative.

118

CONCENTRATION-DEPENDENT DIFFUSION:

(iii ) Linear diffusion coefficients. Using a method similar to Wagner's,R. H. Stokes (1952) obtained solutions for the infinite medium and conditions(7.50), (7.51) for a diffusion coefficient depending linearly on concentration according to the expression

D = D,{\+\a{C l + C2)-aC}.

(7.85)Here Da is the value of D when C = i(C1 + C2), the mean concentration.

By using the substitutions

| i+^-o I

(7'86)

and

the diffusion equation (7.49) reduces to

dw2 v  ̂dw'with the boundary conditions

i > = l ,

w=  +00,

(7.89)

-oo.

(7.90)

For convenience, we denote by b2 the value of v at w = — oo. From (7.85)we see that b is the ratio of the diffusion coefficient at Cx to that at C2.

Stokes obtained numerical solutions of (7.88) by starting at w = 3, v = 1(the value w = 3 is suggested by the known solution for a constant diffusion coefficient) and a chosen small value of dv/dw, say less than 001. The integration proceeds in the direction of decreasing w til l a value of v is reached which is constant to within the accuracy of working. This value of v is b2, and is reached at some negative value of w between — 2 and — 5. Different values of the initial gradient dv/dw lead to different values of b2 which are known only when the solutions are completed. This family of solutions gives, for different bs, values of v and dv/dw at closely spaced intervals in w (the usual interval used by Stokes was 0-1 in w). From these solutions, values of concentration and concentration gradient are readily obtained. They are conveniently expressed in :erms of a new independent variable ya defined by

(7.91)

METHOD S OF SOLUTIO N

119

so that we have

dC = (Q-CJ&l+ft)} *  1 di;

d.ya

2(1-6)

t?±dw'

"

C = C2 + (C1-C2)(l-i;*)/(l-ft) .

(7.93)

Tables 7.4 and 7.5 show -(dC/dya)/(C1-C2) and (C-C2)/(C1-C2) as functions of ya for different values of b. All the solutions shown correspond to b < 1, i.e. to diffusion coefficients which decrease as the concentration increases. The corresponding solutions for b > 1 may be obtained by reversing the sign of ya; thus, for example, the solution for b = 0-1407 becomes the solution for b = 1/0-1407 = 7-106 when the sign of ya is changed. Solutions for intermediate values of b can be obtained by interpolation.

(iv) Diffusion coefficient directly proportional to concentration. The problem treated by Wagner (1950) of a diffusion coefficient given by

D = D0C/C0,

(7.94)has some features of particular interest. Considering first the semi-infinite medium in which

C = Co, x = 0, t > 0,

(7.95)

C = 0, x > 0, t = 0,

(7.96)

and introducing the variables

y = ixADot)* ,

(7-97)

c = C/C0,

(7.98)

the diffusion equation

dt dx

becomes

d2c Idc

4^ = 0.

(7.100)

dy

Further simplification is achieved by substituting v = c2,

(7.101)

when (7.100) becomes

dy2 v2 dy

120

CONCENTRATION-DEPENDENT DIFFUSION:

with boundary conditions

v = 1,

v = 0, y = oo.

(7.103)

(7.104)

Using numerical methods of integration and disregarding temporarily the second condition (7.104), a family of solutions of (7.102) can be obtained for arbitrarily chosen values of (dv/dy)y = 0 = v'o. Clearly if the condition(7.104) at y = oo is to be satisfied, v'o must be negative. Then from (7.102) the second derivative of v with respect to y is positive. If |VQ| « 1, the curve of v against y tends to a constant value at large y as shown in Fig. 7.4, curve A.

FIG. 7.4. Schematic solutions of (7.102).

A solution of this kind does not satisfy (7.104), however. On the other hand,if |v'0| » 1, curves which approach the axis v = 0 with finite slopes as shown schematically by curve B in Fig. 7.6 are obtained. Tentatively we assume that a special value of |v'0| yields a solution for which v vanishes at a certain abscissa y = y0 and satisfies the additional condition

dy

v = 0,

(7.105)

This is the condition that the rate of transport of diffusing substance shal be zero when C = 0, since by eqns (7.97) (7.98), and (7.101) we have for the rate of transport

C dC _ D%C0 dv

° Q & "  4r*  dy'

(7.106)

METHOD S OF SOLUTIO N

121

A function satisfying (7.102), (7.103), and (7.105) can then be combined with the trivial solution v = 0, y ^ y0, so that a solution for the whole range y ^ 0 results.

With the tentative assumption that condition (7.105) is satisfied at a finite value y = y0, the factor y on the right side of (7.102) can be replaced approximately by y0 if v « 1. Thus

dy2

v*  dy

if v « 1, with the boundary conditions

v = 0, y = y 0 ,

(7.108)

dv/dy = 0, y = y0.

(7.109)

Integration yields

v = {2yo(yo-y)}\ v « 1.

(7.110)

Consequently, in the vicinity of y = y0, where v « 1 and hence c « 1 and C « Co, the function v(y) is represented approximately by a parabola and the concentration ratio c = v̂  by a straight line.

To obtain a solution of (7.102) for the whole range 0 < y < y0, numerical integration is required. Since the boundary conditions (7.103) and (7.105)refer to different values of y it is useful to make the substitutions

£ = v/y*9

(7.111)

whereupon eqns (7.102), (7.108), and (7.109) become

0^(1-4'

(7113)

C = 0, £ = 0,

(7.114)

-J = 0, £ = 0.

(7.115)

In order to integrate (7.113) from £ = 0, the second derivative d2C/d£2 at£ = 0 must be known. This cannot be obtained directly from (7.113) because for £ = 0 the right side is indeterminate. By substituting (7.111) and (7.112) in(7.110) and differentiating twice, we obtain

d2C/d22 = 8, £ = 0.

(7.116)On carrying out the numerical integration of (7.113) starting with conditions(7.114), (7.115), (7.116) at I = 0, we obtain C = 2-34 when f = 1, i.e. when

122

CONCENTRATION-DEPENDEN T DIFFUSION :

y = 0. Then it follows from (7.111) and (7.103) that

y = (C*=i)-*  = 0.81.

Transforming (7.112) and substituting (7.117) we have

y = ; M l - « = 0-81(1-£).

Finally it follows from (7.98), (7.101), (7.111), and (7.117) that

(7.117)

(7.118)

(7.119)

A graph of C/Co against \x/(D_ot)*  is shown as curve I in Fig. 7.5.

10

0-8

L \ I

0-6 U 0-4 0-2 0

FIG. 7.5. Concentration distributions.

Curve I, D = D0C/C0; curve II , error function solution (7.120).

0-2 0 -4 0 -6 0 -8 1 0 1-2 1-4 1-6

y=x/(4Dot)*

FIG. 7.6. Concentration distributio n for

D^DiC/C,.

-1-6 -0-8

0

0-8

In Fig. 7.5 curve II shows the corresponding graph for a constant diffusion coefficient, calculated from

C/Co = erfc{ix/(D o0i} -

(7-120)

Curve II approaches the abscissa asymptotically, whereas curve I reaches the abscissa at the finite value y = 0-81 with a finite slope. Thus, in this special case, an advancing velocity of the diffusing component is strictly definable,t and from (7.97) and (7.117) it is given by

(dx/dr)c = 0 = yoD*o/t*  = 2ylD0/x = l-3lD0/x.

(7.121)

tShampine (1973/?) discusses solutions c(rj) = (1-a*/)1^ , 0 ^ Y\ < I/a. c{\]) = 0, >y > I/a,produced by D(c) = (pc(i/2(x2){l — cp/(l +/?)}, where rj  = x/t* and a, p are positive parameters.

METHODS OF SOLUTION

123

Furthermore, (7.113) may be integrated up to ^ = +00, i.e. x = -co,when the solution approaches a limiting value (1, where £i = 6-82. We then have the solution of the problem in an infinite medium for the initial conditions

C = Cl9 x < 0,

x > 0,

(7.122)(7.123)where Ct and C2 are both constant, and the diffusion coefficient D is given by

D = DXCICX,

where Dl is the diffusion coefficient when C = C1. Then from equations(7.98), (7.101), (7.111), and (7.112) we find

C/Cy = (C/Q = oo)1 = (C/Ci)1.

(7.124)This concentration ratio can be related to the non-dimensional variable^x/iDyt)^, which through (7.97) is given by

2{Dxtf= y

= 0-765.V,

(7.125)

where y is calculated from {  using (7.118). A graph of C/Cx as a function of\xl(Dxt)*  is shown in Fig. 7.6. The concentration at x = 0 is 0-59(1̂  instead of 0-50C! which is the value obtained when the diffusion coefficient is constant.

G"

3-5 4-0

FIG. 7.7. Graph of concentration ratio C/Co versus dimensionles variable y = x/(2Dot)*  for desorption problem with diffusion coefficient directly proportional to concentration,D = D0C/C0(e = 00), constant (e = 0), and directly proportional to concentration difference,

D = D0(\-C/C0)(e= -1).

The inset shows on a larger scale the region of intersection of the solutions analysed also by a further power series (see § 9.3.2, p. 176).

Wilkins also calculated the total amount of material that enters the halfspace x  >  0 per unit area up to time t, i.e. M = P Cdx = 2C 0 {Dj) >  P c(y)dy.

Jo Jo

Jo Jo

His expressions for the dimensionless quantity M/C 0 (Dj) 1 are reproduced in Table  7 .6. The conditions for the infinite medium are t = 0, C = C o for x  <  0, C = 0 for x  >  0; for sorption they are C = C o , x = 0, t ^ 0; C = 0, x ^ 0, t = 0 and the usual corresponding conditions hold for desorption. The diffusion coefficient is D = D a (l +%aC 0 -aC) and e = -aC 0 /(\ +\aC 0 ). Pattle (1959)  found a class of exact solutions describing diffusion from a point source when D has the form

References

METHOD S OF SOLUTIO N

125

The equation

dt

ds

has the solution

t \

I S

C = C0~

1-71

t > 0, s2 ^  s 2 ,

C = 0,s2 ^ s2.

(7.127)

These equations represent an expanding diffusion zone with a definite edge, of radius s1 given by

When a quantity Q is liberated at time t = 0 at a point in an infinite line,plane, or volume, the parameters s0, f0 are determined by

(7.128a)

When fc > 1, the concentration gradient at the boundary of the region is infinite; when b = 1, it is finite; and when b < 1, it is zero.

7.2.5. Analytical iterative methods

Kidder (1957) developed a perturbation method for desorption when D(C) = aC with a constant. Successive coefficients in a series solution are the analytical solutions of increasingly complicated ordinary differential equations. The method has been extended by Knight (1973a) to include power-law and exponential relationships between D and C for both sorption and desorption problems.

Parlange (1971a, b) described a method of successive approximations based on an inverted form of the diffusion equation in which the space coordinate x is taken as the dependent variable. This has been improved by Philip (1973b)and Knight and Philip (1973) using a formulation in terms of an integral equation which identifies Parlange's iterative scheme as equivalent to Picard's method of successive approximations (1893).

7.2.6. Exact formal solutions

By exact formal solutions we mean those that can be expressed without approximation in terms of the functions of mathematical analysis. Unfortunately, they are mostly of implicit or parametric form rather than explicit relationships between concentration and the space and time variables.

126

CONCENTRATION-DEPENDEN T D I F F U S I O N :

This means that they do not reveal general features, which is one of the attractions of analytical solutions, nor are they particularly simple to evaluate numerically. The solutions explored by Philip (1960) come nearest to overcoming these disadvantages (§ 7.2.6 (i)).

Fujita (1952, 1954) obtained solutions in parametric form for diffusion into a semi-infinite medium at the surface of which the concentration is held constant. He considered three expressions for D(C) which are (1) D0/(l — XC);

(2) D0/(l -XC)2; (3) D0/(l +2aC + bC2). The last form clearly includes the first two. In all three, Do, X,a,b are constants. Some solutions evaluated by Fujita's methods are presented in Figs. 9.12 and 9.13. Figs. 9.20, 9.21, and

9.22 show an example of the behaviour associated with a diffusion coefficient which passes through a maximum value as C is increased.

Some of Philip's (1968) solutions in connection with swelling soils can be related to Fujita's solutions. Storm (1951) proposed a method which can provide an exact solution for diffusion into a semi-infinite medium, with a specified flux on the surface, when the diffusion coefficient has the same form as that of Fujita's case (2) above. Storm reduced the problem to the solution of a linear equation with linear boundary conditions but again his solution is in parametric form. Knight (1973b) extended Storm's method to more general problems including that of Fujita (1952) and gave explicit exact solutions in some cases including the problems of the instantaneous source and of redistribution in the finite region.

Lee (1971b) considered a time-lag, concentration-dependent diffusion coefficient of the form D0{C(x, t — h)}.

(i) A general class of exact solutions. Philip (1960) showed that there exists an indefinitely large class of functional forms of D(C) for which formal solutions of the diffusion equation may be found analytically. He starts from a postulated solution and derives the D(C) relationship which produces it.

In this section we adopt the nomenclature of Philip's paper (1960) for ease of reference to the functions he develops and tabulates. He is concerned first with the problem

subject to the conditions

0 = 0, x > 0, t = 0,

(7.130)

0 = 1, x = 0, t > 0.

(7.131)

Substitution of the variable

<t>  = x/f±

(7.132)

METHOD S OF SOLUTIO N

127

allows (7.129) to be written as

D=-\te\yd6-

(7133)

It follows that the solution of (7.129) subject to (7.130) and (7.131) exists so long as D(6) is of the form

where F is any single-valued function of 0 in the interval 0 < 0 < 1, which satisfies certain conditions discussed below.

First the function F must satisfy the boundary conditions imposed on </>,and so

F(l) = 0.

(7.135)

Other conditions are imposed by the requirement that D exists. In fact, it is necessary that je0F d6 and dF/d0 exist throughout the range 0 < 0 ^ 1.

We note, however, that sometimes a finite number of discontinuities in D may be allowable or D may be permitted to be infinite at a finite number of points in the range 0 ^ 0 ^ 1, in which cases dF/d0 may either not exist or may be infinite at the appropriate finite number of points in the 0-range.

Furthermore, we do not wish D to become negative. The flux of diffusant in the direction ofx positive is —Dd6/dx =  — f~*Dd0/d</>. For the conditions(7.130) and (7.131) we require D ^ 0 and the flux to be non-negative, i.e.

dO/dcj) ^ 0. This calls for the further condition

dF/d6 ^ 0 , 0 < 0 ^ 1.

(7.136)

Philip (1960) gives a short table of solutions of (7.129), with their associated forms of D, obtained simply by selecting F functions satisfying the above conditions and evaluating (7.134). Unfortunately, all of them have the property that lime_0 D(6) is either zero or infinite. Whilst diffusion coefficients which are zero at zero concentration are sometimes of interest it would seriously limit the importance and generality of Philip's method if all his solutions turned out to have this property. He examines the difficulty in the following way.

The well-known solution (see eqn (2.45) is equivalent in the present nomenclature to the statement that for

F = 2D% inverfc 0, D = Do = constant.

(7.137)Here inverfc denotes the inverse of erfc defined and examined by Philip(1960), who therefore puts

F = 2D% inverfc 0+/(0), Do finite, non-zero

(7.138)

128

CONCENTRAT ION-DEPENDEN T D IFFUSION :

in (7.134) and obtains

where

B(0) = 2n~± exp {  -(inverfc 6)2}.

(7.140)The properties of inverfc 6 and B(6) are treated in detail by Philip (1960),and the functions are tabulated. In obtaining (7.139) we used the relationships

d

1 Cd

—(inverfc 0 )= - - ;

inverfc 6 d9 = \B.

(7.141)

ad

B

Jo

We are concerned with the conditions under which D(0) is finite and non-zero.

A sufficient condition is seen from (7.139) to be that both

lim

0-0

and lim | B-f0 - 0

be finite (including zero). The zero condition ensures that D(0) = Do. If both the above limits are zero it follows that the inverfc term in (7.138)accounts completely for the finite, non-zero value of D(0) in (7.139). It is not difficult to show that the single condition

lim . f = 0

(7.142)

0-0 inverfc u

ensures that both the limits referred to above are zero. By using the relation(Philip 1960)

inverfc 6

n u , .

l i m — — — r = l ,

7.143

0-0 ( — In vy

we find that (7.142) is equivalent to

l im—/— x = 0.

(7.144)

0-0 ( - i n oy

Thus / can become infinite at 6 = 0 but must approach infinity more slowly than ( — In 6)*.

We conclude that there exists a formal solution of (7.129) subject to (7.130)and (7.131) and for which D(0) = Do is finite and non-zero corresponding to every D(6) of the form (7.139) for which 2D% inverfc 04-/ satisfies the appropriate conditions on F discussed above and satisfies (7.142).

METHOD S OF SOLUTIO N

129

A slight extension is that for

F = 2D% inverfc 9±f, (Do finite, non-zero)

but now we require the stronger condition

\df/dO\ ̂  2Dt/B.

We finally note that the condition (7.135) implies

/(I ) = 0.

There is littl e difficulty in generating functions / which satisfy the requirements. Philip (1960) presents a few typical solutions which are reproduced in Table 7.7. He also gives corresponding solutions for the infinite medium.

Unfortunately, it still seems to be true (Philip 1969a) that the functional pairs most readily generated by this promising method are rather complicated in form and are not particularly well adapted to fitting experimental data on

D(8).

7.3. Goodman's integral method

Later in § 13.6.2 (p. 312) we obtain approximate analytical solutions by an'integral method'. Goodman (1964) has applied his method to concentrationdependent and other non-linear systems. The technique is described in detail in § 13.5.2 with reference to problems in which a physically defined boundary surface moves through the medium. The application to concentration-dependent diffusion is so similar that no details are given in this chapter.

It suffices to point out that an artificial boundary at what is called the 'penetration distance' 8(t\ is introduced and thereafter takes the place of the physical boundary of § 13.5.2. Its properties are such that for x > 8(t) the medium is, to the accuracy of working, at its initial concentration. A full account is given by Goodman (1964), who also discusses several ways of improving the accuracy of a solution obtained by the integral method. One of these is the method of moments, which we now describe.

7.4. Methods of moments

If we substitute some approximate solution cn into the one-dimensional diffusion equation we are left with a residual eB, say, such that,

130

CONCENTRATION-DEPENDEN T DIFFUSION :

We seek a solution which makes en smal in some sense. In the version of the method of moments which we shal describe we multiply by a weighting factor Xn and average over the total range in X. On setting this average residual to zero we obtain

ndAT = O, n = 0,1,2,... (7.146)

We choose cn to satisfy the boundary conditions and to contain k unknown parameters. By using k different weighting factors we have enough equations of type (7.146) to determine the k parameters. Clearly, the case n = 0 is identical with the Goodman's integral method. Fujita (1951) inspired by the work of Yamada (1947) applied the method of moments to a sorption problem in a plane sheet of thicknes 2/. His equation is (7.145) with en = 0 and the non-dimensional variables are defined as C/Co = c9x/l = X9Dot/l2 = T,D(C)/D(0) = F(c), where D = Do when C = CO. The problem is specified by the conditions

c = 0, 0 < X < 1, 7 = 0,

(7.147)

c= 1, X = 1, T> 0,

(7.148)

dc/dX = 0, X = 0, T>0.

(7.149)Fujita uses the zero and first moments only and the problem is reduced to that of finding c(X, T) satisfying the two moment equations

and

together with the conditions (7.147) to (7.149). We proceed by considering that in the early stages of diffusion the concentration-distance curve may be represented approximately by a curved portion near the surface of the sheet,followed by a horizontal part coinciding with the x-axis. Strictly, according to the diffusion equation, the concentration becomes finite, though it may be small, everywhere in the sheet at the instant diffusion commences. The region over which the concentration may be assumed zero depends, of course,on the accuracy of working. For a prescribed accuracy, we denote by x0 the point at which the concentration becomes zero and clearly x0 is a function of time. Thus x0 = I when t = 0 and x0 = 0 when t = tl9 say. The time tx is that at which the concentration first becomes finite at the centre of the sheet to the prescribed accuracy of working. Denoting by Xo the value of X

METHOD S OF SOLUTIO N

131

corresponding to x0, i.e. Xo = x0//, we assume that in the region Xo ^ X ̂  1 the concentration is given by a cubic expression of the form

c(X9 T) = B(T){X-X0(T)}2 + E(T){X-X0(T)}\

(7.152)where B(T\ E(T), and X0(T) are functions of T to be determined. We have furthermore

c = 0, 0 ̂  AT ̂  Xo.

(7.153)The condition (7.149) is satisfied by (7.152). Also (7.147) may be written as X0=l 9 T=0.

(7.154)

Introducing (7.148) into (7.152) and putting

B(l-X0)2 = U9 E(l-X0)3 = V,

(7.155)

we obtain the relation between U and V,U+V=l.

(7.156)Inserting (7.152) and (7.153) into (7.150), integrating, and using (7.148) we obtain

which, on eliminating Kby eqn (7.156), becomes

{(lX0)(l+W)}  r^(lit/)F(l) .

(7.158)

Similarly from the first-moment equation (7.151) we find^ { ( 1 - X0)2(l +&)}  = 20G(l),

(7.159)

where

G(c)= f F(c')dc'.

(7.160)

Here F(l) and G(l) denote the values of F and G when c = 1. On integrating,(7.159) becomes

{ 2 = ar,

(7.161)

where

a = 30G(l), £=1-XO9

(7.162)and the integration constant has been determined by (7.154). Inserting

Abstract

7.161) into (7.158) we find d L ocT\ 12/3 OLT

The solution of (7.163) which satisfies the condition f = 0, T = 0, in accordance with (7.162) and (7.154), is  (7.164) where /? is a constant determined from the quadratic equation 24 < xj3 2 F(l) + {a-108F(l)}£ + § = 0.

(7.165)

Clearly for (7.164) to have a physical meaning /? must be positive. The question as to which of the two possible roots of (7.165) should be taken if both are positive is decided in Fujita's treatment by considering the special case of a constant diffusion coefficient. When the solution (7.170) below, derived by the method of moments, is evaluated for a constant diffusion coefficient it is found that better agreement with the formal solution is obtained by taking the larger of the two roots (actually ft = yj) of (7.165).

When the diffusion coefficient is concentration-dependent we take that root of (7.165) which tends to the value -fe as the range in the diffusion coefficient is decreased and we approach a constant coefficient. Denoting by T x the time at which X o = 0, i.e. at time T x the advancing front of the diffusion reaches the centre of the sheet, we have £ = 1, T = T x and hence from (7.164)

P=T X . ( 7

References

METHOD S OF SOLUTIO N

133

distribution when the concentration just ceases to be zero at the centre of

the sheet. It is

c(X, T) = (ap-^X2-(oip-^X\ 0 ̂  X ̂  1. (7.172)

The next step is to derive an approximate solution which holds for later

times when the concentration at the centre of the sheet has become appreciable, according to the accuracy of working. Such a solution must satisfy

(7.149) and (7.148), and must also agree with (7.172) when T = Tx. We therefore assume a cubic equation again of the form

c(X9 T) = Ai(T) + X2Bl{T) + X*El{T\ 0 ̂  X ̂  1, (7.173)

where AX(T\ BX(T\ E^T) are functions of T to be determined. They are of course different from the corresponding functions in (7.152). We see immediately that A^T) in (7.173) is the concentration at the centre of the sheet.

Proceeding as before, by inserting (7.148) in (7.173) we obtain

A1+B1+E1 = 1.

(7.174)

The zero and first-moment equations in this case lead to

^ + ^ + ^ j (2B1 + 3£1)F(1),

(7.175)

^

.

(7.176)

Eliminating Ex by using (7.174) and putting&AJ&T=<t>,

(7.177)

we have

U  ̂ = (3-2^-3^(1),

(7.178)

1

7T

.

(7-179)

d/^

We can eliminate Bl from these two equations, remembering that dG/dA j = F, and obtain

- ^ - = 28F(l) + f FiAJ + ̂ iGiAJ-Giimi).

(7.180)

This can be simplified to the form

% ¥

(7.181)

134

CONCENTRATION-DEPENDEN T DIFFUSION :

by introducing the following variables

f=l-A,

(7.182)

i)j  = 74>/{20F(l)},

(7.183)

1 +

(

«/>-[ F{\)•d/' .

(7.185)

In order that the solution (7.173) should reduce to (7.172) when T = Tl9 over the whole range of X, we must have

A^TJ = 0,

(7.186)

B^T,) = a/J-i

(7.187)

E^T,)  ̂ -otf + f.

(7.188)Eliminating the term (j)dB1/dAl from (7.178) and (7.179) we obtain, in terms of the new variables just introduced,

From (7.182), (7.186), and (7.187) it follows that Bx = <xj?-§ when / = 1,and so from (7.189) we have

Ml) = -&{aj8-f + !<rtl)} .

(7.190)

For any given concentration-dependent diffusion coefficient the quantities r(f) and q(f) can be evaluated from (7.184) and (7.185), the relevant range of/ being 0 ^ / ^ 1 since / = 1 corresponds to T = Tx and / = 0 to T = oo.

Thus (7.190) gives the initial condition to be satisfied by the solution of the differential equation (7.181). In general, numerical integration of (7.181) will be necessary.

When the solution of (7.181) is known, (^(A  ̂ follows from (7.183). Also by integrating (7.177) and using the condition A1 = 0, T = Tx we obtain

A dA't

(

which can be evaluated once 4>(Ax) has been obtained from (7.183). Since from (7.173) Ax represents the concentration at the centre of the sheet, from(7.191) we can calculate how this concentration varies with time. Once the

relationship between Ax and T, and hence between / and T is known, Bl is easily determined as a function of T from (7.189) using (7.183). Finally,

knowing AX{T) and BX{T), E^T) is obtained from (7.174), and hence all functions of Ton the right-hand side of (7.173) are known.

METHODS OF SOLUTION

135

The total amount of diffusing substance Mt taken up by the sheet per unit area at time t is given by

Cl

Mt = 2\ C(x,r)dx,

(7.192)

which in terms of the non-dimensional variables becomes M, = 2/C0 f c(X,T)dX.

(7.193)

Jo

For early times, when the concentration at the centre of the sheet is effectively zero, i.e. T < Tx, c is given by (7.170) and (7.171), and so we have

M '  = 2 / c° ( 8 ^ + i r ) n ° < T < Tl •

(7194)

For later times we find

M t = llCoil-frW-faiT)}.

(7.195)

We note from (7.194) that, in the early stages, Mt is proportional to the square root of time, irrespectively of how the diffusion coefficient depends on concentration. We shal see later, in § 9.4 (p. 179), that this is a characteristic feature of concentration-dependent diffusion.

7.5. Approximation by orthogonal functions

Tsang (1960; 1961) developed a method of obtaining approximate analytic solutions which are simple in form and reasonably accurate for moderately concentration-dependent diffusion coefficients.

He discusses the equation

T f ( r )

(7196)

dt dz\ dzj

subject to the conditions

0 = 1 ,

O ^ Z ^ T C , f = 0

(7.197)

0 = 0, z = 0 and n, t ^ 0.

(7.198)These are conditions for desorption in a sheet of thicknes / expressed in the non-dimensional variables,

z = nx/U 0 = (C-CoViC, - Co), a = D/Do,

where Co is the surface concentration and Cx the initial concentration.

Tsang starts from the expansion

innz.

(7-199)

136

C O N C E N T R A T I O N - D E P E N D E NT D I F F U S I O N:

Substitution in (7.196) followed by the usual procedure for evaluating Fourier coefficients leads to an infinite set of first-order, ordinary differential equations for the functions fn(t), i.e.

dfn(t)dt= £ {oikn(t) + fSkn(t)}fn(t),

(7-200)

n= 1,3,5

where

akn = (-2n2/n) \ a sin kz sin nz dz,

(7.201)

pkn = (2n/n) j (doc/dz) sin kz cos nz dx.

(7.202)

The required initial conditions are

fk(0) = (8/TT/C2)", k = 1, 3, 5,....

(7.203)

Tsang demonstrates that provided a varies slowly with z a reasonable approximation is to neglect all the /„  terms in (7.200) for n > k. He further replaces all/^s for k  ̂ 1 by fk(0) exp ( —/c2f) implying that the harmonics die away rapidly.

As an example, he considers a linear concentration-dependent D for which

a = 1 + /0 = 1 + (2/TT)H/I(0 sin z + ....

(7.204)Using only these two terms for a and the equation for k = 1 in (7.200) Tsang obtains the solution

/64/1

\ n

- sin z,

(7.205)

where (j)0 is the required solution of (7.196) with a = 1, i.e.

</>0(z, t) = £ — e xP ( - n2*) sin nz-

(7.206)

M = 1 , 3 , 5

n7L

For the total amount of penetrant lost M(t) we have Mt = (j) dz = Mo(0~~ —2~~)—2

=r7' (7.207)

where

o A I 4 p ( M 2 r ) .

(7.208)

Values of M(t) calculated from (7.207) for X = 2-5,4-8,10-0 by Tsang agree to within a few per cent with the corresponding solutions shown in Fig. 9.16(p. 180).

8

NUMERICAL METHODS

8.1. Numerical solutions

I N the preceding chapters a large number of mathematical solutions have been presented, most of them in the form of infinite series. Useful though these solutions are their application to practical problems can present difficulties. First, the numerical evaluation of the solutions is usually by no means trivial. Secondly, the analytical methods and solutions are, for the most part, restricted to simple geometries and to constant diffusion properties such as the diffusion coefficient. In other words, they apply strictly only to linear forms of the diffusion equations and the boundary conditions. This can be a severe limitation where the diffusion coefficient in polymer systems, for example, is often markedly concentration dependent.

The solution of mathematical equations which more closely model experimental and practical situations is possible by the methods of numerical analysis. In the days when the calculations had to be performed on a desk calculating machine use of these methods was a formidable task. The advent of the high speed digital computer revolutionized the situation. Recently,considerable developments have taken place in the subject of numerical analysis and in the construction of efficient computer programs to obtain numerical solutions. It is well beyond the scope of this book to attempt even a general introduction to the subject of numerical analysis. Most scientists and engineers, however, at sometime or other feel the need to solve problems for which they cannot find an analytical solution. An experiment is often conducted under conditions dictated by the analytical mathematical solution available even though the experimentalist would prefer an alternative arrangement. Those who have taken courses only in traditional mathematics often find it hard to appreciate that the simpler numerical methods offer,as it were, a new start not necessarily presented as an advanced course or as an extension of analytical methods. It is not necessary to establish a mathematical solution first, into which numbers are then inserted. These remarks have a special relevance to the subject of partial differential equations. This usually comes towards the end of an undergraduate course and is regarded as a branch of higher mathematics.

In order to try to overcome these mental barriers, and to give non-mathematicians an insight into the simpler numerical methods of solving the diffusion equation, we introduce the subject first from a physical point of view. After this, the more mathematical derivation aims to show how real

138

NUMERICA L METHOD S

problems can be tackled and to illustrate some of the pitfalls to be avoided.

The reader should then be able to handle simpler problems himself: in more difficult cases he should at least know how computers obtain numerical solutions and what help the specialists in numerical analysis are able to offer. A few of the many books available for further reading are those by Fox (1962), Mitchell (1969), and Cohen (1973). Smith's (1965) book is a textbook written primarily for students with no previous knowledge of numerical methods whatsoever. The example in § 8.4.1 (p. 143) below is one of many to be found in his book.

8.2. Non-dimensional variables

Inspection of the analytical solutions in the preceding chapters reveals that the group of variables Dt/l2 occurs frequently. The diffusion coefficient D is measured in cm2 s"1, say; it has the dimensions (length)2(time)~ *. Thus if we write the group Dt/l2 = T, we see that T is a dimensionles variable.

There are a number of advantages in using non-dimensional variables in numerical work, though it is not essential to do so. Usually, a good deal of arithmetic is involved in large problems. A whole set of solutions with different physical parameters, e.g. for sheets of different thicknesses, can often be obtained from one basic solution in non-dimensional variables by simple scaling, with considerable economy of computer time. The fundamental parameters are often high-lighted and analogies with physically different systems become clearer, e.g. the distribution of diffusant and electric potential under similar conditions.

For diffusion in a plane sheet of thicknes /, when the diffusion coefficient D is constant, convenient variables are

X = x/l, T = Dt/l2, c = C/Co,

(8.1)where Co is some standard concentration such as the value at the surface of the sheet if it is constant. Then

d C _ d C d X _ < 3 Cl

d2C _ d2C 1

Ix~~Jx~dx~~dX~r ihc^'Jx2!2

and

dC dC dT dC D

~dt ~ ~df~dF ~~dfl2'

Thus, the simple diffusion equation

d-^-Dd2C

(8 2)

dt ~ D ^

(8-2)

NUMERICA L METHOD S

139

becomes

dc d2c

dx2'

(8.3)

where we have substituted C = cC0.

We note that in the non-dimensional variables the thicknes becomes unity,e.g. the sheet lies between X = 0 and X = 1.

8.3. Physical derivation of a numerical solution

Consider a plane sheet in which a concentration gradient of diffusant exists initially. We wish to calculate how the distribution of diffusant changes with time. We divide the sheet into layers each of thicknes h as in Fig. 8.1 and denote by C0,Cl,C2 the concentrations at three neighbouring interfaces.

The dotted lines at R and S denote the mid sections of the two adjacent layers.

X

FIG . 8.1.

We recal Fick's first law of diffusion: rate of transfer of diffusant through unit area is proportional to gradient of concentration and the constant of proportionality is the diffusion coefficient D. Thus in a short time T the amount of diffusant which has entered the shaded layer (Fig. 8.1) through unit area of the surface R is given approximately by qR = — DT(C1 — C0)/h.

140

NUMERICA L METHOD S

In the same time, the amount flowing out through the face at S is approximately qs = —DT(C2 — C1)/h. The net amount of diffusant accumulated in the shaded element in time i is

(

(

(8.4)

If we now take Cx to represent the average concentration in the narrow shaded element, the net gain of diffusant by the element can be written approximately as (C\ — CJ/z, where C\ is the concentration at the end of the interval T. Equating this with (8.4) we have

3<

By choosing Dx/h2 = \ we find

(8.5)

(8.6)

This relationship enables us to calculate by simple arithmetic the concentration at a point at time r + r if we know the concentrations Co, C2 at the two neighbouring points at time t. We can apply (8.6) successively at each point of the sheet and advance the calculation in time steps T.

As an example, suppose the concentration distribution is initially parabolic as in Fig. 8.2, where the values are non-dimensional concentrations c expressed as fractions of the surface concentration at x = 0. The diagram is

FIG . 8.2. Initia l parabolic concentration distribution .

symmetrical about the centre of the sheet and the sheet has been divided into 20 layers each of non-dimensional width h = 0-05. This means that DT/(0-05)2 = \ and hence for the time step we have chosen Dx = 0-00125. The time T itself in seconds can easily be found for a known value of D. This does not enter into our basic calculation, however, for which we need only

NUMERICA L METHOD S

141

(8.6). We first identify CQ,CX, C2 as the initial concentrations (t = 0) at the surface of the sheet and at two layers inside, Co = 1, C1 = 0-81, C2 = 0-64.

Then by (8.6) we have

C\ = ^100 + 064) = 0-82,

for the concentration one layer inside the sheet at t = T. We next apply (8.6)to the points at which the initial concentrations are 0-81, 0-64, and 0-49 respectively and calculate the new concentration at a depth 2h inside the sheet as 0-65. Having calculated a complete line of concentration values at t = T,we repeat the whole proces to obtain a second line of values at t = 2T,and so on. A computer can carry out this repetitive arithmetic easily and quickly.

So far, we have used no calculus nor have we directly referred to the partial differential equation which expresses Fick's second law. Nevertheless, the relation (8.5) is one of the most commonly used formulae in the numerical solution of diffusion or heat-flow equations. But we have made certain approximations, and we have littl e idea of how accurate our solution is.

Other difficulties, too, can arise in using this simple method, and so we now give a more mathematical derivation of (8.5) and of a slightly more complicated alternative.

8.4. Finite-difference solution: explicit method

We return to the non-dimensional equation (8.3) and take the sheet to occupy the space 0 ^ X ^ 1. Let the range in X be divided into equal intervals 5X and the time into intervals ST, so that the X—Tregion is covered by a grid of rectangles, as in Fig. 8.3, of sides dX, ST. Let the coordinates of a representative grid point (X, T) be (iSX, jST\ where i and j are integers. We denote the value of c at the point (iSX, jST) by ctj with corresponding values at neighbouring points labelled as in Fig. 8.3. By using Taylor's series in the T direction but keeping X constant, we can write

from which it follows that

where O(ST) signifies that the leading term to have been neglected is of the order of 8T when we have divided both sides of (8.7) to get (8.8).

142

NUMERICA L METHOD S

•

i-\J

rSTL

FIG . 8.3.

Similarly, by applying Taylor's series in the X direction, keeping T constant, we have

(d2c\

t

dc

8X2 d2c

dxOn adding we find

32c dX<

(SX)2

+ O(8X)2.

(8.9)

(8.10)

(8.11)

By substituting (8.8) and (8.11) in (8.3) and neglecting the error terms we find after slight re-arrangement

(8.12)

where r = ST/(SX)2. If we choose r = \, we regain the equivalent of (8.6).

With reference to Fig. 8.3, we can use (8.12) with a chosen value of r to calculate the values of c at all points along successive time rows of the grid provided we are given some initial starting values at T = 0, and some conditions on each of the boundaries X = 0, X = 1. A formula such as (8.12) which enables one unknown value to be expressed directly in terms of known values is called an 'explicit finite-difference formula'.

Abstract

NUMERICAL METHODS 143 8.4.1. Example Smith (1965) worked out a simple numerical example in which the initial distribution in non-dimensional form consists of two straight lines c = 2X,

c = 2(l-X), i^X^l ,

7=0, (8.13) and the two faces of the sheet are maintained at zero concentration so that c = 0, X = 0 and 1, 7^0.

(8.14)

The initial distribution (8.13) could arise if two separate sheets, each of thickness \, had separately been allowed to reach a steady state with one surface at unit concentration and the other at zero and then they had been placed firmly together. The problem is symmetric about X = \ and so we need the solution only for 0 ^ X ^ \. Take SX = YO

* n= i n 2

In Table  8 .2, the finite-difference solution is compared with values calculated from (8.15) at X = 0-3 and 0-5. The percentage error is the difference of the solutions expressed as a percentage of the analytical solution. The comparisons are seen to be reasonably good on the whole. The largest errors are found at X = 0-5 for small times. This is because of the discontinuity in the initial gradient dc/dX which changes from +2 to -2 at X = 0-5. Table  8 .2 shows, however, that the errors die away as 7 increases. This is the way a discontinuity usually effects the finite-difference solution of a diffusion equation. We shall refer again in §8.10.1 (p. 152) to the special treatment of discontinuities which is needed if we want accurate values of the function near the singularity.

We turn now to a serious limitation on the value of r = ST/(SX) 2 in (8.12). The reader will have no difficulty in repeating the calculations keeping SX = YO but increasing  < 5Tto y^ so tnat r = i-Smith (1965) tabulates the solution and finds the errors to be somewhat larger than for r = JQ but still well within the accuracy of many experimental measurements. However, Figs. 8.4 and 8.5 taken from Smith (1965)  demonstrate that the value of r = \ is critical. In Fig.  8 .4, for r = 0-48, the finite difference solutions agree with the analytical reasonably well, but in Fig.  8 .5 (r = 0-52) oscillations have developed. If a still larger value of r is taken, say r = 1, the finite-difference

References

144

NUMERICAL METHODS

= 0-48

Solution of the differential equation shown by the curves

Solution of the finite-difference

equations shown by the dots

•7=004 8 (/+1 = 10)

T=0-096(/+l=20)

r=0-192(/+l=40)

0 01 0-2 0-3 0-4 0-5 0-6 0-7 0-8 0-9 1-0

X

FIG. 8.4. After Smith 1965.

r = 0-52

r=0-208(/+l=40)

01 0-2 0-3 0-4 0-5 0-6 0-7 0-8 0-9 10

X

FIG. 8.5. After Smith 1965.

solution bears no resemblance to the analytical solution. It has become'unstable' in the sense that the errors increase without limit . We shal discus the subject of instability further in § 8.11 (p. 157). Here we note that a severe limitation is imposed on the value of r, and hence on dT, for a given 5X. We are forced to take a large number of smal time steps when using the simple explicit method. These considerations lead us to search for better formulae.

8.5. Crank-Nicolson implici t method

A method which is widely used was proposed by Crank and Nicolson(1947). They replaced d2c/dX2 by the mean of its finite-difference representations on the jth and (7+ l)th time rows and approximated eqn (8.3) by

ST

(SX)2

{dT)2

(8.16)

NUMERICA L METHOD S

145

where the total error is 0{{5T)2+ {6X)2}. We can write (8.16) in the form

-rcI -_1J + 1+(2 + 2 r )ci J + 1- rc i + 1 J +1 = rcI-_1J + (2-2r)cI .J + rci + lJ (8.17)

where r = ST/(dX)2.

The left side of (8.17) contains three unknowns on the time level 7 + 1, and on the right side the three values of c are known on the jth time level. If there are N internal grid points along each time row, then for j = 0 and i = 1,2,..., N, eqn (8.17) gives N simultaneous equations for N unknown values along the first time row expressed in terms of the known initial values and the boundary values at i = 0 and N + 1. Similarly for 7 = 1, unknown values are expressed along the second time row in terms of those calculated along the first. This type of method, in which the solution of a set of simultaneous equations is called for at each time step, is described as an 'implicit method'.

More work is involved at each time step but the Crank-Nicolson method has the strong advantage of remaining stable for all values of r. We can thus proceed with larger and hence fewer time steps, the limit being set by the accuracy required, having in mind that higher-order terms in the Taylor series have been neglected in deriving (8.17).

8.5.1. Example

Smith (1965) discusses the solution of the problem of § 8.4.1 (p. 143) by the Crank-Nicolson method, taking 5X = YO and ST = J Q̂ SO that r = 1. This is a convenient choice of r for which (8.17) reduces to

j

J+1-ci + 1J+l = ci_1J-\-ci + lJ.

(8.18)Taking j = 0, the values of ci0 (i = 1,2,.. ,9) are given by the first row of Table 8.1. We remember the symmetry of the problem which makes c6 = cA, c7 = c3, etc. Since all the unknowns in the simultaneous equations are on the left side there need be no confusion if we write for any time step cij+l  = ct(i = 1,2,.. ,9).

The set of equations for the first time step is

- 0 + 4 c1 - c2 = 0 + 04

- c 1 + 4 c2 - c 3 = 0-2 + 0-6

- c 2 + 4 c3 - c4 = 0-4 + 0-8

- c 3 + 4 c4 - c 5 = 0-6+1-0

- 2 c4 + 4c5 = 0-8 + 0-8.

(8.19)

These equations are easily solved by a well-known method of elimination.

The first equation is used to eliminate cl from the second equation; the new second equation is used to eliminate c2 from the third equation, and so on.

Finally, the new fourth equation can be used to eliminate c4 from the last

146

NUMERICA L METHOD S

equation, giving one equation with only one unknown c5. The other unknowns c4, c3,c2,cx are then found by back-substitution. The solution is

cx = 0-1989, c2 = 0-3956, c3 = 0-5834,

c4 = 0-7381, c5 = 0-7691.

(8.20)

The simultaneous equations for the values of c along the second time row have left sides identical with those of (8.19) but with values from (8.20)substituted for c,_ ij and ci+1}  on the right sides. Part of this finite-difference solution is given in Table 8.3 and the comparison with the analytical solution at T = 0-1 is good. The implicit method for this example is about as accurate as the explicit method which uses ten times as many time steps for the same total time range. The remarks in § 8.4.1 (p. 143) about the discontinuity in the initial gradient at X = 0-5 apply also to the results of the implicit method.

More details of the elimination method of solving the equations and of alternative iterative methods are to be found in Smith (1965) and in standard works on numerical analysis.

8.6. Other  boundary conditions

8.6.1. Surface concentration a given function of time

The way in which the concentration at the surface of the sheet varies with time may be given in the form of an algebraic formula, a graph or a set of tabulated values. The data can be substituted directly at each time step into(8.12) or (8.17) and the methods proceed as described.

8.6.2. Derivative condition

We have seen that boundary conditions involving the gradient of concentration occur frequently. As an example, we consider the evaporation condition of § 3.3.1 (p. 35), which we write as

dc/dX = a(cs-ce), X = 0,

(8.21)

where cs is the surface concentration at time T and ce is the equilibrium surface concentration corresponding to the vapour pressure in the atmosphere remote from the surface. The algebraic signs need careful attention(§ 1.4.2 (iii ) (d), p. 9). The left side of (8.21) is the rate of transfer away from the surface i.e. in the direction of negative X, and for a condition of loss by evaporation this is a positive quantity. Also for evaporation cs > ce and so the right side of (8.21) is also positive. Fig. 8.6 depicts the relevant grid points at X = 0 and X = 1 if a similar condition were to hold on both surfaces.

NUMERICA L METHOD S

147

- 1

0 1

N-\

X

FIG . 8.6. After  Smith 1965.

N N+]

hi j

The simplest way to represent the condition (8.21) at X = 0 in finite differences is

= a(c0 J-ce) ,

(8.22)

This gives one extra equation for c0J at any time step, to be used in the explicit or implicit schemes instead of a given value of c0J.

A more accurate replacement of (8.21) is possible by introducing a 'fictitious'concentration c_l} at the external grid point (-8XJ8T) (Fig. 8.6). We imagine the sheet extended one layer. The condition (8.21) becomes

(cltj-c-ltj)/(2dX) = a(c0J-ce).

(8.23)The value of c_ t d is unknown, but it can be eliminated by using the replacement of the partial differential equation. For the surface point this is

•

I

(8.24)

dT

(6X)2

Elimination of c_ t j from (8.23) and (8.24) gives

dT S

The explicit form of (8.25) is

( 8 2 5 )

and the Crank-Nicolson formula is

(8.27)

which can easily be rearranged to become the first equation of the set (8.17).

The special case of an impermeable surface corresponds to a = 0 in the above equations.

148

NUMERICA L METHOD S

8.6.3. A restricted amount of diffusant

In §4.3.5 (p. 56) we considered problems in which the condition (4.36)expresses the fact that the rate at which solute leaves a well-stirred solution is equal to that at which it enters a sheet immersed in the solution. Using the non-dimensional variables (8.1) and considering the sheet to be of thicknes/ and the surface X = 0 to be in contact with a stirred solution of extent a,we can write the boundary conditions as

a dc0J8T = I dcOJ/dX9 X = 0, T > 0.

(8.28)In this problem, Co in (8.1) is conveniently taken to be the initial uniform concentration in the solution. The simplest finite-difference replacement of(8.28) is

a  ̂ = -J-(ClJ-c0J).

(8.29)Alternatively, by introducing a fictitious concentration, as in (8.23), we find S^M l+—\ = —^-(c, —cn .)•

(8.30)

01

I OX j \OA)

The explicit and implicit forms of (8.29) and (8.30) follow at once by approximate replacement of dcOJ/dT.

8.7. Finite-difference formulae for  the cylinder  and sphere

In terms of the variables

R = r/a9 T=Dt/a2,

(8.31)

the equation for radial diffusion in a cylinder of radius a becomes

dc 1 dR8C\RdR ] =

The finite-difference approximations corresponding to (8.11), omitting the error term, are

- l j c , - ! , } , i * 0 , (8.33)

ci.j-coj, i = 0.

(8.34)

The nomenclature is as for the plane sheet, namely that ctj is the concentration at the point (idR, jdT), the range 0 ^ R ^ 1 having been divided into equal intervals <5JR. Explicit and implicit formulae follow by combining (8.33)and (8.34) with appropriate replacements for dc/dT.

NUMERICA L METHOD S

149

An alternative method of dealing with a hollow cylinder of internal radius b, suggested by Eyres et al. (1946), is to use

Xx = In (R/b)

(8.35)

as independent variable. Then (8.32) becomes

dc exp(-2X1) d2c dT

b2 dX2>

(8.36)

and we have diffusion in a plane sheet with a variable diffusion coefficient.

The non-dimensional equation for radial diffusion in a sphere of radius a is

8c _ 1 Si 8c\ ^ c 2 3c

df~R~2dR\R d

+

and the finite-difference approximations are 1 8

i # 0 , (8.38)

6 (cu-c0J), i = 0.

(8.39)

The treatment of the various boundary conditions for the cylinder and sphere is precisely analogous to that of § 8.6 (p. 146).

8.8. Composite media

Conditions at the interface between two different media can be dealt with by a slight extension of the methods of § 8.6.2 (p. 146). Considering the plane case first, let x = xs be the interface and let the suffices a, b refer to the left side(x < xs) and right side (x > xs) of the interface respectively. The space intervals (5xa and Sxb may be different if desired. Let F(cs, t) denote the flux acros the interface. The conditions to be satisfied are

Da dcjdx = Db dcjdx = F(cs, t), x = xs,

(8.40)which expresses the fact that diffusant enters one medium at the same rate as it leaves the other, together with some relation between the concentrations on the two sides of the interface. We shal consider the simplest case of

c\ = ch = cs

(8.41)and the modification made necessary by a more general relationship such as

c* = Q

wil l be obvious.

150

NUMERICA L METHOD S

As in § 8.6.2 (p. 146) the simplest procedure is to replace (8.40) by

which relates cs to the concentrations at the two neighbouring points on any time row.

As in § 8.6.2 (p. 146) a more accurate replacement is possible by imagining the medium to the left of the boundary to be extended one step 3xa to the right of xs and eliminating the fictitious concentration there by using (8.40).

We obtain

8t - -

-

- -

( 8 4 3)

Similarly, by extending the medium to the right of the interface one step dxh to the left, we find

(8.44)

By eliminating F from (8.43) and (8.44) we obtain

^ = *^(cs + 1J-csJ)-^-(cSJ-cs_u).

(8.45)

This equation can be written in non-dimensional variables, and explicit or implicit finite difference formula derived by appropriate substitution for dcjdt. Corresponding formulae for composite cylinders and spheres are derived in the same way.

8.9. Two- and three-dimensional diffusion

There is no difficulty in principle in extending the methods described in§§8.4 and 8.5 (pp. 141 and 144) to two and three dimensions. In practice,however, the considerable increase in computational labour called for has stimulated attempts to find more efficient methods. These are still the subject of active research and we can only indicate briefly their general nature.

A typical, simple problem is to obtain solutions of

dc

ld2c d2c\cT \cx cyI over the rectangular region O^x^a,

O^y^b,

subject to the conditions that c is known over the whole region at t = 0 and is prescribed on the boundary for t ^ 0. We cover the region with a rectangular space grid at

NUMERICA L METHOD S

151

each time step and denote coordinates by

x = idx, y = jdy, t = nSt,

(8.47)where i, j , n are positive integers. The values of c at the grid points are denoted by

c(idxjdy9 nSt) = ciJtn.

(8.48)

The explicit finite-difference scheme of § 8.4 (p. 141) becomes

D ,

iJ,n _

(<5*r

D

• ̂ u-u.-  ̂

+ c^J-

(8-49)

This is computationally straightforward but the stability restriction is DIT^I+T^I}***'

(8-5°)which is more severe than r ^ \ as in § 8.4. In three dimensions the restriction is even more severe. Extremely smal steps 6t must be used.

The Crank-Nicolson method becomes

i-cU,»

i J \ d c , d

St

32,, 32,

2c

(8.51)

and requires the solution of (M— 1)(N— 1) simultaneous algebraic equations for each time step St, where NSx = a, Mdy = b. Because five unknown values of c in general appear in each equation they are less amenable to solution by direct elimination methods and are usually solved iteratively.

One of the earliest and still probably the most widely-used method which offers considerably improved efficiency is that of Peaceman and Rachford(1955). The essential feature of Peaceman and Rachford's method and of several later variants is to replace only one second-order derivative, say d2c/dx2, by an implicit difference approximation, leaving the other derivative d2c/dy2 to be treated explicitly. By applying the resulting difference equation to each of the (N — 1) points along a grid line parallel to the x-direction we obtain (N— 1) simultaneous equations, each one containing only three unknown values of c, e.g. for the point (ij,n\ cI-Jtll + 1, Ci_1JilI + 1, ci + lf</> + 1 are unknowns but cftJ-+ltn + 1,cl-t>/-_1>n + 1 do not appear. We have a set of(N—l) equations to solve (M— 1) times for each of the (M — 1) grid lines parallel to the x-direction. This is much easier than the solution of the(N— 1)(M— 1) simultaneous equations needed in an implicit method. The solution is advanced from the (n+ l)th to the (tt + 2)th step by interchanging the treatment of the second-order derivatives, i.e. d2c/dx2 is treated explicitly

152

NUMERICA L METHOD S

and d2c/dy2 implicitly. This and similar methods are generally referred to as alternating direction implicit methods (ADI methods) and are usually stable for all ratios dt/(Sx)2 and St/(3y)2. Mitchell (1969) discusses several methods including three dimensional variants and gives guidance on which to choose for different types of problem. Even greater efficiency of calculation is promised by using the 'hopscotch methods' developed by Gourlay (1970,1971). For other geometries and curved boundaries special finite-difference formulae are needed. (Smith 1965, Mitchell 1969, Fox 1962).

8.10. Singularities: local solutions

8.10.1. One dimension: discontinuity at origin

It is possible to start a finite-difference solution directly from the prescribed initial conditions which give a row of values of c at T = 0. In some cases, e.g.

when the surface concentration is a continuously varying function of time which is known, starting this way will probably be quite satisfactory. In other cases the conditions are such that a singularity exists at T = 0. For example,if the conditions are

c = 0, 0 < X < 1, T = 0,

(8.52)

c = l , X = 0, 7 ^ 0,

(8.53)the limiting value of c is unity as T tends to zero for X = 0, whereas c tends to zero as X approaches zero for T = 0. In other words, the concentration is discontinuous at (0,0). As we neglected higher terms in the Taylor series when deriving the finite-difference replacements for derivatives, the difference solution is likely to be a poor one near a discontinuity where some derivatives will be infinitely large. Although this is confirmed in practice, it is a fortunate property of the diffusion equation that a difference solution quickly approaches the analytical solution and its accuracy is probably acceptable after a few time steps.

We can secure accuracy in the neighbourhood of the singularity either by developing an analytical or a series solution applicable for smal times, or by transforming the variables so that the singularity is removed.

It is often not difficult to find a suitable small-time solution because a medium of any shape behaves as if it were semi-infinite in the early stages of diffusion when the measurable penetration of diffusant is small. Thus the solutions of Chapters 3 or 7 can be used.

For the conditions (8.52) and (8.53) the singularity at (0,0) can be removed by using the variables

£ = X/T\

T = T*.

(8.54)The effect is to expand the origin X = 0, T = 0 into the positive half of the

NUMERICA L METHOD S

153

£ axis and to remove the whole of the positive half of the X-axis to £ = oo.

The discontinuity in c at X = 0, T = 0 is transformed into a smooth change along the positive £-axis. Finite-difference solutions can proceed in terms of the variables £, T, without difficulty, though the diffusion equation is slightly more complicated after the transformation. Thus, the simple diffusion equation (8.3) becomes

2T£ = £-&

(8-55)

and (8.52) and (8.53) are now

c = 0, i c= 1,

; = oo,

£ = 0,

T

T

= 0,

(8.56)

(8.57)

The numerical proces starts with the solution of the ordinary differential equation for c(£) obtained by putting x = 0 in (8.55). In this example, an analytic solution exists: in other cases, e.g. for a variable diffusion coefficient,the methods of Chapter 7 can be used. There will come a time x when the boundary condition on X = 1 will need to be taken into account. We can continue in the transformed plane or return to the original variables (X, T)according to which is more convenient.

Discontinuities in derivatives rather than in the function c itself may also need special treatment, though usually the trouble is less marked. Discontinuities may occur also in the initial condition but not on the boundary as in the example of § 8.4.1 (p. 143).

We have said that the accuracy of finite-difference solutions improves as T increases and usually they have been found to approach the corresponding analytical solutions where these are known. For certain initial and derivative boundary conditions, however, it can happen that a smal difference persists for all time T between the numerical and analytical solutions. This rather specialist topic is discussed by Mitchell (1969).

8.10.2. Two dimensions: boundary discontinuities

Difficulties can arise at a corner on the boundary of the region within which diffusion is taking place. Re-entrant corners, where, the boundary changes direction through an angle exceeding n as at P in Fig. 8.7 are particularly troublesome. Some or all of the derivatives of the concentration may become infinitely large at the corner.

(i) Series solutions. Motz (1946) described how an analytical solution which incorporates the singularity can be welded onto the usual finite-difference solutions of steady-state problems away from the corner. Fox and Sankar

(1969) generalized this method to include other boundary conditions. Bell

154

NUMERICA L METHOD S

r>

r

FIG . 8.7. Re-entrant corner.

and Crank (1973) combined the same idea to solve transient diffusion problems in two-dimensions. They expres the diffusion equation (8.46) in polar coordinates r, 0 centred at P (Fig. 8.8) in the form

n

+

(8.58)

As an example the boundary conditions in the neighbourhood of P are taken to be

= 0 on 0 = O,0o-

(8-59)

Consider a separation of variables solution

C = exp(-0L2Dt)R(r)\l/(6)+W(r, 0),

where W(r, 0) is a solution of Laplace's equation representing the steadystate form of the singularity. We obtain for R and \ji

if,"  = - 0 , 2^

(8.60)

1

/ o)2\

R' + -R+R a2 ^ = 0.

(8.61)

Eqn (8.60) has a solution

\j/ = a cos a>6 + b sin a>6

FIG. 8.8. Corner  in polar  form.

NUMERICA L METHOD S

155

and (8.61) is Bessel's equation for which

R = pjjoir),

CD  ̂ 0,

which is finite at P.

Thus a solution of (8.58) is

C{r, 0, t) = exp ( - 0L2Dt)JJ^r) {A cos coQ + B sin toO) + W(r, 0), (8.62)in which the boundary conditions (8.59) require

B = 0, co = kn/90, k = 0,1,2,...,

and following Motz (1946)

W(r, 0) = f <Vk>l cos kW

with A = n/80.

As an illustration we consider the re-entrant corner at P in Fig. 8.7 for

which 0O = 37i/2, i.e. X = 2/3 and the normal derivatives of C are zero on PPi and PP2- The general solution obtained by summing solutions of type(8.62) for this case is

00 °°

2k8

C(r,0,r)= I I AkJap(-tfDt)J2kl3(af)cos —j=0

fc=0

3

+ £ ckr2k/3 cos = 1 .

(8.63)

We note that although C itself is finite at P, all derivatives with respect to r contain singular terms at P. Hence the need to avoid using finite-differences near P. Instead we use an approximation for smal r based on (8.63) which we can expres as a single power series in r by expanding the Bessel functions and collecting like terms in r. Thus

«

J2k/3\Z) — Z

m =

and (8.63) can be written

C = ao(t) + a j(r) cos |0

+ r2{a2(t) cos 20 - bo(t)} + 0{r$).

(8.64)

The as are functions oft and represent the coefficients of the leading term in each Bessel function expansion together with the corresponding coefficient of the steady-state solution.

The series (8.64) is used, at time t, to obtain function values C at points near the corner in terms of those further away. The two sets of points are referred to as 'near' and 'far' points. One far point is needed to determine each

156

NUMERICA L METHOD S

unknown coefficient in the series. In the simple case of a three-term approximating series, for example, we see that three far points are needed. We can select three near points, both sets being displayed in Fig. 8.9. Eqn (8.64)becomes

20

C = a0 + ax cos —

40

cos

(8.65)

In principle, we use values of C and of r, 0 at Fx, F2, F3 in Fig. 8.9 to determine 0o» fli > a2 fr°m (8.65). We then evaluate C at N1, N2,N3 using appropriate values of r, 0 and those of a0, ax, a2 just determined. These values of C are substituted in the explicit finite-difference formula when required. Elsewhere,the simple difference scheme is used. Practical details of the method and some refinements together with an assessment of accuracy are given by Bell and Crank (1973).

FIG . 8.9. Near  and far  points.

(ii) Heat-balance equation. A simpler treatment of a corner uses the method of § 8.3 (p. 139) and the two-dimensional equivalent of Fig. 8.1. The domain is divided into elementary areas, which are mainly rectangular except where they are made to fit  the shape of the boundary. Bell (1973) has treated heat flow in a chamfered billet by considering elements as shown in Fig. 8.10.

In diffusion terms, the corner concentration CP at P is assumed to be the mean concentration for the corner element, for which a mass-balance equation is used. The rate at which diffusant enters the corner element is approximated by —D(C1 — CP)Ay/Ax over the face RS and by-\D(C2-CP)Ax/Ay over QR. The flux over PQ and PS is specified by the

NUMERICA L METHOD S

157

Corner element

Typical body element

Typical surface

element

• Denotes mesh points

FIG . 8.10. Chamfered corner.

boundary conditions. The net flux into the element through all faces is equated to Vc dCP/dt, where Vc is the volume of the corner element. The resulting equation is used in conjunction with the corresponding ones for all other elements and which are identical with the usual finite-difference equations. This method seems to have been mentioned for the first time by Eyres,Hartree, Ingham, Jackson, Sarjant, and Wagstaff (1946).

8.11. Compatibility , convergence, stability

We have assumed that finite-difference methods provide reasonable approximations to the true solution of the partial differential equation. The investigation of this assumption is an important part of the work of professional numerical analysts. We shal outline the nature of the problems in a general way, leaving the reader to consult standard references for the details.

It is broadly true that the investigation of linear systems is reasonably satisfactory but that relatively littl e progres has been made with general treatments of non-linear systems. In these cases, for the most part, the analysis is based on the assumption of localized linearity.

We are concerned with three related properties:

(a) Compatibility. In deriving the finite-difference equation we neglected higher-order terms in the Taylor series. These constitute a truncation error.

We require that the truncation error should tend to zero as SX and 5T, for example, approach zero. If this is not so, the difference scheme is said to be incompatible or inconsistent with the partial differential equation. In this case, the difference solution is not likely to approach the solution sought.

It is not usually difficult to establish the conditions necessary for the compatibility of a difference scheme.

158

N U M E R I C A L METHOD S

(b) Convergence. Assuming compatability is ensured there next arises the question of whether the solution of the difference equations converges to the solution of the partial differential equation as the grid size approaches zero.

Let U represent the exact solution of a partial differential equation, with x and t independent variables, and u the exact solution of the approximating difference equations. The finite-difference solution is said to be convergent when u tends to U as Sx and dt both tend to zero. Convergence is usually more difficult to investigate than compatability. Once established, however,it should be possible to decrease the difference U — M, usually called the discretization error, and hence improve the difference solution by decreasing dx or dt or both, perhaps subject to some relationship between them. When two solutions obtained with different grid sizes agree to within the desired accuracy it is usually assumed that the proces of solution is complete. Fox and Mayers (1968) have drawn attention to pathological cases in which the assumption may be dangerous.

(c) Stability. If it were possible to carry out calculations to an infinite number of decimal places and if the initial and boundary data were specified exactly, the numerical calculations would produce the exact solution u of the difference equations. In practice, of course, each calculation is carried out to a finite number of figures and 'round off errors are introduced. The solution actually computed is not u but N, say, which we can cal  the 'numerical solution'. The subject of stability is concerned with the possible build up of errors in the calculation which would cause N to be significantly different from u.

A set of finite-difference equations is said to be stable when the cumulative effect of all rounding errors is negligible. If the magnitudes of the errors introduced at the various grid points are each less than <5, then the finitedifference equations are usually considered stable if the maximum value of u — N tends to zero as 5 tends to zero, and does not increase exponentially with the number of time rows in the computation.

Usually it is not possible to determine the magnitude of u — U at a given mesh point for an arbitrary distribution of errors. Standard methods of investigating stability mainly study the growth of an isolated error or a single row of errors. On the whole stability estimates tend to be conservative and numerical solutions are usually more accurate than estimated.

More extensive treatments of these matters are given, e.g. by Smith(1965), Fox (1962), and Mitchell (1969).

8.12. Steady-state problems

Steady-state solutions have been obtained in earlier chapters for onedimensional diffusion in a plane sheet, cylinder, or sphere. In two and three dimensions for these shapes, and particularly for a constant diffusion

NUMERICA L METHOD S

159

coefficient, analytical solutions can sometimes be obtained as in § 2.5 (p. 24).

Even these are usually cumbersome for computation and are not available at all for more complicated shapes or non-linear problems. The numerical methods, which have been used extensively, are mostly referred to as finitedifference methods or finite-element methods.

8.12.1. Finite-difference methods

We are here referring to problems for which dC/dt = 0 everywhere. The finite-difference methods use the same replacements for the space derivatives in the diffusion equation and for the boundary conditions as in § 8.9 (p. 150).

Large sets of simultaneous algebraic equations are solved by direct or iterative methods including the ADI methods. The practical details and discussions of accuracy and convergence are discussed e.g. by Smith (1965), Fox(1962), and Mitchell (1969). Singularities may occur both on the boundary or within it and these need special consideration. We have referred in § 8.10.2(p. 153) to the Motz method (1946). This and other methods are discussed by Woods (1953), Fox and Sankar (1969), Whiteman (1970), Whiteman and Papamichael (1972), and Symm (1966).

8.12.2. Finite-element methods

These methods have been widely used for several years by engineers interested in stres problems and in steady-state heat flow. More recently,mathematicians have attempted to put the methods on a rigorous mathematical basis. The finite-element methods can be described as adaptations of the calculus of variations suited to numerical evaluation by a computer. So far, they have been applied to transient diffusion problems only in a few isolated instances (see e.g. Bruck and Zyvoloski (1973)). None of the results presented in this book have been obtained by using finite elements. The subject is in a very active state of development, however, and may well make a major contribution to the mathematics of diffusion in the next few years.

Meanwhile, the interested reader will find available simple introductions to both finite-difference and finite-element methods in the book by Myers(1971), a more general account by Zienkiewicz (1967, 1971), and the proceedings of a conference on the mathematics of finite elements and applications edited by Whiteman (1973).

SOME CALCULATED RESULTS FOR VARIABL E DIFFUSION COEFFICIENTS

9.1. Steady state

I N the steady state the concentration distribution through a plane sheet,in which diffusion is assumed to be one-dimensional, is given by the solution of the equation

— D—J =0,

(9.1)

where D is the diffusion coefficient, not necessarily constant. The corresponding equations for the hollow cylinder and sphere are obvious.

9.1.1. D a function of concentration

If D is a given function of concentration, i.e.

D = D0{l+f(C)},

the general solution of (9.1) can be written as

Doj{l+f(C)}dC = Ax + B9

(9.2)

where A and B are constants to be determined by the boundary conditions.

The corresponding solution for the hollow cylindrical tube is

Do J {1 +/(Q}  dC = A In r + B,

(9.3)

and for the hollow spherical shell,

D0J{ l+/(C)}dC = ~ + B.

(9.4)

When the boundary conditions for the plane sheet are C=CX, x = 0,

(9.5)

C = C2, x = /,

(9.6)

eqn (9.2) becomes, using Barrer's (1946) nomenclature,

cl^F(c1)-c2-F(c2)= ~r

(9J)

VARIABL E DIFFUSION COEFFICIENT S

161

where

F(Q= f /(C')dC' .

Jo

(9.8)

Similarly, for the cylindrical tube or spherical shel with boundary conditions

C = C X , r = r l 9

(9.9)

r = r2,

we find for the cylinder

In r1 — In r

and for the sphere

Cl+F(C1)-C2-F(C2)

C1-^F(C1)-C2-F(C2)

(9.10)

(9.11)

(9.12)For any given relationship between D and C, the integrals F(C) are readily evaluated either analytically, graphically, or numerically, and the concentration distribution follows immediately from the above equations. Some typical examples calculated by Barrer (1946) are reproduced in Figs. 9.1

0-4 -

0-2 -

00

0-2

0-4

0-6

x/l

0-8

10

FIG . 9.1. Typical steady-state concentration distribution s across a membrane when D = DO{1+/(C)}.C1 = l ,C 2 = 0.

Curve 1: /(C) = aC\a = 100.

Curve 4: /(C) = 0 (simple Fick law obeyed).

Curve 2: /(C) = aC; a = 10.

Curve 5: f(C) = -aC;a = 0-5.

Curve3:/(C) = aC;a = 2.

Curve6:/(C) = ~aC\a = 10.

162

SOME CALCULATE D RESULTS FOR

0-4 „ 0-6

FIG . 9.2. Typical steady-state concentration distribution s across a membrane when

D = D0{\+f(C)}.  Cx = 1, C2 = 0.

Curve 1: /(C) = a ebC; a = 1, 6 = 3.

Curve 5: /(C) = 0 (simple Fick law obeyed).

Curve 2: f(C) =1 + 6C Curve3: / (C)= -

\ a = 100, 6 = 1.

Curve 6: f(C) =1 4- oC; a = 1,6 = 2. Curve7: / (C)= -

\ a = 0-9, 6 = 1.

Curve4:/(C) =aC\+bC\a= 1,6 = 1.

Curve8:/(C) =

= 1.

and 9.2. They illustrate the general conclusion that when D increases as C increases the concentration-distance curves in the steady state are convex away from the distance axis; but when D decreases as C increases the curves are convex towards that axis. If D first increases and then decreases or vice versa, with increasing C, a point of inflexion appears in the concentrationdistance curves.

9.1.2. D a function of distance

If we have

= DO{1+/(*)} ,

or

(9.13)

(9.14)for the sheet or cylinder and sphere, the general solutions (9.2), (9.3), and

VARIABL E DIFFUSION COEFFICIENT S

163

(9.4) are to be replaced by

d X ~

(9.15)

^

-

(9.16)

or

respectively. Denoting by / the integral on the right-hand side of each of these equations, taking x = 0 or r = 0 as the lower limit and /x , I2 the values of / at the two boundary surfaces, we find

C - C W

, 9 1 8)

c c 1T'

Concentration distributions follow immediately for given /(x) or f(r).

Barrer (1946) shows typical curves for f(x) = ax and /(x) = bx + ax2. They are reproduced in Fig. 9.3. When D is an increasing function of x the curves are convex towards the axis of x and when D is a decreasing function of x they are convex away from that axis.

9.1.3. Rate of flow

We saw in § 4.2.2 (p. 46) that the rate of flow F through unit area of a plane membrane of thicknes /, when the concentrations at the two faces are C1,C2 is given by

(9.19)c2

where D is a function of concentration C. The corresponding argument for a cylindrical shel of inner radius rl and outer radius r2 is as follows. Let F denote the rate of flow per unit-length of cylinder. Then

F = -inrDdC/dr,

(9.20)

which on integration becomes

f2 F

fCl

-—dr = DdC.

(9.21)

Jri 2nr Jc2

But in the steady state F is independent of r and hence we find D dC.

(9.22)

2* r

In (r 2/r 1)JC2

164

SOME CALCULATE D RESULTS FOR

FIG. 9.3. Typical steady-state concentration distribution s when D = Do{\ +/(*)} . Cx = 1,C2 = 0.

Curve 1: f(x) = -ax, a = 0-99.

C u r v e 6: f(x) = bx + ax2;a = l,b = 2.

Curve 2: f(x) = -ax;a = 0-90.

Curve 7: f(x) = bx + ax2;a = 2-25, fc = 3.

Curve 3: f(x) = 0 (simple Fick law obeyed). Curve 8: f(x) = ax; a = 9.

C u r v e 4 : f(x) = ax;a= 1 0.

Curve 9: f(x) = ax, a = 99.

Curve 5:/(* ) = ax;a = 20.

The corresponding result for a spherical shel is F = 47C7~Z7J DdC'

(9-23)where F now refers to the total flow through the shell. When D is a function of x or r given by (9.13) or (9.14) it is easy to see from (9.18) that

F = -D— = -Do—

-, for the plane sheet,

(9.24)

and

C —C F = -2nD0-±—-^,

for the cylindrical tube,

(9.25)

F = -AnD0CTl f2, for the spherical shell.

(9.26)

VARIABL E DIFFUSION COEFFICIENT S

165

9.1.4. Asymmetrical diffusion through membranes

Hartley [1948] has indicated that in any membrane for which the diffusion coefficient depends both on concentration and on distance through the membrane, different rates of penetration in the forward and backward direction are to be expected in general. Writing D = /(x, C) we have for the rate of flow

F = -/(x,C)dC/dx.

(9.27)If the function /(x, C) is expressible as the product of two separate functions/ t(x) and /2(C), (9.27) becomes

Jo/iW Jc2/2(QdC,

(9.28)

c2

where the boundaries of the sheet are at x = 0, x = /. In this case, since

(9' 29)

the permeability of the membrane will be symmetrical. The function /(x, C)will not usually be separable in this way, however, except in the simple cases in which fx(x) or /2(C) is constant, and so it is unlikely that the membrane will be symmetrical unless D is constant or a function of either x or C alone.

Sternberg and Rogers (1968) set up a mathematical model of a membrane with a solubility coefficient which varied asymmetrically with position. The model gives a quantitative description of the directional transport process.

Peterlin and Williams (1971) discus four different theoretical models. The subject of selective permeation through asymmetric membranes is reviewed and discussed by Rogers and Sternberg (1971).

9.1.5. Diffusion of one substance through a second substance which is confined between membranes

A point of considerable interest concerning steady-state diffusion was raised by Hartley and Crank (1949). Let a substance B be confined between membranes which are impermeable to B. Also let the concentrations of A in contact with the membranes be maintained by supply and removal of A through the membranes from and to reservoirs of vapour or of solutions of A in B or in any other substance which cannot penetrate the membranes. It is convenient here to use the ideas and nomenclature of § 10.3 (p. 205). Then in the steady state, sections at fixed distances from the membranes are fixed with respect to amount of component B, and the rates of transfer of A acros all such sections must be equal so that

- DBA dCBA/d£B = constant.

(9.30)

166

SOME CALCULATE D RESULTS FOR

We will assume that the partial volumes are constant. Eqns (10.21), (10.26),(10.28) are

d£B = V°BCvBdx;

dCvJdCBA = {VBCVB)2\

DBA = DV(VBCVB)\

(9.31)

and on substituting these relationships in (9.30) we have

-Dv dC\

——y —^ = constant.

(9.32)

VBCB dx

On using

VA—-+ VB—- = 0,

(9.33)

(9.32) becomes

Dv dCl

T T T ^ -~- = constant.

(9.34)

VACVB dx

If, instead, we maintain the steady state by substituting membranes permeable only to B and supplying and removing B in the reverse direction we find, by interchanging A and B in (9.32) and reversal of signs to allow for the reversal of direction,

Dv dCv

B = constant.

(9.35)

VAC\ dx

It is evident that eqns (9.34) and (9.35) require different concentrationdistance functions. The steady state is therefore different, even between the same concentration limits, according to which component is constrained and which is free to diffuse.

This difference is particularly evident in dilute solutions. We shal assume here, in the interests of simplicity, that Dv is constant. The concentration of A being very low, VBCVB can be assumed to be unity. Eqn (9.32) now becomes

dCv

Dv—  ̂ = the constant rate of transfer of A.

(9.36)

dx

This is valid for A diffusing and B restrained.

Substituting from (9.33) we may modify (9.35) to

Dv dCv Dv

A = -—- (In CVA) = constant rate of transfer of B.

(9.37)

VBC\ dx VL

This is valid for A restrained and B diffusing between the same concentration limits.

It will be seen that when the dilute component is diffusing its concentration gradient under these simple conditions is linear. When the same limits are

VARIABL E DIFFUSIO N COEFFICIENT S

167

maintained by diffusing the 'solvent' through membranes impermeable to the 'solute', the gradient of the logarithm of concentration of the latter is linear and hence the concentration itself varies exponentially with distance.

When the total fall of concentration ACVA of the dilute constituent is smal compared with its mean concentration, (9.36) becomes

rate of transfer of A = —- ACVA,

(9.38)

and (9.37) becomes

Dv ACV

equivalent rate of transfer of B = — TT^,

(9.39)

« CAVB

where / is the distance between the membranes. The rate of diffusion of water in such a system down a given, small, mean vapour pressure gradient is therefore not expected to be constant but to be inversely proportional to the mean concentration of the solute. It will further be proportional to the diffusion rate of the solute given by (9.38). Thus if water diffuses from 991 per cent to 990 per cent relative humidity through a layer containing hydrogen chloride, it will do so about twice as rapidly as when the layer contains sodium chloride. If the diffusion occurs from 90-1 per cent to 90-0 per cent relative humidity, each rate will fall to one-tenth of its former value.

These conclusions refer to the case where the membranes are separated by a fixed distance. If, as is more likely to be true in practice, the membranes confine a given amount of component A so that the volume between them will vary inversely as the mean concentration of A, the distance / in (9.39) will be more nearly inversely proportional to CA than constant. In this case the rate of transfer of B will be, to a first approximation, dependent on ACA only and not on the mean value of CA. This result may be obtained directly from equations in £ in the treatment given of the swelling membrane in § 10.6.5. (p. 239).

Diffusion of solvent through a constant amount of solute per unit area thus behaves more simply than diffusion through a constant thickness. This conclusion is not at once obvious and may have some important applications in physiological processes.

A second conclusion of interest may be drawn when we consider what happens in such a steady-state system if the membranes are suddenly rendered completely impermeable. Sections fixed with respect to the membranes are now fixed with respect to volume of solution. The change of concentration with time will therefore from now on be governed by

ct ox \ ex

but, at the instant of change of membranes, (9.32) still holds if A has been the

168

SOME C A L C U L A T E D RESULTS FOR

diffusing component, whence

r\

P\fV\

r\f~*V

r\f~*V

— Dv

= -constant x VB—- = constant x VA—±. (9.41)

ox ox I

ox

ox

Combining (9.40) and (9.41) we obtain

- H = -constant x VA,

(9.42)

^ | dx = dCvA = 0,

(9.43)

since

dt

for CVA constant. Now the constant in (9.30) and (9.42) is the rate of transfer of A at the steady state in standard units of amount. Multiplied by VA it represents the volume rate of transfer of A, or, since we are always considering transfer acros unit area, the linear velocity with which A appeared to pass through the system.

We thus find that, at the instant when A ceases to flow through, the whole concentration-distance distribution commences to move backwards at the velocity with which substance A previously passed through the membrane.

With increasing time, the distribution will flatten out, of course, from the low concentration upwards as the substance A, diffusing down the gradient now,accumulates.

It is evident, therefore, that in the steady state during the passage of substance A there was superimposed on the true diffusion proces a real flow of the whole system.

9.2. Non-steady-state conditions

We present here, in graphical form, a collection of solutions of the equation for diffusion in one dimension. They have been evaluated by one or other of the methods described in Chapters 7 and 8, and refer to various types of concentration-dependent diffusion coefficients and three simple boundary conditions. Solutions for the infinite medium refer to the initial condition

c c

For sorption in a semi-infinite

C=C0;

c = o,

= c,,= c2,

medium, x =

X >

X

X

the 0,0,

<o,

> 0.

conditions are

t > 0,

t = 0,

(9.44)(9.45)

(9.46)(9.47)

VARIABL E DIFFUSION COEFFICIENTS

169

and for desorption

C = 0,

c = c o ,

x = 0,x > 0,

> 0,= 0.

(9.48)(9.49)One example of each type of diffusion coefficient considered is shown in Figs. 9.4(a) and 9.4(b).

20

16

12

0

00 0-2 0-4 0-6 0-8 1-0 0-0 0-2 0-4 0-6 0-8

c

c

FIG. 9.4. Some typical diffusion coefficients.

1. D/Do = 1 + 10(1 -e "2 ' 3 0 3' ) .

5. D/Do = e"2 '3 0 3'

6. D/Do = 1/(1-3-292c +2-877c2).

10

2. D/Do=  1+50 In (1+0-5136c).

3. D/Do = l+9c.

4. D/Do = e2 3 0 3c

7. D/Do = l/(l-0-6838c)2

8. D/Do=  1/(1-0-9c).

9.3. Concentration-distance curves

Shampine (1973a) used a Runge - Kutta computer library program to obtain numerical solutions of the Boltzmann diffusion equation (7.10) subject to C = 1, */ = 0; C = 0, >/ = oo. His 'shooting method' is analagous to that of Lee, § 7.2.2 (iii ) (p. 108). Tabulated values of C(rj) for each of the eight diffusion coefficients listed below Fig. 9.4 may be obtained from L. F. Shampine. In his paper, he also examines the existence and uniquenes properties.

The shapes of the concentration-distance curves are characteristic of the diffusion coefficient and of the boundary conditions. They do not conform to quite such a simple classification as do the corresponding curves in the steady state. Thus, as we saw earlier in § 9.1.1. (p. 162) Barrer (1946) was able to write,with regard to the results of his steady-state calculations, that whenever D increases as C increases, concentration-distance curves are convex away

170

SOME C A L C U L A T E D RESULTS FOR

FIG. 9.5. Concentration-distance curves for D = Daexp p{C-2iCl +C2)} , where jS is positive and given by P{C2 — Cl) = l n ^ / D J. Numbers on curves are values of D1/D2. Dl and D2 are values of D at Cx and C2 respectively.

from the distance axis. Figs. 9.8 and 9.10 show that this is true also for curves relating to desorption from a semi-infinite medium when D is a linearly or exponentially increasing function of concentration. Figs. 9.7 and 9.9 show that for these diffusion coefficients the statement holds also for sorption by a semi-infinite medium over the greater part of the concentration range, but that there is an important difference in behaviour in the region of low conFIG. 9.6. Concentration-distance curves. D = Daexp P{C-2iCl + C2)} , where ft is negative and given by (C2 - Cx) = In {DJD^). Numbers on curves are values of D2/Dl. Dl and D2 are values of D at Cx and C2 respectively.

VARIABL E D IFFUSIO N COEFFICIENT S

171

00

FIG . 9.7. Concentration-distance curves for  linear  diffusion coefficients during sorption for D = D0(l + aC/C0). Numbers on curves are values of a.

centration. This difference is a direct consequence of the boundary condition.

In the steady state, the condition is that the concentration shal have some fixed value, possibly zero, at the face of the membrane through which the diffusing substance emerges. When diffusion occurs into a semi-infinite medium, however, the condition that the concentration shal approach zero at infinity means that the gradient of concentration tends to zero at the limit of penetration into the medium. This produces a point of inflexion in any concentration-distance curve which is convex away from the distance axis at high concentrations. The curves of Fig. 9.11 relate to a diffusion coefficient which increases as C increases but does so at a steadily decreasing rate (see Fig. 9.4(a)). We see that in this case the concentration-distance curves may be convex downwards. The curves of Figs. 9.12 and 9.13 conform with these statements.

The curves shown in Figs. 9.5 and 9.6 for infinite media follow the same general pattern as for the semi-infinite media, except that the boundary conditions ensure that the concentration gradient becomes zero at each end.

172

SOME CALCULATED RESULTS FOR

10 11 12

FIG. 9.8. Concentration-distance curves for linear diffusion coefficients during desorption for D = D0{l+aC/C0). Numbers on curves are values of a.

200

FIG. 9.9. Concentration-distance curves for exponential diffusion coefficients during sorption for D = Do exp (kC/C0). Numbers on curves are values of e\ being the ratio of D at C = Co to D at C = 0.

VARIABL E DIFFUSION COEFFICIENTS

173

9.3.1. Correspondence between sorption and desorption

If (Co — C) is written for C, the diffusion equation in one dimension is unchanged but the conditions (9.46) and (9.47) become respectively (9.48)and (9.49). This means that the solution for sorption when D is a given function of C is also the solution for desorption when D is the same function of(Co — C) and vice versa. For example, the sorption curve for D = Do exp (kC)is also the desorption curve for

D = Do ef c ( c°-C) = (Do efcCo) e"fcC

This allows general statements corresponding to those of § 9.3 to be made for diffusion coefficients which decrease as concentration increases.

Helfferich (1963) has drawn attention to the general nature of this correspondence principle. One system is specified by

dCJdt = div (Dt grad Q,

Dt = /i(ct),

(9.50)

10 0-9

0-8 0-7 0-6 0-5 0-4

0-3 0-2 01

n.n

Ct = /2(x),

/f

i

i

x > 0, t = 0,x = 0, t > 0,

1

1

1

FIG. 9.10. Concentration-distance curves for exponential diffusion coefficients during desorption for D = Do exp (kC/C0). Numbers on curves are values of e\ being the ratio of D at C = Co to D at C = 0.

174

SOME CALCULATED RESULTS FOR

FIG. 9.11. Concentration-distance curves during sorption for D = DO{1 +501n(l +/cC/C0)} .

Numbers on curves are values of 1 + 50In(l +/c), being the ratio of D at C = Co to D at C = 0.

where / t , f2, and /3 are known functions. The solution is

C,. = F(x, t).

The solution remains the same if C, is replaced by C0 — Cj, where C, is variable and Co is a constant equal to or greater than the maximum concentration Cf occurring in the problem. Thus, once calculated, the solution F(x, t) provides the solution also to the corresponding problem

dCj/dt = div (Dj grad C,),

Dj = gl(Cj)=f1(Co-Cj)9

Cj = g2(x) = C0-/2(x), x > 0, t = 0,

VARIABL E DIFFUSION COEFFICIENT S

175

10

0-9

0-8

0-7

0-6

f 05

0-4

0-3

0-2

01

00 L

10 xj{ADot)\ 2-0

30

FIG . 9.12. Concentration-distance curves during sorption for

D = ( l -aC/C0) '

Numbers on curves are values of 1/(1 —a), being ratio of D at C = Co to D at C = 0.

and the solution is

Helfferich lists some typical corresponding solutions for sorption and desorption. The correspondence principle applies in two and three dimensions and in anisotropic media provided that each diffusion coefficient along the principal axes obey a correspondence relation.

The diffusion coefficient may depend on time and position, in addition to concentration and the absolute value of the concentration gradient, provided the dependence is the same in the corresponding functions /x and gx. Temperature- and stress-dependent diffusion systems can also correspond.

176

SOME CALCULATED RESULTS FOR

10

0-9

0-8

0-7

0-6

0-5

0-4

0-3

0-2

01

0-0~

10

20

30

40

Jc/(4Z)0/)i

FIG. 9.13. Concentration-distance curves during sorption for

D = (l-aC/C0)2

Numbers on curves are values of 1/(1 —a)2, being ratio of D at C = Co to D at C = 0.

9.3.2. Common points of intersection

Stokes (1952) drew attention to the fact that if a large-scale graph is prepared from the data of Table 7.3 (p. 384) an interesting property emerges.

Two concentration-gradient curves are shown in Fig. 9.14, one for a constant diffusion coefficient and the other for a diffusion coefficient varying linearly with concentration, the value at the higher concentration being 0-1406 of that at the lower concentration. The other curves are omitted to avoid confusion of the diagram but on his large-scale plot Stokes found that whatever the

t Garg and Ruthven (1972) calculated concentration, and sorption and desorption curves in zeolite spherical crystals for this D and that of Fig. 9.12.

VARIABL E DIFFUSION COEFFICIENTS

177

0-7

0-6

0-5

& 0-4

Y 0-3

s

0-2

01

-2-5 - 20 -1-5 - 10 -0-5

FIG. 9.14. Comparison of concentration-gradient curves. Curve I. For a constant diffusion coefficient. Curve II. For a diffusion coefficient varying linearly with concentration, the value at the higher concentration being 0-1406 of that at the lower concentration.

value of b, all his curves appeared to pass through the point P (Fig. 9.14) of coordinates

dC/dya

y, = 1-205,

=  -0-133.

The nomenclature here is that of §7.2.4. (iii ) (p. 118). If a similar large-scale graph of (C—C2)/(Cl — C2) is prepared from the data of Table 7.4 (p. 385),there appear to be two common points with coordinates

ya = +0-66, (C-C2)/(Cl-C2) = 0-176;

ya = -0-66, (C-C2)/(C1-C2) = 1-0-176 = 0-824.

If the sorption curves of Fig. 9.7 for linear D are replotted against the variable ya they too pass through a 'common point' of coordinates ya = 1-00,C/Co = 0-157. For the replotted desorption curves of Fig. 9.8 the common point is ya = 1-09, C/Co = 0-872. Similar common points are found in other cases. For example, when the curves of Fig. 9.9 for exponential diffusion coefficients are replotted against x/(4Dt)% where D is the integrated mean value D0(Qk— l)//c, they all pass approximately through the point for which C/CQ = 0-25 and x/(4Drf = 0-85.

We can obtain a partial understanding of the significance of these apparently common points by looking at the limiting case of a linear diffusion coefficient of very large range. Thus, a very large D = D0(l +aC/C0) is approximated by D = DoaC/Co, except for very smal C, and this is the form examined by

whose solution is given in §7.2.4 (iv) (p. 119). Wagner's D o is to be identified with D o a of this section, as the value of D when C = C o . Thus, the two curves of Fig.  7 .5 are approximations to the two limiting cases of linear diffusion coefficients having infinite and negligible ranges. When these limiting curves are replotted against the variable y a = x/(4D a tf, where now D a is the diffusion coefficient at C = \C 0 , they intersect at a point very close to the common point of intersection of the replotted curves of Fig.  9 .7 given by y a = 1-00, C/C o = 0-157. Similarly, the replotted Wagner's curve of Fig.  7 .6 for the infinite medium intersects the corresponding curve for a constant diffusion coefficient in two points which are approximately the common points of intersection demonstrated by Stokes from the data of Table  7 .4 (p. 385). A much cruder, but useful, limiting case of an exponential diffusion coefficient of large range is provided by the discontinuous coefficient in. Fig.  13 .7(a) (p. 294) as C x approaches C t . In this case (13.13) and (13.18) for C 2 = 0 and C x -C l small show g(fc/2Df), and hence k/(2D\\ to be small. Writing k/2D\ = 7, say, we have from (13.13), g(Y) = n±Y 2 (l + Y) = n^Y 2 = approximately. Thus, using (13.11) and (13.18), we have

C x since C x is approaching C 1 .

But for the discontinuous diffusion coefficient we have and so finally X 1

= ^ = °'75

= ^ = °'75

Now X is the position of the discontinuities in the concentration curves of Fig.  13 .7, and replotting them against x/(4Dt)* confirms that as C x - >  C 1? X/(4Dtf approximates to 0-75. The intersection with the concentration curve for a constant D will be at about X/{4Dtf = 0-75, C/C l = 0-3, which is not far from the 'common point' of the replotted curves of Fig.  9 .9. Wilkins (1963) , however, carried out a more accurate and systematic study of the concentration curves associated with linear diffusion coefficients of the form D = D 0 (l+aC/C 0 ). He obtained series solutions for a = -1 as well as a = oo (see § 7.2.4, (iv), p. 124) and for small values of a. Table  9 .1 summarizes Wilkins' findings on the positions of the various intersection points and shows that they are quite insensitive to a but not strictly independent of a.

The application of these points to the measurement of concentration dependence as suggested by  Stokes (1952)  and  Crank and Henry (1949b)

References

VARIABL E DIFFUSION COEFFICIENTS

179

is still possible provided the 'spread' demonstrated by Wilkins is within the errors of observation in a practical experiment.

9.4. Sorption- and desorption-time curves

On the basis of the sorption and desorption curves shown in Figs. 9.15,

9.16, and 9.17 and of corresponding curves published elsewhere (Crank and Henry 1949a) we may draw the following general conclusions for a system in which the diffusion coefficient increases as concentration is increased but does not depend on any other variable.

(i) In the early stages, when diffusion takes place essentially in a semiinfinite medium, the amount sorbed or desorbed is directly proportional to the square root of time. This is true, incidentally, whatever the relationship between the diffusion coefficient and concentration, and follows directly from the fact that for the prescribed boundary conditions concentration depends on the single variable x/t* (§ 7.2.1, p. 105). When D increases with concentration increasing, the linear behaviour may extend well beyond 50 per cent of the final equilibrium uptake in the case of sorption. The same is true for desorption when D decreases with concentration increasing.

01 0-2 0-3 0-4 0-5 0-6 0-7 0-8 0-9 10

FIG. 9.15. Sorption curves for D = D0(l+aC/C0). Numbers on curves are values of a.

180

SOME CALCULATED RESULTS FOR

u<

01 0-2 0-3 0-4 0-5 0-6 0-7 0-8 0-9 10

FIG. 9.16. Desorption curves for D = D0(l +aC/C0). Numbers on curves are values of a.

(ii) When they cease to be linear, the sorption and desorption curves plotted against (time)" each become concave towards the (time)1 axis,and steadily approach the final equilibrium value. This is true for all the calculated results obtained for the initial and boundary conditions (9.46),(9.47), (9.48), (9.49) and it is reasonable to conclude that it is a quite general result though no satisfactory general proof has yet been produced. It is an important property because sorption curves have been observed experimentally (Crank and Park 1951; Mandelkern and Long 1951) which show points of inflexion when plotted against (time)*, i.e. there is a region in which the curve is convex to the (time)1 axis. This has been taken as evidence either that the boundary condition (9.46) does not describe the experimental conditions, or that the diffusion coefficient is a function of some variable other than concentrations. Prager (1951) has given a general proof that sorption and desorption curves when plotted against time can never become convex to the time axis, but this is a less stringent restriction than the one just put forward. His proof is as follows.

We wish to show that the integral

= rJoC(x,t)dx,

(9.51)

VARIABL E DIFFUSION COEFFICIENTS

181

0-0 01 0-2 0-3 0-4 0-5 0-6 0-7 0-8 0-9 10 11

(AW/2)*

FIG. 9.17. Sorption and desorption curves for exponential diffusion coefficient D = Do exp {kC/C0).

Numbers on curves are values of ek being ratio of D at C = Co to D at C = 0.

obtained as a solution of

Ddc

(9.52)

with the conditions

C = Co = constant, x = 0, x = /, t > 0,

(9.53)

C = 0, 0 < x < /, t = 0,

(9.54)cannot yield an inflexion point when plotted against t. The diffusion coefficient D is a function of concentration C only and is always positive. On writing

(9.52) becomes

with conditions

s(C) =

D(C)dC,

Jo

d2s ds

s = So, x = 0, x = /, r > 0,5 = 0, 0 < x < /, t = 0.

(9.55)

(9.56)

(9.57)(9.58)

182

SOME CALCULATE D RESULTS FOR

Furthermore, since the rate of transfer acros unit area normal to the xdirection is given by — D 8C/8x = — ds/dx, we have

dMt= -2ds\dxjx=0

(9.59)

allowing for the symmetry of the problem. Because dMJdt is infinite when t = 0, it follows that if there is to be a point of inflexion at some later time,dMr/dt must go through a minimum, and so (ds/dx)x = 0 must go through a maximum as a function of t. This in turn requires that there is some finite length of time, extending just beyond that at which the inflexion is supposed to occur, during which

dt [dx

(9.60)

x = 0

Also, since s = So is constant at x = 0 and x = /, ds/dt must also be negative during that time near x = 0 and x = /. We now show that this is impossible for the given initial and boundary conditions.

For very smal r, the condition dC/dt ^ 0 holds for all x, because we cannot have negative concentrations. Since D is positive everywhere this means that ds/dt = D dC/dt must also be positive or zero everywhere for sufficiently smal t. But dC/dt, and hence ds/dt, is continuous everywhere and ds/dt must therefore first be zero if it is to become negative. Let x = X be the first point at which ds/dt = 0 excepting x = 0 or x = I where this is always true.

Then ds/dt will be positive or zero on both sides of X, i.e. it will show a minimum at X when plotted against x so that

or

dx2

8 8~t

8s

Jt

82s

(9.61)

x = X

But it follows from (9.56) that since ds/dt = 0 at x = X, so also d2s/dx2 = 0 there. Eqn (9.61) then indicates that in the next instant (d2s/dx2)x = x is positive or zero, and so using (9.56) again and remembering that D > 0 we see that (ds/dt)x = x becomes positive or zero. Thus ds/dt can never become negative and so there can never be a point of inflexion in the plot of Mt against r, i.e. in the uptake curve plotted against time.

(iii ) If D increases as concentration increases, the shape of the sorption curve when plotted against time is not very sensitive to the form of the diffusion coefficient. It is often not significantly different from the corresponding curve for a constant diffusion coefficient. This is, of course,

VARIABL E DIFFUSION COEFFICIENT S

183

because the sorption curves are parabolic, i.e. linear against (time)*, over most of their length. The desorption curves when plotted against time are much more sensitive to the form of the diffusion coefficient if this increases as concentration increases. If the diffusion coefficient decreases as concentration increases, then the desorption curve will approximate to that for a constant diffusion coefficient.

(iv) When D increases with concentration increasing throughout the relevant range of concentration, desorption is always slower than sorption,and conversely if D decreases with concentration increasing. This is illustrated by Fig. 9.17. In particular, the last stages of desorption are much slower than those of sorption if D increases with concentration increasing, and vice versa.

Crank and Henry (1949a) examined the sorption and desorption curves associated with a diffusion coefficient which passes through a maximum value at some intermediate concentration. Three such diffusion coefficients are shown in Fig. 9.18, where c = C/Co as usual. They correspond to the algebraic relationships:

D/Do=  l + 14-8c(l-c),

D/Do = 1 + 100c2 exp ( - 10c2),

D/Do = 1 +100(1 - c )2 exp {-10(1 -c )2} .

(9.62)(9.63)(9.64)

r

I 20

1

S 10

00

0

01 0-2 0-3 0-4 0-5 0-6 0-7 0-8 0-9 10 Concentration c

FIG. 9.18. Diffusion coefficient-concentration relationships.

All three satisfy the conditions D/Do = 1 when c = 0 and c = 1; and the maximum value of D/Do is approximately 4-7 in each case. Eqn (9.62) is a symmetrical form in which this maximum occurs at c = 0-5, while the maximum values for (9.63) and (9.64) are at c = 0-3 and 0-7 respectively, since(9.64) follows immediately from (9.63) by writing (1 — c) for c. The sorption and desorption curves for these diffusion coefficients are presented in Fig. 9.19.

184

SOME CALCULATE D RESULTS FOR

1-Or

0-9

0-8

0-7

C5 0-6

0-5

g- 0-4

o

3 0-3

0-2

01

(i) />//)„= l + 14-8c(l-c)

(ii) D/Do= 1+100c2cxp(-10c2)

(iii ) Z)/Z)0 = l +100 (l-c)2exp [-10

0-0

01

0-2 0-3 0-4 0-5 0-6

FIG . 9.19. Sorption and desorption curves.

Since (9.62) is symmetrical in c and (1 — c) it follows from what was said above that for the boundary conditions considered the sorption- and desorptiontime curves are coincident, and this is, of course, true for any symmetrical relationship between D and c. The results show that for D given by (9.63)with a maximum at c = 0-3 the desorption curve lies wholly above that for sorption, while the opposite is true for the relation (9.64) where the maximum value of D occurs at c = 0-7.

The relative behaviour of the sorption- and desorption-time curves is affected by the relative values of the diffusion coefficient at c = 0 and c = 1,and also by the position of the maximum in the D-c curve if one occurs.

This suggests that, in some cases, the desorption curve may be above the sorption curve in the early stages of diffusion but later may cross it so that the final stages of desorption are again slower than those of sorption. This is likely to occur when there is a maximum in the diffusion coefficient-

concentration relationship and when the value of D at c = 1 is greater than at c = 0.

In order to study this behaviour a diffusion coefficient-concentration relationship of the form

D/D o = 1 + a erf (fie) + yc (9.65)

was used, where a, /?, y are constants for any one curve. There is no significance in the precise form of (9.65) except that it leads to diffusion coefficientconcentration curves of the desired form and is convenient to handle numerically. From (9.65) we have = ^fexp(-/J 2 c 2 ) + 7 = 0, (9.66)

when D has a maximum value. All curves given by (  9  is shown in Fig.  9 .21 together with the sorption-and desorption-time curves.

The curves intersect at

(D 0 t/l 2 f = 0-29.

For values of (D 0 t/l 2 )* less than this, desorption proceeds more rapidly than sorption but after the intersection the desorption curve lies below that for sorption. This is to be contrasted with the sorption and desorption curves shown in Fig.  9 .22 which do not intersect and which are for a diffusion coefficient of the form  (19.69)  This diffusion coefficient is also shown inFig. 9.22 where it is seen to differ from that defined by (9.67) in that it has a maximum value at c = 0-6 instead of c = 0-25.

D/D o = 1+29-86 erf (0-98c)-23-40c.

References

186

SOME CALCULATE D RESULTS FOR

^0- 8

8

£0-6

§-0-4

1

0-25

_

-

- /

c

f

1

10

1

00

0-2 0-4 0-6 00

0-2 0-4 0-6 00

4-7

Q

10

o 0-6

CO

§-0-4

c

•2 0-2

g

7

_

//

///f I

|

0-6

f v

\

1

c 10

/

/

?

I

i

0-2 0-4 0-6

FIG. 9.22

FIG. 9.20

FIG. 9.21

Sorption and desorption curves.

FIG . 9.20. D/Do = 1 +4-06 erf (14-50c)-2-56c.

FIG . 9.21. D/Do = 1 +4-62 erf (6- 10c)-3- 12c.

FIG . 9.22. D/Do = 1+29-86 erf (0-98c)-2340c.

maximum value of D/Do = 4-7, as the position of the maximum values moves back from c = 1 to c = 0 there is first a range of positions of the maximum for which the whole proces of desorption is slower than sorption. Continuing to move the position of the maximum towards c = 0 there is evidently a further range of positions for which the desorption and sorption curves intersect, the point of intersection occurring at successively larger values of Dot/l2 as the position of the maximum moves towards c = 0. There is some intermediate position of the maximum for which the desorption curve crosses the sorption curve at the origin only and this is the limiting case between sorption and desorption curves which intersect for t > 0 and those which do not.

For this set of curves having D/Do = 2-5, c = 1, it is found that the limiting position of the maximum for which intersection of the sorption and desorption curves occurs at Dot/l2 = 0 is about c = 0-26. When the maximum occurs at higher values of c than this, desorption is slower than sorption right from D0t/l2 = 0, but when the maximum lies in the range 0 < c < 0-26 the desorption curve is first above the sorption curve but crosses it later so that the final stages of desorption are again slower than those of sorption.

VARIABL E DIFFUSION COEFFICIENT S

187

Still confining attention to the general form of variable diffusion coefficient expressed by (9.65), it is to be expected that the critical position of the maximum for which the sorption and desorption curves have equal gradients in the neighbourhood of t = 0 when plotted against (D0t/l2)*  will vary as the value of D at c = 1 is caused to vary, taking the maximum value of D to remain constant and the condition D/Do = 1, c = 0, to be satisfied in all cases. This expectation is confirmed by the results presented graphically in Fig. 9.23 where the critical position of the maximum is plotted as a function of the value of D/Do at c = 10. The critical position is seen to move towards c = 0 as the value of D at c = 1 is increased.

5 r

5"

I

Sorption quicker  than desorption —curves do not intersect intersect

Sorption slower  than"

desorption initiall y —

curves intersect

Sorption slower  than desorption —curves do not intersect

,J>orption quicker  than desorption

initiall y — curves intersect 00 01 0-2 0-3 0-4 0-5 0-6 0-7 0-8 0-9

Concentration c at which D/Do has a maximum value

FIG. 9.23. Critica l position of the maximum of D/Do as a function of D/Do at c = 10.

The points at each end of the curve of Fig. 9.23 were arrived at by general reasoning and the intermediate points by calculation. Thus considering first a D-c curve for which the value of D/Do at c = 1 is very close to 4-7,which is the value of the maximum D/Do for this family of curves, it is clear that, in general, for a D-c curve of this type the diffusion coefficient is effectively increasing over the whole range of concentration, and sorption will be quicker than desorption throughout. This is true for all positions of the maximum except when it is so near to c = 0 that the diffusion coefficient is effectively constant over the whole range of concentration, in which case the sorption- and desorption-time curves coincide throughout and c = 0 is therefore the limiting position of the maximum when D/Do = 4-7 at c = 1.

By an extension of this argument the critical position of the maximum can be determined when D/Do = 0 at c = 1. It was seen above that the sorption-time curve obtained when D is a certain function of c is the same as the desorption-time curve when D is the same function of (1 -c) and vice versa.

It follows immediately that if the initial rates of sorption and desorption are equal when D is a certain function of c, they will also be equal when D is the

same function of (1 -c), i.e. if the critical position of the maximum value of D is c = c m in the first case, it will be c = 1 -c m in the second case. Now if D is a function of c such that D is very small when c = 1, the corresponding function of (1 -c) is such that the value of D at 1 -c = 1 is relatively very close to the maximum value of D. This function approximates to the type just considered above and the critical position of the maximum value of D is at (1 -c) = 0 and therefore at c = 1 for the original D-c curve.

For any D-c curve of the general family under discussion, the relative behaviour of the sorption-and desorption-time curves can be deduced from Fig.  9 .23 if the value of D/D o at c = 1 and the position of the maximum are known. Four regions are to be distinguished, in two of which the sorptionand desorption-time curves intersect at some time, t  >  0, and in the other two they do not intersect when t  >  0. When the value of D/D o at c = 1 exceeds unity, the initial rate of desorption is more rapid than that of sorption if the curves intersect, and vice versa when D/D o  <  10 at c = 1. The critical position of the maximum no doubt depends on the magnitude of the maximum value of D, and also for a given maximum value it will depend to some extent on the detailed shape of the diffusion coefficient-concentration curve. These aspects of the problem have not yet been investigated.

The relative rates of sorption and desorption are also examined later ( § 13.2, p. 387) for diffusion coefficients which are discontinuous functions of concentration  (Crank and Henry 1951) . If the sorption and desorption curves of Figs. 13.1(d) and 13.2(d) are plotted on one diagram they are found to intersect markedly. A particular example is shown in Fig.  9 .24 for the diffusion coefficient shown in the inset. These curves are for a diffusion coefficient which is infinite over an intermediate range of concentration and it is easy to see the condition necessary in this case for intersection. Referring again to Figs. 13.1 and 13.2 and using that nomenclature, we see that the height of the initial vertical part of the sorption curve of Fig.  13 .1(d) is IC X , and that of the corresponding part of the desorption curve (Fig.  13

.2(d)) is l(C 1 -C Y ). Hence, provided D is greater at high than at low concentrations, intersection occurs if C x -C Y exceeds C x , so that ^a), (9.70)

where a is the concentration range over which D is infinite. Thus the limiting case is when this range is symmetrically situated with respect to the whole concentration range 0 to C x . If the infinite region is mainly in the upper half of the concentration range, desorption is slower than sorption throughout, but if it is mostly in the lower half the sorption and desorption curves intersect.

Clearly, the point of intersection occurs earlier the smaller D 2 is compared with D t in Fig.  13 .1(d). Fig.  9 .25 shows sorption and desorption curves for the diffusion coefficient shown in the inset. These curves were calculated by the numerical methods

References

VARIABL E DIFFUSION COEFFICIENT S

189

10

0-9

0-8

0-7°* 6

05

3

£ 0-4

31

I 0-2

01

I

1

I

I

000 001 002 003 004 005 006 007 008

FIG. 9.24. Sorption and desorption curves.

described in Chapters 7 and 8. Although the value of D in the middle concentration range of the inset of Fig. 9.25 is still relatively high, the intersection is much less marked in Fig. 9.25 than in Fig. 9.24 and becomes even less pronounced if the largest value of D is decreased further.

9.4,1. Effect of the initial concentration on the rate of sorption

It might be expected that the initial rate of sorption by a sheet having a finite, uniform concentration of diffusing substance in it initially would be greater than the corresponding rate for zero initial concentration if the operative diffusion coefficient is smal at low concentrations. Such an effect has been observed experimentally, e.g. by King (1945) for the uptake of methyl alcohol by wool. The effect should be most marked when the diffusion coefficient is zero at low concentrations as in Fig. 13.7(a) (p. 2 94). A convenient measure of initial rate of sorption is the initial gradient of the sorption curve when plotted against (time)*  as in Fig. 13.7, i.e.

dT*\/ C— i , where T =

(9.71)

190

SOME CALCULATE D RESULTS FOR

i

i

i

i

i

I

I

1

000 001 002 003 004 005 006 007 008

D2t/P

FIG. 9.25. Sorption and desorption curves.

l-5r

I 1 0

- 0 - 5

00 01 0-2 0-3 0-4 0-5 0-6 0-7 0-8 0-9 10 Initia l fractional uptake C2/Cl

FIG. 9.26. Effect of initia l uptake on initia l rate of sorption.

VARIABL E DIFFUSION COEFFICIENT S

191

The nomenclature is that of Chapter 13 and Figs. 13.6 and 13.7. The initial rate so calculated is shown in Fig. 9.26 as a function of C2, the initial uniform concentration in the sheet (Crank and Henry 1951). The different curves refer to different values of Cx, the concentration at which D changes discontinuously. In all cases, the initial rate of sorption decreases as the initial regain is increased. This, then, is a further characteristic feature of a purely concentration-dependent system, and in systems which show qualitatively different behaviour some factor other than concentration-dependence must be sought as the cause.

9.5. Diffusion-controlled evaporation

Some evaporative processes are diffusion controlled in the sense that the rate of evaporation depends largely on the rate at which solvent or mixture is supplied to the evaporating surface by internal diffusion. An important consideration is the effect of the proportion of solvent vapour, or the relative humidity, in the atmosphere into which the evaporation takes place. Instances have been reported (Crank 1950), when evaporation takes place through an organic membrane or a polymer film, in which the rate observed in practice is increased by increasing the relative humidity at the evaporating surface. This behaviour has been attributed to the effect of a diffusion coefficient which is low at low solvent concentrations, the argument being that by maintaining some vapour in the outside atmosphere the concentration range over which diffusion within the sheet is difficult is removed. It has been shown theoretically (Crank 1950), by evaluating solutions of the diffusion equation for appropriate diffusion coefficients and boundary conditions, that such behaviour is not to be expected in a purely concentration-dependent system. Both the steady-state evaporation through a membrane and the loss of vapour from a sheet containing solvent have been examined.

9.5.1. Steady-state evaporation through a membrane

We saw in § 4.2.2 (p. 46) that if we have a membrane of thicknes / separating a region of high from one of low vapour pressure, then the rate of evaporation through the membrane in the steady state is F, where

F = (1//) f ° DdC.

(9.72)

Here Co and Cx are the concentrations just within the surfaces of the membranes on the high- and low-pressure sides respectively. The argument leading to (9.72) is true whether D is constant or not. In particular it is true when D is a function of concentration, and provided D is never negative in the range from Co to Cl, the integral in (9.72) must always increase or remain constant as the range of concentration is increased. Thus, as Park has pointed out (see

SOME CALCULATED RESULTS FOR

SOME CALCULATED RESULTS FOR

Abstract

Crank 1950) if the high concentration remains fixed, the rate of evaporation F can never increase as a result of increasing the lower concentration C l5 i.e. the rate of evaporation is greatest into an atmosphere completely free of solvent vapour. Where the experimental facts genuinely differ from this, some alternative explanation must be found.

Abstract

Nooney (1973)  gives examples of hypothetical diffusion coefficients that yield anomalous behaviour. Their essential property is that they become zero or infinite on some surface within or on the entry surface of the membrane.

Abstract

fc, so that D = 2x*/T 2 and D(0,1) = 0 while dC(0)/dx = oo. In his second example, D(x, C) = ix*(l -C)~*. Then C(x) = \-hx 2 and F = h~\ so that D(x, C) = /T^x" 1 and D(0,1) = oo while dC(0)/dx = 0. In both examples, F increases as C(l) increases.

Further insight into the effect of changing the vapour pressure on the low-pressure side when D depends only on concentration is given by Fig.  9 .27. Calculated distributions of concentration through the membrane are shown for a case in which D is an exponential function of concentration such that D increases by 50-fold from C = 0 to C = C o . The concentration, C o , on the high-pressure side is the same for each curve, but in one case C x = 0 and in the other C 1 = jC 0 . The curves show how the concentration distribution adjusts itself so that the rate of flow is greater when C l = 0, even though the region of low diffusion coefficient is then included. Clearly, a low diffusion coefficient is compensated by a high concentration gradient.

References

VARIABL E D IFFUSIO N COEFFICIENT S

193

0-2 0-4 0-6 0-8

Concentration of acetone

(as fraction of initia l concentration)FIG . 9.28. Diffusion coefficients.

10

9.5.2. Evaporation from films and filaments

It is not possible to expres the rate of loss of vapour from a film containing solvent in terms of a simple expression such as (9.72) and so it is less easy to examine the effect of introducing vapour into the outside atmosphere.

However, some illustrative examples have been worked numerically (Crank 1950) for the first diffusion coefficient shown in Fig. 9.28. This is an experimental curve relating to the diffusion of acetone in cellulose acetate. The concentration distributions through a sheet initially containing solvent at a uniform concentration have been calculated for this diffusion coefficient and two different boundary conditions:

(i) The surface of the sheet is assumed to reach equilibrium with the outside

atmosphere instantaneously when evaporation commences, i.e. if the

atmosphere is free of vapour the concentration at the surface falls immediately to zero; if the vapour pressure in the atmosphere is p, the

surface of the sheet immediately reaches the concentration which is in

equilibrium with p.

(ii) A condition expressing the rate of evaporation from the surface is

assumed. This is taken to be

(9.73)

where Cs is the actual concentration in the surface of the sheet at any time

and Co the concentration which would be in equilibrium with the vapour

pressure remote from the surface. The diffusion coefficient Ds is the value

corresponding to the concentration Cs.

194

SOME CALCULATE D RESULTS FOR

00

0-2 0-4 0-6 0-8

10

Fractional distance through sheet

Surface concentration zero

Surface concentration one-tenth

of uniform initia l concentration

through sheet

FIG. 9.29. Concentration distribution s at various times.

Fig. 9.29 shows the calculated variation of concentration with distance through the sheet at two different times for the condition (i), that of vigorous surface evaporation. For each time, curves are shown for the cases in which

(a) the surface concentration falls to zero instantaneously, (b) it falls to onetenth of its initial value instantaneously. We see that there is littl e difference between the two curves at either time. In particular the total solvent content of the sheet at any time, represented by the area under the appropriate curve of Fig. 9.29, is much the same whether the surface concentration falls to zero or to one-tenth of its initial value, i.e. whether the concentration over which D is smal is removed or not. In so far as there is a slight difference, the rate of loss of solvent by the sheet is greater in the vapour-fre atmosphere. As in the steady state, the rate of evaporation is not increased by introducing vapour into the atmosphere.

The reason for this is clear from these calculations as it was in the steady state. When the diffusion coefficient has a smal value at the surface the concentration gradient is correspondingly large so that the rate of loss of vapour, given by D dC/dx at the surface, does not alter appreciably. This compensating effect is most obvious when the diffusion coefficient is zero over a range of low concentrations as in the second diffusion coefficient shown in Fig. 9.28. This is a hypothetical coefficient chosen to exaggerate the effect. The concentration-distance curve for this coefficient is sketched in the inset of Fig. 9.29 from general reasoning. The surface gradient is infinite over the concentration range for which D is zero (in this case for

VARIABL E DIFFUSION COEFFICIENT S

195

concentrations less than 0-10) so that the product can have a non-zero value.

A finite gradient cannot develop for concentrations less than 0-10, since this would imply that solvent had been removed from a region of zero diffusion coefficient under the action of a finite gradient, which is not possible. For such a diffusion coefficient the rate of evaporation is precisely the same for all surface concentrations between zero and 0-1.

The same general conclusion holds for the surface condition (9.73), i.e.

the rate of loss from the sheet is always increased by decreasing the external vapour pressure. Hansen (1968) tabulated concentration distributions and their means for the drying of a lacquer film by solvent evaporation. The concentration-dependent D is approximated by. two exponential curves joined together. Various solvents and drying conditions are covered.

9.6. Effect of a surface skin

Many films and fibres show evidence of a surface skin having properties different from those of the underlying layer or core. In this section we examine the effect of such a skin on diffusion behaviour. The results presented were obtained as part of an attempt to understand some of the peculiar features which are sometimes observed when solvents diffuse into and out of polymer substances (Crank and Park 1951).

We shal restrict ourselves to cases in which the skin and the core are each homogeneous and the boundary between the two is sharply defined.

In the skin the diffusion coefficient is assumed to be either constant or a discontinuous function of concentration, and beneath the skin to be everywhere infinite at all concentrations.

(i) The simplest case is one in which D is constant in the skin, and the medium is semi-infinite. The solution has been given in Chapter 3, eqn(3.57) (p 41), which becomes

M, iDt

2/C0

72

* f 1

»™>

when D2 = oo. Here M, is the total amount of diffusing substance which enters the composite medium in time t if the surface is maintained at a constant concentration Co. When Mt/21CO is plotted as a function of (Dt/l2)*the curve is linear for smal times and its gradient later increases steadily as t increases. When plotted as a function of Dt/l2 the curve is parabolic at first and then becomes linear, the gradient of the linear part being determined by the constant rate of flow acros the outer surface in the final steady state. Both the curves shown in Fig. 9.30 are noticeably different from the corresponding ones for a semi-infinite homogeneous sheet when M, is proportional to r*  for all times.

196

SOME CALCULATE D RESULTS FOR

1-Or

0-2

0-4

0-6

0-8

10

1-2

(Dt/12)± or Dt/12

FIG . 9.30. Sorption curves for  a composite semi-infinite sheet. D in skin is constant; D below skin is infinite , (i) M,/2/Co against Dt/l\ (ii) MJ21CO against {Dt/l2f.

(ii) We consider next a finite sheet having on each surface a skin in which D is a discontinuous function of concentration C of the type shown in Fig.

9.31 (a). The general shape of the sorption-time curve for this case is easily deduced from the concentration-distance curve for the same diffusion coefficient and a homogeneous sheet. Solutions are given in Chapter 13,Figs. 13.6 and 13.7; the sorption-time curve is parabolic for smal times and

0

5

10

15

20

25

Dt/I 2

FIG . 9.31. Sorption and desorption curves for  sheet with skin.

VARIABL E DIFFUSION COEFFICIENT S

197

the concentration-distance curve is characterized by a sharp front which advances according to the square root of time (Fig. 9.3l(b)). It is clear that until this sharp front has penetrated to the inner boundary of the skin the sorption-time curve is the same as for a homogeneous sheet having the properties of the skin throughout. After this the concentration on the outer surface of the sheet remains at Co and that on the inner surface of the skin at Cx til l the uniform concentration throughout the region of infinite diffusion coefficient has reached the value Cx. During this time there is approximately a steady-state flow through the skin so that the rate of sorption by the whole sheet is constant and the sorption-time. curve is linear. When the whole sheet beneath the skin has reached a concentration Cx there is a gradual decrease in rate of sorption as the final equilibrium concentration Co is approached throughout the sheet.

The details of the calculation for this case are as follows. For sorption we require solutions of the usual equation

dc d2c

where in the region 0 < x < /, D is defined by D = 0,

0 < C < Cx,

(9.76)

D = Dl9 CX<C<CO,

(9.77)

and in the region / < x < / + a, D is infinite. The solutions are subject to the conditions

C = Co, x = 0, f > 0 ,

(9.78)

C = 0, 0 < x < / + a, r = 0.

(9.79)

For smal times the concentration-distance curve falls discontinuously from C = Cx to C = 0, and until this vertical part of the curve reaches x = / at, say, time t = t0, the medium is effectively semi-infinite and the solution is

u 0'

( 9'8 0)

where

/lerffc/(2Dt) = Cx-C0,

(9.81)

and the constant k is given by

C —C Tt^k efc2/4£>l

erf(/c/2Df)+ 2D\ °x = °'

(9'82)

After t = t0 the concentration at x = / remains at C = Cx til l an amount

198

SOME CALCULATE D RESULTS FOR

aCx has crossed x = /. During this time the usual solution, §4.3.1, eqn(4.16), (p. 47), for a sheet whose surface concentrations are fixed and in which the initial concentration distribution is /(x), given by substituting t = t0 in (9.80), applies, i.e.

x 2 * Cx cos nn — Co . nnx ,

9 9/ ,l9,

C = CO + (CX-CO)- + - X —

^sin—exp{-/V27r2(r-r0)//2}

i 7i n = i

n

l

2 *  *Mix

Cl

nnx

+ 7 I sml-rexp{-Dln2n2(t-t0)/l2} /(x)sin —dx.

(9.83)

*  M = l

l

^ 0

'

From (9.83) it is easily deduced that the amount M o crossing unit area at x = 0 from time t = t0 onwards is given by

— IM

°° I2

° ( C C ) U ) 2 I

^

(9.84)

< Cx cos «7r - Co + ̂  I / (x) sin ̂  dx >.

I

/ Jo

* J

The amount Mt crossing unit area at x = / in the same time is given by---Ml = (Cx-C0)(t-t0)

" 2 I  (- l r- ^

-C0 +  n^- \ / ( x ) s i n^

x \cxcosnn- 0

/ (x)s in^dxi.

(9.85)

Eqn (9.84) expresses the total amount absorbed by the composite sheet from time r0 onwards and these solutions apply til l M, = aCx as calculated from(9.85). For much of this time there will be approximately a steady-state flow acros the region 0 < x < /.

After the concentration throughout the region / < x < l + a has reached Cx, the boundary condition on x = / is

-D^C/dx = adC/dt,

(9.86)and the solution is conveniently continued by numerical methods described in Chapter 8 using for (9.86) the finite-difference form

dC CS_2-4CS_,+3CS

to ~

Wx '

(9'87)where the range 0 < x < / is divided into equal steps Sx, and Cs+P is the value of C at x = 1 + pSx.

VARIABL E DIFFUSION COEFFICIENT S

199

For desorption we require solutions of eqn (9.75) for the same diffusion coefficient but subject to the conditions

C = 0, x = 0, t > 0,

C = Co, 0 < x < l + a, t = 0.

(9.88)

(9.89)

In this case the concentration-distance curve rises discontinuously at x = 0 from C = 0 to C = Cx, and in the early stages, when the concentration at x = / is not appreciably different from Co to the required accuracy, the solution is simply that for a semi-infinite sheet having a surface concentration

, i.e.

C-CX = (CO-CX) erf7iD.tr

(9.90)

At later times the condition (9.86) again applies and the solution can be continued numerically as for sorption. A typical sorption-time curve is shown in Fig. 9.31 for Cx = \C0 and a skin which forms one-fifth of the halfthickness of the sheet. The corresponding curve for desorption is also shown in Fig. 9.31.

The investigations into the cause of intersecting sorption- and desorptiontime curves discussed in §9.4(iv) (p. 183) suggest that a diffusion coefficient in the skin of the form shown in Fig. 9.32(a) might be interesting. The concentration-distance curve for this diffusion coefficient has a sharp front as in Fig. 9.32(b), and the required mathematical solutions up to the time at which this front reaches the inner surface of the skin are presented in § 13.2.4.

36

(a)

0-5

10

1-5 20

2-5

FIG . 9.32. Sorption and desorption curves for  sheet with skin.

200

SOME CALCULATE D RESULTS FOR

(p. 296), together with a numerical procedure for extending them to later times (Chapter 8). Desorption can be treated by the same equations and methods. Fig. 9.32 shows calculated sorption- and desorption-time curves for the diffusion coefficient of Fig. 9.32(a) and a skin one-fifth of the halfthickness of the sheet as before. Here we see that the curves intersect but the linear part has almost disappeared from the sorption curve. We can now see that this must always be so, for, as we have already noted, intersection of sorption and desorption curves only occurs when the region of high diffusion coefficient is in the lower half of the concentration range, which means that the diffusion coefficient is smal or zero only at very low concentrations. But it is clear from what we have said and from Fig. 9.32(b) that for relatively thin skins the amount absorbed by the sheet when the sorption-time curve ceases to be linear is roughly proportional to the height of the sharp front in the concentration-distance curve, i.e. to the concentration range over which D is smal or zero. It follows that, in general, when the sorption-time curve calculated for the model we have chosen has a long linear portion, desorption wil l be everywhere slower than sorption; conversely if the sorption and desorption curves intersect markedly no appreciable linear part will be observed in the sorption curve.

9,6.1. Composite cylinder

The effect of a skin on the uptake of dye by a cylindrical fibre has been studied (Crank and Godson 1947). The solutions obtained relate to a circular cylinder of infinite length and radius a immersed in a solution. Dye molecules diffuse into the cylinder and are deposited in capillaries of the cylinder.

The concentration of the dye in the solution is always uniform, while the cylinder is initially free of dye. The cylinder has a core of radius b, in which the diffusion coefficient is Db and for b < r < a the diffusion coefficient is Dfl. In any element of the cylinder the amount of dye S deposited in the capillaries and immobilized is related to C, the amount free to diffuse, by the relationship

S = RC\

(9.91)

where R is a constant which, in this example, is chosen so that in the final equilibrium state 90 per cent of the dye initially in the solution has entered the fibre. When the ratio of the volume of solution to that of the fibre is 25:1,R = 70-8. If we denote by Mt the amount of dye in the cylinder after time t, and M ^ the corresponding amount after infinite time, Fig. 9.33 shows MJM  ̂ as a function of log (Dbt/a2) for b = -^a. The several curves correspond to different values of Db/Da. The effect of changing the ratio DJDa is to displace the sorption curve parallel to the time axis, and this is accompanied by a slight change in the shape of the curves. Thus, when MJM  ̂ = 0-5, in Fig. 9.33,the abscissae of points on the curves for Db/Da = 2, 10, and 30 differ from the corresponding abscissa for Da = Db by the amounts 0-30,

VARIABL E DIFFUSION COEFFICIENT S

201

1-0

g. 0-6

I 0-4

0-2

00

1-2

1-6 20

-1-2 -0-8 -0-4 00 0-4 0-8

log( /V/a2)

FIG. 9.33. Sorption curves for  a composite cylinder  b = -^a. Numbers on curves are values of

0

1 2

3

4

5

6

FIG. 9.34. Sorption curves for  a composite cylinder, b = -^a. Numbers on curves are values of

202

SOME CALCULATE D RESULTS FOR

1-00, 145 respectively, i.e. by approximately log 2, log 10, log 30. When MJM  ̂ = 0-8, the abscissae differences are 0-18, 0-78, 1-18 respectively.

Thus the sorption curve for this composite cylinder almost coincides with the corresponding curve for a homogeneous cylinder having a diffusion coefficient Da throughout. The final stages proceed more rapidly in the composite cylinder, however, as is to be expected because of the greater diffusion coefficient in the core. For a thicker skin there is less difference in the shapes of the curves for composite and homogeneous cylinders (Crank and Godson 1947).

60

50

w 40 co

I 30

= 20

i 10

100

0-75

0-50

r/a

0-25

000

FIG . 9.35. Concentration distributio n in a composite cylinder, b = ^a\DJDa = 30. Numbers on curves are values of Dbt/a2.

solution for  homogeneous cylinder  of diffusion coefficient Dh.

In Fig. 9.34 some of the uptake curves are replotted against (Dbt/a2)*  to show that the presence of a skin does not necessarily produce a point of inflexion in the uptake curve plotted against the square root of time, as it does in the problems discussed in § 9.6. Fig. 9.35 shows the over-al concentration (S + C) in a composite cylinder as a function of the radial coordinate at three different times. There is a rapid fall in concentration within the skin and a discontinuity in concentration gradient at the boundary between the skin and the core where the diffusion coefficient changes discontinuously.

10

THE DEFINITION AND MEASUREMENT OF DIFFUSION COEFFICIENTS

10.1. Definitions

Q U A N T I T A T I V E measurements of the rate at which a diffusion proces occurs are usually expressed in terms of a diffusion coefficient. Before describing some methods of measurement, we shal examine the definition of the diffusion coefficients a littl e more carefully than in § 1.2 (p. 2). Confining attention to one dimension only, the diffusion coefficient is defined as the rate of transfer of the diffusing substance acros unit area of a section,divided by the space gradient of concentration at the section. Thus, if the rate of transfer is F, and C the concentration of diffusing substance, and if x denotes the space coordinate, then

F = -DdC/dx,

(10.1)

and (10.1) is a definition of the diffusion coefficient D. In using this definition in practice, it is necessary to specify carefully the section used and the units in which F, C, and x are measured. Only the simplest system of practical importance is considered, which is a two-component system, since it is not possible to set and observe a concentration gradient of a single substance in itself without introducing complicating features such as pressure gradients,etc. The diffusion of isotopes is best regarded as a special case of a twocomponent system.

10.2. A frame of reference when the total volume of the system remains constant

Consider the inter-diffusion of two liquids A and B in a closed vessel and assume that there is no overal change of volume of the two liquids on mixing. Two diffusion coefficients, DVA, DyB, one for each liquid, may be defined by the relationships

FA = -DvAdCA/dx,

(10.2)

FB= -DvBdCB/dx.

(10.3)

CA and CB are the concentrations of A and B respectively, each expressed in the usual way in any convenient unit of amount (e.g. gram or, in the case of simple molecular substances, gram mole) per unit over-al volume. FA and FB are the rates of transfer of A and B measured in the same units of amount

204

THE DEFINITIO N AND MEASUREMEN T

per unit time, acros a section which is defined by the condition that the total volume on either side of it remains constant as diffusion proceeds. In the particular case under consideration it is therefore fixed with respect to the containing vessel. The origin from which x is measured is such that the x-coordinate of the section is constant; x is measured in normal units of length, e.g. centimetres and the same unit of length is used in measuring the volume which appears in the definition of concentration. If the unit of time adopted is the second it follows that the units of DVA and DVB are each cm2 s~1.

These somewhat obvious statements are made here in full because it will be seen later in § 10.3 (p. 205) that other scales of length and alternative ways of measuring concentration are more suitable in some circumstances.

Let VA and VB denote the constant volumes of the unit amounts used in defining the concentrations of A and B. Thus if CA is expressed in grams per unit volume, VA is the volume of 1 g of A. In dilute solutions, where the volume changes in the range of concentration concerned can be considered negligible,VA and VB will be the partial specific or molar volumes. That of the solute may be very different from the specific volume in the pure state. The volume transfer of A per unit time acros unit area of the section defined is therefore

and that of B is

-DvBVBdCB/dx.

By definition of the section as one acros which there is no net transfer of volume we have immediately

DVAVA—- + DVBVB—- = 0.

(10.4)

The volume of A per unit over-al volume of solution is VACA and of B is VBCB, so that, since only molecules of A and B are present, we have

VACA+VBCB=19

(10.5)

which, following differentiation with respect to x, becomes VA—- + VB—- = 0.

(10.6)

In order that (10.4) and (10.6) shal both be satisfied it follows that}A = UBDVA  Dy9

(10.7)

or else that

VA = 0 or VB = 0.

(10.8)

If VA = 0 and VB # 0, it follows from (10.6) that dCB/dx = 0,

(10.9)

OF DIFFUSIO N COEFFICIENT S

205

and further reference is made to this case in § 10.6.4 (p. 234). In either case the behaviour of a two-component system, satisfying the condition of zero volume change on mixing, may be described in terms of a single diffusion coefficient, which may vary with composition. It is convenient to refer to it as the mutual diffusion coefficient denoted henceforth by Dv. This coefficient is familiar in the interdiffusion of gases (Jeans 1940). Its physical significance is considered later in § 10.4 (p. 209).

10.3. Alternativ e frames of reference

The definition of the volume-fixed section used in § 10.2 (p. 203) above is unambiguous only as long as the total volume of the diffusion system remains constant. If there is an over-al change of volume of the two components on mixing, the side of the section on which the volume is to remain constant must be chosen arbitrarily, and the diffusion coefficient becomes equally arbitrary. In such a case some alternative frame of reference must be used in defining the section acros which transfer of diffusing substance is to be measured. There are clearly several possibilities. Thus, for example, the total mass of the system will always be conserved even though volume is not, and a section can be defined consistently such that the mass of the system on either side of the section remains constant during diffusion.

Where a convention other than that of constant volume on either side is used in defining a section, the second-order differential equation describing diffusion may not take the standard form of (7.5). It is clearly convenient if it can be made to do so since the standard form has frequently been used as the starting-point in calculations of diffusion behaviour. This can always be arranged by departing from the orthodox linear scale, e.g. centimetres, for measurement of the spatial coordinate so far denoted by x, and by measuring concentration in a certain way. Let some modified scale of length be denoted by £, and consider two sections, fixed on the same convention, at {  and £, + d£.

The rate of entry of A into the volume enclosed between these sections is FA and that of departure is FA + (dFJd£)d£. The rate of accumulation is therefore

and this is always true independently of how FA and £ are measured. It can only be equated to (dCJdt) d£, however, when CA and £, are measured in certain consistent units. Thus, if the sections are fixed with respect to total mass, then £ must be measured so that equal increments of £ always include equal increments of total mass, and CA must be defined as the amount of A per unit total mass. Similarly, if the sections are fixed with respect to volume or mass of component B, equal increments of f must include equal increments of amount of B, and CA must be expressed as the amount of A per unit amount

206

THE DEFINITIO N AND MEASUREMEN T

of B. In general, for all values of t, and t, the element of unit length in terms of£, and of unit cross-sectional area, is that which contains an amount of A equal to the unit used in defining the concentration CA. When the quantities CA and £ satisfy this condition the usual relationship

follows at once, and by substituting for FA from the relationship

FA= -DdCJdi

(10.11)

we derive the familiar form of the diffusion equation

dt « , - « •

(10-12)

It is convenient that £ should have the dimension of length and D the usual dimensions of (length)2(time)~~ *. This can be arranged without interfering with the generality or simplicity of (10.12), by multiplying the mass of component B (or the total mass of A and B together if this is the reference system being used) by an arbitary constant specific volume. The volume represented by the product of a mass of B, for example, and this arbitrary specific volume will be referred to for convenience as the basic volume of that mass of B.

The concentration of A was defined above as the amount of A per unit amount of B. We now redefine the concentration of A as the amount per unit basic volume of B, and unit £ to contain unit basic volume of B per unit area. A convenient arbitrary specific volume is that of the pure component B, so that the basic volume of a certain mass of B is the volume that mass of B would occupy in the pure state.

The same arbitrary specific volume is used for concentrations expressed in the original definition per unit mass of A and B together, i.e. the basic volume of a mass of A and B together is obtained by multiplying the mass by the same arbitrary specific volume. This is true also for deriving the basic volume of A alone, so that the basic volume has a simple physical significance only in the case of the basic volume of B. Nevertheless, the use of this particular basic volume has the convenience that all the concentrations measured in the different frames of reference tend to the same value in dilute solutions.

Of course, concentration is frequently expressed in a number of different ways and so the symbol CA is retained, but the appropriate index V, B, or M as superscript is added, so that the concentration of A is written CVA,CBA,or CA according as the amount of A is contained in unit volume of solution,or in unit basic volume of B or in unit basic volume of total mass. According as unit f contains, per unit area, unit basic volume of B or of A and B together,

OF DIFFUSION COEFFICIENTS

207

the symbol £B or £M is used. The diffusion coefficients D 9̂D^,D  ̂ also carry an index to indicate the frame of reference to which they refer. The arbitrary specific volume may be denoted by VB9 and then £B and £M are defined formally by the respective relationships

d£B=VBCvBdi,

(10.13)

dx.

(10.14)

10.3.1. Sections fixed with respect to total mass and mass of one component

It was found in § 10.2 (p. 203) that the behaviour of a two-component system satisfying the condition of zero volume change on mixing can be represented in terms of a single diffusion coefficient Dv. A similar result follows readily for a system in which volume changes occur, provided the diffusion coefficients are defined with respect to a mass-fixed section. Thus the equation defining such a section is

^

§5- = 0,

(10.15)

and the definitions of CA and CB lead immediately to the equation Cy + Cjf =1/Kg.

(10.16)On differentiating (10.16) with respect to £M and comparing with (10.15)we find

D% = D%.

(10.17)

If a section fixed with respect to one component, say B, is used, then clearly DB = 0 and only the coefficient DBA is needed to describe the diffusion behaviour. Thus the statement that the diffusion behaviour of a two-component system can be described in terms of a single diffusion coefficient, is valid whether there is a change of volume of the whole system or not, provided the appropriate frame of reference is used in defining the diffusion coefficient. Frames of reference could be so chosen that the two coefficients are not identical and neither is zero, but they would be related through some function of the partial volumes and would not be independent measures of two separate diffusion processes. The possibility of measuring the diffusion of the two molecular species independently is discussed in £ 10.4 (p. 211).

10.3.2. Relations between the diffusion coefficients D^,DA9 DBA

The rate of transfer of A through a Infixed section is greater than that through a total-mass-fixed section by an amount given by the concentration of A per unit mass of B multiplied by the flux of B acros the mass-fixed section. Thus the flux of A acros a infixed section in the direction of {

208

THE DEFINITION AND MEASUREMENT

increasing is

as ~

CMy0 ft* >

v * — ,

using (10.16).

But the rate of transfer acros a infixed section is — DA dCA/d£B so that we have

DB = ——— —- —^-

(1019)

From the definitions of CA and CA it is easy to show that

—& = (V°BC^)2.

(10.20)

Also since

dU = V°B(CVA + CVB) dx9 d£B = V°BCVB dx9

(10.21)

we have

§1 = V%C»,

(10.22)

so that finally, by substituting (10.22) and (10.20) in (10.19), we find

DBA = DM(V°BC% ) 2 ,

(10.23)

since re-arrangement of the partial derivatives in (10.19) is permissible. For a system in which there is zero volume change on mixing, so that VA and VB are constant, the relation between DA and Dv can be similarly established.

Thus the flux of A acros a JB-fixed section in the direction of £, increasing is

^ ^ ^ = - - ^ ^ ,

(10.24)

C dx

VC dxVBCB

using (10.5) and (10.6). But the rate of transfer of A acros a B-fixed section is-DBdCA/d£B, so that we have

VBCVB dx dCBA

From the definition of CVA and CBA it follows that

dC

A  A

y

V ) 2

= (VBCVB)2,

(10.26)

and from the second of (10.21) we have immediately^ = VBCVB,

(10.27)

OF DIFFUSIO N COEFFICIENT S

209

so that on substituting (10.26) and (10.27) in (10.25) we find

DBA = DV{VBCVB)2 = DF(volume fraction of B)2.

(10.28)Since (10.28) applies only when VB is constant, and therefore VB = VB,comparison of (10.28) and (10.23) shows that when there is no over-al volume change accompanying diffusion

DM = DV(CVB/C^)2 = Dv (basic total volume/true total volume)2. (10.29)

10.4. Intrinsi c diffusion coefficients

We saw in § 10.3.1 that any two-component system can be described by a single or mutual diffusion coefficient, which may be a function of composition but will be the same function for both components. In the simplest case,where the molecules of the components A and B are identical in mass and size, the rates of transfer of A and B due to random motion acros a volumefixed section may reasonably be expected to be equal and opposite. In general, however, differences of mass and size of A and B molecules result in the transfer of A by random motions being greater or less than that of B.

Consequently, a hydrostatic pressure tends to be built up in the region of the solution which contributes least to the volume rate of transfer. This pressure is relieved by a compensating bulk-flow of A and B together, that is of the whole solution (Meyer 1899, Jeans 1940, Hartley 1946). This existence of bulk flow can be demonstrated in the case of gases, when diffusion occurs across a porous plate which offers considerable viscous resistance. In this case, an increased pressure is found to arise in that part of the vessel occupied initiall y by the slower diffusing component. It has been demonstrated in metal systems (Darken 1948) and in polymer solvent systems (Robinson 1946) by the insertion of marker particles, t In the latter case, the large polymer molecules will diffuse far more slowly, as a result of random motions, than the smal solvent molecules. Thus the polymer movement measured by the mutual coefficient is almost entirely a bulk-flow.

The over-al rate of transfer, say of component A, acros a volume-fixed section may be expressed as the combined effect of bulk-flow and true diffusion resulting from the random motion of non-uniformly distributed A molecules. From the point of view of interpreting diffusion coefficients in terms of molecular motions, the mutual diffusion coefficient Dv thus appears to be unnecessarily complicated by the presence of the bulk-flow. It is desirable to define new diffusion coefficients, Q)A and 3)B, in terms of the rate of transfer of A and B, respectively, acros a section fixed so that no bulk-flow occurs through it. Such a section may be impossible to determine in practice,except in special conditions mentioned below. It is fixed in a different way

t The marker  movement is often referred to as the Kirkendal l effect, since it was first  observed in metals by Kirkendall , E. O. (1942).

210

THE DEFINITIO N AND MEASUREMEN T

from any of the other sections previously dealt with, and it must follow the bulk-flow although this flow is not normally directly observable. These new diffusion coefficients will be referred to as 'intrinsic diffusion coefficients'.

When the partial volumes are constant they are related to the mutual diffusion coefficient in the following way.

On one side of a section fixed so that no bulk-flow occurs through it, there is a rate of accumulation of total volume of solution, which may be denoted by (/>, where

dCv

dCv^ V®^-'

(10.30)

As thus defined, (j>  is actually the rate of increase of volume on the side of smaller x, and this must be equal to the rate of transfer of total volume by bulk-flow acros a volume-fixed section. Such a bulk-flow involves a rate of transfer of A of <j)CvA, so that, equating two expressions for the net rate of transfer of A acros the volume-fixed section, we find

On substituting for <\>  from (10.30) and using (10.6) we have finally

Dv = VACyA(@B-®A) + @A.

(10.32)

If the molal volumes vary with composition, the coefficient Dv has no physical significance, but 2A, Q)B can still be defined in terms of the rates of transfer of A and B respectively acros a section which moves so that there is no bulk-flow of A and B together, through it. It is convenient in this case to relate the intrinsic diffusion coefficients to DBA. Since the net rate of transfer of B through a B-fixed section is, by definition, zero, it follows that the contributions to the transfer of B resulting from the over-al bulk-flow and from the true diffusion of B relative to the bulk-flow, must be equal and opposite.

The rate of transfer of B by true diffusion relative to the bulk-flow is

-9BdCvB/dx,

in the direction of x increasing and hence the volume transfer of the whole solution accompanying bulk-flow with respect to the B-fixed section is given by

cvB dx'

in the direction of x increasing. This produces a rate of transfer of A through the B-fixed section of

OF DIFFUSION COEFFICIENTS

211

due to the bulk-flow. This is to be combined with the rate of transfer of A relative to the bulk-flow which is given by

-®AdcvA/dx

to give the net rate of transfer of A acros a B-fixed section, which is simply

-DBAdC*/dZBThus we have the equation

_£)* d = - Q ) A d + _£®B *

(10.33)

OQB

OX C B vX

When the molal volumes are not constant, the relationship

vAcA+vBcB = i

still holds, but the differentiated form (10.6J is to be replaced by

Since

it follows immediately from (10.27), (10.33), and (10.34) that

CV VB+cvBdvB/dCvB]'

( }

This reduces to (10.32) when VA and VB are constant.

It is clear from (10.32) or (10.35) that the values of <2)A and Q)B cannot be deduced separately, unless some information other than Dv or DBA is available.

One possibility is to use an observation of the bulk-flow, as suggested by

Darken (1948) and by Hartley and Crank (1949). Sometimes, e.g. in solventpolymer systems, the intrinsic diffusion for one component, e.g. the polymer,

is so much smaller than for the other that it can be assumed to be zero. With

the assumption that Q)B = 0 we have from (10.32)

g>A = Dv/(l - VACVA) = DV/(VBCVB) = D7(volume fraction of B\ (10.36)

which allows the intrinsic diffusion coefficient of component A and its dependence on concentration to be deduced from observations of Dv. The ideas discussed above in §§ 10.1-10.4 have been the subjects of papers by

Darken (1948), Hartley and Crank (1949), Kuusinen (1935), Lamm (1943)

and Pattle, Smith, and Hil l (1967).

212

THE DEFINITIO N AND MEASUREMEN T

10.5. 'Self'-diffusion coefficients

By using radioactively-labelled molecules it is possible to observe the rate of diffusion of one component in a two-component system of uniform chemical composition. Since what is involved is an interchange of labelled and unlabelied molecules which are otherwise identical there is no bulk-flow and the true mobility of the labelled molecules with respect to stationary solution is measured. Nevertheless, the diffusion coefficient so deduced will in general differ from the corresponding intrinsic diffusion coefficient for the same chemical composition. Johnson (1942) has found this to be so in metal systems. Seitz (1948), regarding the diffusion proces as a jumping of molecules from one equilibrium position to another, accounts for the difference on the basis that when there is a gradient of chemical composition the frequency with which a molecule jumps to the right is not the same as that with which it jumps to the left. For the labelled molecules, however, the two frequencies are identical. Darken (1948) and Prager (1953) have related the diffusion coefficient measured by an experiment using radioactive molecules to the intrinsic diffusion coefficient in terms of the thermodynamic properties of the system. Their result can be anticipated as follows.

Consider a two-component system comprising molecules A and B and let the gradient of concentration CA of A be maintained in an equilibrium condition by the application of a force FA per g mol of A in the direction of increasing x. This is purely a hypothetical operation but it can be realized in the case of large molecules, much different in density from the solvent, by a centrifugal field. The generalized form of the condition for this thermodynamic equilibrium is

FA = dfjijdx,

(10.37)

where \iA is the chemical potential of component A. The rate of transfer of A due to the force FA is

r r r a,,

(10.38)oAr)

OAY\ 8x '

where aArj  is a resistance coefficient. But in the equilibrium condition (10.38)is also the rate of transfer by diffusion relative to a section through which there is no bulk-flow and so we have

dx (TArj  dCA dx

and hence

_ C

A ~ °A1£-

(10.40)

OF DIFFUSIO N COEFFICIENT S

213

On applying the same treatment to the labelled molecules in a system of uniform chemical composition we have

.

" £ S ,

(10.41,

ox C*  ox

because of the ideality of the system, where asterisks denote properties of labelled molecules. Instead of (10.40), therefore, we obtain

R T

(10.42)

and finally

QA = @*CA(dfiA/dCA)/RT,

(10.43)

if we assume the resistance coefficient OAY\ to depend only on chemical composition. Carman and Stein (1956) used these concepts in discussing their measurements of self-diffusion coefficients in mixtures of ethyl iodide and n-butyliodide.

Pattle et al. (1967) questioned the validity of this assumption. It implies that the mobility of a few tracer molecules moving relative to all the others is the same as the corresponding mobility in mutual diffusion where all the molecules of one kind are moving in one direction and the rest in the other.

They propose as an alternative a 'one-process' theory which postulates no bulk-flow but instead introduces 'enhancement factors' relating mobilities in mutual and tracer diffusion. The factors are chosen so that the theory fits the experimentally observed values of the different diffusion coefficients and the associated thermodynamic data. Patel et al. agree that the 'two-process'theory incorporating bulk-flow can be modified by the insertion of similar arbitrary parameters. The subject needs further careful experimental investigation of the kind carried out by Pattle et al. in the rubber-benzene system.

Kir k wood, Baldwin, Dunlop, Gosting, and Kegeles (1960) discussed the various frames of reference described in § 10.3 (p. 205) with reference to the transport equations of irreversible thermodynamics. They were particularly concerned to test Onsager's reciprocal relations and to measure diffusion coefficients in systems in which changes of volume occur on mixing. In this connection Fujita and Gosting (1956) presented mathematical solutions of Onsager's flow equations for diffusion in a three-component system with interacting flows. They developed a general procedure for calculating the four diffusion coefficients from experimental data.

Bearman (1961) examined the absolute reaction rate theory (Glasstone,Laidler, and Eyring (1941) and the equations of Hartley and Crank (1949)and of Gordon (1937) from the viewpoint of statistical thermodynamics.

He found the different approaches basically equivalent. In his criticism of the

214

THE DEFINITION AND MEASUREMENT

idea of intrinsic diffusion coefficients Bearman seems to confuse the massfixed frame of reference (§ 10.3.1, p. 207) with that moving with the bulk-flow(§ 10.4, p. 209). Partly for this reason the term 4bulk-flow' may be preferable to 4mass-flow' as originally used by Hartley and Crank (1949). Wright (1972)in a series of papers dealing with gaseous diffusion at 'strictly uniform pressure' obtains expressions similar in algebraic form to those of this section. He sees this as quite natural since the two discussions are expressing the same basic concepts in different terms.

Tyrrell (1971) considers that all the phenomenological descriptions of diffusion based on Fick's original concepts are deceptively too simple.

He discusses critically the problems of the definition of diffusion coefficients and suggests that understanding of diffusion processes is most likely to advance through the application of non-equilibrium thermodynamics and through mechanical analogies involving frictional coefficients (Mill s 1963;Tyrell 1963).

10.6. Methods of measurement

Crank and Park (1968) reviewed the more useful experimental techniques for measuring diffusion coefficients and their concentration dependence. In this section the emphasis is on the associated mathematical analysis.

Most of the earlier methods assumed constant diffusion coefficients.

When such methods are applied to systems in which this is not true, a mean value is obtained. Both steady-state and transient methods are used, sometimes in combination, as in the time-lag method of §4.3.3 (p. 51). Various methods based on the analysis of concentration-distance curves are reviewed by Alexander and Johnson (1949, Chapter X). A variation is to observe the over-al rate of uptake or loss of diffusing substance by a specimen of known size and shape, and to compare this with the calculated rate of uptake expressed as a function of Dt. In some cases, special tables have been constructed to facilitate the calculations. Stefan's tables (1879), to which reference was made earlier in § 4.3.8 (p. 63) refer to the diffusion of solute from a column of solution into a column of water. They give the amount of diffusing substance contained in successive layers of equal height. These tables and others of a similar nature are reproduced and discussed by Jost (1952).

In all these methods, the difficulties lie in the experimental techniques rather than in the subsequent mathematics. Adequate accounts are already available (Barrer 1951; Jost 1952). It suffices to say here, following the discussion of the alternative definitions of diffusion coefficients, that in the early measurements it is usually assumed that the total volume of the system remains constant as diffusion proceeds and so the mutual diffusion coefficient Dv is measured. A notable exception is that of Clack (1916; 1921), who introduced a correction for mass-flow and obtained in effect the coefficient DBA of solute

OF DIFFUSION COEFFICIENTS

215

with respect to stationary solvent. A number of examples are discussed in more detail by Hartley and Crank (1949).

This is a convenient point at which to refer to a method of measurement suggested by Taylor (1953, 1954) based on observations of the dispersion of soluble matter in solvent flowing slowly through a small-bore tube. The distribution of concentration is found to be centred on a point which moves with the mean speed of flow U and is symmetrical in spite of the asymmetry of flow. Taylor (1953) shows that the distribution is determined by a longitudinal diffusion coefficient k which is related to the molecular diffusion coefficient D by the relation

. a2U2

where I/, the mean speed of flow, is defined as \u0, where u0 is the maximum velocity on the axis and a is the radius of the tube.

Two useful experimental conditions are as follows.

(i) Material of mass M concentrated at x = 0 when time t = 0. The solution for this is

C = \Ma-2n-\kty± exp(-x?/4/cr),

where x1 = x — \uot.

(ii) Material of constant concentration Co is allowed to enter the tube at a uniform rate at x = 0, starting at t = 0. Initially the tube is filled with solvent only (C = 0). The solution for this case is

C/Co = i + i e r f j _ ^ } , X ] < o,

In either case /c, and hence D, may be deduced by comparing the appropriate mathematical solution with an observed concentration distribution. The mathematical analysis rests on the assumption that radial differences in concentration are smoothed out quickly by molecular diffusion compared with the time necessary for appreciable effects to appear owing to convective transport. Also longitudinal diffusion is neglected.

In a second paper, Taylor (1954) suggested necessary conditions to be

a D

where L is the length of tube over which appreciable changes in concentration occur. In later papers Philip (1963) criticizes some aspects of this work and

216

THE DEFINITIO N AND MEASUREMEN T

a similar analysis by Aris (1956), and suggests a more generalized approach.

Carrier (1956) deals with the effluent from a tube when the intake is oscillatory.

This is a method which may be of particular interest in physiological systems(Philip 19696).

Two more recent methods rely on less familiar mathematical solutions.

Pasternak, Schimscheimer, and Heller (1970) described a 'dynamic', isobaric permeation experiment in which atmospheric pressure is maintained on both sides of a membrane. One face is in contact with the penetrant and a carrier gas, flowing at a constant rate past the other face, sweeps away the penetrant which diffuses through the membrane to a recording system. Thus the permeation rate is observed continuously. The mathematical statement of an experiment is

C = 0, x = /, t  ̂ 0,

(10.44)

C = Q, x = 0, r = 0,

(10.45)

C = C{, x = 0, t > 0,

(10.46)

C = Ci(/-x)//, 0 ^ x ^ / , r = 0,

(10.47)

C = Cf(/-x)/7, O^x^l,

t = oo.

(10.48)

Thus there is a change from one steady state to another with the concentration at x = / always zero. Pasternak et al. use Holstein's solution (4.27)modified to allow for their initial condition (10.47). It is

F -

l 14 D ( Cf - Q

2 |

^ ) | e x p { -(2n + \)2l2l(ADt)} (10.49)|

where F is the flux at x = /. Taking the first term of the series in (10.49) we have

^) 2exp{- /2/ (4Df) } ,

(10.50)

where AF^ = D(C{ — C)ll is the change in flux from the start to the finish of the experiment. They then write (10.50) in the form

AF/AF^ = (4/TT±)X e~*\

(10.51)

where X2 = l2/(4Dt). Then D is easily derived from a comparison of the master plot of AF/AF^ from (10.51) with the corresponding experimental plot against t.

Evnochides and Henley (1970) used a frequency-response technique to measure the diffusion coefficient and the solubility simultaneously. A

OF DIFFUSION COEFFICIENTS

217

polymer sample is exposed to a permeating gas whose pressure is varied sinusoidally. The phase angle and amplitude of the weight changes are measured as a function of the frequency of the sinusoidal pressure change.

Initially , the main pressure of the gas is Pm and the concentration inside the film is uniform and equal to KPm. At x = ±L  we have the concentration

Cs = KP = K{Pm + AP sin (cot + e)}

where the amplitude AP = ^Pi-P0)- Defining Cm = KPm and Co = KP0 and

we require solutions of

subject to

y = sin

= (C-CJ/(Cm-C0)

dy/dt = D d2y/dx2

e), t > 0, x = ±L.

The full solution is given by Carslaw and Jaeger (1959).

It is

y = Ay sin (art+ £ + 0)

co cossx cos

e X P |

4L2

At large times a periodic steady state is reached y = Ay sin (cot + e + 0),where

sin e}

(10.52)

(10.53)

(10.54)(10.55)

(10.56)

(10.57)

Defining M r, as the mass of gas in the film at time t we have

M, = 2Ap [ Cdx,

(10.60)

Jo

where A and p are the area and density of the film. Taking Mm = WCm and

218

THE DEFINITION AND MEASUREMENT

Mo = WC0, where W is the mas of the film, eqns (10.52) and (10.57) with appropriate substitutions lead after integration of (10.60) to

Mt-Mm = A sin (cot+ e + \l/\

(10.61)

where

J(2)KWAP(sin2 2CL + smh 2CL)2CL(co2CL + h2CL) '

l

fsin2(L-sinh2£L]

, i n , . ,

= tan W .

. u ^ r >.

10.63

[sin2£L + sinh2CLJ

Evnochides and Henley conclude that a single experiment in which both A and \j/ are measured suffices to determine both K and (. Both occur in(10.62) but the phase angle is independent of the solubility.

10.6.1. Analysis of steady-state flow

In a series of papers Ash, Barrer, and others have studied extensively the theory of steady-state flow through membranes. From measurements of the flux through the membrane they have been concerned to extract information about the concentration profile, the amount of diffusant within the membrane,and the dependence of the diffusion coefficient on concentration and the positional coordinate.

Ash and Barrer (1971) have developed a general theory of one-dimensional diffusion in slabs, hollow cylinders, and spherical shells when D is a separable function of concentration and the space coordinate. For v-dimensional diffusion, where v = 1 corresponds to flow through unit area of a slab, v = 2 through a cylinder of unit length, and v = 3 through a spherical shell, the general equation can be written

and in the steady state dC/dt = 0. At the boundaries Rx and R2(R2 > &i)it is assumed that

C(Rl9t) = Cx and C(R2,t) = C2,

(10.65)where Cx and C2 are constant and Cx > C2. Thus flow occurs in the direction of r increasing and is termed 'forward flow'. When Cl and C2 are interchanged we have 'reverse' flow.

Take D to be given by

D = D04>[C)f(r\

(10.66)where </>(0) = 1, f(R{) = 1. The steady-state flow in the direction of r

OF DIFFUSION COEFFICIENTS

219

increasing is

F= -(Dvr^lDo<i){C)f{r)dCldr

(10.67a)

where

dr

and col = 1, co2 = 2n, w3 = An. The expression (10.67b) for F follows from(10.67a) by integrating with respect to r, and remembering that F is independent of r. We note in passing that \F\ is independent of the direction of flow for the type of D assumed in (10.66) (Hartley 1948). Integration of (10.67a)with respect to r from R1to r yields

NJR^r) CCl

CCi

————— <p{u)du= <p(u)du.

(10.68)

NAR\->R2) Jc2

Jc(r)

If 0(C) and f(r) are known, the concentration profile through the membrane,in principle, may be determined from (10.68). Interchanging Cl and C2 in(10.68) gives the corresponding relationship for C(r) in 'reverse' flow. By adding the two relationships we obtain

4>{u)du = 0.

(10.69)

)

In the particular case of constant D, (10.69) becomes

so that the 'reverse' distribution is readily found if the 'forward' distribution is known. It is likely, however, that in practice 4>(C) and f(r) will not be known in advance. Ash and Barrer (1971) propose the following procedure for determining C(r) in such cases.

We keep C2 and R{ constant and make a series of measurements of F = F(C1, R2) for different values of Cl and R2. From (10.68) we have

Nv(Rj, r) = J£ 4>{u) d u- jcc[r) 4>(u) du = F{CX, R2)-F(C(r\ R2)

NV{R19R2)

2̂4>(u)du

F(Cl9R2)

by using (10.67b). We must keep in mind that C(r) is the concentration at the point r, R^  ̂< r < R2 in an experiment for which the surfaces Rx and R2 are at concentrations Cx and C2 respectively, but that F{C(r\ R2) denotes the flow that would be observed in an experiment for which the concentration

220

THE DEFINITIO N AND MEASUREMEN T

at the surface R^  ̂ were C{r). Similarly, F(C1, r) signifies the flow that would be observed through a membrane with surfaces at Rx and r kept at concentrations Cx and C2 respectively. With this nomenclature

fCl

F(C!, r) = covD0 (j)(u) du/Nv (R l, r),

Jc ,

and F(CX, K2) is given by (10.67b).

It follows that

Nv(Rl9r)

F{Cl9R2)

F(Cl9R2)-F(C(r)9R2)

Nv{Rl9R2)

F(Cl9r)

F(Cl9R2)

'

( 1° ' 7 0 )

We now draw two master plots based on experimental data: the first of F against C1 for constant C2, Rx and R2; the second of F against R2 for C^Ci a nd ^1 held constant (Figs. 10.1(a) and 10.1(b)).

(a)

F{C(r),R2)

-.

(b)

C(r)

FIG . 10.1.

We select a value of r in the range Rx < r < R2. From the plot in Fig.

10.1(b) we read the values of FiC^r) and F(Cl9R2) and find their ratio.

The value of F(C(r), R2) follows from (10.70) and from Fig. 10.1(a) the value of C(r) for the selected value of r. Proceeding in this way for various selected

values of r the profile of C(r) against r is determined. To deal with reverse

flow we write

f l <Ku)du+ f l <Ku)du = f l (j)(u)du

J C(r)

J C(r)

J C2

OF D IFFUSIO N COEFFICIENT S

221

by using (10.69). Hence

F(C(r),R2)-F(C(r),R2) = F(C,,R2).

(10.71)

This relation may be substituted into (10.70) to obtain N^R^r)

F(C1;JR2) F(C(r), R2)F(CltR2)'

(10.72)

The master plots allow C(r) to be found as a function of r. The amount of diffusant in the membrane is

M = ojy-lC(r)dr.

(10.73)

Once C(r) has been determined as a function of r the integration of (10.73)can be performed numerically or graphically. The procedures for finding C(r) and M require no knowledge of 0(C) or of /(r). These functions can be obtained, however, at least in theory, from the master plots.

For C2 and Rx held constant (10.67b) may be written

F(Cl9R2)NJLRi9R2) = cOvDoj '<t>(u)du.

Partial differentiation with respect to R2 and Cx respectively gives

—NV(RX , ,R2) = 0,

(10.74)

(10.75)

and

dF(Cl,R2)  ̂a)vD0<t>(C)

dC,

N , ( * i , « 2) '

On combining (10.74) and (10.75) and re-arranging we see that

= ^ T  ̂

dF(Cl,R2)/8R2-

All the quantities needed to find the functional dependence of D can be obtained graphically or numerically from the master plots in Figs. 10.1(a)and 10.1(b).

The particular cases of D = D0(f)(C) or D = Dof(r) only can be extracted from the equations developed above. They are treated separately by Ash and Barrer (1971), who give some additional relationships.

222

THE DEFINITION AND MEASUREMENT

10.6.2. Time-lag methods

In §4.3.3 (p. 51) the approach to steady-state flow through a membrane was analysed and the time-lag L related to the diffusion coefficient by (4.26)for cases of constant D.

Paul and Dibenedetto (1965) have shown how the time-lag technique can be extended to the situation in which the pressure or concentration on the'downstream' side of the membrane increase with time, as the diffusant emerges into a limited volume.

Frisch (1957) has obtained expressions for the time lag which apply also to systems with concentration dependent diffusion coefficients without explicitly solving the diffusion equation. He considers C = Co, x = 0,C = 0, x = U > 0; C - 0, 0 < x < /, t = 0.

We denote the non-steady rate of flow through the surface x = / by F(t),where

F(t)= - I D C ^

\ dx x=l

The total flow through this surface in time t is given by

(10.77)

Q(t) = f

Jo

F(t)dt.

(10.78)

To find Q{t) we first integrate both sides of the diffusion eqn (7.5) over x from x to / and obtain

Integrating again over x from 0 to / and re-arranging we obtain

Finally, by integrating over t from 0 to t and changing the order of integration we find

Q(t) = -U\ D(u)du-\ C(z,t)dzdx>.

(10.79)

' [ Jo

JoJx

)

The asymptote Qs(t) to Q(t) is

QJLt) = F(t-L)

(10.80)since its gradient is the steady-state flow rate F and the time lag L is its

OF DIFFUSION COEFFICIENTS

223

intercept on the t-axis. Comparison of (10.79) with (10.80) using the appropriate form of (10.67b) shows that

where Cs(x) is the concentration distribution through the membrane in the steady state. Integration by parts leads to the form

r l

/cCo

L=\  xCs(x)dx/ D(u)du.

(10.82)

Jo

/ Jo

The appropriate form of (10.68) gives

f ° D(u) du = y f ° D{u) &u.

(10.83)

J cs

' Jo

In principle, Cs(x) can be derived from (10.83) if D(u) is known or (10.82)can be rewritten as

i2fS°wD(w){JS°P(u)du}dw

L ~ WmW •

( }

Provided the functional form of D(C) = Dc is known, the measurement of L for various values of Co allows the constant parameters of D, and hence D as a function of C, to be determined.

It can be shown (Frisch 1958; Pollack and Frisch 1959) that when In Jo ^(M) du is a convex function of C, the time lag is governed by the inequality

1 ^

Barrie and Machin (1967) stres that the relative variation of L with C is always considerably smaller than that of D(C) with C. This is particularly true when D(C) decreases with C increasing. They show graphs of L(C) and D(C) illustrating these general statements for various concentration dependent diffusion coefficients.

Ash, Baker, and Barrer (1968) have suggested two extensions of (10.82)and (10.84) which may be more convenient in practice when D is a function of concentration only. The first is based on the appropriate special case of(10.76) which, in conjunction with the master plots of Figs. 10.1(a) and (b),allows the concentration distribution to be deduced from measurements of

224

THE DEFINITIO N AND MEASUREMEN T

the steady-state flow F. We can determine Cs(x) in (10.82) from the relation x

F(C0)-F{Cs(x)}/ F{C0)

Furthermore, from (10.85a) we have

- /

(10.85a)

dF{Cs(x)},

(10.85b)

and by substituting (10.85a) and (10.85b) in (10.82) we obtain

, = l$FoiCo) CF[F(C0)-F{Cs(x)}]  dF{Cs(x)}

{F(C0)}>

where CF = C[F{Cs(x)}]  and is the value of the concentration which corresponds to F{Cs(x)} on the appropriate master plot. Frisch (1957) illustrates his method for the cases of D constant and D(C) = D0(l + /JC), and also considers more general boundary conditions. Barrer and Ferguson (1958) and also Meares (1958, 1965) quote the expression for L given in (10.86) below for an exponential dependence of D on C.

Frisch (1958) showed that from measurements of L and the steady-state flow F at different pressures, both the parameters in the D(C) functional relationship and the solubility coefficient can be found without resource to a separate measurement of solubility.

Meares (1965) carried out a single permeation experiment for a system in which the diffusion coefficient was known to have the form

One face of the membrane is in contact with vapour at a constant pressure Px.

Frisch's expression (10.84) leads in this case to the relationship

4D0L 4e "c ' - l +e2 ' i C ' ( 2 /?C1-3)

=

The limiting slope as t approaches zero, of the graph expressing Holstein's solution (4.27a) gives a value for Do, since at this time the concentration is still very smal in the greater part of the sheet. The steady-state rate of permeation through a sheet of area A into a volume V in which the pressure is p(t) is given by

^^ jV-ac^^-L,. ,10*7,

When Do has been determined, f}C1 follows from (10.86) and the individual values of jS and Cx are calculated from (10.87).

OF DIFFUSION COEFFICIENTS

225

If Henry's law is obeyed the solubility coefficient S is also obtained from C1 and the pressure on the ingoing face. Meares (1965) found the method successful in three quite different systems.

Frisch (1959) has generalized his early results to include cases in which D may depend explicitly not only on concentration but also on time and x.

He considers the v-dimensional, diffusion problem defined by

dC' *

A " ' "-'*""  ~ " = 1 , 2 , 3,

(10.88)

dty9'

r^'dr]

dr

in R1 < r < R2, t > 0, where

0 = Cj or 0(Cj, Kj , 0 = 0i(O 0 = -̂2 Or 0(^-2 » ^2 »0 = ^2(0 C(r,0) = Co(r).

(10.88a)

Here 0 is a 'potential of diffusion' defined in general by F = —D grad C = — grad 0,and for spherically symmetric systems by

F = -DdC/dr = -dcfr/dr.

(10.89)

Integration of (10.89) gives

4>i(O-02W= I F(r,t)dr9

in general and

2

when D = D{C, t).

The case, v = 1, corresponds to one-dimensional diffusion through a flat membrane of thicknes /, v = 2 to radial diffusion through infinite concentric cylinders and v = 3 to radial diffusion between concentric spheres.

We assume that as t -> oo a steady state is attained and 0 -> 0S, the solution of

dr

with

0^/^) = 0sj = lim <

r-> 00

r-»oo

226

THE DEFINITIO N AND MEASUREMEN T

Following the method outlined above Frisch arrives at the relation L = ^R'r

(10.90)

We note that the expression (10.90) is generally true for all equations of flow

which conform to the conservation of mass condition. Ash et al. (1968) stres

this point and quote expressions analogous to (10.90) for the time lag measured

at any plane in a membrane. When D = D(C\ a function of concentration

only, the second term on the right side of (10.90) vanishes identically. This follows since for D = D{C\ <f>  is independent of t and hence ^( f ) = 0S1?(j)2(t) = 0S2. The first term on the right side then reduces for the particular

case v = 1 and C2 = Co = 0 to (10.82) and hence to (10.84).

Thus in general L(/) can be written as the sum of a 'Fickian' time lag LF(/)and a 'non-Fickian' or 'time-dependent' contribution LT which is independent of /. Frisch (1962a) wrote

where a(Cj) is independent of /. Thus, if time lags can be measured for films of different thicknesses but which are otherwise of identical physical properties a plot of L(/) against I2 should be a straight line of ordinate intercept LT,while the slope gives a value of DiC ,̂ oo) obtained from steady-state measurements. So far, we have considered only the time lag measured at the 'downstream' boundary, e.g. at x = /, for the plane membrane. Frisch (19626)used his technique to obtain expressions for L(x) and in particular L(0)measured at the 'upstream' face of the membrane. The 'upstream-downstream' difference is shown to be

AL = L(/)-L(0) = (1/F) f {C s(x)-C0}  dx.

(10.91)

Jo

Furthermore, we may refer to a time lag measured by an experiment in which Co = C2 as an 'absorption time lag' La. The condition Co = Cl9 leading to a 'desorption time lag' Ld, is also possible. On inserting this value for Co in the Fickian part of (10.90) and taking v = 1 it follows that the absorption-desorption time-lag difference for a Fickian membrane is given by

SL(l) = SL = Ld-Ld = liC^-C^jlF.

(10.92)

The double difference b AL is defined as

3 AL = AL a - AL d = l(C1 - C2)/F.

(10.93)

OF DIFFUSION COEFFICIENTS

227

Barrer (1969) gives a list of time lags and related quantities. Petropoulos and Roussis (1967) made extensive studies of the properties of these time lags and their differences in attempts to detect and characterize different types of non-Fickian behaviour. They distinguish between systems in which the diffusion and solubility parameters are time-dependent or distance-dependent. They introduce the gradient of chemical potential into the diffusion equation which becomes

8 t - a . . , - 7 ~a . . i - , . - r , ,

( 1 0 . 9 4)

with boundary conditions a ( 0 , f) = a o ,

a(l9t) = a l 9

a(x,0) = a l 9

(10.95)and where DT is the 'thermodynamic diffusion coefficient', and PT the corresponding permeability. We assume the a09 a{, ax to be constants. Comparison of (10.94) with (7.5) shows that

D = DTSda/dC.

(10.96)By applying the method of Frisch to (10.94) we find that LT, the non-Fickian time-lag increment, is given by

LT = dr {PT{a, oo)-PT(a, 0}  d a/ PT(a, oo)da. (10.97)

Jo

J ai

I "ai

Petropoulos and Roussis introduced expressions for S(a, t) and DT(a, t) which they thought to be appropriate to diffusion in polymers showing evidence of time-dependent behaviour. They used

S(a,t)/S(a, oo) = l-w(a)exp {-^(a)*} ,

(10.98)

where

u(a) = 1 -S(a, 0)/S(a, oo), u{ax) = 0;DT(a, t)/DT(a, oo) = 1 -w(a)exp {  -P2{a)t}9

(10.99)

where

w(a)= l-DT(a,0)/DT(a,oo).

All these functions of a may alternatively be expressed in terms of C°° = aS(a, oo), the corresponding concentration in the fully relaxed membrane after theoretically infinite time. Substitution of (10.98) and (10.99) in(10.97) remembering (10.96) yields, after integration with respect to t,

u w uW

D(C-,ao)dC-

(10.100)

where all functions in (10.100) are to be taken as functions of C 00 , i.e. u = ^(C 00 ) etc. Petropoulos and Roussis suggested that u and w will normally be much less than unity, so that L T = L Ti + L Tl approximately, which is the sum of the contributions from the time-dependence of 5 and D T respectively. They proceed to examine some examples in detail.

Time-lag expressions for a system in which the solubility and thermodynamic diffusion coefficient are distance-dependent are obtained by the same authors for S = S(fl, x) = S(a 9 0) < Mx), (10.101)

D T = D T (a, x) = D T (a, 0) < £ 2 (x), (10.102)

where (^(O) =  < / >  2 (0) = 1 an d 0iM > < 5M x ) are non-negative, analytic, and continuous functions in 0 ^ x ^ /.

The time-dependent systems we have considered tend towards a Fickian, purely concentration-dependent system in the final steady state of permeation. We have studied the increment in the time lag which results because the system is not Fickian throughout the permeation process. In contrast, the distance-dependence with which we are now concerned persists for all time and so the time-lag increment has a different significance. Any experimentally measured time lag for a non-homogeneous sheet can be interpreted as if it were homogeneous by applying the Frisch method to (7.5). This will yield an apparent diffusion coefficient D = D(C) which is an average function for the sheet and where C is the averaged concentration variable obtained from the corresponding equilibrium sorption measurements; i.e. C = aS = -f Sdx, (10.103) / Jo where S is the apparent solubility coefficient. The purely concentrationdependent parameters D and S define an 'equivalent Fickian system'. We wish to see how the expression for the time lag for a non-homogeneous sheet differs from the standard expression for the equivalent, purely concentrationdependent system.

References

OF DIFFUSIO N COEFFICIENT S

229

where

4>(x) =

faWfalx).

(10.106)

The procedure developed by Frisch (1957) can be applied to (10.104) and yields the result

^ J '

, oo)-Ct }  dx,

(10.107)

where C{x, oo) is given by the solution of

f D(z) dz = { l - ^ H f ° D(z) dz.

(10.108)

Jci

I ^W J Jct The subsidiary functions in (10.107) are

=1o

and the steady-state flow F is now given by

f °

F = {O(/)}- 1 °De(C,0)dC = Z"1 f °5(z)dz,

(10.110)

Jc,

Jet

from which we find

5

(10.111)

Corresponding expressions for time-lag differences were given by Petropoulos and Roussis (1967) and some special cases were examined. Any time lag can be split in this case into L = LF + Lh by analogy with the time-dependent case L = LF-\-LT.

Ash et al. (1968) quote a particular result thought to be relevant for a membrane made by compaction of powder under pressure. The middle of the membrane is less compressed than the outer layers. For a diffusion coefficient D defined by

D = D0/{ l-<ni(l-tt)} ,

(10.112)

where u = x/l and a is a coefficient, they quote the result

If the form of (10.112) is assumed or known for D then (10.113) allows a to be determined from a measurement of Lx.

A few time-lag relationships permit distinction between time- and distance-dependent anomalies in their most general form. For example:

(i) Always, we have ALj(a0, a  ̂= 0,

230

THE DEFINITION AND MEASUREMENT

(ii) All non-Fickian components of time lag are unaffected by flow reversal in time-dependent systems but not in distance-dependent cases except when the solubility and diffusion coefficient are symmetrical about the mid plane of the membrane for all activities.

Other results are given by Petropoulos and Roussis (1967) and are extended(1969a) to cases in which activity and distance factors are not separable.

Ash, Barrer, and Nicholson (1963) and later Paul (1969) used Frisch's method to study the effect of an immobilizing reaction on the diffusion time lag. Paul's diffusion equation is modified to allow for some molecules being trapped in non-diffusing holes according to a Langmuir-type isotherm. It has the form

(10.114)

where C is the concentration of molecules free to diffuse with a diffusion coefficient D, and a and K are parameters of the immobilization isotherm.

Paul gives general expressions for both the absorption and desorption time lags. Commonly used conditions are those of zero concentration at the downstream face of a plane sheet and a constant concentration Co, maintained at the upstream face. In addition, C = 0 initially throughout the sheet for absorption and C = Co initially for desorption. For these cases, Paul obtained for the time lag for absorption La

6LaD2/ /2= 1+Kf(y)9

(10.115)

where

f(y) = 6y-3{y2+y-(\+y)\n(\+ yyh

and for the desorption lag Ld,

3LdD2/l2=  -1+KgOO,

(10.116)

where

g(y) = 3y"3(l +y)-l{b2 + y-U +y? In (1 + j>)}-

Paul discussed the effect of various parameters on the time lags and their implications for models of diffusion in glassy polymers. Petropoulos (1970)examined the physical assumptions underlying earlier treatments.

10.6.3. Analysis of concentration-distance curves

There are a number of optical methods for observing how either the refractive index or its gradient depends on distance measured in the direction of diffusion at a given time (Crank and Park 1968). Concentration-distance curves can also be obtained in the case of two metals interdiffusing (Barrer

OF DIFFUSION COEFFICIENTS

231

1951). If two infinite media are brought together at t = 0, e.g. two long columns of liquid or two metal bars, the diffusion coefficient and its concentration-dependence can readily be deduced from the concentration distribution observed at some known subsequent time. The conditions of the experiment are

C=C^,

x < 0 , t = 0,

(10.117)

C = 0,

x > 0, f = 0,

(10.118)

where C is the concentration of the component in which we are interested,and x = 0 is the position of the initial interface between the two components at time t = 0. Assume for the moment that there is no over-al change of volume on mixing and that C is measured as mass per unit volume of the system. Then we may use the Boltzmann variable rj  = x/2t* and as in § 7.2.1(p. 105) we obtain the ordinary differential equation

2 ^ = T

drj arj \ ]

On integration with respect to rj  (10.119) becomes

,

(.0,20,

since DdC/dt] = 0 when C = 0. Here Cx is any value of C between 0 and CM . Finally, by rearrangement of (10.120) and introducing x and f, we have

Since (D dC/dr])c = Coo = 0 also, it follows from (10.120) that

f °°xdC = f °° qdC = 0,

(10.122)

Jo

Jo

and in order that the boundary conditions shal be satisfied the origin from which x is measured must be such that (10.122) is satisfied. In other words, the plane, x = 0, must be chosen so that the two shaded areas in Fig. 10.2(a) are equal. In a constant volume system (10.122) is a conservation of mass condition and it is clearly satisfied if x is measured from the initial position of the boundary between the two components at time t = 0. In this case, therefore, the procedure is to plot the concentration-distance curve for a known time as in Fig. 10.2 (b), to locate the plane x = 0 by use of(10.122), and then to evaluate D at various concentrations Cx from (10.121).

The integrals can be obtained by using a planimeter or by counting squares and the gradients dx/dC by drawing tangents. In Fig. 10.2(b) the area representing]^1 x dC is shown shaded. Diffusion coefficients in metal systems were

232

THE DEFINITION AND MEASUREMENT

(a)

(b)

FIG. 10.2. Evaluation of D from a concentration-distance curve using (10.121).

obtained by Matano (1932-3) using this method, and since then it has been widely used. Alternative ways of using (10.121) have been suggested.

(i) One development has been found useful in dilute solutions (Eversole,Peterson, and Kinds water 1941). On integrating by parts (10.121) becomes

Cdx' , (10.123)

dx

At (lnCx)*  d(lnC)*

where x1 is the value of x at which C = Cx and the derivatives are to be measured at the point x = xx. The determination of the gradients at various concentrations is made simpler by this modification if the graph of x against(In C)* is nearly linear as it is in some systems.

A corresponding analysis can be applied to the penetration of diffusing substance into an effectively semi-infinite sheet, provided the concentrationdistance curve can be obtained. An example is the diffusion of dye molecules from a well-stirred solution into a cellulose sheet (Crank 1948a). Eqn (10.121)still holds if x is measured from the surface of the sheet.

(ii) Graphical or numerical methods of evaluating the diffusion coefficient from (10.121) have certain disadvantages. They entail the measurement of slopes and areas under curves and it is clear from the behaviour of the concentration-distance curves in Fig. 10.2 that considerable uncertainty arises for concentrations near the limiting values. Often the values of diffusion coefficients for very smal concentrations of one component are of great importance and so it is desirable to be able to calculate them as accurately as the experimental data permit. A method of improving the the accuracy of the calculations near the extremes of the concentration-range has been suggested by Hall (1953). He examines some experimental data of da Silva and Mehl (1951) for the copper-silver system. Using the nomenclature of

OF DIFFUSION COEFFICIENT S

233

the previous section, he takes C to be the concentration of copper and C^to be 100 per cent copper. Fig. 10.3, taken from Hall's paper, is a probability plot of C/C  ̂ against x/t% i.e. the variable u which is used as ordinate is given by

i<l+erfw) = C/C^.

(10.124)

20 1-5

10

0-5 a 00-0-5

- 1 0-1-5

- 2 0

-1000 0000 1000

2000 3000

FIG. 10.3. Probabilit y plot of a concentration distribution . a0 is the side of the unit cell.

Other relationships involving error functions can of course be used. Hall finds (10.124) convenient for purposes of calculation. We avoid his use of the function erfc for the left-hand side of (10.124) because it is not standard notation. The point of interest is that when plotted in this way the concentration-distance curve becomes linear at the two ends of the concentration range.

Now a straight line on this plot corresponds to an equation of the type

u = hrj + k,

so that, from (10.124) and (10.125), we have

It readily follows that

drj

n^

hCr-exp(w2),

(10.125)

(10.126)

(10.127)

and

Jo

hC

(10.128)

234

THE DEFINITIO N AND MEASUREMEN T

If now we write (10.121) in terms of rj and substitute from (10.127) and (10.128)we obtain

1 7E±

D(C) = -^ + /c-y(l+erfu)exp(w2).

(10.129)

\r h

The differences between (10.129) and Hall's final expression are because the Y\ used here differs from his X by a factor of 2. The quantities h and k are obtained respectively as the slope and intercept of the linear portion of the probability plot, and D is evaluated from (10.129) simply by substituting these values and that of u which through (10.124) corresponds to the C/C  ̂ for which D is required. The relationship (10.129) can be applied at each end of the concentration range with appropriate values for h and k. In the intermediate curved portion of Fig. 10.3 slopes and areas must be measured on a plot of the type shown in Fig. 10.2 and the diffusion coefficient deduced from(10.121). Evidence of the improved accuracy resulting from the use of (10.129)is advanced by Hall.

10.6.4. Systems in which there is a volume change on mixing

The interdiffusion of two components forming a system in which volume changes occur on mixing has been considered by Prager (1953) as follows.

The rates at which the concentrations of the two components CA and CB change at a point are given by

dCA dt

8CB dt

d~ dx

d~~dx

a , -T-(VCA),

(10.130)

dx dx

, , ^(vCB\

(10.131)

dx I dx

where 2A and Q)B are the intrinsic diffusion coefficients introduced in § 10.4,and v is the velocity of the mass-flow assumed to be in the x direction and dependent only on the x coordinate and the time t. There is a relationship between CA and CB at constant temperature and pressure which is

VBCB+VACA = 19

(10.132)

where the Vs are the partial molal volumes of the two components, and also we have

(dCB/dCA)P,T = -VA/VB.

(10.133)

Using (10.132) and (10.133) in (10.131) we find

( 1 0 1 3 4)

dcA

dt

d dx

VA

BvBdcAdx

dv

Bdxh vA dcAB

OF DIFFUSION COEFFICIENT S

235

and combining (10.134) with (10.130) yields

-yBir

dx

dx\ dx j dx\ VB dx

Integration by parts from — oo to x transforms (10.135) into

VACMdVR\ldC

(10.135)

dCA dxdx', (10.136)where v and dCJdx have been assumed zero at x = — oo. Substituting(10.136) into (10.130) and (10.131) we find

dt dx

dx -iuMm\**)dt -dx\D dx)

dx\CB)^VBCA\dCAj\8xdx'where Dv is related to Q)A and Q)B by

(10.137)

(10.138)

(10.139)

which is eqn (10.32). We should note that we are here defining Dv by (10.139).

It has the significance of a mutual diffusion coefficient as defined in § 10.2(p. 205) only if there is no volume change on mixing. The second terms on the right-hand sides of (10.137) and (10.138) arise because of the volume changes on mixing, and they vanish when such changes do not occur, i.e. when(dVA/dCA)PT = 0, in which case (10.137) and (10.138) reduce to the usual diffusion equations.

If the initial distribution is such that

cA = o,cA = ca

X

X

t = 0,

(10.140)(10.141)then we can make the Boltzmann substitution (1894) even if (dVA/dCA)PT is not zero. Thus if we suppose CA to be a function of r\ = x/2t* only, eqn(10.137) becomes

dCA

d^

dr]\--\cA DvL m K RCBcA

dr,d»/7, (10.142)

with boundary conditions

CA = 0, ri  =-oo;

CA = CX,

r\ = oo.

(10.143)

If the concentration distribution CA{r\)  is known from experiment, (10.142)

236

THE DEFINITION AND MEASUREMENT

can be solved for Dv to give

The first term on the right-hand side of (10.144), when written in terms of x and t, is the expression (10.121) for calculating D from the concentration distribution when there is no volume change on mixing. The second term is a smal correction term in which we have substituted for Dv from (10.121)written in terms of r\ as an approximation.

It is of interest to examine what diffusion coefficient is obtained by the Matano (1932-3) procedure, as described in § 10.6.3 (p. 230) when there is a volume change on mixing. Continuing to denote by r\ the distance coordinate measured from the initial position of the boundary between the two components, Matano introduces a new coordinate r\1 measured from a new origin chosen so that JQ°° r] l dCA = 0. If the new origin be at rj  = — 8 then we have q1 = rj  + 8 and hence

f (rj-8)dCA = 0,

(10.145)

so that

8 = -^- [ ~ rjdCA.

(10.146)

^o o J o

Furthermore, Matano deduces a diffusion coefficient from the expression dwi fCl

Dc c = -2—1+~

r\idCA.

(10.147)

dCAJ0

Now

5, (10.148)

= f

Jo

o

Jo

and hence the diffusion coefficient calculated in this way is DCA=CI = - 2 ^ - ( | % d C1 + C1A

(10.149)

since dt]JdCA = drj/dCA and where S is given by (10.146). Comparing(10.149) with (10.144) shows that this procedure does not yield exactly the coefficient Dv related to the intrinsic diffusion coefficients by (10.139)but only an approximation to it. It assumesr rBI r T/ \xr dC^ = constant,

(10.150)

Jo CAK

\3CA

the constant being 8, the displacement of the origin. Prager (1953) suggests

OF DIFFUSIO N COEFFICIENT S

237

that a better approximation is to treat VB and (l/CA)(dVB/dCA) as constants,in which case (10.144) becomes

where B is given by

B = -

dCA\ dCA, (10.151)

(10.152)

This procedure, like Matano's, requires no data on the partial molal volumes.

If such data are available it is of course possible, though more laborious, to use the complete equation (10.144) to evaluate Dv.

We can now see what is the physical significance of the diffusion coefficient deduced by the Matano procedure when there is a volume change on mixing.

Returning to eqn (10.142) and writing (j>  for the flow velocity due to volume change, we have

_ 2 ^ = A L K ^ | d

(10.153)

drj drj\ dt] I drj

and on integrating from CA = 0 to CA = C ,̂ this becomes

o

- [C> ] c0«.

(10.154)

/•C

- 2

Jo

\

o

Since dCydf/ = 0 at both ends of the range of integration, we see that ridCA9

(10.155)

where 0^ is the value of <j)  when CA = C^. Thus by choosing the origin of rj such that the right-hand side of (10.155) is zero, we select a frame of reference such that, provided C = 0 at one end of the system, there is no flux of component A at either end due to volume change. It must be emphasized that the removal of the effect of volume change is complete only at the ends of the system, and so the diffusion coefficient deduced by using the Matano procedure is not the mutual diffusion coefficient. In fact, it is not a diffusion coefficient which is readily related to those obtained by other methods.

An alternative treatment of a system in which a volume change occurs makes use of the frame of reference fixed with respect to the total mass of the system. Thus in terms of the variables C™ and £M introduced in § 10.3, eqn(10.121) (p. 231) becomes

238

THE DEFINITION AND MEASUREMENT

and according to the Matano procedure the origin of £M is to be chosen such that

Jo

(10.157)

The upper limit of integration for C™ comes from (10.16) since when £M = oo,C^ = 0. Choosing the origin of £M so that (10.157) holds ensures that the boundary conditions are satisfied as in §10.6.3 (p. 231). Thus, provided concentrations and distance scales are expressed in the new units as described in § 10.3, the coefficient DM is obtained from (10.156) and (10.157).

By combining (10.23) and (10.35) we have a relationship between DM and the intrinsic diffusion coefficients, Q)A and Q)B, which takes the place of(10.139) in Prager's method.

10.6.5. Sorption method

(i) Constant diffusion coefficient. A different approach is to deduce the diffusion coefficient from observations of the over-al rate of uptake of component A by a plane sheet of component B. Such a method has been used,for example, to determine the diffusion coefficient of direct dyes in cellulose sheet (Neale and Stringfellow 1933) and of oxygen in muscle (Hil l 1928). In each case the diffusion coefficient was assumed constant.

We shal describe the method in terms of the uptake of vapour by a plane sheet, first on the assumptions that the diffusion coefficient is constant and the sheet does not swell, and then for cases in which the sheet swells and the diffusion coefficient is concentration-dependent. Its application to other systems will be obvious. The experimental procedure is to suspend a plane sheet of thicknes / in an atmosphere of vapour maintained at constant temperature and pressure, and to observe the increase in weight of the sheet and hence the rate of uptake of vapour. This can be done most conveniently by hanging the sheet on a spring of known stiffness. The appropriate solution of the diffusion equation may be written

if the uptake is considered to be a diffusion proces controlled by a constant diffusion coefficient D. Here Mt is the total amount of vapour absorbed by the sheet at time f, and M ̂  the equilibrium sorption attained theoretically after infinite time. The application of (10.158) is based on the assumption that immediately the sheet is placed in the vapour the concentration at each surface attains a value corresponding to the equilibrium uptake for the vapour pressure existing, and remains constant afterwards. The sheet is considered to be initially free of vapour. The value of t/l2 for which MJM  ̂ = \,

OF DIFFUSION COEFFICIENTS

239

conveniently written (t/l2)±,  is given by

(10.159)

I2),

n*D~{\(>  9 16

approximately, the error being about 0-001 per cent. Thus we have D = 0-049/(t/l%,

(10.160)

and so, if the half-time of a sorption proces is observed experimentally for a system in which the diffusion coefficient is constant, the value of this constant can be determined from (10.160). The extension of this method to less simple systems is as follows.

(ii) Sorption by a swelling sheet. In deriving (10.158) the thicknes / of the sheet is assumed to remain constant as diffusion proceeds. In practice it often happens, however, that the sheet swells and the thicknes increases as the vapour enters. Eqn (10.158) can still be used in such cases, provided we take a frame of reference fixed with respect to the substance of the sheet, and concentration and thicknes are measured in the units discussed in § 10.3(p.207). Thus we take the basic volume of the sheet to be its volume in the absence of vapour and use the unit of length £B such that unit £B contains, per unit area, unit basic volume of the substance of the sheet B. Then the thicknes of the sheet, measured in these units, is constant and equal to the original unswollen thickness, and the diffusion coefficient deduced from (10.158) by substituting the original thicknes for / is that for the diffusion of vapour relative to stationary sheet (denoted by DA in § 10.3). If there is no over-al volume change on mixing, i.e. if the increase in volume of the sheet is equal to the volume of vapour sorbed at the vapour pressure existing in the experiment, the coefficient obtained by this sorption method is related to the mutual diffusion coefficient Dv', deduced by the Matano procedure, by eqn(10.28), i.e.

DBA = Dv(\ -volume fraction of vapour)2.

(10.161)

(iii ) Concentration-dependent diffusion coefficients. Clearly from (10.158)and (10.160) the value of t/l2 for which MJM  ̂ has any given value, and in particular the value of (£//%, is independent of M^ when the diffusion coefficient is constant. Fig. 10.4 shows a set of curves obtained experimentally by Park (see Crank and Park 1949) for the uptake of chloroform by a polystyrene sheet, each curve corresponding to a different vapour pressure and hence a different M^ . It is evident that {t/l2)± decreases considerably the greater the value of the final uptake M^ and therefore the diffusion coefficient is not constant but increases as the concentration of chloroform is increased.

The problem is to deduce quantitatively how the diffusion coefficient is related to concentration, given the half-times of sorption experiments carried out for a number of different vapour pressures.

240

TH E DEFINIT IO N A N D MEASUREMEN T

10

20

30 t/l2x 10 -9( scm-2)

40

50

FIG . 10.4. Rate of uptake of chloroform by polystyrene sheet at 25 °C.

Application of (10.160) to each of the curves of Fig. 10.4 yields some mean value 2), say, of the variable diffusion coefficient averaged over the range of concentration appropriate to each curve. The method devised by Crank and Park (1949) depends on the fact that, for any experiment, D provides a reasonable approximation to (l/Co)Jo°DdC, where 0 to Co is the concentration range existing in the sheet during that experiment. This was shown to be so (Crank and Henry 1949a) by evaluating numerical solutions of the diffusion equation for a number of variable diffusion coefficients. By applying(10.160) to the sorption-time curves so calculated, values of D were obtained and compared with corresponding values of (1/CO) J^DdC. Thus by deducing a value of D from each of the experimental curves of Fig. 10.4 using (10.160), and assuming the approximate relationship

f °

Jo

= (l/C0)f DdC,

(10.162)a graph showing DC0 as a function of Co can be drawn as in Fig. 10.5 and numerical or graphical differentiation of the curve with respect to Co gives a first approximation to the relationship between D and C. Numerical data are given in Table 10.1.

In many cases this first approximation may be sufficiently accurate, but successively better approximations can be obtained as follows. Sorptiontime curves are calculated numerically for the D-C relationship obtained as

OF DIFFUSION COEFFICIENT S

241

20 r

c- 15

©X o

IQ

10

5

10

15

20

Surface percentage regain Co FIG . 10.5. Graph of DC0 as a function of Co.

the first approximation, there being one calculated curve for each experimental curve of Fig. 10.4. The D values derived by applying (10.160) to the calculated curves are shown in Table 10.1, column 6. Comparison of these calculated D values with the experimental ones and therefore with the first estimate of (1/CO) J^0 D dC shows the errors involved in use of (10.162) for this particular type of diffusion coefficient. The correct relationship between D and (1/CO) J£° D dC for the D-C relationship given by the first approximation can be plotted, and from this improved values of (1/CO) J£° D dC can be read off for the experimental values of D. By repeating the differentiation, a second approximation to the diffusion coefficient D is obtained. The proces can be repeated til l the calculated and experimental values of D agree to the accuracy desired. Results are shown in Table 10.1.

In this form the method can be used whatever the relationship between D and C but the calculations involved in evaluating successive approximations are tedious and laborious.

(iv) Exponential and linear diffusion coefficients. In many systems the diffusion coefficient is found to depend either linearly or exponentially on concentration, and so for these cases correction curves have been produced showing the difference between (1/CO) J£°(D/D0)dC and D/Do, where Do is the value of D at zero concentration of vapour or whatever the diffusing substance is. The correction curves are shown in Fig. 10.6. By using the appropriate curve, the diffusion coefficient-concentration relationship can be deduced as readily from sorption experiments as from steady-state measurements. In each case, differentiation of J D dC to obtain D is the

242

THE DEFINITION AND MEASUREMENT

30

25

20

15

io

1

2

3 4 5 6 7 8 910

20 30

DJDO

FIG. 10.6. Correction curves for sorption method. Percentage difference is

(D/D0)-(l/C0)Jg°(D/D0)dC

expressed as a percentage of D/Do. These curves can be applied to both half-times and initial gradients.

only mathematical operation involved. Park (1950) used a method of

differentiation which is considerably more accurate than direct graphical differentiation if D is an exponential function of C. Denoting J^0 {D/Do) dC by /, he plotted log / against Co to obtain a curve which approximates to a straight line. Then d log I/dC0 is easily obtained by graphical differentiation and D follows from the expression

D/Do = d//dC0 - 2-303/ d log I/dC0.

(10.163)The method for exponential and linear diffusion coefficients is therefore as follows:

(1) plot sorption-time curves for different vapour pressures as in Fig.

10.4;

(2) calculate D for each curve using (10.160);

(3) extrapolate D to zero concentration to give Do;

(4) read off from the appropriate correction curve of Fig. 10.6 the value of

(l/C0)JS°(D/D0)dC = / /Co for each D/Do;

(5) differentiate / using (10.163) or otherwise to obtain D/Do and hence D.

A second approximation may be necessary due to the uncertainty in the first estimate of Do. It is, of course, necessary to have some idea of the type of diffusion coefficient involved before the choice of correction curve can be made. For example, if the initial choice is exponential, but the final result is nothing like an exponential function, and if use of the linear correction curve

OF DIFFUSION COEFFICIENTS

243

also fails, then the method of successive approximations has to be carried out as described above in § 10.6.5 (iii ) (p. 239)

For diffusion coefficients varying exponentially with concentration Hansen (1967) calculated correction factors, F.d and Fd, which when applied to D give D(C0), where Co is the surface concentration for absorption or the initial uniform concentration for desorption, i.e.

D(C0) = FaD or FdD.

His computed results are reproduced in Table 10.2, where exp K is the ratio of the diffusion coefficients at the extremes of the concentration range in any experiment and T± = DotJ{L')2, where L' is the half-thicknes of a free sheet or the full thicknes of a film attached on one surface to an impermeable backing. After deducing D from the half-times measured for several concentration ranges, Do is estimated by extrapolation. Values of exp X, and hence of the correction factors F can then be estimated and an approximation to a D(C) relationship obtained. This can be improved iteratively. Hansen finds his results agree reasonably well with those of Table 10.1.

Fels and Huang (1970) described a method of obtaining the diffusion coefficient and free volume parameters (Fujita 1961) from desorption data.

They obtained numerical solutions of the equation

vP \dC

dt " — < " - 1 7 - 1 K x n | -

where a and b involve free volume parameters and the diffusion coefficient,and fP is the volume fraction of the penetrant.

(v) Use of a single sorption experiment. Duda and Vrentas (1971) develop a new technique for deducing the concentration-dependence from a single sorption curve, based on the method of moments (§ 7.4, p. 129). They also use only the first two moments, but a novel feature is that they expres their concentration profile in terms of a variable related to the amount of penetrant in a given part of the polymer rather than the space coordinate as in(7.152). In the nomenclature of § 7.4 (p. 129) their profile can be written

where AQ,AX are undetermined functions of time T, \j/(T) = c(0, T) and

cx

r1

m = {c(X\ T)-il/(T)} dX\ M = {c{X\ T)-^(7)}  dX'.

Jo

*o

Such a form is capable of describing the concentration profile over the entire duration of the sorption experiment. After considerable manipulation Duda and Vrentas arrive at a fairly simple set of two algebraic equations and one

244

THE DEFINITIO N AND MEASUREMEN T

differential equation from which the concentration-dependence F(c) can be obtained when the sorption-time curve and its derivative are available from experimental data. Duda and Vrentas tested the accuracy of the method for exponential diffusion coefficients varying by as much as five-fold and found about 5 per cent accuracy over 80 per cent of the concentration range.

There was a serious loss of accuracy at low concentrations but complementary studies of desorption could circumvent the difficulty. In practice, the need to carry out numerical differentiation may prove a serious drawback. But this and other ways of extracting information from single sorption, desorption or permeation curves deserve further study. Duda and Vrentas include the effects of volume changes on mixing and phase volume change. They also derive expressions for the concentration distribution corresponding to a prescribed diffusion coefficient.

10.6.6. Sorption-desorption method

A method which uses both sorption and desorption data, is very quick and simple in cases to which it is applicable. If Ds is calculated using (10.160) from the half-time for sorption and J5d from the half-time for desorption over the same concentration range, then ^{Ds + Dd) is a better approximation to(l/C0)J£°DdC than either Ds or Dd separately. Often it is a very good approximation and has been used without correction in some instances(Prager and Long 1951; Kokes et al 1952). If the range in D is smal enough for this to give the accuracy required, the method is particularly simple since there is no need even to extrapolate to obtain Do at zero concentration.

Kokes, Long, and Hoard (1952) have applied the sorption-desorption method to successive smal concentration ranges so that the approximation ^{Ds + Dd)can be used with more confidence than it could if applied to the complete concentration range. Should it be necessary to obtain higher accuracy, the correction curves of Fig. 10.7 can be used to obtain better estimates of(1/CO) JQ° D dC. These are then differentiated as in the sorption method to obtain D.

10.6.7. Use of initial rates of sorption and desorption

In § 10.6.5 (p. 240) we deduced an average diffusion coefficient from the half-time of a sorption curve by using (10.160). It is also possible to deduce an average diffusion coefficient from the initial gradient of the sorption curve when plotted against the square root of time. Thus, in the early stages,for a constant diffusion coefficient D and a sheet of thicknes /, we have(§4.3.2, p. 48)

Mt 4 lDt\*

(10.164)

If the initial gradient, R = d(Mr/M00)/d(t//2)^, is observed in a sorption

OF DIFFUSION COEFFICIENT S

245

15

| 10

10

20

30

FIG . 10.7. Correction curve for  sorption-desorption method. Percentage difference is

(\/C0)jc0°(D/D0)dC-%Ds + Dd)/D0

expressed as a percentage of j(Ds + Dd)/D0. (N.B. The differences here are opposite in sign to those of Fig. 10.6.)

experiment in which D is concentration-dependent, then the diffusion coefficient D deduced from (10.164) is

average

D = —R2.

(10.165)

This, too, provides an approximation to (l/C0)j*Q 0DdC, and the sorption method can proceed as above but starting with the new values of D given by(10.165) as original data. Initial rates of desorption can be used similarly.

Correction curves for exponential and linear diffusion coefficients are shown for the sorption method in Fig. 10.6 and for sorption-desorption in Fig. 10.7.

If the sorption curve when plotted against (t/l2)*  is approximately linear as far as MJM  ̂ = \, and this is often true in practice, then it is easy to see that(10.160) and (10.165) yield roughly the same diffusion coefficient. Thus for a

246

THE DEFINITION AND MEASUREMENT

linear sorption curve we have

R = yj(t/l%,

(10.166)

and so from (10.165) we find

D = ̂  /(t/l% = 0049/(f//%

(10.167)

which is the same as (10.160).

10.6.8. Use of final rates of sorption and desorption

In the later stages of diffusion in a plane sheet only the first term in the series of (10.158) need be considered, and we have

— {In {M^-Mt)} = \-.

(10.168)

During a sorption experiment the final concentration, Co say, is approached throughout the sheet; during the final stages of desorption the concentration everywhere tends to zero. If the diffusion coefficient is constant, both experiments should yield the same value on applying (10.168). Otherwise, the application of (10.168) to a sorption experiment gives D(C0), while from desorption we obtain Do, the value at C = 0. By this method, we avoid the extrapolation needed to estimate Do in the method of § 10.6.5 (iii) . Frensdorff

(1964) used both methods and examined the extent of the final linear portions of desorption curves by computing numerical solutions of the diffusion equation for D(C) given by

where Co is the initial equilibrium concentration. His results are reproduced in Fig. 10.8

10.6.9. A step-function approximation to the diffusion coefficient

Prager (1951) described an alternative method of deducing the diffusion coefficient-concentration relationship from sorption data. The principle of the method is to approximate to the actual concentration-dependence by a step function. For such a function the differential equations can be solved analytically (Chapter 13) and the heights of the individual steps computed.

The step function is then smoothed out by an averaging process.

The concentration range to be studied is divided into a number of intervals and we assume that the diffusion coefficient D(C) has a constant (although as yet unknown) value in each. For a diffusion experiment covering only the first concentration interval D is constant throughout and may be calculated if Mt is known as a function oft, using the solution (10.164). For a diffusion experi-

OF DIFFUSION COEFFICIENTS

247

0 1 -

D(0)t/P

FIG. 10.8. Calculated desorption curves for a linear diffusion coefficient D(C)/D{0) = 1 + A'C/Co,where Co is the initial concentration. Numbers on the curves are values of A', and / is the thickness of the sheet. (From Frensdorff 1964).

ment covering the first two intervals, D{C) is given by a step function whose value in the first interval is now known from the first calculation. The value in the second interval may be calculated as described below using the equations of § 13.2.2 (p. 290). This procedure may be continued so as to calculate the value of D(C) in the third interval, its value in the first two being known,and so on, until the entire concentration range has been covered. The method as described here is based on the treatment of diffusion with discontinuous boundaries given in §§ 13.2.2 and 13.2.4 (p. 290 and 296). An alternative treatment is given in Prager's original paper (1951).

Before the concentration in the centre of the film attains an appreciable value we may consider diffusion to take place into a semi-infinite medium.

If we have a two-step diffusion coefficient such that for concentrations greater than Cx , D = D l 9 and for concentrations less than Cx, D = D2,then the diffusion proces can be described by the equations of § 13.2.2 if

248

THE DEFINITION AND MEASUREMENT

D1 and D2 are known. In particular, dMJdt* is given using the nomenclature of that section by

dMt _ 2AD\

Here we have the opposite problem, i.e. given dMJdt  ̂ from an experiment and D2 having been calculated from the previous experiment, to find D1.

If Mt is measured as a function of t*  this means essentially that AD\ is measured. Hence if we estimate D1,k is determined from (13.12) on p. 291 and a new Dl follows from (13.15) of the same section. Successive estimates of D1 are made till  agreement is obtained between estimated and final values of Dx. The graphs shown in Figs. 13.4, 13.5 and 13.6 of Chapter 13 can be used to help the calculation.

The method is readily extended to a three-step diffusion coefficient and then to higher numbers of steps. Thus if

= D2,

the proces is described by the equations of § 13.2.4 (p. 296). Again AD\ is measured and D2, D3 are known from previous experiments. We estimate Dx and calculate kx from (13.32) and k2 from (13.38). Finally we check kl ,k2,D1 in (13.39), repeating if necessary as before. The number of equations of the type (13.38) and (13.39) increases with the number of steps in the diffusion coefficient but the method still holds.

Fujita and Kishimoto (1952) analysed Prager's data by the method of moments, § 7.4.

10.6.10. Sorption by sheets initially conditioned to different uniform concentrations

Barrer and Brook (1953) used a method of measuring the concentrationdependence of the diffusion coefficient based on a series of sorption experiments. The concentration Co at the surface of the specimen is kept constant throughout the series but the initial uniform concentration, Cx, through the sheet, is different for each experiment. Denoting again by Mt the amount of diffusing substance taken up by the sheet in time t, we may write for the initial stages of sorption,

M

C1> C>

C < Cy,

cx>c-. >cy,

(10.169)(10.170)(10.171)

K

(10.172)

Here K is different for each experiment, being a function of Cl 5 the initial concentration through the sheet. A curve showing K as a function of Ct must cut the axis of C, at the point C1 = Co because then the initial rate of sorption, and hence K, is zero, there being no concentration gradient. Thus

the experimental curve of K against Cx, when extrapolated, must always pass

OF DIFFUSION COEFFICIENTS

249

through Cj = Co when K = 0. Furthermore, as the interval Co — C1 is decreased progressively in successive experiments the sorption proces can more and more nearly be described by the diffusion equation and its solution for a constant diffusion coefficient, i.e. by

Mf =

(10.173)

where Do is the value of the diffusion coefficient at the concentration Co.

Hence, as Cx approaches Co, the curve of K against Cx approaches asymptotically a tangent of slope — 4D§/TT*. This differs by a factor of two from the expression given by Barrer and Brook, because they consider the amount entering through one face of the sheet, whereas we include both. If the experimental curve is sufficiently well defined by the data obtained from the sorption experiments, the tangent can be drawn and Do deduced from its gradient using (10.173). By repeating the series of experiments for different values of the surface concentration Co, the relationship between the diffusion coefficient and concentration is obtained. If, as in some zeolites, D decreases as C increases, then the curve of K against Cl approaches the tangent from above as in Fig. 10.9. If, however, D increases as C increases, which is often

FIG. 10.9. Curve of A'against C1 approaching asymptote from above because D decreases as C increases.

the case in solvent-polymer systems, then the tangent is approached from below as in Fig. 10.10. Thus the curves of K and Cl show at a glance the nature of the concentration-dependence of D. If it is practicable to carry out desorption experiments as well as sorption, that is to include values of C1 which are higher than the surface concentration Co, the curve of K against Cl will cross the Cx axis at C^  ̂ = Co, as in Fig. 10.11. This should allow the tangent to be drawn more accurately since extrapolation is avoided.

250

THE DEFINITION AND MEASUREMENT

FIG. 10.10. Curve of K against Cx approaching asymptote from below because D increases as C increases.

C,

FIG. 10.11. Curve of K against C\ using data from both sorption and desorption experiments.

10.7. Weighted-mean diffusion coefficients

In § 10.6.7 (p. 244) we looked upon the average diffusion coefficient deduced from the initial rate of sorption by (10.165) as as approximation to (1/CO) x Jo° D dC. Subsequently, numerical solutions showed that the initial rates of sorption and desorption are much more closely controlled by weightedmean diffusion coefficients of the form

Cp-lD(C)dC

(10.174a)

On the basis of his original calculations for diffusion coefficients increasing with concentration over ranges up to 200-fold in one or other of the ways shown by curves, 1, 3, 4 in Fig.  9 .4, Crank suggested the values p = 1-67, q = 1-85. Kishimoto and Enda (1963)  found good agreement between D(C) obtained for the polymethyl acrylate-benzene system from steady-state measurements and by using (10.174a, b) with these values of p and q. Barrie and Machin (1971)  found that their experimental data also supported the same values. They pointed out, however, that the correspondence principle between sorption and desorption (see  §9.3.1, p. 173)  implies that for very small concentration ranges p and q should approach the same limiting value. By using Lin Hwang's (1952) series solution they concluded that as C o -• 0, p - >  2/(7i-2). Wilkins's (1963) solutions for small e presented in Table  7 .6 confirm this limiting value. Also, we may regard his solutions for e = oo as limiting cases for linear diffusion coefficients of very large range. It is easy to deduce that for D increasing 1-62  <  p  <  1-75 and 1-75  <  q  <  1-89. These ranges include the values of 1-67 and 1-85 which fit experimental measurements over a wide intermediate range of D(C). Kishimoto and Enda (1963)  proposed a convenient approximate way of using (10.174b). They assume

D(C) = D 0 + fc 1 C + /c 2 C 2 + ..., (10.175)

where k 1 ,k 2 etc. are unknown coefficients. By introducing (10.175) into (10.174b) and integrating they find that D d may be written

10.8. Radiotracer methods

10.8. Radiotracer methods

A number of experimental arrangements have been proposed for observing the diffusion of labelled molecules. If the total concentration of labelled and

References

252

THE DEFINIT ION AND MEASUREMENT

unlabelled molecules is kept constant throughout the system, self-diffusion coefficients are measured. The same principles have been applied in the presence of an overal concentration gradient.

In the 'thin-smear' method, Moore and Ferry (1962. 1968) use a radioactively-labelled penetrant in trace amounts so that its concentration is very smal throughout the experiment. Initially, penetrant is spread in a thin layer on one surface of a polymer disc and the variation of activity with time at the opposite face is observed. In general, this activity is due to the integrated effect of /^particles emanating from different depths in the polymer.

The diffusion coefficient is deduced by comparing the measured activity change with the corresponding theoretical expression

N(t)

JV(oo)

- 1 - 2

1 + e 1+48 1 + 9e

(10.178)

where N(t) and iV(oo) are the activities just outside the inert surface of the disc at time t and at equilibrium, i = n2Dt/h2, e = {n/^ih)2, D is the diffusion coefficient, h the disc thickness, and fi the absorption coefficient for the /?-particles in the polymer, assuming an exponential law. Eqn (10.178) takes into account radiation contributions from below the inert surface. If, however,the absorption of the /^-particles is sufficiently high we have the case of e = 0 and the activity is simply proportional to the concentration at the inert surface.

In the twin-disc method (Moore and Ferry 1962), a disc containing unlabelled penetrant is place on top of an identical disc containing labelled penetrant. Sn this case, the activity is taken to measure the concentration of radioactive penetrant at the upper surface of the sample and the appropriate mathematical solution is

N(t)

l - i ( e - < - i e - ^ + i e - 2 5 T - _y

(10.179)

N(oo)

ny >

3

Jackson, Oldland, and Pajaczkowski (1968) used an arrangement which can be described as follows. The radioactive source occupies the region h < x < k\ diffusion takes place into a polymer sheet in k < x < L and into a cover film in 0 < x < h. They used the appropriate particular form of the solution (4,56) to calculate the concentration distribution

C

2L ™ 1

., / nnk nnh\ nnx{-n2x) sin s in— cos-—,

(10.180)

L I

|

/

tA U

\

ft

f\

i->111

Jil l

I V/VyiJ

7

C,

K[k — n) i H

\ L

LI

L

where x = ?i2Dt/L2. This is substituted into the expression for the activity N(r), at the surface x - 0,

rL

N(t) = H\ C/(x)dx,

(10.181)

OF DIFFUSION COEFFICIENTS

253

where f(x) is the fraction of /?-rays reaching the surface from nuclei at distance x; H is a constant of the apparatus. Jackson et ai assume f(x) = exp( — pix) and obtain

N{t) = 1 + / 2L ' " 2 ^ "

7.^._nnk . nnh

N(oo)

where

If the activity is observed at the surface x = L, eqn (10.182) still holds with the modification that

/ cos nn — Q'^

A(n) =

Expressions (10.181) and (10.182) are based on the assumption that the diffusion coefficient is the same throughout the system though there are, in fact, three distinct layers. Jackson et al. (1968) examined another extreme model. The middle layer, in which the polymer is initially confined, is now considered as a perfectly stirred liquid. The penetrant concentration just inside the polymer is K times that in the stirred liquid at the interface between them. Also, the cover film is now taken to be of zero thicknes and so forms the surface x = 0. The mathematical solutions of § 4.3.5 (p. 56) apply, and when substituted in (10.181) result in the expression, for the surface x = L,

where qn are the non-zero positive roots of tan qn — —ocqn,

a = fc/KL, T = Dt/(L-k)2, and B(n) =

Park (1954) who applied a similar technique to the self-diffusion of tricresyl phosphate in polystyrene found it necessary to construct a jS-ray absorption curve under the conditions actually used in the diffusion experiments. He used two layers of equal thicknes and so numerical and graphical methods were needed to obtain the diffusion coefficient.

The j?-particle absorption techniques described above are difficult to apply when the penetrant is volatile. Park (1961) therefore used a radioactive exchange proces in a sealed equilibrium sorption system. The mathematical solutions required are again those of § 4.3.5 (p. 56).

11

NON-FICKIAN DIFFUSION

11.1. Glassy polymers

THE diffusion behaviour of many polymers cannot be described adequately by a concentration-dependent form of Fick's law with constant boundary conditions, especially when the penetrant causes extensive swelling of the polymer. Generally, this is the case with so-called glassy polymers which are said to exhibit 'anomalous' or 'non-Fickian' behaviour. In rubbery polymers,on the other hand, diffusion is generally Fickian. The essential distinction is that polymers in the rubbery state respond rapidly to changes in their condition. For example, a change in temperature causes an almost immediate change to a new equilibrium volume. The properties of a glassy polymer, however, tend to be time-dependent; for example, the stres may be slow to decay after such a polymer has been stretched. Deviations from Fickian behaviour are considered to be associated with the finite rates at which the polymer structure may change in response to the sorption or desorption of penetrant molecules.

Anomalous effects may be directly related to the influence of the changing polymer structure on solubility and diffusional mobility, or they may result from the internal stresses exerted by one part of the medium on another as diffusion proceeds.

Polymers usually have a wide spectrum of relaxation times associated with structural changes, but all of them decrease as temperature or penetrant concentration is increased and motion of the polymer segments enhanced.

At a given concentration, the change from the glassy to the rubbery state is said to occur at the glass transition temperature. A sorption process, for example, will be influenced by those segmental motions which occur at about the same rate or slower than the motivating diffusion process. In rubbery polymers, well above their glass temperature, the polymer chains adjust so quickly to the presence of the penetrant that they do not cause diffusion anomalies.

Alfrey, Gurnee, and Lloyd (1966) proposed a useful classification according to the relative rates of diffusion and polymer relaxation. Three classes are distinguished:

(i) Case I or Fickian diffusion in which the rate of diffusion is much less than that of relaxation;

(ii) Case II diffusion, the other extreme in which diffusion is very rapid compared with the relaxation processes;

NON-FICKIA N DIFFUSION

255

(iii ) Non-Fickian or anomalous diffusion which occurs when the diffusion and relaxation rates are comparable.

The significance of the terms Case I and Case II is that they are both simple cases in the sense that the behaviour of each can be described in terms of a single parameter. Case I systems are controlled by the diffusion coefficient.

In Case II the parameter is the constant velocity of an advancing front which marks the innermost limit of penetration of the diffusant and is the boundary between swollen gel and glassy core. Case II is also a second extreme or limiting case with respect to the shape of the sorption-time curve. If we denote the amount sorbed at time t by Ktn, with K and n constants, then Case II systems are characterized by n = 1 and Case I systems by n = \.

Non-Fickian systems lie between Case I and Case II in that n takes an intermediate value between \ and 1, or changes sigmoidally from one to the other. Also, non-Fickian behaviour needs two or more parameters to describe the interacting diffusion and relaxation effects inherent in it.

11.2. Characteristic features

Extensive reviews are available of the experimentally observed diffusion anomalies in various polymer systems (Rogers 1965; Alfrey et al. 1966;Park 1968; Stannet, Hopfenberg, and Petropoulos 1972; Hopfenberg and Stannet 1973). These contain many references to original papers. We shal confine attention in this chapter to a qualitative description of the main characteristic features. It provides a background for the discussion in § 11.3 below of the mathematical models which have been advanced in partial explanation of the anomalies. The different types of behaviour are summarized in Fig. 11.1, taken from Rogers (1965).

(i) Fickian: Case I. The characteristic features of Fickian diffusion,controlled by a concentration-dependent diffusion coefficient, are listed in§9.4 (p. 179). The term pseudo-Fickian has been used (Rogers 1965) to describe sorption-desorption curves of the same general shape and disposition, but for which the initial portion persists for a shorter time.

(ii) Sigmoid. Curves of the general shape of Fig. ll.l(b ) have been observed experimentally in many systems (Park 1968). The sorption curves are sigmoid in shape with a single point of inflexion often at about 50 per cent equilibrium sorption. The initial rate of desorption exceeds that of sorption, but desorption soon becomes slower and the curves cross.

(iii ) Two-stage sorption. Bagley and Long (1955) carried out a series of'interval' sorptions of acetone by cellulose acetate. The polymer was first brought into equilibrium with acetone vapour at one vapour pressure and then the sorption-(time)̂ relationship resulting from a smal increase in vapour pressure was observed. An initial rapid uptake, a linear function of

256

NON-FICKIAN DIFFUSION

Fickian

/

/

Sigmoid

(b)

/

(a)

Pseudo-Fickian

y

/

Two-stage

(c)

(d)

V

FIG. 11.1. 'Non-Fickian' or 'anomalous' sorption and desorption curves compared with Fickiantype curves. (Rogers 1965).

(time)*, leads to a quasi-equilibrium acetone uptake as in Fig. 11.1c, followed by a slow approach to a final true equilibrium. Bagley and Long (1955)advanced the simple interpretation that a quasi-equilibrium is reached rapidly first at the polymer surface and then by simple diffusion throughout the polymer sheet. The second stage of sorption is associated with an increase in surface concentration which occurs slowly compared with the diffusion proces and is the rate-determining factor for sorption. The concentration is virtually uniform throughout the sheet and increases at a rate independent of the thickness. The sigmoid curve as in Fig. 1 l.l(b) is a special case in which surface concentration changes and diffusion flow occur at comparable rates.

An experimental observation of the acetone distribution in a sheet by Long and Richman (1960) confirmed this interpretation and showed that the surface concentration Cs is well represented by

Q __ Q -\-(C C HI e~^f)

(11 1)

where C{ and Ce are the surface concentrations achieved instantaneously and at final equilibrium, t is time and /? a constant. Park (1961) has shown that the expected relation between the diffusion coefficient calculated from the first stage and the self-diffusion coefficient is satisfied provided the activity

NON-FICKIA N DIFFUSION

257

and volume fraction from the quasi-equilibrium isotherm are used and not those from the final equilibrium isotherm.

(iv) Advancing boundaries: Case II. When a liquid penetrant diffuses into a polymer sheet or filament, sharp boundaries can often be seen under a microscope. The topic is reviewed by Park (1968) and Rogers (1965) with references to original papers. Hartley (1946) noted three boundaries. The inner boundary marks the limit of penetration of the liquid, while the outer boundary shows the limit of the swollen gel. The third, intermediate, boundary is usually thought to lie between polymer in the elastic rubbery state and glassy polymer. When the polymer sheet is in contact with vapour rather than liquid penetrant similar phenomena are observed but in many cases the middle boundary will be missing if the whole system is in the glassy state.

Often the positions of the boundaries are proportional to £\ Cases in which each boundary moves with a constant velocity and also intermediate power laws have been observed by Hartley (1946) and Kwei and Zupko(1969). Wang, Kwei, and Frisch (1969) point out that an alternative expression for the depth of penetration is at + bt*, where a and b are constants.

Robinson (1950) obtained interferometric fringe photographs of chloroform penetrating cellulose acetate between parallel glass plates. In particular,the concentration was seen to change very rapidly in the region of the inner boundary, implying the existence of large internal stresses due to the interaction of the swelling polymer and the central unattacked core of the sheet.

Not only can the orientation of the polymer molecules be changed by these stresses (Dreschel, Hoard, and Long (1953)), but also Hermans (1948) and Alfrey et al. (1966) have observed anisotropic dimensional changes and transverse cracking of the unswollen core.

Related effects in permeation experiments were observed by Park (1951).

Meares (1958) found a rapid initial flux of allyl chloride vapour through a membrane of polyvinyl acetate, which quickly fell to a low value before the more normal gradually increasing flow occurred. Meares attributed the initial behaviour to the increase in diffusion coefficient brought about by the stres exerted by the swollen surface layers on the solvent-free region beneath. Similar overshooting in sorption experiments has been observed(Rogers 1965).

11.3. Mathematical models

A number of authors have proposed mathematical models of the penetrant-polymer diffusion phenomena. No single model successfully predicts all the experimental observations. Nevertheless, each one accounts for some of the features described in § 11.2 (p. 255), and collectively they contribute

258

NON-FICKIAN DIFFUSION

towards an elucidation, albeit incomplete, of the complex mechanisms involved. It is only possible in this book to describe briefly the salient features of some of the models. Details are given in published papers. Essentially they are all concerned with the combination of penetrant diffusion and polymer relaxation proceeding at different relative rates according to the conditions of the experiment.

11.3.1. History-dependence

Crank (1953) explored the suggestion that part of the movement of the polymer molecules may be effectively instantaneous, and part relatively slow compared with the diffusion of penetrant. An increase in penetrant concentration is assumed to lead to an immediate increase in diffusion coefficient, followed by a slow drift towards an equilibrium value as a result of the relaxation proces characteristic of the glassy state. This means that the value of the diffusion coefficient in any element of the system depends on the concentration history of the element. We assume the surface concentration to be held constant and that the fast and slow changes in the diffusion coefficient proceed independently of each other. If the concentration changes infinitely rapidly then we can expect the instantaneous component Dx of the diffusion coefficient to satisfy

Di = DoeflC,

(11.2)

where C is the penetrant concentration and Do and a are constants. At a point that remains at a given concentration C the diffusion coefficient is assumed to increase further with time until a final equilibrium value De is obtained given by

De = DoebC,

(11.3)where b is larger than a. This approach to De is assumed to be a first-order change such that

^ = a(De-D),

(11.4)

where a is also a function of concentration given by a = aoeffC.

(11.5)

The over-al expression for the diffusion coefficient D becomes

ldD\ IdDA IdC

Calculations based on this equation produce sorption-desorption curves exhibiting many features of the sigmoid and psuedo-Fickian types of curves.

With five adjustable parameters available we must not expect to draw detailed

NON-FICK1AN DIFFUSION

259

conclusions from a comparison of calculated curves with experimental data.

Nevertheless, the orders of magnitude obtained were reasonable. This history-dependent model cannot explain two-stage behaviour which must indicate some influence of solubility.

11.3.2. Two-stage theories

We have seen in § 11.2(iii) that a good description of two-stage sorption is afforded by solutions of the concentration-dependent form of the diffusion equation with a time-dependent surface concentration satisfying eqn (11.1).

It is, however, unlikely in general that slow relaxation of the polymer is important only on the surface. In the history-dependent model, internal relaxation influenced only the diffusion coefficient. In the second stage of two-stage sorption the concentration is thought to be uniform throughout the sheet as in § 11.2(iii), and Newns (1956) has developed the other extreme hypothesis that internal relaxation influences only the solubility. Following Flory (1953), Newns considers that in the quasi-equilibrium at the end of the first stage the elastic forces in the swollen polymer network have increased the chemical potential of the sorbed penetrant to such an extent that no further sorption occurs. On standing, the elastic forces slowly relax, the chemical potential decreases, and more penetrant is absorbed to establish equilibrium again. This proces continues to a final, true equilibrium when the elastic forces have decayed away completely or reached equilibrium.

The hypothetical hydrostatic pressure n exerted by the polymer network at a time during the second stage when the concentration is Cq is given by

n = (RT/V)ln(p/pq)9

(11.7)

where V is the partial molar volume of the penetrant, the pressure p is the actual vapour pressure of the penetrant, and pq the pressure that would correspond to a concentration Cq if a final equilibrium had been reached.

The internal stres due to the presence of the penetrant is yAv, where Av is the fractional volume change and y an elastic constant. By balancing the opposing stresses Newns obtained an expression for the ratio of the amount sorbed during the first stage, to that at final equilibrium, and predicted correctly several features of the two-stage sorption curve.

Petropoulose and Roussis (1969b) obtained numerical solutions of eqn(10.94) (p.227) containing 'thermodynamic' parameters, and so incorporated relaxation effects both on the surface and in the body of the polymer.

11.3.3. Strain-dependent models

In §11.2(iv) evidence of internal stresses arising from the differential swelling of an outer swollen layer and an internal core of a sheet or filament was described. Attempts have been made to relate anomalous diffusion behaviour to these stresses.

260

NON-FICKIAN DIFFUSION

Crank (1953) assumed that only the diffusion coefficient is affected by the stresses and not the surface concentration or internal solubility. The essential features of the mathematical model are clear from Fig. 11.2. Sorption experiments (Park 1953) suggest that the cross-sectional area A of the sheet can be assumed to remain effectively constant throughout its thickness.

(a)

(b)

(c)

Q

Ao C

X

FIG. 11.2. From Crank 1953.

The diffusion coefficient in the unstressed polymer is approximated by the step-wise form in Fig. 11.2(c). The associated concentration distribution is shown in Fig. 11.2(b), where Co is the constant surface concentration. We assume the mechanical compression to be uniform in the region 0 < x < X,and that the stress-fre swelling in this region corresponds to that for a mean concentration ^ Co + Cx). The stress-fre swelling in the central core X <x < I is assumed zero. Internal stresses are assumed to have a negligible effect when X = /. The sheet is initially of area Ao and finally Ax, i.e. Al is the stress-fre swelling for a final uniform concentration Co. The increases in area are small, and so in the absence of stres they are taken to be proportional to mean concentrations. In the swollen region, 0 < x < X, the mean stress-fre area AM is given by

AM-A0 = (A1-A0)CJC09

when the mean concentration is CM. The compression is

(11.8)

At the stage shown in Fig. 11.2(a), the swollen region, 0 < x < X, is

NON-FICKIAN DIFFUSION

261

compressed by SAM and the dry region X < x < I extended by SA0. The assumption of constant area throughout the thicknes means that

A =A0 + SA0 = AM-SAM.

(11.9)

By equating total forces of compression and extension we obtain X0SA0{l-X)/A0 = lM5AMX/AM9

(11.10)where Ao and AM are Young's moduli for the dry and swollen polymer respectively. The diffusion coefficients are assumed to be related to SAM and SAoby

(11.11)D2 = D0(l+;ji 08A0/A0)9

(11.12)

where Dl and D2 are the diffusion coefficients in the swollen and dry regions when the area is A, Crank (1953) considerably simplified the mathematics by further assuming that the ratio of the diffusion coefficients for the fully compressed and unstressed states is the same for swollen and dry polymer regions. It then follows from (11.11) and (11.12) that DJD2 remains constant as diffusion proceeds and so

D = D(t)D(C).

(11.13)

Calculations based on this model reproduced an experimental sorption curve for methylene chloride in polystyrene and, to some extent, the change in area with time. The model also predicts qualitatively the experimental observation that in the early stages a thin sheet should absorb more penetrant than a thicker one. But according to the model, plots of MJM  ̂ against t*/l  should all coincide for different thicknesses /, and this is not true.

Another view of the effect of internal stresses has been discussed by Frisch, Wang, and Kwei (1969) and Wang, Kwei, and Frisch (1969). They include in the basic transport equation, in addition to the gradient of chemical potential, a second term deriving from the partial stres of the penetrant.

In this case, the thermodynamics of irreversible processes leads to an expression for the flux of penetrant

dx C dx

(11.14)

where B is a mobility coefficient, \i the chemical potential, and S the partial stress tensor in one dimension. On making the assumption that S is proportional to the total uptake of penetrant so that

S(x) = s I C(x/,r)dx/,

(11.15)

2 62

NON-FICKIAN DIFFUSION

where s is a constant, we arrive at the generalized diffusion equation dC d \

cC

}— = —\l>(C,x9t)- B(C,x9t)sC\.

(11.16)

dt dx {

dx

J

If the stres gradient predominates so that dji/dn « dS/dx, eqn (11.16) is seen to lead to Case II diffusion (§ 11.2(iv), p. 257). Wang et al. (1969) point out that the solution of the linear form of (11.16) (for which D and v = Bs are constants) for diffusion into a penetrant-fre semi-infinite medium x ^ 0, with x = 0 maintained at a constant concentration Co, is

(11.17,

When x is smal compared with vt, inspection of the function erfc reveals that the second term on the right side of (11.17) is much larger than the first.

Wang et al. therefore make the approximation that except for very smal t the movement of any plane X with a given concentration is such that

X = 2ky/(Dt) + vt9

(11.18)

where k is a constant. They then take an expression of this approximate form to describe the movement of the sharp boundary associated with a discontinuous diffusion coefficient (§ 13.2, p. 287). They apply Danckwerts' moving frames of reference (§ 13.4, p. 298) and obtain solutions of the linear form of(11.16) in which, of course, the sharp boundary moves according to (11.18).

Kwei, Wang, and Zupko (1972) find their model predicts successfully the rates of sorption and penetration of acetone in poly(vinyl chloride). The two special cases of D « v and D » v correspond to Fickian and Case II diffusion respectively.

Alfrey et al. (1966) used approximate mathematical models to calculate swelling stresses and fracturing in glassy-polymer discs and cylinders in which two-stage diffusion is occurring.

11.3.4. Irreversible thermodynamical model

Frisch (1964, 1966) has discussed diffusion in glassy polymers in the language of irreversible thermodynamics. In view of the many excellent general accounts of this subject which are available (de Groot 1961; de Groot and Mazur 1962; Prigogine 1967; Haase, 1969] we shal attempt only to convey the essence of Frisch's ideas in the simplest terms.

In addition to the usual thermodynamic variables such as concentration,temperature and pressure, Frisch introduces a set of unspecified internal parameters which are used to describe the gradual 'freezing' or relaxing of internal degrees of freedom as the system passes through a 'glass-like'transition region. Above the transition temperature the system is in internal

NON-FICKIA N DIFFUSION

263

chemical equilibrium with respect to these parameters, but below the

transition region it is not. Thus, the Gibbs free energy per unit mass G is a

function of the mass-fraction concentrations cj9 temperature T, pressure p,and the proposed internal parameters £a (a = 1, 2,..., N). Systems with a glass-like transition are defined to have a characteristic temperature T^cj9 p)such that dG/d£a = 0 for T > T  ̂but is not zero for all a when T < 7J.

Below T* these free energy derivatives depend on £a, which themselves depend on the history of the system as well as its composition, i.e. £a = £a(r, c,-, p)where t is time.

At constant T, p etc. the Gibbs-Duhem relation is given by

j

= ££«<Ua,

T<T^

(11.19)

where Aa = dG/d£a.

We discus the diffusion flux with respect to a mass-fixed section. A basic idea in irreversible thermodynamics is that the flux Jt of one component i depends not only on its own gradient of chemical potential but also on those of the other components in the system. Thus we write

Jt= t Lij xr

T > Tt>

(1 L 2 0)

7 = 0

where in the one-dimensional case the forces X} are given by Xj= -d/ij/dx.

(11.21)The Li} are the so-called Onsager coefficients and for T > T  ̂ they are functions of T, p, c} only, i.e. Li} = L{j{T,p, c). Correspondingly, we define

J,= t LtjXj9 T< 7J,

(11.22)

j = 0

but now Lij  are time-dependent since they are also functions of £a, i.e.

Lij  = L^T, p, Cj, 4). Reciprocal relations

L^Lj^ L^Lji,

(11.23)

are to be satisfied and also

£ •/ , = ().

i = 0

Following Frisch we consider as an example a two-component system in one dimension, with component 0 as the polymer and component 1, the penetrant. Thus q = 1, giving

Jo + Jj = 0, Loo = L01 - - L 1 0 = L n ,

(11.24)

264

NON-FICKIAN DIFFUSION

so that (11.20) and (11.22) with (11.21) become

d

ox

(11.25)In this example, we have only one independent concentration variable since c1 = l—c0. Thus, using (11.19),

OC1 C\ix

where

'tol-dtfrl—df;

{U21)

Finally, the diffusion flux is given by

= -Ddcjdx, T < T;,

(11.28)

where the diffusion coefficients are

T<7 .̂

(11.29)

Thus, even if there is no change of mechanism acros 7 ,̂ i.e. L n = L n ,D will differ from D and will be history-dependent.

Frisch (1964) developed the approach further in other reference frames and in a consideration of boundary conditions he showed that the time-dependent surface concentration observed experimentally by Long and Richman (see eqn (11.1) can be deduced.

11.4. Conclusion

No single one of the models discussed in (11.3) can account satisfactorily for all the known aspects of anomalous diffusion. A synthesizing model is

NON-FICKIA N DIFFUSION

265

still needed to include the combined effects of history, orientation, and stres on the diffusion proces within the polymer system and on the surface concentration. Furthermore, a composite model needs to be of such a form that it can be used to predict diffusion behaviour under given conditions and be useful for the interpretation of experimental data.

12

DIFFUSION IN HETEROGENEOUS MEDIA

12.1.

P R A C T I C AL materials are frequently heterogeneous in structure. We distinguish two types: particulates, in which discrete particles of one phase are dispersed in a continuum of another; and laminates, comprising layers of different properties sandwiched together. Barrer (1968) has reviewed some studies of both types.

12.2. Laminates

We consider some properties of laminates in which the layers A, B, C...

are normal to the direction of flow.

(i) Steady state. In the steady state, the flow through the ith lamina is the same as for any other lamina and is given by

F = -o)vrx-1DidCJdr,

(12.1)

where for a plane sheet, hollow cylinder, and spherical shell, v = 1,2, and 3 respectively and co/"1"1 is the surface area with â  = 1, a>2 = 2ft, and co3 = 4TC for unit area of a plane sheet, unit length of a cylinder, and for a whole spherical shell. If D, is independent of concentration, and the solubility is proportional to the pressure in all laminae, the integration of (12.1) with respect to r gives

F = j ^ ^ y

(12-2)

where ACt is the concentration drop acros the ith lamina and

The permeability is given by Pt = Z)^ where a{ is the solubility coefficient in the ith lamina, i.e. C{ = o^i and so (12.2) may be written

where Ap( is the pressure drop acros the ith lamina which would correspond

DIFFUSION IN HETEROGENEOUS MEDIA

267

to AC;. It follows immediately that

1JR^R}1 + IJR 1̂+ +IJ^RJ

=  — Z ^Pi = ~ ^p,

(12.4)

r i=  1

r

where Ap is the total pressure drop across the n-layer laminate. The over-al permeability P of the composite is defined by

P = W*nM.

(12.5)

ajAp

We arrive at the three formulae

L l2 ln I . . uxi+i+~+i=p>(slab);

In (R JR0) + \njRJRJ + + \n(RJRn^)  = ln (RJR0)p2

pn

( l / R p j - j l / R , )

( / J d / J

P

P

(spherical shell).

(12.6)

Here lt = Ri — Ri_1 and / = Rn — R0. Also on the left sides but not on the right of eqn (12.6) we may substitute P- = Dp  ̂ i =  1,2,..., n. The corresponding relationships between diffusion coefficients follow by putting o =  1 and hence P = D everywhere in (12.6).

Barrer (1968) draws attention to an important property of a laminate in which the diffusion coefficient of each lamina is a function of concentration,and the solubility of the diffusant is not proportional to the pressure. Integration of (12.1) now leads to

^AC| = i % ^ ,

(12.7)

where

D.-dC,

(12.7a)

in which A2i-i»^2i a re t n e values of Ct just within the two surfaces R(_x

268

DIFFUSION IN HETEROGENEOUS MEDIA

and Rt, Or- summation, (12//) becomes

Finally, we may define an overall integral diffusion coefficient for  the laminate D by the expression

— £ ACt = l^R*j R»\

(12,9)

F ^

D

The magnitude of the sum on the left side may depend on the sequence of the laminae. Ash, Bauer, and Palmer  (1965) have investigated the distributio n of concentration through the laminate in the case where each Dt is constant,and Henry s law holds in each lamina. In (12.2) above they substitute AC,- =I2i — ̂ 2i--15 where the Is are as used in (12.7a) above. Then we can writ e

F

i~1

— Ht = (A2l._1-A2l.) f l

fcr

(1 2 i° )

where

and where l2i — kik2i.v x and fe0 = 1. After  summing over  all values of i and re-arrangmg, we find

/ n

— OJVA1 2^ **(.

(12.12)

Also from (12.10) we find

^2i  = K

j = 0 I i = l

»=i

//

By integrating (12.1) from r to R^. x and re-arranging we see that

which can be rewritten by substituting for  l2i-i  fr° m the equivalent of(12.13) if need be.

(ii) Time lag. The time lag as defined in §4.3.3 (p. 51) for  a single lamina has also been calculated for  laminates by methods which avoid the need to obtain complete solutions of the transient diffusion equation. One of these is due to Jaeger (1950b) and employs Laplace transforms. He expresses the time lag in terms of eight subsidiary quantities related to certain determinants.

Four sets of boundary conditions are considered at the two outer  faces of

DIFFUSION IN HETEROGENEOUS MEDIA

269

the laminate:

(i) constant temperature, zero temperature;

(ii) constant heat flux, zero temperature;

(iii ) constant flux, zero flux;

(iv) temperature proportional to time, zero flux.

For each combination he tabulates numerical values for the time lag for heat flow through two different building walls each composed of six layers.

Barrie, Levine, Michaels, and Wong (1963) applied Jaeger's procedure to laminates AB and ABA. Ash, Barrer, and Petropoulos (1963) used Frisch's method described in § 10.6.2 (p. 222) to obtain time lags for repeated laminates ABAB.... Ash, Barrer, and Palmer (1965) deal also with the laminate ABCD...

and with composite hollow cylinders and spherical shells. Barrer (1968)quotes a number of the formulae for particular cases. They are all cumbersome and here we give only the general formula for the v-dimensional case derived by Ash et al. (1965).

(12.15)

Ash et al consider two special systems in more detail: (a) a lamina of substance B is inserted in a medium A and the position of B is varied; (b)the lamina B is inserted centrally in A and its thicknes varied. Results are presented graphically for plane sheets, cylinders and spheres. Kubin and Spacek (1967) consider an ABA type of plane membrane separating two compartments, each of the same finite volume, which contain solutions differing in concentrations of a common solute.

12.3. Disperse phase in a continuum

Holliday (1963) gives examples of practical systems made up of one continuous polymer phase and one dispersed phase. The following parameters are required to describe a composite material of this kind:

(i) The geometry of the dispersed phase (shape, size, and size distribution,concentration and its distribution, orientation, topology);

270

DIFFUSION IN HETEROGENEOUS MEDIA

(ii) the composition, state of matter, and other properties of both the disperse phase and the continuous phase.

Essentially the same mathematical equations describe the phenomena of electrical and heat conductivity, and the diffusion of penetrant. The many theoretical formulae that have been proposed to predict electrical and thermal properties of these composites are easily adapted to permeability studies.

Several authors have summarized some of the papers on the subject and given extensive lists of references. In this account, the methods described have been selected to represent the different types of mathematical approach that have met with some success in correlating experimental and theoretical results. For a formulation of diffusive flow in heterogeneous systems in terms of irreversible thermodynamics, we refer to Barrer (1968) and to Kedem and Katchalsky (1963), who consider multi-component systems and electrolytes.

12.4. The mathematical problem of a two-phase system

We consider a number of discrete particles of material A embedded in a continuous medium of material B. In general, the particles constituting phase A may vary in size and shape, and their distribution in the medium phase B may be random or regular both in respect of spacing, arrangement and orientation. We denote by Da and Db the diffusion coefficients, assumed constant, of materials A and B respectively and by Ca, Cb the corresponding concentrations. These are normally functions of three space variables,but not of time, when steady-state problems are being studied.

The steady-state concentration in each phase satisfies Laplace's equation

V2Cf = 0, i = a9b.

(12.16)The two conditions which the concentration must satisfy are that both the concentration and the flux of the diffusing substance must be continuous everywhere. In particular, on any surface separating two phases we have

Ca = Cb; Da dCJdn = Db dCJdn,

(12.17)

where d/dn denotes the directional derivative normal to the interface.

Conditions (12.17) hold over the whole surface of each of the particles constituting phase A. Additional boundary conditions will be specified over the outermost surface or surfaces of phase B, according to the nature of the problem under consideration. In stating (12.17) we have assumed that no contact resistance exists at the interface. The appropriate modification is easily made if necessary.

DIFFUSION IN HETEROGENEOUS MEDIA

271

12.4.1. Arrays of spheres, cylinders, and ellipsoids

Earlier workers investigated successively more complicated approximations to the general problem. The first paper usually quoted is by Maxwell(1873), who solved the problem of a suspension of spheres so sparsely distributed in the continuum that any interaction between them is negligible.

The volume fraction va of the dispersed phase is therefore small. By applying the conditions (12.17) to appropriate harmonic functions, he obtained an expression for the effective diffusion coefficient of the composite medium,which can be written in the form

D~Db =vf l f>f l " D '-

02.18)

The coefficient D is the diffusion coefficient of a hypothetical homogeneous medium exhibiting the same steady-state behaviour as the two-phase composite. Burger (1919) extended the treatment to ellipsoids and Eucken (1932)included particles of different sizes. Fricke (1931) derived an expression for spheroids suspended in a continuum which he expressed as a generalized form of Maxwell's equation (12.18), namely

D~°b = v . ^ V ^ - ,

(12.19)

D + xDb

where x is a function of DJDh and the ratio a/b is the ratio of the axis of symmetry of the spheroid to the other axis. For the case of spheres, x = 2,we have Maxwell's formula. In general

- ^ - - ^ - - ^

(12.20)

where

M(a <

and

T

3Ll+i M

(0-isin:

s in3 <j)

M(a > b) =

" (Da-Db)-pDb'

2

[DJ(Db1 sin2 (/>'

1 1)}  ' 1+(1-M){ J where cos </> =

1 c o s2 <f>'

2sinVn where cos 6' = b/a.

1 +

1 -

-a/b,

sin (j)'

sin cp'

The influence of the geometric factors of the suspended particles is expressed solely in the parameter /?.

272

DIFFUSION IN HETEROGENEOUS MEDIA

Fricke presented graphs of /? and x against DJDb for different values of a/b and concluded that for a constant volume concentration the diffusion coefficient of the suspension is independent of the size of the suspended particles, and also nearly independent of their form, when the difference between the diffusion coefficient of the two phases is not very large. This is especially true for suspensions of prolate spheroids (a > b) which have a smaller diffusion coefficient than the suspending medium.

Comparison with experimental data for the blood of a dog, for which the values Da = 0, b/a = 4-25, and x = 1-05 are considered appropriate, shows excellent agreement for volume concentrations ranging from 10 per cent to 90 per cent. On the other hand, Hamilton and Grosser (1962) attempted to correlate Fricke's expression (12.19) with experimental data relating to mixtures of rubber and particles of aluminium or balsa in the form of spheres, cylinders, parallelepipeds, or discs. They found that (12.19) predicts all the experimental data more satisfactorily if x is not calculated from (12.20),but from an empirical relationship

x + 1 = 3/tfr.

(12.21)

The sphericity of a particle if/ is defined as the ratio of the surface area of a sphere of volume equal to that of the particle, to the surface area of the particle. In these terms Fricke's values of x +1 would be 3/ij/2 for prolate ellipsoids and 3/I/J1'5 for oblate ellipsoids.

The general conclusion is that if the continuous phase has the higher diffusion coefficient there is littl e shape-effect. In the opposite case, a marked shape-effect is noticeable if the ratio of the diffusion coefficients exceeds 100,and the expression (12.19) with x given by (12.21) accounts satisfactorily for the variation over a wide range of variables.

Starting from solutions of Laplace's equation expressed in Legendre functions, Rayleigh (1892) obtained an improved approximation for identical spheres arrayed on a single cubic lattice. His work was developed further by Runge (1925) and de Vries (I952a,b) to include both body-centred and facecentred cubic lattices and cylinders.

Another way of stating the nature of Maxwell's approximation is that he assumed any one spherical particle to be embedded in a medium whose properties were those of pure phase B, unmodified by the presence of the spheres of phase A. Subsequently, other assumptions were made, notably that the surrounding properties are those of the equivalent homogeneous medium. Barrer (1968) quotes several references and formulae and a table from de Vries (1952a,/?) comparing calculated results for spheres by several authors. These are seen to be consistent only when DJDb is small. Barrer suggests that the formulae may account reasonably well for plastics containing impermeable filler particles, though the question of non-spherical shapes is not resolved. Higuchi and Higuchi (1960) discus a number of

DIFFUSION IN HETEROGENEOUS MEDIA

273

theoretical relationships for both steady and transient How, particularly in relation to pharmaceutical problems,

Keller (1963) obtained an asymptotic solution for a dense cubic array of spheres of infinite diffusivity embedded in a medium with diffusion coefficient D. His expression for the effective diffusion coefficient D00 is

D*/D = - ^ In ((TC/6) - / ) +• ...,

(12.22a)

with (n/6)—f « 1, where / is the volume fraction occupied by the spheres.

The singularity at / = n/6 occurs when the spheres touch each other. The corresponding result for a square array of cylinders is

— =

rr + ... ,

(1 2.22b)

D 2{(7i/4)--/p

with (n/4)—f « 1. Keller (1963) also established the following theorem. Let D00 and D° denote the effective diffusion coefficients of the two composite media obtained by imbedding in a medium of diffusivity D a square lattice of circular cylinders with diffusion coefficients oo and 0, respectively. Then

D°°/D - D/D°,

(12.23a)A similar theorem for a rectangular lattice relates D00 in the x-direction with D° in the y-direction. That theorem also holds for non-circular objects provided they are symmetric in the x- and >'~axes. It states that

D?/D = D/D°,

(12.23b)

where the subscripts x and y indicate the directions in which the effective coefficients are measured. Theorem (12.23a) holds for objects which are symmetric in the x- and y-axes and also in the 45° lines x = + y.

12.4,2. Series-parallel formulae

Some papers have explored the idea that neighbouring parts of a composite medium may be considered to be in series or parallel. We have seen in § 12,2(p. 267) that a laminate composed of n sheets of thicknesses ll912... /„  and diffusion coefficients DX,D2... Dn placed in series has an effective diffusion coefficient D, given by

L+k+ L--L

D. D2 "Dm D '

where / is the total thicknes of the laminate. The effective diffusion coefficient for a composite consisting of n sheets in parallel is given by

Both expressions are based on the assumption that the flow is uni-directional.

If it is not, the relationships are approximations.

274

DIFFUSION IN HETEROGENEOUS MEDIA

y / / /

/ / / 7~/ / // / / /

<

/

z

//

//////

v

(a)

_ J A C L _

L-VM— '

B(d)

AJ

\

10 B

t

+

T

101

(0

FIG. 12.1. Analytical conductivity is determined by considering the fluid-solid suspension as divided into cubes. (After Jefferson et al. 1958).

(i) Uniform spheres on a regular lattice. Jefferson, Witzell, and Sibbet

(1958) consider the composite medium to be divided into a number of cubes as in Fig. 12.1(a), each having a sphere of the discontinuous phase at its centre; Fig. 12.1(b) shows half a typical cube containing a hemisphere.

Jefferson et al. consider this to comprise the three components A, B, and C as in Fig. 12.1(c). The cylinder A has length and radius both equal to the radius of the sphere; the cylinder C has the same radius but its length is the difference between the side of the cube and the radius of the sphere; B is a hollow cylinder of length equal to half the side of the cube, outer diameter twice its length, and inner diameter that of the sphere. The three components are considered to form a series-parallel diffusion circuit, as in Fig. 12.1(d).

The underlying assumption is that the diffusion flow through the composite

DIFFUSION IN HETEROGENEOUS MEDIA

275

is everywhere uni-directional. This implies first, that the net flow through components A and C is the same; and second, that concentrations are constant over all planes perpendicular to the flow In particular, the concentration difference between the ends of B is the sum of the differences across A and C respectively.

In reality, these assumptions are not strictly true, even in the most favourable case of a plane sheet of composite material with opposite faces maintained at different concentrations so that flow would be uni-directional in a homogeneous sheet. In the composite, it will be two- or three-dimensional to an extent depending on the geometry of the discontinuous phase and its distribution, and the relative properties of the two phases. We present Jefferson et a/.'s treatment with slightly modified nomenclature. They were concerned with the corresponding thermal problem.

The diffusion flow through the composite model qs of Figs. 12.1(c) and

12.1 (d) is given by qs = qA + qB- Denote by DA, AA, /A the diffusion coefficient,cross-sectional area, and length of component A, and by ACA the concentration difference between its ends, with corresponding nomenclature for components B and C. Then

Since the total change in concentration acros the half cube is ACS, where ACS = ACA + ACC and also AA = Ac, we find

ACSAA

ACSAADAC

q

l + k '

where DAC is the equivalent diffusion coefficient of A and C taken together.

By considering A and C together in parallel with B we have for the total flow qs through the half-cube,

DA C &CSAA DB ACSAB

—r~n—+—/

'A + 'C

lB

(12.25)

where Ds is the effective diffusion coefficient for the whole system and As the cross-sectional area of the cubic element.

Remembering that /B = /A 4-/c, we have on substituting for DAC from(12.24)

If now we take the sphere to be of unit diameter and component C to be of

12.1(e), and by applying the series formulae similar to the first of (12.24) to a cylindrical element of A lying between r and r + Sr;

_ D A A A AC A _ r = °-5 2nAC A rdr

where D D is the diffusion coefficient of the spheres forming the discrete phase, and D c is already defined for component C which can be identified as the continuous phase.

Substituting x^ = (0-5) 2 -r 2 and x c = 0-5 -x D , and performing the integration we find

2D D D C f D D 7 A Be (12-28)

The parameter, n, is related to the volume fraction v D of the discontinuous phase by the expression n -0403v~1 /3 -0-5.

(12.29) Eqns (12.26), (12,27), (12.28), and (12.29), when combined, yield an expression for the effective diffusion coefficient of an array of uniform spheres arranged on a regular lattice in a continuum, in terms of their volume fraction and the diffusion properties of the two phases.

(ii) Random distribution of discrete phase, Tsao (1961) extended the use of the series-parallel formulae to composites in which the discontinuous phase consists of randomly distributed particles of irregular size and shape. A unit cube of such a composite is shown in Fig.  12 .2(a). It is assumed that the surfaces parallel to the xy« and xz~planes are sealed, so that the over-all direction of diffusion is along the x-axis. The shaded regions represent the discontinuous phase d and the rest is the continuous phase c. Tsao illustrates, by Fig.  12 .2(b), three porosity parameters. For a line in the cube parallel to the x-axis, the one-dimensional porosity P t is defined to be the fraction of the unit length occupied by the discrete phase. For a plane parallel to the yzplane in Fig.  12 .2(b), the two-dimensional porosity P 2 is defined as the fractional area occupied by phase d. Finally, the three-dimensional porosity F 3 is the volume fraction occupied by phase d.

Tsao slices the two-phase composite material into many thin layers, parallel to the yz-plane as in Fig.  12 .2(a). Each layer is so thin that P 2 may be

References

DIFFUSION IN HETEROGENEOUS MEDIA

277

(d)

A

X or Px

FIG. 12.2. From Tsao (1961).

assumed constant within it. Since both the parallel and series formulae are independent of the order in which the separate components are placed, we can re-arrange the elements of the discontinuous phase within each slice and then re-arrange the slices in any order we find convenient. All this assumes that the diffusion may be considered uni-directional in the x-direction. In this way Tsao proceeds through Fig. 12.2(c) to the arrangement of discrete

278

DIFFUSION IN HETEROGENEOUS MEDIA

phase shown in Fig. 12.2(d), in which there no longer exists any variation in the z-direction so that a unit cross-section, perpendicular to z, can be considered, as in Fig. 12.2(e). The slices have become infinitesimally thin to produce a smooth curve whose axes can conveniently be relabelled P{ and P2 as indicated. By applying the series-parallel formulae it is easy to show that the effective diffusion coefficient of the composite De is given by

(12.30)\ + (Dd-Dc)P2

In order to evaluate eqn (12.30), a functional relationship between Pt and P2 is needed.

Tsao assumed that the probability of any given length of discrete phase occurring along any line in the original composite followed the normal distribution curve. This means that the probability W{>P\) of the one-dimensional porosity being greater than P\ can be written

where \x is the mean and o the standard deviation of Pl. But the probability of P\ being exceeded along any line through the composite is equal to the fractional area occupied by the discrete phase for which the one-dimensional porosity equals P\. This is simply P2(P\) since we see from Fig. 12.2(e)that for all P2 less than this particular value, paths for which Px exceeds P\ exist.

Thus we may write

P2(Pi)= W(>Pi)

(12.32)

as defined in (12.31). Substitution from (12.32) for P2 in (12.30) gives an expression for the effective diffusion coefficient of the composite De in terms of Dd, Dc and the distribution parameters \i and o. Since

•J  o

(12.33)

it follows that the mean value // = P3 , the volume fraction of the discrete phase. Tsao decided that the standard deviation a of Pt had to be determined by experiment in addition to the volume fraction, in order to fix the two parameters \i and G in his probability function.

Cheng and Vachon (1969) applied Tsao's basic idea in a different way.

They re-arranged the particles of the discontinuous phase to form a centralized symmetrical area as in Fig. 12.3(a), which they then transformed to

DIFFUSIO N I N HETEROGENEOU S MEDI A

279

Discontinuous

phase

(a)

Discontinuous

phase

(b)

FIG. 12.3. Phase distributio n for a two-phase mixtur e as represented by: (a) the x-axis bisecting the square; (b) the x-axis coinciding with the lower  border of the square. (From Cheng and Vachon 1969).

Fig. 12.3(b) by dropping the x-axis to coincide with the lower edge of the square. Following Tsao, they assumed the discontinuous phase to be dispersed according to a normal distribution so that the curve in Fig. 12.3(b)is of the form

y=Clexp(-C2x2\

(12.34)where Cl and C2 are parameters. Having in mind that — \ ^ x < |, they neglected all higher terms in the expansion of the exponential function in(12.34) and wrote

y = B + Cx2.

(12.35)

From the symmetry of Fig. 12.3(a) we see that B =  -4 /C.

(12.36)

280

DIFFUSION IN HETEROGENEOUS MEDIA

Using (12.35) and (12.36) in the expression for the volume fraction,

rB/2

P3 = 2 ydx,

(12.37)

Jo

we find

B = V(3P3/2), C = -4V2/{V(3P3)} .

(12.38)By applying the series-parallel formulae to Fig. 12.3(b) and remembering that in Tsao's notation y = P2 and x = Pt , we find

1 CB/2 dP

l—B T.-2). B ^ B j T - sr

(1239)

P2 is expressed as a function of Pt from (12.35) using (12.38).

It is convenient to substitute

E = Dc - B(Dd - DG), F = C(Dd - Dc)

(12.40)

and so write two expressions for 1/De:

(a) Dc > Dd.

^ ,

(12.41)

( b ) D c < D d .

J_ -

1 in i v - ' 2-w - /i - -

(1242)

e V ^

In this case F is a negative quantity.

Since only one parameter P3 , the volume fraction, is needed to determine B and C through (12.38) it appears that Cheng and Vachon have removed the need to measure a second parameter experimentally as Tsao suggested.

What they have done is to specify one particular set of normal distributions by their assumption of symmetry in Fig. 12.3(a). In fact, in terms of B and C the normal distribution (12.34) is

y = B exp {Cx2/B\

which is identical with that used by Tsao to derive (12.31) if we identify x = Pi— \i and B/C = 2c2. The only difference is that Tsao normalized his integral by the factor l/(ayj2n), whereas Cheng and Vachon chose B = - 4 /C = (3P3/2)± Clearly they have also chosen a = iJ(3P3) by their method of rearranging the discontinuous phase in Figs. 12.3(a) and 12.3(b).

Cheng and Vachon suggest how their method can be applied to some three- and multi-phase systems for certain ratios of the diffusion coefficients

DIFFUSION IN HETEROGENEOUS MEDIA

281

of the component phases. They also compare results obtained by their own and other formulae with experimental data for two- and three-phase systems.

Fidelle and Kirk (1971) measured thermal conductivities of three different composites covering a broad range of filler concentration and heat conductivity ratios. The composites were carborundum plaster, alumina plaster, and alumina polyester. Over-all, the best predictor of their experimental data is the Cheng-Vachon formula. That theirs is better than the three-dimensional computer results obtained by Fidelle and Kirk (1971)perhaps suggests that the assumption that the spheres are on a regular lattice and not randomly distributed, as in Cheng and Vachon's treatment,is more serious than that of uni-directional flow. The uni-directional,approximate treatment has the advantage of leading to a simple explicit expression for the effective diffusion coefficient.

12.4.3. Numerical solutions

Several authors have obtained numerical solutions of Laplace's equation for a region in which identical uniform particles of one phase are arranged on a regular lattice in a continuum of a different phase.

(i) Fidelle and Kirk (1971) used finite-difference methods analogous to those described in Chapter 8 to compute numerical solutions for Jefferson's model of spherical particles § 12.4.2(i) (p. 274). They took account of the threedimensional nature of the problem but did not reproduce the spherical interfaces exactly. They used the best approximation possible with a rectangular grid of points.

(ii) Bell and Crank (1974) studied a regular two-dimensional array of identical, rectangular blocks, impenetrable by the diffusing substance, i.e.

having zero diffusion coefficient. They first showed that for any region with repeated symmetry, as in Fig. 12.4(a), it suffices to study the steady-state

yf' Z, ^ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ Zj

\\w\\\\\\\\\\v\

(a)

(b)

FIG. 12.4. (a) Aligned rectangular blocks, (b) Basic element.

282

DIFFUSIO N IN HETEROGENEOUS MEDI A

problem in a rectangular region with a re-entrant corner as in Fig. 12.4(b),provided the number of repeating basic units is an integer power of two.

The blocks need not be rectangular. The argument applies in general,provided symmetry is identified. A staggered arrangement, as in Fig. 12.5(a),can be studied by solving the problem for the rectangle with two re-entrant corners, as in Fig. 12.5(b).

o^\\\\\\\\\\\\\\\\\\\\ v

X'

(a)

(b)FIG. 12.5. (a) Staggered rectangular  blocks, (b) Basic element.

Bell and Crank obtained finite-difference solutions for the regions shown in Figs. 12.4(b) and 12.5(b). The singularities at the re-entrant corners (see§§ 8.10.2 and 8.12, pp. 153 and 159) were treated by the methods of Whiteman and Papamichael (1972). An alternative approach by Symm (1973) using integral equations and Green's functions produces the same results. Typical plots of concentration and flow-lines are given in Figs. 12.6 and 12.7. They confirm the approximate nature of the assumptions underlying the seriesparallel model (§ 12.4.2, p. 273). With reference to Figs. 12.4 and 12.5, the series-parallel (SP) expression for the effective diffusion coefficient De of the composite is

D =Dh

D

h + a(\-h)

(12.43)

where v is the volume fraction of the dispersed phase, given by v = (1 — h)o.

In order to derive (12.43) we sum infinitesimal strips perpendicular to the flow by a series formula, and the diffusion coefficient for each strip comes from the formula for diffusion resistances in parallel. Alternatively, we can obtain an approximation based on the summation of strips lying parallel to the flow

D I F F U S I ON IN H E T E R O G E N E O US MEDI A

283

FIG. 12.6. Lines of constant concentration.

FIG. 12.7. Flow lines (where F is the total flow through the region).

rather than acros it. For this problem we obtain the apparently trivial expression

De = Dh

(12.44)which, for convenience, we refer to as the parallel-series or PS approximation.

Fig. 12.8 shows how DJD varies with the 'window' width h and that the numerical solution lies between the SP and PS approximations. These and other calculated results, taken together with Keller's reciprocal relation(12.23b) led Bell and Crank to the general conclusion that for rectangular

oo

10

20

30

0-40 0-36

40

50

60

Window (per cent)

0-32 0-28 0-24 0-20 016 012 Volume fraction v = (l— h)o

80 008

90 100

• 100/z

004 000

FIG. 12.8.

284

DIFFUSION IN HETEROGENEOUS MEDIA

blocks with diffusion coefficient Dd in a continuum with coefficient Dc the effective diffusion coefficient depends primarily on 'window space' h, when Dd « Dc, and on block width a, when Dd » Dc. In passing, they quote results for the limiting case a = 0 of thin discs oriented normal to the flow.

Bell and Crank proposed an improved approximate expression, which is a weighted average of the SP and PS approximations,

,

(12.45)

where

0 = 0-56-0-5(7 + 04/z,

(12.46)

and DSP and Dps are the estimates produced by the SP and PS models.

Expression (12.45), with (12.46), gives values of De differing by only 2 per cent or 3 per cent from the numerical solutions for a range of block sizes and spacings for both the aligned and staggered arrangements.

(iii ) Keller and Sacks (1964) tabulated numerical values of DJD for a regular lattice of impermeable, uniform cylinders of various radii. They confirmed Keller's asymptotic solution (12.22b), adjusted by (12.23a).

Their results for cylinders of radius r agree with those of Bell and Crank

(1974) for square blocks of side 2<r, when suitable scaled so that they have the same cross-sectional area, i.e. r = la/yju. Thus, the geometric shape of the dispersed phase is not important when the areas are normalized, except when the blocks or cylinders are very close together. The weighted approximation(12.45) with (12.46) also represents satisfactorily the results of Keller and Sacks.

Baxley, Nicholas, and Couper (1968) tried a numerical-statistical approach to cope with randomly distributed particles of irregular shape. They considered that any two-phase system could be represented by a three-dimensional cubical system of smal cubes of each phase. Any irregular shaped particle can be built to any degree of approximation by arranging a sufficient number of smal cubes according to a predetermined plan. Also, elementary cubes of the discrete phase can be inserted into the continuum according to any specified statistical distribution. They simulated a two-phase system as a three-dimensional matrix in a computer. An IBM 7040 permitted 8 x 8 x 11 =704 elementary cubes and so the number of discrete phase cubes for a given volume fraction / was 704/ The heterogeneous system was built up in the computer by placing smal solid cubes in storage locations whose coordinates were determined by a constant-density random-number generator. Then a set of finite-difference equations for the composite was solved. The calculated results were compared with measured data for several liquid-solid and liquid-liquid systems. Unexpectedly, Jefferson's series-parallel approximation for spheres arranged on a regular lattice gave equally good results.

DIFFUSION IN HETEROGENEOUS MEDIA

285

In the light of more recent work by Bell and Crank (1973) on rectangular blocks, it could be that the corners of Baxley's cubes are one serious source of error and that the finite-difference representation needs to be improved.

13

MOVING BOUNDARIES

13.1. Introductio n

I  N one general class of problem some of the diffusing molecules are immobilized and prevented from taking further part in the diffusion process.

This may be due to a chemical reaction by which the diffusing molecules are either precipitated or form a new immobile chemical compound. Alternatively, we may have a less specific type of adsorption on fixed sites. We are concerned with immobilization processes which are irreversible, and so rapid compared with the rate of diffusion that they may be considered instantaneous. Only a limited number of molecules can be immobilized in a given volume of the medium. Examples are the diffusion of oxygen into muscle where oxygen combines with the lactic acid; the reaction of Cu2+ ions with CS2 groups as they diffuse in cellulose xanthate; and the diffusion of periodate ions into cellulose fibres and their removal by combination with the glucose groups of the cellulose. An essential feature of the idealized problem of diffusion accompanied by the instantaneous and irreversible immobilization of a limited number of the diffusing molecules is that a sharp boundary surface moves through the medium. It separates a region in which all the sites are occupied from one in which none of them are. In front of the advancing boundary the concentration of freely diffusing molecules is zero, while behind it immobilization is complete. Fig. 13.1 illustrates the situation. The same mathematical problem is presented by heat flow in a medium which undergoes a phase change at some fixed temperature, accompanied by the absorption or liberation of latent heat. Such problems are often referred to as

Empty

Distance

FIG. 13.1. Diffusion of particles which are trapped in immobile holes.

MOVIN G BOUNDARIES

287

'Stefan problems' after J. Stefan (1890). An excellent survey of the literature dating from that time is given by Muehlbauer and Sunderland (1965).

Bankoff (1964) has written a useful review article with numerous references.

Rubenstein's book (1971) gives a systematic presentation of the mathematical aspects of Stefan problems.

The occurence of a sharp boundary does not necessarily imply a chemical reaction. When a liquid penetrant diffuses into a polymer sheet or filament,sharp boundaries are frequently observed under a microscope. They correspond to near-discontinuities in the gradient of the concentration-distance curve (Hartley 1946). They imply discontinuous changes in the diffusion coefficient-concentration relationship and present the same mathematical problem. We consider both analytical and numerical methods of obtaining mathematical solutions.

13.2. Discontinuous diffusion coefficients

We shal first consider diffusion coefficients which change discontinuously from one constant value to another at certain concentrations. They may be zero or infinite over parts of the concentration range. Such coefficients provide examples of extreme types of concentration-dependence and are useful in that they enable limits to be set to the extent to which concentrationdependence of the diffusion coefficient can modify the course of diffusion as indicated, for example, by the shape of the concentration-distance curve.

Some special cases which do not require detailed calculation are considered first, and afterwards solutions are developed for more general cases.

13.2,1. Special cases not requiring detailed calculation

When the diffusion coefficient varies discontinuously with concentration in certain ways, the concentration-distance curves and the sorption- and desorption-time curves can be deduced by general reasoning from the known solutions for a constant diffusion coefficient. Some examples referring to uni-directional diffusion in a plane sheet are presented graphically in Figs. 13.2 and 13.3. These diagrams are largely self-explanatory and need only brief comments. The nomenclature is as follows: c is the concentration of diffusing substance at a distance x measured from the surface of the sheet in the direction of diffusion at time t, and D is the diffusion coefficient.

Also Mt is the total amount of diffusing substance absorbed by or desorbed from unit area of a plane sheet of thicknes / in time t. For sorption the sheet is initially free of diffusing substance and the surface is maintained at c = C1 throughout; for desorption the initial concentration is C{ throughout the sheet and the surface is maintained at zero concentration. In Fig. 13.2(a),over the concentration range Cj > c > Cx for which D is zero, the concentration gradient is infinite and there is no penetration into the sheet. The sorption

288

MOVING BOUNDARIES

(a)

D-c

C !

/C ]

(b)

r*-0O—H

Cx C,

(c)

Cx

(d)

/c,

FIG. 13.2. Sorption behaviour.

behaviour is identical with that for a constant diffusion coefficient Dx and surface concentration Cx, and the equilibrium total content of the sheet is ICX. When D is infinite over any finite interval of concentration at the upper end of the concentration range as in Fig. 13.2(b), the existence of a finite

concentration gradient anywhere in the range Cx > c > Cx would mean an infinite rate of transfer of diffusing substance. Consequently, the concentration must reach its final uniform value Cl throughout the sheet infinitely rapidly, and this is true whatever the form of the D against c curve at low

concentrations, even if D is zero. When D is infinite at low concentrations,

MOVIN G BOUNDARIE S

289

but drops to a constant finite value Dx at c = Cx (Fig. 13.2(c)), the sheet attains a uniform concentration Cx throughout, infinitely rapidly, and the remainder of the sorption behaviour is as for a constant diffusion coefficient Dx. The sorption behaviour is precisely the same for a diffusion coefficient which is infinite for intermediate concentrations and has a constant finite value at high concentrations, as in Fig. 13.2(d), whatever the form of D at low concentrations, again even if D is zero. The curves of Fig. 13.3 for desorption follow by similar arguments and need no comment.

D-c

c-xl(D,t)\

(a)

/c\

KCX-CX)

(b)

r--oo 1 C l F

/c\

/ (C.-Q)

(c)

(d)

Cy

C,

C,r

j

i

/ c

FIG. 13.3. Desorption behaviour.

290

MOVIN G BOUNDARIES

13.2.2. Diffusion coefficients having a discontinuity at one concentration

The more general cases in which the diffusion coefficient changes discontinuously from one constant finite value to another, at one or more concentrations, require detailed calculation. At the concentration at which a discontinuous change in D occurs there is also a discontinuity in the concentration gradient, and the way in which this moves has to be determined.

The problem can be stated mathematically as follows.

Suppose that diffusion takes place into a semi-infinite medium and that the surface x = 0 is maintained at a constant concentration Cx. We shal consider first a diffusion coefficient in which a discontinuity occurs at a concentration Cx. For concentrations less than Cx, D = D2, and for concentrations greater than CX,D = D{. Suppose that at time t the discontinuity in concentration gradient occurring at Cx is at x = X(t); this is a function of t which has to be determined. At time t, let the concentration in the region 0 < x < X be denoted by c1? and in the region x > X by c2. At the discontinuity, the concentrations cl,c2 must be the same, and also the mass of diffusing substance must be conserved, so we have

c,=c2 = Cx, x = X,

(13.1)

Dx dcjdx = D2 dc2/dx, x = X.

(13.2)

In the region 0 < x < X we have to satisfy dcjdt = D1 d2cjdx2,

0 < x < X,

(13.3)

and

Cl = Cj, x = 0.

(13.4)

In the region x > I w e must satisfy

dcjdt = D2 d2c2/dx\

x > X.

(13.5)Also we suppose the concentration to be C2 (constant) at large distances, i.e.

c2 = C2, x = oo.

(13.6)

The following method of solution of these equations is due to Neuman and is used by Carslaw and Jaeger (1959, p. 283) to deal with an analogous problem in heat flow when heat is evolved or absorbed at the boundary.

Neumann's method consists of writing down a particular solution of the differential equations and boundary conditions (13.1) to (13.6), and then seeing what initial condition this solution satisfies. The solution of (13.3)satisfying (13.4) is

M O V I N G B O U N D A R I ES

291

where A is a constant. Also if B is a constant,x

(13.8)

Then (13.1) requires

A erf—i = Cx — Cl,

(13.9)

and

Since (13.9) and (13.10) have to be satisfied for all values of f, X must be proportional to r*, say,

X = kt*9

(13.11)where k is a constant to be determined. Using throughout (13.7), (13.8),(13.9), (13.10), and (13.11) in (13.2) we obtain

Q-Ci cx-c2 _

+/(k/2Df)-U'

(U'U)

g(k/2Df)+/ /2Df)where g and / are functions given by

( m 3 )

When (13.12) is solved numerically, it gives k in terms of Cl 5 C2, C ,̂ and the diffusion coefficients Dx and D2. The numerical solution is greatly facilitated by using Figs. 13.4, 13.5 and 13.6 which show graphs o f / and g.

The same graphs were shown in Danckwerts's paper (1950/?).

Substituting fc = X/t* in (13.9) and (13.10), we obtain

Aerf-^j=Cx-Cl9

(13.15)

k

Berfc —-j = Q - C 2 ,

(13.16)

from which /I and B can be evaluated, knowing k, and hence the concentrations cx and c2 follow from (13.7) and (13.8). When t = 0,X =  0andc2 - C2.

This solution applies strictly only when the medium is semi-infinite, a condition which is effectively satisfied in the early stages of diffusion into a sheet of finite thickness. When the concentration at the centre of the sheet

292

MOVING BOUNDARIES

0

0-5 10 1-5 20 2-5 30

FIG. 13.4 f{k/2D\) for positive values of k/2D\.

— 2

- 4

- 6

- 10

- 1 0

-0-8

-0-6

- 0 - 4

- 0 - 2

kl(2D\)

FIG. 13.5. f(k/2D\) for negative values of k/2D\.

MOVIN G BOUNDARIE S

293

± kl(2D\)

FIG . 13.6. g as a function k/2D\.

becomes appreciable, this solution must be replaced by one in which the finiteness of the sheet is recognized. In general, it is necessary to continue the solution by numerical methods such as are discussed in Chapter 8.

In at least one interesting case, however, a formal solution is possible after the sheet has ceased to be semi-infinite. This is when the diffusion coefficient is zero at low concentrations, i.e. D2 = 0. Since this case can be solved completely without excessive labour, and as it is a limiting case of a diffusion coefficient which is smal at low concentrations and increases with concentration increasing, it justifies detailed consideration.

13.2.3. Diffusion coefficient zero for concentrations less than Cx and constant and finite above Cx

When D2 approaches zero, k/2D\ becomes large, and by applying the asymptotic expansion

1 / 1 1

\

(13.17)

(13.18)

to (13.14) eqn (13.12) reduces to

g(k/2D\) + cY-c2 = o.

Eqn (13.18) can be solved to give k and the solution follows from (13.7).

From (13.2), dcjdx -• oo when D2 -+ 0, unless dc1/dx = 0, which is the final steady state, and hence the concentration gradient is infinite at low concentrations. Examples of concentration curves, plotted against x/^Djt)* ,are shown in Fig. 13.7 for Cx = %Cl9\Cl9%Cl9 and \CX respectively, and

294

MOVING BOUNDARIES

10

0-75 -

0-50 -

0-25 -

00

0-2

0-4 .

0-6

0-8

JC/(4/V)*

FIG. 13.7. Concentration-distance curves for D as in Fig. 13.7(a). Numbers on curves are values

for C2 = 0 in each case. They also apply to the problem of diffusion with precipitation discussed by Hermans (1947), who gives a graph effectively of k/2D\ as a function of (Cx - CX)/(CX - C2), so that the root of (13.18) can be read off for any desired combination of values of C1,C2, and Cx. This is the graph shown in Fig. 13.6.

It is clear from the way in which the concentration-distance curves of Fig. 13.7 terminate abruptly that, from the time the vertical advancing front reaches the centre of a finite sheet, the diffusion coefficient is constant at Dx over the whole of the remaining concentration range. The solution required is thus the well-known one for diffusion into a plane sheet, with a constant diffusion coefficient and a given initial concentration distribution through the sheet. In the present nomenclature, the solution (4.16) given in§4.3.1 (p. 47) is

2/

2(-ir +1/C t

(x) sin

ax

(13.19)

MOVIN G BOUNDARIES

295

where the surface of the sheet x = 0 is maintained at Cx, the centre of the sheet is at x = /, and f(x) is the concentration distribution through the sheet at time t = t0. The total amount, M f , of diffusing substance present in half the sheet at time t is obtained by integrating the right-hand side of(13.19) with respect to x between the limits 0 and /, and is given by

M

°°

— i = 1+2

^ d x ^ ^ l <mo,

o /Cj

2/

(2n + l)27rj

In the present problem, f(x) is given by (13.7) evaluated at time f0, so that

(13.21)

where A is given by (13.9). The time t0 is defined as that at which X = /, so that it is related to the solution of (13.7) by the expression

(13.22)I2

By substituting in (13.20) from (13.21) and (13.22), MJICX is expressed as a function of the single variable D^t/l2. The integral in (13.20) is conveniently evaluated numerically. A family of curves showing MJlCl as a function of(D^/l2)^ is shown in Fig. 13.8 for several values of Cx including Cx = 0,when the solution is simply that for a diffusion coefficient having the constant value Dx. The linear parts of these curves follow readily from the solution(13.7) since we have

dMl=_lDid^l

AD*

and hence

/ c i

n c i \ * /

where A is given by (13.9) and is negative for sorption.

We may note that these curves, which are universal for all values of Dl9 are each linear at first, becoming concave downwards later though it might have been expected that they would show a different behaviour. Thus when the vertical front of a concentration-distance curve (Fig. 13.7) reaches the centre of the sheet, the region of zero diffusion coefficient is immediately removed and the subsequent sorption is governed by a constant and possibly high value of D, i.e. by D1. On these grounds it is not at first unreasonable to

296

MOVIN G BOUNDARIES

0-5

10 (D] ,/ /2)*  1-5

20

FIG. 13.8. Sorption curves for D as in Fig. 13.7(a). Numbers on curves are values of Cx/Cl.

expect the sorption to proceed more rapidly at this stage, i.e. for the gradient of a curve of Fig. 13.8 to be first constant and then to increase. Detailed calculation shows that this is not so, however, even for this limiting case of a discontinuous diffusion coefficient which is zero at low concentrations.

13.2.4. Diffusion coefficients having discontinuities at two concentrations

The above results can be extended to the case of a diffusion coefficient defined by

D = D l 5 C,> c> Q ,

(13.24)

D = D 2 , c<CY,

(13.25)

D = D 3 , Cx>c>CY.

(13.26)It is convenient to refer to this as a two-step diffusion coefficient. At the

MOVIN G BOUNDARIES

297

concentrations Cx and CY there are discontinuities in concentration gradient,and at each discontinuity conditions corresponding to (13.1) and (13.2) are to be satisfied. The method is so closely similar to that just described that the equations can be written down without explanation. Concentrations cx, c2,c3 are associated with the ranges in which the diffusion coefficient has the values DX,D2,D3 respectively. Then if A, B, and E are constants we have the following solutions:

<*1 -

?2 =

The conditions

c,

c2 cx

+ A erf-

+ £ erfc

+ £Jerf

c2

X

2(D2r)^'

X

2(D30*

= ^3 == C3 =

0 < x <

X

prf

•

•

• • c i 1

cx.

Cy,

> Y,

X(D3t)\

I

x =

X =

X,

L X < x < Y.

X,

Y,

(13.27)

(13.28)

(13.29)

(13.30)(13.31)

require that

^ '

( 1 3 3 2)

CY-C2 = £erfc

¥,

(13.33)

. Y „ X

from which it follows that

X = klt* 9 Y=k2t* 9

(13.35)where kl and k2 are constants to be determined. By using the two conditions Dx dcjdx = D3 dcjdx, x = X,

(13.36)

D2 dc2/dx = D3 dc3/dx, x = Y9

(13.37)and eqns (13.27), (13.28), (13.29), (13.32), (13.33), (13.34), and (13.35) we derive the following two equations from which to evaluate kx and k2.

Dt(Cy-Q)exp(-/c^/4D3) = ()

erf(fc^Df)

erf(/c2/2D|)

Dl(Cy-C2)exp(-^/4D2)

erfc(/c2/2D|)

erf(fc2/2Dt)-

Df(CyQ)exp(^/4D3)

rf f / t erfffc^D^) '

298

MOVIN G BOUNDARIES

Once kx and k2 are determined the whole solution follows as before, and it is easy to see that the same initial condition holds, namely, that the region x > 0 is at a uniform concentration C2. Eqns (13.38) and (13.39) can be solved numerically without excessive labour, but for any further extension to a threeor-more step diffusion coefficient the numerical work would probably be prohibitive. However, the two-step form includes several interesting types of diffusion coefficient and by suitable choice of D l 5 D 2 ,D3 and CX,CY a reasonable approximation to many continuously varying diffusion coefficients can be obtained. Some results for two-step diffusion coefficients are discussed in Chapter 9.

13.3. Immobilizin g reaction

The concentration plots in Fig. 13.7 have the form of Fig. 13.1. If we interpret C in §§ 13.2.2 and 13.2.3 to be the total concentration of molecules, i.e.

both freely diffusing and immobilized, then Cx in (13.18) with C2 = 0, can be identified as the concentration of the immobilized component. In order that the front can advance a distance 3X we need to supply an amount Cx SX of diffusant. The amount arriving at X in a time interval 5t is —DlSt dC/dx.

Conservation at the moving boundary therefore requires

-D{dC/dx = CxdX/dt.

If this condition is substituted for (13.2) when D2 = 0, we finally regain (13.18).

In the case of heat flow Cx becomes Lpx where L is the latent heat and px the density of medium 1. Thus, a problem in diffusion with immobilization can be thought of formally as a concentration-dependent diffusion proces in which D is zero when the total concentration C is in the range 0 ^ C < Cx and changes discontinuously to a finite value at C = Cx.

13.4. General problem of the moving boundary

We give now Danckwert's (19506) treatment of the more general problem in which a moving interface is involved. In all the cases considered the two regions are separated by a plane surface and diffusion takes place only in the direction perpendicular to this plane. The concentration is initially uniform in each region. The proces of diffusion may cause changes which bring about the disappearance or appearance of matter at the interface in one or both regions, and hence a resulting bodily movement of the matter in one or both regions relative to the interface. An example which is easy to visualize is afforded by the melting of ice in contact with water; as heat (here regarded as the diffusing substance) flows from water to ice, ice disappears and water appears at the interface, so that both ice and water are in bodily movement with respect to the interface. In all the cases considered the rates of bodily

MOVING BOUNDARIES

299

motion of the matter in the two regions with respect to the interface are directly proportional to each other, e.g. the volume of ice melted is proportional to the volume of water formed. Variations in specific volume or partial specific volume due to changes in concentration (or temperature) are ignored.

The solutions derived below do not apply to systems in which convection currents are important or in which gradients of both concentration and temperature exist.

13.4.1. The problem

Consider two media which are free from convection currents but which

may be in relative bodily motion along the x-axis, which is perpendicular

to the interface. Position in medium 1 is specified by a coordinate in the

x t system which is stationary with respect to medium 1; position in medium 2 by a coordinate in the x2 system, stationary with respect to medium 2.

The media are separated at time t by the plane xx = Xx, x2 = X2, which is initiall y at xl = x2 = 0. Medium 1 occupies all or part of the space X1 <xx < oo, medium 2 all or part of the space — oo < x2 < X2 (Fig. 13.9).

x2= ac x2=0 x-0 xa = X2

FIG. 13.9.

In both media there is a substance which moves by diffusion relative to the Xj and x2 coordinates and is transferred from one medium to the other.

The concentration of the diffusing substance at time t is denoted by cx at xx and by c2 at x2. The following equations are obeyed in the two media,

dcjdt = Dxd2cjdx\,

dc2/dt = D2d2c2/dx22,

(13.40)(13.41)

300

MOVIN G BOUNDARIES

where the diffusion coefficients D1 and D2 are assumed to be independent of At any lime the concentrations c^XJ, c2{X2) at either side of the interface are assumed to be related by an equilibrium expression

c2(X2) = Qc1(X1) + R,

(13.42)where Q and R are constants, e.g. for  the absorption of a gas obeying Henry's law, Q is the solubility of the gas and R = 0. The diffusing substance is conserved at the interface so that

(13.43)We have already said that there is constant proportionalit y between the rates of movement of the two media relative to the interface and hence it follows that

X2 = PX1,

(13.44)

where P is a constant determined by the conditions of the problem and may in some cases be zero.

We now proceed to build up solutions of these equations by what is essentially the same method as was used earlier  for  discontinuous diffusion coefficients, leaving til l later  an examination of the various ways in which the initial and boundary conditions can be specified.

Consider an infinite medium in which eqn (13.40) holds. Then a solution takes the form

C ( Q O )" C l

^ ,

(13.45)where c?i(oc) and ct(0) are given by the initia l and boundary conditions, i.e.

c, = Cl(oo),

Xl > 0, t = 0,

(13.46)

cx = cx(0), x, = 0, t > 0.

(13.47)

Similarly, the solution of (13.41) for  corresponding conditions c2 = c2(-oo), x2 < 0, t = 0,

(13.48)

c2 - c2(0),

x2 = 0, t > 0,

(13.49)

is

For the same conditions, the total amounts of diffusing substance, Vl and

M O V I N G B O U N D A R I ES

301

V2, crossing the planes xx = 0, x2 = 0 respectively in time t in the direction oi decreasing x are

(13.51)V2 = 2{c2(0)-c2(-x)}(D 2r/7c)*.

(13.52)

The solutions (13.45) and (13.50) apply to an infinite medium. Each can be applied equally well to a region bounded by one or two x-planes either stationary or moving, provided that (i) the initial concentration at every point in this restricted region is the same as for the same value of xx or x2 in the infinite medium; and (ii) the concentration at the boundary plane or planes is at all times the same as for the same value of Xj or x2 in the infinite medium. The problems to be discussed here concern media bounded by one or two planes, but they fulfi l the above conditions and so the solutions for infinite media can be used. In other words we shal show that the solutions(13.45) and (13.50) are compatible with (i) eqns (13.42), (13.43), (13.44) and(ii) the conditions determined by the data of the problem which may be of one of two kinds described below as Class A and Class B. It should be noted that the values of cl outside medium 1 and of c2 outside medium 2 have no physical significance.

I3o4o2. Problems of Class A

Here the movement of one or both media relative to the boundary is caused by the transfer of diffusing substance acros the interface. The conditions are that two of the quantities c^oo), cx(0), c^X^, c2( — x ) , c2(0) are specified and also that the magnitudes of Xx and X2 are at all times proportional to the amount of diffusing substance which has crossed the interface(xl = Xl9 x2 = X2). Hence we may write

dt= S<D,dx

dt

(13.53)

where S is a constant of proportionality characteristic of the system and is the ratio of the magnitude of Xx to the amount of diffusing substance which has crossed the interface in the direction of decreasing x. Combining this with (13.43) and (13.44) we have

9 — .~ ~~,,

, „ . — ,,

(13.54)

dt

Substituting (13.42), (13.44), (13.45), and (13.50) in (13.53) and (13.54) we find

df S

— ) e x p ( - X ' / 4 D1 r ) . (13.55)nt

302

MOVING BOUNDARIES

! ( * , » = {c2(0)-C2(-0O)}7Cfexp(-P2Xj/4D2t).

Also from (13.45), putting xt = Xl,cl = c^XJ, we have

c1(X 1) = c1(0)+{c 1(oo)-c1(0)}erf2>/(D10J"

(13.56)

(13.57)

It is clear that (13.55), (13.56), and (13.57) can simultaneously be satisfied for all values of f, if and only if Xl/ti is constant. Put

)*,

(13.58)

(13.59)

(13.60)

so that (13.55), (13.56), and (13.57) become respectively

= n*<x\^ —

c2(0)-c2(c») = K*a|^- --PR-PQc^XMexp c,(*,) = Ci(0)+ {c^ooJ-c^O)}  erf a,

(13.61)while substituting x2 = X2 in (13.50) and using (13.58) and (13.44) gives

c 2(0)-c 2(-oo )

D

(13.62)

Eqns (13.59) to (13.62) are independent and contain, besides physical constants and the parameters R and S, the six quantities cx(0), c^oo), c2(0),c2( — oo), c^{Xx\ and a. Hence if two of the concentrations are given, the four equations can be solved for the other three and a, and the concentrations cx and c2 follow as functions of x and t from (13.45) and (13.50). The expressions so obtained for cl and c2 satisfy both the initial and boundary conditions of the problem and the equation of diffusion, and therefore constitute the required solution. Substitution for a in (13.58) gives X1, and hence X2 from(13.44), in terms of t and known quantities. Finally we notice that the concentrations c^Xj) and c2{X2) at the interface are necessarily constant from(13.61) and (13.42).

13.4.3. Problems of Class B

Here the movements of the media on either side of the interface are not related to the amount of diffusing substance which has crossed the interface by eqns (13.53) and (13.54). Instead, three of the five concentrations

Cj(O), c^X^, c2(0), c2(— oo) are specified.

M O V I N G B O U N D A R I ES

303

Substituting (13.42), (13.44), (13.45), and (13.50) into (13.43) gives

{^(ooJ-MO)}

nt

+ {c2(0) - c2( - oo)}  RM 2 exp ( - P2X2/4D2t)

+ ^ d T { ( 1 ~ P 0 C l ( X l ) ~ p ^ } = a

(13>63)

Taken with (13.57) this can only be true for all values oft x'iXJt  ̂ is constant.

On putting

Xx = 2pt*,

(13.64)

(13.63) becomes

From(13.57)

+P{WcAX,) = c,(

n

PQ)

0) +

'exP(- j52

c^XJ-PF

tcAco)-c,

IDX)

exp(-P

J}  = 0.

2/D2)

(0)}erf(B/Dt),

(13.65)

(13.66)

while from (13.42) and (13.50)

c2(Xi) = Qc^XJ + R = c2(0)H-{c2(0)-c2(-oo)}erf(Pj8/Dj). (13.67)

Eqns (13.65), (13.66), and (13.67) are independent and so, since three of the five concentrations c^oo), cx{Xx\ c^O), c2(0), c2( — oo) are known, the values of the other two and of /? can be determined. Hence Xx can be found as a function of t from (13.64), and cx and c2 as functions of x and f from (13.45)and (13.50).

13.4.4. Examples of Class A problems

(i) Absorption by a liquid of a single component from a mixture of gases.

An ideal mixture of a soluble gas A and an insoluble gas is in contact with a liquid. Let the gas be medium 1 and the liquid medium 2. Initially the mole fraction of A in the gas is c^oo) and the concentration of dissolved A in the liquid, expressed as volume of gas per unit volume of liquid, is uniform and equal to c2( — oo); c^oo) and c2( — oo) are given. There is always equilibrium between the gas and the liquid at the interface, where Henry's law is assumed to be obeyed. It is further assumed that there is no appreciable change in the partial volume or temperature of the liquid when A is absorbed, and also

304

MOVIN G BOUNDARIES

that the diffusion of A in the liquid obeys the simple diffusion equation (13.41).

If the origin of the xx system of coordinates moves so that there is no mass flow of the gaseous mixture acros any plane of constant x2, then eqn(13.40) is obeyed in the gas. For this to be so, X1 must be equal at all times to the volume of component A absorbed by unit area of the liquid surface, i.e.

Xl = V. Thus the conditions of the problem correspond to those specified for Class A problems, with S = 1 in eqns (13.53) and (13.54).

The x2 coordinate of the liquid surface does not change, and hence X2 = 0,c2(X2) = c2(0) for all f; in equation (13.44), P = 0. Eqn (13.42) becomes

R = 0, c2(X2) = c2(0) = Qcx(Xx\

where Q is the solubility of A in the liquid expressed as volume of gaseous A in unit volume of liquid per unit mole fraction of A in the gas. Making the appropriate substitutions and eliminating the unknowns except a, eqns(13.59), (13.60), and (13.61) reduce to

-*— 1—

= 7cTa exp (a2) erfc a = /(a), (13.68)

OL(UD1/D2)'-Q + C2(-oo)

and putting Xl = Kin (13.58) gives

V= 2a(D1t)±.

(13.69)The function / has already been shown in Figs. 13.4 and 13.5 and, using these curves, a is readily evaluated from (13.68) by trial and error for known values of D t , D2, Q, c^oo), and c2( — oo). The rate V at which A is absorbed by the liquid follows immediately from (13.69). It is also easy to show that

( 1 3.7 0)

erfc a

2(0^

c2 = e^i(^ i) + {2c 1(X 1) - c2( -aD) }e r f ^ - ) T .

(13.72)

The same equations may be used for the escape of dissolved gas A from solution. In this case a will be negative and the amount of A leaving the solution in time Ms —V.

For further discussion of the physical conditions under which these solutions are applicable, Danckwerts's original paper (1950b) should be consulted.

A special case arises when c^XJ, the concentration at the interface, is determined by some factor other than diffusion in a liquid. Examples quoted by Danckwerts are the isothermal evaporation of a liquid into still air, when

MOVIN G BOUNDARIES

305

c^/YJ is determined by vapour pressure, and the sorption of a gas by a liquid which is rapidly stirred without deforming the surface, so that Qc^X  ̂ =c2( — oc). For such cases it is easy to show that (13,59) and (13.61) become

(13-73)

where /(a) and a have the same significance as before.

(ii) Tarnishing reactions. A film of tarnish is formed on the surface of a metal by reaction with a gas. The reaction proceeds by diffusion of dissolved gas through the film to the surface of the metal, where its concentration cx(Xx) is assumed to be zero, i.e. the reaction is assumed to be so rapid that the rate of tarnishing is controlled entirely by the diffusion process. The outer surface of the film is constantly saturated with the gas.

Let the film be medium 1. Since c^X^) is not determined by diffusion in another medium, eqns (13.60) and (13.62) are not required. Let Wbe the mass fraction of the gaseous component in the compound which it forms with the metal, p the density of this compound (which is assumed independent of the concentration of the dissolved gas), and cx the concentration of the dissolved gas (expressed as mass of gas per unit volume of the film) at a distance xx beneath the surface of the film. The outer surface of the film is at xx = 0, the metal surface at xx = Xx, the film thicknes being X1. From (13.53)

S = -l(Wp).

(13.74)Furthermore, since c^XY) = 0, ^(0), the saturated concentration of gas at the outer surface of the film, is given by

^ = 7r-aexp(a2)erfa = g(a),

(13.75)

Wp

from (13.59) and (13.61), and

)*,

(13.76)

where Dx is the diffusion coefficient of the dissolved gas in the film. Fig. 13.6 gives g as a function of a, and so values of a corresponding to given values of c^OyiWp) can be read directly from that graph and used to calculate film thickness as a function of time from (13.76). If ct(0) « Wp, expansion of exp(a2) and erf a shows that g = 2a2 approximately and therefore in this case

X, =2Dxcx(Q)t

Wp

(13.77)This means that, if the solubility of the gas in the film is sufficiently small, the film thicknes is given without appreciable error by the formula obtained by

assuming that the concentration gradient in the film is uniform. The problem of tarnishing was also solved by  Booth (1948)  who points out that the form (13.77) is a good approximation for systems usually encountered in practice.

13.4.5. Examples of Class B problems

13.4.5. Examples of Class B problems

(i) Solution of gas in a liquid, followed by reaction with a solute. The surface of the liquid is constantly saturated with the gas B, which is assumed to be undiluted with inert gases. The liquid contains a solute A which effectively reacts instantaneously and irreversibly with the dissolved gas. Diffusion of both A and B is assumed to obey the simple diffusion equation of the types (13.40) and (13.41). Any part of the liquid will contain A or B but not both. There will be a plane, x x = X 1 ,x 2 = X 2 , at which the concentrations of both A and B will be zero. That part of the liquid containing A is taken to be medium 1, that containing B is medium 2. The surface of the liquid is permanently at x x = x 2 = 0, so that X l = X 2 and P = 1 from eqn (13.44). Also

c l {X 1 ) = c 2 (X 2 ) = 0 9 (13.78)

and hence R = 0 in eqn (13.42). We assume n x moles of A to react with n 2 moles of B and so, in order to fulfil the conservation condition (13.43), we put c 1 = -m l n 2 /n l , where m l is the concentration of A at x x in moles per unit volume and c 2 the concentration of B at x 2 in the same units. Further, c 2 (0) is the saturated concentration of B at the surface of the liquid, and m^oo) the initial concentration of A in the liquid. Eqns (13.65) and (13.67) then become n 1 c 2 (0)/(i8/Dt)-«2'w 1 (oo)g(i5/D|) = 0, (13.79)

where / and g are the functions of p/D\ and /?/Df given respectively, as functions of a, in eqns (13.68) and (13.75) and plotted in Figs. 13.4, 13.5, and 13.6. Hence from (13.52) and (13.67) we find the volume of gaseous B absorbed in time t to be given by

V = 2c 2 (0) (13.80)

The value of /? can be found from (13.79) by trial and error, using  Figs. 13.4, 13.5, and 13.6, and substituted in eqn (13.80 ) to obtain V. This problem is also treated by  Hermans (1947) . If the gas is diluted by an insoluble component, the surface concentration c 2 (0) of B in the liquid is determined by diffusion in the gas. In this case, in order to obtain an exact solution, (13.69) and (13.73) must be used together with (13.79) and (13.80). A value of the concentration at the surface of the liquid must be found by trial and error such that the rate of absorption is the same when calculated from either set of equations. The quantities D l9 c^oo), and c^X^) in (13.69) and (13.73) refer respectively to the diffusion

References

MOVIN G BOUNDARIES

307

coefficient of B in the gas and to the mole fractions of B in the bulk of the gas and at the interface.

(ii) Progressive freezing of a liquid. The solution to this problem, given previously by Carslaw and Jaeger (1959), assumes that no change of volume occurs on freezing. The present equations take such a volume change into account. Suppose liquid initially occupies the region x > 0 and that freezing proceeds progressively, due to the removal of heat from the surface, x = 0,which is maintained at a constant temperature To. Subsequently, let the liquid be medium 1, and the solid, medium 2. Since no material crosses the surface maintained at To this corresponds always to x2 = 0. If there is a volume change on freezing there is relative movement of the planes x1 = 0andx2 = 0.

The diffuser in this case is heat. Take L to be the latent heat of fusion per unit mass, p j , p2 t n e densities, al, o2 the specific heats, and Dx, D2 the thermal diffusivities of liquid and solid respectively. The variation of these quantities with temperature is ignored. If Kl,K2 are the thermal conductivities of the liquid and solid respectively, then

Dx = KJfaaJ;

D2 = K2/(p2a2).

(13.81)

The temperature of the liquid is initially 7^ throughout and the solidliquid interface (xx = Xl,x2 = X2) is always at the melting-point Tx.

The heat content of the solid at Tx is taken to be zero, and hence that of the liquid at Tx is L. In this problem, concentration signifies the heat content,and hence, since c2(X2) = 0, we have from (13.42)

cl(Xl) = -R/Q = L/Pl.

(13.82)

Since XJX2 = p2/px, it follows from (13.44) that P = Pi/p2-

(13.83)

We also have

ci =Pi*i(T l-Tx + L/<r l),

(13.84)

c2 = p2o2{T2-Tx),

(13.85)

where Tx is the temperature at xA in the liquid and T2 the temperature at x2 in the solid.

Eliminating Cj(0) and c2{ — oo) from (13.65) to (13.67) and substituting equations (13.81) to (13.85) we find

where / and g are the functions plotted with a as variable in Figs. 13.4, 13.5,and 13.6. The thicknes of the solid formed up to time t is X2, where

(13.87)

308

MOVIN G B O U N D A R I ES

The temperature at any point in the solid is T2, where

T2 = T , - ( r , - 70 | l - e r f { p M p Z ) ! ) j J,

(13.88)

while in the liquid it is Tx, where

Hence if (13.86) is solved by trial and error using Figs. 13.4, 13.5, and 13.6,the resulting value of /? can be used to calculate the thicknes of the solid and the temperatures at any point as functions of time. The equations apply also,with suitable changes of nomenclature, to the melting of a solid which is at a uniform temperature.

It should be noted that a practical system only behaves in the way described by the above equations provided the density is uniform or increases steadily in a downward direction; otherwise convection currents arise.

13.5. Radially symmetric phase growth

We refer here to a particular problem with radial symmetry for which analytical solutions are easily found. A spherical or cylindrical new phase is growing from a negligible radius in an initially uniform medium and equilibrium conditions are maintained at the growing surface. Frank (1950)presents mathematical solutions earlier developed by Rieck (see Huber 1939).

Other relevant papers by Ivantsov (1947), Zener (1949), and Horvay and Cahn

(1961) include the growth of cylinders, paraboloids, and ellipsoids.

Following Frank we denote concentration (or temperature) by 4> and write

(13.90)

where r is the radial coordinate and s is defined by

s = r/{Dt)*.

(13.91)

Then the usual diffusion equation for spherical symmetry becomes

0=-£+?M.

(13.92)

Putting d(j)/ds = p and integrating, we have

d(j)/ds= -As-2Qxp(-\s2)

(13.93)

and hence

4> = A\ z -2exp( - ^z2)dz + (/>00,

(13.94)

MOVIN G BOUNDARIES

309

where 0^ is the value of <j>  at infinity and / l i sa constant. Integration by parts yields

0 - ^ = A{s~l

= AF3(s), say.

(13.95)

Tables and graphs of F3(s) are given by Frank (1950).

The total flux of diffusant over a sphere of radius R = SiDrf is

/ S\

-4nR2D(d(t)/dr)r = R = AnAD^t  ̂ exp - —

(13.96)

using (13.95) and (13.91).

Frank takes q to be the amount of diffusant expelled per unit volume of new phase formed as growing proceeds and assumes the boundary condition.

= q2nS3Dh  ̂

(13.97)

so that

S2

A = \qS3 exp

(13.98)Also, on the surface of the growing sphere, radius S, cj) has the constant value

= qf*(S)+ </>«>,  say.

(13.99)

Frank (1950) tabulates the function /3(S), and shows graphs of 5 as a function

of (</>s — 0oo)3/^ f° r t n e spherical, cylindrical, and linear cases.

For the two-dimensional, cylindrical growth Frank obtains the corresponding solutions

d(j)/ds = -As~l exp ( - is2) ,

(13.100)

<t>-<t>*=-2A

- - i / 4 Ei ( - i s2) = ylF2(s),

(13.101)

where Ei is the exponential integral to be found in standard mathematical tables.

Frank tabulates F2(s). Using the same type of boundary condition as(13.97) we find

A = \qS2 exp (iS2),

310

MOVIN G BOUNDARIES

and so on the surface of the growing cylinder of radius 5, </> has the constant value

(f)s=  - i<yS2exp( iS2)Ei(- iS2) + </>x

= ^/2(S) + 0x -

(13.102)

We note that in the linear case

/1(S) = -|Sexp(iS2)F1(S)

(13.103)

and

Fx{s) = 7r^erfc(|s).

(13.104)

Readers should consult Frank's paper (1950) for related problems which include the cases in which both heat and moisture control phase growth,and where two dissolved substances diffuse independently to form the new phase.

Reiss and La Mer (1950) studied the growth of mono-dispersed aerosols and hydrosols. Their mathematical solutions assume that the flux of material through any surface in the diffusion field is much greater than the rate of change of concentration on that surface.

13.6. Approximate analytic solutions

Formal mathematical solutions have only been obtained for a limited number of problems, mostly in infinite or semi-infinite media. In other cases,for example when the surface concentration varies with time, or the medium is in the form of a cylinder or sphere, or the diffusion coefficient is concentration-dependent, some approximation must be made or a numerical procedure adopted.

13.6.1. Steady-state approximation

Stefan (1891) and Hill  (1928) assumed that the concentration distribution behind the moving boundary approximated at any instant to the steady-state distribution which would be set up if the boundary were fixed in its position at that instant. We illustrate this approach with the following problem.

The surface of a semi-infinite sheet of uniform material is in contact with a well-stirred solution of extent /, and the solute diffuses into the sheet which is initiall y free of solute. The sheet contains S sites per unit volume, on each of which one diffusing molecule can be instantaneously and irreversibly immobilized. The concentration in the solution is always uniform and is initially CB expressed as the number of molecules per unit volume of solution. The concentration at any time just within the surface of the sheet is taken to be that in the solution. We denote by C(x, t) the concentration of freely diffusing molecules at any point x in the sheet at time t expressed in molecules per unit

MOVIN G BOUNDARIE S

311

volume. The concentrat ion of immobilized molecules is zero if C is zero and equal to S when C is non-zero. If we assume the diffusion coefficient D to be constant, the one-dimensional equation

is to be solved subject to C

idC/dt =SdX/dt =

dt l

= 0, t =

D dC/dx,-DdC/dx,

1 dx2

0,

X X

X >

= 0,

= x,

o,

r ^ O ,t > 0.

(13.105)

(13.106)

(13.107)

(13.108)

Here X(r) is the value of x at which C = 0, and denotes the position of the moving boundary. Condition (13.107) expresses the conservation of solute at the surface and (13.108) is derived in § 13.3 (p. 298).

Denote by Cx(i) the value of C at the surface and throughout the wellstirred solution at time t. Thus Cx(r) = CB when t = 0 and decreases as diffusion proceeds. When the advancing boundary is at x = X(t) the quasisteady state is given by

C = CX?-^.

(13.109)

A

On differentiating (13.109) and substituting in (13.107) and (13.108) we find

and

Eliminating Cx from (13.110) and (13.111), integrating the result and using the initial condition that

Q = CB, X = 0,

(13.112)

we find

Substitution for Cx in (13.111), followed by integration, yields Dt

CB {SX

I2

S \IC

- + ln i Hic,

312

MOVIN G BOUNDARIE S

From (13.114) we find X(t) and Cx(t), and then C(x, t) follows from (13.109).

Crank (1957b) gave corresponding approximations for the cylinder and sphere. By comparison with accurate solutions obtained by the numerical procedures of § 13.7 he concluded that when S/CB exceeds 10, the steady-state approximations are good enough for most practical purposes. Thus when S/CB = 10, the approximated position of the moving boundary is in error by about 1 per cent and by about 3 per cent when S/CB = 5.

Improved approximations starting from the steady state solution have been derived by Stefan (1891), Pekeris and Slichter (1939), and Kreith and Romie (1955).

13.6.2. Goodman's integral method

In an approximate method, Goodman (1958) also postulates a concentration profile behind the moving boundary, though not necessarily the steadystate one. It usually takes the form of a polynomial which is made to satisfy all the boundary conditions. It satisfies also an integrated form of the diffusion equation. The position of the moving boundary emerges as the solution of an ordinary differential equation with time as the independent variable. A review of integral methods and some applications are given by Goodman(1964).

We illustrate the procedure by applying it to the problem of the preceeding section, in the particular case of Cx constant. We integrate (13.105) with respect to x from x = 0 to X and use (13.108) to give

where o = S/D, and we have interchanged the order of integration and differentiation. The concentration profile is assumed to have the form

C = a(x-X) + b(x-X)2

(13.116)where a, b are constants to be determined from the boundary conditions and X = X(t). The condition

C = 0, x = X(t)9 t^0,

(13.117)

is satisfied. We also need

C = d = constant; x = 0, t ^ 0.

(13.118)The condition (13.108) is not very convenient as it stands, and so we first differentiate (13.117) with respect to t and obtain

MOVIN G BOUNDARIE S

313

Elimination of dX/dt between (13.108) and (13.119) with use of (13.105)gives

IdC 2

i dx

x = X(t).

(13.120)

dt

dx2'

By substituting (13.118) and (13.120) in the profile (13.116) we find, after some manipulation

a = ^ { i _ ( i + / i ) ± } , b = ^ ^ ,

(13.121)

where // = 2Cl/(aD).

Finally, we use the profile (13.116), with a and b from (13.121), in (13.115)to obtain an ordinary differential equation for X(t). Its solution which satisfies X(0) = 0 is

X = <xt* 9

*-*{*%$$}•

In principle, the method can be applied to a variety of boundary conditions and geometric shapes. Goodman (1964) and Crank and Gupta (1972a)show how additional boundary conditions can be generated by successive differentiation in order to determine successive coefficients in higher-order polynomial profiles. Poots (1962b) has applied integral methods to cylinders and spheres.

Only isolated attempts have been made to extend the integral method to more than one space dimension. There are obvious difficulties in the choice of the profile of the moving boundary. Poots (1962a) obtained a solution of the problem of the solidification of a long bar of square cross-section which compared moderately well with the numerical solution of Allen and Severn(1962). Pleshanov (1962) used a quadratic polynomial for the approximate temperature profile in bodies symmetric in one, two or three dimensions.

Budhia and Kreith (1973) studied melting in a wedge.

13.7. Finite-difference methods

Several numerical methods based on the finite-difference replacements of the diffusion equation described in Chapter 8 have been proposed. They differ in the way they treat the moving boundary and the grid on which numerical values are calculated. In general, the moving boundary will not coincide with a grid line in successive time steps St if we take St to be constant and predetermined. Douglas and Gallie (1955) chose each St iteratively so that the boundary always moved from one grid line to the neighbouring one in an interval St. This means that successive time intervals are of different durations.

314

MOVIN G BOUNDARIES

Crank (1957a) proposed two methods: the first fixes the boundary by a change of the space variable; the second uses special finite-difference formulae based on Lagrangian interpolation for unequal intervals in the neighbourhood of the moving boundary, in order to track its progres between grid lines. Ehrlich (1958) employed Taylor's expansions in time and space near the boundary. Murray and Landis (1959) deformed the grid so that the number of space intervals between the moving boundary and an outer surface remained constant, with suitable transformation of the diffusion equation.

Crank and Gupta (1972a, b) developed several procedures in which the grid is moved with the velocity of the boundary. A recent method (Chernous'ko 1969, 1970; Dix and Cizek 1970) of handling the diffusion equation, which offers a special advantage in Stefan problems, interchanges the concentration and space variables so that x becomes the dependent, and C and t the independent variables. If the boundary is known to occur at a fixed concentration its position comes naturally from the solution without special treatment.

Lazaridis (1970) has extended finite difference methods to two- and threedimensional corner? An alternative approach is mentioned by Crank (1974).

13.7.1. Fixing the boundary

Crank (1957a) obtained numerical solutions for the problem posed in§ 13.6.1 (p. 310) by using two transformations: (i) to remove the singularity at x = 0, t = 0 and (ii) to fix the advancing boundary. The conservation condition (13.107) was used in the integrated form

C = CB-\ f (C + S)dx, x = 0, r ^ 0 .

(13.123)

/ Jo

The singularity is handled by use of the new variables

c = C/CB, s = S/CB, f = x/(Dtf, T = (Dt/a2f, (13.124)when the relevant equations are

d2c dc dc

2—^ = ! — - £ — ,

(13.125)

c = 0, i = oc, T = 0,

(13.126)

1 d£x 1 I8c\ 6,~i^T = ~ b d + ̂ >

T > 0 '

(13.127)

2 dr ST\d^jx 2T

where £x = X/(Dt)* is the position of the moving boundary in the transformed variables. Also

c = 0, I > ix, T > 0 ,

(13.128)

while (13.123) becomes

a Ci

= l — -

/ Jo

(13.129)

M O V I N G B O U N D A R I ES

315

When T = 0, these equations have an analytical solution for 0 ^ £ ^ ix,c = l+flerf(££),

which satisfies c = 1, £ = 0, T = 0. The constants B and £x are determined from (13.127) and (13.128) with T = 0, since

l + B e r f ^ ) = 0

(13.130)

and

= 2/s.

(13.131)

(13.132)

The function on the left-side of (13.131) is plotted in Fig. 13.6.

We now fix the moving boundary by writing

Essentially the same transformation was used previously by Landau (1950)in a consideration of ablating slabs in which the melt is continuously and immediately removed from the surface. Citron (1960) extended the treatment to include temperature-dependent thermal properties. Sanders (1960)obtained an analytical solution for a particular specified motion of the free boundary.f

Using (13.132) in the present problem we obtain

T- , 0 < rj  < 1,

(13.133)

3c*   ̂

'

(13.134)

2 dt ST x̂\drjJl 2T'

a f1

c = l — - (c + sk Ŷdw, *7 = 0,

(13.135)

I Jo

when we have used (dc/drj)l to mean {dc/dr])n=1. The problem is now that of finding values of £x and (dc/drj)1 which are mutually consistent with (13.134)and for which the solution of (13.133) satisfies (13.135). Crank (1957a, b) used a convenient iterative finite-difference scheme to obtain numerical solutions for a plane sheet, cylinder and sphere in which the fraction s = S/CB, i.e. the ratio of the number of sites per unit volume to the number of molecules in unit volume of solution, takes the values 1, 2, 5, 10. For each value of s, solutions were obtained for an unlimited amount of solute, and for two restricted amounts chosen such that in the final equilibrium state respectively 50 per cent and 90 per cent of the solute has entered the medium. For each s, A/na2 is calculated from the expression for the fraction of the total amount of solute

t Spalding and Gibson (1971) coupled this transformation with the idea of a 'penetration distance' (see § 7.3, p. 129) in an economized finite-difference procedure for solving concentration-dependent and other non-linear diffusion problems.

316

MOVIN G BOUNDARIE S

finally in the cylinder, for example, which is

1+s

where a is the radius of the cylinder and A the cross-sectional area of the solution in which the cylinder is immersed. Table 13.1 show values of (Dt/a2)^at which the total uptake is |, \, |, expressed as a fraction of its equilibrium value. Tables 13.2 and 13.3 show values of (Dt/a2)  ̂at which the advancing boundary is ̂ , -|, and \ of the way towards the centre. The time at which the centre itself is reached are shown only for the plane sheet as they are difficult to determine accurately for the cylinder and sphere.

Meadley (1971) considered the back diffusion of solute in a layer of solution when the free surface recedes due to evaporation of the solvent. He fixed the receding surface by a transformation essentially the same as (13.132).

13.7.2. Diffusion on both sides of a moving boundary

For the problem considered in § 13.7.1, the total concentration falls to zero at the advancing boundary, c.f. Fig. 13.7. A more general problem arises when diffusion occurs on both sides of the boundary, as in the example of § 13.2.2(p. 290). We can still use the transformations of § 13.7.1 to fix the boundary,as long as the sheet is behaving semi-infinitely, i.e. the concentration at the centre of the sheet has not changed to within the accuracy of the calculations.

After that, Crank (1957a) proposed either to use two transformations to fix  both the moving boundary and the central plane of the sheet or to employ Lagrangian interpolation formulae to track the boundary. The second approach is described in the next section.

13.7.3. Lagrange interpolation

We return to the x, t plane and develop finite-difference approximations to derivatives based on functional values which are not necessarily equally spaced in the argument. They are generalized forms of the formulae developed in Chapter 8.

The Lagrangian interpolation formula is

/(* ) = t lJLx)f("j)>

(13136)

where

//* ) = , P"\X),, ,,

(13-137)

(x-a})pn(aj)

Pn(x) = (x-ao)(*-fli ) •(*-«,,-!)(*-«„ )

(13.138)and p'n(aj) is its derivative with respect to x, at x = a}. We restrict attention to

MOVING BOUNDARIES

317

three-point formulae, i.e. n = 2, and find that Id2/(x)

f(a0) , f(ax)

2 dx2 (ao-a1)(ao-a2) {a1-a0){a1-a2)

{a2-a0)(a2-a1)

and

dx

(13.139)

(13.140)

where

and

lo\x) —7

7 7 7 >

(ao-a1)(ao-a2)

x -ao){al -a2)

(x-ao) + (>

{a2-a0)(a2-al)

(13.141)

We apply these formulae in the neighbourhood of the moving boundary.

Taking the plane sheet as an example, we consider it to comprise M layers each of thicknes dx, and let the boundary x = X at time t be somewhere in the (m+ l)th layer (Fig. 13.10). Thus X = (m + p)dx where p is fractional and 0 < p < 1. If for x < X we identify

= cm_i, f{al) = cm, f{a2) = cX9

(13.142)

then (13.139) and (13.140) become

x = mSx (13.143)

dx

pdx

m — 2 m—\

m+1

a0 a,

FIG. 13.10.

m + 2 a2

318

MOVIN G BOUNDARIE S

and

Similarly for x > X we have

3x2 (Sx)2\(l-p)(2-p)

l - p ' 2 - p j '

and

= (m+l)dx, (13.145)

We use these formulae for the space derivatives together with the usual explicit or implicit replacements of time derivatives (see Chapter 8) in the diffusion equation itself, and in the conditions on the moving boundary x = X. For points other than mSx, X and (m+ l)dx, we use the usual finitedifference formula developed in Chapter 8 for equal intervals, including any condition on x = 0.

13.7.4. Moving grid system

Crank and Gupta (1972a) dealt with a moving-boundary problem arising from the diffusion of oxygen in absorbing tissue by using Lagrangian-type formulae and a Taylor series near the boundary. Subsequently (19726) they developed an alternative method based on a moving grid.

In the physical problem, oxygen is allowed to diffuse into a medium, and some of the oxygen is absorbed, thereby being removed from the diffusion process. The oxygen concentration at the surface of the medium is maintained constant. This first phase of the problem continues until a steady state is reached, in which the oxygen does not penetrate any further into the medium.

The surface is then sealed so that no further oxygen passes in or out. The medium continues to absorb the available oxygen already in it, and consequently the boundary marking the furthest depth of penetration recedes towards the sealed surface.

The diffusion-with-absorption proces is represented by the equation

where C{X9 T) denotes the concentration of the oxygen free to diffuse at a distance X from the outer surface at time T; D is the diffusion constant; and m, the rate of consumption of oxygen per unit volume of the medium, is also assumed constant. The problem has two parts:

MOVIN G BOUNDARIE S

319

(i) Steady-state. During the initial phase, when oxygen is entering through the surface, the boundary condition there is

C = C0, X = 0, T ^ O,

(13.148)where Co is constant. A steady-state is ultimately achieved, in which dC/dT = 0 everywhere, when both the concentration and its space derivative are zero at a point X = Xo. No oxygen diffuses beyond this point, and we have C = dC/dX = 0, X^X0.

(13.149)

The required solution in the steady state is easily found to be C = ̂ (X-X0)\

(13.150)

where Xo = ^(IDCJm).

(ii) Moving-boundary problem. After the surface has been sealed, the point of zero concentration, originally at X = Xo, recedes towards X = 0. This second phase of the problem can be expressed in terms of the variables

x

by the equations

X

DT

| = 0-i. •

dc/dx = 0, x c = dc/dx = 0, x c = U\-x)\

0

t

= 0,

= xB(0,

^ x ^ 1

D

nX\

xB(

>

= 0,

t I t

c2C0

= 0.

(13.152)

(13.153)

(13.154)

(13.155)

The surface is sealed at t = 0 and xB(f) denotes the position of the moving boundary in the reduced space variable.

An approximate analytical solution can be used to get away from the singularity at x = 0, t = 0 due to the instantaneous sealing of the surface. In the range 0 ^ t ^ 0020, the expression

(13.156)

is sufficiently accurate for most purposes. During this time the boundary has not moved to within the accuracy of the calculations. Once the boundary begins to move, a grid system can be used, moving with the velocity of the moving boundary (Crank and Gupta 1972b). This has the effect of transferring

320

MOVING BOUNDARIES

the unequal space interval from the neighbourhood of the moving boundary to the sealed surface. An improved degree of smoothnes in the calculated motion of the boundary was obtained compared with the results of using Lagrange interpolation.

We divide the region 0 ^ x ^ 1 into n intervals each of width Ax such that xt = i Ax; i = 0,1,... n and n Ax = 1. We denote by c{ the values of c at(i Ax, j At), j = 0, 1,2,... We start at t = 0 with the steady-state solution(13.155). In the first interval At we evaluate cln_ t , and also the new position of the boundary, which has moved from x = 1 to x = 1 — E, say, as in Fig. 13.11.

/ =0

1

1 11

i

£1

£

X n-2

£

A-n- i j!

i

1 I i*

l £

S

x=0

x=\

FIG. 13.11. Moving grid. (From Crank and Gupta \912b).

The whole grid is now moved a distance s to the left, as indicated by the broken

lines. We wish to evaluate values of c° and the second space derivatives at

each of the points x x — e, x2 — E, ..., xn _ x — e, 1 — e, at t = 0. Crank and Gupta

(19726) describe two methods of doing this. In the first method, interpolations are based on cubic splines, and a tridiagonal set of algebraic equations needs to be solved for each step in time. The second method, which we shal

describe, is based on polynomial approximations and is simpler to apply.

In return, we lose some of the continuity which the splines secure.

We represent c(x) at any time between the two points xf, xi + x by

=  a

where a = a(j, /+ 1), etc. We employ the usual expressions

C (•';

Ci - i

^-C\  1 ^ 1 + 1

.

* ~

dx2

(Ax)2

and at the surface x = 0,

c2c0 2

(13.157)

(13.158)

(13.159)

where c = xt — x0. At x = xl9 the Lagrangian type formula is used to allow

MOVIN G BOUNDARIE S

321

for the unequal interval c, namely

From (13.157) we obtain

(13.161)

where c' — d2c/dx2. Assuming the function values to be known at any time j At, when the distance of the moving boundary from the surface x = 0 is^' + rAx, the method proceeds as follows. Obtain the second derivatives at each point of the grid at time 7 At, using the relations (13.158) and (13.159).

By inserting ci,ci+l ,c"i,c"i+l  into (13.157) and (13.161), we derive the coefficients a, /?, y, //, and hence determine the interpolating polynomial (13.157)for each interval xt to xi+l .

The value of c j+ 1, i.e. at the point neighbouring the moving boundary and time (7+I) At, follows from the simple explicit relationship:

{c")l-l,

(13.162)where (c"){ denotes the value of c" at xr at j At. The Taylor's series for cr obtained by expanding about the moving point can be written as

cr = c(x0)-l\-dc\

,Jd2c

dx:

+ ..., (13.163)

where /(O ^ / ^ Ax) is the distance of the moving boundary from xr. We can derive the extra derivatives by differentiating (13.154) with respect to t,i.e.

dc Idc

df  = \dx

dx_ _i_x=x dr

dc

~dt=  0x = xn

(13.164)

Using (13.152) and (13.154) in (13.164) we obtain d2c/dx2 = 1, x = x0.

(13.165)

Similarly, by further differentiation we find

d3c/dx3 = -dxB/dr, x = xB.

(13.166)Provided the boundary is not moving too quickly we can use the Taylor series to obtain approximately

/ = V(2cr).

(13.167)Therefore, once cjr+l  is known from (13.162) we find the position of the moving boundary from (13.167). Hence its movement t;j+  * in the interval from j At to (7+I) At is given by

£;+ 1 = Ax- / ' " M .

(13.168)

322

MOVING BOUNDARIES

Having got e we then interpolate the values of c(x) and c"(x) at t = j At at the points xt -£, x2 —e,..., xn — e using (13.157) and (13.161). The values of c(x) at the new points x{, x2... xr at time (j+  I) At follow at once from

cj+]

)-c\x{-

remembering that

together with

At

v ' 7 '

K{  + 1 = x{-t-j+ \

i = l ,2 . . . , r,

co ~co

(13.169)

At= c"(xo)-l,

x = 0.

(13.170)

We have seen that the space interval xl — x0 varies from one time step to the next. As we proceed in steps At we eventually find that the points x0 and x t come so close together that the values of c there are not significantly different,to the accuracy of calculating. We then replace £ by <J + Ax to get values at the next time step and proceed as before.

Crank and Gupta showed that their solutions obtained by the different numerical procedures were in reasonable agreement. Furthermore, a slightly modified form of Goodman's integral method shows that quite good approximations are provided by the following analytic expressions:

x B ( r ) = 1 - e xp < - 2tx-t\*t-u

c(x, x0) =

x

(13.171)

(13.172)

(13.173)

These solutions are applicable only for the time interval t0 ^ f ^ t{ where t0 = 4/25n and tx =  TC/16. For t ^ t0, the approximate solution for smal times (13.156) holds and from (13.171) tx is seen to be the total time for the concentration everywhere to become zero.

An alternative form of moving grid was used by Murray and Landis(1959). They kept the number of space intervals between x = 0 and x = X constant and equal to n, say. Thus (5x = X(t)/n is different in each time step.

They differentiated partially with respect to time r, following a given grid point instead of at constant x. We have for the point i<5x

dx4

(13.174)

Murray and Landis assumed a general grid point at x to move with velocity

MOVIN G BOUNDARIES

323

dx/dr, where

Then eqn (13.152) become

1 dx

x dt

1 dX~X ~dd'

xt dX dc

~X~dt"!x'

d2c

(13.175)

(13.176)

Finite-difference solutions can be obtained when dX/dt is determined by an appropriate boundary condition. The idea implicit in (13.174) can be applied to any moving grid. If it moves bodily, as assumed by Crank and Gupta, all grid points have the same velocity, dX/dt, the relation (13.175) is not needed and the xJX factor in (13.176) becomes unity.

13.7.5. Isotherm migration method

The aim of all the methods described so far has been to determine how the concentration at a given point changes with time. An alternative method was proposed by Chernous'ko (1969, 1970) and independently by Dix and Cizek(1970). It has a particular advantage where phase changes are involved, and so we describe it in this chapter, though its use is not confined to moving boundary problems. In this method, the way in which a fixed temperature moves through the medium is calculated. Hence it is referred to as the 'isotherm migration method'. In the diffusion analogy we trace the motion of contours of constant concentration.

When a phase change or other boundary occurs at a prescribed temperature,its motion emerges naturally from the solution without any special treatment.

Also the need to evaluate temperature or concentration-dependent parameters at each time step is avoided. The appropriate values are simply carried along with the isotherm. These advantages are partly offset by some increase in complexity of the finite-difference equations and difficulties with some boundary conditions.

Instead of expressing concentration C as a function of x and t, we now rewrite the equations so that x becomes a function of C and t. The dependent variable becomes x(C, t) instead of C(x, t). We note that with reference to the diffusion equation in one dimension we can write

dC

since for C held constant

dx dC

=

<dC

Jx~

dx

dt

dx +dCdtdf

dC dt

= 0

del

324

MOVIN G BOUNDARIES

Starting from the usual diffusion equation

ct dx

and using the above relations we find

dC IdxMdx]-1 S/Sx^1

ldx\-3d2x

i.e.

dx\

dt= DdC dC2'

(13.178)

If we consider, as an example, the simplest form of the problem in § 13.6.1.

(p. 310) in which the condition (13.107) on x = 0 is replaced by

C = Co = constant, x = 0, t ^ 0,

(13.179)

then we can rewrite the condition (13.108) on the moving boundary

'

c = 0 '

f ^ 0 '

( m 8 0 )

remembering that we took C = 0 on x = X(t). The condition (13.179) becomes

x = 0, C = C0, t^0.

(13.181)

In order to start the solution we need to use an analytic or approximate solution suitable for smal times. This provides values of x for equally spaced values of C at a given smal time t from which we can proceed in steps St to obtain values of x on a grid in the C, t-plane by applying the usual finite-difference formulae to the transformed equations.

If we let x" be the value of x at C = i3C, t = nSt, we find the diffusion equation (13.178) becomes approximately

x;.' + i = x? + 4 3 f f 7 A

' l:1} ,

(13.182)

and from (13.180) we have

DdtSC

Crank and Phahle (1973) obtained results by this method, for the problem of melting a block of ice, that agreed well with the exact analytical solution and with solutions obtained by Goodman's integral method and Lagrangian interpolation.

MOVIN G BOUNDARIES

325

13.8. Other  methods

Methods based on applications of Green's functions lead to integrodifferential equations for the position of the phase interface. Short descriptions of these and other methods including Boley's (1961) fictitious boundary conditions or imbedding' techniques, and the variational methods of Biot(1970) and Biot and Daughaday (1962) are given by BankofT (1964) and Goodman (1964), together with references to other papers.

Fox (1974) has written an extensive survey in a book which also contains accounts of new research and of practical problems.

14

DIFFUSION AND CHEMICAL REACTION

14.1. Introductio n

T H E problem discussed in this chapter is that of the absorption of one substance by another through which it can diffuse and with which it can also react chemically. This can be regarded as a problem in diffusion in which some of the diffusing substance becomes immobilized as diffusion proceeds, or as a problem in chemical kinetics in which the rate of reaction depends on the rate of supply of one of the reactants by diffusion. There are numerous practical examples of processes involving simultaneous diffusion and chemical reaction of one sort or another. Thus diffusion may take place within the pores of a solid body which can absorb some of the diffusing substance, or we may have diffusion occurring through a gel and an immobile product resulting from the attraction of the diffusing molecules to fixed sites within the medium. Examples involving diffusion into living cells and microorganisms can be cited from biology and biochemistry. In contrast with the sharp boundary problems of Chapter 13, here we assume that some unoccupied reacting sites are always available. Chemical reactions in high polymer substances are often considerably dependent on the mobility of the reactants as well as on the kinetics of the reaction itself.

14.2. Instantaneous reaction

If the reaction by which the immobilized reactant is formed proceeds very rapidly compared with the diffusion process, local equilibrium can be assumed to exist between the free and immobilized components of the diffusing substance. In the simplest case, the concentration S of immobilized substance is directly proportional to the concentration C of substance free to diffuse, i.e.

S = RC.

(14.1)

In the particular case of diffusion with adsorption on to internal surfaces or sites (14.1) is referred to as a linear adsorption isotherm.

When diffusion is accompanied by absorption, the usual equation for diffusion in one dimension has to be modified to allow for this, and becomes

dC _ d2C dS dt

dx2 dt'

DIFFUSIO N AND CHEMICA L REACTIO N

327

if the diffusion coefficient D is constant. On substituting for S from (14.1) we have

dt R + l dx2

which is seen to be the usual form of equation for diffusion governed by a diffusion coefficient given by D/(R +1). Clearly the effect of the instantaneous reaction is to slow down the diffusion process. Thus if R + 1 = 100, the overal proces of diffusion with reaction is slower than the simple diffusion proces alone by a hundredfold. In fact, if the linear relationship (14.1) holds, solutions of the diffusion-with-reaction problem for given initial and boundary conditions are the same as for the corresponding problem in simple diffusion,except that the modified diffusion coefficient D/(R +1) is to be used. This is true irrespective of whether the diffusion-with-reaction occurs in a plane sheet, cylinder, or sphere, or any other geometric shape, and whether diffusion occurs in one dimension or more.

14.2.1. Non-linear isotherm

If the relationship between S and C is not linear but is of the form

S = RC\

(14.4)

for example, where R and n are constants, then (14.2) still holds, but (14.3)becomes non-linear and solutions of the diffusion-with-reaction problem in this case can only be obtained by numerical methods of integration such as those described in Chapter 8. Some numerical solutions have been obtained(Crank 1948/?, Crank and Godson 1947) describing the uptake of a restricted amount of solute by a cylinder, when diffusion within the cylinder is accompanied by adsorption and where the concentrations of free and adsorbed solute are related by an equation such as (14.4). In this example, 90 per cent of the total amount of solute is taken up by the cylinder in the final equilibrium state. Figs. 14.1 and 14.2 show the effect of the exponent n on the over-al rate of uptake of solute and on the way in which it is distributed through the cylinder at a given time.

MR is large so that dC/dt may be neglected compared with dS/dt, (14.2) may be written

?>-»'%},

(14.5)

dt ~~ dx\ dxj ~ dx\n \R

on substituting for C from (14.4). Thus we see that diffusion accompanied by a non-linear reaction described by (14.4) is formally the same as diffusion governed by a diffusion coefficient which is not constant, but which depends on the total concentration of diffusing substance, free and immobile. This statement holds whatever the relationship between the concentration of

328

DIFFUSIO N AN D CHEMICA L REACTIO N

FIG. 14.1. Diffusion with adsorption into a cylinder  of radius a. Numbers on curves are values of exponent n in (14.4).

50 r

FIG . 14.2. Concentration distribution s in a cylinder  of radius a when Dt/a2 = 5. Numbers on curves are values of exponent n in (14.4).

90 per  cent of solute enters cylinder.

concentration at surface of cylinder  is constant.

free and immobile components, provided it is non-linear. It need not necessarily be of the form of (14.4). If in (14.4) n is fractional, e.g. as in the wellknown Freundlich type of adsorption isotherm, then the effective diffusion coefficient in (14.5), which is given by

increases as the concentration S is increased. If on the other hand n > 1,the effective diffusion coefficient decreases as the concentration is increased.

DIFFUSION AND CHEMICAL REACTION

329

Standing, Warwicker, and Willi s (1948) have considered an extension of this argument to the case in which the product of the reaction is not immobile but can itself diffuse at a rate different from that of the free component.

Vieth and Sladek (1965) considered an isotherm which is a combination of a linear component and a non-linear one of the Langmuir type. The linear part corresponds to gas dissolved in the amorphous regions of a glassy polymer; the non-linear, to gas trapped in smal holes or microvoids in the polymer. The trapped gaseous molecules are immobile. The diffusion equation takes the form

, CH(b/kD)

dx2 dt |_ {i+(b/kD)cDy

where CD is the concentration of gas free to diffuse with diffusion coefficient D, CH is the saturation capacity of the microvoids, and b and kD are parameters in the Langmuir and linear isotherms respectively. Vieth and Sladek obtained finite-difference solutions pertaining to diffusion into a plane sheet from a limited volume of gas. They found that their mathematical model described experimental data satisfactorily, and offered a way of estimating diffusion rates from sorption data for polymers and also for porous catalysts.

14.3. Irreversibl e reaction

If the diffusing substance is immobilized by an irreversible first-order reaction so that the rate of removal of diffusing substance is /cC, where k is a constant, then the equation for diffusion in one dimension becomes

̂ = D^-kQ

(14.6)

dt dx2

provided the diffusion coefficient D is assumed to be constant. This is also the equation representing the conduction of heat along a wire which loses heat from its surface at a rate proportional to its temperature. Some solutions relating to this latter problem are given by Carslaw and Jaeger (1959, p. 134),where use is made of the transformation C = C exp (— kt) which reduces(14.6) to the usual equation in one dimension with C as dependent variable.

Odian and Kruse (1969) used solutions of (14.6) and its steady-state equivalent in discussing the effects of diffusion on radiation-induced graft polymerization.

Danckwerts (1951) has shown how solutions of (14.6) and of the general equation

— = DS/2C-kC

(14.7)

dt

can be deduced by simple transformation of the solutions of the corresponding problems in diffusion without reaction. He applies his method to two types

330

DIFFUSION AND CHEMICAL REACTION

of surface boundary condition. In the first case the surface is in equilibrium at all times with the surrounding atmosphere or solution, and the surface concentration has the constant value Co. In the second case the rate of evaporation or absorption at any time is given by

DdC/dN = a(C0-Cs) ,

(14.8)

where Cs is the actual concentration on the surface at that time, Co the equilibrium surface concentration attained after infinite time, and dC/dN the concentration gradient measured in the outward direction along the normal to the surface. Here a is a constant. For convenience in writing we put h = OL/D in what follows.

In the problems to be considered, therefore, the initial and boundary conditions are

C = 0, t = 0, at all points in the medium,

(14.9)

and either

C = Co, t > 0, at all points on the surface,

(14.10)

or

dC/dN = h(C0 - C), t > 0, at all points on the surface. (14.11)

14.3.1. Danckwerf s method

Let Cj be the solution of the equation for diffusion in one dimension in the absence of reaction, i.e. of

^ = 4%,

,.4,2,

dt

ox

for the same boundary conditions as are imposed on C in (14.9), (14.10), and(14.11). We shal give the argument for diffusion in one dimension and it will be clear, as Danckwerts shows, that it can be applied equally well to the general equation (14.7). If Cx is a solution of (14.12), the solution of(14.6) for the same boundary conditions of the above type is

C = k\ Cxz-kt df' + Qe" * '.

(14.13)

This is easily shown as follows. By differentiating (14.13) with respect to t we obtain

^ = fcC1e-fcr-fcC1e-*' + — e " * ' =  d£lt-  ̂

(14.14)

dt

dt

dt

and on differentiating twice with respect to x we have

dx

J o ox

^x

DIFFUSIO N AN D CHEMICA L REACTIO N

331

Substituting from (14.12) in (14.15) gives

(14.16)

dx2 Jo dt

dt

and finally using (14.14) we find

so that (14.13) is a solution of (14.6).

Furthermore, when t = 0, we see from (14.13) that C = Cx and so C obeys the required initial conditions. For points at which Cx = Co, for all t,

C = kC0\ e-fcr'dt' + Coe-fcf = Co.

(14.18)

J

For points at which

dCJdN ^ M C o - C J,

(14.19)

we find

dC , fr dC,

kt, J , dCx

kt

= hk\ (Co-CJe-^ 'd r'Jo

= h(C0-C).

(14.20)

The solution (14.13) therefore satisfies the required initial and boundary conditions if Cx does.

If the quantity, M r, of diffusing substance absorbed in time t is required, we use in general

F = ̂ =  ff l)|^dS = ifc f^e-^dr' + ̂ e-*'. (14.21)

dt J j dN

Jo

The area integral is taken over the whole surface of the absorbing medium and Fx is the corresponding rate of absorption when no chemical reaction takes place, i.e.

The volume integral is taken over the whole volume of the absorbing medium.

Many of the solutions for diffusion without reaction are available in the form of infinite series which can be written

y,z)e-".

(14.23)

332

DIFFUSION AND CHEMICAL REACTION

Numerous examples have been given in Chapters 3-6. Here / and v are different for each term in the series, but are not functions of t; v is not a function of x, y, z. Applying (14.13) to (14.23) we find

C _

C~o~

Similarly, since in such cases F1 is of the form

^i/C0 = Z g e -w ,

(14.25)where g is different for each term in the series but is not a function of x, y, z, r,we obtain from (14.21)

F

rt+vexPl !-,( t +v,n

Co

[_

K-j-V

J

( 1 4 2 6 )

Co

[_

K-j-V

J

and

j ; [ h ( t + "-'^^' | t + '» + ' ] . (.4.27,

14.3.2. Examples

The method can be applied generally for boundary conditions of the type(14.10) or (14.11). It will be illustrated by the examples quoted by Danckwerts.

(i) Sphere with surface evaporation condition. We take the sphere to be of radius a. Then the solution for diffusion without reaction is (Chapter 6, eqn(6.40)

y

Paw2Q sin mn

Co

r n̂ {a2oc2n+ah(ah-l)}smaoi;

[ ' }

where the a ŝ are the roots of

aa cot aa + ah -1 = 0,

(14.29)

which are given in Table 6.2. Hence

x = 4na2D

, dr

and from (14.26)

o 17 - " exp(-D(x2t)= Snh2CnDa2 Y —, \ , . " ;

(14.30)

and from (14.27)

«• - *"h'c'D°! £ ^ i S ? l w + { ! f ' ' ( 1 4 3 2 )

(/e + D aJ { a a h f i ( a / z l )|

DIFFUSION AND CHEMICAL REACTION

333

(ii) Rectangular block or parallelepiped with constant surface concentration.

We take the block to occupy the space — a < x < a, —b<y<b,

—c<z < c, so that the edges are of lengths 2a, 2b, 2c. The solution for diffusion without reaction is

d _ 64

(2/+1)TCX

xcos 2b

2cexp(-falMII )

where

Hence

a/,m,n =

2m+l\2

(14.33)

(14.34)

00

00

00

ae

l)2(2m + l)

(14.35)

and from (14.26)

( J o o

where by a is understood almn given by (14.34). Similarly Mt follows readily from (14.27).

(ii) Infinite cylinder with surface evaporation condition. We take the cylinder to have radius a and consider diffusion to be entirely radial. The expression for diffusion without reaction is (Chapter 5, eqn (5.46)

Co

where the ans are the roots of

= hJ0(aa),

l ' ]

(14.38)

and J0,Ji are Bessel functions, of the first kind, of order zero and one respectively. Values of an are to be found in Table 5.2. Hence

(14.39)

and from (14.26)

334

DIFFUSIO N AND CHEMICA L REACTIO N

Also Mt is easily found from (14.27). Here Mt and F refer to unit length of cylinder.

Other results may be derived in this way or directly from (14.13) or (14.21).

Some examples of expressions for the rate of uptake F are given below:

(iv) Sphere {radius a) with constant surface concentration

F = 8,aDC0 £ ^ + ̂ x P { - y + D.W)}

ka2 + Dn2n2

(v) Infinite cylinder (radius a) with constant surface concentration. Here F is the rate of uptake through unit length of the curved surface of the cylinder:

F = 4nDC0 i fe + D « " 7 { f + D a" » ,

(14.42)

where the ans are the roots of Jo(aoc) = 0.

(vi) Finite cylinder (radius a, length 21) with constant surface concentration.

Here F is the rate of total uptake through the ends and the curved surface:_ 64DICO « » f /?„,„  I f/c + Dft.,, exp { - t(k + P f t j n

where the ans are the roots of J0(aoc) = 0, and

)2n2/(4l2).

(14.44)

(vii) Semi-infinite solid with surface evaporation condition. The solution is obtained by application of (14.21) to the corresponding solution without reaction (Chapter 3, eqn (3.35)). Here F is the rate of uptake per unit area of plane surface and

F = ^^\[h(Dk)Uvf(ktf

+ h2DQvfch(Dt^Qxp{t(h2D-k)}-k].

(14.45)

n LJ K

(viii ) Semi-infinite medium with constant surface concentration. The mathematical problem and its solution are identical with those for the conduction of heat along a thin rod which loses heat from its surface at a rate proportional to its temperature (Danckwerts 1950a; Carslaw and Jaeger 1959). The expression for the concentration is

C _

Q ~

erfc | ^ - ^ - + >/(*oj -

(14.46)

DIFFUSIO N AND CHEMICA L REACTIO N

335

Also

and

Mt = Co

(14.47)

(14.48)The dimensionles quantity Mtk^/(C0D^) is plotted as a function of kt in Fig. 14.3. From this graph, Mt can be obtained at any time t for any combination of the variables Co, D, and k.

0-2 0-4 0-6 0-8 10

FIG . 14.3. Diffusion with an irreversible reaction into a semi-infinite medium with constant surface concentration.

When kt is large so that erf J{kt) approaches unity, (14.46), (14.47), and(14.48) become

C/Co = exp(-xk±fD%

(14.49)

F = C0{Dkf\

(14.50)

±

(14.51)

336

DIFFUSIO N AND CHEMICA L REACTIO N

Eqns (14.49) and (14.50) show that the concentration at any point and the rate of sorption each tend to a steady value and the total amount taken up increases linearly with time as in Fig. 14.3.

When kt is very smal we find by expanding erf^/cf) and exp( — kt) and neglecting powers of kt higher than the first, that (14.47) and (14.48) become

F = C0{l+kt){D/(nt)}*

(14.52)

and

Mt = 2C0(l+$kt)(Dt/n)\

(14.53)

which reduce to the well-known solutions for diffusion without reaction when k = 0. Further solutions describing the uptake of a restricted amount of diffusing substance which is simultaneously destroyed by an irreversible reaction are given in § 14.4.4 below as special cases of more general solutions for a reversible reaction.

14.3.3. Steady-state solutions

As with the semi-infinite case just discussed so in all systems of the type under consideration, the rate of sorption and the concentration at any point tend to steady values at large times. The steady-state solutions may be obtained by putting dC/dt equal to zero in the appropriate form of (14.7),which may then be solved to give the steady-state solution directly. When the expression for C or F takes the form of (14.24) or (14.26), the steady-state solution may be obtained merely by omitting the time-dependent term,which tends to zero as t tends to infinity. This leads to a solution in the form of a series which is often not readily evaluated.

In some cases the following method leads to a more convenient form of solution. On putting t — oo in (14.13) and (14.21) we find

CJk= fc.e-'-dt,

(14.54)

and

/»00

FJk = F^-^dt.

(14.55)

J o

The expressions on the right-hand sides of these equations are the Laplace transforms of Ct and F1 respectively, the parameter (usually written as p or s in transform notation) taking the value k. Thus, as an example, for a semi-infinite solid with surface evaporation we have, in the absence of reaction,

F, = hDC0 exp (h2Dt) erfc {h{Dtf}.

(14.56)

The Laplace transform of the right-hand side of (14.56) is

DIFFUSIO N AND CHEMICA L REACTIO N

337

and hence from (14.55)

Some other steady-state solutions are given below, preceded by references to the corresponding expressions describing the approach to the steadystate.

(i) Sphere with surface evaporation condition (eqn (14.31)).

(ka2/D)±coth(ka2

(ii) Infinite cylinder with surface evaporation condition (eqn (14.40)).

c~0 = 2nah%D)n^iD)^h h{k^iDf\

(1459)

Here 70 and / t are modified Bessel functions of the first kind of zero and first order respectively.

(iii ) Sphere with constant surface concentration (eqn (14.41)).

^ = AnaD{{ka2IDf coth (ka2/D)*-l).

(14.60)

(iv) Infinite cylinder with constant surface concentration (eqn (14.42)).

A further application of the use of eqn (14.13) is to the problem of the extraction of a dissolved substance from a drop of liquid which is rising or falling through another liquid. It is described in Danckwert's paper (1951).

14.4. Reversible reaction

The most general case for which formal mathematical solutions have so far been obtained is that in which the reaction is first-order and reversible.

The behaviour to be expected when the reaction is reversible depends on the relative rates of diffusion and reaction. Thus we have seen in § 14.2 (p. 326)that when the reaction is very rapid we can assume that the immobilized component is always in equilibrium with the component free to diffuse, and diffusion is the rate-controlling process. At the other extreme is the case of diffusion being so rapid compared with the reaction that the concentrations of diffusing substance and immobilized product are effectively uniform throughout the medium and the behaviour is controlled solely by the reversible reaction. Solutions of the more general case in which the rates of

338

DIFFUSIO N AND CHEMICA L REACTIO N

diffusion and reaction are comparable have been obtained by Wilson

(1948) and Crank (1948c).

The general problem can conveniently be stated in terms of a solute diffusing from a solution into a plane sheet of material. The modifications necessary for corresponding, alternative problems, such as those of a sphere or cylinder suspended in a vapour, will be obvious. Suppose an infinite sheet of uniform material of thicknes 2a is placed in a solution and that the solute is allowed to diffuse into the sheet. As diffusion proceeds, a first-order, reversible reaction occurs and a product, which is non-diffusing, is formed. The sheet occupies the space — a ^ x ^ a, and there is a restricted amount of solution which occupies the space —l — a^x  ̂ —a, a ^ x ^ l + a. The concentration of solute in the solution is always uniform and is initially Co,while initially the sheet is free from solute. Let C be the concentration of solute free to diffuse within the sheet and S that of the immobilized solute,each being expressed as amount per unit volume of sheet.

The diffusion is governed by the equation

dC d2C dS

and we consider the simultaneous reaction to be of the type

dS/dt = AC-fiS.

(14.63)

Here D is the diffusion coefficient and X and \i are the rate constants of the forward and backward reactions respectively. Thus the immobilized solute is formed at a rate proportional to the concentration of solute free to diffuse,and disappears at a rate proportional to its own concentration. We require solutions of (14.62) and (14.63) with the initial condition

S = C = 0, -a<x<a,

t = 0,

(14.64)and with a boundary condition expressing the fact that the rate at which solute leaves the solution is equal to that at which it enters the sheet over the surfaces x = ±a. This condition is

idC/dt = +DdC/dx, x = ±a, t > 0.

(14.65)

We here assume that the concentration of solute free to diffuse just within the surface of the sheet is the same as that in the solution. This may not be so and there may be a distribution factor K, which is not unity, such that the concentration just within the sheet is K times that in the solution. This can clearly be allowed for by using a modified length of solution l/K in place of /in (14.65) and elsewhere. Mathematical solutions follow for these equations and for corresponding equations for the cylinder and sphere.

DIFFUSION AND CHEMICAL REACTION

339

14.4.1. Mathematical solutions

(i) Plane sheet. Solutions of the equations of § 14.4 can be obtained by the method of Laplace transforms. Writing C and 5 for the Laplace transforms of C and S respectively, so that

C = Ce~ptdt,

S =

Se~ptdt,

*o

Jo

(14.66)

we have the following equations for C and S

pC = -PS + Dd2C/dx\

(14.67)

pS = /.C-fiS,

(14.68)

-lC0 + plC = -DdC/dx,

x = a.

(14.69)On eliminating S from (14.67) and (14.68), and replacing the partial derivative by an ordinary derivative since t does not appear, we find

^ ,

(14.70)

D p + fj

of which the solution that gives C an even function of x is C = F(p) cos kx.

(14.71)The function F(p) is determined by the boundary condition (14.69) and it follows immediately that

C = , lC,oC°* kX. , .

(14.72)

pi cos ka — ku sin ka

The derivation of C is straightforward as in Chapter 2, § 2.4.3 (ii), and after some reduction gives

c _ /Co g.

Co exp ( p n t ) c o s knx

l + (R + l)

.t1! \. Ill  \ \a Pn P2ja\ cos kna

\ {Pn + H)2]\2l  2Dkl + 2Dikl\

(14.73)

where the pns are the non-zero roots of

and R = Xj[i  is the partition factor between immobilized and free solute.

The expression for S differs from (14.73) only by having an extra factor A/(pw + ju) multiplying the nth term, including the term pn = 0. Writing Mt for the total amount of solute, both free to diffuse and immobilized, in half

340

DIFFUSIO N AND CHEMICA L REACTIO N

the sheet at time t, and M^ for the corresponding quantity in the final equilibrium state attained theoretically after infinite time, we have

where the pns are given by (14.74) and where

a = l/(R + l)a, M  ̂ = ICO/(1 + a).

(14.76)

(ii) Cylinder. The case of the cylinder was considered by Wilson (1948),using a slightly different method. The final result for a cylinder of radius a,in a solution occupying a region of cross-sectional area A, is

M< i y

( l+a)exp(p.t)

where

a = A/{7ta2(K +1)} , Mx = AC0/(l + a),

(14.78)

and the pns and fcns are given by pn

J,(Ka)

2

PnPn + l + H

. . . - .

Da V(M) '  "  D P + n '

U '

2n

0(M )

The expression for the concentration of free solute is=

AC0

A + (R + l ) 2

\ \na2 , Ap2n } J0(kna)

(14.80)

The expression for S differs from (14.80) only by having an extra factor multiplying the nth term, including the term pn = 0.

(iii ) Sphere. On introducing new variables rC and rS the equations for the spherical case take essentially the same form as those for the plane case, and the same method of solution leads to

1

2"J I  V

where the pns and kns are given by

"  I   Wk^

pn_l = -knacotkna,

k2n = - ^ ^-——,

(14.82)

D pn + u

DIFFUSIO N AN D CHEMICA L REACTIO N

341

and

a = =

, M  ̂ = - ^ .

(14.83)

4na (R + l)

1+a

The expression for C is

3F+47ta3(R+l), y

Coexp(p.t)

a sin fcBr

+ ^ . f , X,i }\2na3 pn

Vpj }~r sin kna

[ ' >

I (

+ ]

and that for S differs from (14.84) only by having an extra factor A,/(pn

multiplying the rcth term, including the term pn = 0.

14.4.2. Physical significance of the mathematical solutions

When mathematical solutions are as complicated in form as those in§ 14.4.1 their physical significance is not immediately obvious. Consider eqns(14.74) and put

x = k2a\ y = pa2/D, £ = a2(/l + ^)/A n = a2fi/D. (14.85)

Then

ly/a = Jx tan Jx,

(14.86)

x = -y-^i

(1487)

y + n

are the equations to be solved for the roots. Graphs of eqns (14.86) and (14.87)are sketched in Fig. 14.4 to show the general location of the roots. The graph of (14.86) is the same for all £, and rj, and from the figure it is easy to see qualitatively how the roots vary with £, and n. When corresponding transformations to those of (14.85) are applied to eqns (14.79) for the cylinder and (14.82)for the sphere, the resulting equations are of the same form as (14.86) and(14.87), so that Fig. 14.4 can be taken as showing qualitatively the location of the roots for all three cases. There is a root for which kna is imaginary given by

ly/a = V(-x)tanh V(-x) .

(14.88)

The general expression for MJM  ̂ therefore comprises a unit term from pn = 0, a term for which kna is imaginary, and two infinite series of terms corresponding to the intersections of the two branches of (14.87) with successive branches of (14.86).

The relative importance of the various terms depends on the parameter n. It is interesting to see quantitatively what happens to the general solution

342

DIFFUSIO N AN D CHEMICA L REACTIO N

Calculated from (14-86)

Calculated from (14-87)

O Successive real roots

£ Root for  which k „  a

is imaginary

\

FIG . 14.4. Location of roots of (14.86) and (14.87).

for the extreme values of this parameter which correspond to very fast and very slow reactions. The roots of (14.87) are given by

2y= _(

(14.89)

the two infinite series arising from the alternative sign. For extreme values of rj  the roots are readily obtained by using the appropriate binomial expansion of the term under the square root sign in (14.89). Proceeding in this way with the aid of Fig. 14.4, it is not difficult to show that if r\ is very large, that is the reaction is very rapid compared with diffusion, the terms in the general solution for MJM  ̂ which arise by taking the negative sign in (14.89) vanish, as does also the term from the imaginary root. The terms from the positive sign lead to

(14.90)

M = 1 ~ ?

where the knas approach the roots of

tan kna = — (xkna,and

P = D/(R + l)a2.

(14.91)

(14.92)This is the solution obtained by Wilson (1948) for the case of an immobilizing reaction which is rapid compared with diffusion.

DIFFUSION AND CHEMICAL REACTION

343

If, however, rj  is smal because the reaction is infinitely slow (JJ. = 0),we find that the terms arising from the positive sign in (14.89) vanish provided a/I is not zero, which case is treated separately in § 14.4.3. The terms from the negative sign combine with that from the imaginary root to give

ML

R I  \ f R + U + Jl

l+l/a  + (l/a)2k2na2

where the kns are given by

tanfcna = -(l/a)kna.

(14.94)

The whole term in the second bracket in (14.93) is to be recognized as the expression for simple diffusion from a finite bath, i.e. diffusion in the absence of any immobilized component. Eqn (14.93) also describes a simple diffusion process,, therefore, and MJM  ̂ changes from zero at t = 0 to\—Rl/{(R+ 1) x(l + a)} at t = oo, which is easily shown to be the fractional uptake of solute to be expected in the absence of immobilized solute. Thus(14.93) indicates the behaviour to be expected on general argument, namely that for an infinitely slow reaction the sheet takes up, by simple diffusion, only the fraction of solute which it can accommodate in the freely diffusing state and none in the immobilized state.

If on the other hand \ia2/D is smal because D is very large, all terms in the general solution vanish except the one associated with the imaginary root and we are left with

Mt . R I

1

Ra

"l  + alit).

(14.95)

This expression is readily deduced from elementary considerations when diffusion is so rapid that the concentration of solute is effectively uniform through the sheet at all times.

The type of behaviour observed in a practical system for which \ia2jD is very small, depends on the time scale of the experiment. If this is such that the reaction occurs very slowly compared with the duration of the experiment the simple diffusion behaviour of eqn (14.93) is observed. If on the other hand diffusion is very rapid compared with the time scale of the experiment, the simple first-order reaction of eqn (14.95) is observed.

14.4.3 Numerical evaluation

When eqns (14.74) and (14.75) are written in terms of pjfi and kna, we see that MJM  ̂ can be calculated as a function oiDt/a2 if three parameters are known. The parameters are I/a, that is the ratio of the volumes occupied by solution and sheet respectively; the partition factor R; and the modified rate constant for the reaction, \ia2/D. Alternatively, since R = X/n, a solution is defined by I/a and the two rate constants \ia2/D and Xa2/D. In some cases it

344

DIFFUSIO N AND CHEMICA L REACTIO N

is more useful to relate R to the fraction of the total amount of solute which is in the sheet finally, i.e. to MJICO, by the relations (14.76). For the cylinder the corresponding parameters are na2/A, R, and fia2/D, and for the sphere 4na3/3V, K, and fia2/D.

Once the roots pn, kna are obtained, the evaluation of each of the expressions for MJM  ̂ for the plane sheet, cylinder, and sphere is straightforward provided /, A, and Fare finite. The cases of/, A, and V infinite, however, need further consideration because the convergence of terms for which pn approaches — \x can be very slow and numerical evaluation becomes awkward and laborious, particularly for smal fxa2/D. For the plane sheet when a = oo, eqn (14.75) reduces to

2D2k2n(l+pn/Li)2exp(pnt)

{

0)

where now kna = {n + \)n. As we saw in § 14.4.2, there are two infinite series in the general expression for MJM .̂ We shal confine attention for the moment

to the series associated with the positive square root in eqn (14.89) since these are the terms for which pn approaches — \i when Dk2J\i is large. Substituting for 1 +pjn from the second of eqns (14.74) we find

= « _ y

l ' }If pn = — n to the order of accuracy required, after the first r non-zero roots,we have

l+pJti)2exp(Pnt)

R

approximately, since

^ k2a

̂ k2n:

n=l  Kna

=  1.

^ 2

(14.98)

(14.99)

The relationship (14.99) follows, for example, from (14.90) when a = oo,since MJM  ̂ = 0 when t = 0. The error involved in use of the approximate form (14.98) is less than

R

£- k2a:

(14.100)

and can be made as smal as desired by choice of r. We may note in passing that since in (14.97) pj[i  and 1 +pjii  occur only with R, this a more convenient form of expression for computation than (14.96) when pj/a is

DIFFUSION AND CHEMICAL REACTION

345

smal or near — 1, particularly for large R, since it is less sensitive to the accuracy of the roots pj\x.

When I/a = oo, it follows from (14.88) that there is no root for which kna is imaginary. The complete expression for MJM  ̂ is therefore that of(14.98) together with terms arising from the negative sign in the roots of(14.89). On using (14.98) numerical evaluation of MJM  ̂ for I/a infinite is straightforward. The corresponding formulae for the plane sheet and the sphere are easily derived.

14.4.4. Irreversible reaction

A special case of the above solutions of particular interest is that of an irreversible reaction, when the rate of formation of immobilized solute is directly proportional to the concentration of free solute. In this case jn = 0,but A is non-zero so that R = oo, a = 0, M^ = /Co. The solution for the plane sheet, for example, for these values follows immediately from (14.74) and(14.75) provided / is finite.

The solution for the case of / = oo is less obvious. When fi = 0, the imaginary root (pf, kt) is given by

lp. = -Dkj tanhkja, k'2 = (Pf + A)//),

(14.101)

where k{ = ik'i9 and so when / = oo,

p. = 0, k? = A/D.

(14.102)When a = 0, \x = 0, and pt is small, we can expand exp (ptt) in powers of ptt and write (14.75) as

M ir

ICpJl+Pit)

$

/Co exp (/y)

Mt = /Co

2T L

IT" ' (14.103)

a Pi

Vi  ̂ n= i . a Pn PJa 2/ IDk'? 2D2k\2

2/ 2Dk22 k2n 2D2k2n

from which, when / = oo, so that lpt is given by (14.101) and (14.102), we have finally

—<- = ^qtanhq + ̂ sech2 q + ̂ -tanhq- t 2D k*^vw,

{ { 4 m )

aC0 a2

2q

^

a2p2

where

kna = (n + \)n, k2 = -(p^ + AyZ), q = ^/{Xa2/D). (14.105)

The first term on the right-hand side of (14.104) gives the rate of uptake of solute due to the chemical reaction in the final steady state.

The forms of (14.77) and (14.79) for the cylinder, and of (14.81) and (14.82)for the sphere when \i = 0, a = 0, are obvious. When A = oo we have for the

346

DIFFUSIO N AND CHEMICA L REACTIO N

cylinder

M,

2Dt Ix(q) l2M) y 4D2/c2exp(/y)—2?r =  1 +—T(lTT~\~j27~\ ~~ L

2 ' (14.106)

where

J 0 ( M = 0, /c2 - - (P |i + ;.)/D, </ - y/(la2/D). (14.107)When F = oo we have for the sphere

— = —^-(gcoth q— 1) — fcosech2 q + |coth q —

(14.108)where

kna = nn, /c2 = - (pn + A)/D, q = J(^a2/D).

(14.109)

The solutions (14.104), (14.106), (14.108) can of course be obtained directly

by use of the Laplace transform or otherwise. When A — oo the concentration at the surface of the cylinder is constant and (14.106) is the integrated form of

(14.42). Similarly (14.108) is the integrated form of (14.41).

14.4.5. Desorption

We have considered diffusion into a plane sheet initially free of solute.

There is the complementary problem in which all the solute is at first uniformly distributed through the sheet and subsequently diffuses out into the solution. If free and immobilized solute are considered to be initially in equilibrium everywhere in the sheet, it is easily seen that the mathematical solutions presented above for sorption also describe desorption, provided

Mt is taken to mean the amount of solute leaving the sheet up to time t, and M ^ the corresponding amount after infinite time. For desorption from a plane sheet, for example, we want solutions of eqns (14.62) and (14.63) satisfying the condition (14.65), but with (14.64) replaced by

C = Co, S = So, -a<x<a,

t =  0.

(14.110)

Writing

Cl=C0-C, Sl=S0-S,

(14.111)

it is easy to see that (14.110) and the other equations for desorption are identical with (14.62), (14.63), (14.64), and (14.65) with C{,S{ written for C, S respectively, remembering only that AC0 — jnS0 =  0, if we have equilibrium throughout the sheet at t =  0. Hence the solutions for Cx for desorption are readily deduced from those for C for sorption, as are also the expressions for relating to desorption.

DIFFUSION AND CHEMICAL REACTION

347

14.4.6. Calculated results

Evaluation of the expressions of § 14.4.4 for the irreversible reaction and any particular set of parameters is comparatively simple and straightforward. On the other hand a considerable amount of painstaking labour is involved in the evaluation of the formulae for the reversible reaction even when there is an infinite amount of solute, and it is therefore worth while to present some numerical values. In Tables 14.1, 14.2, 14.3, 14.4 calculated values of MJM  ̂ are tabulated for the plane sheet, cylinder, and sphere. The arrangement of the tables was decided by ease of presentation.

Three values of the partition factor R are included and for each R three rates of reaction. All tabulated solution refer to an infinite amount of diffusing substance. The values oiMJM  ̂ are believed to be correct to within ± 1 in the third decimal place.

Solutions for the plane sheet are illustrated in Figs. 14.5, 14.6, and 14.7.

Those for the cylinder and sphere show the same general features, differing only in detail. Fig. 14.5 shows how the sorption curves change in shape and position as fia2/D is varied between the two extremes given by \i = oo(infinitely rapid reaction) and \i = 0 (simple diffusion with no reaction). By plotting against {jitf  as in Fig. 14.6 we can show the approach to the curve for D = oo (purely reaction controlled) as \ia2jD tends to zero because of D becoming large. We see also in Fig. 14.6 that the discontinuity in the gradient of the curve for D infinite appears as a 'shoulder' when jia2/D = 0-01. As fia2/D is increased further the shoulder disappears leaving a sorption curve

l-or

0-75 -

0-50 -

0-25 -

0-5

10

15

20

2-5

{Dt\{R+ \)a2}{

FIG. 14.5. Plane sheet, R = 10. Numbers on curves are values of fia2/D.

348

DIFFUSIO N AND CHEMICA L REACTIO N

100

0-75

0-50

0-25

0

D = oo 001

0-5

10

1-5

20

2-5

FIG. 14.6. Plane sheet, R = 10. Numbers on curves are values of na2/D.

with a point of inflexion. At still higher pia2/D the inflexion becomes less noticeable as in Fig. 14.5 and the curves have the simple shape commonly associated with diffusion. Fig. 14.7 shows the influence of the parameter R,the partition factor between immobilized and free solute. As R is increased the height of the shoulder decreases, and if curves for R = 100 were plotted on the present scale no shoulder would be detected for any value of fxa2/D.

One interesting feature of these results is that they indicate limits to the relative rates of diffusion and reaction outside of which the reaction is effectively infinitely rapid or infinitely slow as the case might be. Thus for the plane sheet, the values of MJM  ̂ for fia2/D = 10 differ by only a few per cent from those for an infinitely rapid reaction. The differences are greatest for R = 1 where they are about 5 per cent. At the other extreme the solution for fia2/D = 001, R = 1, is the same as that for an infinitely slow reaction to the same degree of accuracy except at smal times (see Fig. 14.7 for example).

The differences increase in this case as R increases, being about 20 per cent for R = 100.

The significance of these limits is perhaps easier to appreciate when they are expressed in terms of the half-times of the simple diffusion and simple reaction processes respectively. For simple diffusion into the plane sheet from an infinite amount of solution it is easy to show that the half-time td, that is the time at which MJM  ̂ = \, is given by

Dtja2 = -(4/K2)lnn2/16 = 0-2,

(14.112)

DIFFUSION AND CHEMICAL REACTION

349

1-OOr

0-75 -

^ 0 - 5 0

0-25

0-5

10

* 1-5

20

2-5

FIG. 14.7. Plane sheet, R = 1. Numbers on curves are values of fia2/D.

approximately. On the other hand if immobilized solute is formed from a uniform, constant concentration Co of free solute according to the equation dS/dt = XC0-fiS,

this reaction has a half-time tT given by

litr = In 2 = 0-7,

(14.113)

(14.114)approximately, and combining (14.112) and (14.113) we have for the ratio of the half-times,

tr/td = 3-5D/(fia2).

(14.115)

Thus we can say that if the diffusion is more than 1000 times faster than the reaction, the behaviour of the diffusion-reaction proces is roughly the same as it would be if diffusion were infinitely rapid. On the other hand if the half-times for diffusion and reaction are comparable, the behaviour approximates to that for an infinitely rapid reaction. These statements indicate orders of magnitude only. They apply also to the cylinder and sphere.

14.5. A bimolecular  reaction

Katz, Kubu, and Wakelin (1950) and also Reese and Eyring (1950) have considered the problem of diffusion accompanied by an immobilizing reaction which is bimolecular. They consider diffusion in a cylinder, representing

350

DIFFUSIO N AND CHEMICA L REACTIO N

a textile fibre in which there are a number of active groups to which the diffusing molecules can become attached. The proces is described by the equation

dC/dt = DV2C-knC,

(14.116)

where n(r, t) is the number of active groups unattacked at radius r and time t.

Both treatments are approximate only, because (14.116) is non-linear and not amenable to formal solution. Katz et al. first neglect the term knC in(14.116) and then use the known solution of the simplified diffusion equation which yields C as a function of r and t, to obtain an approximation to n through the equation

dn/dt = -knC.

(14.117)

Reese and Eyring (1950) make the assumption that the rate of reaction depends on the average concentration of diffusing molecules throughout the fibre, and not on the concentration C as in (14.117), which depends on the radial coordinate r. More recently, Petropoulos and Roussis (196%) discussed numerical solutions of the complete equation (14.116). They referred also to solutions obtained by Lebedev (1966). Nicolson and Roughton

(1951) applied the Crank-Nicolson numerical method to the diffusion of CO and O2 through the outer membrane of the red blood corpuscle, accompanied by diffusion and chemical reaction in a core of concentrated haemoglobin. The equations take the form

dy

— = -k'py + k(yo-y),

in the haemoglobin core, and

in the surface membrane. Further applications of the mathematical treatment have been made by Klug, Kreuzer, and Roughton (1956). The subject has been reviewed by Roughton (1959).

14.6. Reduced sorption curves

Weisz (1967) suggested that when fractional sorption curves are plotted against a modified time variable there is relatively littl e difference between their behaviour even for the extreme cases of a cweak' linear isotherm and a 'strong1 irreversible sorption characterized by the type of sharp advancing

DIFFUSIO N AN D CHEMICA L REACTIO N

351

boundary discussed in Chapter 13. Weisz used a time variable T given by

Dt P Co

~~ R2 b Cf '

where t is real time, D the diffusion coefficient of the mobile component, R the radius of the cylinder or sphere, P the fractional volume in which diffusion occurs, b a tortuosity factor, and Co and Cf are the surface and the total final concentrations throughout the medium. A second paper by Weisz and Hicks

(1967) gives numerical results.

Further papers by Weisz and co-workers are referred to by Ott and Rys

(1973) who present a general model of diffusion with immobilization including cases of competitive sorption of more than one diffusing species.

14.7. Constant reaction rate

Solutions of the equation

where A represents a constant rate of generation or removal of diffusing substance, have been adequately covered for the standard geometrical shapes by Carslaw and Jaeger (1959). Goldenberg (1951, 1952) solved the heat equation for the case of a constant rate of heat generation in a sphere embedded in an infinite medium having identical (1951) and different (1953)diffusion properties.

15

SIMULTANEOUS DIFFUSION OF HEAT AND MOISTURE

15.1. Introductio n

T H E problem to be discussed in this chapter is that of the diffusion of one substance through the pores of a solid body which may absorb and immobilize some of the diffusing substance with the evolution or absorption of heat. This heat will itself diffuse through the medium and will affect the extent to which the solid can absorb the diffusing substance. We thus have two processes, the transfer of moisture and the transfer of heat, which are coupled together, and we cannot in general consider one proces without considering the other simultaneously. For convenience we shal refer to diffusion through pores, but the theory will apply to alternative systems provided only that some of the diffusing substance is immobilized and that heat is given out in the process. Thus the case of a dissolved substance diffusing through a gel would be included. Equations of the same form would also be obtained,neglecting thermal effects, for the diffusion of two substances through a porous solid, each capable of replacing the other in absorption by the solid.

15.2. Uptake of water  by a textile fibr e

A simple illustration of the coupling between the transfer of heat and that of moisture is afforded by the uptake of moisture by a single textile fibre.

Water penetrates the fibre by diffusion and for a wool fibre a diffusion coefficient of about 10"7 cm2 s"! can be taken as representative. The time for a single fibre to reach say 80 per cent of its final uptake of moisture depends not only on the diffusion coefficient but also on the diameter of the fibre—the thinner the fibre the more quickly it absorbs. Now the average diameter of a fibre is so smal (rather less than 10"3 cm) that for a diffusion coefficient of 10~7 cm2 s~*  we expect 80 per cent absorption to be reached in about 2 seconds. King and Cassie (1940) attempted to demonstrate this conclusion experimentally by measuring the rate of sorption of water vapour by a smal mass of wool (0-25 g) suspended by a sensitive spring-balance in an evacuated chamber into which water vapour was introduced at 23-5 mm pressure. By suspending the wool in an evacuated chamber King and Cassie eliminated diffusion through any surrounding atmosphere, and they expected to measure directly a rate of uptake governed solely by diffusion within the fibres. In view of the smal diameter of the fibre we expect this uptake to be a

SIMULTANEOUS DIFFUSION OF HEAT AND MOISTURE 353

matter of only a few seconds. This does not appear to be at first sight supported by the uptake curve they observed, which reached 80 per cent only after an hour or so.

We must remember, however, that when water vapour is absorbed by wool a large amount of heat is evolved which produces a considerable increase in temperature. King and Cassie showed that when this temperature rise is taken into account the relatively low rate of sorption can be reconciled with the statement that an individual fibre reaches equilibrium with its surroundings effectively instantaneously. Thus the uptake of moisture depends on the vapour pressure and also on temperature; the uptake is greater the higher the vapour pressure but is decreased by a rise in temperature.

In the experiment we have described, the uptake would have been more than 30 per cent if the temperature had remained constant. Because the temperature rose to over 65 °C, however, the uptake immediately acquired was much less than 30 per cent. A temporary equilibrium is reached, in which the uptake is in equilibrium with the external vapour pressure at the modified temperature produced by the heat evolved as the vapour is absorbed. King and Cassie(1940) calculated this temporary equilibrium uptake to be 2-3 per cent and the temperature 80 °C. Subsequently heat is lost and as cooling proceeds the uptake of moisture increases. The uptake curve observed by King and Cassie was thus essentially a cooling curve. The uptake and temperature curves calculated in this way agree well with the corresponding experimental curves.

This experiment in a vacuum may seem artificial, but it illustrates that the immediate reaction of a mass of fibres when presented with a new atmosphere is to modify that atmosphere to be in equilibrium with itself at the expense of only a slight change in its own moisture content.

15.3. Two possible equilibriu m conditions

We consider now an example quoted by Cassie (1940a) having a more direct bearing on the problem in which we are interested. Suppose a sheet of wool fibres conditioned to 45 per cent R.H. at 20 °C, so that its moisture uptake is 10 per cent, is suddenly placed in a stream of air at 65 per cent R.H.

and the same temperature. The wool and air can come to equilibrium in two very different ways:

1. By an increase in the uptake of the wool until it is in equilibrium with

65 per cent R.H. The regain needed is 14 per cent.

2. By an increase in the temperature of the wool and air till  the new vapour

pressure represents only 45 per cent R.H., the uptake of the wool remaining essentially unchanged at 10 per cent. It is easy to calculate

from vapour pressure tables that this will be so if the temperature rises to

25 °C.

354 SIMULTANEOUS DIFFUSION OF HEAT AND MOISTURE

Of these two possible equilibrium conditions the first, involving a considerable change in moisture uptake, can only be achieved after a large volume of air has passed through the wool. The second, involving a temperature rise, is easily attained almost immediately because of the large heat of sorption. Enough heat is produced by a relatively smal increase in moisture uptake to raise the temperature of the wool to 26 °C (̂  per cent will do it if the heat capacity of the air is neglected). For this reason the first equilibrium set up is the one in which the temperature rises but the regain is essentially unchanged. This is only a pseudo-equilibrium, however, because if we continue to blow air at 20 °C over the wool the final temperature must be 20 °C and the final regain 14 per cent. Here we have the essential feature of the propagation of humidity and temperature changes in textiles or similar materials, namely the existence of two equilibrium states—a temporary one set up quickly and involving no change in uptake, and a permanent one set up relatively slowly and involving a change in moisture content.

15.4. Propagation of two disturbances

Clearly, therefore, when the air stream first passes through, a front,separating the original and pseudo-equilibrium conditions, moves through the textile with the speed of the air flow if we neglect the heat capacity of the textile. Thus a fast disturbance representing change of temperature and moisture in the air without change of regain, is followed by a much slower disturbance bringing a change of regain. Furthermore, the same general behaviour is to be expected when the transfer of heat and moisture occurs by diffusion rather than as a result of aerodynamic flow of air.

Mathematical equations describing the diffusion phenomena in detail have been set up and from them it is possible to calculate how concentration,temperature, and total moisture uptake vary with time and distance through the medium til l final equilibrium is attained. Henry (1939,1948) first gave the

FIG. 15.1. Element of textile package.

SIMULTANEOUS DIFFUSION OF HEAT AND MOISTURE 355

theory for diffusion of humid air into a textile package and Cassie (1940b)later gave ihe corresponding theory for air forced through the textile,neglecting diffusion effects entirely. Since then Daniels (1941) has taken into account diffusion of heat and moisture in an air stream forced through the textile. Armstrong and Stannett (1966a) extended the work of Cassie and others to include the effects of the diffusion of moisture in cylindrical fibres.

In plane sheets which are thinner, movement of both heat and moisture were allowed for (Armstrong et al. 1966b). We now give Henry's treatment of the diffusion problem.

15.5. Equations for  diffusion of heat and moisture

15.5.1. Equilibrium equation

Fig. 15.1 shows diagrammatically an element of a textile package occupied partly by fibres and partly by air spaces. This is much oversimplified but serves to fix ideas. We have said that a fibre can always be considered as in equilibrium with its immediate surroundings. We shal further assume linear dependence on both temperature and moisture content and write

M = constant + GC-O>T,

(15.1)

where C is the concentration of water vapour in the air spaces expressed in g cm"3, M is the amount of moisture absorbed by unit mass of fibre, a and a>are constants. We shal consider the equilibrium uptake of moisture by a fibre to be related to water vapour concentration and temperature T by the linear relation (15.1). This is a necessary assumption if the theory is to proceed ; clearly in practice it is only an approximation which is reasonable over smal ranges of humidity and temperature.

15.5.2. Vapour diffusion equation

Consider an element of a textile package. We can derive two equations,one expressing the rate of change of concentration and the other the rate of change of temperature.

The rate of change of concentration is governed by the following:

(i) Diffusion of vapour through the air spaces and through the fibres, both

these being proportional to the concentration gradient in the usual way.

Diffusion through the pores will in many cases be greater than through

the fibres, but even if this is not so we can represent both processes by

one term if we make the assumption that the vapour in the fibre is always

in equilibrium with that in the air in the immediate neighbourhood and

the absorption isotherm is linear as in (15.1).

(ii) The absorption or desorption of moisture by the fibres from the air

spaces.

356 SIMULTANEOUS DIFFUSION OF HEAT AND MOISTURE

Thus we can say,

Net amount of vapour entering element by diffusion

= increase in moisture in air + increase in moisture in fibres. (15.2)

If a fraction v of the total volume of the package is occupied by air and 1 — v by fibre of density ps then, expressing (15.2) mathematically, the equation governing the movement of vapour can be written

where C and M have been defined and DA is the diffusion coefficient for moisture in air. The factor g allows for the fact that the diffusion is not along straight air channels but through a matrix of intertwined fibres and any diffusion along the fibres themselves can also be allowed for in this factor.

It is a factor which can be measured by permeability measurements under steady-state conditions.

15.5.3. Heat diffusion equation

The rate at which the temperature of the element changes is determined by

(i) conduction of heat through air and fibres;

(ii) the heat evolved when moisture is absorbed by fibres.

Thus

Increase in heat content of fibres

= net amount of heat entering by conduction + heat evolved

as fibres absorb moisture,

(15.4)

and this is expressed mathematically by the equation

dT

d2T

dM

/ i c c x

K

( 1 5 5)

where a is the specific heat of the fibres, K the over-al heat conductivity of the package, p the density of the package, expressed as mass of fibre per unit overal volume, and q is the heat evolved when 1 g of water vapour is absorbed by the fibres. In writing (15.5) the reasonable assumption has been made that the heat content of the air is negligible compared with that of the fibres.

One vital point to be noticed is that both eqn (15.3) and (15.5), that is the vapour equation and the temperature equation, involve M, the amount of moisture in the fibres. It is at once obvious that the two processes, the transfer

SIMULTANEOUS DIFFUSION OF HEAT AND MOISTURE 357

of moisture and the transfer of heat, are coupled together in this way and that we cannot in general consider one proces without considering the other simultaneously.

15.5.4. Assumptions underlying the mathematical theory

It is worth while to enumerate some of the assumptions on which the theoretical treatment is based. The main ones are as follows:

(i) The linear dependence of M on C and T to which reference has already been made.

(ii) The quantities DA , K, a, p are assumed constant and independent of moisture concentration and temperature.

(iii ) The heat of sorption q is assumed independent of regain though in practice it is not so.

(iv) Hysteresis of sorption is neglected, that is the equilibrium equation(15.1) is assumed to hold whether the fibre is gaining or losing moisture.

(v) The relative volumes occupied by fibre and air are assumed not to change as diffusion proceeds, i.e. v is assumed constant. In actual fact,as the fibres sorb moisture they swel and occupy progressively more space, and the air correspondingly less. This is thought to be unimportant except for very dense packages.

(vi) No account has been taken of the influence of capillarity in the air spaces. This will be appreciable only at very high humidities or in water,(vii) The fibres have been assumed to reach equilibrium with their immediate surroundings instantaneously. There is some evidence that relatively slow changes of fibre structure may occur as the moisture is taken up,and that while most of the uptake is effectively instantaneous there may be a slow drift of moisture content persisting for some time. The information on this at the moment is too sparse for it to be taken into account even if the mathematics permitted.

15.6. Solution of the equations

Using Henry's nomenclature the equations to be solved can be written

where

" dx2

J2T

d x 1 "dM/BC = a;

" = K/(ap);

dt 8T~dt

- ' dt'dM

8 d t '

dM/dT = co,

y = d-v)/(vp): g = q/a.

(15.7)(15.8)

(15.9)

358 SIMULTANEOUS DIFFUSION OF HEAT AND MOISTURE

Eliminating M, we obtain

..d2C „ dC dT= 0,

(15.10)

d2T

dT dC

v — y — (l + *;co) \-8<J— = 0,

(15.11)

dx

dt dt

which can be written more simply in the forms

d C d

(15.12)

dx dt

where the significance of D, ©, /I, and v is immediately obvious. These equations are now in a form analogous in some respect to those representing two coupled vibrations, and they may be treated in the usual manner, provided X and v are assumed constant, by the introduction of 'normal coordinates',which are linear combinations of C and T, of the form rC + sT. With proper choice of the ratio r/s, eqns (15.12) and (15.13), expressed in terms of the new coordinates, give rise to two simple diffusion equations, each containing only one of the normal coordinates. The quantities represented by the latter consequently diffuse according to the usual law, and independently of each other, just as the normal modes of vibration of coupled mechanical systems,once started, continue without mutual interference. In order to find the normal coordinates, we multiply (15.12) by r/D and (15.13) by s/®, and add,obtaining

If this is to be expressible as a simple diffusion equation for rC + sTwe must have

r/D-sv/Q) _ s/9-rX/D

r

s

i.e.

=

= a2 say.

(15.15)

D r Q) Q) s D

This is a quadratic in r/s and gives the two values of r/s required to form the two normal coordinates. Also, \i2 will have two values, corresponding to the roots of r/s. Eqn (15.14) can now be written

( r C + 5T)^( rC + sT) = 0,

(15.16)

SIMULTANEOUS DIFFUSION OF HEAT AND MOISTURE 359

which is a simple diffusion equation for rC + sT with diffusion coefficient

Vn2-

We can now determine the normal coordinates and their diffusion coefficients. Elimination of r/s between the eqns (15.15) gives

(15.17)the roots of which are

o D + Q) + J\{Q) — D)2 + 4kvDQ)\"2 -

~ v (

*-.

(15.18)

15.6.1. Diffusion rates

If we write \j\x\ = Dx and \j\i\  = D2 in order to preserve the representation of a diffusion coefficient by the letter D, and if we put DjQ) = w, then we have from (15.18)

Dx

2

D u+ 1+71(1 -u)2+4iuv} 'D2 _

2

D u-\-1

(15.19)

(15.20)

Fig. 15.2 shows a nomogram, reproduced from Henry's paper (1948) for

solving these equations. If a straight line be placed so as to cut the two

straight scales at the appropriate values for u and kv, then the points at which

it cuts the circular scale give Dx/D and D2/D respectively. To find DxjQ)

and D2/% \/u must be used in place of u. Usually it is convenient to expres

£>! in terms of D and D2 in terms of Q).

If kv is smal compared with (Q) — D)2/(4D<3), i.e. if either the coupling between the two diffusion processes is weak or D and Q) are of widely different magnitudes, the roots become

2 _ 1 kv

1 kv

(15.21)

approximately. Thus as the coupling becomes weaker \i\ tends towards 1/D, and \i\ tends towards 1/ ,̂ so that we may speak of ±ii l as the vapour roots, and ±fi 2 as the thermal roots, though when coupling exists all roots are concerned with both diffusion processes to a greater or lesser extent.

15.6.2. Expressions for concentration and temperature changes

Proceeding from eqn (15.17) or (15.18) we see that

=  l /D+1/0,

360 SIMULTANEOUS DIFFUSION OF HEAT AND MOISTURE

FIG. 15.2. Nomogram for DJD and D2/D in terms of u and AV

i.e.

Using (15.15) and (15.22) we find that

v D

\-\i\® D

X

(15.22)

(15.23)

Hence if we choose rx and s2 to be equal to unity, the normal coordinates are determined, and the solution of the differential equations (15.6), (15.7),(15.8) can be written

AC

1 _

(15.24)

SIMULTANEOUS DIFFUSION OF HEAT AND MOISTURE 361

^ C = ^2(x, y, z, t),

(15.25)

where AC and AT are the deviations of C and T from some given values(e.g. the initial), and the i//s are solutions of ordinary diffusion equations with diffusion coefficients equal to \j\i\  and \j\i\  respectively, and subject to appropriate boundary and initial conditions. Solving for C and T we get

AC = 01(x,j>,z,t)+—^-<l>2(x 9y9z9t)9

(15.26)

AT = 02(x, y, z, 0 + Y~-0i(x, y, z, r),

(15.27)

where

and

02(x, >;, z, t) = ' 2^ ^ 2 > 2 ( x , y, z, r).

(15.29)

The 0s, being proportional to the i/̂ s, are also solutions of the ordinary diffusion equation with diffusion coefficients equal to \j\i\  and \l\i\  respectively,and with boundary and initial conditions which give the required conditions for C and T.

The physical interpretation of these equations derived by Henry is that each diffusion 'wave' of vapour is accompanied by a temperature 4wave'proceeding at the same rate, whose magnitude is proportional to that of the vapour diffusion wave, the relation between the two depending only upon the properties of the materials. Similarly, the main temperature 'wave' is accompanied by a subsidiary vapour diffusion wave. Even if only one of the external conditions, say the vapour concentration, alters, there will nevertheless be the complete set of two vapour 'waves' and two temperature 'waves',though the latter may be smal if the coupling is weak.

Henry points out that similar reasoning to that just given still holds if eqns (15.12) and (15.13) have on their right-hand sides, instead of zero, any functions of the independent variables x,y, z, and t. Such equations would correspond to the case where either the diffusing substance or heat, or both,are being set free or absorbed in a manner additional to and independent of the diffusion processes, and independent of C and T. There might, for example,be a chemical reaction causing both the diffusing substance and heat to be evolved throughout the medium. In such cases the solution to the problem of the simultaneous transfer of heat and vapour reduces to the sum of solutions

362 SIMULTANEOUS DIFFUSION OF HEAT AND MOISTURE

for the ordinary diffusion of the 'normal coordinates1 with appropriate rates of evolution throughout the medium of the quantities they represent.

15.6.3. Solutions for sudden changes of external conditions

The above equations enable the solution of the coupled diffusion problem to be obtained in terms of the solution for the ordinary diffusion problem with the same boundary conditions. Suppose a specimen of any shape is in equilibrium with its surroundings and that at time t = 0 the concentration C and temperature T of the diffusing substance are suddenly altered to C + A0C and T+A0Trespectively at the boundary, and maintained constant.

Let the solution to the simple diffusion problem, assuming diffusion constants

AC = A0Cj\(x,y,z,t\

(15.30)

AT = A0Tf2(x,y9z,t).

(15.31)

The specimen eventually reaches equilibrium with the new conditions so that

fx and f2 must increase from 0 to 1 as t increases from 0 to infinity. The form

of these functions depends on the shape of the specimen and typical solutions

have been given in earlier chapters for plane sheets, cylinders, and spheres, for

example. Clearly fx and f2, multiplied by suitable constants depending upon

the initial conditions at the boundary, are the functions <j) i and <j> 2 in eqns(15.26) and (15.27). Thus, remembering that the system must eventually come

to equilibrium with AC = A0C and AT = A0T, and that fx and f2 are then

both unity, we find

AC=

^

2

2I{(l1 — jX2)

(15.32)

(15.33)An alternative form of these equations, put forward by Henry (1939) is

4C , 4oC/l J iz i fW- iM, h _,,,.

(15.34|

AT ATf P

AT = A0Tf2

The first term on the right-hand side of each equation represents the 'wave'which would result if there were no coupling between the diffusion processes and which may be referred to as the 'permanent wave'. The second term

SIMULTANEOUS DIFFUSION OF HEAT AND MOISTURE 363

represents the result of the coupling and may be called the 'temporary wave'since it starts at zero, increases to a maximum, and then diminishes to zero again.

In many cases it is required to know the rate at which the amount of diffusing substance absorbed M varies. To determine this we substitute

AM = GAC-OJAT

(15.36)

in (15.34) and (15.35), and after some rearrangement we obtain AM = A0Mfx + { Itf--- — I Ao

1 1

W'~~~Dr'

t*i-l

(15.37)

where from (15.10) and (15.12)

D" = D(l+ya),

(15.38)

and from (15.11) and (15.13)

0" = 0(l+eco).

(15.39)If it is desired to include both the amount absorbed and the amount in the pores, and M' is the total amount of diffusing substance contained in unit mass of solid, then from (15.36) and the definition of y in (15.9) we obtain

AM ' = 1+ —I AM+ — AT,

(15.40)

yo) yo

which may be evaluated using (15.35) and (15.37). If ycr is large, i.e. if much more diffusing substance is absorbed by the solid than is contained in the pores, M' is nearly equal to M and (15.40) is not needed. Henry points out that

this is so for baled cotton, for example, for which yo may be as much as 7000. In this case also, since the terms in the expression (//? — 1/D — eco/^") occurring in (15.37) nearly cancel if eco is fairly large compared with unity, e.g. for cotton it is about 10 or 30, (15.37) may be written approximately

a> AOT\ (/2 - / , ) ,

(15.41)

J

where u is written for D/0. Here co A0Tis the total change in the equilibrium value of M which would be produced by the change in temperature A0T, if C remained constant. Henry (1939) has given numerical values of the various

constants involved in the above equations for the case of baled cotton at densities 0-2, 0-4, 0-6g/cm~3 and has written (15.40) in numerical form for

each density.

364 SIMULTANEOUS DIFFUSION OF HEAT AND MOISTURE

15.6.4. Change in external humidity only

Henry (1948) has explored further the case in which no change is made in the external temperature, only the external humidity being changed. Then we can put A0T = 0 in eqn (15.32) and by substituting \/D1 and 1/D2 for\x\ and \x\ respectively, and then rearranging we obtain for the ratio of the change in C at any instant to the equilibrium value of the change,

AC = P1 U > 2 - P ) /1 - P2 ( P1 - D ) / 2

P)

A0C

This can be written very simply as

AC/A0C = ( l -p ) /1+p /2 ,

(15.43)

where

Thus p is a dimensionles quantity that can be expressed in terms of the ratios DJD and D2/D. We have already seen in eqns (15.19) and (15.20) that these ratios can be calculated directly from u = D/2 and Av, and so p can also be obtained from u and Av. The necessary relationship is

(2p- l )2 = , ( " ~ ^ ..

(15.45)

(w—1) +4wvA

Henry's nomogram (1948) for calculating p in terms of u and Av is reproduced in Fig. 15.3. Since the right-hand side of (15.45) is unaltered if 1/w is substituted for w, the scale for u from 1 to oo enables all possible values of u to be dealt with. It also follows from this symmetry that the same numerical value for p can be used to handle the problem in which the external temperature is changed instead of the humidity.

Putting A0T = 0 in (15.41), we get

4 M - / , - " ! £ ' : •' •' • . - ••

u2

A0M

where

Henry's nomogram for calculating n in terms of u and 1/(1 + sco) is reproduced in Fig. 15.4. Under the conditions for which (15.41) and (15.46) apply we have

u

(l+w)2(l+eo;) + i/

' *

= 1/(1—Av),

(15.48)

approximately.

SIMULTANEOUS DIFFUSION OF HEAT AND MOISTURE 365

- 0 0

-005

- 01

-015

- 0 -2

FIG. 15.3. Nomogram for p in terms of u and Av.

Henry has given a table of values of p and n and also of the diffusion coefficients D, % Dl9 D2 for cotton packages of two densities and three relative humidities and temperatures. For the experimental data on which his calculations are based his original paper (1948) should be consulted. The two densities are 0-2gcm~3 and 0-5 gem"3 at temperatures 20°C, 50°C,and 80 °C, and the relative humidities (R.H.) are 20 per cent, 65 per cent, and 90 per cent. The results are shown in Table 15.1, reproduced from Henry's paper (1948), the significance of the figures being clear from the labelled cells.

Figures for 80 °C and 90 per cent relative humidity are omitted because under these conditions the vapour pressure would be a considerable fraction of atmospheric pressure, and fluid flow would make an appreciable contribution to the process. From this table and eqns (15.43) and (15.46), it is a simple matter to calculate how concentration and total moisture content vary for a package of known size and shape. When dealing with total moisture content,/j and f2 are, of course, functions only of time. As an example, suppose the package is in the form of a large flat sheet then we have (§ 4.3.2, p. 48)

(15.49)

366 SIMULTANEOUS DIFFUSION OF HEAT AND MOISTURE

O-O-i

0 - 5 -

1 0-

2 0 -

( '_

3 0 :

40-50-

1 0 -

20-=

1 0 0 -

FIG. 15.4. Nomogram for n in terms of u and AV or 1/(1 +EOJ).

where m = ^D^/l2,1 being the thicknes of the sheet. The function f2 is the same with Dx replaced by Z)2.

The following points about the solutions are of particular interest.

(i) In Table 15.1 it is seen that, as the temperature rises, the moisture diffusion coefficient D, which is at first much smaller than the thermal diffusion coefficient % eventually becomes much larger. Furthermore, the diffusion coefficient Dx for the slower normal function is always less than either D or Q) but never by a factor of less than \. On the other hand, D2 is always much greater than D or Q). The figures for n show that the secondary wave is of very smal amplitude, as judged by the total moisture content, at low temperatures, but becomes appreciable at high temperatures. The figures for p show that in the case of an external thermal disturbance only, the secondary wave may be important even at room temperatures.

(ii) Since both j \ and f2 always change from 0 to 1 we see from (15.35) that the change in temperature associated with an external change of humidity only (A0T = 0), is a transient one, which increases from zero to a maximum

SIMULTANEOUS DIFFUSION OF HEAT AND MOISTURE 367

and disappears again. This transient temperature has been observed by Cassie and Baxter (1940).

(iii ) If the initial disturbance is one of temperature only there is a corresponding transient change in moisture content.

(iv) The effect of size or shape is all included in the function / and so conversion from one package to another is relatively simple. In particular t and / always appear as t/l2 in (15.49), for example, and we have the usual dependence of the time scale on the square of the linear dimensions, familiar in simple diffusion problems.

(v) For comparisons of calculated and experimental values the papers of Cassie and Baxter (1940) and of Daniels (1941) should be consulted. The former describes a pure diffusion experiment, the latter a flow-under-pressure experiment with diffusion as a complicating feature. It is not to be expected that the theoretical treatment of a subject as complicated as this can reproduce all the features accurately and quantitatively. Its value lies in clarifying the mechanism by which heat and moisture are transferred, in making possible rough estimates of time scales under given conditions, and in particular,showing how the times for a given package can be estimated from measurements on a standard package.

15.7. Surface temperature changes accompanying the sorption of vapours

A much simpler problem, but one of practical interest, is to calculate the temperature change which accompanies the sorption of vapour by a solid,in cases where the temperature rises due to the heat of condensation given up at the surface of the solid and the heat of mixing can be neglected.

We consider a plane sheet suspended in a vapour maintained at constant pressure. The sheet is taken to be so thin that effectively all the vapour enters through the plane faces and a negligible amount through the edges. Uptake of vapour therefore occurs by uni-directional diffusion through the sheet and the amount taken up is assumed proportional to the square root of time.

The heat of mixing is taken to be a negligible fraction of the heat of sorption which thus becomes simply the heat of vaporization. This assumption carries the implication that during sorption heat is evolved only at the two surfaces of the sheet. Values of heat conductivity, specific heat, and density of the sheet are taken to be constant, independent of temperature and vapour content. The calculated results are based in the first place on the assumption that heat is lost from the surfaces by radiation only, according to Stefan's law. For smal temperature differences, however, both radiation and convection losses proceed at rates directly proportional to the temperature difference between the surface and its surroundings, and so convection losses can be allowed for by adjusting the radiation constant.

368 SIMULTANEOUS DIFFUSION OF HEAT AND MOISTURE

15.7.1. Mathematical equations

Taking 9 to be the temperature difference between an element of the sheet and the vapour in which the sheet is suspended, 0o the temperature of this vapour assumed constant, x the space coordinate perpendicular to the surface of the sheet (the surfaces being at x = 0 and x = /), and t the time during which uptake of vapour has occurred, the equation governing the conduction of heat through the sheet is

d9 _ K d2

dt pot dx

Here K is heat conductivity, p density, and a specific heat of the substance of the sheet, all expressed in c.g.s. units. At each surface, heat is continuously evolved, as vapour is taken up, at a rate given by \p\h dR/dt, where R is the regain at time r, i.e. mass of vapour taken up per unit initial mass of sheet, and L the heat of vaporization. Some of this heat is lost by radiation from the surface at a rate which for smal temperature differences is given by k6,where k = 4ao6l and o0 is Stefan's constant. The remainder of the heat enters the sheet by conduction at a rate given by — K d6/dx. The equation expressing conservation of heat at the surface .x = 0 is therefore

2.

(15.50)

^ k d + K8^- = 0, x - 0.

(15.51)

dt

ex

There is a corresponding condition for the surface x = /, but for purposes of calculation it is preferable to consider only half the sheet and to use the condition

dO/dx = 0, x = \l

(15.52)because the uptake of vapour and the heat flow are symmetrical about the central plane of the sheet. We need therefore to evaluate solutions of (15.50)with the boundary conditions (15.51) and (15.52) and the initial condition

0 = 0, 0 < x < £/, t = 0.

(15.53)

We consider the regain JR at time t to be given by R = B{t/12)K

(15.54)

where B is a constant for a given experiment. It follows from eqn (4.20), for example, that

B = 4C0(D/n)K

(15.55)

where Co is the equilibrium regain attained theoretically after infinite time,and D an average diffusion coefficient for the concentration range 0 to Co of vapour. The constant B is thus dependent on the experiment considered, i.e.

on the system, the temperature and the vapour pressure, but is independent of the thicknes of the sheet.

SIMULTANEOUS DIFFUSION OF HEAT AND MOISTURE 369

On introducing the non-dimensional variables

K<x.y 0

Kt

p J BV

pa/2'

(15.56)and substituting for R in (15.51) from (15.54), eqns (15.50), (15.51), (15.52),and (15.53) become

dcj) d 0 3T

dX2'

1 kl ± dcj)

—_ 0_̂ —Z. = o, X = 0,

T > 0,

dcfrldX = 0, X = i

0 = 0, 0 < X < 1,

= 0.

(15.57)

(15.58)

(15.59)(15.60)When expressed in terms of the new variables 0, X, and T, the problem therefore contains only a single non-dimensional parameter kl/K, which we denote for convenience by h. A number of solutions of eqn (15.57) satisfying(15.58), (15.59), and (15.60) have been evaluated for different values of h,

0-8 r

0-7

0-6

0-5

o-4

0-3

0-2

01

0-2 0-4 0-6 0-8 10 1-2 1-4 1-6 1-8 20

00

FIG. 15.5. Variation of surface temperature with (time)*. Numbers on curves are values of

h = kl/K.

370 SIMULTANEOUS DIFFUSION OF HEAT AND MOISTURE

using the numerical methods described in Chapter 8. The calculated surface

temperatures are shown graphically in Fig. 15.5, and together with the two special cases for K = oo and K = 0 they constitute the solution of this

problem for all values of the physical properties involved. For convenience of

scale in Fig. 15.5, (kl(x/p)*(9/BL) is plotted against (kt/lpa)*. These variables

are respectively h*(j) and (hrf and hence are readily deduced from <j>  and T for a given h.

15.7.2. Special cases of zero and infinite conductivity

While the case of zero heat conductivity may be of littl e practical significance it is nevertheles a useful limiting solution from the mathematical point of view. When K = 0, no heat penetrates the sheet and we are concerned

only with eqn (15.51) which becomes

y

= k6.

(15.61)For the particular case of R given by (15.54), integration of (15.61) leads immediately to

S

(1562)

When K is infinite the temperature is always uniform throughout the sheet and some of the heat evolved at the surface is lost by radiation while the rest raises the temperature of the whole sheet. This is expressed by the equation

^plL = 2/c0 + / p a ^,

(15.63)

at

at

which becomes

^A«L

(15.64)

(15.65)

At Ipa

on substituting for R from (15.54). The solution of (15.64) is

-

2kt\ f 1

Ipa

ti exp

2k,

When expressed in terms of the variables h^cj) and hr used in Fig. 15.5, eqn(15.65) becomes

=  exp(-2/ i i) f exp(2/2T1)d(/?iTf)-Jo

Tabulated values of the right-hand side of (15.66) are given by Sakamoto

(1928) for values of  (/IT)* in the range 0 < 2hz < 100. The solution (15.66) is shown as the curve marked K = oo in Fig. 15.5.

SIMULTANEOUS DIFFUSION OF HEAT AND MOISTURE 371

15.7.3. Calculated results. General solution in non-dimensional variables

In Fig. 15.5, \v<\> is plotted against (/IT)* for different values of h = kl/K.

Since both variables and the parameter h are non-dimensional, the variation of surface temperature with time can be deduced from this figure for any system (subject to the basic assumptions) by inserting appropriate values of the physical constants involved.

The following general points are of interest.

(a) For any finite conductivity the surface temperature rises discontinuuously at t = 0 to some finite value and immediately afterwards begins to fall.

(b) For the smaller values of h, i.e. larger conductivities, the surface temperature passes first through a minimum and later through a maximum before falling eventually to the temperature of the surroundings. The initial fall in temperature occurs while the sheet is behaving semi-infinitely with respect to heat flow. The temperature rises when an appreciable amount of the heat entering the sheet through its second surface reaches the surface under consideration. The later maximum in surface temperature occurs when heat is removed from the surface by conduction and radiation (and possibly convection) as quickly as it is given up by the vapour entering the sheet. It is to be remembered that the rate of uptake of vapour, and hence the rate of

supply of heat to the surface, steadily decreases, being proportional to l/^/t.

It is to be expected that the smaller the heat conductivity of the sheet the longer the time that elapses before the heat from one surface reaches the other and hence the later the minimum temperature occurs.

(c) For h > 1 no minimum or maximum temperatures occur, but the surface temperature falls continuously for t > 0, so that theoretically the highest temperature is achieved instantaneously at zero time.

(d) When the conductivity is infinite, the surface temperature rises continuously from that of the surroundings up to a maximum and then falls.

For zero conductivity the surface temperature is theoretically infinite at t = 0 and then falls steadily.

(e) To within the accuracy of plotting, the maximum temperature can be deduced from the curve for K = oo even if the conductivity is finite, provided kl/K < 0-2 approximately.

(f) For a given sheet the temperature change in degrees is proportional to the heat of vaporization L and also to the constant B. We have seen in eqns (15.54) and (15.55) that B is the gradient of the linear plot of regain against (t//2)% and is also proportional to the product of the equilibrium regain and the square root of an average diffusion coefficient.

The following are two examples of the use of the general solution.

(i) Effect of thickness. As an example of the use of the curves of Fig. 15.5 we have calculated the way in which the temperature at the surface of a polymer sheet varies with time as it takes up vapour, and how this depends on

372 SIMULTANEOUS DIFFUSION OF HEAT AND MOISTURE

thickness. The following values are taken as representative of a variety of polymers and vapours:

p = 1-0, a = 0-35, L = 100,

K = 4-5 x l ( T \

k = 1-6x10"

all in c.g.s. units. The value of k comes from Stefan's constant and relates to an ambient temperature of 35 °C. The value B = 710 x 10"5 has been used. It corresponds to a system in which the equilibrium regain is 5 per cent and the average diffusion coefficient is

4 x l O " 7c m2s -1 .

Temperature-time curves are plotted in Fig. 15.6 for a number of thicknesses.

For a sheet 007 cm thick the maximum temperature change is approximately 14 °C at about 65 s. The maximum temperature is lower and occurs later,the thicker the sheet, but for a sheet as thick as 5-66 cm the highest temperature is 0-25 °C attained at t = 0. We note incidentally that in theory for all thicknesses the surface temperature changes instantaneously by 0-25 °C at the beginning of sorption. As we have already mentioned, corresponding curves for other equilibrium regains in the same system can be deduced from those of Fig. 15.6 since 6 is directly proportional to B and hence to Co.

200

1000

Time (s)

FIG. 15.6. Variation of surface temperature with time, shown as exces over 35 °C. Numbers on curves are sheet thicknesses in centimetres, a = 0-35, L = 100, p = 1, B = 71 xlO~5,/c = 1-6 x 10~4, K = 4-5 x 10~4. All units are c.g.s.

SIMULTANEOUS DIFFUSION OF HEAT AND MOISTURE 373

(ii) Limiting rate of sorption for 1 °C rise in surface temperature. G. S. Park suggested that, from an experimental point of view, it is useful to know what is the fastest sorption or alternatively the greatest regain for which the rise in surface temperature does not exceed 1 °C. Accordingly, in Fig. 15.7 are plotted curves which show how the limiting value of B for a 1 °C rise in temperature depends on the thicknes of the sheet. The thicker the sheet the faster the sorption permissible.

00

FIG. 15.7. Upper limits of B for surface temperature rise of 1 °C. Numbers on curves are values of k. I is the thicknes of the sheet in centimetres, a = 0-35, L = 100, p = 1, K = 4-5 x 10"4. All units are c.g.s.

The three curves of Fig. 15.7 are for different values of the emissivity constant k. The middle of the three corresponds to a surface loss purely by radiation when the temperature of the surroundings is 35 °C. Changes in k may be due to differences in ambient temperature 60 since k = 4(jo0l.

Alternatively a higher value of k can correspond to some loss of heat by convection in the vapour, since both the convective term and the radiation term in the heat loss are directly proportional to temperature difference for smal temperature excesses. Thus the curve on Fig. 15.7 for k = 64 x 10~4 could correspond to an experiment in which a stream of vapour is passed over the surfaces of the sheet.

374 SIMULTANEOUS DIFFUSION OF HEAT AND MOISTURE

15.8.

Ash and Barrer (1963) give expressions for the continued flow of matter and heat in the gas phase, surface phase, and intracrystalline phase simultaneously, using the equations of irreversible thermodynamics.

TABLES

TABL E 2.1

Table of the error function and associated functions

X

0 005 01

0-1 5

0-2

0-2 5

0-3

0-3 5

04 045 0-5

0-5 5

0-6 065 0-7

0-7 5

0-8

0-8 5

0-9 095 10 1-2 L-3 L4 1-5 1-6 L-7 L-8 L-9 20 2-1 2-2 2-3 24 2-5 2-6 2-7 2-8 2-9 SO

e*  erf c x 10

0946 0 0-896 5 0-850 9 0809 0 0-770 3 0-734 6 0-701 5 0-670 8 0-642 3 0-615 7 0-590 9 0-567 8 0-546 2 0525 9 0-506 9 0489 1 0-472 3 0456 5 0441 6 0427 6 0401 7 0-378 5 0-357 6 0-338 7 0-321 6 0306 0 0-291 7 0-278 6 0-266 5 0-255 4 0-245 1 0235 6 0-226 7 0-218 5 0-210 8 0-203 6 0196 9 0190 5 0184 6 0179 0

0

0112 6 0-223 4 0-331 0 0433 6 0-530 0 0-618 8 0-698 8 0-769 2 0-829 4 0-878 8 0-917 2 0-944 7 0-961 4 0-967 8 0-964 4 0-952 0 0931 4 0-903 5 0-869 5 0-830 2 0-740 3 0-641 6 0-541 3 0-445 0 0-356 8 0-279 1 0-213 2 0159 1 0116 0 0082 7 0057 6 0039 3 0026 2 0017 1 0010 9 0006 8 0004 2 0002 5 0001 5 0000 8

1128 4 1125 6 1-117 2 1103 3 1084 1 1060 0 1031 3 0-998 3 0-961 5 0-921 5 0-878 8 0-833 8 0-787 2 0-739 5 0-691 3 0-642 9 0-595 0 0-547 9 0-502 0 0457 6 0415 1 0-336 5 0-267 3 0-208 2 0158 9 0118 9 0087 2 0062 7 0044 2 0030 5 0020 7 0013 7 0008 9 0005 7 0003 6 0002 2 0001 3 0000 8 0000 4 0000 3 0000 1

erf x

0

0-05637 2 0-11246 3 016799 6 0-22270 3 0-27632 6 0-32862 7 037938 2 042839 2 047548 2 0-52050 0 0-56332 3 0-60385 6 0-64202 9 0-67780 1 0-71115 6 0-74210 1 0-77066 8 0-79690 8 0-82089 1 0-84270 1 0-88020 5 0-91031 4 0-93400 8 0-95228 5 0-96610 5 0-97634 8 0-98379 0 0-98909 1 0-99279 0 0-99532 2 0-99702 1 0-99813 7 0-99885 7 0-99931 1 0-99959 3 099976 4 099986 6 0-99992 5 0-99995 9 0-99997 8

erf c x

10

0-94362 8 0-88753 7 0-83200 4 0-77729 7 0-72367 4 0-67137 3 0-62061 8 0-57160 8 0-52451 8 047950 0 043667 7 0-39614 4 0-35797 1 0-32219 9 0-28884 4 0-25789 9 0-22933 2 0-20309 2 017910 9 0-15729 9 011979 5 008968 6 006599 2 0-04771 5 003389 5 002365 2 001621 0 001090 9 000721 0 000467 8 000297 9 000186 3 000114 3 000068 9 000040 7 000023 6 000013 4 0-00007 5 000004 1 000002 2

2 ierf c x 1-128 4 1031 2 0-939 6 0-853 7 0-773 2 0-698 2 0-628 4 0-563 9 0-504 3 0449 5 0-399 3 0-353 5 0-311 9 0-274 2 0-240 2 0-209 7 0-182 3 0158 0 0136 4 0-117 3 0100 5 0072 9 0052 1 0036 6 0025 3 0017 2 0011 5 0007 6 0004 9 0003 1 0002 0 0001 2 0000 7 0000 4 0000 2 0000 1 0000 1

376

TABLE S

TABL E 2.1 (contd.)

X

0 005 01 015 0-2

0-2 5

0-3

0-3 5

0-4

0-4 5

0-5

0-5 5

0-6 065 0-7

0-7 5

0-8

0-8 5

09

0-9 5

10 11 1-2 1-3 1-4 1-5 1-6 1-7 1-8 19 20 21 2-2 2-3 24 2-5 2-6 2-7 2-8 2-9 30

4 i 2erf c x 10

0-892 1 0-793 6 0-704 0 0-622 7 0-549 1 0-482 8 0-423 3 0-369 9 0-322 3 0-279 9 0-242 3 0-209 0 0-179 8 0-154 1 0131 6 0112 0 0095 0 0080 3 0-067 7 0056 8 0039 6 0-027 2 0018 4 0012 2 0008 0 0005 2 0003 3 0002 1 0001 3 0000 8 0000 5 0000 3 0000 2 0000 1

6 i 3erf c x 0-564 2 0-493 3 0-430 1 0-374 0 0-324 3 0-280 5 0-241 8 0-207 9 0-178 2 0152 2 0129 7 0110 1 0093 2 0078 7 0066 2 0055 5 0046 4 0038 6 0-032 1 0026 5 0021 8 0014 7 0009 7 0006 3 0004 1 0002 6 0001 6 0001 0 0000 6 0000 3 0000 2 0000 1

8 i 4erf c x 0-2 5

0-214 8 0184 1 0-157 3 0134 1 0113 9 0096 5 0081 6 0068 7 0-057 7 0048 4 0040 4 0033 6 0027 9 0023 1 0019 0 0015 6 0012 8 0010 4 0008 5 0006 9 0004 5 0002 9 0001 9

0001 1 0000 7 0000 4 0000 3 0000 2 0000 1 0000 1

10i 5erfc x 0094 0 0079 5 0067 1 0056 4 0047 4 0039 6 0-033 1 0027 5 0022 8 0018 9 0015 6 0012 8 0010 5 0008 6 0007 0 0005 7 0004 6 0003 7 0003 0 0002 4 0001 9 0001 2 0000 7 0000 4 0000 3 0000 2 0000 1

12i 6erfc x 0-031 3 0026 1 0021 7 0018 0 0014 9 0012 3 0010 1 0008 3 0006 8 0005 5 0004 5 0003 6 0002 9 0002 4 0001 9 0001 5 0001 2 0001 0 0000 8 0000 6 0000 5 0000 3 0000 2 0000 1 0000 1

ierfc x = | erfc f d£ = —z e *2 — x erfc x

- \ :

i 2 e r f c x = I ierfc £d£ = {\{\ + 2 x 2 ) e r f c x - ~ x e~

/.oo

2n i"erf c x = In \ in~l erfc <̂  d^ = i"  ~ 2erf c x - 2x i"" l erfc x.

^ X

- 2 x i e r f c x )

TABLES

377

TABL E 2.2

Table of Laplace transforms

v(p)= f Q~ptv(t)dt

Jo

We write q = J(p/D). D, x and h are always positive, a is unrestricted.

v(p)

v(t)

-7TT> v > " I

sin wf

cos cot

10.

11.

12.

13.

IIT* . - 0 , 1 , 2,

q + h

erfc2(-re-*2/4D'-xerfc *

xM

x

H

erfc —:

x

2DJ 2y/(Dt)

n'f erfc2y/(Dt)

nt

378

TABLES

TABL E 2.2 (contd.)

v(p)

v(t)

14.

15.

16.

pq{q + h)

1

x 1 ,

- erfc —:

e*

h 2y/{Dt) h.

17.

18.

(q + h)2

-2h

h2 2j(Dt) h\n

19.

20.

21.

22.

23.

24.

p-<x

I v{qx')Kv{qx), x > x I v(qx)Kv(qx'), x < x K0(qx)

— exlp

P

- — {l-hx-2h2Dt}ehx

+ Dth2

(a/D) erfc

I e- u W > / 4 D ,7 / i ^

2t

v\2Dt

x"8Dr

^2

, v ^ 0

1

27e

-x2l4Dt

TABLES

379

TABL E 2.2 (contd.)

v(p)

v(t)

25.

26.

27.

28.

r00

du

> 0

v ^ 0

Fractiona l uptak e

0 01 0-2 0-3 0-4 0-5 0-6 0-7 0-8 0-9 10

a

CO

9000 0 4000 0 2-333 3 1-500 0 1000 0 0-666 7 0428 6 0-250 0 0111 1

0

TABLE

Roots of ta n q

4i

1-570 8 1-638 5 1-715 5 1-804 0 1-907 1 2-028 8 2-174 6 2-352 1 2-570 4 2-836 3 3141 6

4-712 4 4-735 9 4-764 8 4-801 4 4-849 0 4-913 2 5003 7 5138 6 5-354 0 5-717 2 6-283 2

4.1

43

7-854 0 7-868 1 7-885 7 7-908 1 7-937 8 7-978 7 8-038 5 8-133 4 8-302 9 8-658 7 9-424 8

q

<?4

10-995 6 11005 7 11018 3 11034 4 11055 8 11085 6 11129 6 11-201 0 11-334 9 11-653 2 12-566 4

4s

14-137 2 14-145 1 14154 9 14-167 4 14-184 1 14-207 5 14-242 1 14-299 0 14-408 0 14-687 0 15-708 0

Qe

17-278 8 17-285 2 17293 3 17303 6 17-317 3 17-336 4 17364 9 17-411 9 17-503 4 17-748 1 18-849 6

TABL E 4.2

Roots of f$ tan /? = L

0 001 01 0-2 0-5 10 20 50 100

100 0

00

0

0099 8 0-311 1 0-432 8 0-653 3 0-860 3 1076 9 1-313 8 1-428 9 1-555 2 1-570 8

3141 6 3144 8 3-173 1 3-203 9 3-292 3 3-425 6 3643 6 4033 6 4-305 8 4-665 8 4-712 4

6-283 2 6-284 8 6299 1 6-314 8 6-361 6 6-437 3 6-578 3 6909 6 7-228 1 7-776 4 7-854 0

9-424 8 9-425 8 9435 4 9-445 9 9-477 5 9-529 3 9-629 6 9-892 8 10-200 3 10-887 1 10-995 6

12-566 4 12-567 2 12-574 3 12-582 3 12-606 0 12-645 3 12-722 3 12-935 2 13-214 2 13-998 1 14-137 2

15-708 0 15-708 6 15-714 3 15-720 7 15-739 7 15-771 3 15-833 6 16010 7 16-259 4 17109 3 17-278 8

380

TABLES

TABL E 5.1

Roots oftxqJ^qJ + UMn) = 0

Fractiona l uptak e

0 0-1 0-2 03 04 0-5 06 0-7 0-8 09 10

a

oo

9000 0 4000 0 2-333 3 1-500 0 1000 0 0-666 7 0428 6 0-250 0 0111 1

0

<7i

2-404 8 2492 2 2-588 8 2-696 2 2-815 9 2-949 6 3098 9 3-264 5 3-445 5 3-637 4 3-831 7

5-520 1 5-559 9 5-608 3 5-668 2 5-743 8 5-841 1 5-969 2 6-140 7 6-371 0 6-669 4 7015 6

8-653 7 8-679 3 8-710 9 8-750 8 8-802 8 8-872 7 8-970 9 9115 6 9-339 7 9-690 7 10-173 5

11-791 5 11-810 3 11-833 7 11863 4 11902 6 11-956 1 12033 4 12152 9 12-354 3 12721 0 13-323 7

Qs

14-930 9 14-945 8 14964 3 14-987 9 15019 2 15062 3 15-125 5 15-225 5 15403 1 15-764 6 16470 6

18-071 1 18083 3 18098 6 18118 3 18144 3 18180 3 18-233 4 18-318 8 18475 4 18-821 5 19-615 9

TABL E 5.2

Roots ofpjW-LJoiP) = 0

L

0 001 01 0-2 0-5 10 20 50 100

100 0

00

Pi

0

0141 2 0-441 7 0617 0 0-940 8 1-255 8 1-599 4 1989 8 2179 5 2380 9 2-404 8

Pi

3-813 7 3-834 3 3-857 7 3-883 5 3-959 4 4079 5 4291 0 4-713 1 5033 2 5465 2 5-520 1

7015 6 7017 0 7029 8 7-044 0 7086 4 7-155 8 7-288 4 7-617 7 7-956 9 8-567 8 8-653 7

PA

10-173 5 10174 5 10183 3 10193 1 10-222 5 10271 0 10-365 8 10-622 3 10-936 3 11-674 7 11-791 5

Ps

13-323 7 13-324 4 13-331 2 13-338 7 13-361 1 13-398 4 13471 9 13-678 6 13-958 0 14783 4 14-930 9

Pe

16470 6 16471 2 16476 7 16482 8 16-501 0 16-531 2 16-591 0 16-763 0 17009 9 17-893 1 18-071 1

TABL E 5.3

Roots of J0(actn) Y0(bccn) - J0{bccn) Y0(aocn

b/a

1-2 1-5 2-0 2-5 30 3-5 40

ace,

15-701 4 6-270 2 3123 0 2-073 2 1-548 5 1-233 9 1024 4

act 2

31412 6 12-559 8 6-273 4 4-177 3 3-129 1 2-500 2 2080 9

47-121 7 18-845 1 9418 2 6-275 4 4-703 8 3760 8 3-132 2

62-830 2 25-129 4 12-561 4 8-371 7 6-276 7 5019 6 4181 6

aai5

78-538 5 31413 3 15-704 0 10467 2 7-848 7 6-277 6 5-230 1

Fractiona l

uptak e

0 01 02 0-3 0-4 0-5 0-6 0-7 0-8 0-9 10

oc

00

9000 0 4000 0 2-333 3 1-500 0 1000 0 0-666 7 0-428 6 0-250 0 0111 1

0

Roots

3141 6 3-241 0 3-348 5 3-465 0 3-590 9 3-726 4 3-871 1 4023 6 4181 1 4-339 5 4-493 4

TABLES

TABLE

of ta n qr

6-283 2 6-335 3 6397 9 6-473 6 6-566 5 6-681 4 6-824 6 7001 9 7216 9 7-464 5 7-725 3

6.1

3ft .

</3

9-424 8 9-459 9 9-502 9 9-556 7 9-625 5 9-715 6 9-836 9 10003 9 10-235 5 10-543 7 10-904 1

12-566 4 12-592 8 12-625 4 12-666 8 12-720 5 12-792 8 12-894 0 13042 4 13-268 9 13-613 3 14066 2

15-708 0 15-729 2 15-755 4 15-788 8 15-832 6 15-892 4 15-977 9 16108 2 16-321 1 16-683 1 17-220 8

381

18-849 6 18-867 1 18-889 1 18-917 2 18-954 1 19004 8 19078 4 19193 2 19-389 8 19-756 4 20371 3

TABL E 6.2

Roots of Pncotpn + L-1 =0

L

0 001 01 0-2 05 10 20 50 100

100 0

oo

Pi

0

0173 0 0-542 3 0-759 3 1165 6 1-570 8 2028 8 2-570 4 2-836 3 3-110 2 3141 6

Pi

4-493 4 4495 6 4-515 7 4-537 9 4604 2 4-712 4 4-913 2 5-354 0 5-717 2 6-220 4 6-283 2

Pi

7-725 3 7-726 5 7-738 2 7-751 1 7789 9 7-854 0 7-978 7 8-302 9 8-658 7 9-330 9 9424 8

P.

10-904 1 10-905 0 10-913 3 10-922 5 10-949 9 10-995 6 11085 6 11-334 9 11-653 2 12-441 4 12-566 4

Ps

14066 2 14066 9 14-073 3 14080 4 14-101 7 14-137 2 14-207 5 14-408 0 14687 0 15-552 2 15-708 0

Pe

17-220 8 17-221 3 17-226 6 17-232 4 17249 8 17-278 8 17336 4 17-503 4 17-748 1 18-663 3 18-849 6

TABL E 7.1

Numerical solutions ofd2s/dn2 = -In esln(1 + A)ds/dn subject to s = 1,

s = 0, n = +oo

= 0;

A br,

Iteration s

required

-(ds/drj)n = 0

1

00 01

0-2 0-3

04

0-5 0-6 0-7 0-8 0-9

10 11

1-2 1-3

14

1-5 1-6 1-7 1-8 1-9

20 21

2-2

0-500 10"2

4

1 212

s

1000 0-879 0-762 0-651 0-548 0455 0-373 0-301 0-240 0188 0146 0112 0084 0063 0-047 0035 0025 0019 0014 0011 0009 0007 0006

1000

io-2

8 1-286

s

1000 0-872 0-749 0-634 0-528 0435 0-353 0-283 0-223 0174 0134 0102 0076 0056 0041 0-030 0-022 0016 0011 0008 0-006 0005 0004

2000 10~2

6

1-399

s

1000 0-861 0-730 0-609 0-501 0408 0-328 0-260 0204 0158 0121 0092 0069 0051 0037 0-027 0020 0014 0011 0008 0006 0005

4000 10"2

7

1-565

s

1000 0-846 0-703 0-576 0-467 0-375 0-299 0-236 0184 0143 0110 0083 0063 0048 0036 0-027 0-021 0016 0013 0011 0011 0010

6000 10"2

8 1-699

1000 0-833 0-682 0-552 0-442 0352 0-277 0-217 0168 0128 0097 0073 0054 0040 0028 0020 0014 0010 0007 0005 0-003 0002

1000 10"2

7

1-895

5

1-000 0-815 0-655 0-521 0413 0-326 0-256 0-200 0155 0119 0091 0069 0052 0040 0030 0-023 0018 0014 0011 0009 0008

2500 10~2 8 2-389

s

1000 0-775 0-596 0460 0-357 0-277 0-214 0165 0126 0096 0072 0053 0039 0-028 0020 0014 0010 0007 0004 0003 0002

1000

io~2

10

3-576

s

1000 0-695 0-502 0-375 0-285 0-218 0167 0127 0097 0073 0055 0041 0030 0021 0015 0010 0007 0005 0004 0002

2000

io-2

10

4-464

s

1000 0-649 0458 0-339 0-256 0195 0150 0115 0088 0067 0051 0-038 0029 0021 0016 0019 0009 0007 0006

5000 5-10"3

10

6091

s

1000 0-589 0406 0-297 0-223 0169 0129 0098 0-075 0056 0042 0031 0028 0017 0012 0008 0006 0004 0002

10000 5-10"3

12 7-787

5

1000 0-545 0-371 0-271 0203 0-155 0119 0091 0070 0054 0041 0031 0024 0018 0015 0012 0009 0008 0007

15000 5-10~3

12 9027

s

1000 0-521 0-353 0-257 0192 0146 0112 0085 0065 0050 0-037 0028 0021 0016 0012 0009 0007 0005 0004

35000

10~3 14

12-38

s

1000 0474 0319 0-232 0173 0132 0101 0077 0059 0045 0034 0-025 0-019 0014

0011 0008 0006 0005

DO

rm

on

From Lee 1971.(a).

Exponential diffusion in an infinite medium; numerical values of the function y, g) oo 0-2 04 06 0-8 10 1-2 1-6 20 2-2 24

Exponential diffusion in an infinite medium; numerical values of the function y, g) oo 0-2 04 06 0-8 10 1-2 1-6 20 2-2 24

-20 _ - _ _ - - - _ - 9 •8 •7 6 •5 4 •3 •2 • 1 0 -0-9 -0-

References

384

TABLE S

TABL E 7.3

Exponential diffusion in a semi-infinite medium; numerical values of the function 1000c(j;s,g)

- 2 4 -2- 2 - 2 0 -1- i

_1. 6 - 1 4 - 1 2 - 1 0 -0- 8 - 0 6  -0- 4 -0- 2 -00 0

0 0 0 1 0-2 0-3 0-4 0-5 06 07 08 0 9•0 1•2•3•4•5•6•7•8•9 2 0

0 78 182 330 600 877 995

1000

0 81 185 325 520 775 960 997

1000

0 84 189 323 497 709 898 981 998

1000

0 87 193 322 479 660 833 944 987 998

1000

0 90 196 321 466 624 778 896 962 989 998

1000

0 93 200 322 457 600 737 851 928 970 989 996 999

1000

0 96 204 322 449 580 704 811 891 944 974 989 996 998 999

1000

0 99 207 323 443 564 678

111

857 915 953 976 988 995 998 999

1000

0 102 210 324 439 551 657 750 827 886 929 958 977 987 994 997 999

1000

0 105 214 325 435 541 639 727 800 860 905 939 961 977 986 992 996 998 999

1000

0 107 217 325 433 534 626 708 779 836 883 919 945 964 977 986 992 995 998 999

1000

0 110 220 328 430 527 614 692 759 816 862 899 928 949 965 977 985 990 994 997 998

0 112 223 329 429 520 604 678 742 797 843 880 910 934 952 966 976 984 989 993 995

+0- 4 +0- 6 + 0 8 + 1 0 +1- 2 + 1 4 + 1 6 + 1 8 + 2 0 +2- 2 + 2 4

00 0 1 0-2 03 0 4 0-5 0 6 0-7 08 0 9 10•1•2•3 4

• 5

•6•7•8•9 2 0

0 115 226 330 427 516 595 666 728 781 826 863 896 919 939 955 967 976 983 988 992

0 117 228 331 426 512 588 656 715 766 811 848 879 905 926 943 956 967 976 982 987

0 120 231 333 425 508 582 647 704 754 797 833 865 891 913 931 946 958 986 975 981

0 122 233 334 424 505 576 639 694 742 784 820 851 878 900 919 935 948 959 968 975

0 124 236 335 424 502 571 632 685 732 773 809 839 866 889 910 925 938 950 960 968

0 126 238 336 423 499 567 626 677 723 763 798 828 855 878 897 914 929 941 952 961

0 128 240 338 423 497 563 620 670 715 754 788 818 844 867 887 904 919 932 944 953

0 130 242 339 422 495 559 615 664 707 745 779 808 835 857 877 895 910 924 935 945

0 132 244 340 422 494 556 610 658 700 738 771 800 825 848 868 886 902 915 928 938

0 134 246 341 422 492 553 606 653 694 731 763 792 817 840 860 878 893 903 920 929

0 136 248 342 422 491 550 602 648 688 724 756 784 809 832 852 870 885 900 912 923

0 138 250 344 422 489 548 599 644 683 718 749

111

802 824 844 862 878 892 905 916

TABLES

385

TABL E 7.4

Linear diffusion in an infinite medium, concentration gradients-(dC/dj/a)/(C1-C2) against y, = x/{2J(D.dt)}

b = ratio of the diffusion coefficient at concentration Cx to that at C2

2-8 2-6 24 2-2

20

1-8 1-6 14 1-2 1-0 0-8 0-6 04 0-2

00-0-2

- 0 4-0-6

- 0 8

- 1 0-1-2

- 1 4-1-6

-1-8

- 2 0-2-2

- 2 4-2-6

-2-8

b = I f

0001 0-002 0-005 0010 0022 0044 0079 0134 0-208 0-298 0-394 0481 0-542 0-564 0-542 0481 0-394 0-298 0-208 0134 0079 0044 0022 0010 0005 0002 0001

b = 0-8806

0001

0-002

0005

0012

0024

0-047

0083

0136

0-207

0-292

0-384

0468

0-533

0-561

0-547

0491

0406

0308

0-212

0135

0-077

0040

0-019

0008

0-003

b = 0-7228

0001

0003

0007

0015

0028

0050

0086

0135

0-200

0-280

0-367

0452

0-522

0-560

0-558

0-511

0423

0-319

0-215

0130

0-071

0035

0015

0006

0002

b = 0-5506

0001

0002

0005

0009

0018

0032

0055

0089

0134

0195

0-268

0-348

0430

0504

0-555

0-569

0-535

0455

0-339

0-221

0125

0061

0-027

0010

0003

0001

b = 0-3270

0002

0004

0007

0013

0023

0039

0062

0092

0134

0188

0-250

0-321

0-398

0474

0-539

0-579

0-577

0-514

0-388

0-232

0108

0039

0011

0003

b = 01407 0003 0006

0011

0017

0028

0043

0066

0095

0132

0179 0-233 0-296 0-365 0439

0-513 0-578 0-621 0-607 0479

0-226 0049

0005

t The data for b = 1 represent the Gaussian curve corresponding to ideal diffusion.

386

TABLE S

TABL E 7.5

Linear diffusion in an infinite medium; relative concentration(C-C2)/(Cl-C2) against y.d = x/{2j(D.J)}

b = rati o of diffusion coefficient at concentration Cx to that at C2

2-6 24 2-2 20 1-8 1-6 14 1-2 10 08 0-6 04 0-2 00-0-2

- 0 4

- 0 6-0-8

- 1 0-1-2

- 1 4-1-6-1-8

- 2 0-2-2

b= 1

0002 0005 0012 0024 0045 0079 0129 0198 0-286 0-389 0-500 0-611 0-714 0-802 0-871 0-921 0-955 0-976 0-988 0-995 0-998 1000

b = 0-8806

0001

0003

0006

0013

0026

0048

0082

0131

0199

0-284

0-385

0495

0606

0-710

0-800

0-872

0-923

0-958

0-979

0-990

0-996

0-999

1000

b = 0-7228

0001

0004

0008

0015

0029

0051

0084

0132

0197

0-279

0-376

0485

0-597

0-705

0-799

0-873

0927

0-961

0-981

0-992

0-997

0-999

1000

b = 0-5506

0-001

0002

0005

0010

0019

0033

0055

0088

0134

0195

0-273

0-367

0-473

0-586

0-697

0-797

0-876

0-933

0-967

0-986

0-995

0-998

1000

1000

b = 0-3270

0001

0002

0004

0007

0013

0024

0039

0061

0093

0137

0194

0-266

0353

0455

0-567

0-683

0793

0-884

0-946

0-980

0-994

0-998

1000

1000

1000

b = 0-1407

0001

0003

0006

0010

0017

0028

0044

0068

0099

0139

0192

0258

0-339

0-434

0-543

0-664

0-785

0-898

0-970

0-995

0-999

1000

1000

1000

1000

TABLE S

387

TABL E 7.6

Amount of material M that has diffused through unit area of plane x = 0 up to time t, expressed as dimensionless ratio M/C0(Dar)i (Wilkins 1963)

Infinit e medium

16TC

= 0-56419(l+0-0010854£2-0-0010854£3+ ... ]£ = oo : -2y32u(0)u'(0) = 0-56486

£ = - 1: -2y32u(0)u'(0) = 0-56486

Sorption

. f 4-7T

• 0 :

— — £ +

„

£+

4n

32TT

= 1-1284(1+0068326-0-04048e2+ ...)e= oo : -2yiu'(0)= 1-2551

£ = - 1 : 2"*/"(0 ) = 0-93922

Desorption

4-7U 64-8 (7 -3^ )TC-7C 2 _e +

y ^ £

2 +

——-e +

——^

£+...

4n

32TC2

= 1-1284(1-0-06832£ 4-0-02784£2+ ...)£ = oo : 2-±/"(0) = 0-93922

£= - 1 : -2yiu'(0) = 1-2551

No.

TABL E 7.7

Some exact solutions with D concentration dependent

en

2(«+ir

n - l l

J

1 8 \— + nB]nB j

}

±?DU—(l-en0+n9en)+Bnen6[nB

Remarks

n > 0. For  minus sign Z)o ^ ™2/16

> 0. For  minus sign

Do has lower  limi t

For  minus sign

> 0. For  minus sign Do ^ TTM2 e2716

odrm

From Philip 1960.

(;-

(j u(j(j u

= 0)T

=  1)= 2)= 3)= 4)= 5)

i X

= 0000

0001

0002

0003

0004

0005

= 0= 0 0 0 0 0 0 0

i = 1 01 0-2000 0-2000 0-2000 0-2000 0-2000 02000

TABLE S

TABL E 8.1 i = 2

0-2

04000

0-4000

0-4000

0-4000

0-4000

0-3999

i = 3 0-3 0-6000 0-6000 0-6000 0-5996 0-5986 0-5971

i = 4 0-4 0-8000 0-8000 0-7960 07896 0-7818 0-7732

i = 5

0-5 10000 0-9600 0-9280 0-9016 0-8792 0-8597

38'

i = 6

0-6 0-8000 0-8000 0-7960 0-7896 0-7818 0-7732

(; = 10) 0-01 0 01996 0-3968 0-5822 0-7281 0-7867 0-7281

0 = 20) 002 0 01938 0-3781 0-5373 0-6486 0-6891

0-6486

From Smith 1965.

TABL E 8.2

F.D.S. = Finite-difference solution: A.S. = Analytical solution

x = 0-3

X = 0-5

F.D.S.

A.S.

Percentage difference

F.D.S.

A.S.

Percentage difference

0005

0-5971

0-5966

008

0-8597

0-8404

2-3

001

0-5822

0-5799

0-4

0-7867

0-7743

1-6

0-02

0-5373

0-5334

0-7

0-6891

0-6809

1-2

010

0-2472

0-2444

11

0-3056

0-3021

1-2

TABL E 8.3

x = o

o-i

0-2

0-3

0-4

0-5

Analytical

solution From Smith

7 = 000 T = 001 T = 002

T= 010 T = 0 10

1965.

0 0

0-2

01989 01936

00948 00934

0-4

0-3956 0-3789

0-1803 01776

0-6

0-5834 0-5400

0-2482 0-2444

0-8

0-7381 0-6461

0-2918 0-2873

10

0-7691 0-6921

0-3069 0-3021

390

TABLES

TABL E 9.1f

Intersections of c(y) for given a with c(y) when a = 0.

c = C/Co, D = D0(l +aC/C0), y = x/{AD.dtf

y c

y c

y c

Infinite

0-6586

0-1758

06653

0-1733

06766

01693

medium

a small,-06586

0-8242

-0-6766

0-8307

-0-6653

0-8267

Sorption tending to zero 10188 01496 a = oo

1-0012

01568 a = - 1

1-0474

01385

Desorption

10188

0-8504

10474

0-8615

10012

0-8432

t Taken from Wilkins (1963).

TABL E 10.1

Diffusion coefficients for chloroform in polystyrene at 25CC. All diffusion coefficients are in cm2 s~ l x 10~ 10

% Regain at equilibrium =

Co

50 7-5 9-9 12-9 13-2 15-1 16 3 16-8

(t/1%

s c m -2x l 0 1 0

1-130

0-620 0-288 0-248

0151 00583 00481

D

experimental

0024

(extrap.)

00437

00797

0-171

0199

0-326 0-846 0-972

1 fCo— DdC(cm2 s""1

10"10)

0024

0-0437 0-0797

0171 0199

0-326 0-846 0-972

1st Approximation

D

0024(extrap.)0116

0-288 0-780 0-970

3-36

105

160

approx.

D

calculated 0024

00504 0103

0-238 0-276 0-585

1-20

2nd

1 f *"°— DdC

C0J0( cm2sM

i o - 1 0 )

0024 0039 0062 0125 0144 0-216

0-583

Approximation

D

0024

012

0-29

0-40

0-54

1-6

6-6

D

calculated 0024

0044

0080

0-17

0-20

0-33

0-85

H

DO

r*m

392

exp K

10°

2

5

101 102 103 104 105 106 107 108

194 x 10"*1-51 x lO" 1 1-05 x 10" *78OxlO"2 2-60 x 10 '2 840x l0~3 2-69 x 10"3 8-60 x 10" 4 2-66 x lO" 4 8-36 x 10"5 2-65 x 10"5

TABLE S

TABL E 10.2 Desorption

Ti

4-90 x 10" 2 380 x l O ' 2 2-56 x 10-2 188 x lO" 2 5-OOxlO"3 1-13 x lO" 3 2-32 xlO~4 4-36 x 10-5 7-87 x l O ' 6 142 x lO" 6 248X10"7

(Fd)i

100 1 56 2-70 40

134

43-3

138-7 443

370

4300

13670

100 155

2-61

3-84 10-2 231 474 890 160-5 290

506

Absorption

1-94 x 10"l

126 x 10-l

6-60 x 10"2

3-90 x 10" 2

640x l0 "3

940 xlO" 4

M9X10"4

148xlO"5

1-74 xlO" 6

2O5xlO"7

2-35 x 10" 8

100 1-3 1-7 201 3-30 4-85 614 763 8-97 10-60 1210

From Hansen 1967.

TABL E 13.1

Values of (Dt/a2f are tabulated; Mt is the total uptake at time t; Ma corresponding amount after infinite time

the

Plane sheet

0-25 0-50 0-75

Cylinder

0-25 0-50 0-75

0-25

Sphere

0-50 075

Unlimited

1

amount

2 of solute 5 10 50%equili- 1

brium

2

uptake of 5

of solute 10 90%equili- 1

brium

2 uptake of 5 solute

10

0-275 0-549 0-825 0-325 0-650 0-976 0446 0-891 1-337 0-596 1191 1-787 0-225 0480 0-778 0-292 0-619 0-994 0436 0-915 1462 0-601 1-265 2006

0146 0-306 0-508 0102 0-216 0-367 0174 0-363 0-598 0-119 0-253 0428 0237 0495 0-814 0160 0-348 0-584 0316 0-660 1080 0-213 0460 0-772 0-119 0-261 0468 0077 0183 0-333 0-156 0-341 0606 0102 0-236 0427 0-220 0-504 0-784 0153 0-349 0-636 0-316 0-702 1-218 0-209 0483 0-867 0176 0403 0-750 0094 0-219 0443 0057 0147 0-309 0-255 0-587 1058 0137 0-320 0-634 0092 0-220 0449 0423 0-942 1-675 0219 0-522 1010 0149 0-356 0-720 0-603 1-340 2-361 0314 0-743 1435 0-213 0-514 1027

TABLE S

TABL E 13.2

Values of (Dt/a2)*  are tabulated

393

s/

Unlimited amount

of solute

50 % equilibriu m

uptake of solute

90% equilibriu m

uptake of solute

\ X/a

1

2

5

10

1

2

5

10

1

2

5

10

0-75

0-202 0-269 0-408 0-568 0-208 0-280 0-425 0-596 0-219 0-293 0-444 0-618

Plane

0-50

0-403 0-538 0-816 1136 0-430 0-582 0-889 1-248 0-482 0-644 0-980 1-375

sheet

0-25

0-605 0-808 1-223 1-705 0-668 0-908 1-397 1-972 0-818 1105 1-700 2-380

0

0-806 1076 1-631 2-273 0-923 1-270 1-970 2-786 1-328 1-850 2-928 4-125

s/Ci

Unlimited amount

of solute

50% equilibriu m

uptake of solute

90% equilibriu m

uptake of solute

ro/a

^ \1 2 5 10 1 2 5 10 1 2 5 10

Values

075

0195 0-259 0-390 0-543 0-206 0-274 0-419 0-587 0-223 0-300 0-454 0-638

TABL E

of(Dtla2f

Cylinder 0-50

0-371 0-491 0-740

1024 0-410 0-553 0-847

1190 0-509 0-683

1046

1-459

13.3

are tabulated

0-25

0-523 0-689 1028 1-427 0-601 0-811 1-247 1-750 0-853 1-167 1-796 2-549

0-75

0187 0-246 0-375 0-522 0-202 0-268 0-412 0-580 0-230 0-309 0-467 0-655

Sphere 0-50

0-344 0-453 0-678 0-942 0-390 0527 0-808 1132 0-533 0-718 1098 1-538

0-25

0-468 0608 0-910 1-242 0-548 0-736 1123 1-569 0-850 1171 1-806 2-535

394

TABLES

TABL E 14.1

Values of MJM., for fia2/D = 0-01

^ \

n

DfAK + l V i * ^ ^ ^0005

001

002

004

006

008

010

0-15

0-2

0-3

04

0-5

10

1-5

20

2-5

50

7-5

10

15

20

40

60

80

Plane 10

0024

0034

0048

0067

0079

0086

0091

0099

0104

0114

0123

0133

0178

0-220

0-261

0-299 0-463 0-588 0-685

0-815 0-891

0-987 0-998

1000

sheet

100

0009

0013

0021

0036

0051

0065

0079

0114

0147

0-210

0-268 0-322 0-537 0-683 0-782 0-850 0-977 0-996 0-999

1000

Cylinder

10 0043 0058 0074 0088 0093 0096 0099 0-104 0108 0118 0128 0-137 0183

0-226 0-267 0-306

0-471

0-597 0-693 0-822 0-896 0-988 0-999

1000

100 0012 0017 0026 0043 0060

0-077

0094 0133 0172

0-243 0-308 0-368 0-597 0-743 0-836 0-895 0-989 0-999

1000

Sphere

10 0057 0073 0086 0093 0096 0098 0100 0105 0109 0119 0129 0138 0184

0-227 0-269 0-307 0-473 0-599 0-695 0-823 0-898 0-989 0-999

1-000

100 0013 0018 0027 0046 0064 0081 0099 0140 0180

0-254 0-322 0-383

0616 0761 0-851

0-907

0-991

0-999

1000

TABL E 14.2

Values of MJM  ̂ for na2/D= 0-1

\

DrAK + l j a 2 ^ ^0005

001

002

004

006

008

010

015

0-2

0-3

04

0-5

10

1-5

20

2-5

50

7-5

10

15

20

40

1 0-057 0080 0113 0160 0197 0-227 0-254 0-310 0-354 0-418 0-459 0-488 0-559 0-601 0-638 0-671 0-797 0-875 0-923 0-971 0-989 1000

Plane sheet 10

0025

0035

0052

0076

0095

0112

0128

0164

0198

0-261

0-320

0-374

0-585

0-724

0-816

0-877

0-983

0-998

1000

100 0017 0032 0062 0116 0166 0-211 0-253 0-343 0-418 0-536 0-626 0-696 0-889 0-959 0-985 0-994 1000

1 0108 0149 0-205 0-277 0-327 0-365 0-395 0-445 0-476 0-507 0-524 0-535 0-579 0-619 0-655 0-687 0-809 0-884 0-929 0-974 0-990 1000

Cylinder

10

0044 0-060 0081 0106 0125 0143 0159 0-200 0-238 0-309 0373 0-432 0-652 0-786 0-868 0-919 0-993 0-999 1000

100 0029 0054 0101 0188 0-265 0-333 0-394 0-519 0-615 0-748 0-832 0-887 0-983 0-997 1000

1 0155 0-210 0-279 0361 0-409 0-441 0-463 0-494 0-508 0-522 0-532 0-542 0-585 0-624 0-660 0-692 0-813 0-886 0-931 0-974 0-990 1000

Sphere

10 0059 0076 0095 0-117 0136 0153 0171 0-212 0-252 0-325 0-391 0-451 0-672 0-804 0-883 0-930 0-995 1000

100 0-037 0068 0-127 0-232 0-324 0-404 0-474 0-613 0-712 0-838 0-907 0-946 0-996 1000

CO

rm

TABL E 14.3

Values of MJMn for fia2/D = 1-0

><*

Dt/(R + l)a2 \ ^0005

001

002

004

006

008

010

015

0-2

0-3

0-4

0-5

10

1-5

20

2-5

50

7-5

1 0057 0081 0115 0164 0-203 0-237 0-267 0334 0390 0-481 0553 0-613 0-804 0-900 0-948 0-973 0-999 1000

Plane sheet 10

0028

0045

0075

0131

0181

0-226

0268

0-358

0-432

0-549

0-637

0-707

0-895

0-962

0-986

0-993

1000

100 0045 0081 0136 0-210 0-264 0-309 0348 0430 0-497 0607 0691 0-758 0927 0-978 0-994 0998 1000

1 0109 0151 0-208 0-285 0-341 0-385 0-423 0495 0-549 0-630 0-691 0-741 0-891 0-954 0-980 0-992 1000

Cylinder

10 0051 0079 0129 0-217 0295 0363 0-423 0-547 0-638 0-768 0-848 0-898 0986 0-998 1000

100 0085 0151 0250 0-378 0-465 0-531 0-587 0692 0-767 0866 0-923 0-955 0-997 1000

1 0155 0211 0-283 0-371 0-429 0471 0504 0-564 0-608 0-676 0-732 0-777 0912 0965 0986 0995 1000

Sphere

10 0070 0105 0166 0-273 0-366 0-445 0514 0-648 0-743 0-860 0-922 0-956 0-997 1000

100 0120 0-212 0-346 0-510 0613 0-687 0-743 0-840 0-899 0959 0-983 0-993 1000

Wrm on

TABLE S

397

TABL E 14.4

Values of MJM  ̂ for fia2/D = 10

Dt/(R + \)a2

0-005 001 002 004 006 008 010 015 0-2 0-3 04 0-5 10 1-5 20 2-5 50

R -

\

Plane sheet 1

0059

0085

0126

0190

0-242

0-288

0-329

0-414

0-484

0-595

0-680

0-746

0-920

0-975

0-992

0-998

1000

Cylinder 1

0112 0159 0230 0336 0420 0-489 0-547 0660 0-740 0-845 0-906 0-943 0-995 1000

Sphere

1

0160 0-224 0-316 0-448 0-546 0-623 0686 0-796 0-865 0-939 0-972 0-987 1000

TABL E 15.1

Diffusion coefficients and amplitudes

20° C

50° C

80° C

20° C

50° C

80° C

20%

4-5 4-1

28 18 140

39 0094

0-34

0-21

R.H.

34

130 41 180

49

420

00037

0050

0-20

p = 0-2 g cm 3

65?

31

2-5

21

9-3

90

17

0192

0-39

017

vo R .H.

12 140 16 230 20

690

00040

0041

Oil

90%

0-93 0-72 50 2-3 D

022

042

P

R.H.

3-2 160 40 250

9

00013

00010

n

20%

14

1-3

84

64 41 17 0050

025

0-30

R.H.

16

63

20

78

24 140

00016

0-027

0-147

p = 0-5 g cm 3

65%

0-92

0-80

5-7

34 27

74 013

0-38

0-24

R.H.

5-7

66 7-7

99 9-8 210

00019

0023

0087

90%

0-28 0-24 1-5 086

015

0-39

R.H.

1-5

62

20

110

00006

00062

The figures in each cel  of the top half are for diffusion coefficients, the arrangement being as shown in the cel  for 80°C and 90% R.H. The unit is 10 5 cm2 s~ l. The significance of the figures in the bottom half is shown in the corresponding cell.

rm

C/3

References

References

References

References

References

References

References

Keywords

Intern, du Froid, Paris

DE VRIES, D. A. (1952fl).

DE VRIES, D. A. (1952fl).

Abstract

The thermal conductivity of granular materials. Bull. Inst.

References

References

References

References

References

Keywords

see Chemical reaction and diffusion. Absorption from a mixture of gases, 303-305. Acetone in cellulose acetate, 193. Anisotropic media, 5-8. Anomalous diffusion: see Non-Fickian diffusion. Basic volume, 206. Bimolecular reaction, 349-350. Boltzmann ' s transformation, 105. Bulk flow, 209. Capillary tube method, 49. Case I diffusion, 254. Case II diffusion, 254. Cellulose, direct dyes in, 232, 238. Cellulose acetate: see Acetone. Chemical reaction and diffusion: immobilization on limited number of fixed sites, 286, 298, 310, on mobile sites, 306, examples of, 326, instantaneous reversible, 326-329, irreversible, 329-337, 345-346, reversible first order, 337-345, 347-349, bimolecular, 349-350, reduced sorption curves, 350-351, constant reaction rate, 351. Chloroform in polystyrene, 239-241. Composite media: infinite, 38-40, semiinfinite, 41, plane membrane, 46-47,64, 196-200, cylindrical, 82, 200-202, spherical, 97, finite-difference formulae for, 149-150, see also Laminates and Particulates. Concentration-dependence, measurement of: see Diffusion coefficient, measurement of. Concentration-dependent diffusion: differential equation for, 4, characteristic features of, 179-189, see also Methods of solution for variable diffusion coefficients, Concentration-distance curves, Sorption curves, and Desorption curves. Concentration-distance curves, steady-state: cylinder, 70, plane sheet, 161-164. Concentration-distance curves, non-steady state: for instantaneous plane source, 12, extended sources, 15, cylindrical and spherical sources, 30, in semi-infinite medium, 37, in composite infinite medium, 39, 40, in plane sheet, 50, 55,

Concentration-distance curves for variable diffusion coefficients  : discontinuous, 288, 289, 294; exponential, 170, 172, 173; proportional to concentration, 122, 123; linear, 171, 172;

References

Diffusion coefficient, measurement of: 214; Taylor
'
s flow method, 215; dynamic method, 216; frequency response method, 216-218; steady-state methods, 218-221; time-lag methods, 222-230; analysis of concentration-distance curves, 230-238; sorption and desorption methods, 238-250; weighted means, 250, 251; radiotracers, 251-253 thin smear and twin disc methods, 252-253. Diffusion equations: 2-7; analogy with heat flow, 8-10; derivation of, 2-4; in plane sheet, 4, 44; in cylinder, 4, 5, 69; in sphere, 4, 5, 89; in anisotropic media, 5-7; in heterogeneous media, 266-284; Boltzmann
'
s transformation, 105; see also Solutions of. Diffusion process, definition and description of, 1. Diffusion wave, 361. Diffusion with chemical reaction: see Chemical reaction and diffusion. Dilute solutions, diffusion in, 16, 232. Discontinuous diffusion coefficients: special cases, 287-289; with one discontinuity, 290-296; with two discontinuities, 188-191, 296-298; in measurements of diffusion coefficients, 246-250; in surface skin, 196-200. Disc source, 31. Dyes in cellulose, 232, 238. Dynamic permeation method, 216

Diffusion coefficient, measurement of: 214; Taylor
'
s flow method, 215; dynamic method, 216; frequency response method, 216-218; steady-state methods, 218-221; time-lag methods, 222-230; analysis of concentration-distance curves, 230-238; sorption and desorption methods, 238-250; weighted means, 250, 251; radiotracers, 251-253 thin smear and twin disc methods, 252-253. Diffusion equations: 2-7; analogy with heat flow, 8-10; derivation of, 2-4; in plane sheet, 4, 44; in cylinder, 4, 5, 69; in sphere, 4, 5, 89; in anisotropic media, 5-7; in heterogeneous media, 266-284; Boltzmann
'
s transformation, 105; see also Solutions of. Diffusion process, definition and description of, 1. Diffusion wave, 361. Diffusion with chemical reaction: see Chemical reaction and diffusion. Dilute solutions, diffusion in, 16, 232. Discontinuous diffusion coefficients: special cases, 287-289; with one discontinuity, 290-296; with two discontinuities, 188-191, 296-298; in measurements of diffusion coefficients, 246-250; in surface skin, 196-200. Disc source, 31. Dyes in cellulose, 232, 238. Dynamic permeation method, 216

Edge effects in membranes,  64. Error functions: definition, 14; tables of, [375] [376] diffusion controlled, [191] [192] [193] [194] [195]

References

Keywords

Moving boundary: associated with discontinuous diffusion coefficients, 287-298, Neumann ' s method, 290, Danckwert ' s general treatment, 298-308, radial phase growth, 308-310, steady state approximation, 310-312, Goodman ' s integral method, 312-313, finitedifference methods, 313-323, isotherm migration method, 323-324, other methods, 325, practical examples, 286, 303-307. Mutual diffusion coefficient, 205, 214

413

413

Abstract

a/50 Methods of solution; Numerical Methods. Mean diffusion coefficient: from steady-state flow, 46, 69, 90; from sorption and desorption half-times, 239-244; from initial rates of sorption and desorption, [244][245] [246][49] [50][51] [52][53] [69][70] [71] 84,[99] [100][101] [160][161] [162][163] [164][191] [192][193]  asymmetrical, 165; in concentration and time dependent membranes, 222-228; non-homogeneous, 228-230; immobilizing reaction, 230. Methods of solution, constant diffusion coefficient: reflection and superposition, 11-17; separation of variables, 17-18; Laplace transform, 19-24; product solutions, 24-25; other methods, 25-26. Methods of solution, discontinuous diffusion coefficients, 287-298. Methods of solution, variable diffusion coefficients: time dependent, 104-105; concentration dependent, 105-136; exponential and linear diffusion coefficients, 112-125; exact formal solutions, 125-129; Goodman's integral method, 129; method of moments, 129-135, orthogonal functional approximations, 135-136; numerical methods, 137-159. Moisture, uptake by wool: see Heat and moisture. Moments, method of: 129-135.

References

Keywords

concentration dependence, 181, diffusion coefficient exhibiting a maximum, 184, discontinuous diffusion coefficient, 288, 289, 296. Sorption and desorption curves: correspondence principle, 173, general properties of, 179-191, effect of surface skin, 195-200, temperature change accompanying sorption, 353, 367. Sphere, steady state with irreversible reaction, 337. Sphere, non-steady state: new variable rC, 89, 102, constant surface concentration, 90-91, variable surface concentration, 91-93, in stirred solution, 93-96, with surface evaporation, 96, with constant surface flux, 96-97, composite, 97, with irreversible reaction, 332, 334, finitedifference formulae, 148-149. Sphere, hollow, steady state, 89-90, 160-164, influence of wall thickness on rate of flow, 90. Sphere, hollow, non-steady state: constant surface concentration, 98-99, flow through wall and time-lag, 99-101, surface evaporation, 101-102. Sphere, region bounded internally by, 102-103. Spherical source, 29. Square-root relationship, 37, 179. Steady-state method, of measuring the diffusion coefficient and its concentration dependence: 44, 218-221. Steady-state solutions: see Cylinder, hollow, plane sheet, sphere hollow. Stepwise diffusion coefficient: see Discontinuous diffusion coefficient

References
