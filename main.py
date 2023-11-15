def play_music():
    music.play(music.builtin_playable_sound_effect(soundExpression.giggle), 
    music.PlaybackMode.UNTIL_DONE)

def play_my_music():
    music.play(music.string_playable("G F G A - F E D", 120),
    music.PlaybackMode.UNTIL_DONE)

def speed():
    x = input.acceleration(Dimension.X)
    led.plot_bar_graph(x, 1023)
    if x > 300:
        music.change_tempo_by(20)
    else:
        music.change_tempo_by(-20)

input.on_button_pressed(Button.A, play_music)
input.on_button_pressed(Button.B, play_my_music)
basic.forever(speed)