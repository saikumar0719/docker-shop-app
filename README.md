# Docker Shop App — the same shop app, packed in a lunchbox

## Docker, in simple words — the lunchbox story

Imagine you pack lunch for a friend. You put the food, a spoon, and a
water bottle in one lunchbox. Your friend can open that same lunchbox
on any table, in any room, and eat the same lunch.

Docker is that lunchbox — for a computer program.

- The **app** is the food.
- **Python** is the spoon — the app needs it to run.
- The **Docker image** is the packed lunchbox: app + Python, packed
  together, with a label on the box (here the label is `shop-app:1.0.0`).
- The **container** is the lunchbox opened and the app running. You can
  open the same lunchbox many times, on any computer, and the app
  always gives the same answer.

Without Docker, the app may run on one computer and fail on another,
because the other computer has a different Python version, or is
missing something. With Docker, the app carries everything it needs
inside its own box.

## What this project does

The same small shop app from the Jenkins project, unchanged:

- A shop gets 11 messy orders.
- The app cleans them: duplicate orders are kept only once (the last
  row), orders with no amount are dropped, orders with a negative
  amount are dropped.
- 8 clean orders are left. Total sales: **10550.00**.

Docker does not change the app. Docker only packs it, so it runs the
same on any computer.

## How to run it (you need Docker Desktop installed)

Docker is not magic — it is a program you install first. On a laptop,
install **Docker Desktop** (free for learning). Then:

```bash
cd docker-shop-app
docker build -t shop-app:1.0.0 .
docker run --rm shop-app:1.0.0
```

Or, in one command, with Docker Compose (see `docker-compose.yml`):

```bash
docker compose up
```

Expected output, every time, on every computer:

```
Raw orders: 11
Clean orders: 8
Total sales: 10550.00
```

The same commands are also in `scripts/build_image.sh` and
`scripts/run_app.sh`. If Docker is not installed, those scripts say
so clearly and stop — they never pretend the app ran.

## What GitHub CI checks

Every time code is pushed to GitHub, GitHub Actions (GitHub's own
automatic checker) runs:

1. The Python tests (`pytest`) — the app still cleans correctly.
2. `bash -n` on the scripts — the scripts have no typing mistakes.
3. The real `docker build` and `docker run` — and it checks that the
   output contains `Total sales: 10550.00`.
4. `docker compose config -q` — a check that the Compose file is
   written correctly (this step is allowed to be skipped if the runner
   does not have Docker Compose; the docker build/run check is the
   required one).

## Honest status — please read this

- Docker build and run are verified in **GitHub CI**, not on the
  computer this project was built on. That computer does not have
  Docker installed, so `docker build` / `docker run` were not run
  there. The tests, the file checks, and the script checks were run
  locally and all passed.
- No cloud accounts were used. No money was spent. No credentials
  are anywhere in this project.
- Jenkins is not started in this project. The `Jenkinsfile` shows
  the pipeline: Checkout → Build → Test → **Build Docker image** →
  Package. Jenkins builds the image only after the tests pass.
  The Jenkinsfile itself is in the Jenkins project repo, and here
  it is the same idea, applied to this Docker project.

## What is NOT in this project

- **No Kubernetes.** Kubernetes runs many lunchboxes together. That
  is the next step, after Docker. Docker is the step before
  Kubernetes.
- **No Linux deep dive.** You do not need Linux commands to run this
  project — Docker Desktop handles that part.
- **No real cloud deploy.** This project only builds and runs the
  image on one computer (or in GitHub CI). Sending it to AWS, Azure,
  or GCP is a later step, and the Jenkins project already shows
  that pattern in dry-run form.

## How to explain it in one line

"I packed the same shop app into a Docker image, so it runs the same
on any computer. Jenkins builds the image only after the tests pass."
