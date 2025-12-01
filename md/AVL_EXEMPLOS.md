# 🌳 Árvore AVL - Exemplos Práticos com Código

Este documento apresenta exemplos práticos de uso da implementação da Árvore AVL, demonstrando cada funcionalidade com código executável e explicações detalhadas.

---

## 📦 Importação e Criação da Árvore

```python
from avl import AVL

# Criar uma nova árvore AVL vazia
arvore = AVL()
print(f"Árvore criada. Raiz: {arvore.root}")  # None
print(f"Altura inicial: {arvore.height()}")    # 0
```

**O que acontece:**
- Uma árvore vazia é criada
- A raiz é `None`
- A altura é 0

---

## 📥 Inserção de Elementos

### Exemplo 1: Inserção Simples (sem rotações)

```python
from avl import AVL

arvore = AVL()

# Inserir elementos que não causam desbalanceamento
arvore.insert(10)
arvore.insert(5)
arvore.insert(15)

print(f"Elementos inseridos: {arvore.inorder()}")  # [5, 10, 15]
print(f"Altura da árvore: {arvore.height()}")      # 2
print(f"Comparações: {arvore.comparisons}")
print(f"Rotações: {arvore.rotations}")             # 0
```

**Estrutura da árvore:**
```
    10
   /  \
  5    15
```

**Explicação:**
- Primeiro insere 10 (vira raiz)
- 5 é menor que 10 → vai para esquerda
- 15 é maior que 10 → vai para direita
- Árvore está balanceada, não precisa de rotações

---

### Exemplo 2: Rotação Simples à Direita (Left-Left)

```python
from avl import AVL

arvore = AVL()

# Inserir em ordem decrescente causa desbalanceamento
arvore.insert(30)
arvore.insert(20)
arvore.insert(10)  # Aqui ocorre a rotação

print(f"Elementos: {arvore.inorder()}")      # [10, 20, 30]
print(f"Raiz após rotação: {arvore.root.key}")  # 20
print(f"Rotações realizadas: {arvore.rotations}")  # 1
```

**Antes da rotação (desbalanceada):**
```
    30
   /
  20
 /
10
```

**Depois da rotação à direita:**
```
    20
   /  \
  10   30
```

**Explicação:**
- Ao inserir 10, o nó 30 fica com fator de balanceamento = 2
- Caso Left-Left detectado
- Rotação à direita no nó 30
- O nó 20 sobe e vira a nova raiz

---

### Exemplo 3: Rotação Simples à Esquerda (Right-Right)

```python
from avl import AVL

arvore = AVL()

# Inserir em ordem crescente
arvore.insert(10)
arvore.insert(20)
arvore.insert(30)  # Aqui ocorre a rotação

print(f"Elementos: {arvore.inorder()}")      # [10, 20, 30]
print(f"Raiz após rotação: {arvore.root.key}")  # 20
print(f"Rotações realizadas: {arvore.rotations}")  # 1
```

**Antes da rotação (desbalanceada):**
```
10
 \
  20
   \
    30
```

**Depois da rotação à esquerda:**
```
    20
   /  \
  10   30
```

**Explicação:**
- Ao inserir 30, o nó 10 fica com fator de balanceamento = -2
- Caso Right-Right detectado
- Rotação à esquerda no nó 10
- O nó 20 sobe e vira a nova raiz

---

### Exemplo 4: Rotação Dupla Esquerda-Direita (Left-Right)

```python
from avl import AVL

arvore = AVL()

# Inserir causando caso Left-Right
arvore.insert(30)
arvore.insert(10)
arvore.insert(20)  # Aqui ocorrem 2 rotações

print(f"Elementos: {arvore.inorder()}")      # [10, 20, 30]
print(f"Raiz após rotações: {arvore.root.key}")  # 20
print(f"Rotações realizadas: {arvore.rotations}")  # 2
```

**Antes das rotações:**
```
  30
 /
10
 \
  20
```

**Após rotação à esquerda em 10:**
```
  30
 /
20
/
10
```

**Após rotação à direita em 30:**
```
    20
   /  \
  10   30
```

**Explicação:**
- Caso Left-Right detectado
- Primeira rotação: esquerda no filho esquerdo (10)
- Segunda rotação: direita no nó desbalanceado (30)
- Resultado: árvore balanceada com 20 na raiz

---

### Exemplo 5: Rotação Dupla Direita-Esquerda (Right-Left)

```python
from avl import AVL

arvore = AVL()

# Inserir causando caso Right-Left
arvore.insert(10)
arvore.insert(30)
arvore.insert(20)  # Aqui ocorrem 2 rotações

print(f"Elementos: {arvore.inorder()}")      # [10, 20, 30]
print(f"Raiz após rotações: {arvore.root.key}")  # 20
print(f"Rotações realizadas: {arvore.rotations}")  # 2
```

**Antes das rotações:**
```
10
 \
  30
 /
20
```

**Após rotação à direita em 30:**
```
10
 \
  20
   \
    30
```

**Após rotação à esquerda em 10:**
```
    20
   /  \
  10   30
```

