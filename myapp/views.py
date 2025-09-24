import requests
from django.core.paginator import Paginator
from django.core.cache import cache
from django.shortcuts import render
from django.http import JsonResponse

API_KEY = "8abbe5f8aa741264361b37dbfdea7968"
BASE_URL = "https://api.themoviedb.org/3"  # <-- this must be here


def home(request):
    query = request.GET.get("q")
    movies = []

    if query:
        url = f"{BASE_URL}/search/movie?api_key={API_KEY}&query={query}"
        try:
            response = requests.get(url)
            data = response.json()
            movies = data.get("results") or []  # fallback to empty list
        except Exception as e:
            print("Error fetching search results:", e)
            movies = []
    else:
        movies = cache.get("popular_movies")
        if not movies:
            movies = []
            for page in range(1, 11):  # fetch 10 pages (~200 movies)
                url = f"{BASE_URL}/movie/popular?api_key={API_KEY}&language=en-US&page={page}"
                try:
                    response = requests.get(url)
                    data = response.json()
                    results = data.get("results")
                    if results:
                        movies.extend(results)
                except Exception as e:
                    print(f"Error fetching popular movies page {page}: {e}")
            cache.set("popular_movies", movies, 60 * 30)

    # Paginate results
    paginator = Paginator(movies, 20)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "myapp/home.html", {"movies": page_obj})

def movie_detail(request, movie_id):
    detail_url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"
    detail_data = requests.get(detail_url).json()

    credits_url = f"https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={API_KEY}&language=en-US"
    credits_data = requests.get(credits_url).json()
    cast = credits_data.get("cast", [])[:20]  # top 20 cast

    return render(request, "myapp/detail.html", {
        "movie": detail_data,
        "cast": cast
    })


from django.http import JsonResponse

def search_suggestions(request):
    query = request.GET.get('q', '')
    suggestions = []

    if query:
        url = f"{BASE_URL}/search/movie?api_key={API_KEY}&query={query}"
        try:
            response = requests.get(url)
            data = response.json()
            results = data.get("results") or []
            # Take first 5 suggestions
            for movie in results[:5]:
                suggestions.append({"title": movie.get("title"), "id": movie.get("id")})
        except Exception as e:
            print("Error fetching suggestions:", e)

    return JsonResponse({"suggestions": suggestions})