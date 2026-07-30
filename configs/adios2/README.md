# ADIOS2 / openPMD options

In this study, ADIOS2 engine parameters are typically set via WarpX/openPMD
input options inside the decks under:

```text
warpx_tests/inputs_3d/opmd/
  regular/           # balanced
  regular_blosc/     # Blosc2
  btd_*/             # BTD + FlattenSteps variants
```

If you extract standalone ADIOS2 XML snippets later, place them here.
