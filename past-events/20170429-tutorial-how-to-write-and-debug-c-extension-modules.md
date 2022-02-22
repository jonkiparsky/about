---
title: Tutorial -  How to Write and Debug C Extension Modules
sidebar_link: false
---

April 29, 2017


   

Description

The CPython interpreter allows us implement modules in C for performance critical code or to interface with external libraries while presenting users with a high level Python API. This tutorial will teach you how to leverage to power of C in your Python projects.

We will start by explaining the C representation of Python objects and how to manipulate them from within C. We will then move on to implementing functions in C for use in Python. We will discuss reference counting and correct exception handling. We will also talk about how to package and build your new extension module so that it may be shared on PyPI. (We will only be covering building extension modules on GNU/Linux and OSX, not Windows).

After the break, we will show how to implement a new type in C. This will cover how to hook into various protocols and properly support cyclic garbage collection. We will also discuss techniques for debugging C extension modules with gdb using the CPython gdb extension.

Instructor Bio Joe Jevnik works at Quantopian where he works on integrating data from various sources into the platform. Joe works on Zipline, Quantopian's open source backtester. He also works on the Blaze ecosystem, mainly on blaze core, odo, and datashape. Pre-Tutorial Instructions You should be comfortable with the Python language and builtin data structures like dict, list, and tuple.

You should understand C control flow like 'if' statements and 'for' loops as well as the standard C types like 'int' and 'float'. You should also be familiar with pointers and how to use them.

Follow the install steps at https://github.com/llllllllll/c-extension-tutorial

Contact:

joejev@gmail.com

Other Notes Food will not be provided, as we do not have sponsors for the event. Lunch options nearby in the Kendall/MIT area include Au Bon Pain, Chipotle, Clover, Champions, and more.


Meetup link: [https://www.meetup.com/bostonpython/events/238341234/](https://www.meetup.com/bostonpython/events/238341234/)

[Back to Past Events Page](index.md)