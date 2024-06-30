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

**109** channels, **927,079.8** hours playtime between **2023-01-17** and **2024-07-01**


### playtime per genre (top 30)

    60490.9h 6.52% Nachrichten
    43503.7h 4.69% Verkaufsshow
    37857.3h 4.08% Krimiserie
    32884.3h 3.55% Werbesendung
    29172.4h 3.15% Dokureihe
    28050.2h 3.03% Dokusoap
    26931.7h 2.91% Regionalmagazin
    24071.8h 2.60% Dokumentation
    23215.2h 2.50% *unknown*
    17075.7h 1.84% Zeichentrickserie
    16912.9h 1.82% Infomercial
    16563.6h 1.79% Animationsserie
    13836.7h 1.49% Comedyserie
    13247.5h 1.43% Magazin
    13041.7h 1.41% Morgenmagazin
    12573.6h 1.36% Religionsmagazin
    12323.4h 1.33% Talkshow
    9171.0h  0.99% E-Sport
    8687.4h  0.94% Sitcom
    8462.5h  0.91% Programmende
    8285.0h  0.89% Wetterbericht
    8045.6h  0.87% Komödie
    8001.6h  0.86% Quiz
    7860.7h  0.85% Börsenmagazin
    6972.4h  0.75% Politikmagazin
    6889.7h  0.74% Wissensmagazin
    6881.3h  0.74% Realityshow
    6474.6h  0.70% Wirtschaftsmagazin
    6337.7h  0.68% Telenovela
    6067.5h  0.65% Musikmagazin
