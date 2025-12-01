# 🌳 Árvore Binária de Busca (BST) - Exemplos Práticos com Código

Este documento apresenta exemplos práticos de uso da implementação da BST, demonstrando cada funcionalidade com código executável e explicações detalhadas.

---

## 📦 Importação e Criação da Árvore

```python
from bst import BST

# Criar uma nova árvore BST vazia
arvore = BST()
print(f"Árvore criada. Raiz: {arvore.root}")  # None
print(f"Altura inicial: {arvore.height()}")    # 0
print(f"Comparações: {arvore.comparisons}")    # 0
```

**O que acontece:**
- Uma árvore vazia é criada
- A raiz é `None`
- A altura é 0
- Contador de comparações inicia em 0

---

## 📥 Inserção de Elementos

### Exemplo 1: Primeira Inserção (Criando a Raiz)

```python
from bst import BST

arvore = BST()

# Primeira inserção cria a raiz
arvore.insert(50)

print(f"Raiz: {arvore.root.key}")           # 50
print(f"Altura: {arvore.height()}")         # 1
print(f"Elementos: {arvore.inorder()}")     # [50]
```

**Estrutura:**
```
50
```

**Explicação:**
- Primeiro elemento inserido vira a raiz
- Árvore com um único nó tem altura 1


### Exemplo 2: Inserção Balanceada

```python
from bst import BST

arvore = BST()

# Inserir elementos de forma balanceada
arvore.insert(50)
arvore.insert(30)
arvore.insert(70)
arvore.insert(20)
arvore.insert(40)
arvore.insert(60)
arvore.insert(80)

print(f"Elementos em ordem: {arvore.inorder()}")
# [20, 30, 40, 50, 60, 70, 80]

print(f"Altura da árvore: {arvore.height()}")  # 3
print(f"Comparações realizadas: {arvore.comparisons}")
```

**Estrutura da árvore:**
```
        50
       /  \
     30    70
    / \   / \
   20 40 60 80
```

**Explicação:**
- 50 é a raiz
- 30 < 50 → vai para esquerda
- 70 > 50 → vai para direita
- 20 < 30 → vai para esquerda de 30
- 40 está entre 30 e 50 → vai para direita de 30
- E assim por diante...

---

### Exemplo 3: Inserção em Ordem Crescente (Pior Caso)

```python
from bst import BST

arvore = BST()

# Inserir em ordem crescente
elementos = [10, 20, 30, 40, 50]

for elem in elementos:
    arvore.insert(elem)

print(f"Elementos: {arvore.inorder()}")  # [10, 20, 30, 40, 50]
print(f"Altura: {arvore.height()}")      # 5 (degenerada!)
```

**Estrutura (degenerada - vira lista):**
```
10
 \
  20
   \
    30
     \
      40
       \
        50
```

**Explicação:**
- BST não faz balanceamento automático
- Inserir em ordem crescente cria uma "lista encadeada"
- Altura = número de elementos (pior caso)
- Desempenho cai para O(n) em vez de O(log n)

---

### Exemplo 4: Inserção em Ordem Decrescente

```python
from bst import BST

arvore = BST()

# Inserir em ordem decrescente
elementos = [50, 40, 30, 20, 10]

for elem in elementos:
    arvore.insert(elem)

print(f"Elementos: {arvore.inorder()}")  # [10, 20, 30, 40, 50]
print(f"Altura: {arvore.height()}")      # 5
```

**Estrutura (degenerada à esquerda):**
```
        50
       /
      40
     /
    30
   /
  20
 /
10
```

**Explicação:**
- Todos os elementos vão para a esquerda
- Também cria uma estrutura degenerada
- Altura máxima = n

---

### Exemplo 5: Tentativa de Inserir Duplicados

```python
from bst import BST

arvore = BST()

arvore.insert(50)
arvore.insert(30)
arvore.insert(50)  # Duplicado - não insere
arvore.insert(30)  # Duplicado - não insere

print(f"Elementos: {arvore.inorder()}")  # [30, 50]
print(f"Quantidade: {len(arvore.inorder())}")  # 2
```

**Explicação:**
- BST não permite valores duplicados
- Ao tentar inserir um valor existente, a função retorna sem inserir
- A árvore mantém apenas valores únicos

---

