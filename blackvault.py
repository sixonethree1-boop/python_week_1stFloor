import tkinter as tk
from tkinter import messagebox


# =========================================================
# LOGIN CREDENTIALS
# =========================================================

VALID_USERNAME = "admin"
VALID_PASSWORD = "BlackVault123"

MAX_ATTEMPTS = 3
login_attempts = 0


# =========================================================
# APP DESIGN
# =========================================================

BG_MAIN = "#0f172a"
BG_PANEL = "#172033"
BG_INPUT = "#1e293b"
BG_BUTTON = "#334155"

BORDER = "#475569"

TEXT_MAIN = "#f8fafc"
TEXT_SECONDARY = "#cbd5e1"
TEXT_MUTED = "#94a3b8"

ACCENT = "#38bdf8"
ACCENT_HOVER = "#7dd3fc"

SUCCESS = "#22c55e"
SUCCESS_HOVER = "#4ade80"

DANGER = "#ef4444"
DANGER_HOVER = "#f87171"

WARNING = "#facc15"


# =========================================================
# CAESAR CIPHER FUNCTIONS
# =========================================================

def caesar_encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            if char.isupper():
                base = ord("A")
            else:
                base = ord("a")

            encrypted_character = chr(
                (ord(char) - base + shift) % 26 + base
            )

            result += encrypted_character

        else:
            result += char

    return result


def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)


# =========================================================
# XOR CIPHER FUNCTIONS
# =========================================================

def xor_encrypt(text, key):
    encrypted_values = []

    for index, char in enumerate(text):
        key_character = key[index % len(key)]

        xor_value = (
            ord(char) ^ ord(key_character)
        )

        encrypted_values.append(
            f"{xor_value:02x}"
        )

    return " ".join(encrypted_values)


def xor_decrypt(encrypted_text, key):
    encrypted_values = encrypted_text.split()
    result = ""

    for index, hex_value in enumerate(encrypted_values):
        encrypted_number = int(hex_value, 16)
        key_character = key[index % len(key)]

        original_character = chr(
            encrypted_number ^ ord(key_character)
        )

        result += original_character

    return result


# =========================================================
# COMBINED ENCRYPTION AND DECRYPTION
# =========================================================

def combined_encrypt(text, shift, key):
    caesar_output = caesar_encrypt(
        text,
        shift
    )

    final_output = xor_encrypt(
        caesar_output,
        key
    )

    return final_output


def combined_decrypt(encrypted_text, shift, key):
    xor_output = xor_decrypt(
        encrypted_text,
        key
    )

    original_text = caesar_decrypt(
        xor_output,
        shift
    )

    return original_text


# =========================================================
# INPUT VALIDATION
# =========================================================

def get_shift():
    shift_text = shift_entry.get().strip()

    if shift_text == "":
        raise ValueError(
            "Please enter a Caesar shift."
        )

    try:
        shift = int(shift_text)

    except ValueError:
        raise ValueError(
            "Caesar shift must be a whole number."
        )

    if shift < 0 or shift > 25:
        raise ValueError(
            "Caesar shift must be from 0 to 25."
        )

    return shift


def get_xor_key():
    key = key_entry.get()

    if key == "":
        raise ValueError(
            "XOR passphrase cannot be empty."
        )

    if len(key) < 4:
        raise ValueError(
            "XOR passphrase must contain "
            "at least four characters."
        )

    return key


def validate_hexadecimal_text(encrypted_text):
    encrypted_values = encrypted_text.split()

    if not encrypted_values:
        raise ValueError(
            "Please enter encrypted hexadecimal text."
        )

    for value in encrypted_values:
        try:
            int(value, 16)

        except ValueError:
            raise ValueError(
                f"'{value}' is not a valid hexadecimal value."
            )


# =========================================================
# ENCRYPTION BUTTON FUNCTIONS
# =========================================================

