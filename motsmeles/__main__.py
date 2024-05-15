from .game import generate, DEFAULT_HEIGHT, DEFAULT_WIDTH
def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="générateur de mots mêlés")
    parser.add_argument("words", nargs="+", help="les mots à placer")
    parser.add_argument("-W", "--width", type=int, default=DEFAULT_WIDTH, help="the width of the grid")
    parser.add_argument("-H", "--height", type=int, default=DEFAULT_HEIGHT, help="the height of the grid")
    #parser.add_argument("-o", "--output-file", help="fichier de sortie")
    parser.add_argument("-d","--no-diagonal", action="store_true", help="no diagonal words")
    parser.add_argument("-r","--no-reverse", action="store_true", help="no reverse words")
    args=parser.parse_args()
    grid,answers=generate(
        args.words,
        args.width,
        args.height,
        no_diagonal=args.no_diagonal,
        no_reverse=args.no_reverse,
        )
    print(grid)
    print(answers)
if __name__=="__main__":
    main()