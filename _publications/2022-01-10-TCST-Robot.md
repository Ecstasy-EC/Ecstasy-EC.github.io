---
title: "Robots' State Estimation and Observability Analysis Based on Statistical Motion Models"
collection: publications
permalink: /publication/2022-01-10-TCST-Robot
excerpt: 'This article presents a generic motion model to capture mobile robots&apos; dynamic behaviors (translation and rotation). The model is based on ...'
date: 2022-01-10
venue: 'IEEE Transactions on Control Systems Technology (TCST)'
paperurl: 'https://ieeexplore.ieee.org/document/9676487'
paperurltext: '[pdf]'
paperbibtex: 'https://scholar.googleusercontent.com/scholar.bib?q=info:du0fIlL7gzMJ:scholar.google.com/&amp;output=citation&amp;scisdr=Cm3pnLgeELeo6o21y_Y:AGlGAw8AAAAAZHCw0_ZU1F1LBr0HFwXcGrti7aI&amp;scisig=AGlGAw8AAAAAZHCw01DaVbIlsAWE3aBw26Rh1Ws&amp;scisf=4&amp;ct=citation&amp;cd=-1'
citation: 'W. Xu, D. He, Y. Cai and F. Zhang, Robots&apos; State Estimation and Observability Analysis Based on Statistical Motion Models,&quot; in <i>IEEE Transactions on Control Systems Technology</i>, vol. 30, no. 5, pp. 2030-2045, Sept. 2022, doi: 10.1109/TCST.2021.3133080.&quot;'
---
## Abstract

This article presents a generic motion model to capture mobile robots&apos; dynamic behaviors (translation and rotation). The model is based on statistical models driven by white random processes and is formulated into a full state estimation algorithm based on the error-state extended Kalman filtering framework (ESEKF). The major benefits of this method are its versatility, being applicable to different robotic systems without accurately modeling the robots&apos; specific dynamics, and the ability to estimate the robot&apos;s (angular) acceleration, jerk, or higher order dynamic states with low delay. Mathematical analyses with numerical simulations are presented to show the properties of the statistical model-based estimation framework and reveal its connection to existing low-pass filters. Furthermore, a new paradigm is developed for robotic observability analysis by developing Lie derivatives and associated partial differentiation directly on manifolds. It is shown that this new paradigm is much simpler and more natural than existing methods based on quaternion parameterizations. It is also scalable to highdimensional systems. A novel thin set concept is introduced to characterize the unobservable subset of the system states, providing the theoretical foundation to observability analysis of robotic systems operating on manifolds and in high dimension. Finally, extensive experiments, including full state estimation and extrinsic calibration (both POS-IMU and IMU-IMU) on a quadrotor unmanned aerial vehicle (UAV), a handheld platform, and a ground vehicle, are conducted. Comparisons with existing methods show that the proposed method can effectively estimate all extrinsic parameters, the robot&apos;s translation/angular acceleration, and other state variables (e.g., position, velocity, and attitude) with high accuracy and low delay.
