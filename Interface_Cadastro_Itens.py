import customtkinter as ctk

ctk.set_appearance_mode('light')
ctk.set_default_color_theme('dark-blue')
app = ctk.CTk()
app.title("Sistema de Autenticação")
app.geometry("1600x900")

#-------------------------------funções----------------------------

def MudarParaProduto():
    BarraLateral.pack(fill="y", side="left")
    Header.pack_propagate(False)
    TelaInicial.forget()
    TelaProdutos.pack(
    pady=(20, 20),
    padx=(20, 20),
    expand=True,
    fill="both"
)
    Header.configure(
        fg_color="#70A5F3")
    TelaInicial.configure(
       fg_color = "#959697"
    )

def BotaoProduto():
    TelaProdutos.pack(
    pady=(20, 20),
    padx=(20, 20),
    expand=True,
    fill="both"
)
    TelaClientes.forget(),TelaAjuda.forget(), TelaConfiguracoes.forget(), TelaPesquisar.forget(), TelaCaixa.forget()

def BotaoCliente():
    TelaClientes.pack(
    pady=(20, 20),
    padx=(20, 20),
    expand=True,
    fill="both"
)    
    TelaProdutos.forget(),TelaAjuda.forget(), TelaConfiguracoes.forget(), TelaPesquisar.forget(), TelaCaixa.forget()

def BotaoAjuda():
    TelaAjuda.pack(
    pady=(20, 20),
    padx=(20, 20),
    expand=True,
    fill="both"
)    
    TelaClientes.forget(), TelaProdutos.forget(), TelaConfiguracoes.forget(), TelaPesquisar.forget(), TelaCaixa.forget()

def BotaoConfiguracao():
    TelaConfiguracoes.pack(
    pady=(20, 20),
    padx=(20, 20),
    expand=True,
    fill="both"
)       
    TelaClientes.forget(), TelaProdutos.forget(),TelaAjuda.forget(), TelaPesquisar.forget(), TelaCaixa.forget()

def BotaoPesquisar():
    TelaPesquisar.pack(
    pady=(20, 20),
    padx=(20, 20),
    expand=True,
    fill="both"
)   
    TelaClientes.forget(), TelaProdutos.forget(),TelaAjuda.forget(), TelaConfiguracoes.forget(), TelaCaixa.forget()

def BotaoCaixa():
    TelaCaixa.pack(
    pady=(20, 20),
    padx=(20, 20),
    expand=True,
    fill="both"
)   
    TelaClientes.forget(),TelaProdutos.forget(),TelaAjuda.forget(), TelaConfiguracoes.forget(), TelaPesquisar.forget()









#----------------------------------------Frame Inicial------------------------------------

Header = ctk.CTkFrame(
    app,
    fg_color="white",
    height=60,
    corner_radius=0
    
)

Header.pack(fill="x", side="top")
Header.pack_propagate(False)

labelOnix = ctk.CTkLabel(
    Header,
    text_color="red",
    text="ONIX",
    font=("Montserrat ExtraBold", 30)
)

labelOnix.pack(side = 'left', padx = (20,0))

BarraLateral = ctk.CTkFrame(app,
                            fg_color='white',
                            corner_radius=0,
                            width = 170,
                           
                            )

#-------------------------------------tela inicial---------------------
TelaInicial = ctk.CTkFrame(app,
                           fg_color="#70A5F3",
                           corner_radius=0)
TelaInicial.pack(fill="both", expand=True)

FrameLogin = ctk.CTkFrame(
    TelaInicial,
    fg_color="white",
)

FrameLogin.pack(
    side="top",
    anchor="n",
    pady=200
)

#--------------------------------------------------------------------------

EntryUsuario = ctk.CTkEntry(
    FrameLogin,
    width=300,
    height=80,
    fg_color="#F2F2F2",
    placeholder_text='Usúario',
    corner_radius=50
)

EntryUsuario.pack(
    pady=(60, 10),
    padx=100
)


EntrySenha = ctk.CTkEntry(
    FrameLogin,
    width=300,
    height=80,
    fg_color="#F2F2F2",
    placeholder_text='Senha',
    corner_radius=50
)

EntrySenha.pack(
    pady=(10, 60),
    padx=100
)

botaoLogar = ctk.CTkButton(
    FrameLogin,
    width=300,
    height=80,
    fg_color="#16A34A",
    corner_radius=50,
    text = 'Logar',
    command = MudarParaProduto
)

botaoLogar.pack(
    pady=(10, 60),
    padx=100
)
#----------------------------------PRODUTOS E SERVIÇOS -----------------------

TelaProdutos = ctk.CTkFrame(app,
                           fg_color="#FFFFFF",
                           corner_radius=0)


BarraLateral = ctk.CTkFrame(app,
                            fg_color='white',
                            corner_radius=0,
                            width = 170,
                            
                           
                            )

BotaoProdutos = ctk.CTkButton(
    BarraLateral,
    fg_color="#FFFFFF",
    corner_radius=0,
    border_width=0.6,
    border_color="#858585",
    width = 170,
    height = 90,
    text = 'Produtos e serviços',
    text_color= 'black',
    hover_color="#5B926F",
    command = BotaoProduto
    
)

