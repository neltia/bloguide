docker run -d --name trivy-api \
--mount type=bind,source=/etc/docker/akd-upload-images,target=/usr/share/docker/upload-images,readonly \
-p 9001:9001 \
-v /var/run/docker.sock:/var/run/docker.sock \
test-api01
