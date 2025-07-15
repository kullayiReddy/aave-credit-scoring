import json
from collections import defaultdict
import pandas as pd

# Load the JSON file
with open("user-wallet-transactions.json", "r") as f:
    transactions = json.load(f)

# Group by wallet
wallet_tx_map = defaultdict(list)
for tx in transactions:
    wallet = tx.get("userWallet")
    if wallet:
        wallet_tx_map[wallet].append(tx)

# Extract features
def extract_features(wallet_tx_map):
    data = []

    for wallet, txs in wallet_tx_map.items():
        actions = [tx["action"] for tx in txs]
        timestamps = [tx["timestamp"] for tx in txs]

        num_transactions = len(txs)
        num_deposits = actions.count("deposit")
        num_borrows = actions.count("borrow")
        num_repays = actions.count("repay")
        num_liquidations = actions.count("liquidationcall")

        deposit_usd = 0.0
        borrow_usd = 0.0
        repay_usd = 0.0

        for tx in txs:
            actionData = tx.get("actionData", {})
            try:
                amount = float(actionData.get("amount", 0)) / 1e6
                price = float(actionData.get("assetPriceUSD", 1))
                amount_in_usd = amount * price

                if tx["action"] == "deposit":
                    deposit_usd += amount_in_usd
                elif tx["action"] == "borrow":
                    borrow_usd += amount_in_usd
                elif tx["action"] == "repay":
                    repay_usd += amount_in_usd

            except:
                continue

        repay_ratio = repay_usd / borrow_usd if borrow_usd > 0 else 1.0
        activity_days = (
            (max(timestamps) - min(timestamps)) / (60 * 60 * 24)
            if len(timestamps) > 1 else 0
        )

        row = {
            "wallet": wallet,
            "num_transactions": num_transactions,
            "num_deposits": num_deposits,
            "total_deposit_usd": deposit_usd,
            "num_borrows": num_borrows,
            "total_borrow_usd": borrow_usd,
            "num_repays": num_repays,
            "total_repay_usd": repay_usd,
            "repay_ratio": repay_ratio,
            "num_liquidations": num_liquidations,
            "activity_days": activity_days,
            "action_diversity": len(set(actions))
        }
        data.append(row)

    return pd.DataFrame(data)

# Run feature extraction and save
df = extract_features(wallet_tx_map)
df.to_csv("wallet_features.csv", index=False)
print("✅ Feature extraction completed. Saved to wallet_features.csv")
