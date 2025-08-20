from django.shortcuts import render

def important_dates_view(request):
    important_dates = [
        {"date": "February 14", "event": "National Donor Day (USA)"},
        {"date": "March 13", "event": "World Kidney Day"},
        {"date": "April", "event": "National Donate Life Month"},
        {"date": "April 7", "event": "World Health Day"},
        {"date": "June 6", "event": "National Transplant Week (UK)"},
        {"date": "August 13", "event": "World Organ Donation Day"},
        {"date": "September 25", "event": "World Heart Day"},
        {"date": "October 10", "event": "World Mental Health Day"},
        {"date": "November", "event": "National Donor Sabbath (USA)"},
        {"date": "December 3", "event": "International Day of Persons with Disabilities"},
    ]
    return render(request, "important_dates.html", {"important_dates": important_dates})
