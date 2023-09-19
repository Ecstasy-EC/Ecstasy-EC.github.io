---
title: "Trajectory Generation and Tracking Control for Aggressive Tail-Sitter Flights"
collection: publications
permalink: /publication/2023-09-19-tailsitter
excerpt: 'We address the theoretical and practical problems related to the trajectory generation and tracking control of tail-sitter UAVs. Theoretically, we ...'
date: 2023-09-19
venue: 'International Journal of Robotics Research'
paperurl: 'https://arxiv.org/pdf/2212.11552.pdf'
paperurltext: '[pdf]'
paperbibtex: 'https://scholar.googleusercontent.com/scholar.bib?q=info:Qb3Iodb5HXMJ:scholar.google.com/&amp;output=citation&amp;scisdr=ClEjYb5MELeo6_R1yzM:AFWwaeYAAAAAZQlw0zNsfxwMWf0I7ZrhF5j4U2o&amp;scisig=AFWwaeYAAAAAZQlw03CJwIGKeYpGN29shWIHkpQ&amp;scisf=4&amp;ct=citation&amp;cd=-1&amp;hl=zh-CN'
citation: 'Lu G, Cai Y, Chen N, et al. Trajectory Generation and Tracking Control for Aggressive Tail-Sitter Flights[J]. arXiv preprint arXiv:2212.11552, 2022.'
---
## Abstract

We address the theoretical and practical problems related to the trajectory generation and tracking control of tail-sitter UAVs. Theoretically, we focus on the differential flatness property with full exploitation of actual UAV aerodynamic models, which lays a foundation for generating dynamically feasible trajectory and achieving high-performance tracking control. We have found that a tail-sitter is differentially flat with accurate (not simplified) aerodynamic models within the entire flight envelope, by specifying coordinate flight condition and choosing the vehicle position as the flat output. This fundamental property allows us to fully exploit the high-fidelity aerodynamic models in the trajectory planning and tracking control to achieve accurate tail-sitter flights. Particularly, an optimization-based trajectory planner for tail-sitters is proposed to design high-quality, smooth trajectories with consideration of kinodynamic constraints, singularity-free constraints, actuator saturation, and obstacle avoidance. The planned trajectory of flat output is transformed to state trajectory in real-time with optional consideration of wind gust. To track the state trajectory, a global, singularity-free, and minimally-parameterized on-manifold MPC is developed, which fully leverages the accurate aerodynamic model to achieve high-accuracy trajectory tracking in the whole flight envelope. The proposed algorithms are implemented on our quadrotor tail-sitter prototype, ``Hong Hu&quot;, and their effectiveness are demonstrated through extensive real-world experiments in both indoor and outdoor field tests, including agile SE(3) flight through consecutive narrow windows (size narrower than the UAV wingspan) with speed up to $10$m/s, typical tail-sitter maneuvers (hovering , transition, level flight and loiter) with speed up to $20$m/s, and extremely aggressive aerobatic maneuvers (Wingover, Loop, Vertical Eight and Cuban Eight) with acceleration up to 2.5g.

## Video
[![Watch the video](https://img.youtube.com/vi/2x_bLbVuyrk/hqdefault.jpg)](https://www.youtube.com/watch?v=2x_bLbVuyrk)
