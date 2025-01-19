import tkinter as tk
from tkinter import messagebox
import subprocess
import sys
import os
import ctypes
import webbrowser

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def disable_all_buttons():
    for button in all_buttons:
        button.config(state='disabled')

def enable_all_buttons():
    for button in all_buttons:
        button.config(state='normal')

def run_command(command, show_console=False):
    try:
        if not is_admin():
            script_path = os.path.abspath(sys.argv[0])
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, script_path, None, 1)
            root.quit()
            return
        
        disable_all_buttons()
        root.iconify()
        root.update()
        
        if show_console or command.startswith("shutdown"):
            # Run command in visible console window
            subprocess.run(
                f'start cmd /k {command}',
                shell=True,
                creationflags=subprocess.CREATE_NEW_CONSOLE
            )
        else:
            # Run command silently
            subprocess.run(
                command, 
                shell=True, 
                capture_output=True, 
                text=True, 
                creationflags=subprocess.CREATE_NO_WINDOW
            )
        
    except:
        pass
    finally:
        root.deiconify()
        enable_all_buttons()

def open_new_window():
    new_window = tk.Toplevel(root)
    new_window.title("New Window")
    new_window.geometry("400x400")  # Set size for the new window
    
    # Label for the Taskkill command
    taskkill_label = tk.Label(
        new_window,
        text="Taskkill Command:",
        font=("Consolas", 10),
        anchor='w',
        padx=5
    )
    taskkill_label.pack(pady=(10, 5))

    # Create a frame for the Taskkill command input
    taskkill_frame = tk.Frame(new_window)
    taskkill_frame.pack(fill='x', pady=(10, 5))

    # Input field for the Taskkill command (non-editable)
    taskkill_entry = tk.Entry(taskkill_frame, font=("Consolas", 10), width=40)
    taskkill_entry.insert(0, 'taskkill /F /IM [taskname]')  # Updated text
    taskkill_entry.config(state='readonly')  # Make it non-editable
    taskkill_entry.pack(side='left', padx=(0, 5))

    # Copy button for the Taskkill command
    copy_taskkill_button = tk.Button(
        taskkill_frame,
        text="Copy",
        command=lambda: root.clipboard_clear() or root.clipboard_append(taskkill_entry.get()),
        width=8,
        height=1,
        bg='#4CAF50',
        fg='white',
        font=("Arial", 9, "bold")
    )
    copy_taskkill_button.pack(side='right')  # Position the copy button on the right side

    # Add a black line separator after the Taskkill command
    separator_taskkill = tk.Frame(new_window, height=1, bg='black')
    separator_taskkill.pack(fill='x', padx=5, pady=(5, 5))  # Added padding for spacing

    # Label for the Hide Folder command
    hide_folder_label = tk.Label(
        new_window,
        text="Hide Folder Command:",
        font=("Consolas", 10),
        anchor='w',
        padx=5
    )
    hide_folder_label.pack(pady=(10, 5))

    # Create a frame for the Hide Folder command input
    hide_folder_frame = tk.Frame(new_window)
    hide_folder_frame.pack(fill='x', pady=(10, 5))

    # Input field for the hide folder command (non-editable)
    hide_folder_entry = tk.Entry(hide_folder_frame, font=("Consolas", 10), width=40)
    hide_folder_entry.insert(0, 'attrib +h +s +r "Folder name"')  # Updated text
    hide_folder_entry.config(state='readonly')  # Make it non-editable
    hide_folder_entry.pack(side='left', padx=(0, 5))

    # Copy button for the hide folder command
    copy_hide_folder_button = tk.Button(
        hide_folder_frame,
        text="Copy",
        command=lambda: root.clipboard_clear() or root.clipboard_append(hide_folder_entry.get()),
        width=8,
        height=1,
        bg='#4CAF50',
        fg='white',
        font=("Arial", 9, "bold")
    )
    copy_hide_folder_button.pack(side='right')  # Position the copy button on the right side

    # Add a black line separator after the Hide Folder command
    separator_hide_folder = tk.Frame(new_window, height=1, bg='black')
    separator_hide_folder.pack(fill='x', padx=5, pady=(5, 5))

    # Label for the Winget Install command
    winget_install_label = tk.Label(
        new_window,
        text="Winget Install Command:",
        font=("Consolas", 10),
        anchor='w',
        padx=5
    )
    winget_install_label.pack(pady=(10, 5))

    # Create a frame for the Winget Install command input
    winget_install_frame = tk.Frame(new_window)
    winget_install_frame.pack(fill='x', pady=(10, 5))

    # Input field for the Winget Install command (non-editable)
    winget_install_entry = tk.Entry(winget_install_frame, font=("Consolas", 10), width=40)
    winget_install_entry.insert(0, 'winget install [ ]')  # Updated text
    winget_install_entry.config(state='readonly')  # Make it non-editable
    winget_install_entry.pack(side='left', padx=(0, 5))

    # Copy button for the Winget Install command
    copy_winget_install_button = tk.Button(
        winget_install_frame,
        text="Copy",
        command=lambda: root.clipboard_clear() or root.clipboard_append(winget_install_entry.get()),
        width=8,
        height=1,
        bg='#4CAF50',
        fg='white',
        font=("Arial", 9, "bold")
    )
    copy_winget_install_button.pack(side='right')  # Position the copy button on the right side

    # Add a black line separator after the Winget Install command
    separator_winget_install = tk.Frame(new_window, height=1, bg='black')
    separator_winget_install.pack(fill='x', padx=5, pady=(5, 5))

    # Label for the Winget Search command
    winget_search_label = tk.Label(
        new_window,
        text="Winget Search Command:",
        font=("Consolas", 10),
        anchor='w',
        padx=5
    )
    winget_search_label.pack(pady=(10, 5))

    # Create a frame for the Winget Search command input
    winget_search_frame = tk.Frame(new_window)
    winget_search_frame.pack(fill='x', pady=(10, 5))

    # Input field for the Winget Search command (non-editable)
    winget_search_entry = tk.Entry(winget_search_frame, font=("Consolas", 10), width=40)
    winget_search_entry.insert(0, 'winget search [ ]')  # Updated text
    winget_search_entry.config(state='readonly')  # Make it non-editable
    winget_search_entry.pack(side='left', padx=(0, 5))

    # Copy button for the Winget Search command
    copy_winget_search_button = tk.Button(
        winget_search_frame,
        text="Copy",
        command=lambda: root.clipboard_clear() or root.clipboard_append(winget_search_entry.get()),
        width=8,
        height=1,
        bg='#4CAF50',
        fg='white',
        font=("Arial", 9, "bold")
    )
    copy_winget_search_button.pack(side='right')  # Position the copy button on the right side

    # Add a separator for the new commands section
    separator_new_commands = tk.Frame(new_window, height=1, bg='black')
    separator_new_commands.pack(fill='x', padx=5, pady=(10, 5))

    # Label for the Debloat commands section
    debloat_commands_label = tk.Label(
        new_window,
        text="Debloat Commands [ PowserShell Commands ]:",
        font=("Consolas", 10),
        anchor='w',
        padx=5
    )
    debloat_commands_label.pack(pady=(10, 5))

    # Create a frame for the first Debloat command input
    debloat_frame_1 = tk.Frame(new_window)
    debloat_frame_1.pack(fill='x', pady=(10, 5))

    # Input field for Debloat command 1 (non-editable)
    debloat_entry_1 = tk.Entry(debloat_frame_1, font=("Consolas", 10), width=40)
    debloat_entry_1.insert(0, 'iwr -useb https://git.io/debloat|iex')  # Command text
    debloat_entry_1.config(state='readonly')  # Make it non-editable
    debloat_entry_1.pack(side='left', padx=(0, 5))

    # Copy button for Debloat command 1
    copy_debloat_button_1 = tk.Button(
        debloat_frame_1,
        text="Copy",
        command=lambda: root.clipboard_clear() or root.clipboard_append(debloat_entry_1.get()),
        width=8,
        height=1,
        bg='#4CAF50',
        fg='white',
        font=("Arial", 9, "bold")
    )
    copy_debloat_button_1.pack(side='right')  # Position the copy button on the right side

    # Add a black line separator after Debloat command 1
    separator_debloat_1 = tk.Frame(new_window, height=1, bg='black')
    separator_debloat_1.pack(fill='x', padx=5, pady=(5, 5))

    # Create a frame for the second Debloat command input
    debloat_frame_2 = tk.Frame(new_window)
    debloat_frame_2.pack(fill='x', pady=(10, 5))

    # Input field for Debloat command 2 (non-editable)
    debloat_entry_2 = tk.Entry(debloat_frame_2, font=("Consolas", 10), width=40)
    debloat_entry_2.insert(0, '& ([scriptblock]::Create((irm "https://debloat.raphi.re/")))')
    debloat_entry_2.config(state='readonly')  # Make it non-editable
    debloat_entry_2.pack(side='left', padx=(0, 5))

    # Copy button for Debloat command 2
    copy_debloat_button_2 = tk.Button(
        debloat_frame_2,
        text="Copy",
        command=lambda: root.clipboard_clear() or root.clipboard_append(debloat_entry_2.get()),
        width=8,
        height=1,
        bg='#4CAF50',
        fg='white',
        font=("Arial", 9, "bold")
    )
    copy_debloat_button_2.pack(side='right')  # Position the copy button on the right side

    # Add a black line separator after Debloat command 2
    separator_debloat_2 = tk.Frame(new_window, height=1, bg='black')
    separator_debloat_2.pack(fill='x', padx=5, pady=(5, 5))

    # Label for the WSL Install command
    wsl_install_label = tk.Label(
        new_window,
        text="WSL Install [ PowerShell Command ] [ Install Linux in Windows ]:",
        font=("Consolas", 10),
        anchor='w',
        padx=5
    )
    wsl_install_label.pack(pady=(10, 5))

    # Create a frame for the WSL Install command input
    wsl_install_frame = tk.Frame(new_window)
    wsl_install_frame.pack(fill='x', pady=(10, 5))

    # Input field for the WSL Install command (non-editable)
    wsl_install_entry = tk.Entry(wsl_install_frame, font=("Consolas", 10), width=40)
    wsl_install_entry.insert(0, 'wsl --install')  # Command text
    wsl_install_entry.config(state='readonly')  # Make it non-editable
    wsl_install_entry.pack(side='left', padx=(0, 5))

    # Copy button for the WSL Install command
    copy_wsl_install_button = tk.Button(
        wsl_install_frame,
        text="Copy",
        command=lambda: root.clipboard_clear() or root.clipboard_append(wsl_install_entry.get()),
        width=8,
        height=1,
        bg='#4CAF50',
        fg='white',
        font=("Arial", 9, "bold")
    )
    copy_wsl_install_button.pack(side='right')  # Position the copy button on the right side

    # Add a black line separator before the Linux Commands command
    separator_linux_commands_new = tk.Frame(new_window, height=1, bg='black')
    separator_linux_commands_new.pack(fill='x', padx=5, pady=(5, 5))

    # Label for the new Linux Commands command
    new_linux_commands_label = tk.Label(
        new_window,
        text="Linux Commands:",
        font=("Consolas", 10),
        anchor='w',
        padx=5
    )
    new_linux_commands_label.pack(pady=(10, 5))

    # Create a frame for the new Linux Commands command input
    new_linux_commands_frame = tk.Frame(new_window)
    new_linux_commands_frame.pack(fill='x', pady=(10, 5))

    # Go button for the new Linux Commands command
    new_linux_commands_button = tk.Button(
        new_linux_commands_frame,
        text="Go",
        command=lambda: webbrowser.open("https://github.com/trinib/Linux-Bash-Commands"),
        width=8,
        height=1,
        bg='#4CAF50',
        fg='white',
        font=("Arial", 9, "bold")
    )
    new_linux_commands_button.pack(side='top', padx=(0, 5))  # Center the button

    # Add a black line separator after the new Linux Commands command
    separator_linux_commands_new_bottom = tk.Frame(new_window, height=1, bg='black')
    separator_linux_commands_new_bottom.pack(fill='x', padx=5, pady=(5, 5))

