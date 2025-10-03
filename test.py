import tkinter as tk

def main():
    # Create main window
    root = tk.Tk()
    root.title("My Tkinter App")
    root.geometry("1000x800")  # Width x Height

    # Add a label
    label = tk.Label(root, text="Hello, Tkinter!", font=("Arial", 16))
    label.pack(pady=20)

    # Add a button
    button = tk.Button(root, text="Click me!!!", command=lambda: label.config(text="Button Clicked!"))
    button.pack(pady=10)

    # Run the application
    root.mainloop()

if __name__ == "__main__":
    main()

#comment