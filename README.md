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

**96** channels, **61,089.2** hours playtime between **2023-01-17** and **2023-02-19**


### playtime per genre (top 30)

    4285.6h 7.02% Nachrichten
    3126.1h 5.12% Verkaufsshow
    2584.1h 4.23% Krimiserie
    2077.8h 3.40% Werbesendung
    2076.0h 3.40% Dokusoap
    1802.9h 2.95% Dokureihe
    1770.5h 2.90% Regionalmagazin
    1524.4h 2.50% Dokumentation
    1500.5h 2.46% *unknown*
    1157.0h 1.89% Zeichentrickserie
    1126.3h 1.84% Infomercial
    1124.7h 1.84% Animationsserie
    1004.5h 1.64% Comedyserie
    865.2h  1.42% Morgenmagazin
    816.1h  1.34% Programmende
    798.1h  1.31% Talkshow
    788.8h  1.29% Religionsmagazin
    669.1h  1.10% Magazin
    645.1h  1.06% E-Sport
    578.2h  0.95% Sitcom
    535.4h  0.88% Wetterbericht
    533.0h  0.87% Börsenmagazin
    504.2h  0.83% Wirtschaftsmagazin
    472.2h  0.77% Wissensmagazin
    464.0h  0.76% Quiz
    450.1h  0.74% Musikmagazin
    442.9h  0.72% Dramaserie
    436.3h  0.71% Gesundheitsmagazin
    424.6h  0.70% Telenovela
    401.2h  0.66% Gerichtsshow
