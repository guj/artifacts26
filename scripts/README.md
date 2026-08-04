# Analysis / job scripts

**Frontier is the primary documented platform.** Perlmutter is analogous (same
WarpX → openPMD-api → ADIOS2 flow). Example Perlmutter Slurm scripts are under
`warpx_tests/PerformanceRun/` (e.g. `BTD/N8/perlmutter.sh`); adapt modules,
account/QOS, and scratch paths as needed.

## Frontier build / env

See [`frontier/`](frontier/):

- `bash.setup.env` — Frontier modules + GPU flags; requires `WORKDIR`
- `build.setup` — builds ADIOS2, openPMD-api, WarpX into `$WORKDIR`

```bash
export WORKDIR=/lustre/orion/<project>/scratch/<user>/<exp>
source frontier/bash.setup.env
./frontier/build.setup
```

## Log → CSV path

Use [`frontier/extract_time_3.6.py`](frontier/extract_time_3.6.py) to pull
**TotalTime** and **IOTime** from WarpX job logs. `cd` to the parent of
`job_id/`, then `python3 frontier/extract_time_3.6.py job_id` (no trailing
slash). Details in `frontier/README.md`. Aggregate into `../results/*.csv`;
figures via Google Sheets (`../results/README.md`).
