"""
Implementação de Árvore Rubro-Negra (Red-Black Tree)
"""

RED = True
BLACK = False

class RBNode:
    def __init__(self, key, color=RED):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
        self.color = color

class RBT:
    def __init__(self):
        self.nil = RBNode(None, BLACK)
        self.root = self.nil
        self.comparisons = 0
        self.rotations = 0
    
    def insert(self, key):
        """Insere um elemento na árvore Rubro-Negra"""
        node = RBNode(key)
        node.left = self.nil
        node.right = self.nil
        
        parent = None
        current = self.root
        
        while current != self.nil:
            parent = current
            self.comparisons += 1
            if node.key < current.key:
                current = current.left
            else:
                current = current.right
        
        node.parent = parent
        
        if parent is None:
            self.root = node
        elif node.key < parent.key:
            parent.left = node
        else:
            parent.right = node
        
        node.color = RED
        self._fix_insert(node)
    
    def _fix_insert(self, node):
        """Corrige as propriedades da árvore após inserção"""
        while node.parent and node.parent.color == RED:
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                
                if uncle.color == RED:
                    # Caso 1: tio é vermelho
                    node.parent.color = BLACK
                    uncle.color = BLACK
                    node.parent.parent.color = RED
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        # Caso 2: nó é filho direito
                        node = node.parent
                        self._rotate_left(node)
                    
                    # Caso 3: nó é filho esquerdo
                    node.parent.color = BLACK
                    node.parent.parent.color = RED
                    self._rotate_right(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                
                if uncle.color == RED:
                    node.parent.color = BLACK
                    uncle.color = BLACK
                    node.parent.parent.color = RED
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self._rotate_right(node)
                    
                    node.parent.color = BLACK
                    node.parent.parent.color = RED
                    self._rotate_left(node.parent.parent)
        
        self.root.color = BLACK
    
    def _rotate_left(self, x):
        """Rotação à esquerda"""
        self.rotations += 1
        y = x.right
        x.right = y.left
        
        if y.left != self.nil:
            y.left.parent = x
        
        y.parent = x.parent
        
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        
        y.left = x
        x.parent = y

    
    def _rotate_right(self, x):
        """Rotação à direita"""
        self.rotations += 1
        y = x.left
        x.left = y.right
        
        if y.right != self.nil:
            y.right.parent = x
        
        y.parent = x.parent
        
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        
        y.right = x
        x.parent = y
    
    def search(self, key):
        """Busca um elemento na árvore"""
        current = self.root
        while current != self.nil:
            self.comparisons += 1
            if key == current.key:
                return True
            elif key < current.key:
                current = current.left
            else:
                current = current.right
        return False
    
    def remove(self, key):
        """Remove um elemento (versão simplificada)"""
        node = self._find_node(key)
        if node == self.nil:
            return
        self._delete_node(node)
    
    def _find_node(self, key):
        """Encontra um nó pela chave"""
        current = self.root
        while current != self.nil:
            if key == current.key:
                return current
            elif key < current.key:
                current = current.left
            else:
                current = current.right
        return self.nil
    
    def _delete_node(self, node):
        """Remove um nó (implementação simplificada)"""
        if node.left == self.nil:
            self._transplant(node, node.right)
        elif node.right == self.nil:
            self._transplant(node, node.left)
        else:
            successor = self._minimum(node.right)
            if successor.parent != node:
                self._transplant(successor, successor.right)
                successor.right = node.right
                successor.right.parent = successor
            self._transplant(node, successor)
            successor.left = node.left
            successor.left.parent = successor
    
    def _transplant(self, u, v):
        """Substitui uma subárvore por outra"""
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent
    
    def _minimum(self, node):
        """Encontra o nó mínimo"""
        while node.left != self.nil:
            node = node.left
        return node
    
    def inorder(self):
        """Percurso in-order"""
        result = []
        self._inorder_recursive(self.root, result)
        return result
    
    def _inorder_recursive(self, node, result):
        if node != self.nil:
            self._inorder_recursive(node.left, result)
            result.append(node.key)
            self._inorder_recursive(node.right, result)
    
    def preorder(self):
        """Percurso pre-order"""
        result = []
        self._preorder_recursive(self.root, result)
        return result
    
    def _preorder_recursive(self, node, result):
        if node != self.nil:
            result.append(node.key)
            self._preorder_recursive(node.left, result)
            self._preorder_recursive(node.right, result)
    
    def postorder(self):
        """Percurso post-order"""
        result = []
        self._postorder_recursive(self.root, result)
        return result
    
    def _postorder_recursive(self, node, result):
        if node != self.nil:
            self._postorder_recursive(node.left, result)
            self._postorder_recursive(node.right, result)
            result.append(node.key)
    
    def height(self):
        """Calcula a altura da árvore"""
        return self._height_recursive(self.root)
    
    def _height_recursive(self, node):
        if node == self.nil:
            return 0
        return 1 + max(self._height_recursive(node.left), 
                       self._height_recursive(node.right))
    
    def reset_metrics(self):
        """Reseta as métricas de comparações e rotações"""
        self.comparisons = 0
        self.rotations = 0
