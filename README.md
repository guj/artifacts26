# PDSW’26 Artifacts

Supporting materials for the paper:

> *Stress-Testing Exascale Scientific Data Output — ADIOS2 Configuration Strategies for WarpX under Extreme Load Imbalance*

This directory is the **single** reproducibility tree for the **Artifact Description (AD)**.
Do **not** create a separate AE tree yet — AE is optional after acceptance.

## Layout

```text
artifacts/
  README.md
  warpx_tests/              # copy of inputs + PerformanceRun scripts
  warpx_tests_INDEX.md      # paper ↔ directory map
  repeat/                   # same runs, organized for ×3 small-N repeats
  configs/                  # pointers into warpx_tests (no duplicate decks)
  scripts/frontier/         # bash.setup.env + build.setup (WORKDIR-based)
  results/                  # numerical results underlying tables/figures
  ad/                       # SC26 AD appendix (LaTeX)
```

**Test tree roles**

| Path | Contents |
|---|---|
| `warpx_tests/inputs_3d/` | All WarpX inputs (balanced 3D **and** BTD) |
| `warpx_tests/PerformanceRun/` | Frontier Slurm scripts (plus some Perlmutter) |
| `repeat/` | Same style of batch scripts, grouped by config (`bp`, `bp_async`, …); **submit each script 3×** for the paper’s small-N repeats — see `repeat/README.md` |
| `scripts/frontier/` | Module env + software build into `$WORKDIR` |
## Software versions (from paper §3)

| Component   | Version |
|------------|---------|
| WarpX      | 25.12   |
| ADIOS2     | 2.11    |
| openPMD-api| as bundled with the WarpX build |
| Engine     | BPFile / BP5 |

ADIOS2 features exercised: `TwoLevelShm`, `EveryoneWritesSerial`, `DataSizeBased`,
`FlattenSteps`, `SPAN`, Blosc2 (lossless), `AsyncWrite`.

## Platforms

- **Primary documented platform: Frontier (ORNL)** — Lustre/ClusterStor ORION; weak scaling up to 2048 nodes. Setup and job scripts in this tree target Frontier.
- **Perlmutter (NERSC)** — all-flash Lustre scratch; weak scaling up to 512 nodes. Uses the same WarpX → openPMD-api → ADIOS2 stack and job pattern; only site modules, account/QOS, and scratch paths differ. A full second script tree is not provided.

Absolute TB/s depends on shared-filesystem load and will differ across platforms and days. Reproducible claims emphasize **relative configuration rankings** and the measurement methodology in the paper.

## Frontier build (ready)

```bash
cd scripts/frontier
export WORKDIR=/lustre/orion/<project>/scratch/<user>/<exp>
source bash.setup.env
./build.setup
```

Personal scratch paths are removed; pass `WORKDIR` instead. See `scripts/frontier/README.md`.

## Run after build

```bash
cd warpx_tests
ln -sfn "$WORKDIR/binary/warpx/bin/<warpx-binary>" EXE
ln -sfn "$WORKDIR/binary/adios/bin/bpls" bpls
# edit #SBATCH -A YOUR_PROJECT in the script, then:
sbatch PerformanceRun/3D/N1/frontier_blosc.sh
# or
sbatch PerformanceRun/BTD/N8/frontier.sh
```

See `warpx_tests_INDEX.md` for which input dir each paper figure uses.

## Results CSVs

Filled under `results/` (Table 1 + Figs. BTD-a..d). See `results/README.md`.

- **Logs → times:** from the parent of `job_id/`, run `python3 scripts/frontier/extract_time_3.6.py job_id` (bare id, no `/`).
- **DataSize:** aggregate output file size observed from each run (on-disk).
- **Figures:** import CSVs into **Google Sheets** and export charts (no plotting scripts in this tree).

## Artifact repository

Primary link: https://github.com/guj/artifacts26  
(recorded as \(A_1\) in `ad/sc26_ad.tex`)

## What to drop in next

1. Push this `artifacts/` tree contents to that repo (if not already)
2. Compile AD: `cd ad && pdflatex sc26_ad.tex` and upload the PDF

## AD vs AE

| | AD | AE |
|---|---|---|
| Required? | Yes (by Aug 14 AoE final) | Optional |
| Lives in | `ad/` | Wait until acceptance |
| Content | Describe + link this tree | Step-by-step install/run/eval |

## License

MIT — see [`LICENSE`](LICENSE). Applies to this `artifacts/` tree (configs, scripts,
results, AD sources), not to the paper PDF or to WarpX/ADIOS2 themselves.
