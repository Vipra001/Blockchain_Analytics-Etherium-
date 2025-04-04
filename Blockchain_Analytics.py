import requests
import pandas as pd

# Replace with your Etherscan API key
API_KEY = "get_your_own_API for free"

# Ethereum wallet address (Vitalik Buterin's wallet)
ETH_ADDRESS = "0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045"

# Base URL for Etherscan API
BASE_URL = "https://api.etherscan.io/api"

# Function to fetch transactions
def fetch_transactions(module, action):
    url = f"{BASE_URL}?module={module}&action={action}&address={ETH_ADDRESS}&apikey={API_KEY}&sort=asc"
    response = requests.get(url).json()
    if response["status"] == "1":
        return response["result"]
    else:
        return []

# Fetch ETH Transactions (Incoming + Outgoing)
eth_transactions = fetch_transactions("account", "txlist")

# Fetch Token Transfers (ERC-20)
token_transfers = fetch_transactions("account", "tokentx")

# Fetch NFT Transfers (ERC-721 & ERC-1155)
nft_transfers = fetch_transactions("account", "tokennfttx")

# Convert to DataFrames
df_eth = pd.DataFrame(eth_transactions)
df_tokens = pd.DataFrame(token_transfers)
df_nfts = pd.DataFrame(nft_transfers)

# Save to Excel with multiple sheets
with pd.ExcelWriter("Ethereum_Transactions.xlsx") as writer:
    df_eth.to_excel(writer, sheet_name="ETH_Transactions", index=False)
    df_tokens.to_excel(writer, sheet_name="Token_Transfers", index=False)
    df_nfts.to_excel(writer, sheet_name="NFT_Transfers", index=False)

print("Transaction data saved to Ethereum_Transactions.xlsx")
