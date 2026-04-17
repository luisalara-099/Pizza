import flet as ft
 
def main(page: ft.Page):
 
    def cambiar(e):
        pepperoni.visible = switchPep.value
        Hongos.visible = switchHongos.value
        olives.visible = switcholives.value
        page.update()
 
    base = ft.Image(src="images/cheesebase.jpg", width=200, height=200)
    pepperoni = ft.Image(src="images/pepperoni.png", visible=False, width=150, height=200)
    Hongos = ft.Image(src="images/mushrooms.png", visible=False, width=150, height=200)
    olives = ft.Image(src="images/olives.png", visible=False, width=100, height=150)
 
    switchPep = ft.Switch(label="Pepperoni", on_change=cambiar)
    switchHongos = ft.Switch(label="Mushrooms", on_change=cambiar)
    switcholives = ft.Switch(label="olives", on_change=cambiar)
 
    page.add(
        ft.Row([
            ft.Stack([base, pepperoni, Hongos, olives]),
            ft.Column([switchPep, switchHongos, switcholives])
        ])
    )
 
ft.run(main=main, assets_dir="assets")
 