# LLM-as-a-Judge for Biological Scientific Discovery

This survey compares what LLMs judge in biological research, how they reach a verdict, and what evidence validates it.

<!-- SUMMARY:START -->

**Survey in progress** · 4 core biological studies · 14 included works · 20 records screened

<!-- SUMMARY:END -->

Content updated **2026-11-19**.

[Framework](#research-framework) · [Reading routes](#reading-guide) · [Compare papers](#tasks-and-methods) · [Validation map](#validation-evidence) · [Further reading](#further-reading) · [Contribute](#scope-and-contributions)

## Research framework

![Four studies grouped by biological task, showing the object, evidence or criteria, verdict and possible use for each judge.](assets/framework.svg)

**Figure 1.** Read across a study to follow one judgment. The two studies in the first band evaluate evidence at different scales: SKiM-GPT scores a whole relationship, while KnowHD counts supported claims in its rationale. A possible use describes what the verdict can inform. The dashed band identifies directions the survey aims to cover.

## Reading guide

1. **Does the literature support this hypothesis?** Start with [SKiM-GPT](https://link.springer.com/article/10.1186/s12859-025-06350-7) for a single verdict on a proposed relationship. Then read [KnowHD](https://ijcai.org/proceedings/2025/0873.pdf) to see how splitting the rationale into claims exposes which premises lack support.
2. **What makes a hypothesis worth testing?** Start with [Biomedical Hypothesis Evaluation · COLM 2024](https://arxiv.org/pdf/2407.08940) for a rubric covering novelty, relevance, significance and verifiability. Compare its novelty rating with [KnowHD’s groundedness score](https://ijcai.org/proceedings/2025/0873.pdf): a new idea can draw on established premises even when its conclusion has little published evidence.
3. **How do you build a judge for a research assistant?** Read the [ChatInvent judge study](https://research.chalmers.se/publication/554919/file/554919_Fulltext.pdf) for its scoring criteria and human agreement tests. Follow with [G-Eval](https://aclanthology.org/2023.emnlp-main.153/) for the general technique of turning a written criterion into evaluation steps and a score.

## Tasks and methods

The core papers address three tasks: checking evidence for a claim, assessing the quality of a proposed hypothesis, and grading a research assistant’s output. The role below each venue identifies whether the paper develops a judge or uses one to study another task.

<!-- COMPARISON:START -->

| Paper & venue | Scientific task | How it judges | Validation & key limit |
|---|---|---|---|
| **SKiM-GPT**<br>BMC Bioinformatics 2026<br>*Judge method*<br>[Paper](https://link.springer.com/article/10.1186/s12859-025-06350-7)&nbsp;·&nbsp;[Code](https://github.com/stewart-lab/skimgpt)&nbsp;·&nbsp;[Notes](docs/evidence.md#skim-gpt) | Literature support for a proposed disease–gene–drug link | Rates support from −2 to +2 using retrieved abstracts. | Judge and expert medians agreed in direction on 13 of 14 hypotheses before filtering. Abstract coverage limits the verdict. |
| **KnowHD**<br>IJCAI 2025<br>*Judge method*<br>[Paper](https://ijcai.org/proceedings/2025/0873.pdf)&nbsp;·&nbsp;[Code](https://github.com/gzxiong/TruthHypo)&nbsp;·&nbsp;[Notes](docs/evidence.md#knowhd) | Literature or graph support for a hypothesis rationale | Tests atomic claims against retrieved text or graph relations and averages the support labels. | Experts preferred the more grounded hypothesis in 59% of 54 selected pairs. Pairs with small score gaps were omitted. |
| **Biomedical Hypothesis Evaluation**<br>COLM 2024<br>*Judge application*<br>[Paper](https://arxiv.org/pdf/2407.08940)&nbsp;·&nbsp;[Code](https://github.com/TsinghuaC3I/LLM4BioHypoGen)&nbsp;·&nbsp;[Notes](docs/evidence.md#qi-biomedical) | Quality of a generated biomedical hypothesis | GPT-4 scores four dimensions from 0 to 3 given the scientific background. | Three experts rated 100 unseen examples. Rank correlations of 0.73–0.94 cover selected generator settings. |
| **ChatInvent judge**<br>Artificial Intelligence in the Life Sciences 2026<br>*Judge method*<br>[Paper](https://research.chalmers.se/publication/554919/file/554919_Fulltext.pdf)&nbsp;·&nbsp;[Code](https://github.com/MolecularAI/langdmta-lab/blob/main/evaluation/langdmta_eval/README.md)&nbsp;·&nbsp;[Notes](docs/evidence.md#chatinvent-judge) | Quality of a drug-discovery assistant’s answer | Assigns four rubric labels using the request, answer and tool context. | Alignment with the expert majority rose from 0.80 to 0.86 on ten validation questions for one assistant. |

<!-- COMPARISON:END -->

## Validation evidence

![Judge tests by paper: repeated calls, expert comparison, controlled changes to supplied evidence and evaluation against external relation labels.](assets/validation-map.svg)

**Figure 2.** Each row is one paper. Runs count calls on the same object; experts count people; hypotheses, examples, questions and pairs count distinct units of evaluation. ChatInvent scheduled three runs on 30 questions per model; one model returned results for 28. A dash records an unreported test and carries no performance judgment. [ChatInvent, §5.3](https://research.chalmers.se/publication/554919/file/554919_Fulltext.pdf) · [Test-by-test source locations](docs/evidence.md)

**What was tested?** SKiM-GPT changed the polarity of supplied abstracts and observed whether its scores followed the evidence. KnowHD compared relation accuracy across groundedness-score groups using TruthHypo labels. The former tests sensitivity to an intervention; the latter tests association with an external benchmark. Expert comparisons likewise depend on what the panel rated: support, perceived truthfulness, hypothesis quality or assistant response quality. [SKiM-GPT, Fig. 5](https://link.springer.com/article/10.1186/s12859-025-06350-7) · [KnowHD, §4.3, Fig. 3 and Table 4](https://ijcai.org/proceedings/2025/0873.pdf) · [COLM, §3.4](https://arxiv.org/pdf/2407.08940) · [ChatInvent, §§5.2–5.4](https://research.chalmers.se/publication/554919/file/554919_Fulltext.pdf)

### Measured uses and benefits

- **Review time.** SKiM-GPT reports 0.23 hours of system time versus 8.42 hours per human reviewer for the same 159 abstracts. [Table 1](https://link.springer.com/article/10.1186/s12859-025-06350-7)
- **Retrospective selection.** KnowHD selected the highest-scoring of five candidates per input. On the graph-plus-literature setting, GPT-4o-mini reached 63.44% relation accuracy; the comparison with greedy decoding and majority voting varied by setting. [§4.4, Fig. 4](https://ijcai.org/proceedings/2025/0873.pdf)
- **Prospective discovery benefit.** Across the four core papers, none reports a prospective comparison linking use of the judge to laboratory-confirmed improvements in discovery yield. Reference labels, expert preferences and system-level results alone cannot establish that benefit. [Study-level outcome records](docs/evidence.md)

**Coverage gaps.** The current core set leaves experimental-design quality and prospective candidate prioritization open. Relevant studies would connect a recorded judge verdict to expert design assessments or measured outcomes for the candidates selected.

**Design your own judge.** Use the [design checklist and example evaluation record](docs/judge-design.md) to define evidence access, record separate verdicts and plan an independent check.

## Further reading

<!-- PAPER-LIST:START -->

<details><summary>General methods and reliability (8)</summary>

- [G-Eval: NLG Evaluation using GPT-4 with Better Human Alignment](https://doi.org/10.18653/v1/2023.emnlp-main.153) — Operationalizes a written evaluation criterion as model-generated evaluation steps and a score. [Notes](docs/evidence.md#g-eval)
- [FActScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation](https://doi.org/10.18653/v1/2023.emnlp-main.741) — Decomposes long answers and estimates the fraction of facts supported by a reference source. [Notes](docs/evidence.md#factscore)
- [Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena](https://arxiv.org/abs/2306.05685) — Introduces MT-Bench and documents position, verbosity, and self-enhancement biases in LLM judges. [Notes](docs/evidence.md#mt-bench)
- [Length-Controlled AlpacaEval: A Simple Way to Debias Automatic Evaluators](https://arxiv.org/abs/2404.04475) — Regresses out answer length to produce a length-controlled win rate, reducing verbosity bias. [Notes](docs/evidence.md#length-controlled-alpacaeval)
- [Investigating Non-Transitivity in LLM-as-a-Judge](https://arxiv.org/abs/2502.14074) — Shows pairwise LLM judgments violate transitivity; analyzes Bradley-Terry limits and round-robin tournament aggregation. [Notes](docs/evidence.md#non-transitivity)
- [Large Language Models are not Fair Evaluators](https://doi.org/10.18653/v1/2024.acl-long.511) — Swapping the order of two answers changes the reported winner. The authors test balanced presentation orders to reduce this effect. [Notes](docs/evidence.md#fair-evaluators)
- [LLM Evaluators Recognize and Favor Their Own Generations](https://arxiv.org/abs/2404.13076) — Tests whether judges recognize their own text and finds that stronger self-recognition tracks a stronger preference for their own answers. [Notes](docs/evidence.md#self-preference)
- [All Verdicts are Not Equal: Rethinking LLM Judge Reliability](https://doi.org/10.18653/2026.aacl-long.207) — Crosses repeated trials with answer-order swaps and reference labels to distinguish reproducibility, order sensitivity, and correctness. [Notes](docs/evidence.md#verdict-reliability)

</details>

**Workflows and adjacent cases (1)**

- [Valsci: an open-source, self-hostable literature review utility for automated large-batch scientific claim verification using large language models](https://doi.org/10.1186/s12859-025-06159-4) — Uses retrieved sources to produce a claim-level evidence report. [Notes](docs/evidence.md#valsci)

**Related reviews (1)**

- [A survey on LLM-as-a-judge](https://doi.org/10.1016/j.xinn.2025.101253) — Maps the LLM-as-a-Judge landscape, including a consistency/reliability cluster covering biases and stability. [Notes](docs/evidence.md#judge-survey)

<!-- PAPER-LIST:END -->

## Scope and contributions

We cover basic biology, biological engineering and drug discovery. Clinical diagnosis and patient advice are adjacent areas. To include a direct judge study, locate the **evaluated object, evidence or criteria, verdict format, and supporting method section or public prompt**. Keep unverified candidates in the [screening record](docs/screening.md).

Edit [papers.yaml](papers.yaml) using one stable ID per work. For each core paper, describe the task under `homepage.flow`, code performed tests under `validation`, and record review time, retrospective selection and prospective benefit under `outcomes`. Give each reported item a source location. Use `Pending verification` when its status is unresolved. Update the content date in this README when revising the survey. With Python 3.9+ and PyYAML, run `python3 generate_paper_list.py`, then `python3 generate_paper_list.py --check`. The script refreshes the marked blocks and both SVG figures.

[Evidence notes](docs/evidence.md) · [Screening decisions and migration history](docs/screening.md)
