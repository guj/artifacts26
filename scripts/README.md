# Analysis / job scripts

**Frontier is the primary documented platform.** Perlmutter uses the same
WarpX → openPMD-api → ADIOS2 flow with a CUDA build.

## Frontier build / env

See [`frontier/`](frontier/):

- `bash.setup.env` — Frontier modules + GPU flags; requires `WORKDIR`
- `build.setup` — builds ADIOS2 and WarpX (bundled openPMD-api) into `$WORKDIR`

```bash
export WORKDIR=/lustre/orion/<project>/scratch/<user>/<exp>
source frontier/bash.setup.env
./frontier/build.setup
```

## Perlmutter build

See [`perlmutter/`](perlmutter/): `build.setup` loads NERSC GPU modules and
builds the same tags with `WarpX_COMPUTE=CUDA`.

```bash
export WORKDIR=/pscratch/sd/<user>/<exp>
./perlmutter/build.setup
```

Example Slurm: `warpx_tests/PerformanceRun/BTD/N8/perlmutter.sh`.

## Log → CSV path

Use [`frontier/extract_time_3.6.py`](frontier/extract_time_3.6.py) to pull
**TotalTime** and **IOTime** from WarpX job logs (both sites). `cd` to the parent of
`job_id/`, then `python3 frontier/extract_time_3.6.py job_id` (no trailing
slash). Details in `frontier/README.md`. Aggregate into `../results/*.csv`;
figures via Google Sheets (`../results/README.md`).
