---
title: "ProbPer-LiLo: Probabilistic Persistency Modeling for Life-Long Mapping"
collection: publications
permalink: /publication/2025-12-09-ProbPer-LiLo
excerpt: '3D mapping is vital for a broad range of applications that rely on a consistent and accurate representation of the environment. Change is an ...'
date: 2025-12-09
venue: 'IEEE Robotics and Automation Letters (RAL)'
paperurl: 'https://ieeexplore.ieee.org/document/11345986'
paperurltext: '[pdf]'
paperbibtex: 'https://scholar.googleusercontent.com/scholar.bib?q=info:6i8Jir2Z5Z8J:scholar.google.com/&amp;output=citation&amp;scisdr=CoZ3028IEKGYrS0h7Hc:AIL1Nv4AAAAAavsn9HfJjqJluit3zjcv4FDa3aw&amp;scisig=AIL1Nv4AAAAAavsn9NaOP946LMGN_cccQy2LjiA&amp;scisf=4&amp;ct=citation&amp;cd=-1&amp;hl=en'
citation: 'Ali, W., Cai, Y., Jensfelt, P., &amp; Nguyen, T.-M. (2026). ProbPer-LiLo: Probabilistic Persistency Modeling for Life-Long Mapping. <i>IEEE Robotics and Automation Letters</i>, 11(3), 2530-2537.'
image: 'figures/probper-lilo.png'
---
## Abstract

3D mapping is vital for a broad range of applications that rely on a consistent and accurate representation of the environment. Change is an ever-persistent force in our world and with the evolution of a scene its 3D map becomes outdated. Thus, a mapping framework that can adapt and refine the 3D maps with the changes in the scene is necessary. In this letter, we propose a lifelong mapping framework where map maintenance is based on two objectives including the preservation of static structures and the refinement of the 3D map. To preserve only the static structures, we classify the object’s state and remove the dynamic objects and the quasi-static objects, i.e., objects which temporarily appear static. For classifying the state of objects, we propose a discrete probabilistic solution utilizing a factor graph. Using this classification, we generate static maps from multiple sessions which are used for map refinement. The refinement is based on change detection and map update, leveraging semantic and geometric information. For the evaluation, we collect a multi-campus lifelong dataset as an extension of the MCD datasets from KTH and NTU campuses. The proposed approach is capable of accurately detecting quasi-static objects even in highly dynamic environments. Our system demonstrates state of the art performance in large scale environments. Furthermore, our approach can handle both SLAM-generated and survey-grade maps.
