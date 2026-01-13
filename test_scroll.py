"""
Test Scroll Distance - Use this to calibrate the perfect scroll distance
This script will perform a single scroll so you can verify it moves exactly 3 items
"""

import pyautogui
import pygetwindow as gw
import time

# Configuration
WINDOW_TITLE = "BlueStacks App Player"
DRAG_START_Y_RATIO = 0.7  # Start at 70% down
DRAG_END_Y_RATIO = 0.3    # End at 30% down
DRAG_DURATION = 0.5

print("=" * 70)
print("  Scroll Distance Test")
print("=" * 70)

# Enable fail-safe
pyautogui.FAILSAFE = True
print("✅ Fail-safe enabled (move mouse to top-left corner to stop)")

# Find window
print(f"\n🔍 Looking for '{WINDOW_TITLE}' window...")
windows = gw.getWindowsWithTitle(WINDOW_TITLE)

if not windows:
    print(f"❌ Error: Could not find window with title '{WINDOW_TITLE}'")
    print("\n💡 Run 'python find_window.py' to see all available windows")
    exit(1)

window = windows[0]
x, y, width, height = window.left, window.top, window.width, window.height
print(f"✅ Found window at: ({x}, {y}) - Size: {width}x{height}")

# Calculate positions
start_x = x + int(width * 0.5)
start_y = y + int(height * DRAG_START_Y_RATIO)
end_x = x + int(width * 0.5)
end_y = y + int(height * DRAG_END_Y_RATIO)

print(f"\n📍 Scroll will drag from:")
print(f"   Start: ({start_x}, {start_y})")
print(f"   End:   ({end_x}, {end_y})")
print(f"   Distance: {start_y - end_y} pixels")

# Countdown
print("\n⏱️  Starting in 3 seconds...")
for i in range(3, 0, -1):
    print(f"   {i}...", end='\r')
    time.sleep(1)
print("   GO! 🚀" + " " * 20)

# Perform scroll
print("\n⬆️  Performing scroll...")
pyautogui.moveTo(start_x, start_y)
time.sleep(0.1)
pyautogui.dragTo(end_x, end_y, duration=DRAG_DURATION)

print("✅ Scroll complete!")
print("\n" + "=" * 70)
print("📊 Check your BlueStacks window:")
print("   - Did it scroll exactly 3 items?")
print("   - If too much: Decrease DRAG_END_Y_RATIO (try 0.35 or 0.4)")
print("   - If too little: Increase DRAG_END_Y_RATIO (try 0.25 or 0.2)")
print("   - Or adjust DRAG_START_Y_RATIO")
print("\n💡 Update these values in app.py Config class")
print("=" * 70)