## 🔍 Busca de Elementos

### Exemplo 1: Busca Básica

```python
from bst import BST

arvore = BST()
elementos = [50, 30, 70, 20, 40, 60, 80]

for elem in elementos:
    arvore.insert(elem)

# Resetar contador antes de buscar
arvore.reset_metrics()

# Buscar elementos existentes
print(f"Buscar 40: {arvore.search(40)}")  # True
print(f"Comparações: {arvore.comparisons}")

arvore.reset_metrics()
print(f"Buscar 100: {arvore.search(100)}")  # False
print(f"Comparações: {arvore.comparisons}")
```

**Estrutura:**
```
        50
       /  \
     30    70
    / \   / \
   20 40 60 80
```

**Caminho para buscar 40:**
1. Compara com 50 → 40 < 50, vai para esquerda
2. Compara com 30 → 40 > 30, vai para direita
3. Compara com 40 → encontrou! (3 comparações)

**Caminho para buscar 100:**
1. Compara com 50 → 100 > 50, vai para direita
2. Compara com 70 → 100 > 70, vai para direita
3. Compara com 80 → 100 > 80, vai para direita
4. Chegou em None → não encontrou (3 comparações)

---

### Exemplo 2: Comparando Desempenho de Busca

```python
from bst import BST

# Árvore balanceada
arvore_balanceada = BST()
arvore_balanceada.insert(50)
arvore_balanceada.insert(30)
arvore_balanceada.insert(70)
arvore_balanceada.insert(20)
arvore_balanceada.insert(40)
arvore_balanceada.insert(60)
arvore_balanceada.insert(80)

# Árvore degenerada
arvore_degenerada = BST()
for i in range(10, 80, 10):
    arvore_degenerada.insert(i)

# Buscar o último elemento em ambas
arvore_balanceada.reset_metrics()
arvore_balanceada.search(80)
print(f"Comparações (balanceada): {arvore_balanceada.comparisons}")  # ~3

arvore_degenerada.reset_metrics()
arvore_degenerada.search(70)
print(f"Comparações (degenerada): {arvore_degenerada.comparisons}")  # 7
```

**Explicação:**
- Árvore balanceada: busca em O(log n)
- Árvore degenerada: busca em O(n)
- A ordem de inserção afeta drasticamente o desempenho

---

## ❌ Remoção de Elementos

### Exemplo 1: Remover Folha (Nó sem Filhos)

```python
from bst import BST

arvore = BST()
arvore.insert(50)
arvore.insert(30)
arvore.insert(70)
arvore.insert(20)
arvore.insert(40)

print(f"Antes: {arvore.inorder()}")  # [20, 30, 40, 50, 70]

arvore.remove(20)  # Remove folha

print(f"Depois: {arvore.inorder()}")  # [30, 40, 50, 70]
```

**Antes:**
```
    50
   /  \
  30   70
 / \
20 40
```

**Depois:**
```
    50
   /  \
  30   70
   \
   40
```

**Explicação:**
- Nó 20 é uma folha (sem filhos)
- Simplesmente remove o nó
- Ajusta o ponteiro do pai (30.left = None)

---

### Exemplo 2: Remover Nó com Um Filho

```python
from bst import BST

arvore = BST()
arvore.insert(50)
arvore.insert(30)
arvore.insert(70)
arvore.insert(60)

print(f"Antes: {arvore.inorder()}")  # [30, 50, 60, 70]

arvore.remove(70)  # Remove nó com um filho

print(f"Depois: {arvore.inorder()}")  # [30, 50, 60]
```

**Antes:**
```
    50
   /  \
  30   70
      /
     60
```

**Depois:**
```
    50
   /  \
  30   60
```

**Explicação:**
- Nó 70 tem apenas um filho (60)
- Remove 70 e coloca 60 no lugar
- O filho "sobe" para a posição do pai

---

### Exemplo 3: Remover Nó com Dois Filhos

```python
from bst import BST

arvore = BST()
elementos = [50, 30, 70, 20, 40, 60, 80]

for elem in elementos:
    arvore.insert(elem)

print(f"Antes: {arvore.inorder()}")  # [20, 30, 40, 50, 60, 70, 80]

arvore.remove(30)  # Remove nó com dois filhos

print(f"Depois: {arvore.inorder()}")  # [20, 40, 50, 60, 70, 80]
```

