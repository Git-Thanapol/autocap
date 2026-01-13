"""
TikTok Seller List Auto-Capture Script
Automates screenshot capture from BlueStacks emulator with precise scrolling.
"""

import pyautogui
import pygetwindow as gw
from PIL import Image
import os
import time
from datetime import datetime

# ============================================================================
# CONFIGURATION
# ============================================================================

class Config:
    """Configuration settings for the automation script"""
    
    # Safety settings
    FAILSAFE_ENABLED = True
    COUNTDOWN_SECONDS = 5
    SCROLL_DELAY = 1.5  # Delay after each scroll to allow UI to load
    
    # Drag settings (for scrolling)
    DRAG_DURATION = 0.5  # Duration of drag motion in seconds
    
    # BlueStacks window title (adjust if needed)
    WINDOW_TITLE = "BlueStacks"
    
    # Screenshot region offset (adjust based on your BlueStacks layout)
    # These are offsets from the window's top-left corner
    CAPTURE_OFFSET_X = 0
    CAPTURE_OFFSET_Y = 0
    CAPTURE_WIDTH = None  # None = use full window width
    CAPTURE_HEIGHT = None  # None = use full window height
    
    # Drag coordinates (relative to window)
    # These will be set dynamically based on window size
    DRAG_START_X_RATIO = 0.5  # Center horizontally
    DRAG_START_Y_RATIO = 0.7  # Bottom of list (70% down)
    DRAG_END_X_RATIO = 0.5    # Center horizontally
    DRAG_END_Y_RATIO = 0.3    # Top of list (30% down)


# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def find_bluestacks_window():
    """
    Find the BlueStacks window and return its coordinates.
    Returns: tuple (x, y, width, height) or None if not found
    """
    try:
        windows = gw.getWindowsWithTitle(Config.WINDOW_TITLE)
        
        if not windows:
            print(f"❌ Error: Could not find window with title '{Config.WINDOW_TITLE}'")
            print("\nAvailable windows:")
            all_windows = gw.getAllWindows()
            for i, win in enumerate(all_windows[:10], 1):  # Show first 10
                print(f"  {i}. {win.title}")
            return None
        
        # Get the first matching window
        window = windows[0]
        
        # Activate the window to bring it to front
        try:
            window.activate()
        except:
            print("⚠️  Warning: Could not activate window, but will continue...")
        
        return (window.left, window.top, window.width, window.height)
    
    except Exception as e:
        print(f"❌ Error finding window: {e}")
        return None


def create_capture_folder():
    """
    Create a timestamped folder for storing captures.
    Returns: folder path
    """
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    folder_name = f"captures_{timestamp}"
    folder_path = os.path.join(os.getcwd(), folder_name)
    
    os.makedirs(folder_path, exist_ok=True)
    print(f"📁 Created folder: {folder_path}")
    
    return folder_path


def countdown(seconds):
    """Display a countdown timer"""
    print(f"\n⏱️  Starting in {seconds} seconds...")
    print("   (Move mouse to top-left corner to abort)")
    
    for i in range(seconds, 0, -1):
        print(f"   {i}...", end='\r')
        time.sleep(1)
    
    print("   GO! 🚀" + " " * 20)


def capture_screenshot(window_coords, save_path):
    """
    Capture a screenshot of the BlueStacks window.
    
    Args:
        window_coords: tuple (x, y, width, height)
        save_path: path to save the screenshot
    """
    x, y, width, height = window_coords
    
    # Apply offsets if configured
    capture_x = x + Config.CAPTURE_OFFSET_X
    capture_y = y + Config.CAPTURE_OFFSET_Y
    capture_width = Config.CAPTURE_WIDTH or width
    capture_height = Config.CAPTURE_HEIGHT or height
    
    # Take screenshot of the region
    screenshot = pyautogui.screenshot(region=(
        capture_x,
        capture_y,
        capture_width,
        capture_height
    ))
    
    # Save the screenshot
    screenshot.save(save_path)


def perform_scroll(window_coords):
    """
    Perform a drag-to-scroll gesture in the BlueStacks window.
    
    Args:
        window_coords: tuple (x, y, width, height)
    """
    x, y, width, height = window_coords
    
    # Calculate drag start and end positions
    start_x = x + int(width * Config.DRAG_START_X_RATIO)
    start_y = y + int(height * Config.DRAG_START_Y_RATIO)
    end_x = x + int(width * Config.DRAG_END_X_RATIO)
    end_y = y + int(height * Config.DRAG_END_Y_RATIO)
    
    # Perform the drag
    pyautogui.moveTo(start_x, start_y)
    time.sleep(0.1)  # Brief pause before dragging
    pyautogui.dragTo(end_x, end_y, duration=Config.DRAG_DURATION)


# ============================================================================
# MAIN SCRIPT
# ============================================================================

def main():
    """Main automation script"""
    
    print("=" * 70)
    print("  TikTok Seller List Auto-Capture Script")
    print("=" * 70)
    
    # Enable fail-safe
    if Config.FAILSAFE_ENABLED:
        pyautogui.FAILSAFE = True
        print("✅ Fail-safe enabled (move mouse to top-left corner to stop)")
    
    # Get user input
    try:
        num_scrolls = int(input("\n📊 How many scrolls do you want to perform? "))
        if num_scrolls <= 0:
            print("❌ Error: Number of scrolls must be positive")
            return
    except ValueError:
        print("❌ Error: Please enter a valid number")
        return
    
    # Find BlueStacks window
    print("\n🔍 Looking for BlueStacks window...")
    window_coords = find_bluestacks_window()
    
    if not window_coords:
        print("\n💡 Tip: Make sure BlueStacks is running and visible")
        print("   You can also modify Config.WINDOW_TITLE in the script")
        return
    
    x, y, width, height = window_coords
    print(f"✅ Found window at: ({x}, {y}) - Size: {width}x{height}")
    
    # Create capture folder
    capture_folder = create_capture_folder()
    
    # Display countdown
    countdown(Config.COUNTDOWN_SECONDS)
    
    # Main capture loop
    print(f"\n🎬 Starting capture sequence ({num_scrolls} scrolls)...\n")
    
    try:
        for i in range(num_scrolls):
            print(f"📸 Capture {i + 1}/{num_scrolls}...", end=' ')
            
            # Take screenshot
            save_path = os.path.join(capture_folder, f"capture_{i + 1:04d}.png")
            capture_screenshot(window_coords, save_path)
            print(f"✅ Saved to {os.path.basename(save_path)}")
            
            # Don't scroll after the last capture
            if i < num_scrolls - 1:
                print(f"   ⬆️  Scrolling...", end=' ')
                perform_scroll(window_coords)
                print("Done")
                
                # Wait for UI to load
                print(f"   ⏳ Waiting {Config.SCROLL_DELAY}s for UI to load...")
                time.sleep(Config.SCROLL_DELAY)
        
        # Summary
        print("\n" + "=" * 70)
        print("✨ Capture complete!")
        print(f"📁 Total screenshots: {num_scrolls}")
        print(f"💾 Saved to: {capture_folder}")
        print("=" * 70)
    
    except pyautogui.FailSafeException:
        print("\n\n⚠️  FAIL-SAFE TRIGGERED - Script stopped by user")
        print(f"📁 Partial results saved to: {capture_folder}")
    
    except Exception as e:
        print(f"\n\n❌ Error during capture: {e}")
        print(f"📁 Partial results saved to: {capture_folder}")


# ============================================================================
# ENTRY POINT
# ============================================================================

if __name__ == "__main__":
    main()
