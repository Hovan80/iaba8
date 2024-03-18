import flet as ft

class MaterialSelect(ft.Row):
    def __init__(self):
        super().__init__()
        # заменить на функцию получения данных из бд
        self.materials = [
            {
            "name": "Газоселикат",
            "square": 9,
            "square_dev": 0.8,
            "porosity": 0.09,
            "porosity_dev": 0.05
            },
            {
            "name": "Паралон",
            "square": 10,
            "square_dev": 0.3,
            "porosity": 0.04,
            "porosity_dev": 0.01   
            }
        ]
        self.curent_material = self.materials[0]
        self.text_field = ft.Text(f'Площадь поры: {self.curent_material['square']}\n Отклонение: {self.curent_material['square_dev']}\n Пористость: {self.curent_material['porosity']}\n Отклонение: {self.curent_material['porosity_dev']}')
        self.controls = [
                ft.Column(
                    controls=[
                        ft.Dropdown(
                            label='Материал',
                            on_change=self.select_change,
                            options=[ft.dropdown.Option(key=x, text=self.materials[x]['name']) for x in range(len(self.materials))]
                        ),
                        ft.FilledButton('Изменить'),
                        ft.FilledButton('Снимок')
                    ]
                ),
                self.text_field
            ]
    
    def select_change(self, e):
        self.curent_material = self.materials[int(e.data)]
        self.text_field.value = f'Площадь поры: {self.curent_material['square']}\n Отклонение: {self.curent_material['square_dev']}\n Пористость: {self.curent_material['porosity']}\n Отклонение: {self.curent_material['porosity_dev']}'
        self.update()
   