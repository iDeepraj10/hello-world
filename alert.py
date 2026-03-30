import ctypes

# Display Windows alert
ctypes.windll.user32.MessageBoxW(1, "Hello Dexter", "Alert", 0)
