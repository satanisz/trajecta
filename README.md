# TRAJECTA

**Trajectory-Aware Foundation Models for Dynamic Systems** — a research workspace combining a curated reading library with an educational continuous-time Markov chain (CTMC) baseline.

The project starts from the conversation “Pragma i Master Equation”. Its research direction connects event representations, temporal graphs, constrained transition rates and explicit dynamic propagation. The current implementation is a small, fully observed CTMC laboratory. Neural encoders, transfer learning, TTA/period folding and economic data integrations are proposed work, described in the architecture notes.

## Quick start

Requires **Python 3.10+**. The laboratory and scripts use the Python standard library; no package installation is needed when running from the repository root.

```powershell
python -m unittest discover -s tests -v
python -m experiments.synthetic_ctmc --seed 42
```

The experiment simulates training and held-out trajectories, estimates a generator by maximum likelihood and compares it with the true generator and a unit-rate baseline. It writes `outputs/synthetic_ctmc.json`, which Git ignores. Ten tests cover analytical solutions, probability mass, censoring, estimation, simulation and chronological period composition. See the [experiment notes](docs/experiments.md) for the measured example and its limits.

## Publication library

The [annotated bibliography](publications/BIBLIOGRAPHY.md) contains **49 distinct publications** from the source conversation. The local audit dated **2026-10-25** records **39 PDFs and two books as text HTML editions**. Eight full texts remain unavailable; the bibliography lists their sources and access limitations.

Publication files are excluded from Git. Cloning the repository gives you the catalog, descriptions and download scripts. To retrieve available copies:

```powershell
python scripts/download_publications.py
python scripts/download_web_books.py
```

The PDF script also supports `--list`, repeatable `--id` filters and optional `--system-client` for an installed `curl`. It reports inaccessible items in `local/download-report.json`; a successful script exit does not mean every publication was downloaded. HTML editions preserve text, with some images, styles and interactions still requiring internet access.

See [library instructions and provenance](publications/README.md) for versions, hashes, access statuses and corrections to source-chat references. After editing `publications/catalog.json`, regenerate its Markdown description with:

```powershell
python scripts/render_bibliography.py
```

## Research and learning

- [Proposed architecture](docs/architecture.md): state semantics, rate constraints, Master Equation, training objectives and the boundary between uniformization and TTA.
- [Experiments](docs/experiments.md): implemented baseline, observed results and staged evaluation plan.
- [Reading plan](docs/reading-plan.md): six learning stages with practical exercises.
- [Potential data sources](docs/data-sources.md): event logs, production networks and trade data; no connectors implemented yet.

Detailed research notes and bibliography descriptions are in Polish, matching the source discussion.

## Repository layout

```text
trajecta/                CTMC generator, simulation, estimation and propagation
experiments/             Reproducible synthetic example
tests/                   Numerical and statistical correctness checks
scripts/                 Publication downloads and bibliography rendering
publications/
  catalog.json           Metadata, source URLs and dated local audit
  BIBLIOGRAPHY.md         Generated descriptions of all 49 publications
  files/                 Ignored PDFs and HTML books, grouped by subject
docs/                    Architecture, experiments, learning and data notes
outputs/                 Ignored experiment results, created on demand
local/                   Ignored download reports and working files
data/                    Reserved, ignored local research datasets
```

## Scope and limitations

The solver uses dense matrices and row-vector probabilities, `dp/dt = p Q`. Uniformization reports truncation error separately; it does not implement the transmutation trajectory analysis method discussed in the source conversation. MLE assumes stationary rates and fully observed jump times. The synthetic example does not establish performance on real data, causal identification or cross-domain transfer.

No project-wide license has been selected yet. Individual publications retain their authors’ and publishers’ terms. The repository does not redistribute the downloaded texts.
