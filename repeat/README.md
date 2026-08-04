# Three-trial repeat scripts

Slurm scripts used for the paper’s small-scale **×3 repeats**
(`results/repeat_runs_raw.csv`, `results/repeat_summary.csv`).

These are **not** a different experiment stack: they use the same WarpX inputs
and the same batch pattern as `warpx_tests/PerformanceRun/`. They are only
**reorganized** under one tree by configuration (e.g. `bp/`, `bp_async/`,
`bp_flatten/`, `h5/`) so the repeat campaign is easy to re-run.

## How to reproduce the repeats

1. In `warpx_tests/`, symlink `EXE` and `bpls` as in the top-level README
   (scripts under `repeat/` resolve to `../warpx_tests/{EXE,bpls,inputs_3d}`).
2. Replace `#SBATCH -A YOUR_PROJECT` with your OLCF allocation in each script.
3. From the appropriate subdirectory, submit **each script three times**:

```bash
sbatch bp.frontier.sh
sbatch bp.frontier.sh
sbatch bp.frontier.sh
```

4. Extract times with `scripts/frontier/extract_time_3.6.py` (parent of each
   `job_id/` directory; bare job id, no trailing `/`).

## Layout

```text
repeat/
  3D/
    N8/8.sh          # balanced 3D BP (EWS/TLS/null as configured in script)
    N8/h5.8.sh       # balanced 3D HDF5 @ 8 nodes
    N16/16.sh
    N32/32.sh
  BTD/
    N8|N16|N32/
      bp/            # SPAN baseline
      bp_async/      # SPAN + AsyncWrite
      bp_flatten/    # SPAN + FlattenSteps
    N8/h5/           # BTD HDF5 @ 8 nodes
  repeat.tar         # archive of the same scripts (+ this README)
```

Relative paths (same pattern as `PerformanceRun/`, with an extra `../` out of
`repeat/`):

| Script location | `EXE` / `bpls` / `inputs_3d` |
|---|---|
| `3D/N*/…` | `../../../warpx_tests/…` |
| `BTD/N*/<config>/…` | `../../../../warpx_tests/…` |