def encrypt_button_clicked():
    try:
        message = input_text.get(
            "1.0",
            tk.END
        ).rstrip("\n")

        if message == "":
            raise ValueError(
                "Please enter a message."
            )

        shift = get_shift()
        xor_key = get_xor_key()

        encrypted = combined_encrypt(
            message,
            shift,
            xor_key
        )

        output_text.config(
            state="normal"
        )

        output_text.delete(
            "1.0",
            tk.END
        )

        output_text.insert(
            "1.0",
            encrypted
        )

        output_text.config(
            state="disabled"
        )

        status_label.config(
            text=(
                "ENCRYPTION COMPLETE  |  "
                "CAESAR → XOR → HEX"
            ),
            fg=ACCENT
        )

    except ValueError as error:
        messagebox.showerror(
            "Invalid Input",
            str(error)
        )


def decrypt_button_clicked():
    try:
        encrypted_text = input_text.get(
            "1.0",
            tk.END
        ).strip()

        if encrypted_text == "":
            raise ValueError(
                "Please enter encrypted hexadecimal text."
            )

        validate_hexadecimal_text(
            encrypted_text
        )

        shift = get_shift()
        xor_key = get_xor_key()

        decrypted = combined_decrypt(
            encrypted_text,
            shift,
            xor_key
        )

        output_text.config(
            state="normal"
        )

        output_text.delete(
            "1.0",
            tk.END
        )

        output_text.insert(
            "1.0",
            decrypted
        )

        output_text.config(
            state="disabled"
        )

        status_label.config(
            text=(
                "DECRYPTION COMPLETE  |  "
                "HEX → XOR → CAESAR"
            ),
            fg=SUCCESS
        )

    except ValueError as error:
        messagebox.showerror(
            "Decryption Failed",
            str(error)
        )


def copy_result_to_input():
    output_text.config(
        state="normal"
    )

    result = output_text.get(
        "1.0",
        tk.END
    ).rstrip("\n")

    output_text.config(
        state="disabled"
    )

    if result == "":
        messagebox.showinfo(
            "No Result",
            "There is no result to copy."
        )
        return

    input_text.delete(
        "1.0",
        tk.END
    )

    input_text.insert(
        "1.0",
        result
    )

    status_label.config(
        text="RESULT COPIED TO INPUT",
        fg=WARNING
    )


def copy_result_to_clipboard():
    output_text.config(
        state="normal"
    )

    result = output_text.get(
        "1.0",
        tk.END
    ).rstrip("\n")

    output_text.config(
        state="disabled"
    )

    if result == "":
        messagebox.showinfo(
            "No Result",
            "There is no result to copy."
        )
        return

    root.clipboard_clear()
    root.clipboard_append(result)

    status_label.config(
        text="RESULT COPIED TO CLIPBOARD",
        fg=WARNING
    )


def clear_fields():
    input_text.delete(
        "1.0",
        tk.END
    )

    output_text.config(
        state="normal"
    )

    output_text.delete(
        "1.0",
        tk.END
    )

    output_text.config(
        state="disabled"
    )

    shift_entry.delete(
        0,
        tk.END
    )

    shift_entry.insert(
        0,
        " "
    )

    key_entry.delete(
        0,
        tk.END
    )

    key_entry.insert(
        0,
        " "
    )

    show_xor_key_var.set(False)
    key_entry.config(show="●")

    status_label.config(
        text="SYSTEM READY",
        fg=TEXT_MUTED
    )

    input_text.focus()


# =========================================================
# LOGIN FUNCTIONS
# =========================================================

