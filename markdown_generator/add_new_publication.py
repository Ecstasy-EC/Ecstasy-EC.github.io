import pandas as pd

publications = pd.read_csv("publications.tsv", sep="\t", header=0)

last_id = publications.shape[0]
new_item=publications.loc[last_id-1].copy(deep=True)

new_item.pub_date="2024-11-27"
new_item.title="Swarm-LIO2: Decentralized Efficient LiDAR-inertial Odometry for UAV Swarms"
new_item.venue="IEEE Transactions on Robotics (TRO)"
new_item.excerpt="Aerial swarm systems possess immense potential in various aspects, such as cooperative exploration, target tracking, search and rescue. Efficient, accurate self and mutual state estimation are the critical preconditions for completing these swarm tasks, which remain challenging research topics. This paper proposes Swarm-LIO2: a fully decentralized, plug-and-play, computationally efficient, and bandwidth-efficient LiDAR-inertial odometry for aerial swarm systems. Swarm-LIO2 uses a decentralized, plug-and-play network as the communication infrastructure. Only bandwidth-efficient and low-dimensional information is exchanged, including identity, ego-state, mutual observation measurements, and global extrinsic transformations. To support the plug-and-play of new teammate participants, Swarm-LIO2 detects potential teammate UAVs and initializes the temporal offset and global extrinsic transformation all automatically. To enhance the initialization efficiency, novel reflectivity-based UAV detection, trajectory matching, and factor graph optimization methods are proposed. For state estimation, Swarm-LIO2 fuses LiDAR, IMU, and mutual observation measurements within an efficient ESIKF framework, with careful compensation of temporal delay and modeling of measurements to enhance the accuracy and consistency. Moreover, the proposed ESIKF framework leverages the global extrinsic for ego-state estimation in case of LiDAR degeneration or refines the global extrinsic along with the ego-state estimation otherwise. To enhance the scalability, Swarm-LIO2 introduces a novel marginalization method in the ESIKF, which prevents the growth of computational time with swarm size. Extensive simulation and real-world experiments demonstrate the broad adaptability to large-scale aerial swarm systems and complicated scenarios, including GPS-denied scenes, degenerated scenes for cameras or LiDARs. The experimental results showcase the centimeter-level localization accuracy which outperforms other state-of-the-art LiDAR-inertial odometry for a single UAV system. Furthermore, diverse applications demonstrate the potential of Swarm-LIO2 to serve as reliable infrastructure for various aerial swarm missions. In addition, we open-source all the system designs on GitHub to benefit society: https://github.com/hku-mars/Swarm-LIO2."
new_item.citation="Zhu, F., Ren, Y., Yin, L., Kong, F., Liu, Q., Xue, R., Liu, W., Cai, Y., Lu, G., Li, H. & Zhang, F. (2024). Swarm-LIO2: Decentralized, Efficient LiDAR-inertial Odometry for UAV Swarms. in <i>IEEE Transactions on Robotics</i>."
new_item.url_slug="SWARM-LIO2"
new_item.paper_url="ttps://arxiv.org/abs/2409.17798"
new_item.bibtex="https://scholar.googleusercontent.com/scholar.bib?q=info:gxa7PCDd3eAJ:scholar.google.com/&output=citation&scisdr=ClH1yDsaEJnQqv59B7c:AFWwaeYAAAAAZ0d7H7fX9RC2eo86E61pN0VaFMs&scisig=AFWwaeYAAAAAZ0d7H6rA22jZcXH49TyKa9IPT5s&scisf=4&ct=citation&cd=-1"
new_item.video="https://www.youtube.com/watch?v=Q7cJ9iRhlrY"
new_item.img="-"

new_df = new_item.to_frame()
new_df = pd.concat([publications,new_df.T])
print(new_df)
new_df.to_csv("publications.tsv",sep="\t",index=False)