from project.data.protocols.protocols import MainLike
from project.engine.events.event_types import EventTypes


def set_flag(main: MainLike, data):
    main.events.emit(EventTypes.CHANGEFLAG, data)
