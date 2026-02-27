from space.engine.debug.logs.main_log import log_info


class CameraControl:
    def __init__(self, main):
        self._camera_x, self._camera_y = 0, 0
        self.old_camera_x, self.old_camera_y = 0, 3
        self._zoom = 1
        self.old_zoom = 1
        self.main = main
        log_info('Камера создана!')


    @property
    def zoom(self):
        return self._zoom

    @property
    def camera_x(self):
        return self._camera_x
    @camera_x.setter
    def camera_x(self, value):
        self._camera_x = value
        self.main.manager.objects.update_visible_objects()

    @property
    def camera_y(self):
        return float(self._camera_y)
    @camera_y.setter
    def camera_y(self, value):
        self._camera_y = value
        self.main.manager.objects.update_visible_objects()

    @zoom.setter
    def zoom(self, value):
        self._zoom = float(value)
        self.main.manager.animation.rescale_sprites()
        self.main.manager.objects.update_visible_objects()

