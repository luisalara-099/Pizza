import flet as ft

def main(page: ft.Page):

    def cambiar(e):
        pepperoni.visible = switchPep.value
        mushrooms.visible = switchMush.value
        olives.visible = switchOlives.value
        page.update()

    base = ft.Image(
        src="assets/cheesebase.jpg",
        width=300,
        height=300
    )

    pepperoni = ft.Image(
        src="assets/pepperoni.png",
        width=300,
        height=300,
        visible=False
    )

    mushrooms = ft.Image(
        src="assets/mushrooms.png",
        width=300,
        height=300,
        visible=False
    )

    olives = ft.Image(
        src="assets/olives.png",
        width=300,
        height=300,
        visible=False
    )

    switchPep = ft.Switch(label="Pepperoni", on_change=cambiar)
    switchMush = ft.Switch(label="Mushrooms", on_change=cambiar)
    switchOlives = ft.Switch(label="Olives", on_change=cambiar)

    page.add(
        ft.Row([
            ft.Stack([
                base,
                pepperoni,
                mushrooms,
                olives
            ]),
            ft.Column([
                switchPep,
                switchMush,
                switchOlives
            ])
        ])
    )

ft.app(target=main)