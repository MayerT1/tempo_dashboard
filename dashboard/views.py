from django.http import JsonResponse
from django.shortcuts import render


def home(request):
    return JsonResponse({
        "status": "ok",
        "message": "TEMPO Dashboard Running",
        "links": {
            "map": "/map/",
        }
    })


def map_view(request):
    return render(request, 'dashboard/map.html')


def map_markers_api(request):
    """
    Simple marker API scaffold.
    GET  /api/markers/  → list saved markers from session
    POST /api/markers/  → save a marker to session
    """
    if request.method == 'POST':
        import json
        data = json.loads(request.body)
        markers = request.session.get('markers', [])
        markers.append({
            'id': len(markers) + 1,
            'lat': data.get('lat'),
            'lng': data.get('lng'),
            'label': data.get('label', f'Pin #{len(markers)+1}'),
        })
        request.session['markers'] = markers
        return JsonResponse({'status': 'saved', 'marker': markers[-1]})

    markers = request.session.get('markers', [])
    return JsonResponse({'markers': markers})
