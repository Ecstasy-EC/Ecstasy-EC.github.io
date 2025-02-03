import pandas as pd

publications = pd.read_csv("publications.tsv", sep="\t", header=0)

last_id = publications.shape[0]
new_item=publications.loc[last_id-1].copy(deep=True)

new_item.pub_date="2025-01-29"
new_item.title="Safety-assured high-speed navigation for MAVs"
new_item.venue="Science Robotics"
new_item.excerpt="Micro air vehicles (MAVs) capable of high-speed autonomous navigation in unknown environments have the potential to improve applications like search and rescue and disaster relief, where timely and safe navigation is critical. However, achieving autonomous, safe, and high-speed MAV navigation faces systematic challenges, necessitating reduced vehicle weight and size for high-speed maneuvering, strong sensing capability for detecting obstacles at a distance, and advanced planning and control algorithms maximizing flight speed while ensuring obstacle avoidance. Here, we present the safety-assured high-speed aerial robot (SUPER), a compact MAV with a 280-millimeter wheelbase and a thrust-to-weight ratio greater than 5.0, enabling agile flight in cluttered environments. SUPER uses a lightweight three-dimensional light detection and ranging (LIDAR) sensor for accurate, long-range obstacle detection. To ensure high-speed flight while maintaining safety, we introduced an efficient planning framework that directly plans trajectories using LIDAR point clouds. In each replanning cycle, two trajectories were generated: one in known free spaces to ensure safety and another in both known and unknown spaces to maximize speed. Compared with baseline methods, this framework reduced failure rates by 35.9 times while flying faster and with half the planning time. In real-world tests, SUPER achieved autonomous flights at speeds exceeding 20 meters per second, successfully avoiding thin obstacles and navigating narrow spaces. SUPER represents a milestone in autonomous MAV systems, bridging the gap from laboratory research to real-world applications."
new_item.citation="Ren, Y., Zhu, F., Lu, G., Cai, Y., Yin, L., Kong, F., Lin, J., Chen, N. & Zhang, F. (2025) Safety-assured high-speed navigation for MAVs. in <i>Science Robotics</i>."
new_item.url_slug="SUPER"
new_item.paper_url="https://www.science.org/doi/10.1126/scirobotics.ado6187"
new_item.bibtex="https://scholar.googleusercontent.com/scholar.bib?q=info:YAMVgIEstUUJ:scholar.google.com/&output=citation&scisdr=ClEyjFtnEKyZihzbLfY:AFWwaeYAAAAAZ6DdNfatHIP23ereMlpME0chScs&scisig=AFWwaeYAAAAAZ6DdNU-6pDc0KWrBrsGIlallk0s&scisf=4&ct=citation&cd=-1"
new_item.video="https://www.youtube.com/watch?v=GPHuzG0ANmI"
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