def open_linux_commands_window():
    linux_window = tk.Toplevel(root)
    linux_window.title("Linux Commands")

    line = tk.Frame(linux_window, height=2, bg='black')
    line.pack(fill='x', pady=(10, 5))

    go_button = tk.Button(
        linux_window,
        text="Go",
        command=lambda: webbrowser.open("https://github.com/trinib/Linux-Bash-Commands"),
        width=10,
        height=2,
        bg='#4CAF50',
        fg='white',
        font=("Arial", 12, "bold")
    )
    go_button.pack(pady=(10, 5))

    line = tk.Frame(linux_window, height=2, bg='black')
    line.pack(fill='x', pady=(5, 10))

# Initialize the main window
root = tk.Tk()
root.title("System Utilities")
root.geometry("600x700")  # Increased height for new command

# Create main frame
frame = tk.Frame(root, padx=15, pady=10)
frame.pack(expand=True, fill='both')

# Define all commands (removed Shutdown, Restart, Log Off)
commands_info = [
    ("Windows Setup Script", "powershell -Command \"Start-Process powershell -ArgumentList '-NoProfile -ExecutionPolicy Bypass -Command iwr -useb https://christitus.com/win | iex' -Verb RunAs\""),
    ("Disk Cleanup", "cleanmgr"),
    ("User Accounts", "control userpasswords2"),
    ("Computer Defaults", "computerdefaults"),
    ("DirectX Diagnostic", "dxdiag"),
    ("Disk Management", "diskmgmt.msc"),
    ("System Configuration", "msconfig"),
    ("System Information", "msinfo32"),
    ("Power Options", "powercfg.cpl"),
    ("Steps Recorder", "psr"),
    ("Windows Version", "winver"),
    ("Network Connections", "ncpa.cpl"),
    ("Programs and Features", "appwiz.cpl"),
    ("Package Manager", "winget"),
    ("Update All Packages", "winget upgrade --all"),
    ("Windows Firewall", "firewall.cpl"),
    ("Temporary Files", "explorer %temp%"),
    ("Performance Options", "SystemPropertiesPerformance.exe"),
    # Removed Debloat Command
    # Removed Shutdown, Restart, Log Off
]

