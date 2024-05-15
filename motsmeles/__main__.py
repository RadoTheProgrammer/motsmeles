from .game import generate, load, DEFAULT_HEIGHT, DEFAULT_WIDTH
def cli_generate(args):
    game,answers=generate(
        args.words,
        args.width,
        args.height,
        no_diagonal=args.no_diagonal,
        no_reverse=args.no_reverse,)
    print(game)
    print(answers)
    
def cli_solve(args):
    answers=load(args.file).solve()
    print(answers)
def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="word cross generator")
    subparsers = parser.add_subparsers(title="subcommands", description="valid subcommands", help="additional help", dest='command')
    
    parser_generate = subparsers.add_parser("gen",help="generate a game")
    parser_generate.add_argument("words", nargs="+", help="the words to place")
    parser_generate.add_argument("-W", "--width", type=int, default=DEFAULT_WIDTH, help="the width of the grid")
    parser_generate.add_argument("-H", "--height", type=int, default=DEFAULT_HEIGHT, help="the height of the grid")
    parser_generate.add_argument("-d","--no-diagonal", action="store_true", help="no diagonal words")
    parser_generate.add_argument("-r","--no-reverse", action="store_true", help="no reverse words")
    parser_generate.set_defaults(func=cli_generate)
    
    parser_solve = subparsers.add_parser("solve",help="solve a game")
    parser_solve.add_argument("file",type=str,help="the file of the game")
    parser_solve.set_defaults(func=cli_solve)
    args=parser.parse_args()

    args.func(args)
    #print(grid)
    #print(answers)
if __name__=="__main__":
    main()