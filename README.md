 This is a word crossing game generator, install it with `pip3 install motsmeles`

# Usage

To use it, just import the library

```python
import motsmeles

game,answers=motsmeles.generate(
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



```

The `game` variable contain the grid and the words of the game, you can display it or save it in a file

```python

print(game)
game.save("mygame.txt")
```

# Solver

You can also load a game from a file

```python
game = motsmeles.load("game1.txt")
```

And then solve it

```python
answers=game.solve()
print(answers)
```

# CLI Usage

You can generate a game using the command gen:

```

motsmeles gen PYTHON JAVA CPP HTML CSS PHP RUBY SWIFT PERL RUST -W 10 -H 10
```

Or solve a game using the command `solve`, where you need to insert the file arg where the game is

```

motsmeles solve game1.txt
```
