
# Binary Search Tree
# Node and Tree Class Definitations
# Add New Node
# Find Value
# Size
# Height
# Delete ?

class Node():
    def __init__(self, text, value):
        self.value = value
        self.text = text
        self.left = None
        self.right = None

class BinaryTree():
    def __init__(self,text:str,value:int):
        """
        This methods uses text and value to construct binary tree
        text: this parameter will be used as a key
        value: this parameter will be used as a position of the Node
        """
        self.root = Node(text,value)
          
    def add_node(self,text,value):
        new_node = Node(text,value)
        current_node = self.root
        while True:
            if value>current_node.value:
                if current_node.right is None:
                    current_node.right = new_node
                    break
                else:
                    current_node = current_node.right
            elif value<current_node.value:
                if current_node.left is None:
                    current_node.left = new_node
                    break
                else:
                    current_node = current_node.left
            else:
                print("ERRROR : Value is already exist!!")
                break

    def search_value(self,value):
        current_node = self.root
        while True:
            if current_node.value == value:
                return current_node.text
            if value<current_node.value:
                if current_node.left is None:
                    return "ERROR : Not found."
                current_node = current_node.left
            elif value>current_node.value:
                if current_node.right is None:
                    return "ERROR : Not found"
                current_node = current_node.right

    def size(self):
        return self._size(self.root)
        
    def _size(self, current_node):
        if current_node is None:
            return 0
        return 1 + self._size(current_node.left) + self._size(current_node.right)

    def height(self):
        return self._height(self.root)
    def _height(self, current_node):
        if current_node is None:
            return 0
        return 1 + max(self._height(current_node.left),self._height(current_node.right))

if __name__ == "__main__":
    my_tree = BinaryTree("Mehmet",32)
    my_tree.add_node("Sabriye",9)
    my_tree.add_node("Emirhan",31)
    my_tree.add_node("Ata",41)
    my_tree.add_node("Burdur",15)
    my_tree.add_node("Konya",42)
    my_tree.add_node("Bilecik",11)

    print(my_tree.search_value(41))
    print(my_tree.search_value(82))
    print(my_tree.size())
    print(my_tree.height())