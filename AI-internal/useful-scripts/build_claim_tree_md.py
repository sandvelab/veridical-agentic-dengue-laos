#!/usr/bin/env python3
"""Generate a Markdown mirror of the claim tree, for browsing on the repository host.

The HTML report (`build_hierarchical_report.py`) needs a browser and a checkout; a
repository host renders Markdown and Mermaid natively, with relative links between
files. So this writes, under `AI-generated/claim-tree/`:

- `README.md` — the overview: the reported conclusion, a Mermaid diagram of the whole
  tree (main path solid, paths not taken dashed), and a linked indented list of every
  node, because the host's Mermaid does not follow links.
- `analysis/**/README.md` — one page per node, laid out as **Claim:** and **Result:**,
  then the claims from the collection that rest on it, its children, and links into
  the node's real `results/`, `scripts/`, `provenance/` and `run.sh`. A folder's
  README is what the host shows when the folder is opened, so the tree is browsed by
  clicking down through folders.
- `claims.md` — the claim collection, each claim linked to its node and its grounds,
  with a Mermaid map of which node each claim rests on and which claims cite others.

Presentation only: it reads `claim.md` files and the claim collection through the
HTML builder's own parsing, so the two views cannot disagree about what a node says,
and it computes nothing. Generated — never hand-edit the output.

Dual interface:
    API:  build_tree_md(root=".", out="AI-generated/claim-tree") -> Path
    CLI:  python build_claim_tree_md.py [--root .] [--out DIR]
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_hierarchical_report as report  # noqa: E402  — the tree's parsing, shared
import claims as claim_collection  # noqa: E402

REGENERATE = ".venv/bin/python AI-internal/useful-scripts/build_claim_tree_md.py"
KEEP = {"provenance.md"}  # written by hand, appended to, never regenerated


def _commit(root: Path) -> str:
    try:
        return subprocess.run(["git", "-C", str(root), "rev-parse", "--short", "HEAD"],
                              capture_output=True, text=True).stdout.strip() or "not committed"
    except FileNotFoundError:
        return "git unavailable"


def _one_line(text: str, limit: int = 170) -> str:
    line = " ".join(text.split())
    return line if len(line) <= limit else line[:limit].rsplit(" ", 1)[0] + " …"


def _demote(text: str) -> str:
    """Headings inside an answer become level four, so they nest under the page's own."""
    return re.sub(r"^#{1,3} ", "#### ", text, flags=re.M)


def _link_claim_ids(text: str, to_claims: str) -> str:
    return re.sub(r"\bC(\d+)\b", lambda m: f"[C{m.group(1)}]({to_claims}#c{m.group(1)})", text)


def _grounds(c: dict, to_repo_root: str) -> str:
    out = []
    for t in c.get("grounds", "").split("·"):
        t = t.strip().strip("`")
        if t:
            out.append(f"[`{Path(t).name}`]({to_repo_root}{t})")
    return " · ".join(out)


class Tree:
    """The claim tree, read once: each node's info, whether it is on a path not taken."""

    def __init__(self, root: Path):
        self.root = root
        self.info: dict[str, dict] = {}
        self.not_taken: set[str] = set()
        self.order: list[str] = []
        self._walk(root / "analysis", inherited=False)

    def _walk(self, node: Path, inherited: bool) -> None:
        rel = node.relative_to(self.root).as_posix()
        info = report._read(node)
        self.info[rel] = info
        self.order.append(rel)
        if inherited:
            self.not_taken.add(rel)
        for c in info["children"]:
            off = info["kind"] == "alternatives" and c.name != info["main_path"]
            self._walk(c, inherited or off)

    def children(self, rel: str) -> list[str]:
        return [c.relative_to(self.root).as_posix() for c in self.info[rel]["children"]]