BotaoProdutos.pack()

BotaoClientes = ctk.CTkButton(
    BarraLateral,
    fg_color="#FFFFFF",
    corner_radius=0,
    border_width=0.6,
    border_color="#858585",
    width = 170,
    height = 90,
    text = 'Clientes',
    text_color= 'black',
    hover_color="#5B926F",
    command = BotaoCliente
    
)

BotaoClientes.pack()

BotaoCaixa = ctk.CTkButton(
    BarraLateral,
    fg_color="#FFFFFF",
    corner_radius=0,
    border_width=0.6,
    border_color="#858585",
    width = 170,
    height = 90,
    text = 'Caixa',
    text_color= 'black',
    hover_color="#5B926F",
    command = BotaoCaixa
    
    
)

BotaoCaixa.pack()

BotaoConfiguracoes = ctk.CTkButton(
    BarraLateral,
    fg_color="#FFFFFF",
    corner_radius=0,
    border_width=0.6,
    border_color="#858585",
    width = 170,
    height = 90,
    text = 'Configurações',
    text_color= 'black',
    hover_color="#5B926F",
    command = BotaoConfiguracao
    
)

BotaoConfiguracoes.pack()

BotaoAjuda = ctk.CTkButton(
    BarraLateral,
    fg_color="#FFFFFF",
    corner_radius=0,
    border_width=0.6,
    border_color="#858585",
    width = 170,
    height = 90,
    text = 'Ajuda',
    text_color= 'black',
    hover_color="#5B926F",
    command = BotaoAjuda
    
)

BotaoAjuda.pack()

BotaoPesquisar = ctk.CTkButton(
    BarraLateral,
    fg_color="#FFFFFF",
    corner_radius=0,
    border_width=0.6,
    border_color="#858585",
    width = 170,
    height = 90,
    text = 'Pesquisar',
    text_color= 'black',
    hover_color="#5B926F",
    command = BotaoPesquisar
    
)

BotaoPesquisar.pack()

#------------------------- Telas -------------------

#------------------------------Tela Cliente --------------------
TelaClientes = ctk.CTkFrame(app,
                           fg_color="#FFFFFF",
                           corner_radius=0)

LabelTexoPrincipal = ctk.CTkLabel(
    TelaClientes,
    text_color="#70A5F3",
    text="Cadastro de Clientes",
    font=("Montserrat ExtraBold", 20)
)



LabelTexoPrincipal.pack(side = 'top', anchor = 'w', pady = (10), padx = (10))

frameCadastro = ctk.CTkFrame(TelaClientes,
                           fg_color="#FFFFFF",
                           corner_radius=0,
                            border_width=0.6,
                            border_color="#858585",)

frameCadastro.pack(
    side = 'top', anchor = 'n',
    pady=(20),
    padx=(20),
    expand=True,
    fill="both"
)


LabelNome = ctk.CTkLabel(
    frameCadastro,
    font=("Montserrat ExtraBold", 15),
    text='Nome',
    corner_radius=0
)

LabelNome.pack(
    side = 'top', anchor = 'w',
    pady=(20, 0),
    padx=20
)




EntryNome = ctk.CTkEntry(
    frameCadastro,
    width=700,
    height=40,
    fg_color="#F2F2F2",
    placeholder_text='Enzo Nunes Lopes',
    corner_radius=0
)

EntryNome.pack(
    side = 'top', anchor = 'w',
    pady=(0, 20),
    padx=20
)


FrameEntradas = ctk.CTkFrame(
    frameCadastro,
    fg_color='transparent'
)

FrameEntradas.pack(
    anchor="w",
    padx=10,
    pady = 10
)


FrameCpf = ctk.CTkFrame(
    FrameEntradas,
    fg_color="transparent"
)
FrameCpf.pack(side="left", padx=10)

LabelCpf = ctk.CTkLabel(
    FrameCpf,
    font=("Montserrat ExtraBold", 15),
    text="Cpf"
)
LabelCpf.pack(anchor="w")

EntryCpf = ctk.CTkEntry(
    FrameCpf,
    width=250,
    height=40,
    fg_color="#F2F2F2",
    placeholder_text="123.456.789-09",
    corner_radius=0
)
EntryCpf.pack()


FrameRg = ctk.CTkFrame(
    FrameEntradas,
    fg_color="transparent"
)
FrameRg.pack(side="left", padx=10)

LabelRg = ctk.CTkLabel(
    FrameRg,
    font=("Montserrat ExtraBold", 15),
    text="Rg"
)
LabelRg.pack(anchor="w")

EntryRg = ctk.CTkEntry(
    FrameRg,
    width=250,
    height=40,
    fg_color="#F2F2F2",
    placeholder_text="12.345.678-9",
    corner_radius=0
)
EntryRg.pack()

FrameCnpj = ctk.CTkFrame(
    FrameEntradas,
    fg_color="transparent"
)

FrameCnpj.pack(side="left", padx=10)

LabelCnpj = ctk.CTkLabel(
    FrameCnpj,
    font=("Montserrat ExtraBold", 15),
    text="Cnpj"
)

