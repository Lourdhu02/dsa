"""Practice CLI: pick the next unsolved problem, mark problems done, run all tests.

Usage:
    python -m common.practice list                 # show every problem with status
    python -m common.practice next                 # print the next unsolved problem
    python -m common.practice next --module 03     # next unsolved in module 03
    python -m common.practice done 03-linked-lists/04-reverse-list
    python -m common.practice undone 03-linked-lists/04-reverse-list
    python -m common.practice sync                 # re-run pytest and tick passing problems
    python -m common.practice stats                # per-module pass/total counts

Status is stored in ``.practice_status.json`` at the repo root.  Each problem
folder owns an ``index.json`` describing its difficulty and tags.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Iterable

REPO_ROOT = Path(__file__).resolve().parent.parent
STATUS_FILE = REPO_ROOT / ".practice_status.json"


@dataclass
class Problem:
    module: str       # e.g. "03-linked-lists"
    slug: str         # e.g. "04-reverse-list"
    title: str
    difficulty: str   # "easy" | "medium" | "hard"
    tags: list[str]

    @property
    def key(self) -> str:
        return f"{self.module}/{self.slug}"

    @property
    def path(self) -> Path:
        return REPO_ROOT / self.module / "problems" / self.slug


def discover() -> list[Problem]:
    """Walk every ``NN-module/problems/NN-slug/index.json`` and load problems.

    Time:  O(P) where P is the number of problem folders.
    Space: O(P) for the returned list.
    """
    problems: list[Problem] = []
    for module_dir in sorted(REPO_ROOT.glob("[0-9][0-9]-*")):
        problems_dir = module_dir / "problems"
        if not problems_dir.is_dir():
            continue
        for slug_dir in sorted(problems_dir.iterdir()):
            idx = slug_dir / "index.json"
            if not idx.is_file():
                continue
            meta = json.loads(idx.read_text(encoding="utf-8"))
            problems.append(
                Problem(
                    module=module_dir.name,
                    slug=slug_dir.name,
                    title=meta.get("title", slug_dir.name),
                    difficulty=meta.get("difficulty", "medium"),
                    tags=meta.get("tags", []),
                )
            )
    return problems


def load_status() -> dict[str, bool]:
    if not STATUS_FILE.exists():
        return {}
    try:
        return json.loads(STATUS_FILE.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return {}


def save_status(status: dict[str, bool]) -> None:
    STATUS_FILE.write_text(json.dumps(status, indent=2, sort_keys=True), encoding="utf-8")


def cmd_list(args: argparse.Namespace) -> int:
    problems = discover()
    status = load_status()
    for p in problems:
        if args.module and not p.module.startswith(args.module):
            continue
        mark = "X" if status.get(p.key) else " "
        print(f"  [{mark}] {p.difficulty[0].upper()}  {p.key:55s}  {p.title}")
    return 0


def cmd_next(args: argparse.Namespace) -> int:
    problems = discover()
    status = load_status()
    for p in problems:
        if args.module and not p.module.startswith(args.module):
            continue
        if args.difficulty and p.difficulty != args.difficulty:
            continue
        if not status.get(p.key):
            print(f"Next up: {p.key}")
            print(f"         {p.title}  [{p.difficulty}]")
            print(f"         {p.path}")
            print(f"         pytest {p.path.relative_to(REPO_ROOT).as_posix()}/tests -q")
            return 0
    print("All problems done. Nice.")
    return 0


def cmd_done(args: argparse.Namespace) -> int:
    status = load_status()
    status[args.problem] = True
    save_status(status)
    print(f"Marked {args.problem} as done.")
    return 0


def cmd_undone(args: argparse.Namespace) -> int:
    status = load_status()
    status.pop(args.problem, None)
    save_status(status)
    print(f"Marked {args.problem} as undone.")
    return 0


def cmd_sync(args: argparse.Namespace) -> int:
    """Run pytest per problem and flip status based on pass/fail.

    Slow but honest.  Use ``--module`` to limit scope.
    """
    problems = discover()
    status = load_status()
    changed = 0
    for p in problems:
        if args.module and not p.module.startswith(args.module):
            continue
        tests = p.path / "tests"
        if not tests.is_dir():
            continue
        rel = tests.relative_to(REPO_ROOT).as_posix()
        result = subprocess.run(
            [sys.executable, "-m", "pytest", rel, "-q", "--no-header"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        passed = result.returncode == 0
        prev = status.get(p.key, False)
        if passed != prev:
            status[p.key] = passed
            changed += 1
            print(f"  {'PASS' if passed else 'FAIL'}  {p.key}")
    save_status(status)
    print(f"\n{changed} status change(s).")
    return 0


def cmd_stats(args: argparse.Namespace) -> int:
    problems = discover()
    status = load_status()
    by_module: dict[str, list[Problem]] = {}
    for p in problems:
        by_module.setdefault(p.module, []).append(p)
    print(f"\n{'module':45s}  done / total")
    print("-" * 70)
    total_done = 0
    for mod in sorted(by_module):
        items = by_module[mod]
        done = sum(1 for p in items if status.get(p.key))
        total_done += done
        print(f"{mod:45s}  {done:>4d} / {len(items):<4d}")
    print("-" * 70)
    print(f"{'TOTAL':45s}  {total_done:>4d} / {len(problems):<4d}")
    return 0


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="practice")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_list = sub.add_parser("list", help="show every problem with status")
    p_list.add_argument("--module", help="restrict to module prefix, e.g. 03")
    p_list.set_defaults(func=cmd_list)

    p_next = sub.add_parser("next", help="print next unsolved problem")
    p_next.add_argument("--module", help="restrict to module prefix")
    p_next.add_argument("--difficulty", choices=("easy", "medium", "hard"))
    p_next.set_defaults(func=cmd_next)

    p_done = sub.add_parser("done", help="mark a problem solved")
    p_done.add_argument("problem", help="e.g. 03-linked-lists/04-reverse-list")
    p_done.set_defaults(func=cmd_done)

    p_undone = sub.add_parser("undone", help="mark a problem unsolved")
    p_undone.add_argument("problem", help="e.g. 03-linked-lists/04-reverse-list")
    p_undone.set_defaults(func=cmd_undone)

    p_sync = sub.add_parser("sync", help="run tests and update status from pass/fail")
    p_sync.add_argument("--module", help="restrict to module prefix")
    p_sync.set_defaults(func=cmd_sync)

    p_stats = sub.add_parser("stats", help="per-module pass / total")
    p_stats.set_defaults(func=cmd_stats)

    args = parser.parse_args(list(argv) if argv is not None else None)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