def _stamp(today: str, commit: str) -> str:
    return (f"> **A snapshot, generated {today} from the tree at commit `{commit}`.** "
            f"Everything here is derived from files the repository versions and regenerates "
            f"in seconds with `{REGENERATE}` (or `/hierarchical-report`). If the tree has "
            f"changed since that commit, rebuild rather than trust this copy; never hand-edit.")


def _node_page(tree: Tree, rel: str, out: Path, by_node: dict[str, list[dict]],
               stamp: str) -> None:
    info = tree.info[rel]
    depth = len(Path(rel).parts)
    to_mirror = "../" * depth
    to_repo = "../" * (depth + 2)
    to_claims = to_mirror + "claims.md"
    parts_ = Path(rel).parts

    trail = [f"[overview]({to_mirror}README.md)"]
    for i, name in enumerate(parts_[:-1]):
        trail.append(f"[{name}]({'../' * (len(parts_) - 1 - i)}README.md)")
    lines = [" / ".join(trail) + f" / **{parts_[-1]}**", "", f"# {parts_[-1]}", ""]
    if rel in tree.not_taken:
        lines += ["*On a path not taken — an alternative the reported analysis did not use. "
                  "It is complete and runnable, and the stability analysis ran it.*", ""]

    lines += [f"**Claim:** {info['claim']}", ""]
    answer = report.answers_text(info["answers"])
    lines += ["**Result:**", "", _demote(answer) if answer else "*No result recorded.*", ""]

    mine = by_node.get(rel, [])
    if mine:
        lines += ["## Claims resting on this node", ""]
        for c in mine:
            lines.append(f"- **[{c['id']}]({to_claims}#{c['id'].lower()})** — "
                         f"{_link_claim_ids(c['statement'], to_claims)}")
        lines.append("")

    kids = tree.children(rel)
    if kids:
        kind = info["kind"] or "?"
        head = "Alternatives" if kind == "alternatives" else "Sub-analyses"
        lines += [f"## {head}", ""]
        if kind == "alternatives":
            lines += ["Competing ways of answering this node's claim. The reported analysis "
                      "takes the **main path**; the others are run by `05_stability`.", ""]
        for k in kids:
            name = Path(k).name
            tag = ""
            if kind == "alternatives":
                tag = " — **main path**" if name == info["main_path"] else " — *not taken*"
            n = len(by_node.get(k, []))
            ntag = f" · {n} claim{'s' * (n != 1)}" if n else ""
            lines.append(f"- [{name}]({name}/README.md){tag}{ntag}  ")
            lines.append(f"  {_one_line(tree.info[k]['claim'])}")
        lines.append("")

    node = tree.root / rel
    material = [f"[`claim.md`]({to_repo}{rel}/claim.md)"]
    for sub in ("results", "scripts", "provenance"):
        if report._files(node / sub, tree.root):
            material.append(f"[`{sub}/`]({to_repo}{rel}/{sub})")
    if (node / "results" / "main").is_dir():
        material.append(f"[`results/main/`]({to_repo}{rel}/results/main)")
    if (node / "run.sh").exists():
        material.append(f"[`run.sh`]({to_repo}{rel}/run.sh)")
    lines += ["## Material", "", "The node's own files: " + " · ".join(material) + ".", "",
              "---", "", stamp, ""]

    page = out / rel / "README.md"
    page.parent.mkdir(parents=True, exist_ok=True)
    page.write_text("\n".join(lines))


def _headline(root: Path) -> list[str]:
    p = root / "analysis" / "results" / "main" / "conclusion.json"
    if not p.is_file():
        return []
    c = json.loads(p.read_text())
    h = root / "analysis" / "results" / "main__holdout" / "conclusion.json"
    ho = json.loads(h.read_text()) if h.is_file() else None
    n = report._num
    text = (f"**{c.get('our_model')}**, skill score {n(c.get('skill_score'), 4)} against the "
            f"reference model on the development backtest"
            + (f", {n(ho.get('skill_score'), 4)} on the held-out year" if ho else "")
            + f". Mean CRPS {n(c.get('crps_ours'))} against {n(c.get('crps_reference'))}"
            + (f", and {n(ho.get('crps_ours'))} against {n(ho.get('crps_reference'))} on the "
               f"holdout" if ho else "") + ".")
    return ["## The reported conclusion", "", text, "",
            "It is one member of a distribution over the whole perturbation set — see "
            "[05_stability](analysis/05_stability/README.md) and the claims that rest on it.", ""]


