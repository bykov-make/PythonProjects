# Scheduler Web App 🌐

A modern, web-based task management application built with Streamlit for organizing your todos with a clean, responsive interface.

## ✨ Features

- **Web-Based Interface**: Access your todos from any browser
- **Real-time Updates**: Instant saving and synchronization
- **Checkbox Management**: Easy task completion with checkboxes
- **Persistent Storage**: Tasks saved automatically to local file
- **Minimalist Design**: Clean, distraction-free interface
- **Responsive**: Works on desktop, tablet, and mobile devices

## 🖥️ Application Preview

```
My Todo App
───────────────────────────
This is my todo app

This app is to increase productivity...

☐ Buy groceries
☐ Finish project report  
☐ Call dentist

[Add new to-do...]
```

## 🚀 Quick Start

### Prerequisites
- Python 3.7 or higher
- Streamlit library

### Installation & Running

1. **Navigate to the project directory**
   ```bash
   cd scheduler_web
   ```

2. **Install Streamlit**
   ```bash
   pip install streamlit
   ```

3. **Run the web application**
   ```bash
   streamlit run app.py
   ```

4. **Open your browser**
   - The app automatically opens at `http://localhost:8501`
   - Or manually navigate to the URL shown in your terminal

## 📖 How to Use

### Adding a Task
1. Type your task in the text input at the bottom
2. Press **Enter** to add it to your list
3. The task immediately appears with a checkbox

### Completing a Task
1. Click the checkbox next to any task
2. The task is instantly removed from your list
3. Your changes are automatically saved

### Managing Multiple Tasks
- Add as many tasks as you need
- Complete tasks in any order
- All changes persist between sessions

## 🗂️ File Structure

```
scheduler_web/
├── app.py                 # Main Streamlit application
├── functions.py           # Shared todo functions (same as desktop version)
├── files/
│   └── todos.txt          # Shared task storage (compatible with desktop app)
└── README.md
```

## 🛠️ Technical Details

### Built With
- **Streamlit** - Web application framework
- **Python 3** - Backend logic
- **Session State** - Real-time state management
- **File I/O** - Persistent data storage

### Key Features
- **Session Management**: Maintains state across interactions
- **Automatic Reruns**: Updates interface immediately after changes
- **Shared Backend**: Uses same `functions.py` as desktop version
- **Cross-Platform**: Accessible from any device with a browser

## 🔄 Integration with Desktop Version

**Shared Data File**: Both web and desktop versions use the same `todos.txt` file, allowing you to:
- Manage tasks on desktop during work hours
- Access and update from web browser anywhere
- Seamlessly switch between interfaces

## 🌐 Deployment Options

### Local Development
```bash
streamlit run app.py
```

### Cloud Deployment
Easily deploy to:
- **Streamlit Community Cloud** (free)
- **Heroku**
- **AWS/Azure/Google Cloud**
- **Docker containers**

### Deploy to Streamlit Cloud
1. Push your code to GitHub
2. Visit [share.streamlit.io](https://share.streamlit.io)
3. Connect your repository
4. Deploy with one click

## 🔧 Customization

### Changing the Theme
Modify the appearance by editing `app.py`:
```python
# Add custom CSS
st.markdown("""
<style>
    .main { background-color: #f0f2f6; }
</style>
""", unsafe_allow_html=True)
```

### Adding Features
Easy extensions you can add:
- Due dates and deadlines
- Task categories or tags
- Priority levels
- Progress tracking
- Data export functionality

## 🐛 Troubleshooting

### Common Issues

**Module not found:**
```bash
pip install streamlit
```

**Port already in use:**
```bash
streamlit run app.py --server.port 8502
```

**Tasks not syncing:**
- Ensure both web and desktop apps point to the same `todos.txt` file
- Check file permissions in the `files/` directory

## 📊 Performance

- **Fast Loading**: Lightweight interface loads instantly
- **Real-time Updates**: No page refreshes needed
- **Efficient Storage**: Simple text-based storage system
- **Scalable**: Handles hundreds of tasks efficiently

## 🤝 Contributing

This web app shares the same backend as the desktop version, making it easy to maintain both interfaces. Contributions welcome for:
- UI/UX improvements
- New features
- Mobile optimization
- Deployment scripts

---

**💡 Pro Tip**: Bookmark your local Streamlit URL for quick access throughout the day. Perfect for keeping your task list handy while working across different applications!

*Stay productive anywhere, anytime!* 🚀