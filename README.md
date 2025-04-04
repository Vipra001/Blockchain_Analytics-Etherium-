# Etherscan Transaction Tracker

## Overview
This project is a Python-based **Ethereum Transaction Tracker** that fetches and organizes **ETH transactions, ERC-20 token transfers, and NFT transfers** using the **Etherscan API**. The data is saved into an Excel file for easy analysis.

## Features 🚀
- ✅ **Fetch ETH Transactions** (incoming & outgoing)
- ✅ **Retrieve ERC-20 Token Transfers**
- ✅ **Fetch NFT Transfers (ERC-721 & ERC-1155)**
- ✅ **Save Data to an Excel File** with multiple sheets

## Requirements 📌
- Python 3.x
- `requests` and `pandas` libraries (install using `pip install requests pandas`)
- An **Etherscan API Key**
- A valid **Ethereum Wallet Address** (Make sure to change the ETH address in `script.py` before running the script)

## Installation & Usage ⚙️
1. Clone this repository:
   ```bash
   git clone https://github.com/Vipra001/etherscan-tracker.git
   cd etherscan-tracker
   ```
2. Install dependencies:
   ```bash
   pip install requests pandas
   ```
3. Update **API Key & Ethereum Address** in `script.py`:
   ```python
   API_KEY = "YOUR_ETHERSCAN_API_KEY"
   ETH_ADDRESS = "YOUR_ETH_WALLET_ADDRESS"  # Change this to your Ethereum wallet address
   ```
4. Run the script:
   ```bash
   python script.py
   ```

## Output 📊
- The script will create an `Ethereum_Transactions.xlsx` file containing:
  - **ETH_Transactions** sheet (ETH transfers)
  - **Token_Transfers** sheet (ERC-20 transfers)
  - **NFT_Transfers** sheet (ERC-721 & ERC-1155 transactions)

## API Used 🌐
[Etherscan API](https://etherscan.io/apis) - A powerful tool to interact with Ethereum blockchain data.

## License 📝
This project is **open-source** under the MIT License.

## Hashtags 🔖
#Blockchain #Ethereum #Crypto #Etherscan #DataAnalytics #Python #Web3 #NFTs #CryptoTransactions #PythonScripts

---
🔥 **Developed by [Vipra Sharma](https://github.com/Vipra001)** 🚀