# Create buttons list to store all buttons
all_buttons = []

# Create a frame for each command
for display_name, command in commands_info:
    cmd_frame = tk.Frame(frame)
    cmd_frame.pack(fill='x', pady=(5, 5))  # Added vertical padding for equal gaps
    
    # Command name label (left-aligned)
    label = tk.Label(
        cmd_frame,
        text=display_name,
        font=("Consolas", 10),
        anchor='w',
        bg='#f0f0f0',
        padx=5
    )
    label.pack(side='left', fill='x', expand=True)
    
    # Go button (left-aligned, next to the label)
    button = tk.Button(
        cmd_frame,
        text="Go",
        command=lambda cmd=command: run_command(cmd, show_console=cmd.startswith("winget")) if cmd != "open_new_window" else open_new_window(),
        width=8,
        height=1,
        bg='#4CAF50',
        fg='white',
        font=("Arial", 9, "bold")
    )
    button.pack(side='left', padx=(10, 0))  # Added horizontal padding for equal gaps
    all_buttons.append(button)

    # Button hover effect
    def on_enter(e):
        e.widget['bg'] = '#45a049'  # Darker green on hover

    def on_leave(e):
        e.widget['bg'] = '#4CAF50'  # Original color when not hovering

    button.bind("<Enter>", on_enter)
    button.bind("<Leave>", on_leave)

    # Add a black line separator after each command
    separator = tk.Frame(frame, height=1, bg='black')
    separator.pack(fill='x', padx=5, pady=(0, 5))  # Added padding for spacing

next_button = tk.Button(
    root,
    text="Next",
    command=open_new_window,
    width=10,
    height=2,
    bg='#4CAF50',
    fg='white',
    font=("Arial", 12, "bold")
)
next_button.pack(pady=(20, 0))  # Add some padding to center it vertically

# Center the Next button in the window
next_button.place(relx=0.5, rely=0.5, anchor='center')  # Center the button

# Set up window close handler
root.protocol("WM_DELETE_WINDOW", lambda: root.destroy())

# Start the application
if __name__ == "__main__":
    try:
        root.mainloop()
    except:
        sys.exit(0)