'''
Менеджер состояний нажатий. Переключает состояния и при необходимости обращается к cell.trigger
'''
from space.engine.debug.logs.main_log import log_info
from space.scripts.utils.exit import hardcore_exit
from space.settings.constants.click_constants import ClickStates
from space.settings.constants.trigger_constants import Triggers


class ClickManager:
    def __init__(self, main):
        try:
            self.main = main
            self.state = None
        except Exception as e:
            log_info(f'Ошибка {e} при подключении менеджера нажатий.')
            hardcore_exit(self.main, e)
            raise e
        else:
            log_info('Менеджер нажатий подключен успешно')


    def set_state(self, state):
        self.state = state
        cursor = self.main.manager.cursor
        if state == ClickStates.SelectShipState:
            cursor.cell.trigger(Triggers.INFORMATION_CLICK)
            cursor.selecting_state = ClickStates.SelectMoveCellState

        if state == ClickStates.SelectMoveCellState:
            cursor.reset_cursor_choice() if cursor.cell.trigger(Triggers.MOVING_CLICK) else None

        if state == ClickStates.SelectAttackCellState:
            cursor.cell.trigger(Triggers.ATTACK_CLICK)