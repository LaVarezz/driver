from enum import Enum

from project.engine.modules.UI_modules.widget_module.widgets.basic_widget import BasicWidget
from project.engine.modules.UI_modules.widget_module.widgets.buttons.button import Button
from project.engine.modules.UI_modules.widget_module.widgets.labels.label import Label
from project.engine.modules.UI_modules.widget_module.widgets.panel.panel import Panel


class WidgetTypes(Enum):
    BasicWidget = BasicWidget
    ButtonWidget = Button
    PanelWidget = Panel
    LabelWidget = Label
