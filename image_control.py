import flet as ft

class ImageControl(ft.UserControl):
    def build(self):
        self.contrast = ft.Slider(min=0, max=100, divisions=10, label='{value}%')
        self.brightnes = ft.Slider(min=0, max=100, divisions=10, label='{value}%')
        self.sharp = ft.Slider(min=0, max=100, divisions=10, label='{value}%')
        return ft.Column(
            controls=[
                ft.Text('Контрастность'),
                self.contrast,
                ft.Text('Яркость'),
                self.brightnes,
                ft.Text('Резкость'),
                self.sharp
            ]
        )
        