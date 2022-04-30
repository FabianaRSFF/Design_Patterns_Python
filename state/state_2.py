from __future__ import annotations
from abc import ABC, abstractmethod

class Spotify:
    def __init__(self) -> None:
        self.mode: PlayMode = RadioMode(self)
        self.playing = 0
    
    def change_mode(self, mode: PlayMode) -> None:
        print(f'Changing to : {mode.__class__.__name__}')
        print()
        self.playing = 0
        self.mode = mode

    def press_next(self) -> None:
        self.mode.press_next()
        print(self)
    
    def press_prev(self) -> None:
        self.mode.press_prev()
        print(self)

    def __str__(self) -> str:
        return str(self.playing)


class PlayMode(ABC):
    def __init__(self, spotify: Spotify) -> None:
        self.spotify = spotify

    @abstractmethod
    def press_next(self) -> None: pass

    @abstractmethod
    def press_prev(self) -> None: pass


class RadioMode(PlayMode):
    def press_next(self) -> None:
        self.spotify.playing += 1000

    def press_prev(self) -> None:
        self.spotify.playing -= 1000 if self.spotify.playing > 0 else 0


class MusicMode(PlayMode):
    def press_next(self) -> None:
        self.spotify.playing += 1

    def press_prev(self) -> None:
        self.spotify.playing -= 1 if self.spotify.playing > 0 else 0


if __name__=='__main__':
    spotify = Spotify()
    spotify.press_next()
    spotify.press_next()
    spotify.press_next()
    spotify.press_next()
    spotify.press_next()
    spotify.press_prev()
    spotify.press_prev()
    spotify.press_prev()

    print()
    spotify.change_mode(MusicMode(spotify))
    spotify.press_next()
    spotify.press_next()
    spotify.press_next()
    spotify.press_next()
    spotify.press_next()
    spotify.press_prev()
    spotify.press_prev()
    spotify.press_prev()
    print()
