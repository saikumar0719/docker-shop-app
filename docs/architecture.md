# How the pieces fit together

Text diagram — read it top to bottom:

```
code (app/main.py + sample_orders.csv)
  -> Dockerfile (the packing recipe)
  -> docker build
  -> image shop-app:1.0.0  (the packed lunchbox)
  -> docker run
  -> container (the lunchbox opened, the app running)
  -> output, always the same:
       Raw orders: 11
       Clean orders: 8
       Total sales: 10550.00
```

## Where Jenkins fits

```
GitHub (new code)
  -> Jenkins reads the Jenkinsfile
  -> Checkout -> Build -> Test (the gate)
  -> Build Docker image (only if Test passed)
  -> Package (keep a copy of the packed files)
```

Jenkins does not change the app. Jenkins only makes sure the steps
happen in order, and stops everything if a test fails.

## What is NOT here

- No Kubernetes. Kubernetes runs many lunchboxes together. That is
  the next step, after Docker.
- No cloud. The image is built and run on one computer (or in
  GitHub CI). Sending it to AWS, Azure, or GCP is a later step.
