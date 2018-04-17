from ui import panel

# Requires Python >= 3.4
if "bpy" in locals():
    from importlib import reload
    if "panel" in locals():
        reload(panel)

if __name__ == "__main__":
    print("Loading...")
    panel.main()
