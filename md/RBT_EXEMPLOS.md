# 🔴⚫ Árvore Rubro-Negra (Red-Black Tree) - Exemplos Práticos com Código

Este documento apresenta exemplos práticos de uso da implementação da Árvore Rubro-Negra (RBT), demonstrando cada funcionalidade com código executável e explicações detalhadas.

---

## 📦 Importação e Criação da Árvore

```python
from rbt import RBT, RED, BLACK

# Criar uma nova árvore RBT vazia
arvore = RBT()

print(f"Raiz: {arvore.root.key}")  # None (nó sentinela)
print(f"Cor da raiz: {arvore.root.color}")  # False (BLACK)
print(f"Altura inicial: {arvore.height()}")  # 0
print(f"Comparações: {arvore.comparisons}")  # 0
print(f"Rotações: {arvore.rotations}")  # 0
```

**O que acontece:**
- Uma árvore vazia é criada
- A raiz aponta para o nó sentinela `nil` (sempre preto)
- Todos os contadores iniciam em 0

**Propriedades da RBT:**
1. Todo nó é vermelho ou preto
2. A raiz é sempre preta
3. Folhas (NIL) são pretas
4. Filhos de nós vermelhos são pretos
5. Todos os caminhos têm o mesmo número de nós pretos

---

## 📥 Inserção de Elementos

### Exemplo 1: Primeira Inserção (Criando a Raiz)

```python
from rbt import RBT

arvore = RBT()

# Primeira inserção
arvore.insert(50)

print(f"Raiz: {arvore.root.key}")  # 50
print(f"Cor da raiz: {'RED' if arvore.root.color else 'BLACK'}")  # BLACK
print(f"Altura: {arvore.height()}")  # 1
print(f"Rotações: {arvore.rotations}")  # 0
```

**Estrutura:**
```
50(B)
```
Legenda: (B) = Black, (R) = Red

**Explicação:**
- Primeiro nó inserido vira a raiz
- Inicialmente vermelho, mas `_fix_insert` força a raiz a ser preta
- Propriedade 2 mantida: raiz é preta

---

### Exemplo 2: Inserção Simples (Sem Rotações)

```python
from rbt import RBT

arvore = RBT()

# Inserir elementos
arvore.insert(50)
arvore.insert(30)
arvore.insert(70)

print(f"Elementos: {arvore.inorder()}")  # [30, 50, 70]
print(f"Rotações: {arvore.rotations}")  # 0
print(f"Altura: {arvore.height()}")  # 2
```

**Estrutura:**
```
     50(B)
    /    \
  30(R)  70(R)
```

**Explicação:**
- 50 é a raiz preta
- 30 e 70 são inseridos como vermelhos
- Não há violação (filhos da raiz podem ser vermelhos)
- Nenhuma rotação necessária

---

### Exemplo 3: Caso 1 - Tio Vermelho (Recoloração)

```python
from rbt import RBT

arvore = RBT()

# Inserir elementos que causam recoloração
arvore.insert(50)
arvore.insert(30)
arvore.insert(70)
arvore.insert(20)  # Aqui ocorre recoloração

print(f"Elementos: {arvore.inorder()}")  # [20, 30, 50, 70]
print(f"Rotações: {arvore.rotations}")  # 0 (apenas recoloração)
```

**Antes de inserir 20:**
```
     50(B)
    /    \
  30(R)  70(R)
```

**Depois de inserir 20:**
```
     50(B)
    /    \
  30(B)  70(B)
  /
20(R)
```

**Explicação:**
- 20 é inserido como filho vermelho de 30 (vermelho)
- Violação: dois vermelhos seguidos
- Tio (70) é vermelho → Caso 1
- Solução: recolore pai (30) e tio (70) para preto, avô (50) para vermelho
- Raiz volta a ser preta
- Sem rotações!

---

### Exemplo 4: Caso 2 e 3 - Rotação Simples à Direita

```python
from rbt import RBT

arvore = RBT()

# Inserir em ordem decrescente
arvore.insert(50)
arvore.insert(30)
arvore.insert(20)  # Aqui ocorre rotação

print(f"Elementos: {arvore.inorder()}")  # [20, 30, 50]
print(f"Raiz: {arvore.root.key}")  # 30
print(f"Rotações: {arvore.rotations}")  # 1
```

