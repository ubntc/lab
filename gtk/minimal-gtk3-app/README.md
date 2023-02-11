# Pinnable Gtk3 App (PyGtk)
This demonstrates how to create a Gtk3 app and make it pinnable
in the GNOME Shell Dock.

## Features
* Minimal App with a minimal (local) install script
* App can be pinned to the GNOME Shell Dock after installation
* Pinned launch icon and all app windows share the same place in the Dock
* Child windows are grouped in the Dock
* App can be launched from anywhere

## How does it work?
Most of the magic is managed my GNOME Shell.
It will match the names of running binaries with the names of the `.desktop`
files found in the system. Here is what you need to do.

1. Ensure your both files have the same basename, `my-app.desktop` and `my-app`
2. In the `.desktop` file use `Exec=my-app` as you would call it in a terminal
3. Put your `my-app` binary on the `PATH`

You can then start the app in the terminal or via the app finder. GNOME Shell will
detect it and group it to your pinned launch icon.

If you use `Exec=/path/to/some/script.py` or the basenames are different,
app pinning in the Dock does not seem to work. The launch icon from the desktop file
will be separate from the running app instances.
