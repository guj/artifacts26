# Frontier setup scripts

Primary documented platform for this artifact (Perlmutter is analogous).

## Quick start

```bash
export WORKDIR=/lustre/orion/<project>/scratch/<user>/<exp-dir>
source bash.setup.env          # or: source bash.setup.env "$WORKDIR"
./build.setup                 # or: ./build.setup "$WORKDIR"
```

After a successful build, re-source `bash.setup.env` in new shells before running WarpX.

## What was cleaned

- Removed personal scratch paths (`/lustre/orion/.../junmin/...`).
- `WORKDIR` is required (env var or first argument).
- Clones use **upstream** repos (not personal forks):
  - ADIOS2 → `ornladios/ADIOS2` (default tag `v2.11.0`)
  - WarpX → `BLAST-WarpX/warpx` (default tag `25.12`), with **bundled**
    openPMD-api (`WarpX_openpmd_internal=ON`) as in the paper
- Override tags: `ADIOS2_TAG=... WARPX_TAG=... ./build.setup`
- To build ADIOS2 with Blosc (Table I), add `-DADIOS2_USE_Blosc2=ON` to the
  ADIOS2 `cmake` line in `build.setup` (needs a c-blosc2 install).

## Layout created under `$WORKDIR`

```text
$WORKDIR/
  binary/{adios,warpx}
  build/{adios,warpx}
  src/{adios,warpx}
```

## Log → times (`extract_time_3.6.py`)

After a Slurm job finishes, extract **TotalTime** (wall) and **IOTime** (largest
`WriteToFile` “to” time in the WarpX timer dump) from job logs.

Go to the **parent** directory that contains the data folder named after the
job id (e.g. `5130062/`), then run with the bare job id (**no trailing slash**):

```bash
cd /path/to/parent          # contains job_id/ as a subdirectory
python3 /path/to/artifacts/scripts/frontier/extract_time_3.6.py job_id
# example:
#   cd .../runs
#   python3 extract_time_3.6.py 5130062
```

Optional: `python3 extract_time_3.6.py job_id --root /path/to/parent` if you
are not already in that parent directory.

Expects layout `<parent>/<job_id>/<encoding>_<job_id>_<type>_<numNodes>n/outs/output.*`.
Prints a table: `jobid`, `type`, `BPEngine_Agg`, `numNodes`, `TotalTime`, `IOTime`.

Paper Option‑1 I/O time is then `TotalTime(I/O run) − TotalTime(nullcore)` when
nullcore jobs are available; `IOTime` is the isolated WriteToFile cross-check.
**DataSize** for throughput is the aggregate **file size observed from each
run** (on-disk output for that step). Combine times + observed sizes into the
CSVs under `../../results/` for Google Sheets plots.
