import tkinter as tk
from pan import executar

def tela_simples():

    def enviar():
        executar()

    # Janela principal
    janela = tk.Tk()
    janela.title("Envio de Arquivos - Simples")
    janela.configure(bg="#e6f2ff")
    janela.resizable(False, False)

    screen_width = janela.winfo_screenwidth()
    screen_height = janela.winfo_screenheight()
    window_width = int(screen_width * 0.4)
    window_height = int(screen_height * 0.3)
    x_position = (screen_width - window_width) // 2
    y_position = (screen_height - window_height) // 2
    janela.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    # Topo
    top_frame = tk.Frame(janela, bg="#0052cc", height=int(window_height * 0.3))
    top_frame.pack(fill="x")

    titulo = tk.Label(top_frame, text="Envio de Arquivos", font=("Helvetica", 20, "bold"), fg="white", bg="#0052cc")
    titulo.place(relx=0.5, rely=0.5, anchor="center")

    # Área de conteúdo
    frame_conteudo = tk.Frame(janela, bg="#ffffff", padx=20, pady=20)
    frame_conteudo.place(relx=0.5, rely=0.6, anchor="center")

    frame_caminho_interno = tk.Frame(frame_conteudo, bg="white")
    frame_caminho_interno.grid(row=0, column=1, sticky="w", pady=10)


    # Botões Enviar e Ver Planilhas
    frame_botoes = tk.Frame(frame_conteudo, bg="white")
    frame_botoes.grid(row=1, column=0, columnspan=2, pady=15)

    btn_enviar = tk.Button(frame_botoes, text="Enviar", bg="#0052cc", fg="white", font=("Helvetica", 12, "bold"), width=12, command=enviar)
    btn_enviar.pack(side="left", padx=10)

    # Rodapé
    rodape = tk.Label(janela, text="© 2025 Felipe da Silva | Portfólio", bg="#e6f2ff", font=("Helvetica", 9))
    rodape.pack(side="bottom", pady=10)

    janela.mainloop()

if __name__ == '__main__':
    tela_simples()