def _mermaid_tree(tree: Tree, by_node: dict[str, list[dict]]) -> list[str]:
    ids = {rel: f"n{i}" for i, rel in enumerate(tree.order)}
    lines = ["```mermaid", "flowchart LR"]
    for rel in tree.order:
        n = len(by_node.get(rel, []))
        label = Path(rel).name + (f"<br/><i>{n} claim{'s' * (n != 1)}</i>" if n else "")
        lines.append(f'  {ids[rel]}["{label}"]')
    for rel in tree.order:
        for k in tree.children(rel):
            arrow = "-.->" if k in tree.not_taken and rel not in tree.not_taken else "-->"
            lines.append(f"  {ids[rel]} {arrow} {ids[k]}")
    lines.append("  classDef notTaken stroke-dasharray:5 4,color:#888,stroke:#999")
    lines.append("  classDef claims stroke-width:2.5px")
    taken_with_claims = [ids[r] for r in tree.order if by_node.get(r) and r not in tree.not_taken]
    if tree.not_taken:
        lines.append("  class " + ",".join(ids[r] for r in tree.order if r in tree.not_taken)
                     + " notTaken")
    if taken_with_claims:
        lines.append("  class " + ",".join(taken_with_claims) + " claims")
    lines.append("```")
    return lines


def _tree_list(tree: Tree, by_node: dict[str, list[dict]]) -> list[str]:
    lines = []
    for rel in tree.order:
        depth = len(Path(rel).parts) - 1
        parent = str(Path(rel).parent)
        tag = ""
        if parent in tree.info and tree.info[parent]["kind"] == "alternatives":
            tag = (" — **main path**" if Path(rel).name == tree.info[parent]["main_path"]
                   else " — *not taken*")
        cl = by_node.get(rel, [])
        ctag = (" · " + ", ".join(f"[{c['id']}](claims.md#{c['id'].lower()})" for c in cl)
                if cl else "")
        lines.append(f"{'  ' * depth}- [{Path(rel).name}]({rel}/README.md){tag}{ctag}  ")
        lines.append(f"{'  ' * depth}  {_one_line(tree.info[rel]['claim'], 140)}")
    return lines


def _claims_page(tree: Tree, all_claims: list[dict], by_node: dict[str, list[dict]],
                 stamp: str) -> list[str]:
    node_ids = {rel: f"s{i}" for i, rel in enumerate(r for r in tree.order if r in by_node)}
    known = {c["id"] for c in all_claims}
    lines = ["[overview](README.md) / **claims**", "", "# The claim collection", "",
             stamp, "",
             f"Every statement the analysis supports — {len(all_claims)} of them — each bound "
             "to the node it rests on and the result files grounding it. Generated from "
             "[`Human-AI-collaboration/claims/claims.md`](../../Human-AI-collaboration/claims/claims.md), "
             "the collection the manuscript is written from.", "",
             "## Map", "",
             "Each box is a node of the tree, holding the claims that rest on it. A dotted "
             "arrow is one claim citing another.", "",
             "```mermaid", "flowchart LR"]
    for rel, sid in node_ids.items():
        short = rel.removeprefix("analysis/") if rel != "analysis" else "analysis (root)"
        lines.append(f'  subgraph {sid}["{short}"]')
        lines.append("    direction TB")
        for c in by_node[rel]:
            lines.append(f"    {c['id']}")
        lines.append("  end")
    for c in all_claims:
        text = " ".join(str(c.get(k, "")) for k in ("statement", "scope", "alternatives"))
        for ref in sorted(set(re.findall(r"\bC\d+\b", text)) - {c["id"]},
                          key=lambda x: int(x[1:])):
            if ref in known:
                lines.append(f"  {c['id']} -.-> {ref}")
    lines += ["```", "", "## By node", "", "| Node | Claims |", "|---|---|"]
    for rel in node_ids:
        ids = ", ".join(f"[{c['id']}](#{c['id'].lower()})" for c in by_node[rel])
        lines.append(f"| [`{rel}`]({rel}/README.md) | {ids} |")
    lines.append("")
    for c in all_claims:
        rel = c.get("node", "")
        node_link = f"[`{rel}`]({rel}/README.md)" if rel in tree.info else f"`{rel or '-'}`"
        lines += [f"## {c['id']}", "", _link_claim_ids(c["statement"], ""), ""]
        lines.append(f"- **Node:** {node_link}")
        g = _grounds(c, "../../")
        if g:
            lines.append(f"- **Grounds:** {g}")
        for key, label in (("scope", "Scope"), ("alternatives", "Alternatives")):
            if c.get(key):
                lines.append(f"- **{label}:** {_link_claim_ids(c[key], '')}")
        if c.get("by"):
            lines.append(f"- **By:** {c['by']}")
        lines.append("")
    return lines


