import random
from pathlib import Path

import pandas as pd

BASE = Path(__file__).resolve().parents[1]
INPUT = BASE / "data" / "input"
OUTPUT = BASE / "data" / "output"
INPUT.mkdir(parents=True, exist_ok=True)
OUTPUT.mkdir(parents=True, exist_ok=True)


def main():
    df = pd.DataFrame([
        {
            "record_id": f"REC{i:06d}",
            "customer_id": None if i % 117 == 0 else f"CUST{random.randint(1000,9999)}",
            "amount": -100 if i % 143 == 0 else round(random.uniform(5, 3000), 2),
            "event_date": "2026-06-15",
            "source_system": random.choice(["crm", "billing", "claims", "payments"]),
        }
        for i in range(1, 2001)
    ])
    df = pd.concat([df, df.iloc[[10, 20, 30]]], ignore_index=True)
    df.to_csv(INPUT / "sample_data_raw.csv", index=False)

    checks = []
    checks.append({"rule_name": "total_records", "metric_value": len(df), "status": "INFO"})
    checks.append({"rule_name": "null_customer_id", "metric_value": int(df["customer_id"].isna().sum()), "status": "FAIL" if df["customer_id"].isna().sum() > 0 else "PASS"})
    checks.append({"rule_name": "negative_amount", "metric_value": int((df["amount"] <= 0).sum()), "status": "FAIL" if (df["amount"] <= 0).sum() > 0 else "PASS"})
    checks.append({"rule_name": "duplicate_record_id", "metric_value": int(df.duplicated(subset=["record_id"]).sum()), "status": "FAIL" if df.duplicated(subset=["record_id"]).sum() > 0 else "PASS"})

    report = pd.DataFrame(checks)
    report.to_csv(OUTPUT / "data_quality_report.csv", index=False)

    clean = df.dropna(subset=["customer_id"])
    clean = clean[clean["amount"] > 0]
    clean = clean.drop_duplicates(subset=["record_id"])
    clean.to_csv(OUTPUT / "clean_dataset.csv", index=False)

    print("Data quality observability framework completed")
    print(report)


if __name__ == "__main__":
    main()
