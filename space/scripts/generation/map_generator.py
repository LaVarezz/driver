from space.engine.debug.logs.main_log import log_info
from space.scripts.generation.cell_generation import create_cell


def script_create_map(self, load):
    log_info("Карта создается...")
    for x in range(self.settings.battlefield_settings.BATTLEFIELD_SIZE_X):
        for y in range(self.settings.battlefield_settings.BATTLEFIELD_SIZE_Y):
            create_cell((x, y), self, load)


    log_info('Карта успешно создана!')

