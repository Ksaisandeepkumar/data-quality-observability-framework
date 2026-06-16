# Data Quality Observability Framework

## Business Problem
Data teams need reusable quality checks to identify null keys, duplicate records, negative values, schema issues, and operational data problems before datasets reach analytics users.

## Objective
Build a reusable data quality framework that profiles input datasets, applies validation rules, produces quality reports, and creates clean output datasets.

## Architecture
```text
Raw Dataset
  -> Data Quality Rules
  -> Quality Report
  -> Clean Dataset
```

## Key Data Engineering Concepts
- Null checks
- Duplicate detection
- Negative value validation
- Quality reporting
- Clean dataset generation

## How to Run
```bash
python src/run_pipeline.py
```

## Resume Bullet
Built a reusable data quality observability framework that validates datasets for null keys, duplicate records, and invalid numeric values while generating quality reports and clean curated outputs.
