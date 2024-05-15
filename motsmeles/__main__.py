from .game import generate, DEFAULT_HEIGHT, DEFAULT_WIDTH
def cli_generate(args):
    grid,answers=generate(
        args.words,
        args.width,
        args.height,
        no_diagonal=args.no_diagonal,
        no_reverse=args.no_reverse,)
    print(grid)
    print(answers)
def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="word cross generator")
    subparsers = parser.add_subparsers(title="subcommands", description="valid subcommands", help="additional help", dest='command')
    
    parser_generate = subparsers.add_parser("gen",help="generate a game")
    parser_generate.add_argument("words", nargs="+", help="les mots à placer")
    parser_generate.add_argument("-W", "--width", type=int, default=DEFAULT_WIDTH, help="the width of the grid")
    parser_generate.add_argument("-H", "--height", type=int, default=DEFAULT_HEIGHT, help="the height of the grid")
    parser_generate.add_argument("-d","--no-diagonal", action="store_true", help="no diagonal words")
    parser_generate.add_argument("-r","--no-reverse", action="store_true", help="no reverse words")
    parser_generate.set_defaults(func=cli_generate)
    #parser_solve = subparsers.add_parser("solve","solve a game")
    args=parser.parse_args()

    #print(grid)
    #print(answers)
if __name__=="__main__":
    main()