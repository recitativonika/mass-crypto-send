from web3 import Web3

# Connect to Ethereum and Binance Smart Chain nodes
eth_node = "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"  # Replace with your Ethereum node URL
bsc_node = "https://bsc-dataseed.binance.org/"  # Replace with your BSC node URL

w3_eth = Web3(Web3.HTTPProvider(eth_node))
w3_bsc = Web3(Web3.HTTPProvider(bsc_node))

# Your wallet private key (DO NOT expose or hard-code this in production)
private_key = "YOUR_PRIVATE_KEY"  # Replace with your private key
account = w3_eth.eth.account.from_key(private_key)
nonce = w3_eth.eth.getTransactionCount(account.address)

def send_eth(to_address, amount):
    global nonce
    tx = {
        'nonce': nonce,
        'to': to_address,
        'value': w3_eth.toWei(amount, 'ether'),  # Convert ETH to Wei
        'gas': 2000000,
        'gasPrice': w3_eth.toWei('50', 'gwei'),  # Adjust gas price as needed
        'chainId': 1  # Mainnet
    }
    signed_tx = w3_eth.eth.account.sign_transaction(tx, private_key)
    tx_hash = w3_eth.eth.sendRawTransaction(signed_tx.rawTransaction)
    nonce += 1
    return tx_hash.hex()

def send_bnb(to_address, amount):
    global nonce
    tx = {
        'nonce': nonce,
        'to': to_address,
        'value': w3_bsc.toWei(amount, 'ether'),  # Convert BNB to Wei
        'gas': 2000000,
        'gasPrice': w3_bsc.toWei('5', 'gwei'),  # Adjust gas price as needed
        'chainId': 56  # BSC Mainnet
    }
    signed_tx = w3_bsc.eth.account.sign_transaction(tx, private_key)
    tx_hash = w3_bsc.eth.sendRawTransaction(signed_tx.rawTransaction)
    nonce += 1
    return tx_hash.hex()

def read_addresses_from_file(filename):
    with open(filename, 'r') as f:
        addresses = f.read().splitlines()
    return addresses

def main():
    input_file = "addresses.txt"  # Input file containing addresses and amounts
    addresses = read_addresses_from_file(input_file)

    for line in addresses:
        address, amount, chain = line.split(",")  # Assuming format: address,amount,chain
        amount = float(amount)
        print(f"Sending {amount} to {address} on {chain}...")

        if chain.lower() == 'eth':
            tx_hash = send_eth(address, amount)
            print(f"ETH Transaction Hash: {tx_hash}")
        elif chain.lower() == 'bsc':
            tx_hash = send_bnb(address, amount)
            print(f"BNB Transaction Hash: {tx_hash}")
        else:
            print(f"Unsupported chain: {chain}")

if __name__ == "__main__":
    main()
