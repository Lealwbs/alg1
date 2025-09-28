import sys

def main( argv=sys.argv, argc=len(sys.argv) ):
    print(f"Arguments count: {argc}")
    for i, arg in enumerate(argv):
        print(f"Argument {i}: {arg}")


if __name__ == "__main__":
    main()