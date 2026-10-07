# PDF QA Bot — Evaluation guide

Start with the smallest path that exercises the project. Distinguish source inspection,
syntax/build checks, functional behavior and domain validation when recording a result.

## Guided reading and demonstration

1. **Upload a text PDF.** PyPDF2 extracts text page by page. Image-only scans have no implemented
OCR path.

2. **Embed the whole text.** The application creates one all-MiniLM-L6-v2 embedding for the
complete document. Long text can be truncated by the model rather than becoming a rich chunk
index.

3. **Ask a question.** The query is embedded and dot-product scores rank in-memory document
vectors. There is no normalized-cosine calculation or relevance threshold.

4. **Inspect the answer and context.** The selected text and question are sent to Cohere. The UI
shows context, but no page-level citations or factual enforcement mechanism.

## Declared checks

These commands/checks describe the intended verification path. Their presence in this
guide does not claim that they passed. See the dated evidence below and the README for setup.

```text
python -m py_compile app.py
```

## Evidence levels

| Level | What it establishes | What it does not establish |
| --- | --- | --- |
| Source review | A path exists in tracked code | Successful runtime behavior |
| Syntax/build | Parser/compiler accepts that path | End-to-end correctness |
| Behavioral check | A specific input/output case passed | Generalization beyond cases |
| Domain evaluation | Performance on a stated target setting | Other users/data/environments |

## What to record

- Commit, environment, dependency versions and date.
- Input provenance and whether data is synthetic, public or privately supplied.
- Absolute pass/fail/skip counts; keep failed cases and their root causes.
- Whether external services, hardware or a production deployment were actually exercised.
- Expected output and an artifact showing the observation.

## Review scenarios

- **Whole-document retrieval:** The current data unit is the PDF text, not a page or paragraph
chunk.

- **Dot product is named accurately:** The operation in source is not normalized cosine similarity.

- **Context display is not verification:** Visible retrieved text helps inspection but cannot
guarantee grounded generation.

## Documentation inspection — 7 October 2026

The documentation was traced to committed source and checked for local links, balanced
code fences and supported implementation claims. Historical notebook outputs remain labeled
as historical. Live provider access, private databases and hardware behavior are not inferred
from configuration or dependency files. Any fresh run is recorded separately in the README.

## Next evidence to collect

- Verify the configured provider model/SDK together.
- Introduce tested chunking and citation attribution if expanding the project.
- Evaluate irrelevant questions, scans and long PDFs with known answers.
