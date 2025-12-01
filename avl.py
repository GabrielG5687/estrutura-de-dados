"""
Implementação de Árvore AVL
"""

class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVL:
    def __init__(self):
        self.root = None
        self.comparisons = 0
        self.rotations = 0
    
    def insert(self, key):
        """Insere um elemento na árvore AVL"""
        self.root = self._insert_recursive(self.root, key)
    
    def _insert_recursive(self, node, key):
        if node is None:
            return AVLNode(key)
        
        self.comparisons += 1
        if key < node.key:
            node.left = self._insert_recursive(node.left, key)
        elif key > node.key:
            node.right = self._insert_recursive(node.right, key)
        else:
            return node
        
        # Atualiza altura
        node.height = 1 + max(self._get_height(node.left), 
                              self._get_height(node.right))
        
        # Calcula fator de balanceamento
        balance = self._get_balance(node)
        
        # Rotação à direita (Left-Left)
        if balance > 1 and key < node.left.key:
            return self._rotate_right(node)
        
        # Rotação à esquerda (Right-Right)
        if balance < -1 and key > node.right.key:
            return self._rotate_left(node)
        
        # Rotação dupla esquerda-direita (Left-Right)
        if balance > 1 and key > node.left.key:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)
        
        # Rotação dupla direita-esquerda (Right-Left)
        if balance < -1 and key < node.right.key:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)
        
        return node
    
    def _rotate_left(self, z):
        """Rotação simples à esquerda"""
        self.rotations += 1
        y = z.right
        T2 = y.left
        
        y.left = z
        z.right = T2
        
        z.height = 1 + max(self._get_height(z.left), 
                           self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), 
                           self._get_height(y.right))
        
        return y
    
    def _rotate_right(self, z):
        """Rotação simples à direita"""
        self.rotations += 1
        y = z.left
        T3 = y.right
        
        y.right = z
        z.left = T3
        
        z.height = 1 + max(self._get_height(z.left), 
                           self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), 
                           self._get_height(y.right))
        
        return y

    
    def _get_height(self, node):
        """Retorna a altura de um nó"""
        if node is None:
            return 0
        return node.height
    
    def _get_balance(self, node):
        """Calcula o fator de balanceamento"""
        if node is None:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)
    
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
            
            # Nó com dois filhos
            min_node = self._find_min(node.right)
            node.key = min_node.key
            node.right = self._remove_recursive(node.right, min_node.key)
        
        if node is None:
            return None
        
        # Atualiza altura
        node.height = 1 + max(self._get_height(node.left), 
                              self._get_height(node.right))
        
        # Rebalanceia
        balance = self._get_balance(node)
        
        # Left-Left
        if balance > 1 and self._get_balance(node.left) >= 0:
            return self._rotate_right(node)
        
        # Left-Right
        if balance > 1 and self._get_balance(node.left) < 0:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)
        
        # Right-Right
        if balance < -1 and self._get_balance(node.right) <= 0:
            return self._rotate_left(node)
        
        # Right-Left
        if balance < -1 and self._get_balance(node.right) > 0:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)
        
        return node
    
    def _find_min(self, node):
        """Encontra o nó com valor mínimo"""
        while node.left is not None:
            node = node.left
        return node
    
    def inorder(self):
        """Percurso in-order"""
        result = []
        self._inorder_recursive(self.root, result)
        return result
    
    def _inorder_recursive(self, node, result):
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.key)
            self._inorder_recursive(node.right, result)
    
    def preorder(self):
        """Percurso pre-order"""
        result = []
        self._preorder_recursive(self.root, result)
        return result
    
    def _preorder_recursive(self, node, result):
        if node:
            result.append(node.key)
            self._preorder_recursive(node.left, result)
            self._preorder_recursive(node.right, result)
    
    def postorder(self):
        """Percurso post-order"""
        result = []
        self._postorder_recursive(self.root, result)
        return result
    
    def _postorder_recursive(self, node, result):
        if node:
            self._postorder_recursive(node.left, result)
            self._postorder_recursive(node.right, result)
            result.append(node.key)
    
    def height(self):
        """Retorna a altura da árvore"""
        return self._get_height(self.root)
    
    def reset_metrics(self):
        """Reseta as métricas de comparações e rotações"""
        self.comparisons = 0
        self.rotations = 0
