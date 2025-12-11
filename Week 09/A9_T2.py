
import sys

def main() -> None:
    print("Program starting.")
    feed = input("Insert exit code (0-255): ")
    ExitCode = int(feed)
    if ExitCode == 0:
        print("Clean exit.")
    else:
        print("Error code")
    sys.exit(ExitCode)
    print("Program ending.")
    return None

main()