**Antes:**
```
        50
       /  \
     30    70
    / \   / \
   20 40 60 80
```

**Depois:**
```
        50
       /  \
     40    70
    /     / \
   20    60 80
```

**Explicação:**
- Nó 30 tem dois filhos (20 e 40)
- Encontra o sucessor: menor valor da subárvore direita = 40
- Substitui 30 por 40
- Remove o nó 40 original (que tinha no máximo um filho)

---

### Exemplo 4: Remover a Raiz

```python
from bst import BST

arvore = BST()
elementos = [50, 30, 70, 20, 40, 60, 80]

for elem in elementos:
    arvore.insert(elem)

print(f"Raiz antes: {arvore.root.key}")  # 50
print(f"Antes: {arvore.inorder()}")

arvore.remove(50)  # Remove a raiz

print(f"Nova raiz: {arvore.root.key}")  # 60
print(f"Depois: {arvore.inorder()}")  # [20, 30, 40, 60, 70, 80]
```

**Antes:**
```
        50
       /  \
     30    70
    / \   / \
   20 40 60 80
```

**Depois:**
```
        60
       /  \
     30    70
    / \     \
   20 40    80
```

**Explicação:**
- Raiz 50 tem dois filhos
- Sucessor = 60 (menor da subárvore direita)
- 60 vira a nova raiz
- Estrutura mantém propriedades da BST

---

## 📚 Percursos da Árvore

```python
from bst import BST

arvore = BST()
elementos = [50, 30, 70, 20, 40, 60, 80]

for elem in elementos:
    arvore.insert(elem)

print("=== Percursos da Árvore ===\n")

# In-order (esquerda → raiz → direita)
print(f"In-order: {arvore.inorder()}")
# [20, 30, 40, 50, 60, 70, 80] - ORDENADO!

# Pre-order (raiz → esquerda → direita)
print(f"Pre-order: {arvore.preorder()}")
# [50, 30, 20, 40, 70, 60, 80]

# Post-order (esquerda → direita → raiz)
print(f"Post-order: {arvore.postorder()}")
# [20, 40, 30, 60, 80, 70, 50]
```

**Estrutura:**
```
        50
       /  \
     30    70
    / \   / \
   20 40 60 80
```

### Explicação dos Percursos

**In-order (em ordem):**
- Visita: esquerda → raiz → direita
- Resultado: valores em ordem crescente
- Caminho: 20 → 30 → 40 → 50 → 60 → 70 → 80
- **Uso:** Listar elementos ordenados

**Pre-order (pré-ordem):**
- Visita: raiz → esquerda → direita
- Resultado: raiz primeiro, depois subárvores
- Caminho: 50 → 30 → 20 → 40 → 70 → 60 → 80
- **Uso:** Copiar/serializar árvore, expressões prefixas

**Post-order (pós-ordem):**
- Visita: esquerda → direita → raiz
- Resultado: raiz por último
- Caminho: 20 → 40 → 30 → 60 → 80 → 70 → 50
- **Uso:** Deletar árvore, expressões pós-fixas

---

## 📐 Altura da Árvore

### Exemplo 1: Altura em Diferentes Configurações

```python
from bst import BST

# Árvore vazia
arvore1 = BST()
print(f"Altura (vazia): {arvore1.height()}")  # 0

# Árvore com 1 nó
arvore2 = BST()
arvore2.insert(50)
print(f"Altura (1 nó): {arvore2.height()}")  # 1

# Árvore balanceada
arvore3 = BST()
for elem in [50, 30, 70, 20, 40, 60, 80]:
    arvore3.insert(elem)
print(f"Altura (balanceada): {arvore3.height()}")  # 3

# Árvore degenerada
arvore4 = BST()
for elem in [10, 20, 30, 40, 50]:
    arvore4.insert(elem)
print(f"Altura (degenerada): {arvore4.height()}")  # 5
```

**Comparação visual:**

Balanceada (altura 3):
```
        50
       /  \
     30    70
    / \   / \
   20 40 60 80
```

Degenerada (altura 5):
```
10
 \
  20
   \
    30
     \
      40
       \
        50
```

**Explicação:**
- Altura = maior distância da raiz até uma folha
- Árvore balanceada: altura ≈ log₂(n)
- Árvore degenerada: altura = n
- BST não garante balanceamento