LabelCnpj.pack(anchor="w")

EntryCnpj = ctk.CTkEntry(
    FrameCnpj,
    width=250,
    height=40,
    fg_color="#F2F2F2",
    placeholder_text="12.345.678/0001-95",
    corner_radius=0
)

EntryCnpj.pack()

#----------------------------------------
FrameDTnascimento = ctk.CTkFrame(
    FrameEntradas,
    fg_color="transparent"
)

FrameDTnascimento.pack(side="left", padx=10)

LabelDTnascimento = ctk.CTkLabel(
    FrameDTnascimento,
    font=("Montserrat ExtraBold", 15),
    text="Data Nacimento"
)

LabelDTnascimento.pack(anchor="w")

EntryDTnascimento = ctk.CTkEntry(
    FrameDTnascimento,
    width=250,
    height=40,
    fg_color="#F2F2F2",
    placeholder_text="00/00/0000",
    corner_radius=0
)

EntryDTnascimento.pack()

#---------------------------------------------------------

LabelContatos = ctk.CTkLabel(
    frameCadastro,
    text="Contatos Pessoais",
    font=("Montserrat ExtraBold", 20),
    text_color="#868686",   
)


FrameEntradas2 = ctk.CTkFrame(
    frameCadastro,
    fg_color='#FAF9F9',
    width= 1400,
    height= 90
)

FrameEntradas2.pack(
    anchor="w",
    padx=10,
    pady = 10
)

FrameEntradas2.pack_propagate(False)

FramePais = ctk.CTkFrame(
    FrameEntradas2,
    fg_color="#FAF9F9"
)


FramePais.pack(
    side="left",
    pady=10,
    padx=10
)

ComboPais = ctk.CTkComboBox(
    FramePais,
    values=["BR +55", "US +1", "PT +351", "ES +34"],
    width=100,
    height=40
)

ComboPais.pack(
    side="left",
    pady=(20, 0)
)


FrameNumeroCelular = ctk.CTkFrame(
    FrameEntradas2,
    fg_color="transparent"
)

FrameNumeroCelular.pack(
    side="left",
    padx=10
)

LabelNumeroCelular = ctk.CTkLabel(
    FrameNumeroCelular,
    font=("Montserrat ExtraBold", 15),
    text="Celular"
)

LabelNumeroCelular.pack(
    anchor="w"
)

EntryNumeroCelular = ctk.CTkEntry(
    FrameNumeroCelular,
    width=350,
    height=40,
    fg_color="#F2F2F2",
    placeholder_text="(11) 99999-9999",
    corner_radius=0
)

EntryNumeroCelular.pack()

FrameObservacoes = ctk.CTkFrame(
    FrameEntradas2,
    fg_color="transparent"
)

FrameObservacoes.pack(
    side="left",
    padx=10
)

LabelObservacoes = ctk.CTkLabel(
    FrameObservacoes,
    font=("Montserrat ExtraBold", 15),
    text="Observações"
)

LabelObservacoes.pack(
    anchor="w"
)

EntryObservacoes = ctk.CTkEntry(
    FrameObservacoes,
    width=350,
    height=40,
    fg_color="#F2F2F2",
    placeholder_text="Digite uma observação",
    corner_radius=0
)

EntryObservacoes.pack()

#-------------------------------------- frame3---------------------
FrameEntradas3 = ctk.CTkFrame(
    frameCadastro,
    fg_color='#FAF9F9',
    width=1400,
    height=90
)

FrameEntradas3.pack(
    anchor="w",
    padx=10,
    pady=10
)

FrameEntradas3.pack_propagate(False)

FrameEmail = ctk.CTkFrame(
    FrameEntradas3,
    fg_color="#FAF9F9"
)

FrameEmail.pack(
    side="left",
    pady=10,
    padx=10
)

ComboEmail = ctk.CTkComboBox(
    FrameEmail,
    values=["Gmail", "Hotmail", "Outlook"],
    width=100,
    height=40
)

ComboEmail.pack(
    side="left",
    pady=(20, 0)
)

FrameNumeroEmail = ctk.CTkFrame(
    FrameEntradas3,
    fg_color="transparent"
)

FrameNumeroEmail.pack(
    side="left",
    padx=10
)

LabelNumeroEmail = ctk.CTkLabel(
    FrameNumeroEmail,
    font=("Montserrat ExtraBold", 15),
    text="E-mail"
)

LabelNumeroEmail.pack(
    anchor="w"
)

EntryNumeroEmail = ctk.CTkEntry(
    FrameNumeroEmail,
    width=350,
    height=40,
    fg_color="#F2F2F2",
    placeholder_text="Digite seu e-mail",
    corner_radius=0
)

EntryNumeroEmail.pack()

FrameObservacoesEmail = ctk.CTkFrame(
    FrameEntradas3,
    fg_color="transparent"
)

FrameObservacoesEmail.pack(
    side="left",
    padx=10
)

LabelObservacoesEmail = ctk.CTkLabel(
    FrameObservacoesEmail,
    font=("Montserrat ExtraBold", 15),
    text="Observações"
)

