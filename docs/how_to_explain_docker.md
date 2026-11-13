# How to explain Docker — ready to say

Say these lines as they are. Simple words are strong.

## 30-second version

"I packed the same shop app into a Docker image, so it runs the same
on any computer. Jenkins builds the image only after the tests pass."

## 1-minute version

"I took the same shop app from my Jenkins project — it cleans 11
messy orders into 8 clean orders, total sales 10550. I wrote a
Dockerfile, which is the recipe for packing the app together with
Python into a Docker image. An image is like a lunchbox: everything
the app needs is inside one box. When I run the image, it becomes a
container, and the app gives the same answer on any computer. I also
added a Jenkins stage, Build Docker image, after the Test stage, so
Jenkins builds the image only if the tests pass. I checked the build
and run in GitHub CI, because Docker was not installed on my local
computer."

## 4 questions and answers

**Q1. What is Docker?**
A. "Docker packs an app together with everything it needs to run,
into one box called an image. That box runs the same on any computer."

**Q2. What is an image vs a container?**
A. "An image is the packed lunchbox. A container is the lunchbox
opened and the app running. One image can be opened many times, and
each time is a container."

**Q3. What happens if a test fails?**
A. "Jenkins stops at the Test stage. The Docker image is never built.
The wrong code cannot go forward. I fix the code, and run again."

**Q4. Why does the same app give the same total in Docker?**
A. "Because the app and its data are packed together in the same
image. The numbers are the same — raw 11, clean 8, total sales
10550.00 — because the app code did not change. Docker only changed
how it is packed and run, not what it does."
