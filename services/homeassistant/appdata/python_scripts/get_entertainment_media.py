from PyArr import RadarrAPI, SonarrAPI
import json

radarr_host = data.get('RADARR_INTERNAL_DOMAIN')
radarr_api_key = data.get('RADARR_API_KEY')
sonarr_host = data.get('SONARR_INTERNAL_DOMAIN')
sonarr_api_key = data.get('SONARR_API_KEY')

logger.info("Radarr host %s with api key %s", radarr_host, radarr_api_key)
logger.info("Sonarr host %s with api key %s", sonarr_host, sonarr_api_key)


# Fetch movies
if (radarr_host is not None and radarr_host is not None):
    radarr = RadarrAPI(radarr_host, radarr_api_key)
    movies = list(radarr.getMovie())
    for i, movie in enumerate(movies):
        print (f"{i}: {movie['title']}")


# Fetch series
if (radarr_host is not None and radarr_host is not None):
    sonarr = SonarrAPI(sonarr_host, sonarr_api_key)