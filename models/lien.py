import flet as ft


class Lien(ft.Container):
    def __init__(self, lien: str) -> None:
        self.lien = lien
        super().__init__()

        self.on_hover = self.hovered
        self.on_click = self.clicked

        self.text = ft.Text(
            value=self.lien,
            size=24,
            font_family="Inter",
            color=ft.colors.WHITE,
            weight=ft.FontWeight.NORMAL,

        )


        self.content = self.text

    @staticmethod
    def hovered(e: ft.ControlEvent) -> None:
        if e.control.content.style is None:
            e.control.content.style = ft.TextStyle(
                decoration=ft.TextDecoration.UNDERLINE,
                decoration_style=ft.TextDecorationStyle.WAVY,
                decoration_color=ft.colors.WHITE

            )
        else:
            e.control.content.style = None
        e.control.update()

    def clicked(self, e: ft.ControlEvent) -> None:
        pass