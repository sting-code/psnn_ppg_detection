"""Phase 1 — Data loading from MIMIC-III via WFDB."""
import yaml
import numpy as np
import wfdb

def load_config(path="configs/config.yaml"):
    with open(path) as f:
        import yaml; return yaml.safe_load(f)
