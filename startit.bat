docker start pg_swapi
docker run -it --rm --expose 8001 -p 8001:8000 --link pg_swapi -v C:/Users/aaron.tesch/github/swapi:/swapi --workdir /swapi python:2.7.16 make install build load_data serve