**Antes da rotação:**
```
     50(B)
    /
  30(R)
  /
20(R)
```

**Depois da rotação:**
```
     30(B)
    /    \
  20(R)  50(R)
```

**Explicação:**
- 20 é inserido como vermelho
- Violação: 20(R) → 30(R) (dois vermelhos)
- Tio é preto (nil) → Caso 3 (Left-Left)
- Solução: rotação à direita em 50, recoloração
- 30 vira raiz preta, 20 e 50 ficam vermelhos

---

### Exemplo 5: Caso 2 e 3 - Rotação Simples à Esquerda

```python
from rbt import RBT

arvore = RBT()

# Inserir em ordem crescente
arvore.insert(50)
arvore.insert(70)
arvore.insert(80)  # Aqui ocorre rotação

print(f"Elementos: {arvore.inorder()}")  # [50, 70, 80]
print(f"Raiz: {arvore.root.key}")  # 70
print(f"Rotações: {arvore.rotations}")  # 1
```

**Antes da rotação:**
```
50(B)
   \
   70(R)
      \
      80(R)
```

**Depois da rotação:**
```
     70(B)
    /    \
  50(R)  80(R)
```

**Explicação:**
- 80 é inserido como vermelho
- Violação: 70(R) → 80(R)
- Tio é preto → Caso 3 (Right-Right)
- Solução: rotação à esquerda em 50, recoloração
- 70 vira raiz preta

---

### Exemplo 6: Rotação Dupla (Left-Right)

```python
from rbt import RBT

arvore = RBT()

# Inserir causando rotação dupla
arvore.insert(50)
arvore.insert(30)
arvore.insert(40)  # Aqui ocorrem rotações

print(f"Elementos: {arvore.inorder()}")  # [30, 40, 50]
print(f"Raiz: {arvore.root.key}")  # 40
print(f"Rotações: {arvore.rotations}")  # 2
```

**Antes das rotações:**
```
     50(B)
    /
  30(R)
     \
     40(R)
```

**Após rotação à esquerda em 30:**
```
     50(B)
    /
  40(R)
  /
30(R)
```

**Após rotação à direita em 50:**
```
     40(B)
    /    \
  30(R)  50(R)
```

**Explicação:**
- Caso Left-Right detectado
- Primeira rotação: esquerda em 30 (transforma em Left-Left)
- Segunda rotação: direita em 50
- Recoloração: 40 fica preto, 30 e 50 ficam vermelhos

---

### Exemplo 7: Inserção de Múltiplos Elementos

```python
from rbt import RBT

arvore = RBT()

# Inserir vários elementos
elementos = [50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 45]

for elem in elementos:
    arvore.insert(elem)

print(f"Elementos em ordem: {arvore.inorder()}")
print(f"Altura da árvore: {arvore.height()}")
print(f"Total de rotações: {arvore.rotations}")
print(f"Total de comparações: {arvore.comparisons}")
```

**Estrutura final (simplificada):**
```
         40(B)
       /      \
     30(R)    60(B)
    /   \    /   \
  20(B) 35(B) 50(R) 70(R)
  /  \           \
10(R) 25(R)      80(B)
      /
    45(R)
```

**Explicação:**
- RBT mantém balanceamento através de rotações e recolorações
- Altura permanece O(log n)
- Menos rotações que AVL em média
- Propriedades rubro-negras mantidas

---

## 🔍 Busca de Elementos

```python
from rbt import RBT

arvore = RBT()
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

# Buscar raiz
arvore.reset_metrics()
print(f"Buscar raiz: {arvore.search(arvore.root.key)}")  # True
print(f"Comparações: {arvore.comparisons}")  # 1
```

**Estrutura:**
```
         40(B)
       /      \
     30(R)    60(B)
    /        /   \
  20(B)   50(R)  70(R)
                    \
                   80(B)
```

**Explicação:**
- Busca funciona como BST normal
- Ignora as cores dos nós
- Balanceamento garante O(log n) comparações
- Usa nó sentinela `nil` como condição de parada

---

## ❌ Remoção de Elementos

### Exemplo 1: Remover Folha

