import sys

# 1. The Node Class
class Node:
    def __init__(self, sku, quantity):
        self.sku = sku
        self.quantity = quantity
        self.left = None
        self.right = None

# 2. The Manager Class
class InventoryManager:
    def __init__(self):
        self.root = None

    # --- PUBLIC METHODS (Called by the main loop) ---

    def add(self, sku, quantity):
        # Start the recursion from the root
        self.root = self._add_recursive(self.root, sku, quantity)
        print(f"Added: SKU={sku}, Stock={quantity}")

    def find(self, sku):
        result_node = self._find_recursive(self.root, sku)
        if result_node:
            print(f"Found: SKU={result_node.sku}, Stock={result_node.quantity}")
        else:
            print(f"Not found: SKU={sku}")

    def between(self, low, high):
        results = []
        self._between_recursive(self.root, low, high, results)
        
        if not results:
            print(f"Between [{low}-{high}]: none")
        else:
            # Format list as comma-separated string
            print(f"Between [{low}-{high}]: {results}")

    def depth(self):
        d = self._depth_recursive(self.root)
        print(f"Tree depth: {d}")

    def route(self, sku):
        path = []
        found = self._route_recursive(self.root, sku, path)
        if found:
            print(f"Route to {sku}: {path}")
        else:
            print(f"Route to {sku}: not found")

    def list_all(self):
        results = []
        self._list_recursive(self.root, results)
        print(f"Sorted: {results}")

    # --- PRIVATE HELPER METHODS (You implement these!) ---

    def _add_recursive(self, current, sku, quantity):
        # TODO: Implement the logic to insert a node
        # 1. Base case: if current is None, return new Node
        # 2. If sku < current.sku, recurse left
        # 3. If sku > current.sku, recurse right
        # 4. If sku == current.sku, update quantity
        # if current == None:
        #     return
        # if sku < current.sku:

        pass 

    def _find_recursive(self, current, sku):
        # TODO: Implement logic to find a node and return it
        pass

    def _between_recursive(self, current, low, high, result_list):
        # TODO: Implement In-Order traversal
        # 1. Go Left if current > low
        # 2. Add current to list if in range
        # 3. Go Right if current < high
        pass

    def _depth_recursive(self, current):
        # TODO: Calculate depth
        # Return -1 if current is None
        # Return 1 + max(left_depth, right_depth)
        pass

    def _route_recursive(self, current, target_sku, path_list):
        # TODO: Trace path
        # 1. Append current sku to path_list
        # 2. Check match. If match, return True
        # 3. Recurse left or right
        # 4. If end of tree reached without match, return False
        pass

    def _list_recursive(self, current, result_list):
        # TODO: Standard In-Order Traversal (Left -> Root -> Right)
        pass

# --- MAIN EXECUTION LOOP ---
def solve():
    # This part handles reading the input format
    # Simulating the "N" operations loop
    case_number = 1
    
    # You would typically read from sys.stdin here
    # Example loop structure:
    # while True:
    #     try:
    #         line = sys.stdin.readline()
    #         if not line: break
    #         N = int(line.strip())
    #         if N == 0: break
    #         
    #         manager = InventoryManager()
    #         print(f"Case {case_number}:")
    #         
    #         for _ in range(N):
    #             # Parse operation (ADD, FIND, etc.)
    #             # Call manager.add(), manager.find(), etc.
    #         
    #         print("") # Blank line after case
    #         case_number += 1
    #     except ValueError:
    #         break
    pass

if __name__ == "__main__":
    solve()