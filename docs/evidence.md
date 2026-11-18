# Evidence notes

For each core study, the method describes the information available when the judge produces a verdict. The tests section identifies how the authors examined the judge. The outcomes section records measured review time, retrospective selection and prospective experimental benefit separately. A dash in the homepage map means that the paper did not report that specific test. “Pending verification” marks unresolved evidence. Background and historical entries retain their original screening fields.

[Reading guide](../README.md#reading-guide) · [Judge design checklist and example record](judge-design.md) · [Screening decisions](screening.md)

<!-- PAPER-LIST:START -->

### skim-gpt

**[SKiM-GPT: combining biomedical literature-based discovery with large language model hypothesis evaluation](https://doi.org/10.1186/s12859-025-06350-7)** · BMC Bioinformatics 27, 16 (online 17 December 2025) · 2026

A · included · full text checked

Scores how strongly the retrieved abstracts support a proposed biomedical relationship.

Tasks: hypothesis quality, claim support. Methods: pointwise scoring, retrieval-augmented.

- **Object** — The judge evaluates a proposed disease–gene–drug relationship.
- **Criteria and evidence** — It reads PubMed titles and abstracts linking the terms, optionally filtered for relevance.
- **Judge output** — It returns a support score from −2 to +2 and explains its rating.
- **Method location** — Implementation, Fig. 1. Results, Score alignment evaluation (Fig. 3), Cost estimation (Table 1), Retrieved text vs. memory. [Source](https://link.springer.com/article/10.1186/s12859-025-06350-7)

**Tests of the judge**

- **Repeated calls** — Ten independent calls for each of 14 selected hypotheses. Fig. 3 plots score distributions. [Results, Score alignment evaluation, Fig. 3](https://link.springer.com/article/10.1186/s12859-025-06350-7)
- **Expert comparison** — Four computational biologists read the same abstracts. Before filtering, the median model and expert scores agreed in direction on 13 of 14 hypotheses. [Results, Score alignment evaluation, Fig. 3A](https://link.springer.com/article/10.1186/s12859-025-06350-7)
- **Controlled evidence perturbation** — The authors supplied synthetic abstracts with positive, neutral or negative evidence and compared conditions including real abstracts and no text. Ratings responded to the supplied material. Fig. 4 separately measures relevance-filter performance. [Results, Retrieved text vs. memory, Fig. 5B–D](https://link.springer.com/article/10.1186/s12859-025-06350-7)
- **External relation labels** — Not reported

**Measured use and benefit**

- **Review time** — For 159 abstracts, mean time was 8.42 hours per human reviewer and 0.23 hours for the system. This times a review task. [Results, Cost estimation, Table 1](https://link.springer.com/article/10.1186/s12859-025-06350-7)
- **Retrospective selection** — Not reported
- **Prospective experimental or discovery benefit** — Not reported

- **Limitation** — The selected hypotheses cover 14 relationships. Abstract coverage and publication bias restrict the evidence.
- **Screening rationale** — Design and expert comparison of the evidence-based judge are central contributions.

[doi](https://doi.org/10.1186/s12859-025-06350-7) · [code](https://github.com/stewart-lab/skimgpt) · [Other version](https://doi.org/10.1101/2025.07.28.664797)

### knowhd

**[Toward Reliable Scientific Hypothesis Generation: Evaluating Truthfulness and Hallucination in Large Language Models](https://doi.org/10.24963/ijcai.2025/873)** · IJCAI 2025, 7849–7857 · 2025

A · included · full text checked

Estimates how much of a hypothesis and its rationale is grounded in earlier knowledge.

Tasks: claim support, hypothesis quality. Methods: retrieval-augmented, classification.

- **Object** — The judge evaluates atomic claims extracted from a hypothesis and its reasoning.
- **Criteria and evidence** — It receives retrieved PubMed passages, knowledge-graph relations, or both.
- **Judge output** — Each claim receives a binary support decision. Equation 3 averages these decisions across claims.
- **Method location** — §3, Fig. 2 and Eqs. 1–3 for the judge; §4.3, Fig. 3 for external labels; §4.4, Fig. 4 for retrospective selection; §5, Table 4 for the expert study. [Source](https://ijcai.org/proceedings/2025/0873.pdf)

**Tests of the judge**

- **Repeated calls** — Not reported
- **Expert comparison** — Two experts chose the more likely true hypothesis in 54 pairs selected for a large groundedness gap. Expert–expert agreement was 80%. Experts chose the higher-grounded item in 59.26% of pairs. Neither percentage is biological accuracy. [§5, Human Study on Open-ended Tasks, Table 4](https://ijcai.org/proceedings/2025/0873.pdf)
- **Controlled evidence perturbation** — Not reported
- **External relation labels** — The authors grouped hypotheses by KnowHD score and measured relation-prediction accuracy against TruthHypo labels. Fig. 3 plots groups with at least ten hypotheses. This evaluates the association at hypothesis level; individual entailment decisions lack a claim-level gold standard in this test. [§§2.1–2.3 and §4.3, Fig. 3](https://ijcai.org/proceedings/2025/0873.pdf)

**Measured use and benefit**

- **Review time** — Not reported
- **Retrospective selection** — For each input, select the highest-grounded of five generated candidates. Fig. 4 compares resulting GPT-4o-mini relation accuracy with greedy decoding and majority voting. The combined graph-and-literature generation setting reached 63.44%; the advantage varied by setting. [§4.4, Fig. 4](https://ijcai.org/proceedings/2025/0873.pdf)
- **Prospective experimental or discovery benefit** — Not reported

- **Limitation** — Retrieval misses count against groundedness. Selection for a large score gap limits extrapolation to close pairs. The score does not measure novelty or biological truth.
- **Screening rationale** — KnowHD is a separately specified and evaluated biomedical evidence judge.

[doi](https://doi.org/10.24963/ijcai.2025/873) · [arxiv](https://arxiv.org/abs/2505.14599) · [code](https://github.com/gzxiong/TruthHypo)

### chatinvent-judge

**[Designing an LLM-based evaluation system for agentic AI in drug discovery through human alignment](https://doi.org/10.1016/j.ailsci.2026.100187)** · Artificial Intelligence in the Life Sciences 10, 100187 · 2026

A · included · full text checked

Validates a rubric for grading a drug-discovery assistant’s responses against expert ratings.

Tasks: output quality. Methods: pointwise scoring, classification.

- **Object** — The judge grades ChatInvent’s answer to a drug-discovery request.
- **Criteria and evidence** — It sees the request, response, evaluation context and expected, accepted and actual tool calls.
- **Judge output** — It assigns a rubric label and justification for completeness, relevancy, structural clarity and scope adherence. A separate program checks tool-call correctness.
- **Method location** — Fig. 1 and Table 2, then §§5.2–5.4 and Table 4 (journal full text). [Source](https://research.chalmers.se/publication/554919/file/554919_Fulltext.pdf)

**Tests of the judge**

- **Repeated calls** — Four judge models were each scheduled for three trials on 30 unique questions. Claude returned usable results for 28 questions. The authors report within-model consistency by rubric dimension. [§5.3, Intra-LLM agreement, Fig. 3](https://research.chalmers.se/publication/554919/file/554919_Fulltext.pdf)
- **Expert comparison** — Five experts annotated assistant responses. Judge ratings were compared with the human majority. On a ten-question validation split for prompt optimization, agreement rose from 0.80 to 0.86. The tool-call check uses direct comparison. [Fig. 1, Table 2, §§5.2–5.4 and Table 4](https://research.chalmers.se/publication/554919/file/554919_Fulltext.pdf)
- **Controlled evidence perturbation** — Not reported
- **External relation labels** — Not reported

**Measured use and benefit**

- **Review time** — Not reported
- **Retrospective selection** — Not reported
- **Prospective experimental or discovery benefit** — Not reported

- **Limitation** — One assistant. Agreement varies by dimension. Prompt optimization was evaluated on ten validation questions. Scores concern the answer delivered to the user.
- **Screening rationale** — The central contribution is judge design and expert alignment in drug discovery.

[doi](https://doi.org/10.1016/j.ailsci.2026.100187) · [arxiv](https://arxiv.org/abs/2608.21057) · [code](https://github.com/MolecularAI/langdmta-lab/blob/main/evaluation/langdmta_eval/README.md)

### qi-biomedical

**[Large Language Models as Biomedical Hypothesis Generators: A Comprehensive Evaluation](https://arxiv.org/abs/2407.08940)** · COLM 2024 · 2024

B · included · full text checked

Compares hypothesis generators using a GPT-4 assessment alongside text-overlap and human assessments.

Tasks: hypothesis quality. Methods: pointwise scoring.

- **Object** — GPT-4 evaluates a generated biomedical hypothesis.
- **Criteria and evidence** — It receives the scientific background and criteria for novelty, relevance, significance and verifiability.
- **Judge output** — It assigns each dimension a score from 0 to 3 and explains the score.
- **Method location** — §3.1 evaluation metrics, pp. 4–5. §3.4 Human Evaluation and Case Study, Table 1. [Source](https://arxiv.org/pdf/2407.08940)

**Tests of the judge**

- **Repeated calls** — Not reported
- **Expert comparison** — Three biomedical experts rated 100 unseen examples from selected generator settings. Table 1 reports Spearman correlations of 0.73–0.94 between average model and human ratings across the listed settings. The paper also evaluates generators with reference hypotheses; those comparisons do not validate individual judge scores. [§3.1, Evaluation metrics; §3.4, Human Evaluation and Case Study, Table 1](https://arxiv.org/pdf/2407.08940)
- **Controlled evidence perturbation** — Not reported
- **External relation labels** — Not reported

**Measured use and benefit**

- **Review time** — Not reported
- **Retrospective selection** — Not reported
- **Prospective experimental or discovery benefit** — Not reported

- **Limitation** — Human review concentrated on selected high-performing settings. Perceived novelty and verifiability are rubric judgments.
- **Screening rationale** — The generator comparison is the main research question. Its scoring module meets all four inclusion criteria.

[doi](https://doi.org/10.48550/arXiv.2407.08940) · [arxiv](https://arxiv.org/abs/2407.08940) · [code](https://github.com/TsinghuaC3I/LLM4BioHypoGen)

### valsci

**[Valsci: an open-source, self-hostable literature review utility for automated large-batch scientific claim verification using large language models](https://doi.org/10.1186/s12859-025-06159-4)** · BMC Bioinformatics 26, 140 · 2025

D · included · full text checked

Uses retrieved sources to produce a claim-level evidence report.

Tasks: claim support. Methods: retrieval-augmented, classification.

- **Object** — User-supplied scientific claim.
- **Criteria and evidence** — Supporting and contradictory excerpts from retrieved papers, with abstracts as fallback.
- **Judge output** — Cited synthesis and a categorical verdict from contradiction to high support, including mixed or missing evidence.
- **Method location** — Implementation, report synthesis and the published “Synthesize report” system/user prompts. Results, SciFact evaluation. [Source](https://link.springer.com/article/10.1186/s12859-025-06159-4)
- **Repeated judgments** — Pending verification
- **Expert agreement** — Pending verification
- **Literature support** — Compared with SciFact labels and audited generated citations.
- **Biological experimental validation** — Not reported
- **Decision or efficiency benefit** — Workflow-level time comparison with undergraduate literature review. The study does not isolate the judge or measure successful discoveries.
- **Limitation** — Retrieval coverage constrains the verdict. SciFact performance does not establish the value of prospective biological decisions.
- **Screening rationale** — Adjacent scientific literature-review workflow with an identifiable judge. Its target is general claim verification.

[doi](https://doi.org/10.1186/s12859-025-06159-4) · [code](https://github.com/bricee98/Valsci)

### g-eval

**[G-Eval: NLG Evaluation using GPT-4 with Better Human Alignment](https://doi.org/10.18653/v1/2023.emnlp-main.153)** · EMNLP 2023 · 2023

C · included · full text checked

Operationalizes a written evaluation criterion as model-generated evaluation steps and a score.

Tasks: output quality. Methods: pointwise scoring.

- **Object** — Generated summary or dialogue response.
- **Criteria and evidence** — Task instructions, criterion, source context and evaluation steps.
- **Judge output** — Dimension score with probability weighting over rating choices.
- **Method location** — §2, scoring function and Fig. 1. [Source](https://aclanthology.org/2023.emnlp-main.153.pdf)
- **Repeated judgments** — Not reported
- **Expert agreement** — Human-rating correlations reported on NLG datasets. Biomedical expert alignment was not reported.
- **Literature support** — Not reported
- **Biological experimental validation** — Not reported
- **Decision or efficiency benefit** — Not reported
- **Limitation** — Text quality benchmarks supply the evidence for human alignment. Transfer to biology requires a new rubric and validation.
- **Screening rationale** — Template for specifying criteria and comparing rubric scores with human ratings.

[doi](https://doi.org/10.18653/v1/2023.emnlp-main.153) · [arxiv](https://arxiv.org/abs/2303.16634)

### factscore

**[FActScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation](https://doi.org/10.18653/v1/2023.emnlp-main.741)** · EMNLP 2023 · 2023

C · included · full text checked

Decomposes long answers and estimates the fraction of facts supported by a reference source.

Tasks: claim support. Methods: retrieval-augmented, classification.

- **Object** — Atomic factual assertions in generated biographies.
- **Criteria and evidence** — Retrieved passages from a designated knowledge source.
- **Judge output** — Support decisions aggregated into factual precision.
- **Method location** — §§3–4, human evaluation and automatic estimation. [Source](https://aclanthology.org/2023.emnlp-main.741.pdf)
- **Repeated judgments** — Not reported
- **Expert agreement** — Not reported
- **Literature support** — Estimator compared with human source-based atomic-fact annotations.
- **Biological experimental validation** — Not reported
- **Decision or efficiency benefit** — Not reported
- **Limitation** — A biography benchmark with a fixed knowledge source offers limited evidence for novel scientific claims.
- **Screening rationale** — Methodological precursor to claim-level groundedness metrics.

[doi](https://doi.org/10.18653/v1/2023.emnlp-main.741) · [arxiv](https://arxiv.org/abs/2305.14251)

### mt-bench

**[Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena](https://arxiv.org/abs/2306.05685)** · NeurIPS 2023 Datasets and Benchmarks · 2023

C · included · full text checked

Introduces MT-Bench and documents position, verbosity, and self-enhancement biases in LLM judges.

Tasks: output quality. Methods: pointwise scoring, pairwise comparison.

- **Object** — One or two assistant replies.
- **Criteria and evidence** — Question, grading instructions and optional reference solution.
- **Judge output** — Single grade or pairwise winner/tie.
- **Method location** — §§3.1, 3.3 and 4. Appendix grading prompts, Figs. 5–7. [Source](https://arxiv.org/pdf/2306.05685)
- **Repeated judgments** — Pending verification for identical-input repetitions. The order-swap test changes the input.
- **Expert agreement** — Compares model judgments with expert votes on MT-Bench and crowd preferences in Arena.
- **Literature support** — Not reported
- **Biological experimental validation** — Not reported
- **Decision or efficiency benefit** — Not reported
- **Limitation** — Chat preferences leave biological accuracy untested.
- **Screening rationale** — Baseline for designing pointwise and pairwise biological rubrics.

[doi](https://doi.org/10.52202/075280-2020) · [arxiv](https://arxiv.org/abs/2306.05685) · [code](https://github.com/lm-sys/FastChat)

### length-controlled-alpacaeval

**[Length-Controlled AlpacaEval: A Simple Way to Debias Automatic Evaluators](https://arxiv.org/abs/2404.04475)** · COLM 2024 · 2024

C · included · full text checked

Regresses out answer length to produce a length-controlled win rate, reducing verbosity bias.

Tasks: output quality. Methods: pairwise comparison.

- **Object** — Two instruction-following answers.
- **Criteria and evidence** — AlpacaEval pairwise preference protocol. Regression adjusts for answer lengths.
- **Judge output** — Judge preference followed by a statistically adjusted win rate.
- **Method location** — Method for length-controlled win rates and Fig. 3 length intervention. [Source](https://arxiv.org/pdf/2404.04475)
- **Repeated judgments** — Not reported
- **Expert agreement** — Compared ranking correlations with Chatbot Arena human preferences. Domain-expert validation was not reported.
- **Literature support** — Not reported
- **Biological experimental validation** — Not reported
- **Decision or efficiency benefit** — Not reported
- **Limitation** — Length adjustment targets a specified confounder and depends on model assumptions.
- **Screening rationale** — Helps audit whether detailed scientific outputs win because they are longer.

[doi](https://doi.org/10.48550/arXiv.2404.04475) · [arxiv](https://arxiv.org/abs/2404.04475) · [code](https://github.com/tatsu-lab/alpaca_eval)

### non-transitivity

**[Investigating Non-Transitivity in LLM-as-a-Judge](https://arxiv.org/abs/2502.14074)** · ICML 2025 · 2025

C · included · full text checked

Shows pairwise LLM judgments violate transitivity; analyzes Bradley-Terry limits and round-robin tournament aggregation.

Tasks: output quality. Methods: pairwise comparison, ranking.

- **Object** — Pairs of answers to a common instruction.
- **Criteria and evidence** — AlpacaEval judge prompt and position-switched comparisons.
- **Judge output** — Pairwise preferences aggregated across tournament schedules.
- **Method location** — Judge models and Position Switching, p. 4. Appendix G.1 prompt. [Source](https://arxiv.org/pdf/2502.14074)
- **Repeated judgments** — Not reported
- **Expert agreement** — Comparison with Arena crowd rankings. Biological expert labels were not reported.
- **Literature support** — Not reported
- **Biological experimental validation** — Not reported
- **Decision or efficiency benefit** — Not reported
- **Limitation** — Model-level instruction-following rankings provide no direct test of biological candidate selection.
- **Screening rationale** — Supplies a diagnostic for cyclic preferences before aggregating candidate rankings.

[doi](https://doi.org/10.48550/arXiv.2502.14074) · [arxiv](https://arxiv.org/abs/2502.14074)

### fair-evaluators

**[Large Language Models are not Fair Evaluators](https://doi.org/10.18653/v1/2024.acl-long.511)** · ACL 2024 · 2024

C · included · full text checked

Swapping the order of two answers changes the reported winner. The authors test balanced presentation orders to reduce this effect.

Tasks: output quality. Methods: pairwise comparison.

- **Object** — Two answers to the same benchmark question.
- **Criteria and evidence** — Question and comparison instructions with the presentation order reversed.
- **Judge output** — Scores/preferences combined across orderings.
- **Method location** — Evaluation template and balanced position calibration, pp. 2–4 of the preprint. [Source](https://arxiv.org/pdf/2305.17926)
- **Repeated judgments** — Not reported
- **Expert agreement** — Comparison with human preferences on the evaluation set. Biological expertise was not assessed.
- **Literature support** — Not reported
- **Biological experimental validation** — Not reported
- **Decision or efficiency benefit** — Not reported
- **Limitation** — An ordering control leaves validity of the underlying criterion unresolved.
- **Screening rationale** — A practical order-swap control for ranking scientific responses.

[doi](https://doi.org/10.18653/v1/2024.acl-long.511) · [arxiv](https://arxiv.org/abs/2305.17926)

### self-preference

**[LLM Evaluators Recognize and Favor Their Own Generations](https://arxiv.org/abs/2404.13076)** · NeurIPS 2024 · 2024

C · included · full text checked

Tests whether judges recognize their own text and finds that stronger self-recognition tracks a stronger preference for their own answers.

Tasks: output quality. Methods: pointwise scoring, pairwise comparison.

- **Object** — Model-written summaries.
- **Criteria and evidence** — Summary evaluation instructions in individual and paired conditions, with separate authorship-recognition tasks.
- **Judge output** — Individual 1–5 quality rating or pairwise preference.
- **Method location** — Individual and pairwise measurements, p. 2. [Source](https://arxiv.org/pdf/2404.13076)
- **Repeated judgments** — Not reported
- **Expert agreement** — Not reported
- **Literature support** — Not reported
- **Biological experimental validation** — Not reported
- **Decision or efficiency benefit** — Not reported
- **Limitation** — Experiments establish a risk in summarization. Its magnitude on hypotheses is unknown.
- **Screening rationale** — Tests a confounder when a hypothesis generator also evaluates its own outputs.

[doi](https://doi.org/10.48550/arXiv.2404.13076) · [arxiv](https://arxiv.org/abs/2404.13076)

### verdict-reliability

**[All Verdicts are Not Equal: Rethinking LLM Judge Reliability](https://doi.org/10.18653/2026.aacl-long.207)** · AACL-IJCNLP 2026 · 2026

C · included · full text checked

Crosses repeated trials with answer-order swaps and reference labels to distinguish reproducibility, order sensitivity, and correctness.

Tasks: output quality. Methods: pairwise comparison, pointwise scoring.

- **Object** — Responses in preference/correctness benchmarks.
- **Criteria and evidence** — Question and evaluation instructions varied across prompt formats, orders and repetitions.
- **Judge output** — Repeated verdicts compared with reference labels.
- **Method location** — §4.3 Prompt Formats and repeated-trial evaluation. [Source](https://arxiv.org/pdf/2610.12083)
- **Repeated judgments** — Repeated trials within condition plus order changes. Agreement with reference labels is evaluated separately.
- **Expert agreement** — Not reported
- **Literature support** — Not reported
- **Biological experimental validation** — Not reported
- **Decision or efficiency benefit** — Not reported
- **Limitation** — Reference labels and task difficulty affect interpretation outside the benchmark.
- **Screening rationale** — Separates repeatability, order invariance and agreement with reference labels.

[doi](https://doi.org/10.18653/2026.aacl-long.207) · [arxiv](https://arxiv.org/abs/2610.12083)

### judge-survey

**[A survey on LLM-as-a-judge](https://doi.org/10.1016/j.xinn.2025.101253)** · The Innovation, article 101253 (arXiv first posted 2024) · 2026

E · included · full text checked

Maps the LLM-as-a-Judge landscape, including a consistency/reliability cluster covering biases and stability.

- **Object** — Not applicable to the survey role.
- **Criteria and evidence** — Not applicable to the survey role.
- **Judge output** — Not applicable to the survey role.
- **Method location** — §§2–4, especially agreement, bias and robustness in §4. [Source](https://arxiv.org/html/2411.15594v6)
- **Repeated judgments** — Not applicable to citation-tracing use of this review.
- **Expert agreement** — Not applicable to citation-tracing use of this review.
- **Literature support** — Not applicable to citation-tracing use of this review.
- **Biological experimental validation** — Not applicable to citation-tracing use of this review.
- **Decision or efficiency benefit** — Not applicable to citation-tracing use of this review.
- **Limitation** — Broad survey. Biology-specific claims require the underlying primary paper.
- **Screening rationale** — Citation tracing and terminology. Counted only as a review.

[doi](https://doi.org/10.1016/j.xinn.2025.101253) · [arxiv](https://arxiv.org/abs/2411.15594)

### rewardbench

**[RewardBench: Evaluating Reward Models for Language Modeling](https://arxiv.org/abs/2403.13787)** · Findings of NAACL 2025 · 2025

C · excluded · abstract only

Benchmark probing reward-model / judge reliability across chat, reasoning, and safety prompts.

Tasks: output quality. Methods: .

- **Object** — Preferred and rejected outputs for a prompt.
- **Criteria and evidence** — Constructed prompt–chosen–rejected triples spanning chat, reasoning and safety.
- **Judge output** — Whether a reward model assigns the preferred response the higher reward. A direct prompted-LLM verdict was not established in this audit.
- **Method location** — Abstract (screening decision only). [Source](https://arxiv.org/abs/2403.13787)
- **Repeated judgments** — Pending verification
- **Expert agreement** — Pending verification
- **Literature support** — Pending verification
- **Biological experimental validation** — Pending verification
- **Decision or efficiency benefit** — Pending verification
- **Limitation** — Method-level evidence has not been extracted for this catalogue.
- **Screening rationale** — Historical benchmark for reward models. Its benchmark labels alone do not establish biological LLM judgment.

[doi](https://doi.org/10.18653/v1/2025.findings-naacl.96) · [arxiv](https://arxiv.org/abs/2403.13787) · [code](https://github.com/allenai/reward-bench)

### rankrefine

**[Post Hoc Regression Refinement via Pairwise Rankings](https://arxiv.org/abs/2508.16495)** · NeurIPS 2025 · 2025

C · excluded · abstract only

Combines a regression prediction with information from pairwise comparisons.

Tasks: . Methods: pairwise comparison.

- **Object** — Items whose continuous property is to be predicted.
- **Criteria and evidence** — Comparisons with reference items having known values.
- **Judge output** — Pairwise order information used to refine a numerical prediction.
- **Method location** — Abstract (screening decision only). [Source](https://arxiv.org/abs/2508.16495)
- **Repeated judgments** — Pending verification
- **Expert agreement** — Pending verification
- **Literature support** — Pending verification
- **Biological experimental validation** — Pending verification
- **Decision or efficiency benefit** — Pending verification
- **Limitation** — Method-level evidence has not been extracted for this catalogue.
- **Screening rationale** — The linked paper refines continuous property estimates with pairwise rankings. The legacy title misidentified the method as repair of LLM judge rankings.

[doi](https://doi.org/10.48550/arXiv.2508.16495) · [arxiv](https://arxiv.org/abs/2508.16495)

### same-input

**[Same Input, Different Scores: A Multi Model Study on the Inconsistency of LLM Judge](https://arxiv.org/abs/2603.04417)** · arXiv preprint · 2026

C · excluded · full text checked

Repeats scoring on identical inputs to measure within-judge variation, between-judge differences, and sensitivity to sampling temperature.

Tasks: output quality. Methods: pointwise scoring.

- **Object** — Enterprise chatbot answers.
- **Criteria and evidence** — Question and answer with attribute definitions including relevance, reliability and completeness.
- **Judge output** — Per-attribute numeric ratings.
- **Method location** — §3 Experiment, attribute definitions and temperature settings. [Source](https://arxiv.org/pdf/2603.04417)
- **Repeated judgments** — Compares repeated scores within model and across two temperatures.
- **Expert agreement** — Pending verification
- **Literature support** — Pending verification
- **Biological experimental validation** — Not reported
- **Decision or efficiency benefit** — Not reported
- **Limitation** — Application to biological decisions has not been demonstrated.
- **Screening rationale** — Archived after screening. The enterprise scoring task overlaps the repeatability diagnostics already retained.

[doi](https://doi.org/10.48550/arXiv.2603.04417) · [arxiv](https://arxiv.org/abs/2603.04417)

### coin-flip

**[The Coin Flip Judge? Reliability and Bias in LLM-as-a-Judge Evaluation](https://arxiv.org/abs/2606.13685)** · arXiv preprint · 2026

C · excluded · full text checked

Compares repeated pairwise verdicts with pointwise score gaps and estimates how many votes recover a reference verdict in the studied sample.

Tasks: output quality. Methods: pairwise comparison, pointwise scoring.

- **Object** — Pairs of answers on 29 selected questions.
- **Criteria and evidence** — Question, two competitive responses, evaluation prompt and controlled order/settings.
- **Judge output** — A/B/tie or a separate 1–10 pointwise grade.
- **Method location** — Definitions 1–4 and §4 Methodology. [Source](https://arxiv.org/pdf/2606.13685)
- **Repeated judgments** — Compares repeated vote distributions with pointwise score gaps and a 50-trial reference verdict.
- **Expert agreement** — Pending verification
- **Literature support** — Pending verification
- **Biological experimental validation** — Not reported
- **Decision or efficiency benefit** — Not reported
- **Limitation** — Application to biological decisions has not been demonstrated.
- **Screening rationale** — Archived as a supplementary voting study. The 50-trial reference is the judge’s own consensus, so it supplies no external criterion for a biological verdict.

[doi](https://doi.org/10.48550/arXiv.2606.13685) · [arxiv](https://arxiv.org/abs/2606.13685)

### judgebench

**[JudgeBench: A Benchmark for Evaluating LLM-based Judges](https://arxiv.org/abs/2410.12784)** · ICLR 2025 · 2025

C · excluded · abstract only

Tests whether judges identify the correct response in hard pairs spanning knowledge, reasoning, mathematics, and code.

Tasks: output quality. Methods: pairwise comparison.

- **Object** — Two responses to a challenging question.
- **Criteria and evidence** — The original question and a response pair with an objectively checkable quality distinction.
- **Judge output** — Preferred response, evaluated against the reference choice.
- **Method location** — Abstract (screening decision only). [Source](https://arxiv.org/abs/2410.12784)
- **Repeated judgments** — Pending verification
- **Expert agreement** — Pending verification
- **Literature support** — Pending verification
- **Biological experimental validation** — Pending verification
- **Decision or efficiency benefit** — Pending verification
- **Limitation** — Method-level evidence has not been extracted for this catalogue.
- **Screening rationale** — General benchmark. The present collection prioritizes transferable methods already used in the reading guide.

[doi](https://doi.org/10.48550/arXiv.2410.12784) · [arxiv](https://arxiv.org/abs/2410.12784)

### pairwise-alignment

**[Aligning with Human Judgement: The Role of Pairwise Preference in Large Language Model Evaluators](https://arxiv.org/abs/2403.16950)** · COLM 2024 · 2024

C · excluded · abstract only

Studies residual disagreement after bias calibration and uses pairwise human preferences to improve evaluator alignment.

Tasks: output quality. Methods: pairwise comparison.

- **Object** — Generated language-model answers.
- **Criteria and evidence** — Human preference data inform evaluator alignment.
- **Judge output** — Pending verification
- **Method location** — Abstract (screening decision only). [Source](https://arxiv.org/abs/2403.16950)
- **Repeated judgments** — Pending verification
- **Expert agreement** — Pending verification
- **Literature support** — Pending verification
- **Biological experimental validation** — Pending verification
- **Decision or efficiency benefit** — Pending verification
- **Limitation** — Method-level evidence has not been extracted for this catalogue.
- **Screening rationale** — Historical evaluator-training reference. Human preference alignment is covered by direct drug-discovery evidence in this reading set.

[doi](https://doi.org/10.48550/arXiv.2403.16950) · [arxiv](https://arxiv.org/abs/2403.16950)

<!-- PAPER-LIST:END -->
