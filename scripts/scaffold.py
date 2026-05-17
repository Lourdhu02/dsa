"""Generate per-problem boilerplate for a module from a manifest.

Each module that uses this generator has a ``_manifest.py`` next to its
``README.md`` containing:

    PROBLEMS = [
        {
            "slug": "01-two-sum",
            "title": "Two sum",
            "difficulty": "easy",
            "tags": ["hash-map"],
            "statement": "...",        # markdown body
            "signature": "def two_sum(...): ...",
            "examples_md": "...",      # markdown table
            "constraints": "...",
            "hint": "...",
            "starter": "...",          # body of solution.py
            "reference": "...",        # body of reference.py
            "tests": "...",            # body of tests/test_solution.py
        },
        ...
    ]

Usage:
    python scripts/scaffold.py 02-hashing
    python scripts/scaffold.py --all
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path
from textwrap import dedent

REPO_ROOT = Path(__file__).resolve().parent.parent

CONFTEST_BODY = dedent(
    """\
    import sys
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
    """
)

README_TEMPLATE = dedent(
    """\
    # {number}. {title}  `[{difficulty}]`

    {statement}

    ## Function signature

    ```python
    {signature}
    ```

    {examples_md}

    {constraints_section}

    ## Hint

    <details>
    <summary>Hint</summary>

    {hint}
    </details>
    """
)


def _load_manifest(module_dir: Path) -> list[dict]:
    manifest_path = module_dir / "_manifest.py"
    if not manifest_path.is_file():
        raise FileNotFoundError(f"No _manifest.py in {module_dir}")
    spec = importlib.util.spec_from_file_location(f"_manifest_{module_dir.name}", manifest_path)
    assert spec is not None and spec.loader is not None
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    if not hasattr(mod, "PROBLEMS"):
        raise AttributeError(f"{manifest_path} must define PROBLEMS")
    return mod.PROBLEMS  # type: ignore[attr-defined]


def _write(path: Path, content: str) -> bool:
    path.parent.mkdir(parents=True, exist_ok=True)
    existing = path.read_text(encoding="utf-8") if path.is_file() else None
    if existing == content:
        return False
    path.write_text(content, encoding="utf-8")
    return True


def scaffold_module(module_name: str) -> int:
    module_dir = REPO_ROOT / module_name
    problems = _load_manifest(module_dir)
    base = module_dir / "problems"
    written = 0
    for i, p in enumerate(problems, start=1):
        slug: str = p["slug"]
        title: str = p["title"]
        difficulty: str = p["difficulty"]
        tags: list[str] = p.get("tags", [])

        prob_dir = base / slug
        tests_dir = prob_dir / "tests"

        # index.json
        idx = {"title": title, "difficulty": difficulty, "tags": tags}
        if _write(prob_dir / "index.json", json.dumps(idx) + "\n"):
            written += 1

        # README.md
        constraints = p.get("constraints", "").strip()
        constraints_section = f"## Constraints\n\n{constraints}\n" if constraints else ""
        readme = README_TEMPLATE.format(
            number=f"{i:02d}",
            title=title,
            difficulty=difficulty,
            statement=p["statement"].strip(),
            signature=p["signature"].strip(),
            examples_md=p["examples_md"].strip(),
            constraints_section=constraints_section,
            hint=p["hint"].strip(),
        )
        if _write(prob_dir / "README.md", readme):
            written += 1

        # solution.py
        if _write(prob_dir / "solution.py", p["starter"].lstrip("\n").rstrip() + "\n"):
            written += 1

        # reference.py
        if _write(prob_dir / "reference.py", p["reference"].lstrip("\n").rstrip() + "\n"):
            written += 1

        # tests
        if _write(tests_dir / "conftest.py", CONFTEST_BODY):
            written += 1
        if _write(tests_dir / "test_solution.py", p["tests"].lstrip("\n").rstrip() + "\n"):
            written += 1
    print(f"{module_name}: wrote {written} files for {len(problems)} problems")
    return written


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("module", nargs="?")
    parser.add_argument("--all", action="store_true", help="scaffold every module that has a _manifest.py")
    args = parser.parse_args(argv)

    if args.all:
        names = sorted(p.parent.name for p in REPO_ROOT.glob("[0-9][0-9]-*/_manifest.py"))
    elif args.module:
        names = [args.module]
    else:
        parser.error("specify a module or --all")
        return 2

    for name in names:
        scaffold_module(name)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
