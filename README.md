# Python Projects Portfolio 🐍

A collection of Python applications demonstrating practical programming skills across desktop, web, and utility development.

## 📁 Projects

### [Scheduler Desktop App](/scheduler_desktop/) 🖥️📅
A desktop task management application with graphical interface for organizing daily todos.

**Features:**
- Graphical user interface built with FreeSimpleGUI
- Persistent task storage with text file backend
- Add, edit, complete, and delete todo items
- Real-time clock display
- Icon-based buttons with fallback text
- Cross-platform compatibility

**Tech Stack:**
- Python 3
- FreeSimpleGUI for desktop interface
- File I/O for data persistence
- Modular architecture with separate GUI and functions modules

### [Scheduler Web App](/scheduler_web/) 🌐📅  
A modern web-based task management application accessible from any browser.

**Features:**
- Streamlit web interface
- Real-time task updates and synchronization
- Checkbox-based task completion
- Responsive design for all devices
- Shared data backend with desktop version
- Automatic saving and session management

**Tech Stack:**
- Python 3
- Streamlit for web interface
- Session state management
- Same backend functions as desktop version

### 🔄 Integrated System
Both scheduler applications share the same data file (`todos.txt`), allowing seamless task management across desktop and web interfaces.

## 🛠️ Technologies Used

- **Core Language**: Python 3
- **Desktop GUI**: FreeSimpleGUI
- **Web Framework**: Streamlit
- **Data Persistence**: File I/O (text files)
- **Architecture**: Modular design with separation of concerns
- **Development**: PyCharm, virtual environments, Git

## 🚀 Getting Started

### Prerequisites
- Python 3.7 or higher
- Required libraries: FreeSimpleGUI, Streamlit

### Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/python-projects.git
   cd python-projects
   ```

2. **Set up a virtual environment (recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install FreeSimpleGUI streamlit
   ```

### Running the Applications

**Scheduler Desktop App:**
```bash
cd scheduler_desktop
python gui.py
```

**Scheduler Web App:**
```bash
cd scheduler_web
streamlit run app.py
```

## 📁 Project Structure

```
python-projects/
├── scheduler_desktop/          # Desktop task manager
│   ├── gui.py                 # Main GUI application
│   ├── functions.py           # Business logic and file operations
│   ├── files/
│   │   ├── todos.txt          # Task storage (shared with web app)
│   │   └── images/            # Application icons
│   └── README.md
├── scheduler_web/              # Web-based task manager  
│   ├── app.py                # Streamlit web application
│   ├── functions.py          # Shared business logic
│   └── README.md
├── requirements.txt
└── README.md (this file)
```

## 🎯 Learning Objectives

This portfolio demonstrates:
- **Desktop Application Development**: GUI creation with FreeSimpleGUI
- **Web Application Development**: Streamlit web interfaces
- **Data Persistence**: File handling and cross-application data sharing
- **Event-Driven Programming**: User interaction handling in both desktop and web
- **Software Architecture**: Modular design patterns and code reuse
- **Multi-Platform Development**: Same backend logic for different frontends

## 🌟 Project Highlights

| Project | Type | Key Skills Demonstrated |
|---------|------|------------------------|
| Scheduler Desktop | Desktop App | GUI development, file I/O, event handling, modular architecture |
| Scheduler Web | Web App | Streamlit framework, session management, responsive design |

## 🔄 Shared Architecture

**Code Reusability**: Both applications use the same `functions.py` module, demonstrating:
- Efficient code organization
- Backend/frontend separation
- Maintainable architecture
- Easy feature synchronization

**Data Consistency**: Single `todos.txt` file ensures tasks are accessible from both interfaces.

## 💭 Development Philosophy

All projects in this portfolio are built with attention to:
- **Clean Code**: Readable, maintainable, and well-documented
- **User Experience**: Intuitive interfaces with clear functionality
- **Practicality**: Solving real-world problems with Python
- **Learning Focus**: Each project explores different Python ecosystems

## 🔮 Future Project Roadmap

- **Data Analysis Tools**: Pandas-based data processing applications
- **Automation Scripts**: File management and workflow automation
- **API Integrations**: Web services and data fetching utilities
- **Machine Learning**: Basic ML models and data visualization
- **Game Development**: PyGame or other gaming frameworks

## 🤝 Contributing

This is primarily a personal learning portfolio, but feedback and suggestions are welcome:
- Report any issues or bugs
- Suggest improvements or new features
- Share your own Python project ideas
- Discuss architecture and design patterns

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

**💡 About the Developer**  
This portfolio represents my journey in Python development, focusing on practical applications that solve real problems. Each project is built with attention to code quality, user experience, and maintainability.

*Exploring Python's diverse ecosystems through hands-on projects and continuous learning.* 🚀

*"From desktop to web, mastering Python one project at a time."*