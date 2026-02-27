from space.game_objects.ships.operations.attack import attack
from space.game_objects.ships.operations.moving import move_to
from space.scripts.utils.battle_utils.get_ship import get_object
from space.scripts.utils.reselect_ship import reselect
from space.settings.constants.ship_constants import States
from space.settings.constants.trigger_constants import Triggers
from space.settings.protocols.protocols import CellLike


def cell_trigger(self:CellLike, type):
    ''' Двухэтапный скрипт.
    если состояние выбора "выделить", то выделяется корабль, а так же активируется ивент создания\удаления(если уже существует и не вылеоен новй корабль)
    панели управления.
    если состояния выбора "Двигаться", то:
    - если нажатая клетка имеет корабль, отрабатывает первый блок скрипта.
    - в противном случае, если корабль готов, активируется перемещение корабля, а затем меняется выделенный корабль на следующий в очереди.
    '''

    if type == Triggers.INFORMATION_CLICK:
        if self.content:
            main = self.game.main
            main.manager.cursor.select_ship()

            if not self.game.control_panel:
                main.manager.events.emit('selected_ship_changed_raw', None, True,
                                         object=get_object(self.game.main, main.manager.cursor.selected_ship))
            else:
                if not main.manager.cursor.selected_ship:
                    main.manager.events.emit('selected_ship_changed_raw', None, True, object=None)
                else:
                    ''' Пересоздание '''
                    main.manager.events.emit('selected_ship_changed_raw', None, True, object=None)
                    main.manager.events.emit('selected_ship_changed_raw', None, True,
                                             object=get_object(self.game.main, main.manager.cursor.selected_ship))

    elif type == Triggers.MOVING_CLICK:
        main = self.game.main
        main.manager.cursor.select_cell()
        ship = main.manager.cursor.ship
        cell = main.manager.cursor.targeted_cell
        if cell:
            if cell.content:
                self.trigger(Triggers.INFORMATION_CLICK)
            elif ship:
                ship = get_object(main, ship)
                ''' Проверка на готовность к перемещению. '''
                if ship.state == States.IDLE:
                    if ship == self.game.queue.current_mover:
                        ship.operation(move_to)
                        reselect(main)

    elif type == Triggers.ATTACK_CLICK:
        main = self.game.main
        main.manager.cursor.select_cell()
        ship = main.manager.cursor.ship
        cell = main.manager.cursor.targeted_cell

        if cell:
            if cell.content:
                if ship:
                    ship = get_object(main, ship)
                    if ship.side != get_object(self.game.main, cell.content).side:
                        if ship.state == States.IDLE:
                            if ship == self.game.queue.current_mover:
                                ship.operation(attack)
                                reselect(main)
