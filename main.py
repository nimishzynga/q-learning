#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# (c) Mihai Maruseac, 341C3 (2010), mihai.maruseac@rosedu.org
#

import gtk

TITLE = "Robot in a Grid"

class MainWindow(gtk.Window):
    """
    Holds the definition for the main window from the GUI and all data
    associated with it.
    """

    def __init__(self):
        """
        Builds the window. Connects all the signals and displays all the
        widgets.
        """
        super(MainWindow, self).__init__()
        self.set_size_request(800, 600)
        self.set_title(TITLE)
        self.set_icon_from_file('robot.png')
        self.connect('delete_event', self.__on_exit)

        self._build_gui()

        self.show()
        self.show_all()

    def _build_gui(self):
        """
        Builds the interface of this window, the entire tree of widgets.
        """
        self._vbox = gtk.VBox()
        self.add(self._vbox)

        self._build_toolbar()

    def _build_toolbar(self):
        """
        Builds the toolbar and the associated buttons used to control the
        application.
        """
        self._toolbar = gtk.Toolbar()
        self._toolbar.set_orientation(gtk.ORIENTATION_HORIZONTAL)
        self._toolbar.set_style(gtk.TOOLBAR_BOTH)
        self._toolbar.set_border_width(5)
        self._vbox.pack_start(self._toolbar, False, False, 5)

        self._btnNew = self._add_button_to_toolbar(gtk.STOCK_NEW, "New",
                "Starts a new simulation", self.__on_new_game)
        self._toolbar.insert(gtk.SeparatorToolItem(), -1)
        self._btnStep = self._add_button_to_toolbar(gtk.STOCK_GO_FORWARD,
                "Step", "Do one step of the simulation", self.__on_step)
        self._btnPlayPause = self._add_button_to_toolbar(gtk.STOCK_MEDIA_PLAY,
                "Play", "Play the simulation", self.__on_play)
        self._toolbar.insert(gtk.SeparatorToolItem(), -1)
        self._btnAbout = self._add_button_to_toolbar(gtk.STOCK_ABOUT,
                "About", "About this program", self.__on_about)

        self._btnStep.set_sensitive(False)
        self._btnPlayPause.set_sensitive(False)

    def _add_button_to_toolbar(self, img_stock, label, tooltip, callback):
        """
        Adds a new button to a toolbar.

        img_stock   stock image to use
        label       label of button
        tooltip     tooltip for the button
        callback    callback when button is clicked
        """
        img = gtk.Image()
        img.set_from_stock(img_stock, gtk.ICON_SIZE_LARGE_TOOLBAR)
        btn = gtk.ToolButton(img, label)
        btn.set_tooltip_text(tooltip)
        btn.connect('clicked', callback)
        self._toolbar.insert(btn, -1)
        return btn

    def _switch_play_button_type(self):
        """
        Used to switch the type of play/pause button.
        """
        s = self._btnPlayPause.get_label()
        if s == 'Play':
            label = 'Pause'
            img_stock = gtk.STOCK_MEDIA_PAUSE
        elif s == 'Pause':
            label = 'Play'
            img_stock = gtk.STOCK_MEDIA_PLAY
        self._btnPlayPause.get_icon_widget().set_from_stock(img_stock,
                gtk.ICON_SIZE_LARGE_TOOLBAR)
        self._btnPlayPause.set_label(label)

    def __on_exit(self, widget, data=None):
        """
        Called when destroying the main window. Leave the gtk threads (and
        finish application).
        """
        gtk.main_quit()

    def __on_new_game(self, widget, data=None):
        """
        Called when the user issues a request for a new game.
        """
        print "New Game"

    def __on_step(self, widget, data=None):
        """
        Called when the user clicks the Step button.
        """
        print "Step"

    def __on_play(self, widget, data=None):
        """
        Called when the user clicks the Play/Pause button.
        """
        print "Play"
        self._switch_play_button_type()

    def __on_about(self, widget, data=None):
        """
        Called when the user issues a request for the About dialog.
        """
        print "About"

def main():
    """
    Main function. Construct the windows and start all application threads.
    """
    w = MainWindow()
    gtk.gdk.threads_init()
    gtk.gdk.threads_enter()
    gtk.main()
    gtk.gdk.threads_leave()

if __name__ == '__main__':
    main()

