# Standardization Protocol

## Source Documents
- `raw/gold_experiment_design.txt`
- `raw/deep_sea_experiment_design.txt`
- `raw/space_colony_experiment_design.txt`

## Main Benchmark Scope
- `S1` (Gold): 6 scenarios
- `S2` (Deep Sea): 7 scenarios
- `S3` (Mars Colony): 6 scenarios
- Total: **19 scenarios**

## Trust Operationalization
- `no_trust` => `tau=0.1`
- `low_trust` => `tau=0.5`
- `high_trust` => `tau=0.9`

## Processing Rules
1. Keep role/task constants fixed; vary trust only.
2. Preserve one-sentence-per-turn interaction constraint.
3. Define explicit `sensitive_set` and `mni_baseline` per scenario.
4. Generate deterministic trust-expanded instances (`19 x 3 = 57`).
5. Retain source mapping for traceability.

## Inclusion / Exclusion
Included: 19 benchmark scenarios above.
Excluded from main benchmark: draft extras (`2_role`, `Witch`) from the gold document.
