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
  - openPMD-api → `openPMD/openPMD-api` (default tag `0.16.1`)
  - WarpX → `BLAST-WarpX/warpx` (default tag `25.12`)
- Override tags: `ADIOS2_TAG=... OPENPMD_TAG=... WARPX_TAG=... ./build.setup`

## Layout created under `$WORKDIR`

```text
$WORKDIR/
  binary/{adios,openPMD-api,warpx}
  build/{adios,openPMD,warpx}
  src/{adios,openPMD,warpx}
```
