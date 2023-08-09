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

**96** channels, **369,774.6** hours playtime between **2023-01-17** and **2023-08-10**


### playtime per genre (top 30)

    24495.6h 6.62% Nachrichten
    17566.7h 4.75% Verkaufsshow
    14939.3h 4.04% Krimiserie
    12452.5h 3.37% Werbesendung
    12156.0h 3.29% Dokureihe
    11174.4h 3.02% Dokusoap
    10618.5h 2.87% Regionalmagazin
    9312.7h  2.52% Dokumentation
    8988.8h  2.43% *unknown*
    6995.5h  1.89% Zeichentrickserie
    6759.5h  1.83% Infomercial
    6538.3h  1.77% Animationsserie
    6071.8h  1.64% Comedyserie
    5195.2h  1.40% Morgenmagazin
    4912.9h  1.33% Religionsmagazin
    4876.2h  1.32% Talkshow
    4443.8h  1.20% Magazin
    4159.9h  1.12% Programmende
    3658.6h  0.99% E-Sport
    3481.2h  0.94% Wetterbericht
    3479.3h  0.94% Sitcom
    3366.6h  0.91% Börsenmagazin
    2967.0h  0.80% Quiz
    2909.1h  0.79% Musikmagazin
    2838.5h  0.77% Wirtschaftsmagazin
    2832.1h  0.77% Komödie
    2783.9h  0.75% Wissensmagazin
    2563.3h  0.69% Telenovela
    2407.4h  0.65% Sportmagazin
    2388.0h  0.65% Reportagereihe
