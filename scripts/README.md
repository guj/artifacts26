# Analysis / job scripts

**Frontier is the primary documented platform.** Perlmutter is analogous (same
WarpX → openPMD-api → ADIOS2 flow); only modules, account/QOS, and scratch paths
differ — no separate Perlmutter script tree is required.

## Frontier build / env

See [`frontier/`](frontier/):

- `bash.setup.env` — Frontier modules + GPU flags; requires `WORKDIR`
- `build.setup` — builds ADIOS2, openPMD-api, WarpX into `$WORKDIR`

```bash
export WORKDIR=/lustre/orion/<project>/scratch/<user>/<exp>
source frontier/bash.setup.env
./frontier/build.setup
```

## Still TODO

- `parse_warpx_timers.py` — extract I/O and nullcore wall times → CSV
- `make_table1.py` — regenerate Frontier 3D throughput table
- `plot_btd_*.py` — regenerate BTD figures
- `submit_frontier.sh` — sanitized Frontier job template

Keep a small “smoke” path (1–8 nodes) documented in comments.
