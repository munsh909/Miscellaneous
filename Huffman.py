import heapq
from collections import defaultdict, Counter

class TreeNode:
    def __init__(self, symbol, weight):
        self.symbol = symbol
        self.weight = weight
        self.left = None
        self.right = None
    
    def __lt__(self, other):
        return self.weight < other.weight

def generate_huffman_tree(freq_dict):
    priority_queue = [TreeNode(symbol, weight) for symbol, weight in freq_dict.items()]
    heapq.heapify(priority_queue)

    while len(priority_queue) > 1:
        left_child = heapq.heappop(priority_queue)
        right_child = heapq.heappop(priority_queue)
        merged_node = TreeNode(None, left_child.weight + right_child.weight)
        merged_node.left = left_child
        merged_node.right = right_child
        heapq.heappush(priority_queue, merged_node)

    return priority_queue[0]

def map_huffman_codes(node, path='', code_map=defaultdict()):
    if node is not None:
        if node.symbol is not None:
            code_map[node.symbol] = path
        map_huffman_codes(node.left, path + '0', code_map)
        map_huffman_codes(node.right, path + '1', code_map)
    return code_map

def encode_message(message):
    frequency_dict = Counter(message)
    huffman_root = generate_huffman_tree(frequency_dict)
    huffman_code_map = map_huffman_codes(huffman_root)

    encoded_str = ''.join(huffman_code_map[char] for char in message)
    return encoded_str, huffman_code_map

def decode_message(encoded_str, huffman_code_map):
    reversed_map = {code: symbol for symbol, code in huffman_code_map.items()}
    current_code = ''
    decoded_chars = []

    for bit in encoded_str:
        current_code += bit
        if current_code in reversed_map:
            decoded_chars.append(reversed_map[current_code])
            current_code = ''

    return ''.join(decoded_chars)

if __name__ == "__main__":
    sample_text = "this is an encoded message"
    
    encoded, code_map = encode_message(sample_text)
    print("Encoded Message:", encoded)
    print("Huffman Code Map:", code_map)
    
    decoded = decode_message(encoded, code_map)
    print("Decoded Message:", decoded)
