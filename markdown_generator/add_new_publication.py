import pandas as pd

publications = pd.read_csv("publications.tsv", sep="\t", header=0)

last_id = publications.shape[0]
new_item=publications.loc[last_id-1].copy(deep=True)

new_item.pub_date="2025-09-18"
new_item.title="DeltaFlow: An Efficient Multi-frame Scene Flow Estimation Method"
new_item.venue="NeurIPS 2025 (Spotlight)"
new_item.excerpt="Previous dominant methods for scene flow estimation focus mainly on input from two consecutive frames, neglecting valuable information in the temporal domain. While recent trends shift towards multi-frame reasoning, they suffer from rapidly escalating computational costs as the number of frames grows. To leverage temporal information more efficiently, we propose DeltaFlow, a lightweight 3D framework that captures motion cues via a Delta scheme, extracting temporal features with minimal computational cost, regardless of the number of frames. Additionally, scene flow estimation faces challenges such as imbalanced object class distributions and motion inconsistency. To tackle these issues, we introduce a Category-Balanced Loss to enhance learning across underrepresented classes and an Instance Consistency Loss to enforce coherent object motion, improving flow accuracy. Extensive evaluations on the Argoverse 2 and Waymo datasets show that Flow achieves state-of-the-art performance with up to 22% lower error and  faster inference compared to the next-best multi-frame supervised method, while also demonstrating a strong cross-domain generalization ability. The code is open-sourced at https://github.com/Kin-Zhang/DeltaFlow along with trained model weights."
new_item.citation="Zhang, Q., Zhu, X., Zhang, Y., Cai, Y., Andersson, O., & Jensfelt, P. (2025). DeltaFlow: An Efficient Multi-frame Scene Flow Estimation Method. in <i>NeurIPS 2025 (Spotlight) </i>."
new_item.url_slug="DELTAFLOW"
new_item.paper_url="https://arxiv.org/abs/2508.17054"
new_item.bibtex="https://scholar.googleusercontent.com/scholar.bib?q=info:tYOTq3QHnhAJ:scholar.google.com/&output=citation&scisdr=CgIZ17YeELusyB4BYPA:AAZF9b8AAAAAaNgHePC811Rgz-uVfzYOwizZOtY&scisig=AAZF9b8AAAAAaNgHeG0y-rmS0ZG6j-j2DLggI0U&scisf=4&ct=citation&cd=-1&hl=en"
new_item.video="-"
new_item.img="-"

# new_item.pub_date="2025-01-27"
# new_item.title="LVBA: LiDAR-Visual Bundle Adjustment for RGB Point Cloud Mapping"
# new_item.venue="2025 IEEE International Conference on Robotics and Automation (ICRA)"
# new_item.excerpt="Point cloud maps with accurate color are crucial in robotics and mapping applications. Existing approaches for producing RGB-colorized maps are primarily based on real-time localization using filter-based estimation or sliding window optimization, which may lack accuracy and global consistency. In this work, we introduce a novel global LiDAR-Visual bundle adjustment (BA) named LVBA to improve the quality of RGB point cloud mapping beyond existing baselines. LVBA first optimizes LiDAR poses via a global LiDAR BA, followed by a photometric visual BA incorporating planar features from the LiDAR point cloud for camera pose optimization. Additionally, to address the challenge of map point occlusions in constructing optimization problems, we implement a novel LiDAR-assisted global visibility algorithm in LVBA. To evaluate the effectiveness of LVBA, we conducted extensive experiments by comparing its mapping quality against existing state-of-the-art baselines (i.e., R3LIVE and FAST-LIVO). Our results prove that LVBA can proficiently reconstruct high-fidelity, accurate RGB point cloud maps, outperforming its counterparts."
# new_item.citation="Li, R., Liu, X., Li, H., Liu, Z., Lin, J., Cai, Y., & Zhang, F. (2025). LVBA: LiDAR-Visual Bundle Adjustment for RGB Point Cloud Mapping.in <i>2025 IEEE International Conference on Robotics and Automation (ICRA)</i>"
# new_item.url_slug="LVBA"
# new_item.paper_url="http://arxiv.org/abs/2409.10868"
# new_item.bibtex="https://scholar.googleusercontent.com/scholar.bib?q=info:Bm2J5Y5NYUgJ:scholar.google.com/&output=citation&scisdr=ClEyjFblEKyZiidJs8M:AFWwaeYAAAAAZ5tPq8NFzDUgVlaGuPCOaLpVuvI&scisig=AFWwaeYAAAAAZ5tPq2oD55o4MNqej5pBxsZQ5KQ&scisf=4&ct=citation&cd=-1"
# new_item.video="https://www.youtube.com/watch?v=jtIUBI0U76c"
# new_item.img="-"

new_df = new_item.to_frame()
new_df = pd.concat([publications,new_df.T])
print(new_df)
new_df.to_csv("publications.tsv",sep="\t",index=False)