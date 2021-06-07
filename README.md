# Jukebox-APIs

DOCUMENT : Backend APIs are browsable api can be used as both JSON and API

below is assignment detail:

	1. API to create/update music album records:
		Endpoint: /api/albums/
		Method: POST/PATCH
		Request Format: 
		{
			"album_name": "album_name",
			"album_release_date": album_release_date,
			"album_genre": album_genre[choice of ("CM", "Country music"),("EM", "Electronic music"),("RM", "Rock music"),("HM", "Hip hop music"),("LM", "Latin music"),("PM", "Pop music")],
			"album_price": decimal value,
			"album_description": "album_description",
			"album_musicians": [list of musician id ]
		}
	2. API to create/update musician records
		Endpoint: /api/musicians/
		Method: POST/PATCH
		Request Format: 
		{
			"musicians_name": "musicians_name",
			"musicians_type": musicians_type [choice of ("V", "Vocalist"), ("I", "Instrumentalist")]
		}
	3. API to retrieve the list of Music albums sorted by Date of release in ascending order (i.e Oldest first)
		Endpoint: /api/albums/
		Method: GET
	4. API to retrieve the list of Music albums for a specified musician sorted by Price in ascending order (i.e Lowest first)
		Endpoint: /api/musicians/list-album-musician/<uuid:musicians_token>/
		Method: GET
	5. API to retrieve the list of musicians for a specified music album sorted by musician's Name in ascending order.
		Endpoint: /api/musicians/list-sorted-album/<uuid:album_token>/
		Method: GET
