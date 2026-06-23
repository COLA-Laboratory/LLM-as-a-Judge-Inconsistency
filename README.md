# ⚖️ Awesome LLM-as-a-Judge Inconsistency [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

[![MIT License](https://img.shields.io/badge/license-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/COLA-Laboratory/LLM-as-a-Judge-Inconsistency)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat)](http://makeapullrequest.com)
[![Last Update](https://img.shields.io/badge/Last_Update-2026.06-blue.svg)](https://github.com/COLA-Laboratory/LLM-as-a-Judge-Inconsistency)

A curated, up-to-date collection of work on **inconsistency in LLM-as-a-Judge**: when LLM evaluators give unstable, biased, or non-rankable preferences. We organize the literature by the *source* of inconsistency, and separately track the **baselines** (judging / aggregation methods) and **datasets** commonly used to study it.

> **Scope**: We focus on papers that *measure, explain, or repair* inconsistency in LLM judges — including order/self-preference/length biases, non-transitivity (cyclic preferences), run-to-run instability, calibration, and the aggregation models (Bradley–Terry, Elo, and extensions) used to turn noisy judgments into rankings. General LLM-as-a-Judge methods are included only when inconsistency is a central concern.

---

## Table of Contents

* [Taxonomy](#taxonomy) — How we classify inconsistency
* [Baselines](#baselines) — Judging paradigms & aggregation methods
* [Datasets & Benchmarks](#datasets--benchmarks)
* [Paper List](#paper-list) — Organized by source of inconsistency
* [Contributing](#contributing)
* [Abbreviations](#abbreviations)

---

## Taxonomy

We classify inconsistency by **where it comes from**, not by which model exhibits it. The first two clusters (non-transitivity, run-to-run stability) are under-covered by existing lists and are the focus of this collection.

<!-- Add a taxonomy figure here once ready: -->
<!-- ![Taxonomy](assets/taxonomy.png) -->

| Cluster | What it captures |
|---|---|
| **Position / Order bias** | Verdict depends on candidate ordering; swap-based correction |
| **Self-preference bias** | Judge favors its own (or same-family) outputs |
| **Length / Verbosity bias** | Longer answers scored higher; length-controlled correction |
| **Non-transitivity** | A≻B, B≻C, yet C≻A — cyclic triads, transitivity violation |
| **Stability / Self-consistency** | Variance across runs, temperature, prompt perturbations |
| **Calibration & Reliability** | Confidence calibration, conformal / uncertainty guarantees |
| **Aggregation models** | Bradley–Terry, Elo, mElo, multidimensional capability models |
| **Mitigation & Repair** | Debiasing, conflict isolation, post-hoc preference repair |

---

## Baselines

Methods commonly used as comparison points. Split into *judging paradigms* (how a single verdict is produced) and *aggregation* (how many verdicts become a ranking).

### Judging paradigms

| Method | Idea | Typical inconsistency studied |
|---|---|---|
| Pairwise comparison | Judge picks the better of two answers | Position bias, non-transitivity |
| Pointwise grading | Judge scores a single answer (e.g. 1–10) | Calibration, scale drift |
| Reference-guided | Judge compares against a gold answer | Self-preference, bias |
| Round-robin tournament | All-pairs pairwise, then aggregate | Cyclic triads |

### Aggregation models

| Method | Note |
|---|---|
| Bradley–Terry (BT) | Scalar-strength assumption; baseline ranking model |
| Elo | Online update; order-sensitive |
| mElo / multidimensional Elo | Captures non-transitive (cyclic) structure |
| Bayesian Hodge-BT | Hodge decomposition + Bayesian BT |
| GPM | General preference / capability modeling |
| RankRefine | Post-hoc BT regression refinement |

---

## Datasets & Benchmarks

| Dataset | Emphasis | Link |
|---|---|---|
| MT-Bench | Multi-turn, pairwise judging | [paper](https://arxiv.org/abs/2306.05685) |
| Chatbot Arena | Large-scale human preferences | [paper](https://arxiv.org/abs/2403.04132) |
| Arena-Hard | Hard, discriminative pairwise prompts | [repo](https://github.com/lmarena/arena-hard-auto) |
| AlpacaEval 2.0 (LC) | Length-controlled win rate | [paper](https://arxiv.org/abs/2404.04475) |
| WildBench | Real-world task distribution | [paper](https://arxiv.org/abs/2406.04770) |
| RewardBench | Reward-model / judge benchmark | [paper](https://arxiv.org/abs/2403.13787) |
| JudgeBench | Judge reliability benchmark | [paper](https://arxiv.org/abs/2410.12784) |

> Verify links/versions before publishing — these are seed entries.

---

## Paper List

> A curated collection of papers on inconsistency in LLM-as-a-Judge, grouped by the **source** of inconsistency rather than by model or task. Each entry gives the paper link, publication date, code (where available), and a one-sentence takeaway. Within each category, papers are ordered chronologically so the progression of ideas is easy to follow.

<!-- PAPER-LIST:START -->

### Surveys (1)

* [A Survey on LLM-as-a-Judge](https://arxiv.org/abs/2411.15594) ![date](https://img.shields.io/badge/date-2024.11-b31b1b.svg)
  > Maps the LLM-as-a-Judge landscape, including a consistency/reliability cluster covering biases and stability.

### Position / Order Bias (1)

* [Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena](https://arxiv.org/abs/2306.05685) ![date](https://img.shields.io/badge/date-2023.06-b31b1b.svg) [![code](https://img.shields.io/badge/code-link-black.svg)](https://github.com/lm-sys/FastChat)
  > Introduces MT-Bench and documents position, verbosity, and self-enhancement biases in LLM judges.

### Length / Verbosity Bias (1)

* [Length-Controlled AlpacaEval: A Simple Way to Debias Automatic Evaluators](https://arxiv.org/abs/2404.04475) ![date](https://img.shields.io/badge/date-2024.04-b31b1b.svg) [![code](https://img.shields.io/badge/code-link-black.svg)](https://github.com/tatsu-lab/alpaca_eval)
  > Regresses out answer length to produce a length-controlled win rate, reducing verbosity bias.

### Non-Transitivity (1)

* [Investigating Non-Transitivity in LLM-as-a-Judge](https://arxiv.org/abs/2502.14074) ![date](https://img.shields.io/badge/date-2025.02-b31b1b.svg)
  > Shows pairwise LLM judgments violate transitivity; analyzes Bradley-Terry limits and round-robin tournament aggregation.

### Calibration & Reliability (1)

* [RewardBench: Evaluating Reward Models for Language Modeling](https://arxiv.org/abs/2403.13787) ![date](https://img.shields.io/badge/date-2024.03-b31b1b.svg) [![code](https://img.shields.io/badge/code-link-black.svg)](https://github.com/allenai/reward-bench)
  > Benchmark probing reward-model / judge reliability across chat, reasoning, and safety prompts.

### Mitigation & Repair (1)

* [RankRefine: Post-hoc Bradley-Terry Refinement for LLM Judge Rankings](https://arxiv.org/abs/2508.16495) ![date](https://img.shields.io/badge/date-2025.08-b31b1b.svg)
  > Refines noisy judge rankings via post-hoc Bradley-Terry regression.

<!-- PAPER-LIST:END -->

---

## Contributing

Contributions are welcome! To add a paper, append an entry to [`papers.yaml`](papers.yaml) and open a PR:

```yaml
- title: "Paper Title"
  url: "https://arxiv.org/abs/XXXX.XXXXX"
  date: "2026.01"          # YYYY.MM
  category: "Non-Transitivity"   # must match a category below
  code: "https://github.com/..."  # optional
  tldr: "One-sentence summary of the contribution."
```

Valid categories: `Surveys`, `Position / Order Bias`, `Self-Preference Bias`, `Length / Verbosity Bias`, `Non-Transitivity`, `Stability & Self-Consistency`, `Calibration & Reliability`, `Aggregation Models`, `Mitigation & Repair`.

---

## Abbreviations

| Abbr. | Meaning |
|---|---|
| BT | Bradley–Terry model |
| LC | Length-Controlled |
| RM | Reward Model |
| LLM-aaJ | LLM-as-a-Judge |
