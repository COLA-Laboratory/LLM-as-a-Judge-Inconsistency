# Judge design checklist and example evaluation record

Use the checklist before designing a prompt. Then copy one record per evaluation unit so another reader can reconstruct what the judge saw, what it decided and what action followed. For published methods and their validation evidence, see the [evidence notes](evidence.md).

[Design checklist](#design-checklist) · [Copyable record](#copyable-record) · [Illustrative example](#illustrative-example)

## Design checklist

- [ ] **Object and unit.** Identify the item being judged. Specify whether one verdict covers a whole hypothesis, a single claim, a pair of proposals or one assistant response.
- [ ] **Criteria.** Phrase each dimension as an answerable question. Define what counts as a match, a contradiction or an out-of-scope case before scoring.
- [ ] **Evidence access.** List allowed sources, exact passages or versions, search scope and cutoff. Separate what the judge can see from material reserved for independent checks.
- [ ] **Output contract.** Choose a label, score or preference for each dimension. Define every label or scale endpoint. Require a brief rationale and evidence IDs for each decision.
- [ ] **Abstention.** Reserve an explicit abstention label. Record the cause, such as missing evidence, conflicting sources or ambiguous wording, and what would resolve it. An empty result or a zero score obscures this distinction.
- [ ] **Independent validation.** Choose a held-out reference, separate search or blinded reviewer appropriate to each dimension. Record the comparison unit, planned check, status and observed result. Repeat calls can test stability; agreement with an independent reference answers a different question.
- [ ] **Research action.** Decide in advance which verdict triggers additional reading, revision or human review. Record the action actually taken separately from the rule.

## Copyable record

Copy the YAML block and replace the placeholders. List the allowed labels and their meanings in the versioned rubric. Cite only evidence the judge was allowed to see. Add a validation entry for each distinct check, and leave its result as `null` until that check has been performed.

```yaml
id: "<record ID>"
unit: "<one item, its scope and the exact question or claim>"
model_version: "<provider, model and dated version>"
prompt_version: "<prompt ID, version and retrievable location>"
rubric_version: "<rubric ID, version and retrievable location>"
evidence_scope: "<allowed sources, search coverage, cutoff and exclusions>"
evidence:
  - {id: E1, source: "<document/version and passage>", content: "<visible excerpt>"}
judgments:
  literature_support: {label: "<label>", evidence_ids: [], reason: "<basis or reason for abstention>"}
  novelty: {label: "<label>", evidence_ids: [], reason: "<basis or reason for abstention>"}
  experimental_testability: {label: "<label>", evidence_ids: [], reason: "<basis or reason for abstention>"}
validation:
  - dimension: "<dimension>"
    independent_material: "<material or reviewer withheld from the judge>"
    check: "<what will be compared, and on which unit>"
    status: planned
    result: null
action_rule: "<decision rule>"
action_taken: null
```

## Illustrative example

This hand-filled record uses a fictional hypothesis about a plant trait. G, T, C1 and C2 are placeholders. The evidence cards are invented text for illustrating the rubric. No model was run, no expert supplied a rating and no biological measurements were made.

**Prompt v1.** Read only the claim and the visible evidence cards. Return one label per dimension using the rubric below. For each label, cite the relevant card IDs and give one sentence of reasoning. If the necessary information is missing, abstain on that dimension and name what is missing.

**Rubric v1**

| Dimension | Question | Label meanings |
|---|---|---|
| Literature support | Does the visible literature address the stated group, comparison, trait and direction? | `direct` = all four match and support the claim; `indirect` = relevant evidence with a material scope mismatch; `contradicted` = matched evidence supports the opposite direction; `abstain` = missing or conflicting evidence prevents a verdict. |
| Novelty | Does a documented prior-art search identify this same claim? | `prior_match` = a matching claim was located; `no_match_in_scope` = a completed, bounded search found none; `abstain` = the search scope or coverage is inadequate. |
| Experimental testability | Does the statement specify an observable comparison and an outcome that would count against it? | `specified` = both are identifiable; `needs_revision` = a clear omission prevents a test; `abstain` = the available wording cannot be interpreted. This criterion covers test design at the level of the claim; practical feasibility requires separate assessment. |

```yaml
id: teaching-plant-trait-01
unit: "One hypothesis: in plant group G, mean observable trait T is higher in C1 than in C2."
model_version: "None. Hand-filled teaching example."
prompt_version: "v1, Prompt v1 above"
rubric_version: "v1, Rubric v1 above"
evidence_scope: "Only cards E1 and E2. No outside search, prior-art corpus or search cutoff."
evidence:
  - id: E1
    source: "Fictional literature card, version 1, passage A"
    content: "This placeholder describes the same directional comparison for a different group, G-other."
  - id: E2
    source: "Fictional definitions card, version 1, passage B"
    content: "T denotes an observable trait. C1 and C2 identify two distinguishable conditions."
judgments:
  literature_support:
    label: indirect
    evidence_ids: [E1]
    reason: "E1 concerns G-other. Direct support would require evidence about the stated group G."
  novelty:
    label: abstain
    evidence_ids: []
    reason: "No prior-art search was available. Record the corpus, query, cutoff and matches before judging novelty."
  experimental_testability:
    label: specified
    evidence_ids: [E2]
    reason: "The claim identifies a comparison. An equal or lower mean T in C1 would count against its predicted direction."
validation:
  - dimension: literature_support
    independent_material: "Planned held-out source passage and a reviewer blinded to the judge label."
    check: "For this claim, compare the reviewer's scope-match label with the recorded support label."
    status: planned
    result: null
  - dimension: novelty
    independent_material: "Planned independent prior-art search with documented coverage and cutoff."
    check: "Have a separate reader inspect retrieved claims for a match before revisiting the abstention."
    status: planned
    result: null
  - dimension: experimental_testability
    independent_material: "Planned independent reader given only the claim and definitions."
    check: "Compare the reader's observable contrast and disconfirming outcome with the stated rationale."
    status: planned
    result: null
action_rule: "Route indirect support to a source review for group G. Defer any novelty claim until the search is documented."
action_taken: null
```

The three labels lead to different actions. The group mismatch calls for a source review, novelty remains open until someone performs a search, and the wording already identifies a testable contrast. A single “scientific correctness” score would hide the missing search and allow testability to compensate numerically for weak support. None of these labels establishes the biological outcome.

[Survey homepage](../README.md) · [Evidence notes from published studies](evidence.md)