LabelObservacoesEmail.pack(
    anchor="w"
)

EntryObservacoesEmail = ctk.CTkEntry(
    FrameObservacoesEmail,
    width=350,
    height=40,
    fg_color="#F2F2F2",
    placeholder_text="Digite uma observação",
    corner_radius=0
)

#-------------------- frame4 ------------------------------

FrameEntradas4 = ctk.CTkFrame(
    frameCadastro,
    fg_color='#FAF9F9',
    width=1400,
    height=90
)
FrameEntradas4.pack(
    anchor="w",
    padx=10,
    pady=20
)
FrameEntradas4.pack_propagate(False)


FrameResidencial = ctk.CTkFrame(
    FrameEntradas4,
    fg_color="#FAF9F9"
)
FrameResidencial.pack(
    side="left",
    pady=10,
    padx=10
)

ComboResidencial = ctk.CTkComboBox(
    FrameResidencial,
    values=["Casa", "Apartamento", "Condomínio"],
    width=150,
    height=40
)
ComboResidencial.pack(
    side="left",
    pady=(20, 0)
)


FrameCep = ctk.CTkFrame(
    FrameEntradas4,
    fg_color="transparent"
)
FrameCep.pack(
    side="left",
    padx=10
)

LabelCep = ctk.CTkLabel(
    FrameCep,
    font=("Montserrat ExtraBold", 15),
    text="CEP"
)
LabelCep.pack(
    anchor="w"
)

EntryCep = ctk.CTkEntry(
    FrameCep,
    width=200,
    height=40,
    fg_color="#F2F2F2",
    placeholder_text="00000-000",
    corner_radius=0
)
EntryCep.pack()


FrameComplemento = ctk.CTkFrame(
    FrameEntradas4,
    fg_color="transparent"
)
FrameComplemento.pack(
    side="left",
    padx=10
)

LabelComplemento = ctk.CTkLabel(
    FrameComplemento,
    font=("Montserrat ExtraBold", 15),
    text="Complemento"
)
LabelComplemento.pack(
    anchor="w"
)

EntryComplemento = ctk.CTkEntry(
    FrameComplemento,
    width=250,
    height=40,
    fg_color="#F2F2F2",
    placeholder_text="Digite o complemento",
    corner_radius=0
)
EntryComplemento.pack()


FrameNumeroCasa = ctk.CTkFrame(
    FrameEntradas4,
    fg_color="transparent"
)
FrameNumeroCasa.pack(
    side="left",
    padx=10
)

LabelNumeroCasa = ctk.CTkLabel(
    FrameNumeroCasa,
    font=("Montserrat ExtraBold", 15),
    text="Número da casa"
)
LabelNumeroCasa.pack(
    anchor="w"
)

EntryNumeroCasa = ctk.CTkEntry(
    FrameNumeroCasa,
    width=150,
    height=40,
    fg_color="#F2F2F2",
    placeholder_text="Número",
    corner_radius=0
)
EntryNumeroCasa.pack()


FrameObservacaoCasa = ctk.CTkFrame(
    FrameEntradas4,
    fg_color="transparent"
)
FrameObservacaoCasa.pack(
    side="left",
    padx=10
)

LabelObservacaoCasa = ctk.CTkLabel(
    FrameObservacaoCasa,
    font=("Montserrat ExtraBold", 15),
    text="Observação"
)
LabelObservacaoCasa.pack(
    anchor="w"
)

EntryObservacaoCasa = ctk.CTkEntry(
    FrameObservacaoCasa,
    width=300,
    height=40,
    fg_color="#F2F2F2",
    placeholder_text="Digite uma observação",
    corner_radius=0
)
EntryObservacaoCasa.pack()

EntryObservacoesEmail.pack()

# ---------------- botoes -----------------

FrameBotoesEnviarCadastro = ctk.CTkFrame(
    frameCadastro,
    fg_color='transparent',
    
)

FrameBotoesEnviarCadastro.pack(pady = 20, anchor = 'w', padx = 20)

buttonCadastrar = ctk.CTkButton(
    FrameBotoesEnviarCadastro,
    fg_color= "#16A34A",
    text = 'Enviar',
    text_color= 'black'
)

buttonCadastrar.pack(side = 'left', padx = 10)

buttonApagar = ctk.CTkButton(
    FrameBotoesEnviarCadastro,
    fg_color= "#4395E2",
    text = 'Apagar',
    text_color= 'black'
)

buttonApagar.pack(side='left')













#----------------------------------------------------------------------   
TelaProdutos = ctk.CTkFrame(app,
                           fg_color="#FFFFFF",
                           corner_radius=0)

LabelTexoPrincipal2 = ctk.CTkLabel(
    TelaProdutos,
    text_color="#70A5F3",
    text="Produtos e serviços",
    font=("Montserrat ExtraBold", 20)
)

LabelTexoPrincipal2.pack(side = 'top', anchor = 'w', pady = (10), padx = (10))

frameProduto = ctk.CTkFrame(
    TelaProdutos,
    fg_color="#FFFFFF",
    corner_radius=0,
    border_width=0.6,
    border_color="#858585"
)