**Explicação:**
- Caso Right-Left detectado
- Primeira rotação: direita no filho direito (30)
- Segunda rotação: esquerda no nó desbalanceado (10)
- Resultado: árvore balanceada

---

## 🔍 Busca de Elementos

```python
from avl import AVL

arvore = AVL()
elementos = [50, 30, 70, 20, 40, 60, 80]

for elem in elementos:
    arvore.insert(elem)

# Resetar métricas antes de buscar
arvore.reset_metrics()

# Buscar elementos existentes
print(f"Buscar 40: {arvore.search(40)}")  # True
print(f"Comparações: {arvore.comparisons}")

arvore.reset_metrics()
print(f"Buscar 100: {arvore.search(100)}")  # False
print(f"Comparações: {arvore.comparisons}")

# Buscar raiz (mais rápido)
arvore.reset_metrics()
print(f"Buscar 50: {arvore.search(50)}")  # True
print(f"Comparações: {arvore.comparisons}")  # 1
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
- A busca segue o caminho da BST
- Árvore balanceada garante O(log n) comparações
- Buscar a raiz é mais rápido (1 comparação)
- Elementos inexistentes percorrem até folhas

---

## ❌ Remoção de Elementos

### Exemplo 1: Remover Folha

```python
from avl import AVL

arvore = AVL()
arvore.insert(50)
arvore.insert(30)
arvore.insert(70)
arvore.insert(20)

print(f"Antes: {arvore.inorder()}")  # [20, 30, 50, 70]

arvore.remove(20)  # Remove folha

print(f"Depois: {arvore.inorder()}")  # [30, 50, 70]
print(f"Altura: {arvore.height()}")   # 2
```

**Antes:**
```
    50
   /  \
  30   70
 /
20
```

**Depois:**
```
    50
   /  \
  30   70
```

---

### Exemplo 2: Remover Nó com Um Filho

```python
from avl import AVL

arvore = AVL()
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

---

### Exemplo 3: Remover Nó com Dois Filhos

```python
from avl import AVL

arvore = AVL()
elementos = [50, 30, 70, 20, 40, 60, 80]

for elem in elementos:
    arvore.insert(elem)

print(f"Antes: {arvore.inorder()}")  # [20, 30, 40, 50, 60, 70, 80]

arvore.remove(50)  # Remove raiz (tem dois filhos)

print(f"Depois: {arvore.inorder()}")  # [20, 30, 40, 60, 70, 80]
print(f"Nova raiz: {arvore.root.key}")  # 60 (sucessor)
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
- Nó 50 tem dois filhos
- Encontra o sucessor (menor valor da subárvore direita) = 60
- Substitui 50 por 60
- Remove o nó 60 original
- Rebalancea se necessário

---

## 📚 Percursos da Árvore

```python
from avl import AVL

arvore = AVL()
elementos = [50, 30, 70, 20, 40, 60, 80]

for elem in elementos:
    arvore.insert(elem)

# In-order (esquerda → raiz → direita) - ORDENADO
print(f"In-order: {arvore.inorder()}")
# [20, 30, 40, 50, 60, 70, 80]

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

**Explicação dos percursos:**

**In-order:** Visita em ordem crescente
- 20 → 30 → 40 → 50 → 60 → 70 → 80

**Pre-order:** Visita raiz primeiro (útil para copiar árvore)
- 50 → 30 → 20 → 40 → 70 → 60 → 80

**Post-order:** Visita raiz por último (útil para deletar árvore)
- 20 → 40 → 30 → 60 → 80 → 70 → 50

---

## 📏 Altura e Balanceamento

```python
from avl import AVL

arvore = AVL()

# Árvore vazia
print(f"Altura (vazia): {arvore.height()}")  # 0

# Inserir um elemento
arvore.insert(10)
print(f"Altura (1 nó): {arvore.height()}")  # 1

# Inserir mais elementos
arvore.insert(5)
arvore.insert(15)
print(f"Altura (3 nós): {arvore.height()}")  # 2

# Inserir mais elementos (árvore cresce)
arvore.insert(3)
arvore.insert(7)
arvore.insert(12)
arvore.insert(17)
print(f"Altura (7 nós): {arvore.height()}")  # 3

# Verificar balanceamento
print(f"Elementos: {arvore.inorder()}")
# [3, 5, 7, 10, 12, 15, 17]
```

**Estrutura final (balanceada):**
```
        10
       /  \
      5    15
     / \   / \
    3  7  12 17
```

**Explicação:**
- AVL mantém altura O(log n)
- Com 7 nós, altura máxima = 3
- Árvore desbalanceada poderia ter altura 7
- Balanceamento garante eficiência

---

## 🔁 Métricas de Desempenho

