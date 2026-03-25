import os
from dotenv import load_dotenv
from google import genai
import leitor_pdf

# Abre o "cofre" (.env) e carrega as chaves para a memória
load_dotenv(override=True)

def gerar_contestacao(texto_processo, chave_api):
    print("\n🧠 Iniciando a análise jurídica com Inteligência Artificial...")
    cliente = genai.Client(api_key=chave_api)
    
    prompt = f"""
    Atue como um advogado sênior especialista em litígios e contencioso cível.
    Analise o documento anexo, que é a petição inicial de um processo judicial.
    
    [VERBOS DE AÇÃO E TAREFAS]
    1. ANALISE os fatos narrados pelo autor.
    2. IDENTIFIQUE os pedidos formulados e os pontos fracos da argumentação.
    3. GERE o esqueleto completo de uma CONTESTAÇÃO (defesa) para o réu.
    
    [ESTRUTURA OBRIGATÓRIA DA RESPOSTA]
    Estruture a peça processual em:
    - SÍNTESE DOS FATOS (Resuma o que o autor alegou)
    - PRELIMINARES (Se houver inépcia, ilegitimidade, prescrição, etc.)
    - DO MÉRITO (Fundamente a defesa rebatendo cada ponto com base na legislação brasileira atual)
    - DOS PEDIDOS (Os requerimentos finais da defesa)
    
    [TOM E ESTILO]
    Tom técnico, formal, persuasivo e estritamente jurídico.
    
    [TEXTO EXTRAÍDO DO PROCESSO]
    {texto_processo}
    """
    
    print("⏳ Redigindo a peça processual... Isso pode levar alguns segundos.")
    resposta = cliente.models.generate_content(
        model='gemini-2.5-flash', 
        contents=prompt
    )
    
    return resposta.text

## ==========================================
# PAINEL DE CONTROLE
# ==========================================
if __name__ == "__main__":
    MINHA_CHAVE_IA = os.getenv("GEMINI_API_KEY")
    
    if not MINHA_CHAVE_IA:
        print("❌ Erro: Chave da API não encontrada no arquivo .env.")
    else:
        # A MÁGICA DO DEBUG: Vamos ver as últimas 4 letras da chave que ele achou!
        print(f"Chave carregada com sucesso! Terminada em: ...{MINHA_CHAVE_IA[-4:]}")
        
        nome_do_arquivo = "processo_teste.pdf" 
        texto_extraido = leitor_pdf.extrair_texto_pdf(nome_do_arquivo)
        
        if "❌" not in texto_extraido:
            peca_redigida = gerar_contestacao(texto_extraido, MINHA_CHAVE_IA)
            
            with open("minuta_defesa.txt", "w", encoding="utf-8") as arquivo:
                arquivo.write(peca_redigida)
                
            print("\n✅ Sucesso! A minuta da defesa foi salva.")