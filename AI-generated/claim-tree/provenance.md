# Provenance — the Markdown claim tree

The append-only record of each build. Everything else in this folder is generated and is
rebuilt by the command below; this file is not, and is never overwritten.

## The first build — 2026-09-27, row 35

```
result:              AI-generated/claim-tree/   (README.md, claims.md, and one README.md per
                     node under analysis/ -- 71 nodes, 48 claims)
script:              AI-internal/useful-scripts/build_claim_tree_md.py
                     sha256:99453c64bf842df2209da3c58dde6b125924181f88a9b83f6ce8ae240ab034ff
                     imports AI-internal/useful-scripts/build_hierarchical_report.py
                     sha256:769304b52ba8b55e2fe45e4481a9077d07369b0cddf301eb7d56b0cd6f55303f
                     and AI-internal/useful-scripts/claims.py
                     sha256:f9c2951668c503c726ead0dabf626cf1a56875554ea62c3dc78516c7e4330ab3
invocation:          .venv/bin/python AI-internal/useful-scripts/build_claim_tree_md.py
inputs:              analysis/**/claim.md, and Human-AI-collaboration/claims/claims.md
commit:              3d89200
produced:            2026-09-27
node:                not a node -- a view over the tree, like the HTML report
```

A presentation of the tree for reading on GitHub, which renders Markdown and Mermaid but
shows HTML as source. It reads the tree through the HTML builder's own parsing and computes
nothing. Both Mermaid diagrams were rendered with mermaid-cli before committing to confirm
that they parse.
