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

**109** channels, **1,010,682.0** hours playtime between **2023-01-17** and **2024-08-24**


### playtime per genre (top 30)

    65768.6h 6.51% Nachrichten
    47054.8h 4.66% Verkaufsshow
    41550.3h 4.11% Krimiserie
    36406.8h 3.60% Werbesendung
    31755.4h 3.14% Dokureihe
    30556.2h 3.02% Dokusoap
    29486.5h 2.92% Regionalmagazin
    26368.2h 2.61% Dokumentation
    24645.2h 2.44% *unknown*
    18742.3h 1.85% Zeichentrickserie
    18509.4h 1.83% Infomercial
    18104.0h 1.79% Animationsserie
    14863.7h 1.47% Comedyserie
    14186.0h 1.40% Morgenmagazin
    13734.2h 1.36% Religionsmagazin
    13533.2h 1.34% Magazin
    13254.4h 1.31% Talkshow
    9996.7h  0.99% E-Sport
    9624.3h  0.95% Sitcom
    9123.7h  0.90% Wetterbericht
    9096.8h  0.90% Programmende
    8868.9h  0.88% Komödie
    8711.7h  0.86% Quiz
    8145.9h  0.81% Börsenmagazin
    7558.7h  0.75% Politikmagazin
    7521.7h  0.74% Wissensmagazin
    7494.1h  0.74% Realityshow
    6903.6h  0.68% Wirtschaftsmagazin
    6655.9h  0.66% Telenovela
    6598.3h  0.65% Dramaserie
