from project.data.protocols.protocols import MainLike
from project.engine.events.event_types import EventTypes

def activate_function(main: MainLike, data):
    main.events.emit(EventTypes.ACTIVATEFUNCTION, data)
