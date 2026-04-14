#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path('/Users/qiu/Desktop/dataset')

scenarios = [json.loads(line) for line in (ROOT / 'data' / 'scenarios.jsonl').read_text(encoding='utf-8').splitlines() if line.strip()]
instances = [json.loads(line) for line in (ROOT / 'data' / 'instances.jsonl').read_text(encoding='utf-8').splitlines() if line.strip()]

scenario_ids = {s['scenario_uid'] for s in scenarios}
assert len(scenarios) == 19, f'Expected 19 scenarios, got {len(scenarios)}'
assert len(scenario_ids) == 19, 'Duplicate scenario_uid found'

inst_ids = {i['instance_id'] for i in instances}
assert len(instances) == 57, f'Expected 57 instances, got {len(instances)}'
assert len(inst_ids) == 57, 'Duplicate instance_id found'

for i in instances:
    assert i['scenario_uid'] in scenario_ids, f"Unknown scenario_uid: {i['scenario_uid']}"
    assert i['trust_level'] in {'no_trust', 'low_trust', 'high_trust'}
    assert i['tau'] in {0.1, 0.5, 0.9}
    assert isinstance(i.get('task_objective'), str) and i['task_objective'].strip()
    assert isinstance(i.get('mni_baseline'), str) and i['mni_baseline'].strip()
    assert isinstance(i['role_prompts'], dict) and len(i['role_prompts']) >= 2

print('Validation passed: 19 scenarios, 57 instances, English canonical fields complete.')
