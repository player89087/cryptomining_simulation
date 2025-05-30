import hashlib
import random
from time import sleep
import time
import os 

transaction = ""
nonce = 0 
blockchain = []
block_number = 0 
prev_transaction_hash = ""
y = 1 
try:
    while True: 
        for i in range(0,1):
            letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
                    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
            numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0] 
            sender = random.choice(letters)
            receiver = random.choice(letters)
            amount = random.choice(numbers)
            
            transaction_str = f"{sender} has sent {receiver} {amount} BTC {nonce} Previous Hash {prev_transaction_hash}"
            print(f"Generated transaction: {transaction_str}")
            sleep(3)
            start = time.time()
            
            
        for i in range(0,1000000000000):  
            nonce = i 
            transaction_str = f"{sender} has sent {receiver} {amount} BTC {nonce} Previous Hash {prev_transaction_hash}"
            transaction_hash = hashlib.sha256(transaction_str.encode("utf-8")).hexdigest()
            if transaction_hash.startswith("0" * y):
                end = time.time()
                print("Valid Nonce found: " + str(i))
                print(transaction_hash)
                blockchain.append("Block " + "   "+  str(block_number)  +  "       "+ "Block_Hash " + "   "+  transaction_hash + "      "+ "transaction "+ "   " + transaction_str + "   "+ "Previous Blockhash " + prev_transaction_hash)
                block_number += 1
                os.system('cls||clear')
                x = len(blockchain)           
                x = round(x)
                x = int(x)
                for x in range(0,x):
                    print(blockchain[x])
                    with open("blockchain.txt", "a") as file:
                        file.write(blockchain[x])
                    x += 1
                dur = end - start 
                 

                if dur >= 60:
                    y -= 1
                elif dur <= 60:
                    y += 1
                print(f"The time for the block was {dur} seconds")   
                nonce = 0 
                prev_transaction_hash = transaction_hash
                sleep(5)
                os.system('cls||clear') 
                
                break
            else:
                print("current hash: " + transaction_hash )
                transaction_str = f"{sender} has sent {receiver} {amount} "
                print(i)

    
        sleep(3)
except KeyboardInterrupt: 
    os.system('cls||clear')
    print("Bye :)")
