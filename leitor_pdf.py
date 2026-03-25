import PyPDF2

def extrair_texto_pdf(caminho_arquivo):
    print(f"Tentando abrir o arquivo: {caminho_arquivo}...")
    texto_completo = ""
    
    try:
        # Abre o arquivo em modo de leitura binária ("rb")
        with open(caminho_arquivo, "rb") as arquivo:
            leitor = PyPDF2.PdfReader(arquivo)
            numero_paginas = len(leitor.pages)
            print(f"📄 Sucesso! O documento tem {numero_paginas} páginas.")
            
            # Varre cada página do PDF e extrai o texto
            for i in range(numero_paginas):
                pagina = leitor.pages[i]
                texto_completo += pagina.extract_text() + "\n"
                
        return texto_completo
        
    except FileNotFoundError:
        return "❌ Erro: Arquivo PDF não encontrado. Verifique o nome do arquivo."
    except Exception as e:
        return f"❌ Ocorreu um erro inesperado: {e}"

# ==========================================
# PAINEL DE CONTROLE (Teste da Função)
# ==========================================
if __name__ == "__main__":
    nome_do_arquivo = "processo_teste.pdf" 
    
    texto_extraido = extrair_texto_pdf(nome_do_arquivo)
    
    # Se não der erro, vamos imprimir apenas um pedaço do texto 
    # para não poluir o terminal com 50 páginas de uma vez
    if "❌" not in texto_extraido:
        print("\n--- TRECHO INICIAL DO TEXTO EXTRAÍDO ---")
        print(texto_extraido[:800]) # Mostra apenas os primeiros 800 caracteres
        print("\n----------------------------------------")