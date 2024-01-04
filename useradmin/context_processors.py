from datetime import datetime


def tyear(request):
    return {"current_year": datetime.now().year }