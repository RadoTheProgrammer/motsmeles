import argparse

def add(args):
    result = args.x + args.y
    print(f"The result of addition is: {result}")

def subtract(args):
    result = args.x - args.y
    print(f"The result of subtraction is: {result}")

def main():
    parser = argparse.ArgumentParser(description="A simple calculator with subcommands")
    
    #parser.add_argument("text",type=str,help="text to print")
    subparsers = parser.add_subparsers(title="subcommands", description="valid subcommands", help="additional help", dest='command')
    #subparsers.required = True

    # Create the parser for the "add" command
    parser_add = subparsers.add_parser('add', help='add two integers')
    parser_add.add_argument('x', type=int, help='first integer')
    parser_add.add_argument('y', type=int, help='second integer')
    parser_add.set_defaults(func=add)

    # Create the parser for the "subtract" command
    parser_subtract = subparsers.add_parser('subtract', help='subtract two integers')
    parser_subtract.add_argument('x', type=int, help='first integer')
    parser_subtract.add_argument('y', type=int, help='second integer')
    parser_subtract.set_defaults(func=subtract)

    # Parse the arguments
    args = parser.parse_args()
    print(args.command)
    args.func(args)

if __name__ == "__main__":
    main()
