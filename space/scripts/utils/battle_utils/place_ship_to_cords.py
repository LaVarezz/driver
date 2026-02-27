from space.engine.debug.logs.main_log import log_info


def place_ship_to_cords(ship, cords, game, new_ship=False):
    target_field = game.main.manager.objects.cells[cords[0]][cords[1]]
    if not new_ship:
        game.main.manager.objects.cells[ship.x][ship.y].content = None
        target_field.content = ship.id

        ship.x = cords[0]
        ship.y = cords[1]
        ship.place = target_field
        log_info(f'Ship {ship} переместился в {ship.x, ship.y}')
        # тут проигрывается анимация перемещения, пока пусто.

    else:

        target_field.content = ship.id
        ship.x = cords[0]
        ship.y = cords[1]
        log_info(f'Корабль {ship} создан в {ship.x, ship.y}')
    ship.update_ship_visual()
