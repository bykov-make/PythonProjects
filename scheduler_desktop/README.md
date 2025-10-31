# Scheduler Desktop App 📅

A clean and intuitive desktop task management application built with Python and FreeSimpleGUI for organizing your daily todos and reminders.

## ✨ Features

- **Task Management**: Add, edit, and complete todo items
- **Persistent Storage**: Automatically saves tasks to a local file
- **Visual Interface**: Clean GUI with icon buttons and real-time clock
- **Easy Navigation**: Simple and intuitive task operations
- **Cross-Platform**: Works on Windows, macOS, and Linux

## 🖼️ Application Preview

```
My Scheduler App
───────────────────────────
[Nov 15, 2024 14:30:25]

Type in a To-Do:
[Input Box] [➕ Add]

[Task List Display]
• Buy groceries
• Finish project report
• Call dentist

[✏️ Edit] [✅ Complete] [❌ Exit]
```

## 🚀 Installation & Setup

### Prerequisites
- Python 3.7 or higher
- FreeSimpleGUI library

### Installation

1. **Clone or download the project**
   ```bash
   cd scheduler_desktop
   ```

2. **Install FreeSimpleGUI**
   ```bash
   pip install FreeSimpleGUI
   ```

3. **Run the application**
   ```bash
   python gui.py
   ```

## 📖 How to Use

### Adding a Task
1. Type your task in the input box
2. Click the **Add** button (or press Enter)
3. Your task appears in the list below

### Editing a Task
1. Select a task from the list
2. The task text appears in the input box
3. Modify the text as needed
4. Click the **Edit** button

### Completing a Task
1. Select the completed task from the list
2. Click the **Complete** button
3. The task is removed from your list

### Exiting the App
- Click the **Exit** button or close the window
- Your tasks are automatically saved

## 🗂️ File Structure

```
scheduler_desktop/
├── gui.py                 # Main application window
├── functions.py           # Business logic and utilities
├── files/
│   ├── todos.txt          # Task storage (auto-created)
│   └── images/
│       ├── add.png        # Add task icon
│       ├── edit.png       # Edit task icon
│       ├── complete.png   # Complete task icon
│       └── close.png      # Exit app icon
└── README.md
```

## 🛠️ Technical Details

### Built With
- **Python 3** - Core programming language
- **FreeSimpleGUI** - Graphical user interface framework
- **File I/O** - Persistent data storage
- **OS Module** - Cross-platform file path handling

### Key Components
- **gui.py**: Main application window and event loop
- **functions.py**: Data management and utility functions
- **Image-based Buttons**: Custom icon buttons with fallback text
- **Real-time Clock**: Live time display in the interface

## 🔧 Customization

### Changing the Theme
Modify the theme in `gui.py`:
```python
sg.theme("DarkBlue3")  # Change to "LightGreen", "Dark", etc.
```

### Adding New Features
The modular architecture makes it easy to extend:
- Add due dates to tasks
- Implement task categories
- Add notification reminders
- Export tasks to other formats

## 🐛 Troubleshooting

### Common Issues

**Images not loading:**
- The app will automatically use text buttons as fallback
- Ensure image files are in `files/images/` directory

**Tasks not saving:**
- Check file permissions in the project directory
- Verify the `files/todos.txt` file exists

**Module not found error:**
- Ensure FreeSimpleGUI is installed: `pip install FreeSimpleGUI`

## 🤝 Contributing

Feel free to fork this project and submit pull requests for:
- New features
- Bug fixes
- UI improvements
- Documentation enhancements

## 📄 License

This project is open source and available under the MIT License.

---

**💡 Pro Tip**: Keep the app running in the background throughout your day for quick task management! The real-time clock helps you stay on schedule while managing your todos.

*Stay organized and productive!* 🚀