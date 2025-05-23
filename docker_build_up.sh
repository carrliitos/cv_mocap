echo "========== down =========="
echo "docker compose -f concurrent_camera_reader/docker-compose.yaml down"
docker compose -f concurrent_camera_reader/docker-compose.yaml down
echo "========== build =========="
echo "docker compose -f concurrent_camera_reader/docker-compose.yaml build"
docker compose -f concurrent_camera_reader/docker-compose.yaml build
echo "========== up =========="
echo "docker compose -f concurrent_camera_reader/docker-compose.yaml up"
docker compose -f concurrent_camera_reader/docker-compose.yaml up
echo "=========="