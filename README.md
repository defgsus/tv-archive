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

**108** channels, **856,134.3** hours playtime between **2023-01-17** and **2024-05-16**


### playtime per genre (top 30)

    55920.2h 6.53% Nachrichten
    40776.9h 4.76% Verkaufsshow
    34868.7h 4.07% Krimiserie
    29968.8h 3.50% Werbesendung
    26953.4h 3.15% Dokureihe
    25871.9h 3.02% Dokusoap
    24926.8h 2.91% Regionalmagazin
    22175.3h 2.59% Dokumentation
    21772.8h 2.54% *unknown*
    15737.5h 1.84% Zeichentrickserie
    15574.6h 1.82% Infomercial
    15248.8h 1.78% Animationsserie
    12917.2h 1.51% Comedyserie
    12157.4h 1.42% Magazin
    12080.7h 1.41% Morgenmagazin
    11576.1h 1.35% Religionsmagazin
    11405.1h 1.33% Talkshow
    8506.9h  0.99% E-Sport
    7923.3h  0.93% Programmende
    7908.4h  0.92% Sitcom
    7609.4h  0.89% Wetterbericht
    7533.1h  0.88% Börsenmagazin
    7409.1h  0.87% Quiz
    7326.5h  0.86% Komödie
    6329.8h  0.74% Wissensmagazin
    6311.4h  0.74% Realityshow
    6310.6h  0.74% Politikmagazin
    6106.1h  0.71% Wirtschaftsmagazin
    6093.1h  0.71% Telenovela
    5675.4h  0.66% Musikmagazin
