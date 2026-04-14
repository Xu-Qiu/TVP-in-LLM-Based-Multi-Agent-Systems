# Contributing

## Requirements
- Python 3.9+
- No external dependencies are required for build/validate scripts.

## Quick Start
```bash
python3 /Users/qiu/Desktop/dataset/scripts/build_dataset.py
python3 /Users/qiu/Desktop/dataset/scripts/validate_dataset.py
```

## Contribution Rules
1. Keep the benchmark scope fixed at 19 scenarios unless explicitly version-bumped.
2. Any new scenario must define: roles, sensitive_set, mni_baseline, trust_clauses, and risk_focus.
3. Run validation before opening a PR.
4. Keep all user-facing docs in English.
