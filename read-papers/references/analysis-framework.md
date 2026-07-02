# Paper analysis framework

## Contents

1. Evidence standard
2. Background and task
3. Method and derivation
4. Innovation
5. Experiments
6. Limitations
7. Batch synthesis

## 1. Evidence standard

Use three evidence states:

- **Reported**: explicitly stated or shown in the paper. Attach a locator.
- **Derived**: reconstructed from reported equations or algorithm steps. State the starting evidence and assumptions.
- **Inferred**: a critical interpretation not claimed by the paper. Mark it as analysis and explain the evidence.

Prefer locators in this order: `p. 7, Eq. (4)`; `p. 7, Sec. 3.2`; `Table 2`; `Fig. 3`; `Appendix B`. Never fabricate page or equation numbers. Avoid long quotations; paraphrase technical claims faithfully.

## 2. Background and task

Extract:

- Application or scientific context and why the problem matters.
- Exact task, inputs, outputs, supervision, constraints, and deployment setting.
- Prior-work bottleneck that motivates this paper.
- Scope: what the paper does and does not attempt.
- One-sentence contribution in the form: “For [task], the paper proposes [mechanism] to address [gap], evaluated by [main evidence].”

Do not confuse the broad field with the actual task. For example, “medical imaging” is a field; “few-shot 3D liver segmentation under cross-site shift” is a task.

## 3. Method and derivation

Build a causal chain:

`problem definition → representation/model → core transformation → objective/constraint → optimization/training → inference/output`.

For each central equation:

1. Give its role in plain language.
2. Define symbols, shapes or domains when relevant.
3. State where quantities come from.
4. Derive the next important expression or algorithmic step.
5. Explain the effect of each loss term, constraint, or hyperparameter.
6. Connect the mathematics to the claimed benefit.

Cover complexity, convergence, or identifiability only when the paper provides evidence or when a clearly labeled derivation is possible. For empirical systems without meaningful mathematics, give an algorithmic trace or pseudocode-style data flow instead of manufacturing equations.

Use these labels:

- `论文原式/原推导`: faithful rendering of a paper equation or proof step.
- `重建推导`: algebra or logic reconstructed from paper evidence.
- `解释`: intuition or consequence.

## 4. Innovation

For each innovation, state:

- The closest prior practice or baseline.
- The exact technical difference.
- Why that difference should matter.
- Which experiment, ablation, theorem, or analysis supports it.
- Whether it is an architectural, objective, optimization, data, theoretical, or evaluation contribution.

Separate real novelty from engineering integration and from the authors' marketing language. If novelty cannot be assessed without broader literature search, say so.

## 5. Experiments

Extract a structured record:

- **Datasets**: name, domain, scale, split, preprocessing, augmentation, licensing or access notes if reported.
- **Metrics**: name, formula or interpretation, direction (higher/lower is better), aggregation, and protocol.
- **Baselines**: model/version, comparison category, tuning fairness, and source.
- **Implementation**: backbone, optimizer, schedule, batch size, hardware, seeds, parameter count, FLOPs, latency, or training cost when reported.
- **Results**: main values, uncertainty, significance tests, best/second-best conventions, and protocol caveats.
- **Ablations**: changed factor, controlled variables, observed effect, and what claim it supports.
- **Robustness**: cross-domain, sensitivity, failure cases, and reproducibility evidence.

Never infer superiority from bold formatting alone. Verify metric direction, table headers, dataset split, and evaluation protocol. Do not compare numbers across incompatible settings.

## 6. Limitations

Separate:

1. `作者承认的局限`: explicitly acknowledged in the paper.
2. `基于证据的评估`: limitations inferred from missing controls, narrow data, assumptions, compute cost, weak baselines, metric mismatch, statistical uncertainty, reproducibility gaps, or deployment risk.

Phrase criticism proportionally. Missing evidence means the claim is unsupported in this paper, not necessarily false. Include likely failure modes and what experiment would resolve each important uncertainty.

## 7. Batch synthesis

Compare papers only after their individual records are complete. Group by compatible task and protocol. Identify:

- Common problem formulations and recurring method families.
- Genuine differences in assumptions, objectives, and evidence.
- Dataset or benchmark concentration and possible blind spots.
- Contradictory findings and whether protocol differences explain them.
- Strong reusable components and open research questions.
- A reading order based on foundational value, methodological clarity, and relevance.

Record `完整`, `部分完成`, or `失败` for every requested paper so batch summaries never silently omit an input.

