import motsmeles

grid,answers=motsmeles.Grid.generate(
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
print(answers)
print(grid.solve())#


