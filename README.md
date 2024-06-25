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

**109** channels, **919,798.8** hours playtime between **2023-01-17** and **2024-06-26**


### playtime per genre (top 30)

    60063.5h 6.53% Nachrichten
    43228.2h 4.70% Verkaufsshow
    37543.8h 4.08% Krimiserie
    32567.2h 3.54% Werbesendung
    28949.0h 3.15% Dokureihe
    27816.0h 3.02% Dokusoap
    26752.4h 2.91% Regionalmagazin
    23878.9h 2.60% Dokumentation
    23075.7h 2.51% *unknown*
    16928.9h 1.84% Zeichentrickserie
    16770.5h 1.82% Infomercial
    16429.9h 1.79% Animationsserie
    13745.5h 1.49% Comedyserie
    13127.7h 1.43% Magazin
    12955.8h 1.41% Morgenmagazin
    12467.1h 1.36% Religionsmagazin
    12235.9h 1.33% Talkshow
    9100.4h  0.99% E-Sport
    8610.2h  0.94% Sitcom
    8406.0h  0.91% Programmende
    8215.4h  0.89% Wetterbericht
    7953.5h  0.86% Komödie
    7946.2h  0.86% Quiz
    7843.5h  0.85% Börsenmagazin
    6916.9h  0.75% Politikmagazin
    6827.4h  0.74% Realityshow
    6827.1h  0.74% Wissensmagazin
    6441.3h  0.70% Wirtschaftsmagazin
    6318.5h  0.69% Telenovela
    6026.2h  0.66% Musikmagazin
