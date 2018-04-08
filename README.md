# pychain
Educational Blockchain implementation in Python. The development is separated into stages from a simple to a complex implementation. I made a point of using seminal papers to implement the blockchain from first principles. This implementation is mostly modeled after bitcoin for sake of simplicity. 

## Stage 1
The first stage more or less simulates a blockchain without yet implementing all the cryptographic proofs and security. There is no network yet, only a single node accepting transactions, calculating PoW and signing a block. 

* Node
    * Accept transaction
    * Combine transactions into a block
    * Calculate Proof of Work
    * Sign block and append it to the blockchain
* Block model
    * Previous Hash
    * List of all transactions
    * Nonce
    * Signature
* Transaction model
    * Public Key receiver
    * value
    * transaction hash
    * Signature with private key
* Wallet
    * Generate keypairs
    * Build and sign transaction

### Project structure
The node is implemented as a Flask API and meant to run only locally. The blockchain is kept in memory.

## Stage 2
* Block model
    * Implement merkle tree for the transactions