```python
from rbt import RBT

arvore = RBT()
arvore.insert(50)
arvore.insert(30)
arvore.insert(70)
arvore.insert(20)

print(f"Antes: {arvore.inorder()}")  # [20, 30, 50, 70]

arvore.remove(20)  # Remove folha

print(f"Depois: {arvore.inorder()}")  # [30, 50, 70]
```

**Antes:**
```
     50(B)
    /    \
  30(R)  70(R)
  /
20(B)
```

**Depois:**
```
     50(B)
    /    \
  30(R)  70(R)
```

**Explicação:**
- Remove nó folha 20
- Implementação simplificada (não faz fix-up completo)
- Pode violar propriedades em casos complexos

---

### Exemplo 2: Remover Nó com Um Filho

```python
from rbt import RBT

arvore = RBT()
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
     50(B)
    /    \
  30(R)  70(R)
         /
       60(B)
```

**Depois:**
```
     50(B)
    /    \
  30(R)  60(R)
```

---

### Exemplo 3: Remover Nó com Dois Filhos

```python
from rbt import RBT

arvore = RBT()
elementos = [50, 30, 70, 20, 40, 60, 80]

for elem in elementos:
    arvore.insert(elem)

print(f"Antes: {arvore.inorder()}")

arvore.remove(50)  # Remove nó com dois filhos

print(f"Depois: {arvore.inorder()}")
print(f"Nova raiz: {arvore.root.key}")
```

**Explicação:**
- Encontra o sucessor (menor da subárvore direita)
- Substitui o valor do nó
- Remove o sucessor
- **Nota:** Implementação simplificada, não faz fix-up completo de cores

---

## 📚 Percursos da Árvore

```python
from rbt import RBT

arvore = RBT()
elementos = [50, 30, 70, 20, 40, 60, 80]

for elem in elementos:
    arvore.insert(elem)

print("=== Percursos da Árvore RBT ===\n")

# In-order (esquerda → raiz → direita)
print(f"In-order: {arvore.inorder()}")
# [20, 30, 40, 50, 60, 70, 80] - ORDENADO!

# Pre-order (raiz → esquerda → direita)
print(f"Pre-order: {arvore.preorder()}")

# Post-order (esquerda → direita → raiz)
print(f"Post-order: {arvore.postorder()}")
```

**Estrutura (exemplo):**
```
         40(B)
       /      \
     30(R)    60(B)
    /        /   \
  20(B)   50(R)  70(R)
                    \
                   80(B)
```

**Explicação dos percursos:**

**In-order:** Retorna valores ordenados
- Útil para listar elementos em ordem crescente
- Ignora as cores

**Pre-order:** Raiz primeiro
- Útil para serializar/copiar a árvore
- Pode incluir informações de cor

**Post-order:** Raiz por último
- Útil para deletar a árvore com segurança

---

## 📐 Altura da Árvore

```python
from rbt import RBT

# Árvore vazia
arvore1 = RBT()
print(f"Altura (vazia): {arvore1.height()}")  # 0

# Árvore com 1 nó
arvore2 = RBT()
arvore2.insert(50)
print(f"Altura (1 nó): {arvore2.height()}")  # 1

# Árvore com vários nós
arvore3 = RBT()
for elem in [50, 30, 70, 20, 40, 60, 80, 10, 25]:
    arvore3.insert(elem)

print(f"Altura (9 nós): {arvore3.height()}")
print(f"Elementos: {arvore3.inorder()}")
```

**Explicação:**
- RBT garante altura ≤ 2 * log₂(n + 1)
- Mais flexível que AVL (permite pequenos desbalanceamentos)
- Menos rotações em média que AVL
- Altura ainda é O(log n)

---

## 🔁 Métricas de Desempenho

```python
from rbt import RBT

arvore = RBT()

print("=== Inserindo elementos ===")
elementos = [50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 45]

for elem in elementos:
    arvore.insert(elem)

print(f"Total de comparações na inserção: {arvore.comparisons}")
print(f"Total de rotações: {arvore.rotations}")

# Resetar e fazer buscas
print("\n=== Buscando elementos ===")
arvore.reset_metrics()

buscas = [10, 50, 80, 100, 25]
for valor in buscas:
    encontrou = arvore.search(valor)
    print(f"Buscar {valor}: {encontrou}")

print(f"Total de comparações nas buscas: {arvore.comparisons}")
print(f"Rotações nas buscas: {arvore.rotations}")  # 0

# Resetar e fazer remoções
print("\n=== Removendo elementos ===")
arvore.reset_metrics()

arvore.remove(20)
arvore.remove(70)

print(f"Elementos restantes: {arvore.inorder()}")
```

