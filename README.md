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

**101** channels, **760,644.4** hours playtime between **2023-01-17** and **2024-03-17**


### playtime per genre (top 30)

    49510.7h 6.51% Nachrichten
    36549.2h 4.81% Verkaufsshow
    31001.9h 4.08% Krimiserie
    26381.5h 3.47% Werbesendung
    24218.3h 3.18% Dokureihe
    22979.0h 3.02% Dokusoap
    22092.2h 2.90% Regionalmagazin
    19621.1h 2.58% Dokumentation
    19509.3h 2.56% *unknown*
    14040.4h 1.85% Zeichentrickserie
    13837.2h 1.82% Infomercial
    13456.7h 1.77% Animationsserie
    11544.5h 1.52% Comedyserie
    10792.9h 1.42% Morgenmagazin
    10374.5h 1.36% Magazin
    10268.9h 1.35% Religionsmagazin
    10131.0h 1.33% Talkshow
    7498.5h  0.99% E-Sport
    7179.0h  0.94% Programmende
    7129.5h  0.94% Sitcom
    6757.6h  0.89% Wetterbericht
    6749.7h  0.89% Börsenmagazin
    6469.4h  0.85% Quiz
    6413.1h  0.84% Komödie
    5682.1h  0.75% Wissensmagazin
    5507.4h  0.72% Politikmagazin
    5505.3h  0.72% Realityshow
    5493.6h  0.72% Wirtschaftsmagazin
    5440.2h  0.72% Telenovela
    5179.1h  0.68% Musikmagazin