frameProduto.pack(
    side='top',
    anchor='n',
    pady=20,
    padx=20,
    fill='both',
    expand=True
)

FrameEntradas = ctk.CTkFrame(
    frameProduto,
    fg_color="transparent"
)

FrameEntradas.pack(
    anchor="w",
    padx=10,
    pady=10
)


FrameNomeProduto = ctk.CTkFrame(
    FrameEntradas,
    fg_color="transparent"
)

FrameNomeProduto.pack(
    side="left",
    padx=10
)

LabelNomeProduto = ctk.CTkLabel(
    FrameNomeProduto,
    font=("Montserrat ExtraBold", 15),
    text="Nome do Produto",
    corner_radius=0
)

LabelNomeProduto.pack(
    anchor="w"
)

EntryNomeProduto = ctk.CTkEntry(
    FrameNomeProduto,
    width=200,
    height=40,
    fg_color="#F2F2F2",
    placeholder_text="Digite o nome do produto",
    corner_radius=0
)

EntryNomeProduto.pack()


FrameCodigoProduto = ctk.CTkFrame(
    FrameEntradas,
    fg_color="transparent"
)

FrameCodigoProduto.pack(
    side="left",
    padx=10
)

LabelCodigoProduto = ctk.CTkLabel(
    FrameCodigoProduto,
    font=("Montserrat ExtraBold", 15),
    text="Código do produto",
    corner_radius=0
)

LabelCodigoProduto.pack(
    anchor="w"
)

EntryCodigoProduto = ctk.CTkEntry(
    FrameCodigoProduto,
    width=200,
    height=40,
    fg_color="#F2F2F2",
    placeholder_text="Código do produto",
    corner_radius=0
)

EntryCodigoProduto.pack()

FrameCodigoBarrasProduto = ctk.CTkFrame(
    FrameEntradas,
    fg_color="transparent"
)

FrameCodigoBarrasProduto.pack(
    side="left",
    padx=10
)

LabelCodigoBarrasProduto = ctk.CTkLabel(
    FrameCodigoBarrasProduto,
    font=("Montserrat ExtraBold", 15),
    text="Código de Barras",
    corner_radius=0
)

LabelCodigoBarrasProduto.pack(
    anchor="w"
)

EntryCodigoBarrasProduto = ctk.CTkEntry(
    FrameCodigoBarrasProduto,
    width=200,
    height=40,
    fg_color="#F2F2F2",
    placeholder_text='Código De Barras',
    corner_radius=0
)

EntryCodigoBarrasProduto.pack()

FrameCategoria = ctk.CTkFrame(
    FrameEntradas,
    fg_color= 'transparent'
)

FrameCategoria.pack(
    side="left",
    pady=10,
    padx=10
)

LabelCategoria = ctk.CTkLabel(
    FrameCategoria,
    text = 'Categoria',
    font=("Montserrat ExtraBold", 15)
    
)

LabelCategoria.pack(anchor = 'w')

ComboCategoria = ctk.CTkComboBox(
    FrameCategoria,
    values=["Bebidas",
            "Biscoitos e Snacks",
            "Alimentos",
            "Limpeza",
            "Higiene Pessoal",
            "Carnes",
            "Hortifruti",
            "Laticínios",
            "Padaria",
            "Pet Shop",
            "Congelados",
            "Doces e Chocolates",
            "Bebês",
            "Outros"],
    width=100,
    height=40

)

ComboCategoria.pack(
    side="left",
    pady=(0, 0)
)


FrameMarca = ctk.CTkFrame(
    FrameEntradas,
    fg_color= 'transparent'
)

FrameMarca.pack(
    side="left",
    pady=10,
    padx=10
)

LabelMarca = ctk.CTkLabel(
    FrameMarca,
    text = 'Categoria',
    font=("Montserrat ExtraBold", 15)
    
)

LabelMarca.pack(anchor = 'w')

ComboMarca = ctk.CTkComboBox(
    FrameMarca,
    values=[
        "Coca-Cola",
        "Nestlé",
        "Sadia",
        "Bauducco",
        "Ypê",
        "Unilever"],
        width=100,
        height=40
)

ComboMarca.pack(
    side="left",
    pady=(0, 0)
)


FrameDescricao = ctk.CTkFrame(
    FrameEntradas,
    fg_color="transparent"
)

FrameDescricao.pack(
    side="left",
    padx=10
)

LabelDescricao = ctk.CTkLabel(
    FrameDescricao,
    font=("Montserrat ExtraBold", 15),
    text="Descrição",
    corner_radius=0
)

LabelDescricao.pack(
    anchor="w"
)

EntryDescricao = ctk.CTkEntry(
    FrameDescricao,
    width=400,
    height=40,
    fg_color="#F2F2F2",
    placeholder_text='Fruta banana',
    corner_radius=0
)

EntryDescricao.pack()


#------------------------------------------------------------


LabelValores = ctk.CTkLabel(
    frameProduto,
    font=("Montserrat ExtraBold", 20),
    text_color="#70A5F3",
    text="Valores",
)

LabelValores.pack(
    pady = (10,0),
    padx = 20,
    anchor = 'w'
)

