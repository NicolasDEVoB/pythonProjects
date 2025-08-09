import dearpygui.dearpygui as dpg

dpg.create_context()

# Função para calcular o resultado
def calcular(sender, app_data, user_data):
    try:
        expressao = dpg.get_value("entrada")
        resultado = eval(expressao)
        dpg.set_value("resultado", f"= {resultado}")
    except Exception as e:
        dpg.set_value("resultado", "Erro")

# Função para adicionar texto à entrada
def adicionar_texto(sender, app_data, user_data):
    texto_atual = dpg.get_value("entrada")
    dpg.set_value("entrada", texto_atual + user_data)

# Função para limpar a entrada
def limpar(sender, app_data, user_data):
    dpg.set_value("entrada", "")
    dpg.set_value("resultado", "")

# Interface da Calculadora
with dpg.window(label="Calculadora", width=300, height=400):
    dpg.add_input_text(tag="entrada", readonly=True, width=250)
    dpg.add_text("", tag="resultado")
    dpg.add_spacing(count=2)

    # Botões numéricos e operadores
    botoes = [
        ["7", "8", "9", "/"],
        ["4", "5", "6", "*"],
        ["1", "2", "3", "-"],
        ["0", ".", "C", "+"],
    ]

    for linha in botoes:
        with dpg.group(horizontal=True):
            for btn in linha:
                if btn == "C":
                    dpg.add_button(label=btn, width=60, callback=limpar)
                else:
                    dpg.add_button(label=btn, width=60,
                                   callback=adicionar_texto, user_data=btn)

    # Botão de calcular "="
    dpg.add_spacing(count=1)
    dpg.add_button(label="=", width=250, height=40, callback=calcular)

dpg.create_viewport(title="Calculadora DPG", width=300, height=400)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
