"""
Verification Suite for 100M-Round Blackjack Datasets
BlackjackMath Research Group / Applied Probability Institute
"""

import csv
import sys
from pathlib import Path

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

DATA_DIR = Path(__file__).parent.parent / "data"

def verify_dealer_probabilities():
    path = DATA_DIR / "dealer_upcard_probabilities.csv"
    if not path.exists():
        print(f"ERROR: {path} not found")
        sys.exit(1)
    
    with open(path, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        count = 0
        for row in reader:
            probs = [
                float(row["prob_17"]),
                float(row["prob_18"]),
                float(row["prob_19"]),
                float(row["prob_20"]),
                float(row["prob_21"]),
                float(row["prob_bust"])
            ]
            total = sum(probs)
            assert abs(total - 1.0) < 0.005, f"Row sum for {row['dealer_upcard']} ({row['rule']}) = {total} != 1.0"
            count += 1
    
    print(f"✓ Verified {count} dealer upcard probability distribution profiles (sum = 1.00 ± 0.005).")

def verify_rules_matrix():
    path = DATA_DIR / "blackjack_rules_house_edge_matrix.csv"
    if not path.exists():
        print(f"ERROR: {path} not found")
        sys.exit(1)
    
    with open(path, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        count = 0
        for row in reader:
            edge = float(row["house_edge_pct"])
            rtp = float(row["player_rtp_pct"])
            assert abs((edge + rtp) - 100.0) < 0.01, f"Edge + RTP != 100% for {row['rule_key']}"
            count += 1
            
    print(f"✓ Verified {count} casino rule permutation benchmarks (Edge + RTP = 100.00%).")

if __name__ == "__main__":
    print("[BlackjackMath Dataset Audit]")
    verify_dealer_probabilities()
    verify_rules_matrix()
    print("✓ All research datasets verified.")
