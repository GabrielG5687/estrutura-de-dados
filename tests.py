"""
Script de testes de desempenho para as três árvores
"""

import random
import time
from bst import BST
from avl import AVL
from rbt import RBT

def test_tree(tree_class, tree_name, data_sizes):
    """Testa uma árvore com diferentes tamanhos de dados"""
    print(f"\n{'='*70}")
    print(f"TESTES PARA {tree_name}")
    print(f"{'='*70}\n")
    
    results = []
    
    for size in data_sizes:
        print(f"Testando com {size} elementos...")
        
        # Gera dados aleatórios
        data = random.sample(range(1, size * 10), size)
        search_keys = random.sample(data, min(100, size))
        remove_keys = random.sample(data, min(50, size))
        
        # Cria a árvore
        tree = tree_class()
        
        # Teste de inserção
        start_time = time.time()
        for key in data:
            tree.insert(key)
        insert_time = time.time() - start_time
        
        insert_comparisons = tree.comparisons
        rotations = tree.rotations if hasattr(tree, 'rotations') else 0
        tree.reset_metrics()
        
        # Teste de busca
        start_time = time.time()
        for key in search_keys:
            tree.search(key)
        search_time = time.time() - start_time
        
        search_comparisons = tree.comparisons
        tree.reset_metrics()
        
        # Teste de remoção
        start_time = time.time()
        for key in remove_keys:
            tree.remove(key)
        remove_time = time.time() - start_time
        
        remove_comparisons = tree.comparisons
        
        # Calcula altura final
        final_height = tree.height()
        
        # Armazena resultados
        result = {
            'size': size,
            'insert_time': insert_time,
            'search_time': search_time,
            'remove_time': remove_time,
            'total_time': insert_time + search_time + remove_time,
            'height': final_height,
            'rotations': rotations,
            'avg_insert_comp': insert_comparisons / size if size > 0 else 0,
            'avg_search_comp': search_comparisons / len(search_keys) if search_keys else 0,
            'avg_remove_comp': remove_comparisons / len(remove_keys) if remove_keys else 0
        }
        results.append(result)
    
    # Imprime tabela de resultados
    print_results_table(tree_name, results)
    
    return results

def print_results_table(tree_name, results):
    """Imprime tabela formatada com os resultados"""
    print(f"\n{tree_name} - RESULTADOS DETALHADOS")
    print("-" * 100)
    print(f"{'Tamanho':<10} {'Tempo Total':<15} {'Altura':<10} {'Rotações':<12} "
          f"{'Comp/Insert':<15} {'Comp/Search':<15}")
    print("-" * 100)
    
    for r in results:
        print(f"{r['size']:<10} {r['total_time']:<15.6f} {r['height']:<10} "
              f"{r['rotations']:<12} {r['avg_insert_comp']:<15.2f} "
              f"{r['avg_search_comp']:<15.2f}")
    
    print("-" * 100)

def compare_trees(data_sizes):
    """Compara as três árvores"""
    print("\n" + "="*70)
    print("COMPARAÇÃO DE DESEMPENHO DAS TRÊS ÁRVORES")
    print("="*70)
    
    bst_results = test_tree(BST, "BST (Árvore Binária de Busca)", data_sizes)
    avl_results = test_tree(AVL, "AVL (Árvore Balanceada)", data_sizes)
    rbt_results = test_tree(RBT, "RBT (Árvore Rubro-Negra)", data_sizes)
    
    # Tabela comparativa
    print("\n" + "="*70)
    print("TABELA COMPARATIVA - TEMPO TOTAL (segundos)")
    print("="*70)
    print(f"{'Tamanho':<15} {'BST':<20} {'AVL':<20} {'RBT':<20}")
    print("-" * 70)
    
    for i, size in enumerate(data_sizes):
        print(f"{size:<15} {bst_results[i]['total_time']:<20.6f} "
              f"{avl_results[i]['total_time']:<20.6f} "
              f"{rbt_results[i]['total_time']:<20.6f}")
    
    print("\n" + "="*70)
    print("TABELA COMPARATIVA - ALTURA FINAL")
    print("="*70)
    print(f"{'Tamanho':<15} {'BST':<20} {'AVL':<20} {'RBT':<20}")
    print("-" * 70)
    
    for i, size in enumerate(data_sizes):
        print(f"{size:<15} {bst_results[i]['height']:<20} "
              f"{avl_results[i]['height']:<20} "
              f"{rbt_results[i]['height']:<20}")
    
    print("\n" + "="*70)
    print("TABELA COMPARATIVA - ROTAÇÕES")
    print("="*70)
    print(f"{'Tamanho':<15} {'BST':<20} {'AVL':<20} {'RBT':<20}")
    print("-" * 70)
    
    for i, size in enumerate(data_sizes):
        print(f"{size:<15} {'N/A':<20} "
              f"{avl_results[i]['rotations']:<20} "
              f"{rbt_results[i]['rotations']:<20}")
    
    print("\n")

if __name__ == "__main__":
    # Define os tamanhos de teste
    data_sizes = [100, 1000, 10000]
    
    # Executa os testes
    compare_trees(data_sizes)
    
    print("\nTestes concluídos!")
