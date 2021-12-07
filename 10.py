import os

for dirname, dirnames, filenames in os.walk('C:\\walk'):
    level = dirname.count(os.sep) # os.sep == /  - считаем слешы для отсупов подпипок и файлов
    indent = " " * 4 * level # пробелы отступов для папок
    #print("путь к каталогу: ",dirname)
    print(f"{indent}[{os.path.basename(dirname)}]") # os.path.basename - будет выводить только папку без пути
    sub_indent = " " * 4 * (level+1)  # пробелы отступов для файлов

    # print("список каталогов: ",dirnames) # не используем так как сделали "путь к каталогу: " os.path.basename
    #for subdirname in dirnames:
        #print("Подпапка:", subdirname, level, indent,sub_indent)
        #print(f"{sub_indent}{subdirname}")

    #print("список файлов: ", filenames)
    for filename in filenames:
        #print("Файл: ",filename)
        print(f"{sub_indent}{filename}")