.. redict documentation master file, created by
   sphinx-quickstart on Mon Sep  5 08:21:19 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

redict
==================================

Contents:

.. toctree::
   :maxdepth: 2

  redict


Say you have a bunch of datafile names (or stings in general) that contain 
information about the data saved in the file. Perhaps half the files have
a flag signifying they were taken under condition set A and half under 
condition set B. If you want to plot data fromt the files you might check
which flag each filename has, and then assign that line on the plot  to be
red or blue respectively. This module provides a shortcut for accomplishing 
this task::

    style_defs = { '.*condition=A.*': {'color': 'red'}, 
                   '.*condition=B.*': {'color': 'blue'}}
    styles = ReDict(style_defs)

    for path in paths:
      style = styles.re_get(path)  # {'color: 'red'}
      plot(data, style)


Todo
===================================

Add compatibility with the ``reglean`` module.


API Docs
==================

* :ref:`modindex`