**Explicação:**
- `comparisons`: conta comparações de chaves
- `rotations`: conta rotações realizadas
- RBT geralmente faz menos rotações que AVL
- Útil para análise comparativa

---

## 🎯 Exemplo Completo: Sistema de Prioridades

```python
from rbt import RBT

# Criar árvore para gerenciar prioridades de tarefas
tarefas = RBT()

print("=== Sistema de Prioridades ===\n")

# Adicionar tarefas com prioridades (1-100)
prioridades = [50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 45]

print("Adicionando tarefas:")
for prioridade in prioridades:
    tarefas.insert(prioridade)
    print(f"  Tarefa com prioridade {prioridade} adicionada")

print(f"\nTotal de tarefas: {len(tarefas.inorder())}")
print(f"Altura da árvore: {tarefas.height()}")
print(f"Rotações realizadas: {tarefas.rotations}")

# Listar tarefas por prioridade
print(f"\n=== Tarefas por prioridade (crescente) ===")
print(tarefas.inorder())

# Buscar tarefas específicas
print(f"\n=== Verificando tarefas ===")
tarefas.reset_metrics()

verificar = [20, 50, 100]
for prioridade in verificar:
    existe = tarefas.search(prioridade)
    status = "Encontrada" if existe else "Não encontrada"
    print(f"Prioridade {prioridade}: {status}")

print(f"Comparações realizadas: {tarefas.comparisons}")

# Remover tarefas concluídas
print(f"\n=== Removendo tarefas concluídas ===")
concluidas = [10, 40, 70]

for prioridade in concluidas:
    tarefas.remove(prioridade)
    print(f"  Tarefa {prioridade} removida")

print(f"\nTarefas restantes: {tarefas.inorder()}")
print(f"Total restante: {len(tarefas.inorder())}")

# Estatísticas
print(f"\n=== Estatísticas ===")
prioridades_restantes = tarefas.inorder()
print(f"Menor prioridade: {min(prioridades_restantes)}")
print(f"Maior prioridade: {max(prioridades_restantes)}")
print(f"Altura da árvore: {tarefas.height()}")
```

**Saída esperada:**
```
=== Sistema de Prioridades ===

Adicionando tarefas:
  Tarefa com prioridade 50 adicionada
  Tarefa com prioridade 30 adicionada
  Tarefa com prioridade 70 adicionada
  ...

Total de tarefas: 11
Altura da árvore: 4
Rotações realizadas: 3

=== Tarefas por prioridade (crescente) ===
[10, 20, 25, 30, 35, 40, 45, 50, 60, 70, 80]

=== Verificando tarefas ===
Prioridade 20: Encontrada
Prioridade 50: Encontrada
Prioridade 100: Não encontrada
Comparações realizadas: 8

=== Removendo tarefas concluídas ===
  Tarefa 10 removida
  Tarefa 40 removida
  Tarefa 70 removida

Tarefas restantes: [20, 25, 30, 35, 45, 50, 60, 80]
Total restante: 8

=== Estatísticas ===
Menor prioridade: 20
Maior prioridade: 80
Altura da árvore: 4
```

---

## 🧪 Testando Propriedades da RBT

### Verificando Cores dos Nós

```python
from rbt import RBT, RED, BLACK

arvore = RBT()

# Inserir elementos
for elem in [50, 30, 70, 20, 40]:
    arvore.insert(elem)

# Função auxiliar para mostrar cores
def mostrar_arvore(node, nivel=0, prefixo="Raiz: "):
    if node != arvore.nil:
        cor = "RED" if node.color == RED else "BLACK"
        print("  " * nivel + prefixo + f"{node.key}({cor})")
        if node.left != arvore.nil or node.right != arvore.nil:
            mostrar_arvore(node.left, nivel + 1, "L--- ")
            mostrar_arvore(node.right, nivel + 1, "R--- ")

print("=== Estrutura da Árvore com Cores ===")
mostrar_arvore(arvore.root)
```

