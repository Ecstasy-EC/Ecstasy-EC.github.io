---
title: "Learned Controllers for Agile Quadrotors in Pursuit-Evasion Games"
collection: publications
permalink: /publication/2026-11-04-PursuitEvasion
excerpt: 'In this letter we study 1v1 quadrotor pursuit-evasion, where a pursuer and an evader are trained via reinforcement learning (RL) by competing against ...'
date: 2026-11-04
venue: 'IEEE Robotics and Automation Letters (RAL)'
paperurl: 'https://arxiv.org/abs/2506.02849'
paperurltext: '[pdf]'
citation: 'Sanchez Roncero, A., Cai, Y., Andersson, O., &amp; Ögren, P. (2026). Learned Controllers for Agile Quadrotors in Pursuit-Evasion Games. <i>IEEE Robotics and Automation Letters</i>.'
video: 'U1tWZzHgv60'
---
## Abstract

In this letter we study 1v1 quadrotor pursuit-evasion, where a pursuer and an evader are trained via reinforcement learning (RL) by competing against each other. Such adversarial settings face well-known challenges: each agent's policy changes during training, creating a non-stationary environment; agents might overfit to the current opponent and forget earlier strategies (catastrophic forgetting); and the competitive dynamics can cause strategy cycling or policy collapse. To address these issues, we propose Asynchronous Multi-Stage Population-Based training with Hedge sampling (AMSPBH), a method based on Policy-Space Response Oracles (PSRO) and adapted to quadrotor RL control. PSRO maintains a population of previously trained policies and trains new approximate best responses against mixtures of that population instead of against a single opponent. In AMSPBH, each generation trains one agent with Proximal Policy Optimization (PPO) against frozen opponent policies, while a Hedge sampler assigns higher probability to opponents that are currently difficult to beat. We show that: (i) AMSPBH discovers new strategies while retaining competence against older opponents, reaching a regime where additional best-response training gives limited improvement; (ii) compared to training against only the latest opponent, population-based training generalizes better across diverse and unseen strategies; and (iii) the learned population contains distinct pursuit and evasion behaviors, providing useful strategic diversity for finding weaknesses and improving controller robustness. We validate the trained policies with hardware experiments on Crazyflie brushless quadrotors, showing zero-shot sim-to-real transfer of agile, reactive pursuit-evasion behavior against both handcrafted and learned adversaries, with physical flights reaching up to 4.87 m/s.

## Video
[![Watch the video](https://img.youtube.com/vi/U1tWZzHgv60/maxresdefault.jpg)](https://www.youtube.com/watch?v=U1tWZzHgv60)
