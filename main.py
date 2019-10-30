from blockchain import Blockchain

if __name__ == '__main__':
    blockchain = Blockchain()

    blockchain.add_new_block('Primeiro Bloco!')
    blockchain.add_new_block('Segundo Bloco!')
    blockchain.add_new_block('terceiro Bloco!')

    print(blockchain.get_all())