# LLM-as-a-Judge for Biological Scientific Discovery

*Tasks, Methods, and Validation*

How do language models judge a hypothesis, a mechanism, an experiment, a candidate or a research result? This reading collection for a survey follows each judgment from the evidence available to the model through its verdict to any measured change in research decisions. Its scope covers basic biology, biological engineering and drug discovery. Clinical diagnosis and patient advice are adjacent areas.

[Reading guide](#reading-guide) · [Literature by role](#literature-by-role) · [Evidence notes](docs/evidence.md) · [Screening and migration](docs/screening.md) · [Contributing](#contributing)

## Reading guide

- Start with [SKiM-GPT](docs/evidence.md#skim-gpt) to see four experts and a model assess the same abstracts. Compare what the authors measured about agreement and review time.
- Read [KnowHD](docs/evidence.md#knowhd) alongside [FActScore](docs/evidence.md#factscore) to see how claim-level evidence becomes a score. A newly proposed relationship can lack prior support even when its premises are sound.
- Compare the [ChatInvent judge](docs/evidence.md#chatinvent-judge) with the [biomedical hypothesis generator study](docs/evidence.md#qi-biomedical). The former validates an evaluator. The latter uses a scoring rubric to compare generators.

## Inclusion criteria

For a direct judge record, identify the evaluated object, the criteria or evidence available to the LLM, its verdict format, and a full-text method, appendix or public prompt that establishes the first three. Primary research here means work that introduces, implements or tests a method. Generation alone, human-only review, property prediction and programmatic metrics do not qualify a paper as using an LLM judge.

Each work has one role. Task and method tags describe the judgment independently. A and B form the biological primary reading set. D covers workflows and adjacent applications with an identifiable judge. Surveys are counted separately. The evidence notes distinguish repeated judgments, expert agreement, literature support, experimental confirmation and downstream benefit.

## Literature by role

<!-- PAPER-LIST:START -->

### A. Judge methods and validation (3)

- [SKiM-GPT: combining biomedical literature-based discovery with large language model hypothesis evaluation](docs/evidence.md#skim-gpt) (2026). Scores how strongly the retrieved abstracts support a proposed biomedical relationship.
- [Toward Reliable Scientific Hypothesis Generation: Evaluating Truthfulness and Hallucination in Large Language Models](docs/evidence.md#knowhd) (2025). Estimates how much of a hypothesis and its rationale is grounded in earlier knowledge.
- [Designing an LLM-based evaluation system for agentic AI in drug discovery through human alignment](docs/evidence.md#chatinvent-judge) (2026). Validates a rubric for grading a drug-discovery assistant’s responses against expert ratings.

### B. Biological studies using a judge (1)

- [Large Language Models as Biomedical Hypothesis Generators: A Comprehensive Evaluation](docs/evidence.md#qi-biomedical) (2024). Compares hypothesis generators using a GPT-4 assessment alongside text-overlap and human assessments.

### C. General methods and reliability (8)

- [G-Eval: NLG Evaluation using GPT-4 with Better Human Alignment](docs/evidence.md#g-eval) (2023). Operationalizes a written evaluation criterion as model-generated evaluation steps and a score.
- [FActScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation](docs/evidence.md#factscore) (2023). Decomposes long answers and estimates the fraction of facts supported by a reference source.
- [Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena](docs/evidence.md#mt-bench) (2023). Introduces MT-Bench and documents position, verbosity, and self-enhancement biases in LLM judges.
- [Length-Controlled AlpacaEval: A Simple Way to Debias Automatic Evaluators](docs/evidence.md#length-controlled-alpacaeval) (2024). Regresses out answer length to produce a length-controlled win rate, reducing verbosity bias.
- [Investigating Non-Transitivity in LLM-as-a-Judge](docs/evidence.md#non-transitivity) (2025). Shows pairwise LLM judgments violate transitivity; analyzes Bradley-Terry limits and round-robin tournament aggregation.
- [Large Language Models are not Fair Evaluators](docs/evidence.md#fair-evaluators) (2024). Swapping the order of two answers changes the reported winner. The authors test balanced presentation orders to reduce this effect.
- [LLM Evaluators Recognize and Favor Their Own Generations](docs/evidence.md#self-preference) (2024). Tests whether judges recognize their own text and finds that stronger self-recognition tracks a stronger preference for their own answers.
- [All Verdicts are Not Equal: Rethinking LLM Judge Reliability](docs/evidence.md#verdict-reliability) (2026). Crosses repeated trials with answer-order swaps and reference labels to distinguish reproducibility, order sensitivity, and correctness.

### D. Workflows and adjacent cases (1)

- [Valsci: an open-source, self-hostable literature review utility for automated large-batch scientific claim verification using large language models](docs/evidence.md#valsci) (2025). Uses retrieved sources to produce a claim-level evidence report.

### E. Related reviews (1)

- [A survey on LLM-as-a-judge](docs/evidence.md#judge-survey) (2026). Maps the LLM-as-a-Judge landscape, including a consistency/reliability cluster covering biases and stability.

<!-- PAPER-LIST:END -->

## Contributing

Edit [papers.yaml](papers.yaml). Copy a record of the same role, assign a permanent ID, and record the publication year, venue and available version identifiers. Put the preprint and published paper on one record. Use the five validation fields independently. Use “Not reported” for an unreported endpoint and “Pending verification” for one that could not be checked. Specify a concrete method location and source before marking a work included.

Install PyYAML with `python3 -m pip install PyYAML`. Run `python3 generate_paper_list.py` to rebuild the index and evidence pages, then `python3 generate_paper_list.py --check` to validate the files. Edit prose outside the marked blocks. Put longer manual notes outside those blocks and reference the permanent paper ID.