FrameEntradas2 = ctk.CTkFrame(
    frameProduto,
    fg_color='#FAF9F9',
    width= 1400,
    height= 90
)

FrameEntradas2.pack(
    anchor="w",
    padx=10,
    pady = 10
)

FrameEntradas2.pack_propagate(False)

FramePreco = ctk.CTkFrame(
    FrameEntradas2,
    fg_color="transparent"
)

FramePreco.pack(
    side="left",
    padx=10
)

LabelValorCusto = ctk.CTkLabel(
    FramePreco,
    font=("Montserrat ExtraBold", 15),
    text="Preço de custo",
    corner_radius=0
)

LabelValorCusto.pack(
    anchor="w"
)

EntryValorCusto = ctk.CTkEntry(
    FramePreco,
    width=400,
    height=40,
    fg_color="#F2F2F2",
    placeholder_text='R$ 0,00',
    corner_radius=0
)

EntryValorCusto.pack()


FramePrecoVenda = ctk.CTkFrame(
    FrameEntradas2,
    fg_color="transparent"
)

FramePrecoVenda.pack(
    side="left",
    padx=10
)

LabelPrecoVenda = ctk.CTkLabel(
    FramePrecoVenda,
    font=("Montserrat ExtraBold", 15),
    text="Valor de Venda",
    corner_radius=0
)

LabelPrecoVenda.pack(
    anchor="w"
)

EntryPrecoVenda = ctk.CTkEntry(
    FramePrecoVenda,
    width=400,
    height=40,
    fg_color="#F2F2F2",
    placeholder_text='R$ 0,00',
    corner_radius=0
)

EntryPrecoVenda.pack()


FrameMargemLucro = ctk.CTkFrame(
    FrameEntradas2,
    fg_color="transparent"
)

FrameMargemLucro.pack(
    side="left",
    padx=10
)

LabelMargemLucro = ctk.CTkLabel(
    FrameMargemLucro,
    font=("Montserrat ExtraBold", 15),
    text="Porcentagem Lucro",
    corner_radius=0
)

LabelMargemLucro.pack(
    anchor="w"
)

EntryMargemLucro = ctk.CTkEntry(
    FrameMargemLucro,
    width=400,
    height=40,
    fg_color="#F2F2F2",
    placeholder_text='50%',
    corner_radius=0,
    state = 'readonly'
)

EntryMargemLucro.pack()

#-----------------------------------------------------

LabelEstoque = ctk.CTkLabel(
    frameProduto,
    font=("Montserrat ExtraBold", 20),
    text_color="#70A5F3",
    text="Estoque",
)

LabelEstoque.pack(
    pady = (20,0),
    padx = 20,
    anchor = 'w'
)

FrameEntradas3 = ctk.CTkFrame(
    frameProduto,
    fg_color='#FAF9F9',
    width= 1400,
    height= 90
)

FrameEntradas3.pack(
    anchor="w",
    padx=10,
    pady = 10
)

FrameEntradas3.pack_propagate(False)

FrameEstoque = ctk.CTkFrame(
    FrameEntradas3,
    fg_color="transparent"
)

FrameEstoque.pack(
    side="left",
    padx=10
)

LabelEstoque = ctk.CTkLabel(
    FrameEstoque ,
    font=("Montserrat ExtraBold", 15),
    text="Estoque Inicial",
    corner_radius=0
)

LabelEstoque .pack(
    anchor="w"
)

EntryEstoque  = ctk.CTkEntry(
    FrameEstoque ,
    width=400,
    height=40,
    fg_color="#F2F2F2",
    placeholder_text='50',
    corner_radius=0,
)

EntryEstoque .pack()

FrameEstoqueMinimo = ctk.CTkFrame(
    FrameEntradas3,
    fg_color="transparent"
)

FrameEstoqueMinimo.pack(
    side="left",
    padx=10
)

LabelEstoqueMinimo = ctk.CTkLabel(
    FrameEstoqueMinimo ,
    font=("Montserrat ExtraBold", 15),
    text="Estoque",
    corner_radius=0
)

LabelEstoqueMinimo .pack(
    anchor="w"
)

EntryEstoqueMinimo  = ctk.CTkEntry(
    FrameEstoqueMinimo ,
    width=400,
    height=40,
    fg_color="#F2F2F2",
    placeholder_text='10',
    corner_radius=0,
)

EntryEstoqueMinimo.pack()

00
FrameCorredor = ctk.CTkFrame(
    FrameEntradas3,
    fg_color="transparent"
)

FrameCorredor.pack(
    side="left",
    padx=10
)

LabelCorredor = ctk.CTkLabel(
    FrameCorredor ,
    font=("Montserrat ExtraBold", 15),
    text="Corredor",
    corner_radius=0
)

LabelCorredor .pack(
    anchor="w"
)

EntryCorredor = ctk.CTkEntry(
    FrameCorredor ,
    width=400,
    height=40,
    fg_color="#F2F2F2",
    placeholder_text='3',
    corner_radius=0,
)

EntryCorredor.pack()

00

