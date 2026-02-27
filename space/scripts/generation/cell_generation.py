from space.game_objects.cells.cell import Cell

def create_cell(cords, self, load):
    game = self
    window = self.main.window

    cell = Cell(cords, self)

    cell.game = game
    cell.window = window

    self.main.manager.objects.add_object(cell)

    load.draw_update_interface()


    return cell
