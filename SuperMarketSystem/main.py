from uuid import uuid4
import dearpygui.dearpygui as dpg
from dearpygui.dearpygui import get_value, set_value
from lib.database_functions import create, init_db, read, delete

init_db(['nome', 'id'])

dpg.create_context()

def atualizar(registros):
    set_value("texto_registros", registros)


def ler_df():
    df = read()
    return df.to_string(index=False)


def adicionar(sender, app_data, user_data):
    texto = get_value("nome")
    create([{'id' : str(uuid4()), 'nome': texto}])  # Note: create espera lista de dicts
    registros = ler_df()
    atualizar(ler_df())
    set_value("nome", "")

def deletar(sender, app_data, user_data):
    id = get_value("id")
    try:
        delete({'id' : id})
    except Exception as e:
        print(f'Erro: {e}')
    delete({'id' : id})
    atualizar(ler_df())
    set_value("id", "")


with dpg.theme(tag="monospace_theme"):
    with dpg.theme_component(dpg.mvAll):
        pass

with dpg.window(label='Minha janela', width=600, height=600):
    dpg.add_text('Adicionar Registro')

    with dpg.group(horizontal=True):
        dpg.add_input_text(label="", tag="nome")
        dpg.add_button(label="Registrar", callback=adicionar)

    dpg.add_separator()

    dpg.add_text('Deletar Registro')

    with dpg.group(horizontal=True):
        dpg.add_input_text(label="", tag="id")
        dpg.add_button(label=" Deletar ", callback=deletar)

    dpg.add_separator()

    dpg.add_text("", tag="texto_registros")
    dpg.bind_item_theme("texto_registros", "monospace_theme")# Texto que será atualizado
    dpg.add_button(label="Atualizar", callback=lambda: atualizar(ler_df()))
    atualizar(ler_df())

dpg.create_viewport(title='App De Registros', width=600, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
