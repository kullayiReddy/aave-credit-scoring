import pandas as pd
import matplotlib.pyplot as plt

# Load features
df = pd.read_csv("wallet_features.csv")

# Scoring logic
def compute_credit_score(row):
    score = 500  # Base score
    
    # Positive behaviors
    score += min(row["total_deposit_usd"], 50000) * 0.005     # Max +250
    score += min(row["repay_ratio"], 1.5) * 100                # Max +150
    score += min(row["activity_days"], 365) * 0.2              # Max +73
    score += row["action_diversity"] * 10                      # Max +50

    # Negative behavior
    score -= row["num_liquidations"] * 50                     # Penalty

    return max(0, min(1000, round(score)))

# Apply scoring
df["credit_score"] = df.apply(compute_credit_score, axis=1)

# Save scores to CSV
df[["wallet", "credit_score"]].to_csv("wallet_credit_scores.csv", index=False)
print("✅ Scores saved to wallet_credit_scores.csv")

# Plot histogram
plt.figure(figsize=(10,6))
plt.hist(df["credit_score"], bins=10, range=(0,1000), edgecolor="black", color="skyblue")
plt.title("Wallet Credit Score Distribution")
plt.xlabel("Score Range")
plt.ylabel("Number of Wallets")
plt.grid(True)
plt.savefig("score_distribution.png")
print("📊 Histogram saved to score_distribution.png")
plt.show()
