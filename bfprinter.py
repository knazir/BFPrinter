import argparse


def generate_program(text, pretty):
    if pretty:
        joiner = '\n'
    else:
        joiner = ''
    return joiner.join(('+' * ord(character)) + '.>' for character in text)


def setup_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--pretty', help='format output with new lines', action='store_true')
    return parser.parse_args()


def main():
    args = setup_args()
    print(generate_program(raw_input("Enter string to print in BrainFu*k: "), args.pretty))


if __name__ == '__main__':
    main()