---

## 🔁 Métricas de Desempenho

```python
from bst import BST

arvore = BST()

# Inserir elementos
print("=== Inserindo elementos ===")
elementos = [50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 45]

for elem in elementos:
    arvore.insert(elem)

print(f"Total de comparações na inserção: {arvore.comparisons}")

# Resetar e fazer buscas
print("\n=== Buscando elementos ===")
arvore.reset_metrics()

buscas = [10, 50, 80, 100, 25]
for valor in buscas:
    encontrou = arvore.search(valor)
    print(f"Buscar {valor}: {encontrou}")

print(f"Total de comparações nas buscas: {arvore.comparisons}")

# Resetar e fazer remoções
print("\n=== Removendo elementos ===")
arvore.reset_metrics()

arvore.remove(20)
arvore.remove(70)

print(f"Total de comparações nas remoções: {arvore.comparisons}")
print(f"Elementos restantes: {arvore.inorder()}")
```

**Explicação:**
- `comparisons`: conta cada comparação de chaves
- `reset_metrics()`: zera o contador para nova medição
- Útil para:
  - Analisar desempenho
  - Comparar com outras estruturas (AVL, RBT)
  - Identificar casos problemáticos

---

## 🎯 Exemplo Completo: Sistema de Inventário

```python
from bst import BST

# Criar árvore para IDs de produtos
inventario = BST()

print("=== Sistema de Inventário ===\n")

# Adicionar produtos (por ID)
produtos = [500, 300, 700, 200, 400, 600, 800, 150, 250]

print("Adicionando produtos:")
for id_produto in produtos:
    inventario.insert(id_produto)
    print(f"  Produto ID {id_produto} adicionado")

print(f"\nTotal de produtos: {len(inventario.inorder())}")
print(f"Altura do inventário: {inventario.height()}")

# Listar produtos em ordem
print(f"\n=== Produtos em ordem de ID ===")
print(inventario.inorder())

# Buscar produtos específicos
print(f"\n=== Verificando estoque ===")
inventario.reset_metrics()

verificar = [200, 500, 999]
for id_prod in verificar:
    existe = inventario.search(id_prod)
    status = "Em estoque" if existe else "Não encontrado"
    print(f"Produto {id_prod}: {status}")

print(f"Comparações realizadas: {inventario.comparisons}")

# Remover produtos vendidos
print(f"\n=== Removendo produtos vendidos ===")
vendidos = [150, 400, 700]

for id_prod in vendidos:
    inventario.remove(id_prod)
    print(f"  Produto {id_prod} removido")

print(f"\nProdutos restantes: {inventario.inorder()}")
print(f"Total restante: {len(inventario.inorder())}")

# Estatísticas
print(f"\n=== Estatísticas ===")
ids = inventario.inorder()
print(f"Menor ID: {min(ids)}")
print(f"Maior ID: {max(ids)}")
print(f"Altura da árvore: {inventario.height()}")
```

**Saída esperada:**
```
=== Sistema de Inventário ===

Adicionando produtos:
  Produto ID 500 adicionado
  Produto ID 300 adicionado
  Produto ID 700 adicionado
  Produto ID 200 adicionado
  Produto ID 400 adicionado
  Produto ID 600 adicionado
  Produto ID 800 adicionado
  Produto ID 150 adicionado
  Produto ID 250 adicionado

Total de produtos: 9
Altura do inventário: 4

=== Produtos em ordem de ID ===
[150, 200, 250, 300, 400, 500, 600, 700, 800]

=== Verificando estoque ===
Produto 200: Em estoque
Produto 500: Em estoque
Produto 999: Não encontrado
Comparações realizadas: 7

=== Removendo produtos vendidos ===
  Produto 150 removido
  Produto 400 removido
  Produto 700 removido

Produtos restantes: [200, 250, 300, 500, 600, 800]
Total restante: 6

=== Estatísticas ===
Menor ID: 200
Maior ID: 800
Altura da árvore: 4
```

---

## 🧪 Testando Casos Especiais

### Caso 1: Remover de Árvore Vazia

```python
from bst import BST

arvore = BST()
arvore.remove(50)  # Não faz nada

print(f"Elementos: {arvore.inorder()}")  # []
print(f"Altura: {arvore.height()}")      # 0
```

