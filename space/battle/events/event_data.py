
class EventData:
    ''' Тут нужно как-то собирать данные для отправки подписчику, но пока это просто контейнер '''

    def __init__(self, data, type, configuration=0):
        if configuration == 0:
            ''' При событии типа "у обьекта изменились параметры '''
            self.object = data['object']
            self.value = data['value']
        elif configuration == 1:
            ''' При событии типа "Обьект изменился" '''
            self.object = data['object']
        self.type = type
        self.configuration = configuration


    def __repr__(self):
        return 'Event data class'
