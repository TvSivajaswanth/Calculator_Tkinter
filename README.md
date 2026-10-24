# Calculator_Tkinter

A simple desktop calculator built with Python and Tkinter. It supports brackets, powers, and a calculation history panel.

## 📸 Preview

<img width="472" height="492" alt="image" src="https://github.com/user-attachments/assets/8a03f991-e398-4d4a-bb18-e56be0894696" />

---

## Features

- Basic operations: addition, subtraction, multiplication, division
- Power operator (`^`), for example `2^3 = 8`
- Brackets, for example `2+(3*4) = 14`
- Correct order of operations (`2+3*4` gives `14`, not `20`)
- Chained calculations, for example `10+5-3 = 12`
- Last calculation shown above the display (like `6*5 = 30`)
- History list on the right with all past calculations, newest on top
- Clear History button
- Clear (`C`) button for the current input
- Input is checked before calculating, so invalid text shows `Invalid` instead of crashing
- Division by zero is handled safely

---

## Requirements

- Python 3.x
- Tkinter (comes pre-installed with Python on Windows and macOS)

On some Linux systems you may need to install it first:

```bash
sudo apt install python3-tk
```

No other libraries are needed.

---

## How to Run

1. Clone the repository:

   ```bash
   git clone https://github.com/<your-username>/Calculator_Tkinter.git
   cd Calculator_Tkinter
   ```

2. Run the program:

   ```bash
   python calculator.py
   ```

   (Use `python3` instead of `python` on macOS/Linux if needed. Change `calculator.py` to match your file name.)

---

## How to Use

| Button | What it does |
|---|---|
| `0-9` and `.` | Type numbers |
| `+` `-` `*` `/` | Add, subtract, multiply, divide |
| `^` | Power (`2^3` = 8) |
| `(` `)` | Brackets |
| `=` | Calculate the result and save it to history |
| `C` | Clear the current input |
| `Clear History` | Remove all saved calculations |
| `Exit` | Close the calculator |

**Example:** press `2`, `+`, `(`, `3`, `*`, `4`, `)`, `=` and the display shows `14`. The history shows `2+(3*4) = 14`.

---

## How It Works

- Pressing a button adds its character to the entry box.
- When you press `=`, the expression is converted (`^` becomes `**`) and checked: only digits, `+ - * / . ( )` and spaces are allowed. Anything else is rejected.
- The expression is then evaluated, shown in the display, and added to the history (the small label and the list box).
- Errors such as an incomplete expression or division by zero show `Invalid`.

---

## Project Structure

```
Calculator_Tkinter/
├── calculator.py    # main program
└── README.md
```

---

## Future Improvements

- Replace `eval` with a custom parser or the `ast` module
- Keyboard input support
- Backspace button
- Save history to a text file so it survives closing the app
- Clicking a history item puts it back in the display
- Dark mode and a nicer modern look
- Percentage, square root and other scientific functions

---

## What I Learned

- Building a GUI with Tkinter (`Entry`, `Button`, `Label`, `Listbox`, `grid`)
- Handling button clicks with functions and `lambda`
- Validating user input and handling errors with `try/except`
- Organizing a project and documenting it on GitHub

---

## Author

Made by **<Tv.Siva Jaswanth>**. Feel free to open an issue or suggest improvements.

## License

This project is open source.
