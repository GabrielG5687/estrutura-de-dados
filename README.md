# Projeto de Árvores Binárias
## BST, AVL e Rubro-Negra

Este projeto implementa três tipos de árvores binárias em Python: BST (Árvore Binária de Busca), AVL (Árvore Balanceada) e RBT (Árvore Rubro-Negra).

## 📁 Estrutura do Projeto

```
.
├── bst.py          # Implementação da Árvore Binária de Busca
├── avl.py          # Implementação da Árvore AVL
├── rbt.py          # Implementação da Árvore Rubro-Negra
├── tests.py        # Testes de desempenho automatizados
├── main.py         # Interface interativa com menu
├── RELATORIO.md    # Relatório técnico completo
└── README.md       # Este arquivo
```

## 🚀 Como Executar

### Requisitos
- Python 3.6 ou superior
- Nenhuma biblioteca externa necessária (usa apenas biblioteca padrão)

### Executar Testes de Desempenho

Para executar os testes automatizados com 100, 1.000 e 10.000 elementos:

```bash
python tests.py
```

Este script irá:
- Gerar dados aleatórios
- Testar inserção, busca e remoção nas três árvores
- Medir tempo de execução, altura, rotações e comparações
- Exibir tabelas comparativas

### Executar Interface Interativa

Para usar o menu interativo:

```bash
python main.py
```

Funcionalidades do menu:
1. Inserir elemento
2. Remover elemento
3. Buscar elemento
4. Imprimir árvore (in-order)
5. Exibir métricas (altura, comparações, rotações)
6. Trocar tipo de árvore
7. Limpar árvore

## 📊 Funcionalidades Implementadas

### BST (Árvore Binária de Busca)
- ✅ Inserção
- ✅ Busca
- ✅ Remoção
- ✅ Percursos: in-order, pre-order, post-order
- ✅ Cálculo de altura
- ✅ Contagem de comparações

### AVL (Árvore Balanceada)
- ✅ Inserção com balanceamento automático
- ✅ Busca
- ✅ Remoção com rebalanceamento
- ✅ Rotações simples (esquerda e direita)
- ✅ Rotações duplas (LR e RL)
- ✅ Cálculo de fator de balanceamento
- ✅ Percursos: in-order, pre-order, post-order
- ✅ Cálculo de altura
- ✅ Contagem de comparações e rotações

### RBT (Árvore Rubro-Negra)
- ✅ Inserção com ajuste de cores
- ✅ Busca
- ✅ Remoção (versão simplificada)
- ✅ Rotações com manutenção de propriedades
- ✅ Validação de propriedades rubro-negras
- ✅ Percursos: in-order, pre-order, post-order
- ✅ Cálculo de altura
- ✅ Contagem de comparações e rotações

## 📈 Exemplo de Uso

```python
from bst import BST
from avl import AVL
from rbt import RBT

# Criar uma árvore AVL
tree = AVL()

# Inserir elementos
for value in [50, 30, 70, 20, 40, 60, 80]:
    tree.insert(value)

# Buscar elemento
found = tree.search(40)  # Retorna True

# Imprimir em ordem
print(tree.inorder())  # [20, 30, 40, 50, 60, 70, 80]

# Ver métricas
print(f"Altura: {tree.height()}")
print(f"Comparações: {tree.comparisons}")
print(f"Rotações: {tree.rotations}")

# Remover elemento
tree.remove(30)
```

## 📝 Relatório

O relatório técnico completo está disponível em `RELATORIO.md` e inclui:
- Introdução teórica sobre cada tipo de árvore
- Explicação detalhada da implementação
- Análise de complexidade (temporal e espacial)
- Tabelas de desempenho com resultados dos testes
- Comparação entre as três estruturas
- Conclusões e recomendações de uso

## 🎯 Resultados Esperados

Ao executar `tests.py`, você verá:
- Tempo de execução para cada operação
- Altura final de cada árvore
- Número de rotações (AVL e RBT)
- Média de comparações por operação
- Tabelas comparativas entre as três estruturas

## 📚 Conceitos Implementados

- **BST**: Estrutura básica sem balanceamento
- **AVL**: Balanceamento rigoroso (fator -1, 0, 1)
- **RBT**: Balanceamento relaxado com propriedades de cor

## 🔧 Personalização

Para testar com tamanhos diferentes, edite `tests.py`:

```python
# Linha no final do arquivo
data_sizes = [100, 1000, 10000]  # Modifique aqui
```

## 📄 Licença

Este projeto foi desenvolvido para fins acadêmicos.

## 👨‍💻 Autor

Trabalho acadêmico - Estrutura de Dados