```python
from avl import AVL

arvore = AVL()

# Inserir elementos
elementos = [50, 30, 70, 20, 40, 60, 80, 10, 25]

for elem in elementos:
    arvore.insert(elem)

print(f"Total de comparações na inserção: {arvore.comparisons}")
print(f"Total de rotações: {arvore.rotations}")

# Resetar métricas
arvore.reset_metrics()

# Fazer buscas
arvore.search(10)
arvore.search(50)
arvore.search(80)
arvore.search(100)  # Não existe

print(f"Comparações nas buscas: {arvore.comparisons}")
print(f"Rotações nas buscas: {arvore.rotations}")  # 0

# Resetar novamente
arvore.reset_metrics()

# Fazer remoções
arvore.remove(20)
arvore.remove(70)

print(f"Comparações nas remoções: {arvore.comparisons}")
print(f"Rotações nas remoções: {arvore.rotations}")
```

**Explicação:**
- `comparisons`: conta quantas vezes compara chaves
- `rotations`: conta quantas rotações foram feitas
- `reset_metrics()`: zera contadores para nova medição
- Útil para análise de desempenho e comparação com outras estruturas

---

## 🎯 Exemplo Completo: Sistema de Notas

```python
from avl import AVL

# Criar árvore para armazenar notas de alunos
notas = AVL()

# Inserir notas
print("=== Inserindo notas ===")
lista_notas = [75, 60, 85, 50, 70, 80, 90, 45, 55]

for nota in lista_notas:
    notas.insert(nota)
    print(f"Nota {nota} inserida")

print(f"\nTotal de rotações: {notas.rotations}")
print(f"Altura da árvore: {notas.height()}")

# Listar notas em ordem
print(f"\n=== Notas em ordem crescente ===")
print(notas.inorder())

# Buscar notas específicas
print(f"\n=== Buscando notas ===")
notas.reset_metrics()

buscar = [75, 90, 100]
for nota in buscar:
    encontrou = notas.search(nota)
    print(f"Nota {nota}: {'Encontrada' if encontrou else 'Não encontrada'}")

print(f"Total de comparações: {notas.comparisons}")

# Remover notas abaixo da média
print(f"\n=== Removendo notas abaixo de 60 ===")
notas.remove(50)
notas.remove(45)
notas.remove(55)

print(f"Notas restantes: {notas.inorder()}")
print(f"Nova altura: {notas.height()}")

# Estatísticas finais
print(f"\n=== Estatísticas ===")
print(f"Quantidade de notas: {len(notas.inorder())}")
print(f"Menor nota: {min(notas.inorder())}")
print(f"Maior nota: {max(notas.inorder())}")
```

**Saída esperada:**
```
=== Inserindo notas ===
Nota 75 inserida
Nota 60 inserida
Nota 85 inserida
Nota 50 inserida
Nota 70 inserida
Nota 80 inserida
Nota 90 inserida
Nota 45 inserida
Nota 55 inserida

Total de rotações: 2
Altura da árvore: 4

=== Notas em ordem crescente ===
[45, 50, 55, 60, 70, 75, 80, 85, 90]

=== Buscando notas ===
Nota 75: Encontrada
Nota 90: Encontrada
Nota 100: Não encontrada
Total de comparações: 9

=== Removendo notas abaixo de 60 ===
Notas restantes: [60, 70, 75, 80, 85, 90]
Nova altura: 3

=== Estatísticas ===
Quantidade de notas: 6
Menor nota: 60
Maior nota: 90
```

---

## 🧪 Testando Casos Extremos

### Inserção de Elementos Duplicados

```python
from avl import AVL

arvore = AVL()

arvore.insert(10)
arvore.insert(10)  # Duplicado - não insere
arvore.insert(10)  # Duplicado - não insere

print(f"Elementos: {arvore.inorder()}")  # [10]
print(f"Altura: {arvore.height()}")      # 1
```

### Árvore com Muitos Elementos

```python
from avl import AVL
import random

arvore = AVL()

# Inserir 100 elementos aleatórios
elementos = random.sample(range(1, 1001), 100)

for elem in elementos:
    arvore.insert(elem)

print(f"Elementos inseridos: {len(arvore.inorder())}")
print(f"Altura da árvore: {arvore.height()}")
print(f"Rotações realizadas: {arvore.rotations}")

# Altura teórica mínima: log2(100) ≈ 6.64
# AVL garante altura ≤ 1.44 * log2(n)
print(f"Altura máxima teórica AVL: {int(1.44 * 6.64)}")  # ≈ 9
```

---

## ✅ Resumo das Operações

| Operação | Complexidade | Exemplo |
|----------|--------------|---------|
| `insert(key)` | O(log n) | `arvore.insert(50)` |
| `search(key)` | O(log n) | `arvore.search(50)` |
| `remove(key)` | O(log n) | `arvore.remove(50)` |
| `inorder()` | O(n) | `arvore.inorder()` |
| `preorder()` | O(n) | `arvore.preorder()` |
| `postorder()` | O(n) | `arvore.postorder()` |
| `height()` | O(1) | `arvore.height()` |
| `reset_metrics()` | O(1) | `arvore.reset_metrics()` |

---

## 🎓 Conclusão

A implementação da Árvore AVL garante:
- ✅ Balanceamento automático
- ✅ Operações em O(log n)
- ✅ Altura controlada
- ✅ Métricas de desempenho
- ✅ Percursos completos

Use AVL quando precisar de:
- Muitas operações de busca
- Garantia de desempenho
- Dados inseridos aleatoriamente
