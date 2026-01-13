"""
Quick Configuration Guide for TikTok Auto-Capture
Run this script to help you find the correct window title and test coordinates.
"""

import pygetwindow as gw

print("=" * 70)
print("  BlueStacks Window Finder")
print("=" * 70)

print("\n🔍 Searching for all open windows...\n")

all_windows = gw.getAllWindows()

# Filter out empty titles
windows_with_titles = [w for w in all_windows if w.title.strip()]

print(f"Found {len(windows_with_titles)} windows with titles:\n")

for i, window in enumerate(windows_with_titles, 1):
    print(f"{i:2d}. Title: '{window.title}'")
    print(f"    Position: ({window.left}, {window.top})")
    print(f"    Size: {window.width}x{window.height}")
    print()

print("=" * 70)
print("\n💡 Tips:")
print("   1. Find your BlueStacks window in the list above")
print("   2. Copy the exact title (everything between the quotes)")
print("   3. Update Config.WINDOW_TITLE in app.py with this title")
print("\n   Example:")
print("   If you see: 15. Title: 'BlueStacks App Player'")
print("   Then set: WINDOW_TITLE = 'BlueStacks App Player'")
print("=" * 70)
