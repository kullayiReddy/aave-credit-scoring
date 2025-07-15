# 🔍 Credit Score Analysis

# 📊 Score Distribution

Score Range  Wallet Count (approx)

0–100            0

100–200          0

200–300          0 

300–400          0

400–500          0

500–600          ≈20

600–700         ≈900

700–800         ≈450

800–900         ≈1800

900–1000        ≈300

# ❌ Low Score Wallets (0–600)

These wallets showed:

Low or zero repayments

High liquidation counts

Single-day activity bursts

Performed limited types of actions (e.g., borrow only)

# ✅ High Score Wallets (800–1000)

These wallets had:

High deposits and regular repayments

Excellent repay-to-borrow ratio (>0.9)

Long-term usage (multi-day or month-wise activity)

3+ types of actions (deposit, repay, redeem, etc.)

Zero liquidation events

# 🔢 Summary Insights

Most wallets fell in the 800–900 range, showing healthy user behavior.

Very few wallets were penalized heavily (e.g., due to liquidation).

The ML model achieved low MAE and high R2, mimicking the rule-based logic well.

Use ml_wallet_scores.csv if you want to use the machine learning-based scoring instead of the rule-based one.
