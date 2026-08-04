# Map: paper experiments → `warpx_tests/`

`artifacts/warpx_tests/` is a full copy of the benchmark inputs and PerformanceRun scripts.

Expected layout at `warpx_tests/` root (see README there):

```text
warpx_tests/
  EXE          -> symlink to WarpX binary from $WORKDIR/binary/warpx/...
  bpls         -> symlink to ADIOS2 bpls
  inputs_3d/   # all WarpX input decks (3D + BTD)
  PerformanceRun/  # Slurm scripts (Frontier primary; some Perlmutter)
```

## Inputs (`inputs_3d/`)

| Directory | Role in paper |
|---|---|
| `opmd/regular/` | Balanced 3D Cartesian (ADIOS2/openPMD) |
| `opmd/regular_blosc/` | Balanced 3D + Blosc2 |
| `opmd/regular_h5/` | HDF5 comparison (small-scale) |
| `opmd/btd_default/`, `btd_joined/` | BTD baseline / joined writes |
| `opmd/btd_flatten/`, `btd_flatten_joined/` | BTD + FlattenSteps |
| `opmd/btd_*_sst/`, `PerformanceRun/SST_BTD/` | Exploratory staging (RDMA / SST); not primary figures |
| `opmdx8/` | Variants with different openPMD/ADIOS settings |
| `plot/`, `plot/btd/` | Plotting-oriented decks |
| `frontier_bb/` | Burst-buffer exploratory runs |

Per-node-count decks follow `input.n${NNODES}` (and `f`/`g` suffixes where used).

## Run scripts (`PerformanceRun/`)

| Path | Role |
|---|---|
| `3D/N1/frontier_blosc.sh`, `3D/N1/1.sh` | Frontier balanced smoke / Blosc |
| `3D/N8/*.sh` | Frontier balanced N=8 |
| `3D/scripts/` | Timer helpers (`writeToFindTime.sh`, …) |
| `BTD/N8/frontier.sh` | Frontier BTD (primary) |
| `BTD/N8/perlmutter.sh` | Example Perlmutter BTD script (adapt for other scales) |
| `BTD/N8/N8/bp/`, `.../h5/` | BP vs HDF5 BTD checks |
| `SST_BTD/` | Staging alternatives (secondary) |

Scripts resolve inputs relatively, e.g.:

```bash
INPUTS=${pwd}/../../../inputs_3d/opmd/regular_blosc/input.n${SLURM_NNODES}
```

Replace `#SBATCH -A YOUR_PROJECT` with your OLCF/NERSC allocation before submitting.

## Three-trial repeats (`../repeat/`)

For the small-\(N\) ×3 campaign summarized in `results/repeat_*.csv`, use the
scripts under [`../repeat/`](../repeat/) (e.g. `BTD/N8/bp_async/`). These are the
same class of runs as `PerformanceRun/`, regrouped by config; submit **each
script three times**. Details: `../repeat/README.md`.
