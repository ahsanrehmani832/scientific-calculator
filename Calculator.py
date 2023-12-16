import math
import tkinter as tk
from tkinter import messagebox

class ScientificCalculator:
    def __init__(self):
        self.current_value = ""
        self.memory = 0

    def append_to_expression(self, value):
        self.current_value += str(value)

    def clear_expression(self):
        self.current_value = ""

    def evaluate_expression(self):
        try:
            result = eval(self.current_value)
            self.current_value = str(result)
        except Exception as e:
            messagebox.showerror("Error", "Invalid expression")

    def square_root(self):
        try:
            result = math.sqrt(float(self.current_value))
            self.current_value = str(result)
        except Exception as e:
            messagebox.showerror("Error", "Invalid input for square root")

    def save_to_memory(self):
        try:
            self.memory = float(self.current_value)
        except Exception as e:
            messagebox.showerror("Error", "Invalid input for memory")

    def recall_memory(self):
        self.current_value = str(self.memory)

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Scientific Calculator")
        self.root.geometry("400x600")
        self.root.configure(bg="#F0F0F0")

        self.calculator = ScientificCalculator()

        self.result_var = tk.StringVar()
        self.result_var.set("")

        self.create_widgets()

    def create_widgets(self):
        entry = tk.Entry(self.root, textvariable=self.result_var, justify="right", font=("Arial", 18), bd=10)
        entry.grid(row=0, column=0, columnspan=4, sticky="nsew")

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('÷', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('x', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('Reset', 4, 1), ('Ans', 4, 2), ('+', 4, 3),
            ('√', 5, 0), ('MC', 5, 1), ('MR', 5, 2), ('M+', 5, 3),
            ('.', 6, 0), ('%', 6, 1), ('^', 6, 2), ('(', 6, 3),
            (')', 7, 0), ('sin', 7, 1), ('cos', 7, 2), ('tan', 7, 3)
        ]

        for (text, row, col) in buttons:
            tk.Button(self.root, text=text, command=lambda t=text: self.on_button_click(t),
                      width=5, height=2, font=("Arial", 12, "bold"), bd=5, bg="#3399FF", fg="white").grid(row=row, column=col, padx=5, pady=5)

        # Configure row and column weights
        for i in range(8):
            self.root.grid_rowconfigure(i, weight=1)
            self.root.grid_columnconfigure(i, weight=1)

    def on_button_click(self, button_text):
        if button_text in '0123456789':
            self.calculator.append_to_expression(button_text)
        elif button_text == '.':
            if '.' not in self.calculator.current_value:
                self.calculator.append_to_expression(button_text)
        elif button_text == 'Reset':
            self.calculator.clear_expression()
        elif button_text == 'Ans':
            self.calculator.evaluate_expression()
        elif button_text == '√':
            self.calculator.square_root()
        elif button_text == 'MC':
            self.calculator.memory = 0
        elif button_text == 'MR':
            self.calculator.recall_memory()
        elif button_text == 'M+':
            self.calculator.save_to_memory()
        elif button_text == 'x':
            self.calculator.append_to_expression('*')  # Replace 'x' with '*'
        elif button_text == '÷':
            self.calculator.append_to_expression('/')  # Replace '÷' with '/'
        else:
            self.calculator.append_to_expression(button_text)

        self.result_var.set(self.calculator.current_value)

# Main function to run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
