# Docker words, in simple words

Docker is a **lunchbox**. The app + Python are packed together in the
box, so it runs the same on any computer.

- **Image** — the packed lunchbox. The app + Python, packed and labelled, ready to carry. Example here: `shop-app:1.0.0`.
- **Container** — the lunchbox opened and the app running. Example here: when you run the image, the app prints Raw 11, Clean 8, Total sales 10550.00.
- **Dockerfile** — the recipe for packing the lunchbox. It is a text file that lists the packing steps, top to bottom.
- **Build** — packing the lunchbox. The command is `docker build`. Example here: `docker build -t shop-app:1.0.0 .`
- **Run** — opening the lunchbox and starting the app. The command is `docker run`. Example here: `docker run --rm shop-app:1.0.0`.
- **Tag** — the label on the lunchbox. It has a name and a version, like `shop-app:1.0.0`. The same label is used in the Dockerfile steps, the Jenkinsfile, and the scripts, so everyone means the same box.
- **Port** — a door number for a website or a service to talk through. This app only prints numbers, it is not a website, so it needs no port.
- **Volume** — a shared folder between your computer and the lunchbox, so files can be kept after the box is closed. This app needs no volume, because it only reads its small orders file and prints numbers.
- **Registry** — a shop shelf where packed lunchboxes are kept, so other computers can take one. Examples: Docker Hub, or a cloud registry. This project does not push the image to any registry — it only builds and runs it on one computer.

Remember the one line: image = the packed box, container = the box
opened and running. Many people mix these two up. You will not.
