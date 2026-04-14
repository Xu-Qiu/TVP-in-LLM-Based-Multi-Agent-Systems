# Dataset Card: TVP-ScenarioGame-EN

## Overview
TVP-ScenarioGame-EN is a controlled benchmark for evaluating trust-conditioned information exposure in LLM-based multi-agent systems.

## Data Units
- **Scenario-level template** (`Sx-y`): task setup, roles, secrets, MNI baseline.
- **Instance-level sample**: one scenario under one trust level (`no_trust`, `low_trust`, `high_trust`).

## Core Fields
- `scenario_uid`, `macro_scene_id`, `macro_scene_name`, `subscene_title`
- `trust_level`, `tau`, `trust_policy`
- `task_objective`, `mni_baseline`
- `role_prompts`, `risk_focus`, `interaction_constraint`

## Intended Use
- OER/AD benchmarking under controlled trust interventions
- Cross-model and cross-framework comparison
- Security-oriented analysis of trust-mediated coordination

## Limitations
- This release contains scenario templates and prompts, not generated dialogue traces.
- OER/AD values must be computed from downstream model interaction logs.