LabelObservacoes = ctk.CTkLabel(
    frameProduto,
    font=("Montserrat ExtraBold", 20),
    text_color="#70A5F3",
    text="Observações",
)

LabelObservacoes.pack(
    pady = (20,0),
    padx = 20,
    anchor = 'w'
)

FrameEntradas4 = ctk.CTkFrame(
    frameProduto,
    fg_color='#FAF9F9',
    width= 1400,
    height= 90
)

FrameEntradas4.pack(
    anchor="w",
    padx=10,
    pady = 10
)

FrameEntradas4.pack_propagate(False)

00

FrameFornecedor = ctk.CTkFrame(
    FrameEntradas4,
    fg_color="transparent"
)

FrameFornecedor.pack(
    side="left",
    padx=10
)

LabelFornecedor = ctk.CTkLabel(
    FrameFornecedor ,
    font=("Montserrat ExtraBold", 15),
    text="Fornecedor",
    corner_radius=0
)

LabelFornecedor .pack(
    anchor="w"
)

EntryFornecedor = ctk.CTkEntry(
    FrameFornecedor ,
    width=400,
    height=40,
    fg_color="#F2F2F2",
    placeholder_text='3',
    corner_radius=0,
)

EntryFornecedor.pack()

00
FrameValidade = ctk.CTkFrame(
    FrameEntradas4,
    fg_color="transparent"
)

FrameValidade.pack(
    side="left",
    padx=10
)

LabelValidade = ctk.CTkLabel(
    FrameValidade ,
    font=("Montserrat ExtraBold", 15),
    text="Validade",
    corner_radius=0
)

LabelValidade.pack(
    anchor="w"
)

EntryValidade = ctk.CTkEntry(
    FrameValidade ,
    width=400,
    height=40,
    fg_color="#F2F2F2",
    placeholder_text='22|05|2029',
    corner_radius=0,
)

EntryValidade.pack()
    
00
FrameObservacao = ctk.CTkFrame(
    FrameEntradas4,
    fg_color="transparent"
)

FrameObservacao.pack(
    side="left",
    padx=10
)

LabelObservacao = ctk.CTkLabel(
    FrameObservacao ,
    font=("Montserrat ExtraBold", 15),
    text="Observação",
    corner_radius=0
)

LabelObservacao.pack(
    anchor="w"
)

EntryObservacao= ctk.CTkEntry(
    FrameObservacao ,
    width=400,
    height=40,
    fg_color="#F2F2F2",
    placeholder_text='Produto de lot numero 02',
    corner_radius=0,
)

EntryObservacao.pack()    

#------------------------------ Botoes ------------------

FrameBotoesEnviarProduto = ctk.CTkFrame(
    frameProduto,
    fg_color='transparent',
    
)

FrameBotoesEnviarProduto.pack(pady = 20, anchor = 'w', padx = 20)

buttonCadastrarProduto = ctk.CTkButton(
    FrameBotoesEnviarProduto,
    fg_color= "#16A34A",
    text = 'Enviar',
    text_color= 'black'
)

buttonCadastrarProduto.pack(side = 'left', padx = 10)

buttonApagarProduto = ctk.CTkButton(
    FrameBotoesEnviarProduto,
    fg_color= "#4395E2",
    text = 'Apagar',
    text_color= 'black'
)

buttonApagarProduto.pack(side='left')

#-----------------------------------------------TELA CAIXA----------------------------------------------

TelaPesquisar = ctk.CTkFrame(
    app,
    fg_color="#FFFFFF",
    corner_radius=0
)

framePesquisar = ctk.CTkFrame(
    TelaPesquisar,
    fg_color="#FFFFFF",
    corner_radius=0,
    border_width=0.6,
    border_color="#858585"
)

framePesquisar.pack(
    side="top",
    anchor="n",
    pady=20,
    padx=20,
    fill="both",
    expand=True
)


# CLIENTE
FrameProcurarCliente = ctk.CTkFrame(
    framePesquisar,
    fg_color="#FFFFFF",
    corner_radius=0,
    border_width=0.6,
    border_color="#858585",
    width=400,
    height=470,
)

FrameProcurarCliente.pack_propagate(False)

FrameProcurarCliente.pack(
    side="left",
    anchor="n",
    pady=20,
    padx=20
)


ProcurarClienteFrameAzul = ctk.CTkFrame(
    FrameProcurarCliente,
    fg_color="#3D83EC",
    corner_radius=0,
    height=70,
    border_width=1,
    border_color="#858585",
)

FrameProcurarCliente.pack_propagate(False)

ProcurarClienteFrameAzul.pack(
    side="top",
    padx=0,
    pady=0,
    fill="x"
)

0
LabelProcurarClienteTitulo = ctk.CTkLabel(
    ProcurarClienteFrameAzul,
    text="Clientes",
    text_color= 'white',
    font=("Arial", 25, "bold"),
)

LabelProcurarClienteTitulo.pack(pady='25')


# FUNCIONÁRIO
FrameProcurarFuncionario = ctk.CTkFrame(
    framePesquisar,
    fg_color="#FFFFFF",
    corner_radius=0,
    border_width=0.6,
    border_color="#858585",
    width=400,
    height=470
)

