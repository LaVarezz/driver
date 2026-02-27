def reselect(main):
    next = main.scene.game.queue.current_mover
    main.manager.cursor.select_ship(next)
    main.manager.events.emit('selected_ship_changed', None, True, object=next)
