import flet as ft
from image_control import ImageControl
from report import ReportWindow

class MainWindow(ft.UserControl):
    def build(self):
        return ft.GridView(
            expand=1,
            runs_count=5,
            max_extent=300,
            child_aspect_ratio=1.0,
            spacing=5,
            run_spacing=5,
            controls=[
                ImageControl(),
                ReportWindow()
            ]
        )
    
def main(page: ft.Page):
    page.add(MainWindow())
    page.update()
    
if __name__ == '__main__':
    ft.app(target=main)