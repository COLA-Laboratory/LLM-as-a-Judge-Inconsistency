# Screening and migration

The snapshots preserve the original data, descriptions, generator and README at their exact revisions. Main contained six records. The earlier draft contained twelve, including seven additions and the removal of RankRefine. “Legacy” below identifies the source of each record. Screening decisions refer to this survey's selection criteria.

- [Main before reorganization](https://github.com/COLA-Laboratory/LLM-as-a-Judge-Inconsistency/tree/cfae24570b1eefffcbaaab9f7d7b8eae3b6525cb)
- [Earlier literature draft](https://github.com/COLA-Laboratory/LLM-as-a-Judge-Inconsistency/tree/3468768cf15c8fed59583a2a69bc5581bef88c96)

The old README also linked resources outside its structured paper list. Chatbot Arena, Arena-Hard and WildBench remain in the historical benchmark directory in the main snapshot. Named aggregation baselines there are historical pointers. Robin, Co-Scientist and BioDiscoveryAgent were outside this seed audit. No standalone judge-method credit is assigned from a system name or a system-level result.

[Evidence notes](evidence.md) · [Main page](../README.md)

<!-- PAPER-LIST:START -->

| Record | Legacy | Role | Decision | Reading | Reason |
|---|---|---|---|---|---|
| [skim-gpt](evidence.md#skim-gpt) | New | A | included | full text checked | Design and expert comparison of the evidence-based judge are central contributions. |
| [knowhd](evidence.md#knowhd) | New | A | included | full text checked | KnowHD is a separately specified and evaluated biomedical evidence judge. |
| [chatinvent-judge](evidence.md#chatinvent-judge) | New | A | included | full text checked | The central contribution is judge design and expert alignment in drug discovery. |
| [qi-biomedical](evidence.md#qi-biomedical) | New | B | included | full text checked | The generator comparison is the main research question. Its scoring module meets all four inclusion criteria. |
| [valsci](evidence.md#valsci) | New | D | included | full text checked | Adjacent scientific literature-review workflow with an identifiable judge. Its target is general claim verification. |
| [g-eval](evidence.md#g-eval) | New | C | included | full text checked | Template for specifying criteria and comparing rubric scores with human ratings. |
| [factscore](evidence.md#factscore) | New | C | included | full text checked | Methodological precursor to claim-level groundedness metrics. |
| [mt-bench](evidence.md#mt-bench) | main, draft | C | included | full text checked | Baseline for designing pointwise and pairwise biological rubrics. |
| [length-controlled-alpacaeval](evidence.md#length-controlled-alpacaeval) | main, draft | C | included | full text checked | Helps audit whether detailed scientific outputs win because they are longer. |
| [non-transitivity](evidence.md#non-transitivity) | main, draft | C | included | full text checked | Supplies a diagnostic for cyclic preferences before aggregating candidate rankings. |
| [fair-evaluators](evidence.md#fair-evaluators) | draft | C | included | full text checked | A practical order-swap control for ranking scientific responses. |
| [self-preference](evidence.md#self-preference) | draft | C | included | full text checked | Tests a confounder when a hypothesis generator also evaluates its own outputs. |
| [verdict-reliability](evidence.md#verdict-reliability) | draft | C | included | full text checked | Separates repeatability, order invariance and agreement with reference labels. |
| [judge-survey](evidence.md#judge-survey) | main, draft | E | included | full text checked | Citation tracing and terminology. Counted only as a review. |
| [rewardbench](evidence.md#rewardbench) | main, draft | C | excluded | abstract only | Historical benchmark for reward models. Its benchmark labels alone do not establish biological LLM judgment. |
| [rankrefine](evidence.md#rankrefine) | main | C | excluded | abstract only | The linked paper refines continuous property estimates with pairwise rankings. The legacy title misidentified the method as repair of LLM judge rankings. |
| [same-input](evidence.md#same-input) | draft | C | excluded | full text checked | Archived after screening. The enterprise scoring task overlaps the repeatability diagnostics already retained. |
| [coin-flip](evidence.md#coin-flip) | draft | C | excluded | full text checked | Archived as a supplementary voting study. The 50-trial reference is the judge’s own consensus, so it supplies no external criterion for a biological verdict. |
| [judgebench](evidence.md#judgebench) | draft | C | excluded | abstract only | General benchmark. The present collection prioritizes transferable methods already used in the reading guide. |
| [pairwise-alignment](evidence.md#pairwise-alignment) | draft | C | excluded | abstract only | Historical evaluator-training reference. Human preference alignment is covered by direct drug-discovery evidence in this reading set. |

<!-- PAPER-LIST:END -->
