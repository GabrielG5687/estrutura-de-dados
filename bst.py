"""
Implementação de Árvore Binária de Busca (BST)
"""

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
        self.comparisons = 0
    
    def insert(self, key):
        """Insere um elemento na árvore"""
        self.root = self._insert_recursive(self.root, key)
    
    def _insert_recursive(self, node, key):
        if node is None:
            return Node(key)
        
        self.comparisons += 1
        if key < node.key:
            node.left = self._insert_recursive(node.left, key)
        elif key > node.key:wwwwwwwwwwwwww
            node.right = self._insert_recursive(node.right, key)
        
        return node
    
    def search(self, key):
        """Busca um elemento na árvore"""
        return self._search_recursive(self.root, key)
    
    def _search_recursive(self, node, key):
        if node is None:
            return False
        
        self.comparisons += 1
        if key == node.key:
            return True
        elif key < node.key:
            return self._search_recursive(node.left, key)
        else:
            return self._search_recursive(node.right, key)
    
    def remove(self, key):
        """Remove um elemento da árvore"""
        self.root = self._remove_recursive(self.root, key)
    
    def _remove_recursive(self, node, key):
        if node is None:
            return None
        
        self.comparisons += 1
        if key < node.key:
            node.left = self._remove_recursive(node.left, key)
        elif key > node.key:
            node.right = self._remove_recursive(node.right, key)
        else:
            # Nó encontrado
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            
            # Nó com dois filhos: pega o sucessor
            min_node = self._find_min(node.right)
            node.key = min_node.key
            node.right = self._remove_recursive(node.right, min_node.key)
        
        return node
    
    def _find_min(self, node):
        """Encontra o nó com valor mínimo"""
        while node.left is not None:
            node = node.left
        return node

    
    def inorder(self):
        """Percurso in-order (esquerda, raiz, direita)"""
        result = []
        self._inorder_recursive(self.root, result)
        return result
    
    def _inorder_recursive(self, node, result):
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.key)
            self._inorder_recursive(node.right, result)
    
    def preorder(self):
        """Percurso pre-order (raiz, esquerda, direita)"""
        result = []
        self._preorder_recursive(self.root, result)
        return result
    
    def _preorder_recursive(self, node, result):
        if node:
            result.append(node.key)
            self._preorder_recursive(node.left, result)
            self._preorder_recursive(node.right, result)
    
    def postorder(self):
        """Percurso post-order (esquerda, direita, raiz)"""
        result = []
        self._postorder_recursive(self.root, result)
        return result
    
    def _postorder_recursive(self, node, result):
        if node:
            self._postorder_recursive(node.left, result)
            self._postorder_recursive(node.right, result)
            result.append(node.key)
    
    def height(self):
        """Calcula a altura da árvore"""
        return self._height_recursive(self.root)
    
    def _height_recursive(self, node):
        if node is None:
            return 0
        return 1 + max(self._height_recursive(node.left), 
                       self._height_recursive(node.right))
    
    def reset_metrics(self):
        """Reseta as métricas de comparações"""
        self.comparisons = 0
