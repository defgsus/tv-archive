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

**96** channels, **82,927.9** hours playtime between **2023-01-17** and **2023-03-03**


### playtime per genre (top 30)

    5902.9h 7.12% Nachrichten
    4192.5h 5.06% Verkaufsshow
    3525.4h 4.25% Krimiserie
    2813.9h 3.39% Werbesendung
    2752.9h 3.32% Dokusoap
    2467.9h 2.98% Regionalmagazin
    2467.6h 2.98% Dokureihe
    2029.1h 2.45% Dokumentation
    1959.9h 2.36% *unknown*
    1577.6h 1.90% Animationsserie
    1517.2h 1.83% Infomercial
    1515.9h 1.83% Zeichentrickserie
    1357.1h 1.64% Comedyserie
    1197.8h 1.44% Morgenmagazin
    1127.9h 1.36% Programmende
    1086.5h 1.31% Talkshow
    1083.9h 1.31% Religionsmagazin
    883.7h  1.07% Magazin
    858.8h  1.04% E-Sport
    787.4h  0.95% Sitcom
    743.1h  0.90% Börsenmagazin
    733.7h  0.88% Wetterbericht
    677.5h  0.82% Wirtschaftsmagazin
    652.9h  0.79% Wissensmagazin
    624.2h  0.75% Quiz
    608.6h  0.73% Dramaserie
    600.2h  0.72% Musikmagazin
    593.7h  0.72% Gesundheitsmagazin
    577.9h  0.70% Telenovela
    539.4h  0.65% Gerichtsshow