def login():
    global login_attempts

    entered_username = (
        username_entry.get().strip()
    )

    entered_password = (
        password_entry.get()
    )

    if (
        entered_username == VALID_USERNAME
        and entered_password == VALID_PASSWORD
    ):
        login_attempts = 0

        username_entry.delete(
            0,
            tk.END
        )

        password_entry.delete(
            0,
            tk.END
        )

        login_status.config(
            text="ACCESS GRANTED",
            fg=SUCCESS
        )

        show_main_application()

    else:
        login_attempts += 1

        remaining_attempts = (
            MAX_ATTEMPTS - login_attempts
        )

        password_entry.delete(
            0,
            tk.END
        )

        password_entry.focus()

        if remaining_attempts > 0:
            login_status.config(
                text=(
                    "ACCESS DENIED  |  "
                    f"{remaining_attempts} "
                    "ATTEMPT(S) REMAINING"
                ),
                fg=DANGER
            )

            messagebox.showerror(
                "Access Denied",
                "Incorrect username or password."
            )

        else:
            login_status.config(
                text="SYSTEM LOCKED",
                fg=DANGER
            )

            login_button.config(
                state="disabled"
            )

            username_entry.config(
                state="disabled"
            )

            password_entry.config(
                state="disabled"
            )

            messagebox.showerror(
                "System Locked",
                "Maximum login attempts reached.\n\n"
                "Restart the application to try again."
            )


def toggle_password():
    if show_password_var.get():
        password_entry.config(show="")
    else:
        password_entry.config(show="●")


def toggle_xor_key():
    if show_xor_key_var.get():
        key_entry.config(show="")
    else:
        key_entry.config(show="●")


def move_to_password(event=None):
    password_entry.focus()


def show_main_application():
    login_frame.pack_forget()

    main_application_frame.pack(
        fill="both",
        expand=True
    )

    root.title(
        "IWC Black Vault"
    )

    input_text.focus()


def logout():
    clear_fields()

    main_application_frame.pack_forget()

    login_frame.pack(
        fill="both",
        expand=True
    )

    username_entry.config(
        state="normal"
    )

    password_entry.config(
        state="normal"
    )

    login_button.config(
        state="normal"
    )

    username_entry.delete(
        0,
        tk.END
    )

    password_entry.delete(
        0,
        tk.END
    )

    show_password_var.set(False)
    password_entry.config(show="●")

    login_status.config(
        text="AUTHORIZED PERSONNEL ONLY",
        fg=TEXT_MUTED
    )

    root.title(
        "IWC Black Vault - Login"
    )

    username_entry.focus()


# =========================================================
# MAIN WINDOW
# =========================================================

root = tk.Tk()

root.title(
    "IWC Black Vault - Login"
)

root.geometry(
    "900x760"
)

root.resizable(
    False,
    False
)

root.configure(
    bg=BG_MAIN
)

# Uncomment this when blackvault.ico is in the same folder:
# root.iconbitmap("blackvault.ico")


# =========================================================
# LOGIN SCREEN
# =========================================================

login_frame = tk.Frame(
    root,
    bg=BG_MAIN
)

login_frame.pack(
    fill="both",
    expand=True
)


login_container = tk.Frame(
    login_frame,
    bg=BG_PANEL,
    highlightbackground=BORDER,
    highlightthickness=1,
    padx=45,
    pady=38
)

login_container.place(
    relx=0.5,
    rely=0.5,
    anchor="center",
    width=450,
    height=520
)


login_icon = tk.Label(
    login_container,
    text="▣",
    font=("Consolas", 42, "bold"),
    bg=BG_PANEL,
    fg=ACCENT
)

login_icon.pack(
    pady=(0, 8)
)


login_title = tk.Label(
    login_container,
    text="IWC BLACK VAULT",
    font=("Arial", 25, "bold"),
    bg=BG_PANEL,
    fg=TEXT_MAIN
)

login_title.pack()


login_subtitle = tk.Label(
    login_container,
    text="SECURE ACCESS TERMINAL",
    font=("Consolas", 10, "bold"),
    bg=BG_PANEL,
    fg=TEXT_MUTED
)

login_subtitle.pack(
    pady=(5, 30)
)


username_label = tk.Label(
    login_container,
    text="USERNAME",
    font=("Consolas", 10, "bold"),
    bg=BG_PANEL,
    fg=TEXT_SECONDARY
)

