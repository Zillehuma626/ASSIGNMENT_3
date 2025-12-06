# selenium-tests/Dockerfile
FROM python:3.12-slim

# 1. Install system dependencies
# Added --no-install-recommends to keep image small
# Added rm -rf /var/lib/apt/lists/* to clean up apt cache
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    curl \
    xvfb \
    gnupg2 \
    ca-certificates \
    --no-install-recommends \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# 2. Install Google Chrome (Fixed for Debian Trixie/Sid)
RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | gpg --dearmor -o /usr/share/keyrings/google-chrome.gpg \
    && echo "deb [arch=amd64 signed-by=/usr/share/keyrings/google-chrome.gpg] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list \
    && apt-get update && apt-get install -y google-chrome-stable \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# 3. Set working directory
WORKDIR /app

# 4. Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy Selenium tests
COPY . .

# 6. Run the test
CMD ["python", "test8.py"]