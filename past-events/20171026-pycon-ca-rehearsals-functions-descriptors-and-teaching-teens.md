---
title: Pycon.ca rehearsals -  Functions, Descriptors, and Teaching Teens
sidebar_link: false
---

October 26, 2017


   

Sponsored by Department of Biomedical Informatics at Harvard Medical School (http://dcic.4dnucleome.org/)

InsightSquared will sponsor drinks afterward.

Pycon.ca (https://2017.pycon.ca/) is the Canadian regional PyCon. It's in Montréal, Nov 18-21. We have three Boston people speaking there. They will rehearse their talks with us.

Jack Diederich, HOWTO write a function

Writing a function that the compiler will accept is much easier than writing a function that will get through code review on the first pass. I've written and reviewed lots of functions and the same advice comes up again and again. 1) Your function should have three parts: input, transform, and output. You should do them in order and not intermingle the three. 2) Keep the function readable by giving your reader context and keeping the amount of implied context low. 3) You can mostly ignore cargo cult practices like one-entry-one-exit and strict function length limits. We'll talk about why those cults exist and how to defend against them in a code review.

Jesse Shapiro, Descriptors, magic methods, and inheritance: oh my!

It's very simple to write straightforward imperative code with Python. You can easily define classes and functions, and write behavior inside them. However, pure imperative design means that you'll likely end up writing the same patterns of code over and over - whether it's requests.get() or LOGGER = getLogger(__name__). By taking advantage of some of the more advanced features of the Python language, like descriptors, overridden magic methods, and creative uses of inheritance, we can make our code smaller and more expressive. Proper abstractions will also make it easier to test your code thoroughly and effectively - because you're not reimplementing behavior unnecessarily, you can properly test the one place you do implement it, and rely on it from then on. And, it becomes much easier to add features later on that rely on existing behavior - you just need to describe them in terms of the things you've already implemented.

Robyn Allen, Teaching Python to teens

How does one design a workshop accessible to beginners yet also challenging to seasoned Python programmers? This talk will summarize two pieces of curriculum which have proven successful in engaging teenagers in an extracurricular setting. Unlike traditional computer science lecture material, these problems ask the learner to spend the majority of their time designing an original solution (in pseudocode or outline form). The goal of this talk is to empower attendees to offer similar workshops (for teens) regardless of prior programming experience. As the world faces not only a shortage of software engineers but also a shortage of available engineer-teachers, new curriculum which enables non-programmers to teach programming is urgently needed. Whether or not you have teaching experience (or Python experience), come to this talk and help further the conversation about Python literacy!


Meetup link: [https://www.meetup.com/bostonpython/events/242251013/](https://www.meetup.com/bostonpython/events/242251013/)

[Back to Past Events Page](index.md)