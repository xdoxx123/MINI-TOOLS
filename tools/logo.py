from rich.console import Console
from rich.text import Text
import pyfiglet
from rich.color import Color

def print_text(txt):
    console = Console()

    # Generate big ASCII art
    ascii_text = pyfiglet.figlet_format(txt)

    # Create an empty Rich Text object
    rich_text = Text()

    # Get start and end colors
    start_color = Color.from_rgb(0, 0, 255).triplet  # Blue
    """138, 43, 226"""
    end_color = Color.from_rgb(255,0,0).triplet  # BlueViolet

    def lerp(a, b, t):
        return int(a + (b - a) * t)

    # Flatten the ascii_text (no gradient per-line, only per-character)
    total_chars = len(ascii_text.replace("\n", ""))  # Total non-newline characters
    current_char = 0

    for char in ascii_text:
        if char == "\n":
            rich_text.append("\n")
        else:
            # Calculate gradient for each character
            t = current_char / total_chars
            r = lerp(start_color.red, end_color.red, t)
            g = lerp(start_color.green, end_color.green, t)
            b = lerp(start_color.blue, end_color.blue, t)
            hex_color = f"#{r:02x}{g:02x}{b:02x}"

            # Append character to rich_text with gradient color
            rich_text.append(char, style=f"bold {hex_color}")
            current_char += 1

    # Print the result to the console
    console.print(rich_text)

if __name__ == "__main__":
    print_text("test")
