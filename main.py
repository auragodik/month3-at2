import flet as ft 
from datetime import datetime
def main(page: ft.Page):
    page.title = 'Мое первое приложение'
    greeting_text = ft.Text("Hello world")
    greeting_history = []
    history_text = ft.Text('история приветствий:')


    def on_button_click(_):
        name = name_input.value.strip()
        print(name)  

        # print(greeting_text.value)
        timestamp = datetime.now().strftime('%H:%M')
        if name:
            greeting_text.value = f'{timestamp} Hello {name}'
            name_input.value = ''
            greeting_history.append(f'{timestamp} - {name}')
            history_text.value = 'история приветствий:\n' + '\n'.join(greeting_history)
        else:
            greeting_text.value = 'введите корректное имя'
            greeting_text.color = ft.Colors.RED


        # print(greeting_text.value)
        page.update()

    name_input = ft.TextField(label='Введите имя', on_submit=on_button_click)
    name_button = ft.ElevatedButton('send', icon=ft.Icons.SEND, on_click=on_button_click)
    # name_button_text = ft.TextButton('send')
    # name_button_icon = ft.IconButton(icon=ft.Icons.SEND)

    page.add(greeting_text, name_input, name_button, history_text)


ft.app(target=main)