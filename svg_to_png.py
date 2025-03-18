import os
from cairosvg import svg2png

def convert_svg_to_png():
    # Создаем выходную директорию, если она не существует
    if not os.path.exists('./png_out'):
        os.makedirs('./png_out')
    
    # Получаем список всех SVG файлов
    svg_files = [f for f in os.listdir('./svg_in') if f.endswith('.svg')]
    
    for svg_file in svg_files:
        input_path = os.path.join('./svg_in', svg_file)
        output_path = os.path.join('./png_out', os.path.splitext(svg_file)[0] + '.png')
        
        try:
            # Конвертируем SVG в PNG с прозрачным фоном
            svg2png(url=input_path, write_to=output_path, output_width=1024, output_height=1024)
            print(f'Успешно конвертирован: {svg_file}')
        except Exception as e:
            print(f'Ошибка при конвертации {svg_file}: {str(e)}')

if __name__ == '__main__':
    convert_svg_to_png()
