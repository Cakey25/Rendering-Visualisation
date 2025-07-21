
import pygame as pg

def get_all_events() -> dict[int: bool]:
    event_flags: dict[int: bool] = {}
    
    def type_check(event, event_type):
        if event.type == event_type:
            event_flags[event_type] = True
            return True
        return False

    def key_check(event, event_key):
        if event.key == event_key:
            event_flags[event_key] = True
            return True
        return False

    for event in pg.event.get():
        type_check(event=event, event_type=pg.QUIT)
        if type_check(event=event, event_type=pg.KEYDOWN):
            key_check(event=event, event_key=pg.K_ESCAPE) 

    return event_flags

def get_event(event: int, event_flags: dict[int: bool]) -> bool:
    return event_flags.get(event, False)