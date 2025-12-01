# 🖥️ Estruturas de Dados: Árvores

## BST • AVL • RBT

---

# 🌳 Visão Geral do Projeto

Este projeto implementa três estruturas fundamentais de árvores binárias de busca:

- **BST** – Binary Search Tree
- **AVL** – Árvore AVL (auto-balanceada)
- **RBT** – Árvore Rubro-Negra

Cada implementação inclui:
- Inserção, Busca, Remoção
- Percursos (inorder, preorder, postorder)
- Métricas de desempenho (comparações e rotações)

---

# 🧱 BST - Binary Search Tree

## Estrutura mais simples

✔ Mantém a propriedade: **esquerda < raiz < direita**

✔ Operações: Inserção, Busca, Remoção, Percursos, Altura

❌ **Não é balanceada**
- Pode se degradar para uma lista encadeada (O(n))

---

# 📦 Classes da BST

## Node
- `key` - valor armazenado
- `left` - filho esquerdo
- `right` - filho direito

## BST
- `root` - raiz da árvore
- `comparisons` - contador de comparações

---

# 🔧 Principais Funções da BST

- `insert()` / `_insert_recursive()` - Inserção
- `search()` / `_search_recursive()` - Busca
- `remove()` / `_remove_recursive()` - Remoção
- `_find_min()` - Encontra menor valor
- `inorder()`, `preorder()`, `postorder()` - Percursos
- `height()` - Calcula altura
- `reset_metrics()` - Reseta contadores

---

# 🔍 Funcionamento da Inserção na BST

1. Compare com o nó atual
2. Se **menor** → vai para esquerda
3. Se **maior** → vai para direita
4. Se **None** → cria nó
5. Incrementa `comparisons`

⚠️ **Sem balanceamento**
A forma da árvore depende da ordem de inserção

---

# 🌲 AVL - Árvore Auto-Balanceada

## Sempre balanceada

✔ Diferença de alturas ≤ 1

✔ Garantia de **O(log n)** em busca, inserção e remoção

✔ Usa rotações para balancear:
- Rotação simples esquerda
- Rotação simples direita
- Rotação dupla esquerda-direita
- Rotação dupla direita-esquerda

---

# ⚙️ Classes da AVL

## AVLNode
- `key`, `left`, `right`
- `height` - altura do nó

## AVL
- `root`, `comparisons`, `rotations`

---

# 🔧 Principais Funções da AVL

- `insert()` / `_insert_recursive()` - Inserção com balanceamento
- `_rotate_left()`, `_rotate_right()` - Rotações
- `_get_height()` - Retorna altura
- `_get_balance()` - Calcula fator de balanceamento
- `remove()` - Remoção com rebalanceamento
- Percursos, `height()`, `reset_metrics()`

---

# 🔄 Casos de Rotação da AVL

## 1. Left-Left
Desbalanceamento à esquerda → **rotação direita**

## 2. Right-Right
Desbalanceamento à direita → **rotação esquerda**

## 3. Left-Right
Rotação esquerda no filho + rotação direita

## 4. Right-Left
Rotação direita no filho + rotação esquerda

---

# 🌑🔴 RBT - Árvore Rubro-Negra

## Árvore balanceada por cores

✔ Não requer balanceamento perfeito como AVL

✔ **Propriedades essenciais:**
1. Nó é vermelho ou preto
2. Raiz é preta
3. NIL é preto
4. Vermelho não pode ter filho vermelho
5. Caminhos têm a mesma quantidade de nós pretos

---

# 💪 Vantagem da RBT

✔ Excelente performance em **inserção e remoção**

✔ **Menos rotações** que AVL

✔ Usada em bibliotecas padrão:
- `std::map` e `std::set` (C++)
- `TreeMap` (Java)
- Implementações de bancos e índices

---

# ⚙️ Classes da RBT

## RBNode
- `key`, `parent`, `left`, `right`
- `color` - RED ou BLACK

## RBT
- `root`, `nil` (sentinela)
- `comparisons`, `rotations`

---

# 🔧 Funções Importantes da RBT

- `insert()` - Inserção
- `_fix_insert()` - Corrige violações de cor
- `_rotate_left()`, `_rotate_right()` - Rotações
- `search()` - Busca
- `remove()` / `_delete_node()` - Remoção
- `_transplant()`, `_minimum()`
- Percursos, `height()`, `reset_metrics()`

---

# 🟥 Como a RBT Corrige Inserções?

## Casos clássicos:

**1. Tio Vermelho**
- Recolore pai e tio → sobe o avô

**2. Tio Preto + nó interno**
- Rotação simples para formar caso 3

**3. Tio Preto + nó externo**
- Rotação + recoloração

**Garantia final:** raiz é preta, regras 4 e 5 não são violadas

---

# ⚖️ Comparativo Geral

| Característica | BST | AVL | RBT |
|---------------|-----|-----|-----|
| Balanceamento | ❌ | ✔ rígido | ✔ flexível |
| Altura máxima | O(n) | O(log n) | O(log n) |
| Inserção | Rápida | Média | Rápida |
| Remoção | Média | Difícil | Média |
| Busca | Variável | Mais rápida | Rápida |
| Rotações | 0 | Muitas | Poucas |
| Complexidade | Simples | Média | Alta |

---

# 🧠 Quando Usar Cada Uma?

## ✨ BST
- Estruturas simples
- Dados quase aleatórios
- Pouca modificação

## ⚡ AVL
- Aplicações que exigem buscas MUITO rápidas
- Tabelas estáticas com raras remoções

## 🔥 RBT
- Sistemas com muitas inserções/remoções
- Bibliotecas padrão (C++, Java)
- Implementações de bancos e índices

---

# 📏 Métricas de Desempenho

## `comparisons`
Mostra a eficiência lógica (busca, inserção, remoção)

## `rotations`
Aplica-se a AVL e RBT
Mostra o quanto a estrutura precisou se reorganizar

**Ideal para análises comparativas entre as árvores**

---

# 🧪 Demonstrações Incluídas

O projeto apresenta:
- ✅ Código limpo e estruturado
- ✅ Execução das três árvores
- ✅ Comparação de métricas
- ✅ Percursos e visualização
- ✅ Ferramentas para análise de complexidade

**Ideal para:**
- Estudos
- Trabalhos acadêmicos
- Demonstrações práticas

---

# 🎯 Conclusão

## Este projeto demonstra:

**🌱 BST** - Uma base simples e eficiente

**🌲 AVL** - Busca extremamente rápida com balanceamento rígido

**🌑🔴 RBT** - O melhor equilíbrio entre inserção, remoção e busca

---

# 🙌 Obrigado!

Projeto completo de Estruturas de Dados

**Árvores Binárias de Busca**

BST • AVL • RBT