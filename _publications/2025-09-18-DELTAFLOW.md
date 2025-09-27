---
title: "DeltaFlow: An Efficient Multi-frame Scene Flow Estimation Method"
collection: publications
permalink: /publication/2025-09-18-DELTAFLOW
excerpt: 'Previous dominant methods for scene flow estimation focus mainly on input from two consecutive frames, neglecting valuable information in the ...'
date: 2025-09-18
venue: 'NeurIPS 2025 (Spotlight)'
paperurl: 'https://arxiv.org/abs/2508.17054'
paperurltext: '[pdf]'
paperbibtex: 'https://scholar.googleusercontent.com/scholar.bib?q=info:tYOTq3QHnhAJ:scholar.google.com/&amp;output=citation&amp;scisdr=CgIZ17YeELusyB4BYPA:AAZF9b8AAAAAaNgHePC811Rgz-uVfzYOwizZOtY&amp;scisig=AAZF9b8AAAAAaNgHeG0y-rmS0ZG6j-j2DLggI0U&amp;scisf=4&amp;ct=citation&amp;cd=-1&amp;hl=en'
citation: 'Zhang, Q., Zhu, X., Zhang, Y., Cai, Y., Andersson, O., &amp; Jensfelt, P. (2025). DeltaFlow: An Efficient Multi-frame Scene Flow Estimation Method. in <i>NeurIPS 2025 (Spotlight) </i>.'
---
## Abstract

Previous dominant methods for scene flow estimation focus mainly on input from two consecutive frames, neglecting valuable information in the temporal domain. While recent trends shift towards multi-frame reasoning, they suffer from rapidly escalating computational costs as the number of frames grows. To leverage temporal information more efficiently, we propose DeltaFlow, a lightweight 3D framework that captures motion cues via a Delta scheme, extracting temporal features with minimal computational cost, regardless of the number of frames. Additionally, scene flow estimation faces challenges such as imbalanced object class distributions and motion inconsistency. To tackle these issues, we introduce a Category-Balanced Loss to enhance learning across underrepresented classes and an Instance Consistency Loss to enforce coherent object motion, improving flow accuracy. Extensive evaluations on the Argoverse 2 and Waymo datasets show that Flow achieves state-of-the-art performance with up to 22% lower error and  faster inference compared to the next-best multi-frame supervised method, while also demonstrating a strong cross-domain generalization ability. The code is open-sourced at https://github.com/Kin-Zhang/DeltaFlow along with trained model weights.
