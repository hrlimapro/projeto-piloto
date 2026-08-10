import flet as ft

def main(page: ft.Page):
    page.title = "Pomodoro Timer"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Hello World / Setup Inicial
    text = ft.Text(
        value="🍅 Pomodoro Timer - Setup Pronto!",
        size=24,
        weight=ft.FontWeight.BOLD,
    )
    
    page.add(text)

if __name__ == "__main__":
    ft.app(target=main)
