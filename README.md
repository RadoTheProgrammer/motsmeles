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

The `game` variable contain the grid and the words of the game, it's a numpy array, display it using `motsmeles.print()` or save in a file with `motsmeles.save()`

```python

motsmeles.print(game)
motsmeles.save(game,file="motsmeles.txt")
```

# CLI Usage

You can also execute the cli version

```

motsmeles PYTHON JAVA CPP HTML CSS PHP RUBY SWIFT PERL RUST -W 10 -H 10
```
