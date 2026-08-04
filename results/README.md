# Numerical results (paper tables / figures)

| File | Paper element | Units |
|---|---|---|
| `frontier_3d_throughput.csv` | Table 1 (Frontier 3D) | TB/s (Blosc = effective) |
| `fig_btd_a_flatten_frontier.csv` | Fig. BTD-a | GB/s |
| `fig_btd_b_span_async_frontier.csv` | Fig. BTD-b | GB/s |
| `fig_btd_c_agg_perlmutter.csv` | Fig. BTD-c | GB/s |
| `fig_btd_d_subfiles_perlmutter.csv` | Fig. BTD-d | GB/s |
| `repeat_runs_raw.csv` | Per-job repeated trials (from `repeat.pdf`) | seconds |
| `repeat_summary.csv` | mean±stdev IOTime by setting | seconds |

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
numerator — see paper §3). Times and sizes are aggregated into the CSVs below.

## Plotting (Google Sheets)

Paper figures were produced in **Google Sheets**, not from scripts in this repo:

1. Import the CSV for the target figure/table (File → Import, or paste).
2. Recreate the chart (scatter/line/column as in the paper).
3. Export the chart (e.g. PNG/PDF) for inclusion in the manuscript.

`frontier_3d_throughput.csv` was used for Table 1 (and any matching 3D throughput chart).
BTD figures use `fig_btd_*.csv` as listed above. No matplotlib/gnuplot drivers are required to replot.
