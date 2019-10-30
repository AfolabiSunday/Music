import pygame

def play():
    BUFFER = 3072  # audio buffer size, number of samples since pygame 1.8.
    FREQ, SIZE, CHAN = getmixerargs()
    pygame.mixer.init(FREQ, SIZE, CHAN, BUFFER)
    file = 'HarrySong-Ft-Kiss-Daniel-Reekado-Bank-Selense.mp3'
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pass
def getmixerargs():
    pass
    pygame.mixer.init()
    freq, size, chan = pygame.mixer.get_init()
    return freq, size, chan


def initMixer():
        BUFFER = 3072  # audio buffer size, number of samples since pygame 1.8.
        FREQ, SIZE, CHAN = getmixerargs()
        pygame.mixer.init(FREQ, SIZE, CHAN, BUFFER)

def stop():
    return pygame.mixer.music.stop()

def next():
    pass

def previous():
    pass


play()
