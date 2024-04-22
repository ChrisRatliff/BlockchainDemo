from block import Block
import os

class Blockchain:
    def __init__(self):
        self.head = None

    def add_block(self, new_block):
        new_block.next = self.head
        self.head = new_block

    def mine(self, new_block):
        if self.head is None:
            new_block.previous_hash = "0"
        else:
            new_block.previous_hash = self.head.hash
        new_block.hash = new_block.calculate_hash()
        self.add_block(new_block)

if __name__ == "__main__":
    blockchain = Blockchain()
    output_data = ""
    for n in range(10):
        blockchain.mine(Block("Block " + str(n+1), None))
    current_block = blockchain.head
    while current_block is not None:
        output_data += current_block.hash + "\n"
        current_block = current_block.next

    output_path = r"C:\Users\lilsl\OneDrive\Documents\School\INFSYS3864\blockchain_lab"
    output_file = os.path.join(output_path, "output.txt")

    try:
        with open(output_file, "w") as file:
            file.write(output_data)
        print("Output has been successfully saved to:", output_file)
    except Exception as e:
        print("An error occurred while writing to the file:", e)