def build_tree_md(root: str | Path = ".", out: str | Path = "AI-generated/claim-tree") -> Path:
    root = Path(root).resolve()
    if not (root / "analysis" / "claim.md").exists():
        raise SystemExit(f"no claim tree at {root / 'analysis'}")
    out = root / out
    out.mkdir(parents=True, exist_ok=True)
    # Wholly generated apart from KEEP, so clear it: a node that was removed or renamed
    # must not leave a page behind that the overview no longer links.
    for p in out.iterdir():
        if p.name in KEEP:
            continue
        shutil.rmtree(p) if p.is_dir() else p.unlink()

    report._IGNORED.clear()
    report._IGNORED.update(report._load_ignored(root))
    tree = Tree(root)
    all_claims = claim_collection.load(root)
    by_node: dict[str, list[dict]] = {}
    for c in all_claims:
        by_node.setdefault(c.get("node", ""), []).append(c)

    today, commit = date.today().isoformat(), _commit(root)
    stamp = _stamp(today, commit)
    for rel in tree.order:
        _node_page(tree, rel, out, by_node, stamp)
    (out / "claims.md").write_text("\n".join(_claims_page(tree, all_claims, by_node, stamp)))

    n_alt = sum(1 for r in tree.order if tree.info[r]["kind"] == "alternatives")
    index = out / "README.md"
    index.write_text("\n".join([
        "# The claim tree", "", stamp, "",
        "The analysis is a tree of questions. Each node states a **claim** — what it sets out "
        "to establish — and the **result** it found, and each child answers part of its "
        f"parent. {len(tree.order)} nodes; {n_alt} of them are forks between alternatives, "
        "where the reported analysis takes the main path and the paths not taken stay in the "
        f"tree, complete and runnable. {len(all_claims)} claims in the "
        "[claim collection](claims.md) rest on the nodes.", "",
        "**Ways in:** click down from [the root node](analysis/README.md), start from a "
        "claim in [the claim collection](claims.md), or use the list below. To descend a "
        "reported number to the per-cell scores it averages, build the HTML report "
        "(`/hierarchical-report`) and open `AI-generated/hierarchical-report/index.html`.", "",
        *_headline(root),
        "## The tree", "",
        "Solid arrows are the path the reported analysis takes; dashed boxes are paths not "
        "taken. Bold boxes carry claims. The diagram is not clickable — the list below is.", "",
        *_mermaid_tree(tree, by_node), "",
        "## Every node", "",
        *_tree_list(tree, by_node), "",
    ]))
    return index


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--root", default=".")
    ap.add_argument("--out", default="AI-generated/claim-tree")
    a = ap.parse_args(argv)
    print(f"wrote {build_tree_md(a.root, a.out)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
