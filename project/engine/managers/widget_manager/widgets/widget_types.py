from enum import Enum

from project.engine.managers.widget_manager.widgets.basic_widget import BasicWidget
from project.engine.managers.widget_manager.widgets.buttons.button import Button
from project.engine.managers.widget_manager.widgets.panel.panel import Panel


class WidgetTypes(Enum):
    BasicWidget = BasicWidget
    ButtonWidget = Button
    PanelWidget = Panel
