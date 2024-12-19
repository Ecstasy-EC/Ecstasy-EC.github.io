import pandas as pd

publications = pd.read_csv("publications.tsv", sep="\t", header=0)

last_id = publications.shape[0]
new_item=publications.loc[last_id-1].copy(deep=True)

new_item.pub_date="2024-12-19"
new_item.title="Autonomous Tail-Sitter Flights in Unknown Environments"
new_item.venue="IEEE Transactions on Robotics (TRO)"
new_item.excerpt="Trajectory generation for fully autonomous flights of tail-sitter unmanned aerial vehicles (UAVs) presents substantial challenges due to their highly nonlinear aerodynamics. In this paper, we introduce, to the best of our knowledge, the world's first fully autonomous tail-sitter UAV capable of high-speed navigation in unknown, cluttered environments. The UAV autonomy is enabled by cutting-edge technologies including LiDAR-based sensing, differential-flatness-based trajectory planning and control with purely onboard computation. In particular, we propose an optimization-based tail-sitter trajectory planning framework that generates high-speed, collision-free, and dynamically-feasible trajectories. To efficiently and reliably solve this nonlinear, constrained \textcolor{black}{problem}, we develop an efficient feasibility-assured solver, EFOPT, tailored for the online planning of tail-sitter UAVs. We conduct extensive simulation studies to benchmark EFOPT's superiority in planning tasks against conventional NLP solvers. We also demonstrate exhaustive experiments of aggressive autonomous flights with speeds up to 15m/s in various real-world environments, including indoor laboratories, underground parking lots, and outdoor parks."
new_item.citation="Lu, G., Ren, Y., Zhu, F., Li, H., Xue, R., Cai, Y., ... & Zhang, F. (2024). Autonomous Tail-Sitter Flights in Unknown Environments. in <i>IEEE Transactions on Robotics</i>."
new_item.url_slug="Tailsitter-TRO"
new_item.paper_url="https://arxiv.org/abs/2411.15003"
new_item.bibtex="https://scholar.googleusercontent.com/scholar.bib?q=info:51g-l06bAyQJ:scholar.google.com/&output=citation&scisdr=ClE7y4DKEJnQqt0db0w:AFWwaeYAAAAAZ2Qbd0zj95J_tNdAmCWRJlLbPKs&scisig=AFWwaeYAAAAAZ2Qbd8b8wEL1wR7UXNFXX0mGHmI&scisf=4&ct=citation&cd=-1"
new_item.video="https://www.youtube.com/watch?v=OvqhlB2h3k8"
new_item.img="-"

new_df = new_item.to_frame()
new_df = pd.concat([publications,new_df.T])
print(new_df)
new_df.to_csv("publications.tsv",sep="\t",index=False)