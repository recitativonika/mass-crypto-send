# Mass sending cryptocurrency to multiple addresses across different blockchains (like Ethereum and Binance Smart Chain)

## Please note that handling private keys and sending transactions should be done with great caution, as it can lead to loss of funds if not done properly!.

## - Important Warning -

• Security Risks: This script involves handling private keys, which should never be exposed or hard-coded in your scripts. Always use secure methods to manage your keys.
• Test on a Testnet: Before using this script on the mainnet, make sure to thoroughly test it on a testnet (like Ropsten for Ethereum or Testnet for BSC) to avoid any loss of funds.

## Installation & how to run?

install :
```bash
git clone https://github.com/recitativonika/mass-crypto-send.git
cd mass-crypto-send
pip install -r requirements.txt
```

before you run the script, you must:

• Add your Private Key and RPC URLs in the crypto.py script, replace the following placeholders:
```bash
YOUR_INFURA_PROJECT_ID: Your actual Infura project ID or another Ethereum node URL.
YOUR_PRIVATE_KEY: Your actual private key.
Adjust gas prices if necessary.
```
• Create a text file named addresses.txt and list your addresses with the amount and chain type (Ethereum or BSC). The format should be:
```bash
0x742d35Cc6634C0532925a3b844Bc454e4438f44e,0.01,eth
0x5c69a1aA9dF1c27C31fB9d0D66E6BfF0B1E9C4c6,0.02,bsc
```
• Run the Script with :
```bash
python crypto.py
```

# Important Notes:

• Gas Fees: Ensure you have enough ETH/BNB in your wallet to cover transaction fees for sending.

• Error Handling: The script does not currently handle errors extensively. It is advisable to add try-except blocks to handle potential exceptions.

• Testing: Test this script on a test network before using it on the main network to avoid losing funds.


This script allows you to efficiently send cryptocurrency balances to multiple addresses across Ethereum and Binance Smart Chain. Always exercise caution when handling private keys and making transactions!
