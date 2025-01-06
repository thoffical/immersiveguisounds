from xbmc import Player, Monitor, GUI
import xbmcgui

def play_sound(sound_name):
    """Plays a sound by its name."""
    sound_file = GUI.getLocalizedString(32000 + sound_name)
    if sound_file:
        player = Player()
        player.play(sound_file)

def on_gui_event(event):
    if event == xbmc.GUIEVENT_ON_SHOW:
        play_sound("kodi_open")  # Use a placeholder sound for opening
    elif event == xbmc.GUIEVENT_ON_CLOSE:
        play_sound("close")
    elif event in (xbmc.GUIEVENT_NAV_NEXT, xbmc.GUIEVENT_NAV_PREVIOUS):
        play_sound("cursor")
    elif event in (xbmc.GUIEVENT_MOUSE_DOWN, xbmc.GUIEVENT_CLICK):
        play_sound("click")
    elif event == xbmc.GUIEVENT_MOUSE_UP:
        play_sound("click_back")

# Register event listeners
xbmc.Monitor().onGUIEvent(on_gui_event)