FrameProcurarFuncionario.pack_propagate(False)

FrameProcurarFuncionario.pack(
    side="left",
    anchor="n",
    pady=20,
    padx=20
)


ProcurarFuncionarioFrameAzul = ctk.CTkFrame(
    FrameProcurarFuncionario,
    fg_color="#3D83EC",
    corner_radius=0,
    height=70
)

ProcurarFuncionarioFrameAzul.pack_propagate(False)

ProcurarFuncionarioFrameAzul.pack(
    side="top",
    padx=0,
    pady=0,
    fill="x"
)



00
FrameProcurarProduto = ctk.CTkFrame(
    framePesquisar,
    fg_color="#FFFFFF",
    corner_radius=0,
    border_width=0.6,
    border_color="#858585",
    width=400,
    height=470
)

FrameProcurarProduto.pack_propagate(False)

FrameProcurarProduto.pack(
    side="left",
    anchor="n",
    pady=20,
    padx=20
)


ProcurarProdutoFrameAzul = ctk.CTkFrame(
    FrameProcurarProduto,
    fg_color="#3D83EC",
    corner_radius=0,
    height=70
)

LabelProcurarProdutoTitulo = ctk.CTkLabel(
    ProcurarProdutoFrameAzul,
    text="Pedidos",
    text_color= 'white',
    font=("Arial", 25, "bold"),
)

LabelProcurarProdutoTitulo.pack(pady='25')

ProcurarProdutoFrameAzul.pack_propagate(False)

ProcurarProdutoFrameAzul.pack(
    side="top",
    padx=0,
    pady=0,
    fill="x"
)

LabelProcurarFuncionarioTitulo = ctk.CTkLabel(
    ProcurarFuncionarioFrameAzul,
    text="Funcionários",
    text_color= 'white',
    font=("Arial", 25, "bold"),
)

LabelProcurarFuncionarioTitulo.pack(pady='25')

00

FramePesquisaCliente = ctk.CTkFrame(
    FrameProcurarCliente,
    fg_color="transparent"
)

FramePesquisaCliente.pack(
    side="left",
    anchor="nw",
    padx=10,
    pady=10
)




EntryPesquisaCliente = ctk.CTkEntry(
    FramePesquisaCliente,
    width=300,
    height=40,
    fg_color="#FFFFFF",
    placeholder_text="10",
    corner_radius=0
)

EntryPesquisaCliente.pack(
    side="left",
    padx=0,
    pady=0
)


ButtonPesquisaCliente = ctk.CTkButton(
    FramePesquisaCliente,
    width=60,
    height=40,
    corner_radius=0,
    text="⌕",
    text_color= 'white',
    font=("Arial", 30, "bold"),
    fg_color="#20C9C3",
)

ButtonPesquisaCliente.pack(
    side="left",
    padx=0,
    pady=0
)

00

FramePesquisaFuncionario = ctk.CTkFrame(
    FrameProcurarFuncionario,
    fg_color="transparent"
)

FramePesquisaFuncionario.pack(
    side="left",
    anchor="nw",
    padx=10,
    pady=10
)


EntryPesquisaFuncionario = ctk.CTkEntry(
    FramePesquisaFuncionario,
    width=300,
    height=40,
    fg_color="#FFFFFF",
    placeholder_text="10",
    corner_radius=0
)

EntryPesquisaFuncionario.pack(
    side="left",
    padx=0,
    pady=0
)


ButtonPesquisaFuncionario = ctk.CTkButton(
    FramePesquisaFuncionario,
    width=60,
    height=40,
    corner_radius=0,
    text="⌕",
    text_color="white",
    font=("Arial", 30, "bold"),
    fg_color="#20C9C3"
)

ButtonPesquisaFuncionario.pack(
    side="left",
    padx=0,
    pady=0
)

00

FramePesquisaProduto = ctk.CTkFrame(
    FrameProcurarProduto,
    fg_color="transparent"
)

FramePesquisaProduto.pack(
    side="left",
    anchor="nw",
    padx=10,
    pady=10
)


EntryPesquisaProduto = ctk.CTkEntry(
    FramePesquisaProduto,
    width=300,
    height=40,
    fg_color="#FFFFFF",
    placeholder_text="10",
    corner_radius=0
)

EntryPesquisaProduto.pack(
    side="left",
    padx=0,
    pady=0
)


ButtonPesquisaProduto = ctk.CTkButton(
    FramePesquisaProduto,
    width=60,
    height=40,
    corner_radius=0,
    text="⌕",
    text_color="white",
    font=("Arial", 30, "bold"),
    fg_color="#20C9C3"
)

ButtonPesquisaProduto.pack(
    side="left",
    padx=0,
    pady=0
)































#--------------------------------------------------------------------------
TelaConfiguracoes = ctk.CTkFrame(app,
                           fg_color="#FFFFFF",
                           corner_radius=0)

TelaAjuda = ctk.CTkFrame(app,
                           fg_color="#FFFFFF",
                           corner_radius=0)


TelaCaixa = ctk.CTkFrame(
    app,
    fg_color="#FFFFFF",
    corner_radius=0
)









app.mainloop()