**Saída esperada:**
```
=== Estrutura da Árvore com Cores ===
Raiz: 50(BLACK)
  L--- 30(RED)
    L--- 20(BLACK)
    R--- 40(BLACK)
  R--- 70(BLACK)
```

---

## 📊 Comparação: RBT vs Inserção Ordenada

```python
from rbt import RBT

# Cenário 1: Inserção aleatória
arvore1 = RBT()
aleatorio = [50, 30, 70, 20, 40, 60, 80]
for elem in aleatorio:
    arvore1.insert(elem)

print("=== Inserção Aleatória ===")
print(f"Elementos: {aleatorio}")
print(f"Altura: {arvore1.height()}")
print(f"Rotações: {arvore1.rotations}")

# Cenário 2: Inserção ordenada
arvore2 = RBT()
ordenado = [20, 30, 40, 50, 60, 70, 80]
for elem in ordenado:
    arvore2.insert(elem)

print("\n=== Inserção Ordenada ===")
print(f"Elementos: {ordenado}")
print(f"Altura: {arvore2.height()}")
print(f"Rotações: {arvore2.rotations}")

print("\n=== Comparação ===")
print(f"RBT mantém altura O(log n) mesmo com inserção ordenada!")
print(f"Altura aleatória: {arvore1.height()}")
print(f"Altura ordenada: {arvore2.height()}")
```

**Explicação:**
- RBT mantém balanceamento automático
- Inserção ordenada não degenera a árvore
- Altura permanece logarítmica
- Mais rotações que inserção aleatória, mas ainda eficiente

---

## 🔬 Casos Especiais

### Inserir Duplicados

```python
from rbt import RBT

arvore = RBT()

arvore.insert(50)
arvore.insert(50)  # Duplicado
arvore.insert(50)  # Duplicado

print(f"Elementos: {arvore.inorder()}")  # [50, 50, 50]
```

**Nota:** Esta implementação permite duplicados (eles vão para a direita). Algumas implementações não permitem.

### Árvore com Muitos Elementos

```python
from rbt import RBT
import random

arvore = RBT()

# Inserir 1000 elementos aleatórios
elementos = random.sample(range(1, 10001), 1000)

for elem in elementos:
    arvore.insert(elem)

print(f"Elementos inseridos: {len(arvore.inorder())}")
print(f"Altura da árvore: {arvore.height()}")
print(f"Rotações realizadas: {arvore.rotations}")
print(f"Comparações totais: {arvore.comparisons}")

# Altura teórica máxima: 2 * log2(1000) ≈ 20
import math
altura_max_teorica = 2 * math.log2(1001)
print(f"Altura máxima teórica: {altura_max_teorica:.2f}")
```

---

## ✅ Resumo das Operações

| Operação | Complexidade | Exemplo |
|----------|--------------|---------|
| `insert(key)` | O(log n) | `arvore.insert(50)` |
| `search(key)` | O(log n) | `arvore.search(50)` |
| `remove(key)` | O(log n)* | `arvore.remove(50)` |
| `inorder()` | O(n) | `arvore.inorder()` |
| `preorder()` | O(n) | `arvore.preorder()` |
| `postorder()` | O(n) | `arvore.postorder()` |
| `height()` | O(n) | `arvore.height()` |
| `reset_metrics()` | O(1) | `arvore.reset_metrics()` |

*Nota: Remoção é simplificada nesta implementação

---

## 🎓 Conclusão

A Árvore Rubro-Negra oferece:
- ✅ Balanceamento automático
- ✅ Operações garantidas em O(log n)
- ✅ Menos rotações que AVL em média
- ✅ Altura ≤ 2 * log₂(n + 1)
- ✅ Usada em bibliotecas padrão (C++ map, Java TreeMap)
- ⚠️ Implementação mais complexa que BST e AVL
- ⚠️ Remoção simplificada neste código

**Quando usar RBT:**
- Muitas inserções e remoções
- Necessidade de balanceamento garantido
- Menos rotações que AVL é importante
- Implementação de estruturas de dados avançadas

**Vantagens sobre BST:**
- Não degenera em lista
- Desempenho garantido

**Vantagens sobre AVL:**
- Menos rotações em média
- Melhor para inserções/remoções frequentes

**Desvantagens:**
- Mais complexa de implementar
- Busca pode ser ligeiramente mais lenta que AVL (altura maior)
