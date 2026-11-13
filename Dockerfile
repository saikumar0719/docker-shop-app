# Dockerfile — the recipe for packing the lunchbox.
# Each line is one packing step. Read it top to bottom.

# Start from a small, ready-made Python box (version 3.11, slim = small).
FROM python:3.11-slim

# Work inside a folder called /app in the box.
WORKDIR /app

# Copy the list of test tools, and install them.
# Honest note: the app itself needs only Python's built-in tools,
# so this install is really for the tests (pytest). It changes
# nothing about how the app runs.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the shop app into the box.
COPY app/ ./app/

# When the box is opened (the container runs), run the app.
CMD ["python", "-m", "app.main"]