### Caso 2: Buscar em Árvore Vazia

```python
from bst import BST

arvore = BST()
resultado = arvore.search(50)

print(f"Encontrou: {resultado}")  # False
```

### Caso 3: Remover Todos os Elementos

```python
from bst import BST

arvore = BST()
elementos = [50, 30, 70]

for elem in elementos:
    arvore.insert(elem)

print(f"Antes: {arvore.inorder()}")  # [30, 50, 70]

# Remover todos
for elem in elementos:
    arvore.remove(elem)

print(f"Depois: {arvore.inorder()}")  # []
print(f"Raiz: {arvore.root}")         # None
print(f"Altura: {arvore.height()}")   # 0
```

### Caso 4: Árvore com Muitos Elementos

```python
from bst import BST
import random

arvore = BST()

# Inserir 1000 elementos aleatórios
elementos = random.sample(range(1, 10001), 1000)

for elem in elementos:
    arvore.insert(elem)

print(f"Elementos inseridos: {len(arvore.inorder())}")
print(f"Altura da árvore: {arvore.height()}")
print(f"Comparações totais: {arvore.comparisons}")

# Buscar alguns elementos
arvore.reset_metrics()
for _ in range(10):
    arvore.search(random.choice(elementos))

print(f"Média de comparações por busca: {arvore.comparisons / 10:.2f}")
```

---

## 📊 Comparação: BST vs Ordem de Inserção

```python
from bst import BST

# Cenário 1: Inserção aleatória (melhor caso)
arvore1 = BST()
aleatorio = [50, 30, 70, 20, 40, 60, 80]
for elem in aleatorio:
    arvore1.insert(elem)

print("=== Inserção Aleatória ===")
print(f"Elementos: {aleatorio}")
print(f"Altura: {arvore1.height()}")  # 3
print(f"Comparações: {arvore1.comparisons}")

# Cenário 2: Inserção ordenada (pior caso)
arvore2 = BST()
ordenado = [20, 30, 40, 50, 60, 70, 80]
for elem in ordenado:
    arvore2.insert(elem)

print("\n=== Inserção Ordenada ===")
print(f"Elementos: {ordenado}")
print(f"Altura: {arvore2.height()}")  # 7
print(f"Comparações: {arvore2.comparisons}")

# Comparação de busca
arvore1.reset_metrics()
arvore1.search(80)
comp1 = arvore1.comparisons

arvore2.reset_metrics()
arvore2.search(80)
comp2 = arvore2.comparisons

print(f"\n=== Buscar elemento 80 ===")
print(f"Comparações (aleatória): {comp1}")
print(f"Comparações (ordenada): {comp2}")
```

---

## ✅ Resumo das Operações

| Operação | Melhor Caso | Pior Caso | Exemplo |
|----------|-------------|-----------|---------|
| `insert(key)` | O(log n) | O(n) | `arvore.insert(50)` |
| `search(key)` | O(log n) | O(n) | `arvore.search(50)` |
| `remove(key)` | O(log n) | O(n) | `arvore.remove(50)` |
| `inorder()` | O(n) | O(n) | `arvore.inorder()` |
| `preorder()` | O(n) | O(n) | `arvore.preorder()` |
| `postorder()` | O(n) | O(n) | `arvore.postorder()` |
| `height()` | O(n) | O(n) | `arvore.height()` |
| `reset_metrics()` | O(1) | O(1) | `arvore.reset_metrics()` |

---

## 🎓 Conclusão

A BST é uma estrutura fundamental que:
- ✅ Implementa busca binária em árvore
- ✅ Mantém elementos ordenados
- ✅ Oferece operações básicas eficientes (quando balanceada)
- ⚠️ Pode degenerar em lista (quando desbalanceada)
- ⚠️ Não faz balanceamento automático

**Quando usar BST:**
- Dados inseridos aleatoriamente
- Implementação simples necessária
- Não há requisito rígido de desempenho

**Quando NÃO usar BST:**
- Dados ordenados ou quase ordenados
- Necessidade de garantia de O(log n)
- Muitas operações críticas de desempenho

**Alternativas balanceadas:**
- AVL (balanceamento rígido)
- Red-Black Tree (balanceamento flexível)
