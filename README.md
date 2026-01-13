# TikTok Seller Auto-Capture Script

A Python automation script to capture screenshots from a TikTok Seller list running in BlueStacks emulator with precise scrolling control.

## Features

✅ **Automatic Window Detection** - Finds BlueStacks window automatically using `pygetwindow`  
✅ **Drag-to-Scroll** - Uses click-and-drag instead of mouse wheel for reliable scrolling in emulators  
✅ **Fail-Safe Protection** - Move mouse to top-left corner to stop the script at any time  
✅ **5-Second Countdown** - Time to focus the BlueStacks window before automation starts  
✅ **Timestamped Folders** - Organizes captures in `captures_YYYY-MM-DD_HH-MM-SS` folders  
✅ **Configurable** - Easy-to-adjust settings for different screen sizes and scroll speeds  

## Installation

1. **Activate virtual environment:**
   ```powershell
   .\venv\Scripts\Activate.ps1
   ```

2. **Install dependencies:**
   ```powershell
   pip install -r requirements.txt
   ```

## Usage

1. **Open BlueStacks** and navigate to your TikTok Seller list
2. **Run the script:**
   ```powershell
   python app.py
   ```
3. **Enter the number of scrolls** when prompted
4. **Focus the BlueStacks window** during the 5-second countdown
5. **Wait for completion** - screenshots will be saved automatically

## Configuration

Edit the `Config` class in `app.py` to customize:

### Window Settings
```python
WINDOW_TITLE = "BlueStacks"  # Change if your window has a different title
```

### Scroll Settings
```python
SCROLL_DELAY = 1.5           # Delay after each scroll (seconds)
DRAG_DURATION = 0.5          # Speed of drag motion
DRAG_START_Y_RATIO = 0.7     # Start drag at 70% down the window
DRAG_END_Y_RATIO = 0.3       # End drag at 30% down the window
```

### Safety Settings
```python
FAILSAFE_ENABLED = True      # Enable fail-safe (move mouse to corner to stop)
COUNTDOWN_SECONDS = 5        # Countdown before starting
```

## Troubleshooting

### "Could not find window with title 'BlueStacks'"
- Make sure BlueStacks is running and visible
- Check the exact window title in your taskbar
- Update `Config.WINDOW_TITLE` in `app.py` to match

### Scroll distance is off (capturing partial items)
- Adjust `DRAG_START_Y_RATIO` and `DRAG_END_Y_RATIO` in the Config class
- Start with small adjustments (±0.05)
- Test with 2-3 scrolls first to calibrate

### UI not loading in time
- Increase `SCROLL_DELAY` in the Config class
- Try 2.0 or 2.5 seconds for slower connections

### Screenshots include desktop/taskbar
- The script automatically captures only the BlueStacks window
- If issues persist, adjust `CAPTURE_OFFSET_X/Y` in Config

## Output

Screenshots are saved as:
```
captures_2026-01-13_00-42-30/
├── capture_0001.png
├── capture_0002.png
├── capture_0003.png
└── ...
```

## Safety Features

- **Fail-Safe**: Move mouse to top-left corner (0,0) to immediately stop
- **Countdown**: 5-second delay before starting automation
- **Error Handling**: Partial results are saved even if script is interrupted

## Tips for Best Results

1. **Maximize BlueStacks** for consistent window size
2. **Test with 2-3 scrolls first** to calibrate the drag distance
3. **Ensure stable internet** so the list loads quickly
4. **Don't move the BlueStacks window** during capture
5. **Close unnecessary apps** to free up system resources

## License

MIT License - Feel free to modify and use as needed!
