---
title: PyCon tutorial -  Intermediate Twisted -  Test-Driven Networking Software
sidebar_link: false
---

February 02, 2013


   

In preparation for his PyCon tutorial, Itamar will rehearse it for Boston Python members.

Itamar Turner-Trauring, Intermediate Twisted: Test-Driven Networking Software (https://us.pycon.org/2013/schedule/presentation/15/)

Unit testing is one of the most important methods for building more reliable, robust software; test-driven development, where tests are written first, even more so. But testing network applications presents additional difficulties:

Data can arrive over the network with arbitrary delays, in arbitrary chunks, Connections can break at random, Timeouts are an important feature, but a unittest that takes 2 hours to pass is unacceptable, Relying on actual networking for tests leads to more fragile tests, etc. In order to deal with these issues, the Twisted event-driven networking framework provides an extensive set of functionality for testing, making it an excellent choice for building reliable applications.

This tutorial aims to teach you how to write well-tested network applications with Twisted using a series of hands-on exercises. We will begin with a quick lecture on how to test Twisted code. Then you will get your hands dirty coding by trying to make a provided set of tests pass; the result will be a toy HTTP server. For the final exercise, you will need to come up with the list of tests yourself, as you would in real world development.

Prerequisites: Intermediate knowledge of Python: classes, functions, etc.. A basic understanding of Twisted (protocols, transports, Deferreds), e.g. as provided by the introductory Twisted tutorial. Previous experience with other event-driven frameworks may suffice, however, given enough programming experience. Some experience with the unittest module would also be very helpful.

Please arrive with a laptop configured with a recent version of Twisted (12.2 or later) and Python 2.7. Ubuntu, Debian or some other version of Linux or Unix (e.g. OS X) is highly recommended, but not necessary. If you’re using Windows please make very very sure you have a Twisted development environment set up before the class has started; in particular you should be able to run the trial command-line program.

PyCon tutorials are half-day in-depth courses presented in the days preceding the bulk of PyCon. Rehearsing with a real audience is a great way to prepare. Come ready to learn, and also to provide feedback!

Note: Space is very limited for these events, please do not sign up for more than one, to give others a chance.

No food is being provided at this event.

Location:

We are in an MIT classroom, 2-135, which is in Building 2, first floor. This map shows where building 2 is: http://whereis.mit.edu/?go=2

* The closest T stop is the Kendall T stop on the Red Line.
* The closest bus stop is the 84 Massachusetts Avenue stop on the #1.
* There is paid garage parking at 5 Cambridge Center and at 1 Kendall Square (by the Kendall Square Cinema).


Meetup link: [https://www.meetup.com/bostonpython/events/100333602/](https://www.meetup.com/bostonpython/events/100333602/)

[Back to Past Events Page](index.md)