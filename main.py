import time

import flet as ft
import random

from models.lien import Lien


def main(page: ft.Page) -> None:
    page.bgcolor = ft.colors.TRANSPARENT
    page.scroll = ft.ScrollMode.HIDDEN
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT
    page.fonts = {
        "Inter": "fonts/Inter-VariableFont_opsz,wght.ttf"
    }

    img_s = ["nature.jpg", "bg.png", "natbig.png", "nat.jpg"]
    for i in random.sample(img_s, len(img_s)):
        page.decoration = ft.BoxDecoration(
            bgcolor="#5F44AB",
            image=ft.DecorationImage(
                src=i,
                fit=ft.ImageFit.FILL
            )
        )

    def visible(e: ft.ControlEvent) -> None:
        e.control.parent.parent.parent.parent.visible = False
        e.page.update()

    def visible2(e: ft.ControlEvent) -> None:
        anim.visible = True
        anim.content = login
        e.page.update()

    def switched(e: ft.ControlEvent) -> None:
        if anim.content.data == "register":
            anim.content = login
        else:
            anim.content = register
        anim.update()


    logo = ft.Text(
        value="LOGO",
        color=ft.colors.WHITE,
        size=32,
        font_family="Inter",
    )

    btn = ft.ElevatedButton(
        text="Login",
        bgcolor=ft.colors.TRANSPARENT,
        color=ft.colors.WHITE,
        adaptive=True,
        on_click=visible2
    )

    nav = ft.Row(
        spacing=92,
        controls=[
            Lien(lien="Home"),
            Lien(lien="Services"),
            Lien(lien="Contact"),
            Lien(lien="About"),
            btn
        ]
    )


    header = ft.Row(
        spacing=324,
        controls=[
            logo, nav
        ]
    )

    login = ft.Container(
        border=ft.border.all(width=1, color=ft.colors.WHITE),
        blur=(19, 19),
        width=470, height=539,
        border_radius=20,
        visible=True,
        bgcolor=ft.colors.with_opacity(opacity=0.2, color="#D9D9D9"),
        content=ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True,
            controls=[
                ft.Container(
                    bgcolor="#290042",
                    border_radius=ft.border_radius.only(top_left=15, bottom_right=15),
                    width=40, height=40,
                    #alignment=ft.alignment.top_right,
                    margin=ft.margin.only(top=15, left=420),
                    content=ft.IconButton(
                        icon=ft.icons.CLOSE,
                        expand=True,
                        icon_color=ft.colors.WHITE,
                        on_click=visible
                    )
                ),
                ft.Text(
                    value="Login",
                    font_family="Inter",
                    size=32,
                    weight=ft.FontWeight.BOLD,
                    color="#290042",
                ),
                ft.Divider(color=ft.colors.TRANSPARENT, height=12),
                ft.TextField(
                    label="Email",
                    label_style=ft.TextStyle(color="#290042"),
                    suffix_icon=ft.icons.EMAIL,
                    width=329, height=46,
                    border=ft.InputBorder.UNDERLINE,
                    border_color="#4D1471",

                ),
                ft.Divider(color=ft.colors.TRANSPARENT, height=12),
                ft.TextField(
                    label="Password",
                    label_style=ft.TextStyle(color="#290042"),
                    password=True,
                    can_reveal_password=True,
                    width=329, height=46,
                    border=ft.InputBorder.UNDERLINE,
                    border_color="#4D1471",
                ),
                ft.Row(
                    spacing=78,
                    width=320, height=38,
                    controls=[
                        ft.Row(
                            spacing=-2,
                            controls=[
                                ft.Checkbox(),
                                ft.Text(
                                    value="Remember me",
                                    color="#290042",
                                    size=13
                                )
                            ]
                        ),
                        ft.TextButton(
                            content=ft.Text(
                                value="Forget Password",
                                color="#290042",
                                size=13
                            )
                        )
                    ]
                ),
                ft.Divider(color=ft.colors.TRANSPARENT, height=18),
                ft.Container(
                    width=320, height=40,
                    bgcolor="#290042",
                    alignment=ft.alignment.center,
                    border_radius=ft.border_radius.all(value=10),
                    on_click=switched,
                    content=ft.Text(
                        value="Login",
                        color=ft.colors.WHITE,
                        size=20,
                        weight=ft.FontWeight.BOLD
                    )
                ),
                ft.Row(
                    width=256, height=25,
                    controls=[
                        ft.Text(
                            value="Don't have an account?",
                            size=16,
                            color="#290042",
                        ),
                        ft.TextButton(
                            content=ft.Text(
                                value="Register",
                                size=16,
                                color="#290042",
                                weight=ft.FontWeight.BOLD
                            ),
                            style=ft.ButtonStyle(
                                overlay_color=ft.colors.TRANSPARENT
                            ),
                            on_click=switched
                        )
                    ]
                )
            ]
        )
    )

    register = ft.Container(
        data="register",
        border=ft.border.all(width=1, color=ft.colors.WHITE),
        blur=(19, 19),
        width=470, height=539,
        border_radius=20,
        content=ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True,
            controls=[
                ft.Container(
                    bgcolor="#290042",
                    border_radius=ft.border_radius.only(top_left=15, bottom_right=15),
                    width=40, height=40,
                    # alignment=ft.alignment.top_right,
                    margin=ft.margin.only(top=15, left=420),
                    content=ft.IconButton(
                        icon=ft.icons.CLOSE,
                        expand=True,
                        icon_color=ft.colors.WHITE,
                        on_click=visible
                    )
                ),
                ft.Text(
                    value="Registration",
                    font_family="Inter",
                    size=32,
                    weight=ft.FontWeight.BOLD,
                    color="#290042",
                ),
                ft.Divider(color=ft.colors.TRANSPARENT, height=12),
                ft.TextField(
                    label="Name",
                    label_style=ft.TextStyle(color="#290042"),
                    suffix_icon=ft.icons.PERSON,
                    width=329, height=46,
                    border=ft.InputBorder.UNDERLINE,
                    border_color="#4D1471",

                ),
                ft.Divider(color=ft.colors.TRANSPARENT, height=12),
                ft.TextField(
                    label="Email",
                    label_style=ft.TextStyle(color="#290042"),
                    suffix_icon=ft.icons.EMAIL,
                    width=329, height=46,
                    border=ft.InputBorder.UNDERLINE,
                    border_color="#4D1471",

                ),
                ft.Divider(color=ft.colors.TRANSPARENT, height=12),
                ft.TextField(
                    label="Password",
                    label_style=ft.TextStyle(color="#290042"),
                    password=True,
                    can_reveal_password=True,
                    width=329, height=46,
                    border=ft.InputBorder.UNDERLINE,
                    border_color="#4D1471",
                ),
                ft.Row(
                    width=320, height=38,
                    spacing=-2,
                    controls=[
                        ft.Checkbox(),
                        ft.Text(
                            value="I agree to the terms & conditions",
                            color="#290042",
                            size=15
                        )
                    ]
                ),
                ft.Divider(color=ft.colors.TRANSPARENT, height=18),
                ft.Container(
                    width=320, height=40,
                    bgcolor="#290042",
                    alignment=ft.alignment.center,
                    border_radius=ft.border_radius.all(value=10),
                    on_click=switched,
                    content=ft.Text(
                        value="Register",
                        color=ft.colors.WHITE,
                        size=20,
                        weight=ft.FontWeight.BOLD
                    )
                ),
                ft.Row(
                    width=256, height=25,
                    controls=[
                        ft.Text(
                            value="Already have account?",
                            size=16,
                            color="#290042",
                        ),
                        ft.TextButton(
                            content=ft.Text(
                                value="Login",
                                size=16,
                                color="#290042",
                                weight=ft.FontWeight.BOLD
                            ),
                            style=ft.ButtonStyle(
                                overlay_color=ft.colors.TRANSPARENT
                            ),
                            on_click=switched
                        )
                    ]
                )
            ]
        )
    )

    anim = ft.AnimatedSwitcher(
        content=login,
        transition=ft.AnimatedSwitcherTransition.FADE,
        duration=500,
        reverse_duration=100,
        switch_in_curve=ft.AnimationCurve.EASE_IN_OUT_SINE,
        switch_out_curve=ft.AnimationCurve.EASE_IN_OUT_SINE,
        visible=False
    )

    page.add(
        ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=50,
            controls=[
                header,
                anim
            ]
        )
    )

    page.update()


ft.app(target=main, assets_dir="assets", view=ft.AppView.WEB_BROWSER)
