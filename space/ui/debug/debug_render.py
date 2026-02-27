from space.scripts.calculators.get_scripts import get_pixel_position
from space.settings.protocols.protocols import ShipLike, CellLike
from pygame import draw

def debug_ship_draw(ship: ShipLike):
    pos = get_pixel_position(ship)
    tm = ship.game.main.test_mode
    if tm.show_hp:
        ship.text_hp.draw(ship.game.main.window, (pos[0], pos[1] + 20))
    if tm.show_id:
        ship.text_id.draw(ship.game.main.window, pos)
    if tm.show_collides:
        draw.rect(ship.game.main.window, 'purple', ship.rect, 2)

def debug_ship_update(ship: ShipLike):
    tm = ship.game.main.test_mode
    if tm.show_hp:
        ship.text_hp = ship.font.render_text(f'health: {ship.health}')
    if tm.show_id:
        ship.text_id = ship.font.render_text(f"id: {ship.id}")



def debug_cell_draw(cell: CellLike):
    tm = cell.game.main.test_mode
    if tm.show_grid_position:
        cell.text_cords.draw(cell.game.main.window, (cell.kx, cell.ky))


def debug_cell_update(cell: CellLike):
    cell.kx, cell.ky = cell.rect.bottomleft
    cell.ky -= 20
    cell.kx += 10
    cell.text_cords = cell.font.render_text(f'{cell.x} {cell.y}')


def debug_show_fps(self):
    fps = str(round(self.clock.get_fps()))
    font = self.ws.GLOBAL_TEXT_CACHE['big']
    font.render_text(fps).draw(self.window, (10, 10))