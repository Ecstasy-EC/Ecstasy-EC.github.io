---
title: "Memory-Efficient Boundary Map for Large-Scale Occupancy Grid Mapping"
collection: publications
permalink: /publication/2026-01-27-BoundaryMap
excerpt: 'Determining the occupancy status of locations in the environment is a fundamental task for safety-critical robotic applications. Traditional ...'
date: 2026-01-27
venue: 'International Journal of Robotics Research'
paperurl: 'https://journals.sagepub.com/doi/full/10.1177/02783649261425266'
paperurltext: '[pdf]'
paperbibtex: 'https://scholar.googleusercontent.com/scholar.bib?q=info:d-NlBvasX1cJ:scholar.google.com/&amp;output=citation&amp;scisdr=CoZ3028IEKGYrS0uK7Q:AIL1Nv4AAAAAavsoM7Tf6kkG9uDVSDPUp-iyw_E&amp;scisig=AIL1Nv4AAAAAavsoM-A2VnBHo6VDJPueUcz-E6w&amp;scisf=4&amp;ct=citation&amp;cd=-1&amp;hl=en'
citation: 'Tang, B., Ren, Y., Cai, Y., Kong, F., Liu, W., Zhu, F., Yin, L., Shi, L., &amp; Zhang, F. (2026). Memory-Efficient Boundary Map for Large-Scale Occupancy Grid Mapping. <i>The International Journal of Robotics Research</i>.'
video: 'GzunpivVaag'
---
## Abstract

Determining the occupancy status of locations in the environment is a fundamental task for safety-critical robotic applications. Traditional occupancy grid mapping methods subdivide the environment into a grid of voxels, each associated with one of three occupancy states: free, occupied, or unknown. These methods explicitly maintain all voxels within the mapped volume and determine the occupancy state of a location by directly querying the corresponding voxel that the location falls within. However, maintaining all grid voxels in high-resolution and large-scale scenarios requires substantial memory resources. In this paper, we introduce a novel representation that only maintains the boundary of the mapped volume. Specifically, we explicitly represent the boundary voxels, such as the occupied voxels and frontier voxels, while free and unknown voxels are automatically represented by volumes within or outside the boundary, respectively. As our representation maintains only a closed surface in two-dimensional (2D) space, instead of the entire volume in three-dimensional (3D) space, it significantly reduces memory consumption. Then, based on this 2D representation, we propose a method to determine the occupancy state of arbitrary locations in the 3D environment. We term this method as boundary map. Besides, we design a novel data structure for maintaining the boundary map, supporting efficient occupancy state queries. Theoretical analyses of the occupancy state query algorithm are also provided. Furthermore, to enable efficient construction and updates of the boundary map from the real-time sensor measurements, we propose a global-local mapping framework and corresponding update algorithms. Finally, we will make our implementation of the boundary map open-source on GitHub to benefit the community:https://github.com/hku-mars/BDM.

## Video
[![Watch the video](https://img.youtube.com/vi/GzunpivVaag/maxresdefault.jpg)](https://www.youtube.com/watch?v=GzunpivVaag)
