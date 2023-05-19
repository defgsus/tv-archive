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

**96** channels, **222,816.0** hours playtime between **2023-01-17** and **2023-05-20**


### playtime per genre (top 30)

    15030.1h 6.75% Nachrichten
    10802.1h 4.85% Verkaufsshow
    9019.1h  4.05% Krimiserie
    7385.4h  3.31% Werbesendung
    7235.1h  3.25% Dokureihe
    6636.2h  2.98% Dokusoap
    6424.8h  2.88% Regionalmagazin
    5684.7h  2.55% Dokumentation
    5507.5h  2.47% *unknown*
    4148.4h  1.86% Zeichentrickserie
    4079.0h  1.83% Infomercial
    4011.8h  1.80% Animationsserie
    3729.4h  1.67% Comedyserie
    3097.2h  1.39% Morgenmagazin
    3031.5h  1.36% Programmende
    2941.3h  1.32% Talkshow
    2906.9h  1.30% Religionsmagazin
    2567.4h  1.15% Magazin
    2220.3h  1.00% E-Sport
    2102.4h  0.94% Sitcom
    2034.8h  0.91% Börsenmagazin
    2018.7h  0.91% Wetterbericht
    1768.0h  0.79% Wirtschaftsmagazin
    1735.1h  0.78% Wissensmagazin
    1720.7h  0.77% Quiz
    1718.3h  0.77% Musikmagazin
    1577.3h  0.71% Telenovela
    1546.1h  0.69% Sportmagazin
    1542.7h  0.69% Komödie
    1504.5h  0.68% Gesundheitsmagazin
