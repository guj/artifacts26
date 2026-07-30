# warpx_tests

WarpX I/O benchmark inputs and Slurm scripts used for the PDSW’26 study
(Frontier primary; some Perlmutter scripts included).

## Layout

```text
warpx_tests/
  EXE                 # you create: symlink to WarpX binary
  bpls                # you create: symlink to ADIOS2 bpls
  inputs_3d/          # all input decks (balanced 3D + BTD)
  PerformanceRun/     # job scripts
    3D/               # balanced Cartesian
    BTD/              # boosted-frame back-transformed diagnostics
    SST_BTD/          # exploratory staging (optional)
```

See `../warpx_tests_INDEX.md` for a paper↔directory map.

## One-time setup after building software

```bash
export WORKDIR=/lustre/orion/<project>/scratch/<user>/<exp>
# build with artifacts/scripts/frontier/{bash.setup.env,build.setup}

cd /path/to/warpx_tests
ln -sfn "$WORKDIR/binary/warpx/bin/warpx.3d.MPI.HIP.DP.OPMD.FFT" EXE   # adjust binary name
ln -sfn "$WORKDIR/binary/adios/bin/bpls" bpls
ls -l EXE bpls inputs_3d
```

## Run (Frontier example)

1. Edit `#SBATCH -A YOUR_PROJECT` in the script you will submit.
2. From a `PerformanceRun/...` directory:

```bash
sbatch frontier.sh          # or frontier_blosc.sh, etc.
```

Inputs are picked up via relative paths into `inputs_3d/opmd/...`.
