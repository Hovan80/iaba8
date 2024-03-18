import flet as ft

class ReportWindow(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.porosity_data = 0,
        self.porosity_number = 0
        
    def build(self):
        return ft.Column(
            controls=[
                ft.Text('Отчёт:'),
                ft.Text(f'пористость = {self.porosity_data}'),
                ft.Text('Пористость в норме'),
                ft.Text(f'Количество пор, площадь которых превышает норму: {self.porosity_number}'),
                ft.FilledButton(text='Сохранить в отчёт')
            ]
        )