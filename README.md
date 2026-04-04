# jerry_website
individual website

# Docker build
Raspberry Pi 5 uses ARM64 (linux/arm64). Build from your Mac with:
"sudo docker build -t jerrynguyen0210/jerry_web:latest ."
# Docker push
"sudo docker tag jerry-website:latest jerrynguyen0210/jerry_web:latest"
"sudo docker push jerrynguyen0210/jerry_web:latest"
# Docker pull
"sudo docker pull jerrynguyen0210/jerry_web:latest"
# Docker run
sudo docker run -d -p 8501:8501 jerrynguyen0210/jerry_web:latest