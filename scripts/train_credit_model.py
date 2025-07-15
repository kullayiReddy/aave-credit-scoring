import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score
import joblib

# Load feature + score data
df = pd.read_csv("wallet_features.csv")

# Recompute scores to be sure
def compute_score(row):
    score = 500
    score += min(row["total_deposit_usd"], 50000) * 0.005
    score += min(row["repay_ratio"], 1.5) * 100
    score += min(row["activity_days"], 365) * 0.2
    score += row["action_diversity"] * 10
    score -= row["num_liquidations"] * 50
    return max(0, min(1000, round(score)))

df["credit_score"] = df.apply(compute_score, axis=1)

# Define features and target
features = [
    'num_transactions', 'num_deposits', 'total_deposit_usd',
    'num_borrows', 'total_borrow_usd', 'num_repays', 'total_repay_usd',
    'repay_ratio', 'num_liquidations', 'activity_days', 'action_diversity'
]
X = df[features]
y = df["credit_score"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
print(f"MAE: {mean_absolute_error(y_test, y_pred):.2f}")
print(f"R2: {r2_score(y_test, y_pred):.2f}")

# Save model
joblib.dump(model, "credit_model.pkl")
