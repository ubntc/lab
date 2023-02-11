#!/usr/bin/env python

import os
import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

app_version = "v164144.2023-02-11"
gtk_version = ".".join(f"{v}" for v in gi.version_info)


def add_window(w: Gtk.Window):
    child = Gtk.Window(title="ChildWindow")
    child.show_all()


def app():
    w = Gtk.Window(title=f"MyApp {app_version} - Gtk {gtk_version}")
    w.connect("destroy", Gtk.main_quit)
    w.connect("show", add_window)
    w.show_all()
    w.resize(500, 400)
    Gtk.main()


if __name__ == "__main__":
    app()
