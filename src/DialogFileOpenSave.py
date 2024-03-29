##
#   Project: gespeaker - A GTK frontend for espeak  
#    Author: Fabio Castelli <muflone@vbsimple.net>
# Copyright: 2009-2010 Fabio Castelli
#   License: GPL-2+
#  This program is free software; you can redistribute it and/or modify it
#  under the terms of the GNU General Public License as published by the Free
#  Software Foundation; either version 2 of the License, or (at your option)
#  any later version.
# 
#  This program is distributed in the hope that it will be useful, but WITHOUT
#  ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
#  FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
#  more details.
# 
# On Debian GNU/Linux systems, the full text of the GNU General Public License
# can be found in the file /usr/share/common-licenses/GPL-2.
##

import gtk

class DialogFileOpenSave(gtk.FileChooserDialog):
  def __init__(self, useForOpen=True, title=None, initialDir=None, initialFile=None, askOverwrite=True):
    gtk.FileChooserDialog.__init__(
      self, title=title, parent=None,
      action=gtk.FILE_CHOOSER_ACTION_SAVE, 
      buttons=(
        gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL, 
        useForOpen and gtk.STOCK_OPEN or gtk.STOCK_SAVE, gtk.RESPONSE_OK
      )
    )
    self.connect('response', self._response_callback)
    if initialDir:
      self.set_current_folder(initialDir)
    if initialFile:
      self.set_current_name(initialFile)
    self.set_do_overwrite_confirmation(askOverwrite)
    self.filename = None
    self.lastFilter = None

  def _response_callback(self, *args):
    self.response = args[1]
    if args[1] == gtk.RESPONSE_OK:
      self.filename = self.get_filename()
      self.lastFilter = self.get_filter()
    self.destroy()

  def show(self):
    super(self.__class__, self).run()
    return self.response==gtk.RESPONSE_OK
  
  def addFilter(self, name, patterns=None, mimetypes=None):
    filter = gtk.FileFilter()
    filter.set_name(name)
    if patterns:
      for pattern in patterns:
        filter.add_pattern(pattern)
    if mimetypes:
      for mimetype in mimetypes:
        filter.add_mime_type(mimetype)
    super(self.__class__, self).add_filter(filter)

class DialogFileSave(DialogFileOpenSave):
  def __init__(self, title=None, initialDir=None, initialFile=None, askOverwrite=True):
    super(self.__class__, self).__init__(
      useForOpen=False,
      title=title,
      initialDir=initialDir,
      initialFile=initialFile,
      askOverwrite=askOverwrite
    )

class DialogFileOpen(DialogFileOpenSave):
  def __init__(self, title=None, initialDir=None, initialFile=None):
    super(self.__class__, self).__init__(
      useForOpen=True,
      title=title,
      initialDir=initialDir,
      initialFile=initialFile,
      askOverwrite=False
    )
