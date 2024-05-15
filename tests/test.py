import motsmeles

game,answers=motsmeles.Game.generate(
    [
        "PYTHON",
        "JAVA",
        "CPP",
        "HTML",
        "CSS",
        "PHP",
        "RUBY",
        "SWIFT",
        "PERL",
        "RUST",
    ],
    width = 10, 
    height = 10)
#print(answers)
print(game)#
#game.save(file="mygame.txt")
game.save(file="game1.txt")

