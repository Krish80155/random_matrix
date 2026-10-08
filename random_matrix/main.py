import os
import random
import shutil
import sys
import time


DURATION = 120  # 2 minutes


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def hide_cursor():
    print("\033[?25l", end="", flush=True)


def show_cursor():
    print("\033[?25h", end="", flush=True)


def generate_matrix():
    terminal = shutil.get_terminal_size((80, 24))

    width = terminal.columns
    height = terminal.lines

    # Create a falling stream for each column
    streams = []

    for _ in range(width):
        streams.append({
            "row": random.randint(-height, 0),
            "speed": random.choice([1, 1, 1, 2]),
            "length": random.randint(4, 15),
        })

    start_time = time.time()

    hide_cursor()

    try:
        while time.time() - start_time < DURATION:

            # ANSI home position
            print("\033[H", end="")

            # Create empty screen
            screen = [
                [" " for _ in range(width)]
                for _ in range(height)
            ]

            # Generate falling numbers
            for column, stream in enumerate(streams):

                row = stream["row"]
                length = stream["length"]

                for i in range(length):

                    current_row = row - i

                    if 0 <= current_row < height:
                        screen[current_row][column] = str(
                            random.randint(0, 9)
                        )

                stream["row"] += stream["speed"]

                # Restart stream after reaching bottom
                if stream["row"] - length > height:
                    stream["row"] = random.randint(-height, 0)
                    stream["speed"] = random.choice([1, 1, 1, 2])
                    stream["length"] = random.randint(4, 15)

            # Print screen
            for row in screen:
                print("".join(row))

            time.sleep(0.05)

    finally:
        show_cursor()
        clear_screen()


def main():
    print("Random Matrix")
    print("Running for 2 minutes...")
    print("Press Ctrl+C to stop.\n")

    time.sleep(1)

    try:
        clear_screen()
        generate_matrix()

    except KeyboardInterrupt:
        show_cursor()
        clear_screen()

    print("Matrix animation completed.")
    print("Thank you for using random-matrix!")


if __name__ == "__main__":
    main()