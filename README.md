# @blackjackmath/research-papers

[![License: CC-BY-4.0](https://img.shields.io/badge/License-CC--BY--4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Data: Open Access](https://img.shields.io/badge/Data-Open%20Access-purple.svg)](https://github.com/blackjackmath-research/research-papers)
[![Portal: blackjackmath.org](https://img.shields.io/badge/Portal-blackjackmath.org-00E5FF.svg)](https://blackjackmath.org)

Academic preprints, reproducibility test suites, empirical datasets, and verification scripts for the **BlackjackMath Research Group** under the **Applied Probability Institute**.

---

## 📁 Repository Structure

```text
├── data/
│   ├── dealer_upcard_probabilities.csv    # Final total distribution vectors for 2-A under S17 and H17
│   └── blackjack_rules_house_edge_matrix.csv  # Combinatorial rule permutations across decks 1–8
├── papers/
│   └── blackjack-100m-simulation-study.md # Formal preprint on the 100M-hand empirical evaluation
└── scripts/
    └── verify_simulations.py              # Python 3.11 dataset validation suite
```

---

## 🔬 Dataset Verification

Run the verification suite using Python 3.11+:

```bash
python scripts/verify_simulations.py
```

Expected output:
```text
[BlackjackMath Dataset Audit]
✓ Verified 20 dealer upcard probability distribution profiles (sum = 1.00 ± 0.005).
✓ Verified 10 casino rule permutation benchmarks (Edge + RTP = 100.00%).
✓ All research datasets verified.
```

---

## 🏛️ Affiliation & Interactive Tools

Published openly by the **BlackjackMath Research Group** at the **Applied Probability Institute**.

- **Interactive Quant Suite**: [blackjackmath.org/en/tools/](https://blackjackmath.org/en/tools/)
- **Academic Mission**: [blackjackmath.org/en/about/](https://blackjackmath.org/en/about/)

---

## License

Creative Commons Attribution 4.0 International (CC-BY-4.0) © 2026 [BlackjackMath Research Group](https://blackjackmath.org)
