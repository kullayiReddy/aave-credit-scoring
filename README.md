 #  Aave V2 Wallet Credit Scoring System

🧐 Overview

This project creates a credit scoring system for wallets that interact with the Aave V2 protocol on the Polygon network. The scores range from 0 to 1000, indicating the financial reliability of DeFi users. We use a two-step approach:

#Rule-Based Model (baseline)#

Machine Learning Regression Model (Random Forest)

🔄 Architecture & Processing Pipeline

Raw JSON (~100K tx)
     ⬇️
Group by wallet
     ⬇️
Feature Engineering (wallet_features.csv)
     ⬇️
Rule-Based Scoring ✅
     ⬇️
Train ML Model ⚖️ (Random Forest)
     ⬇️
Predict ML Scores (ml_wallet_scores.csv)


# ⚖️ Features Used Per Wallet 

num_transactions

num_deposits, total_deposit_usd

num_borrows, total_borrow_usd

num_repays, total_repay_usd

repay_ratio = repay / borrow

num_liquidations

activity_days (last - first tx)

action_diversity (number of unique actions)

# 📊 Rule-Based Scoring Formula 

score = 500

score += min(deposit_usd, 50000) * 0.005        # Max +250

score += min(repay_ratio, 1.5) * 100            # Max +150

score += min(activity_days, 365) * 0.2          # Max +73

score += action_diversity * 10                  # Max +50

score -= num_liquidations * 50                  # Penalty

# 🚀 ML Model Training 

Model: RandomForestRegressor

Target: Rule-based score (used as ground truth)

Input: Engineered features

Output: ml_wallet_scores.csv

# 📄 Files in This Repo 
aave-credit-scoring/
├── data/

│   ├─ user-wallet-transactions.json

│   ├─ wallet_features.csv

│   ├─ wallet_credit_scores.csv

│   ├─ ml_wallet_scores.csv

│   └─ score_distribution.png

├─ scripts/

│   ├─ feature_extraction.py

│   ├─ score_wallets.py

│   ├─ train_credit_model.py

│   └─ predict_with_model.py

├─ credit_model.pkl

├─ README.md

└─ analysis.md

# 📃 How to Run

python scripts/feature_extraction.py

python scripts/score_wallets.py

python scripts/train_credit_model.py

python scripts/predict_with_model.py



