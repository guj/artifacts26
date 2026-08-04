# AD appendix (SC26 format, AD only)

Fill/update `sc26_ad.tex`, especially the **TODO** artifact URL/DOI.

Compile (either engine works):

```bash
cd artifacts/ad
tectonic sc26_ad.tex    # lightweight; installed via: brew install tectonic
# or: pdflatex sc26_ad.tex
```

Output: `sc26_ad.pdf`

Vendored for offline build: `IEEEtran.cls`, `sc26repro.sty`, local `tagging.sty` stub.

Do **not** add an AE section until after acceptance (optional badges).
