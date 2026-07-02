---
name: read-papers
description: Read and critically analyze one or many academic papers from PDFs, local documents, URLs, DOIs, arXiv links, or pasted text, then generate structured Markdown notes. Use when Codex needs to extract a paper's research background and task, reconstruct core methods and mathematical derivations, identify innovations and limitations, summarize datasets, metrics, baselines, ablations, and results, or compare a batch of papers in a literature matrix or synthesis report.
---

# Read Papers

Produce evidence-grounded paper notes in Markdown for either one paper or a batch. Preserve English titles, formulas, variable names, dataset names, model names, and citations; write the explanation in the user's language unless requested otherwise.

## Choose the workflow

- For one paper, create one note from `assets/single-paper-template.md`.
- For multiple papers, create one note per paper plus `index.md` from `assets/batch-index-template.md`.
- If the user requests one combined file, merge the per-paper sections and comparison synthesis into that file.
- If the user supplies a directory, run `scripts/prepare_review.py` to inventory supported paper files and create collision-safe output paths.
- If the user gives only citations, titles, URLs, or DOIs, locate the authoritative paper or an accessible full-text version before analysis. Clearly label any abstract-only analysis.

Read `references/analysis-framework.md` before analyzing any paper. It defines the evidence rules, derivation standard, and extraction schema.

## Read the sources

1. Inventory every requested paper and report unreadable, duplicate, or missing inputs.
2. Read the full paper, including appendices and supplementary material when available. Inspect equations, tables, figures, captions, and footnotes rather than relying only on extracted prose.
3. Use OCR when a PDF is scanned. If equations or tables remain illegible, mark the affected fields as `无法从当前来源可靠提取` and state what is missing.
4. Treat the paper as the primary source. Use external sources only to resolve metadata, locate full text, or verify a technical dependency; distinguish external information from paper claims.
5. Capture a source locator for every important claim: page plus section, equation number, theorem, algorithm, table, or figure. If pagination is unavailable, use the most precise section-level locator.

Do not invent missing details. Use `文中未报告` for absent experimental information and `无法确认` for ambiguous content.

## Analyze each paper

Follow this order:

1. Record bibliographic metadata and the paper's one-sentence contribution.
2. Explain the background, concrete task, input/output, assumptions, and why prior approaches are insufficient.
3. Reconstruct the method from problem formulation through objective, algorithm, training, and inference.
4. Extract innovations as testable differences from the closest prior work, not as a restatement of the abstract.
5. Extract datasets, splits, preprocessing, metrics, baselines, implementation details, main results, ablations, and efficiency evidence.
6. Critique limitations by separating limitations acknowledged by the authors from your own evidence-based assessment.
7. Complete every template section. Keep unknown fields explicit rather than deleting them.

For mathematical work:

- Define every symbol before using it.
- Show the dependency chain from assumptions and inputs to the final objective or prediction.
- Include the core intermediate steps needed to understand why the method works; do not merely paste the final loss function.
- Label content as `论文原式/原推导` when directly supported and `重建推导` when filling omitted algebra or connecting steps.
- Never present a reconstructed step as a verbatim claim by the authors.

## Handle batches

1. Keep the same extraction schema across all papers.
2. Write each paper note independently before producing cross-paper conclusions.
3. Build a comparison matrix covering task, key mechanism, objective, datasets, metrics, baselines, strongest result, compute/efficiency, and limitations.
4. Normalize aliases only when equivalence is certain. Preserve metric direction and units, and never compare values from incompatible datasets or protocols as if they were directly comparable.
5. Synthesize research trends, meaningful disagreements, reusable ideas, open problems, and recommended reading order.
6. Report completion counts and any failed or partial reads in `index.md`.

For a large local batch, use:

```powershell
python scripts/prepare_review.py <paper-or-directory> --output <output-directory> --recursive
```

Read the generated `manifest.json`, fill the assigned note files, update each manifest status to `complete`, `partial`, or `failed`, then run:

```powershell
python scripts/validate_review.py <output-directory>
```

Fix missing required sections before delivery. The validator checks structure, not factual correctness; perform an evidence pass separately.

## Deliver Markdown

- Use GitHub-Flavored Markdown and LaTeX math.
- Default output names to `<paper-slug>.md` for notes and `index.md` for batch synthesis.
- Make all local source and note links relative inside generated artifacts when practical.
- Include a compact source-location column in extraction tables.
- End each note with a short confidence and completeness statement.
- Tell the user exactly which files were created and which inputs were only partially analyzed.