username_label.pack(
    anchor="w"
)


username_entry = tk.Entry(
    login_container,
    font=("Consolas", 12),
    bg=BG_INPUT,
    fg=TEXT_MAIN,
    insertbackground=ACCENT,
    relief="flat",
    highlightbackground=BORDER,
    highlightcolor=ACCENT,
    highlightthickness=1
)

username_entry.pack(
    fill="x",
    ipady=8,
    pady=(6, 18)
)


password_label = tk.Label(
    login_container,
    text="PASSWORD",
    font=("Consolas", 10, "bold"),
    bg=BG_PANEL,
    fg=TEXT_SECONDARY
)

password_label.pack(
    anchor="w"
)


password_entry = tk.Entry(
    login_container,
    font=("Consolas", 12),
    bg=BG_INPUT,
    fg=TEXT_MAIN,
    insertbackground=ACCENT,
    show="●",
    relief="flat",
    highlightbackground=BORDER,
    highlightcolor=ACCENT,
    highlightthickness=1
)

password_entry.pack(
    fill="x",
    ipady=8,
    pady=(6, 8)
)


show_password_var = tk.BooleanVar()

show_password_check = tk.Checkbutton(
    login_container,
    text="Show password",
    variable=show_password_var,
    command=toggle_password,
    font=("Arial", 9),
    bg=BG_PANEL,
    fg=TEXT_MUTED,
    activebackground=BG_PANEL,
    activeforeground=TEXT_MAIN,
    selectcolor=BG_INPUT,
    cursor="hand2"
)

show_password_check.pack(
    anchor="w"
)


login_button = tk.Button(
    login_container,
    text="ENTER",
    command=login,
    font=("Arial", 11, "bold"),
    bg=ACCENT,
    fg="#082f49",
    activebackground=ACCENT_HOVER,
    activeforeground="#082f49",
    relief="flat",
    cursor="hand2"
)

login_button.pack(
    fill="x",
    ipady=8,
    pady=(22, 18)
)


login_status = tk.Label(
    login_container,
    text="AUTHORIZED PERSONNEL ONLY",
    font=("Consolas", 9, "bold"),
    bg=BG_PANEL,
    fg=TEXT_MUTED
)

login_status.pack()


username_entry.focus()

username_entry.bind(
    "<Return>",
    move_to_password
)

password_entry.bind(
    "<Return>",
    lambda event: login()
)


# =========================================================
# MAIN APPLICATION SCREEN
# =========================================================

main_application_frame = tk.Frame(
    root,
    bg=BG_MAIN
)


top_bar = tk.Frame(
    main_application_frame,
    bg=BG_MAIN
)

top_bar.pack(
    fill="x",
    padx=35,
    pady=(20, 5)
)


title_area = tk.Frame(
    top_bar,
    bg=BG_MAIN
)

title_area.pack(
    side="left"
)


title_label = tk.Label(
    title_area,
    text="BLACK VAULT",
    font=("Arial", 24, "bold"),
    bg=BG_MAIN,
    fg=TEXT_MAIN
)

title_label.pack(
    anchor="w"
)


subtitle_label = tk.Label(
    title_area,
    text="CAESAR + XOR ENCRYPTION SYSTEM",
    font=("Consolas", 10, "bold"),
    bg=BG_MAIN,
    fg=ACCENT
)

subtitle_label.pack(
    anchor="w",
    pady=(2, 0)
)


logout_button = tk.Button(
    top_bar,
    text="LOGOUT",
    command=logout,
    width=10,
    font=("Arial", 9, "bold"),
    bg=BG_BUTTON,
    fg=DANGER_HOVER,
    activebackground=BORDER,
    activeforeground="#ffffff",
    relief="flat",
    cursor="hand2"
)

logout_button.pack(
    side="right",
    pady=10,
    ipady=4
)


main_frame = tk.Frame(
    main_application_frame,
    bg=BG_PANEL,
    highlightbackground=BORDER,
    highlightthickness=1,
    padx=25,
    pady=22
)

