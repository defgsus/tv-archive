# Archive of TV-shows

Scraped directly from a german webpage, started at about mid-January 2023.

TV is not as important anymore but still, archiving the decisions of which programs to run at what time
becomes another puzzle piece in the revelation of mind-control.. 

Data is stored in [docs/data/YEAR/MONTH/YEAR-MONTH-DAY.ndjson](docs/data/) files. 
Each entry looks like this:

```python
{
  "id": "181043890", 
  "url": "https://www.hoerzu.de/tv-programm/south-park-kohle-an-den-chefkoch/bid_181043890/", 
  "channel": "Comedy Central", 
  "title": "South Park", 
  "date": "2023-01-17T05:15:00",    # probably Europe/Berlin timezone 
  "length": 25,                     # minutes 
  "sub_title": "Serie", 
  "genre": "Erwachsenen-Animationsserie", 
  "season": 2, 
  "episode": 14, 
  "year": 1998, 
  "countries": ["USA"],
}
```

## Statistics

**101** channels, **776,413.6** hours playtime between **2023-01-17** and **2024-03-26**


### playtime per genre (top 30)

    50536.2h 6.51% Nachrichten
    37314.3h 4.81% Verkaufsshow
    31664.5h 4.08% Krimiserie
    27002.1h 3.48% Werbesendung
    24679.3h 3.18% Dokureihe
    23442.6h 3.02% Dokusoap
    22568.3h 2.91% Regionalmagazin
    20038.3h 2.58% Dokumentation
    19925.0h 2.57% *unknown*
    14301.7h 1.84% Zeichentrickserie
    14128.0h 1.82% Infomercial
    13780.7h 1.77% Animationsserie
    11775.4h 1.52% Comedyserie
    11014.2h 1.42% Morgenmagazin
    10610.1h 1.37% Magazin
    10497.5h 1.35% Religionsmagazin
    10368.4h 1.34% Talkshow
    7655.3h  0.99% E-Sport
    7303.7h  0.94% Programmende
    7250.7h  0.93% Sitcom
    6895.2h  0.89% Börsenmagazin
    6890.7h  0.89% Wetterbericht
    6639.7h  0.86% Quiz
    6530.8h  0.84% Komödie
    5797.7h  0.75% Wissensmagazin
    5646.9h  0.73% Politikmagazin
    5599.5h  0.72% Realityshow
    5597.4h  0.72% Wirtschaftsmagazin
    5555.3h  0.72% Telenovela
    5261.3h  0.68% Musikmagazin
