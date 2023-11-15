input.onButtonPressed(Button.A, function play_music() {
    music.play(music.builtinPlayableSoundEffect(soundExpression.giggle), music.PlaybackMode.UntilDone)
})
input.onButtonPressed(Button.B, function play_my_music() {
    music.play(music.stringPlayable("G F G A - F E D", 120), music.PlaybackMode.UntilDone)
})
basic.forever(function speed() {
    let x = input.acceleration(Dimension.X)
    led.plotBarGraph(x, 1023)
    if (x > 300) {
        music.changeTempoBy(20)
    } else {
        music.changeTempoBy(-20)
    }
    
})
