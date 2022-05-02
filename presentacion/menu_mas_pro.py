import curses

menu = ['Gestionar equipos', 'Gestionar ciclistas', 'Cargar resultados de una etapa', 'Consultar clasificación general o por etapas']

banner = """
  _   __         ____         _____     __           __   _     
 | | / /_ _____ / / /____ _  / ___/__  / /__  __ _  / /  (_)__ _
 | |/ / // / -_) / __/ _ `/ / /__/ _ \/ / _ \/  ' \/ _ \/ / _ `/
 |___/\_,_/\__/_/\__/\_,_/  \___/\___/_/\___/_/_/_/_.__/_/\_,_/ 
"""



def imprimir_multilinea_centrado(ventana, indice_de_fila_seleccionada, multilinea):
    multilinea = multilinea.split('\n')
    ventana.clear()
    altura_de_ventana, ancho_de_ventana = ventana.getmaxyx()
    for i, opcion in enumerate(multilinea):
        x = ancho_de_ventana//2 - len(opcion)//2
        y = altura_de_ventana//2 - len(multilinea)//2 + i
        if i == indice_de_fila_seleccionada:
            ventana.attron(curses.color_pair(1))
            ventana.addstr(y, x, opcion)
            ventana.attroff(curses.color_pair(1))
        else:
            ventana.addstr(y, x, opcion)
    ventana.refresh()



def print_menu(ventana, indice_de_fila_seleccionada):
    ventana.clear()
    altura_de_ventana, ancho_de_ventana = ventana.getmaxyx()
    for i, opcion in enumerate(menu):
        x = ancho_de_ventana//2 - len(opcion)//2
        y = altura_de_ventana//2 - len(menu)//2 + i
        if i == indice_de_fila_seleccionada:
            ventana.attron(curses.color_pair(1))
            ventana.addstr(y, x, opcion)
            ventana.attroff(curses.color_pair(1))
        else:
            ventana.addstr(y, x, opcion)
    ventana.refresh()


def print_center(stdscr, text):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    x = w//2 - len(text)//2
    y = h//2
    stdscr.addstr(y, x, text)
    stdscr.refresh()


def main(stdscr):
    # turn off cursor blinking
    curses.curs_set(0)

    # color scheme for selected row
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

    # specify the current selected row
    current_row = 0

    print('aaa')
    # print_center(stdscr,banner)

    # print the menu
    print_menu(stdscr, current_row)
    imprimir_multilinea_centrado(stdscr, current_row, banner)


    while True:
        key = stdscr.getch()

        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(menu)-1:
            current_row += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            print_center(stdscr, "You selected '{}'".format(menu[current_row]))
            stdscr.getch()
            # if user selected last row, exit the program
            if current_row == len(menu)-1:
                break
        print_menu(stdscr, current_row)


curses.wrapper(main)