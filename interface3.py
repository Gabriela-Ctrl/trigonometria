import tkinter as tk
import math  #Realiza operações matemáticas
from PIL import Image, ImageTk #Manipulação de imagens
import os #operações com o sistema de arquivois
import sys #manipulação de variáveis

def resource_path(relative_path):

    """
    Obtém o caminho absoluto para o recurso, funciona tanto em ambiente de desenvolvimento quanto após o empacotamento com PyInstaller
    """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)
    
    def calcular():
        """
        Realiza o cálcul dos valores trigonométricos (seno, cosseno e tangente) do ângulo fornecido e atualiza as labels com os resultados.
        """

        try:
            angulo = float(entrada_angulo.get())
            radiano = math.radians(angulo)

            # Calcular os valores trigonométricos
            seno = math.sin(radiano)
            cosseno = math.cos(radiano)
            tangente = math.tan(radiano)

            #Atualiza as labels com os resultados formatados com 3 casas decimais
            resultado_seno.config(text=f"{seno:.3f}")
            resultado_cosseno.config(text=f"{cosseno:.3f}")
            resultado_tangente.config(text=f"{tangente:.3f}")
        except ValueError:
            resultado_seno.config(text="Erro")
            resultado_cosseno.config(text="Erro")
            resultado_tangente.config(text="Erro")

            def limpar():
                """
                Limpa a entrada do usuário e reseta as labels dos resultados.
                """

            entrada_angulo.delete(0, tk.END) #Limpa o capo de entrada
            resultado_seno.config(text="")
            resultado_cosseno.config(text="")
            resultado_tangente.config(text="")

            def validar_entrada(texto):
                """
                Valida a entrada do usuário permitindo apenas npumeros e garantindo que o valor esteja entre 0 e 90.
                """

                if texto.isdigit() or texto == "": #Permite apenas npumetos ou campo vazio
                    if texto == "": #Se o campo estiver vazio, permite a entrada
                        return True
                    valor = int(texto) #Converte o texto para inteiro
                    return 0 <= valor <= 90 #retorna True se o valor esitiver entre 0 e 90, caso contrário False
                return False
            
            # _________________________INTERFACE________________________

            janela = tk.Tk()
            janela.title("Calculadora Trigonométrica")
            janela.geometry("400x550")
            janela.configure(bg="#f0f0f0")

            #Ícone da janela
            try:
                icone_path = resource_path("seno.png")
                icone = Image.open(icone_path)
                icone = ImageTk.PhotoImage(icone) #Converte a imagem para um formato compativel com Tkinter
                janela.iconphoto(True, icone) #define a imagem como ícone
            except FileNotFoundError:
                print("Imagem 'seno.png' não encontrada para o ícone")

                #magem seno2.png
            try:
                    image_path = resource_path("seno2.pgn")
                    imagem = Image.open(image_path)
                    imagem = imagem.resize((380, 200), Image.LANCZOS) #redimensiona a imagem
                    foto = ImageTk.PhotoImage(imagem) #Converte a imagem para um formato compativel com Tkinter
                    label_imagem = tk.Label(janela, image=foto, bg="#f0f0f0", borderwidth=0)
                    label_imagem.image = foto #mantém ima referência da imagem para evotar que o garbage collector a remova
                    label_imagem.pack (pady=20)

            except FileNotFoundError:
                label_imagem = tk.Label(janela, text="Imagem 'seno2.png' não encontrada", bg="#f0f0f0")
                label_imagem.pack(pady=20)

            #Entrada do ângulo
            frame_entrada = tk.Frame(janela, bg="#f0f0f0") #cria um frame para organizar a entrada
            frame_entrada.pack(pady=(0, 5))

            validacao = janela.register(validar_entrada)
            entrada_angulo = tk.Entry(frame_entrada, width=3, justify='center', font=('Arial', 16),
                                      bd=0, highlightthickness=0, relief='flat', bg="f0f0f0", fg='red',
                                      validate="key", validatecommand=(validacao, '%P' )) #cria o ca´po de entrada do ângulo
            entrada_angulo.pack() #posiciona o campo de entrada

            #Linha abaixo do campo de entrada 
            linha = tk.Frame(frame_entrada, bg="black", height=1, width=entrada_angulo.winfo_reqwidth()) #cria uma linha decorativa abaixo do campo de entrada
            linha.pack(pady=(0,5))

            #Botões
            frame_botoes = tk.Frame(janela, bg="#f0f0f0")
            frame_botoes.pack(pady=20)

            botao_calcular = tk.Button(frame_botoes, text="Cacular", command=calcular, font=('Arial', 12),
                                        bg="#d9d9d9", relief='flat', bd=0, highlightthickness=0)#botao para calcular valores trigonométricos
            botao_calcular.pack(side=tk.LEFT, padx=10) #Posiciona o botão à esquerda com um espaçamento horizontal

            botao_limpar = tk.Button(frame_botoes, text="Limpar", command=limpar, font=('Arial', 12),
                                     bg="d9d9d9", relied='flat', bd=0, highlightthickness=0)
            botao_limpar.pack(side=tk.RIGHT, padx=10) 

            #Resultados
            frame_resultados = tk.Frame(janela, bg="f0f0f0")
            frame_resultados.pack(pady=10)

            #Label resultado seno
            label_seno= tk.Label(frame_resultados, text="Seno:", font=('Arial', 12), bg="f0f0f0")
            label_seno.grid(row=0, column=0, padx=10, pady=5, sticky='e')
            resultado_seno = tk.LABEL(frame_resultados, text="", font=('Arial', 12, 'bold'), fg='red', bg="f0f0f0")
            resultado_seno.grid(row=0, column=1, padx=10, pady=5, sticky='w')

            #Label resultado cosseno
            label_cosseno= tk.Label(frame_resultados, text="cosseno:", font=('Arial', 12), bg="f0f0f0")
            label_cosseno.grid(row=0, column=0, padx=10, pady=5, sticky='e')
            resultado_cosseno = tk.LABEL(frame_resultados, text="", font=('Arial', 12, 'bold'), fg='red', bg="f0f0f0")
            resultado_cosseno.grid(row=0, column=1, padx=10, pady=5, sticky='w')

            #Label resultado tangente
            label_tangente= tk.Label(frame_resultados, text="tangente:", font=('Arial', 12), bg="f0f0f0")
            label_tangente.grid(row=0, column=0, padx=10, pady=5, sticky='e')
            resultado_tangente = tk.LABEL(frame_resultados, text="", font=('Arial', 12, 'bold'), fg='red', bg="f0f0f0")
            resultado_tangente.grid(row=0, column=1, padx=10, pady=5, sticky='w')

            janela.mainloop()








            