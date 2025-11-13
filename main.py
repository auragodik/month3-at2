import flet as ft 
from datetime import datetime

def main(page: ft.Page):
    page.title = 'Мое первое приложение'
    greeting_text = ft.Text("Hello world")
    greeting_history = []
    history_text = ft.Text('история приветствий:')
    page.theme_mode
    age_input = ft.TextField(label='введите возраст')

    def on_button_click(_):
        name = name_input.value.strip()
        age = age_input.value.strip()
        print(name)  
        print(age)
        # print(greeting_text.value)
        timestamp = datetime.now().strftime('%H:%M')
        if name:
            greeting_text.value = f'{timestamp} Hello {name}, you age {age}'
            name_input.value = ''
            age_input.value = ''
            greeting_history.append(f'{timestamp} - {name}')
            history_text.value = 'история приветствий:\n' + '\n'.join(greeting_history)
        else:
            greeting_text.value = 'введите корректное имя и возраст'
            greeting_text.color = ft.Colors.RED


        # print(greeting_text.value)
        page.update()

    name_input = ft.TextField(label='Введите имя', on_submit=on_button_click)
    name_button = ft.ElevatedButton('send', icon=ft.Icons.SEND, on_click=on_button_click)

    def clear_history(_):
        greeting_history.clear()
        print(greeting_history)
        history_text.value = 'история приветствий:'
        page.update()


    def dl_history(_):
        if greeting_history:
            greeting_history.pop()
            history_text.value = 'История приветствий:\n ' + '\n'.join(greeting_history)
        else:
            print('История пуста!')
        page.update()



    dl_button = ft.ElevatedButton('delete', on_click=dl_history)
        
    clear_button = ft.IconButton(icon=ft.Icons.DELETE, on_click=clear_history)
    # name_button_text = ft.TextButton('send')
    # name_button_icon = ft.IconButton(icon=ft.Icons.SEND)

    page.add(greeting_text, name_input, age_input, name_button, clear_button, dl_button, history_text)


ft.app(target=main)