main_frame.pack(
    padx=35,
    pady=15,
    fill="both",
    expand=True
)


input_label = tk.Label(
    main_frame,
    text="MESSAGE OR ENCRYPTED HEXADECIMAL TEXT",
    font=("Consolas", 10, "bold"),
    bg=BG_PANEL,
    fg=TEXT_SECONDARY
)

input_label.pack(
    anchor="w"
)


input_text = tk.Text(
    main_frame,
    height=7,
    font=("Consolas", 11),
    bg=BG_INPUT,
    fg=TEXT_MAIN,
    insertbackground=ACCENT,
    selectbackground="#0c4a6e",
    selectforeground=TEXT_MAIN,
    relief="flat",
    highlightbackground=BORDER,
    highlightcolor=ACCENT,
    highlightthickness=1,
    wrap="word"
)

input_text.pack(
    fill="x",
    pady=(8, 18)
)

settings_frame = tk.Frame(
    main_frame,
    bg=BG_PANEL
)

settings_frame.pack(
    fill="x",
    pady=5
)

# Parehong lapad ang dalawang columns
settings_frame.grid_columnconfigure(
    0,
    weight=1,
    uniform="settings"
)

settings_frame.grid_columnconfigure(
    1,
    weight=1,
    uniform="settings"
)


# =========================================================
# CAESAR SHIFT
# =========================================================

shift_label = tk.Label(
    settings_frame,
    text="CAESAR SHIFT",
    font=("Consolas", 10, "bold"),
    bg=BG_PANEL,
    fg=TEXT_SECONDARY
)

shift_label.grid(
    row=0,
    column=0,
    sticky="w",
    padx=(0, 15)
)


shift_entry = tk.Entry(
    settings_frame,
    font=("Consolas", 11),
    bg=BG_INPUT,
    fg=TEXT_MAIN,
    insertbackground=ACCENT,
    relief="flat",
    highlightbackground=BORDER,
    highlightcolor=ACCENT,
    highlightthickness=1
)

shift_entry.grid(
    row=1,
    column=0,
    sticky="ew",
    padx=(0, 15),
    pady=(6, 3),
    ipady=6
)

shift_entry.insert(
    0,
    ""
)


# =========================================================
# XOR KEY / PASSPHRASE
# =========================================================

key_label = tk.Label(
    settings_frame,
    text="XOR KEY / PASSPHRASE",
    font=("Consolas", 10, "bold"),
    bg=BG_PANEL,
    fg=TEXT_SECONDARY
)

key_label.grid(
    row=0,
    column=1,
    sticky="w",
    padx=(15, 0)
)


key_entry = tk.Entry(
    settings_frame,
    font=("Consolas", 11),
    bg=BG_INPUT,
    fg=TEXT_MAIN,
    insertbackground=ACCENT,
    show="●",
    relief="flat",
    highlightbackground=BORDER,
    highlightcolor=ACCENT,
    highlightthickness=1
)

key_entry.grid(
    row=1,
    column=1,
    sticky="ew",
    padx=(15, 0),
    pady=(6, 3),
    ipady=6
)

key_entry.insert(
    0,
    ""
)


show_xor_key_var = tk.BooleanVar()

show_xor_key_check = tk.Checkbutton(
    settings_frame,
    text="Show XOR passphrase",
    variable=show_xor_key_var,
    command=toggle_xor_key,
    font=("Arial", 9),
    bg=BG_PANEL,
    fg=TEXT_MUTED,
    activebackground=BG_PANEL,
    activeforeground=TEXT_MAIN,
    selectcolor=BG_INPUT,
    cursor="hand2"
)

show_xor_key_check.grid(
    row=2,
    column=1,
    sticky="w",
    padx=(15, 0),
    pady=(2, 0)
)

shift_spacer = tk.Label(
    settings_frame,
    text="",
    font=("Arial", 9),
    bg=BG_PANEL
)

