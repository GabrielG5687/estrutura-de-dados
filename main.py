"""
Menu interativo para manipulação de árvores
"""

from bst import BST
from avl import AVL
from rbt import RBT

def print_menu():
    """Imprime o menu principal"""
    print("\n" + "="*50)
    print("SISTEMA DE ÁRVORES - MENU PRINCIPAL")
    print("="*50)
    print("1. Inserir elemento")
    print("2. Remover elemento")
    print("3. Buscar elemento")
    print("4. Imprimir árvore (in-order)")
    print("5. Exibir métricas da árvore")
    print("6. Trocar tipo de árvore")
    print("7. Limpar árvore")
    print("0. Sair")
    print("="*50)

def print_tree_menu():
    """Menu para escolher o tipo de árvore"""
    print("\n" + "="*50)
    print("ESCOLHA O TIPO DE ÁRVORE")
    print("="*50)
    print("1. BST (Árvore Binária de Busca)")
    print("2. AVL (Árvore Balanceada)")
    print("3. RBT (Árvore Rubro-Negra)")
    print("="*50)

def create_tree(tree_type):
    """Cria uma árvore do tipo especificado"""
    if tree_type == 1:
        return BST(), "BST"
    elif tree_type == 2:
        return AVL(), "AVL"
    elif tree_type == 3:
        return RBT(), "RBT"
    return None, None

def main():
    """Função principal"""
    print("\nBem-vindo ao Sistema de Árvores!")
    
    # Escolhe o tipo de árvore inicial
    print_tree_menu()
    while True:
        try:
            choice = int(input("\nEscolha (1-3): "))
            if choice in [1, 2, 3]:
                tree, tree_name = create_tree(choice)
                print(f"\n✓ Árvore {tree_name} criada com sucesso!")
                break
            else:
                print("Opção inválida!")
        except ValueError:
            print("Por favor, digite um número válido!")
    
    # Loop principal
    while True:
        print_menu()
        print(f"Árvore atual: {tree_name}")
        
        try:
            option = int(input("\nEscolha uma opção: "))
            
            if option == 0:
                print("\nEncerrando o programa. Até logo!")
                break
            
            elif option == 1:
                key = int(input("Digite o valor a inserir: "))
                tree.insert(key)
                print(f"✓ Valor {key} inserido com sucesso!")
            
            elif option == 2:
                key = int(input("Digite o valor a remover: "))
                tree.remove(key)
                print(f"✓ Valor {key} removido (se existia)!")
            
            elif option == 3:
                key = int(input("Digite o valor a buscar: "))
                found = tree.search(key)
                if found:
                    print(f"✓ Valor {key} ENCONTRADO na árvore!")
                else:
                    print(f"✗ Valor {key} NÃO encontrado na árvore!")
            
            elif option == 4:
                elements = tree.inorder()
                if elements:
                    print(f"\nÁrvore (in-order): {elements}")
                else:
                    print("\nÁrvore vazia!")
            
            elif option == 5:
                print("\n" + "="*50)
                print("MÉTRICAS DA ÁRVORE")
                print("="*50)
                print(f"Tipo: {tree_name}")
                print(f"Altura: {tree.height()}")
                print(f"Comparações acumuladas: {tree.comparisons}")
                if hasattr(tree, 'rotations'):
                    print(f"Rotações acumuladas: {tree.rotations}")
                elements = tree.inorder()
                print(f"Número de elementos: {len(elements)}")
                print("="*50)
            
            elif option == 6:
                print_tree_menu()
                choice = int(input("\nEscolha o novo tipo (1-3): "))
                if choice in [1, 2, 3]:
                    tree, tree_name = create_tree(choice)
                    print(f"\n✓ Trocado para árvore {tree_name}!")
                else:
                    print("Opção inválida!")
            
            elif option == 7:
                choice = input("Tem certeza que deseja limpar a árvore? (s/n): ")
                if choice.lower() == 's':
                    tree, tree_name = create_tree(
                        1 if tree_name == "BST" else 2 if tree_name == "AVL" else 3
                    )
                    print("✓ Árvore limpa!")
            
            else:
                print("Opção inválida!")
        
        except ValueError:
            print("Erro: Digite um número válido!")
        except Exception as e:
            print(f"Erro: {e}")

if __name__ == "__main__":
    main()
