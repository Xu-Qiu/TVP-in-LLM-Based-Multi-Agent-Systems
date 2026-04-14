# TVP-ScenarioGame-EN

Publication-ready open-source release of the scenario-game dataset for studying the Trust-Vulnerability Paradox (TVP) in LLM-based multi-agent systems.

## Benchmark Summary
- Scenario templates: **19**
- Trust-conditioned instances: **57** (`19 x 3`)
- Macro scenes:
  - `S1`: Gold Company Collaboration (6)
  - `S2`: Deep Sea Exploration Center (7)
  - `S3`: Mars Oasis Colony (6)
- Trust mapping:
  - `no_trust -> tau=0.1`
  - `low_trust -> tau=0.5`
  - `high_trust -> tau=0.9`

## Repository Structure
- `data/scenarios.jsonl`: canonical scenario templates (English)
- `data/instances.jsonl`: canonical trust-expanded instances (English)
- `data/*_zh_archive.jsonl`: archived Chinese-source standardized variants
- `metadata/`: dataset metadata, indexes, source mapping
- `docs/`: data card, standardization protocol, schema
- `scripts/`: build/export/validation scripts
- `raw/`: text extracted from original design documents

## Build and Validate
```bash
python3 /Users/qiu/Desktop/dataset/scripts/build_dataset.py
python3 /Users/qiu/Desktop/dataset/scripts/validate_dataset.py
```

## Citation
Please cite this dataset in your paper/repository release notes. A `CITATION.cff` file is included.
