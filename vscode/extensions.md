# Recommended VS Code Extensions

Each extension listed here earns its slot — one sentence on why.

## Required

| Extension | ID | Why |
|---|---|---|
| Python | `ms-python.python` | Language server, debugger, env discovery — required to run anything. |
| Pylance | `ms-python.vscode-pylance` | Fast type-aware IntelliSense; catches misuse of stdlib data structures before you run. |
| Python Test Explorer for VS Code | `ms-python.pytest` (bundled with Python ext) | One-click run / debug for individual tests next to the gutter — the red/green loop the course is built around. |
| Jupyter | `ms-toolsai.jupyter` | Needed to open the notebooks in modules 00, 06, 09, 12, and 14. |

## Strongly recommended

| Extension | ID | Why |
|---|---|---|
| Ruff | `charliermarsh.ruff` | Fast linter + import sorter; catches dead code and unused imports while you type. |
| Black Formatter | `ms-python.black-formatter` | Idiomatic Python formatting on save — keeps your solutions readable when you diff against `reference.py`. |
| Markdown All in One | `yzhang.markdown-all-in-one` | TOC, link checking, list editing — useful when you write your own notes in module READMEs. |
| Markdown Preview Mermaid Support | `bierner.markdown-mermaid` | Renders the Mermaid diagrams from the lesson READMEs inside VS Code (GitHub already renders them natively). |
| GitLens | `eamodio.gitlens` | Inline blame and history when you revisit your old solutions. |

## Optional

| Extension | ID | Why |
|---|---|---|
| Error Lens | `usernamehw.errorlens` | Inlines linter / type errors next to the code — faster feedback loop. |
| Python Indent | `KevinRose.vsc-python-indent` | Smart indent for multi-line expressions; small quality-of-life win. |
| Path Intellisense | `christian-kohler.path-intellisense` | Autocomplete file paths — handy in this repo's deep folder structure. |

## Install all required + recommended at once (PowerShell)

```powershell
$ids = @(
  "ms-python.python",
  "ms-python.vscode-pylance",
  "ms-toolsai.jupyter",
  "charliermarsh.ruff",
  "ms-python.black-formatter",
  "yzhang.markdown-all-in-one",
  "bierner.markdown-mermaid",
  "eamodio.gitlens"
)
$ids | ForEach-Object { code --install-extension $_ }
```
