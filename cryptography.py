import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import tkinter.font as tkFont

def encode_message(message, shift=3):
    """Encode a message using Caesar cipher with given shift."""
    encoded = ""
    for char in message:
        if char.isalpha():
            # Shift uppercase and lowercase letters
            if char.isupper():
                encoded += chr((ord(char) - 54 + shift) % 26 + 54)
            else:
                encoded += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            # Keep non-alphabetic characters as-is
            encoded += char
    return encoded

def decode_message(encoded_message, shift=3):
    """Decode a message encoded with Caesar cipher."""
    return encode_message(encoded_message, -shift)

class CaesarCipherGUI:
    def __init__(self, root):
        self.root = root
        self.setup_window()
        self.create_widgets()
        
    def setup_window(self):
        """Configure the main window."""
        self.root.title("Caesar Cipher - Cryptography Tool")
        self.root.geometry("800x600")
        self.root.configure(bg='#2c3e50')
        self.root.resizable(True, True)
        
        # Center the window
        self.center_window()
        
    def center_window(self):
        """Center the window on screen."""
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
        
    def create_widgets(self):
        """Create and arrange all GUI widgets."""
        # Main container
        main_frame = tk.Frame(self.root, bg='#2c3e50')
        main_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Title
        title_font = tkFont.Font(family="Arial", size=24, weight="bold")
        title_label = tk.Label(
            main_frame,
            text="🔐 CRYPTOGRAPHY PBL",
            font=title_font,
            bg='#2c3e50',
            fg='#ecf0f1'
        )
        title_label.pack(pady=(0, 30))
        
        # Shift value frame
        shift_frame = tk.Frame(main_frame, bg='#2c3e50')
        shift_frame.pack(fill='x', pady=(0, 20))
        
        shift_label = tk.Label(
            shift_frame,
            text="Shift Value:",
            font=('Arial', 12, 'bold'),
            bg='#2c3e50',
            fg='#ecf0f1'
        )
        shift_label.pack(side='left')
        
        self.shift_var = tk.StringVar(value="3")
        shift_spinbox = tk.Spinbox(
            shift_frame,
            from_=1,
            to=25,
            textvariable=self.shift_var,
            width=5,
            font=('Arial', 12),
            bg='#ecf0f1',
            fg='#2c3e50',
            buttonbackground='#3498db',
            relief='flat',
            bd=2
        )
        shift_spinbox.pack(side='left', padx=(10, 0))
        
        # Input section
        input_frame = tk.LabelFrame(
            main_frame,
            text="Input Message",
            font=('Arial', 12, 'bold'),
            bg='#34495e',
            fg='#ecf0f1',
            relief='raised',
            bd=2
        )
        input_frame.pack(fill='both', expand=True, pady=(0, 15))
        
        self.input_text = scrolledtext.ScrolledText(
            input_frame,
            height=8,
            font=('Consolas', 11),
            bg='#ecf0f1',
            fg='#2c3e50',
            relief='flat',
            bd=5,
            wrap='word'
        )
        self.input_text.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Buttons frame
        button_frame = tk.Frame(main_frame, bg='#2c3e50')
        button_frame.pack(fill='x', pady=(0, 15))
        
        # Style for buttons
        button_style = {
            'font': ('Arial', 12, 'bold'),
            'relief': 'flat',
            'bd': 0,
            'cursor': 'hand2',
            'width': 12,
            'height': 2
        }
        
        encode_btn = tk.Button(
            button_frame,
            text="🔒 ENCODE",
            command=self.encode_text,
            bg='#e74c3c',
            fg='white',
            activebackground='#c0392b',
            **button_style
        )
        encode_btn.pack(side='left', padx=(0, 10))
        
        decode_btn = tk.Button(
            button_frame,
            text="🔓 DECODE",
            command=self.decode_text,
            bg='#27ae60',
            fg='white',
            activebackground='#229954',
            **button_style
        )
        decode_btn.pack(side='left', padx=(0, 10))
        
        clear_btn = tk.Button(
            button_frame,
            text="🗑️ CLEAR",
            command=self.clear_all,
            bg='#f39c12',
            fg='white',
            activebackground='#e67e22',
            **button_style
        )
        clear_btn.pack(side='left', padx=(0, 10))
        
        copy_btn = tk.Button(
            button_frame,
            text="📋 COPY",
            command=self.copy_result,
            bg='#3498db',
            fg='white',
            activebackground='#2980b9',
            **button_style
        )
        copy_btn.pack(side='left')
        
        # Output section
        output_frame = tk.LabelFrame(
            main_frame,
            text="Output Result",
            font=('Arial', 12, 'bold'),
            bg='#34495e',
            fg='#ecf0f1',
            relief='raised',
            bd=2
        )
        output_frame.pack(fill='both', expand=True)
        
        self.output_text = scrolledtext.ScrolledText(
            output_frame,
            height=8,
            font=('Consolas', 11),
            bg='#ecf0f1',
            fg='#2c3e50',
            relief='flat',
            bd=5,
            wrap='word',
            state='disabled'
        )
        self.output_text.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Status bar
        self.status_var = tk.StringVar(value="Ready")
        status_bar = tk.Label(
            main_frame,
            textvariable=self.status_var,
            font=('Arial', 10),
            bg='#34495e',
            fg='#ecf0f1',
            relief='sunken',
            bd=1,
            anchor='w'
        )
        status_bar.pack(fill='x', pady=(10, 0))
        
    def get_shift_value(self):
        """Get the current shift value from the spinbox."""
        try:
            return int(self.shift_var.get())
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid shift value (1-25)")
            return None
            
    def encode_text(self):
        """Encode the input text."""
        shift = self.get_shift_value()
        if shift is None:
            return
            
        input_message = self.input_text.get(1.0, tk.END).strip()
        if not input_message:
            messagebox.showwarning("Warning", "Please enter a message to encode")
            return
            
        try:
            encoded_message = encode_message(input_message, shift)
            self.display_output(encoded_message)
            self.status_var.set(f"Message encoded with shift {shift}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
            
    def decode_text(self):
        """Decode the input text."""
        shift = self.get_shift_value()
        if shift is None:
            return
            
        input_message = self.input_text.get(1.0, tk.END).strip()
        if not input_message:
            messagebox.showwarning("Warning", "Please enter a message to decode")
            return
            
        try:
            decoded_message = decode_message(input_message, shift)
            self.display_output(decoded_message)
            self.status_var.set(f"Message decoded with shift {shift}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
            
    def display_output(self, text):
        """Display text in the output area."""
        self.output_text.config(state='normal')
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(1.0, text)
        self.output_text.config(state='disabled')
        
    def clear_all(self):
        """Clear both input and output areas."""
        self.input_text.delete(1.0, tk.END)
        self.output_text.config(state='normal')
        self.output_text.delete(1.0, tk.END)
        self.output_text.config(state='disabled')
        self.status_var.set("Cleared all text")
        
    def copy_result(self):
        """Copy the output result to clipboard."""
        try:
            output_content = self.output_text.get(1.0, tk.END).strip()
            if output_content:
                self.root.clipboard_clear()
                self.root.clipboard_append(output_content)
                self.status_var.set("Result copied to clipboard")
            else:
                messagebox.showinfo("Info", "No result to copy")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to copy: {str(e)}")

def main():
    """Main function to run the GUI application."""
    root = tk.Tk()
    app = CaesarCipherGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()