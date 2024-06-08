from solders.keypair import Keypair
import base58

new_account = Keypair()
wallet_address = str(new_account.pubkey())
private_key_bytes = new_account.secret()
public_key_bytes = bytes(new_account.pubkey())
encoded_keypair = private_key_bytes + public_key_bytes
private_key = base58.b58encode(encoded_keypair).decode()

print(f"Wallet Address: {wallet_address}")
print(f"Private Key: {private_key}")