shift_spacer.grid(
    row=2,
    column=0,
    sticky="w",
    padx=(0, 15),
    pady=(2, 0)
)


# =========================================================
# BUTTON CONTAINER
# =========================================================

button_frame = tk.Frame(
    main_frame,
    bg=BG_PANEL
)

button_frame.pack(
    pady=16
)


encrypt_button = tk.Button(
    button_frame,
    text="ENCRYPT",
    width=14,
    command=encrypt_button_clicked,
    bg=ACCENT,
    fg="#082f49",
    activebackground=ACCENT_HOVER,
    activeforeground="#082f49",
    relief="flat",
    font=("Arial", 10, "bold"),
    cursor="hand2"
)

encrypt_button.grid(
    row=0,
    column=0,
    padx=5,
    ipady=5
)


decrypt_button = tk.Button(
    button_frame,
    text="DECRYPT",
    width=14,
    command=decrypt_button_clicked,
    bg=SUCCESS,
    fg="#052e16",
    activebackground=SUCCESS_HOVER,
    activeforeground="#052e16",
    relief="flat",
    font=("Arial", 10, "bold"),
    cursor="hand2"
)

decrypt_button.grid(
    row=0,
    column=1,
    padx=5,
    ipady=5
)


copy_input_button = tk.Button(
    button_frame,
    text="RESULT TO INPUT",
    width=16,
    command=copy_result_to_input,
    bg=BG_BUTTON,
    fg=TEXT_MAIN,
    activebackground=BORDER,
    activeforeground=TEXT_MAIN,
    relief="flat",
    font=("Arial", 9, "bold"),
    cursor="hand2"
)

copy_input_button.grid(
    row=0,
    column=2,
    padx=5,
    ipady=6
)


copy_clipboard_button = tk.Button(
    button_frame,
    text="COPY",
    width=10,
    command=copy_result_to_clipboard,
    bg=BG_BUTTON,
    fg=TEXT_MAIN,
    activebackground=BORDER,
    activeforeground=TEXT_MAIN,
    relief="flat",
    font=("Arial", 9, "bold"),
    cursor="hand2"
)

copy_clipboard_button.grid(
    row=0,
    column=3,
    padx=5,
    ipady=6
)


clear_button = tk.Button(
    button_frame,
    text="CLEAR",
    width=10,
    command=clear_fields,
    bg=DANGER,
    fg="#ffffff",
    activebackground=DANGER_HOVER,
    activeforeground="#ffffff",
    relief="flat",
    font=("Arial", 10, "bold"),
    cursor="hand2"
)

clear_button.grid(
    row=0,
    column=4,
    padx=5,
    ipady=5
)


output_label = tk.Label(
    main_frame,
    text="RESULT",
    font=("Consolas", 10, "bold"),
    bg=BG_PANEL,
    fg=TEXT_SECONDARY
)

output_label.pack(
    anchor="w"
)


output_text = tk.Text(
    main_frame,
    height=7,
    font=("Consolas", 11),
    bg=BG_INPUT,
    fg=ACCENT,
    insertbackground=ACCENT,
    selectbackground="#0c4a6e",
    selectforeground=TEXT_MAIN,
    relief="flat",
    highlightbackground=BORDER,
    highlightcolor=ACCENT,
    highlightthickness=1,
    wrap="word",
    state="disabled"
)

output_text.pack(
    fill="x",
    pady=(8, 13)
)


status_label = tk.Label(
    main_frame,
    text="SYSTEM READY",
    font=("Consolas", 9, "bold"),
    bg=BG_PANEL,
    fg=TEXT_MUTED
)

status_label.pack(
    anchor="w"
)


warning_label = tk.Label(
    main_application_frame,
    text=(
        "IWU"
    ),
    font=("Consolas", 8),
    bg=BG_MAIN,
    fg=TEXT_MUTED
)

warning_label.pack(
    pady=(0, 15)
)


root.mainloop()