import pandas as pd
import joblib

# Step 1: Load the features file
df = pd.read_csv("wallet_features.csv")

# Step 2: Define feature columns (same as during training)
features = [
    'num_transactions', 'num_deposits', 'total_deposit_usd',
    'num_borrows', 'total_borrow_usd', 'num_repays', 'total_repay_usd',
    'repay_ratio', 'num_liquidations', 'activity_days', 'action_diversity'
]

# Step 3: Load the trained model
model = joblib.load("credit_model.pkl")

# Step 4: Predict ML-based credit score
df["ml_credit_score"] = model.predict(df[features]).round(2)

# Step 5: Save predictions to CSV
df[["wallet", "ml_credit_score"]].to_csv("ml_wallet_scores.csv", index=False)
print("✅ ML-based credit scores saved to ml_wallet_scores.csv")
