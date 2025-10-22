
from funcoes import (
    garantir_arquivos, carregar_produtos, cadastrar_produto,
    listar_produtos, editar_produto, excluir_produto, log_action
)
import os
import sys
import time



def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def pausa():
    input("\nPressione Enter para continuar...")

def menu_principal():
    garantir_arquivos()
    produtos = carregar_produtos()


    while True:
        limpar_tela()
        print("="*50)
        print("             Loja de Roupa Python Dress")
        print("="*50)
        print("1) Cadastrar produto")
        print("2) Listar produtos")
        print("3) Editar produto")
        print("4) Excluir produto")
        print("5) Ver contador de registros / Contagem por categoria")
        print("6) Ver log (últimas linhas)")
        print("0) Sair")
        print("-"*50)
        opc = input("Escolha uma opção: ").strip()
        if opc == "1":
            cadastrar_produto(produtos)
            produtos = carregar_produtos()  
            pausa()
        elif opc == "2":
            tipo = input("Mostrar (1) Detalhado ou (2) Resumo? [1/2]: ").strip()
            listar_produtos(produtos, mostrar_tudo=(tipo!="2"))
            log_action("Visualização de produtos")
            pausa()
        elif opc == "3":
            editar_produto(produtos)
            produtos = carregar_produtos()
            pausa()
        elif opc == "4":
            excluir_produto(produtos)
            produtos = carregar_produtos()
            pausa()
        elif opc == "5":
            print("\nContagem de registros:", len(produtos))
            categorias = {}
            for p in produtos:
                cat = p.get("categoria","(sem categoria)") or "(sem categoria)"
                categorias[cat] = categorias.get(cat,0) + 1
            print("Contagem por categoria:")
            for c, q in categorias.items():
                print(f"  {c}: {q}")
            log_action("Consulta: contagem de registros por categoria")
            pausa()
        elif opc == "6":
            caminho = "dados/log.txt"
            try:
                n = int(input("Quantas últimas linhas do log mostrar? [10]: ") or "10")
            except:
                n = 10
            try:
                with open(caminho, "r", encoding="utf-8") as f:
                    linhas = f.readlines()
                    ultimas = linhas[-n:] if len(linhas) >= n else linhas
                    print("\n--- Últimas entradas do log ---")
                    for ln in ultimas:
                        print(ln.rstrip())
            except FileNotFoundError:
                print("Arquivo de log não encontrado.")
            except Exception as e:
                print("Erro ao ler o log:", e)
            log_action("Visualização do arquivo de log")
            pausa()
        elif opc == "0":
            log_action("Saída do sistema")
            print("Saindo...")
            time.sleep(0.6)
            sys.exit(0)
        else:
            print("Opção inválida. Tente novamente.")
            pausa()

if __name__ == "__main__":
    try:
        menu_principal()
    except KeyboardInterrupt:
        print("\nInterrompido pelo usuário. Saindo...")


