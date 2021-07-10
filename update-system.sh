
export COMPOSE_HTTP_TIMEOUT=1000

echo "Fetching updates"
docker-compose pull

echo "Stopping services"
docker-compose down

echo "Rebuilding services"
docker-compose up -d --force-recreate --remove-orphans

#containers=$(docker ps --format '{{.Names}}')
containers=$(docker-compose config --services)
stop=(appdaemon node_red wireguard csgo_server diskspeed magicmirror mosquitto redis seafile seafile_db seafile_memcached seafile_elasticsearch webtrees webtrees_db)

res=($(comm -12 <(echo ${containers[*]}| tr " " "\n"| sort) <(echo ${stop[*]} | tr " " "\n"| sort)| sort -g))

echo "Stopping unused containers ${res[*]}"
#docker-compose stop ${res[*]}


echo "Pruning system"
docker system prune -af --volumes


sleep 5
docker-compose ps
echo "Done"
