# Numerical results (paper tables / figures)

CSV files have a **header on row 1** (no `#` comment lines) so Google Sheets
File → Import can chart them directly.

| File | Paper element | Units | Notes |
|---|---|---|---|
| `frontier_3d_throughput.csv` | Table I (Frontier 3D) | TB/s | Blosc columns = application-level effective bandwidth (uncompressed bytes / I/O time) |
| `3D-perlmutter.csv` | Fig. 2 | GB/s + size | Perlmutter 3D: `EWS_GBps` / `TLS_GBps` (GB/s); `Size_GB` is per-step output size for the dashed line (TB = GB/1000). TLS at 512 nodes is 1723 GB/s ($\approx$1.7 TB/s). |
| `fig_btd_a_flatten_frontier.csv` | Fig. 3 | GB/s | Frontier: EWS vs EWS+FlattenSteps |
| `fig_btd_b_span_async_frontier.csv` | Fig. 4 | GB/s | Frontier: Default / SPAN / SPAN+AsyncWrite; starts at \(N{=}16\) |
| `fig_btd_c_agg_perlmutter.csv` | Fig. 5 | GB/s | Perlmutter, one subfile/rank. DSB = DataSizeBased; EWS = EveryoneWritesSerial; TLS = TwoLevelShm |
| `fig_btd_d_subfiles_perlmutter.csv` | Fig. 6 | GB/s | Perlmutter \(N{=}8\) (32 ranks); throughput vs number of subfiles |
| `repeat_runs_raw.csv` | Per-job repeated trials | seconds | already header-on-row-1 |
| `repeat_summary.csv` | mean±stdev IOTime by setting | seconds | already header-on-row-1 |

Repeated trials (×3): balanced 3D EWS/TLS/null @ \(N{=}8,16,32\); 3D HDF5 @ 8;
BTD SPAN / SPAN+Async / SPAN+Flatten (EWS+TLS) @ \(N{=}8,16,32\).
Larger \(N\) and Blosc remain single-trial in the paper.

Batch scripts for those repeats live under [`../repeat/`](../repeat/) (same inputs
and job pattern as `warpx_tests/PerformanceRun/`, just organized by config such
as `bp_async/`). **Run each script three times**; see `../repeat/README.md`.

## Log → CSV

Per-job **TotalTime** and **IOTime** come from
[`../scripts/frontier/extract_time_3.6.py`](../scripts/frontier/extract_time_3.6.py).
From the parent of the job data directory:

```bash
cd <parent>    # contains job_id/ (e.g. 5130062/)
python3 ../scripts/frontier/extract_time_3.6.py job_id   # bare id, no trailing /
```

See `../scripts/frontier/README.md`. Paper throughput uses Option‑1 timing where
applicable:
\(\mathrm{IOTime}_{\mathrm{Option1}} = \mathrm{TotalTime}_{\mathrm{I/O}} - \mathrm{TotalTime}_{\mathrm{nullcore}}\).
**DataSize** is the aggregate output **file size observed from each run**
(on-disk bytes written for that checkpoint/step; for Blosc columns the paper
uses the uncompressed application byte count as the effective-bandwidth
numerator — see paper §III-C). Times and sizes are aggregated into the CSVs below.

## Plotting (Google Sheets)

Paper figures were produced in **Google Sheets**, not from scripts in this repo:

1. Import the CSV for the target figure/table (File → Import, or paste).
2. Recreate the chart (scatter/line/column as in the paper).
3. Export the chart (e.g. PNG/PDF) for inclusion in the manuscript.

`frontier_3d_throughput.csv` was used for Table I.
Fig. 2 uses `3D-perlmutter.csv`. Figs. 3–6 use `fig_btd_*.csv` as listed above.
No matplotlib/gnuplot drivers are required to replot.
