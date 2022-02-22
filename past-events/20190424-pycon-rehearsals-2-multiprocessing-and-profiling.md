---
title: PyCon Rehearsals 2 -  Multiprocessing and Profiling
sidebar_link: false
---

April 24, 2019


   

Pizza and drinks sponsored by True Tickets (https://true-tickets.com/), hosted by iZotope

Tonight we have two PyCon talk rehearsals!

Pamela McANulty: Things I Wish They Told Me About The Multiprocessing Module in Python 3

If you haven't tried multiprocessing or you are trying to move beyond multiprocessing.map(), you will likely find that using Python's multiprocessing module can get quite intricate and convoluted. This talk focuses on a few techniques (starting, shutting down, data flow, blocking, etc) that will maximize multiprocessing’s efficiency, while also helping you through the complex issues related to coordinating startup and especially shutdown of your multiprocess app.

Emin Martinian: Statistical Profiling (and other fun with the sys module)

Profiling involves computing a set of data about how often and how long various parts of your program are executed. Profiling is useful to understand what makes your program slow and how you can improve it. After a quick review of deterministic profiling tools and techniques, I will describe how you can do statistical profiling with existing packages or write your own from scratch.

Statistical profiling involves occasionally sampling what your program is doing instead of watching each line or function. A key feature of statistical profiling is that by using a moderate sampling frequency, you can profile your production code with almost no overhead. This lets you find the actual bottlenecks in real use cases.

The core technical focus of the talk is python's sys module and how it lets you easily examine a running program. I also describe some tricks to be aware of related to threading, context switches, locks, and so on. At the conclusion of the talk, you will hopefully understand how to use an existing statistical profiler or write a customized version yourself.


Meetup link: [https://www.meetup.com/bostonpython/events/258331662/](https://www.meetup.com/bostonpython/events/258331662/)

[Back to Past Events Page](index.md)