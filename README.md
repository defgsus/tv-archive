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

**109** channels, **947,000.3** hours playtime between **2023-01-17** and **2024-07-14**


### playtime per genre (top 30)

    61715.3h 6.52% Nachrichten
    44279.8h 4.68% Verkaufsshow
    38744.3h 4.09% Krimiserie
    33747.6h 3.56% Werbesendung
    29782.1h 3.14% Dokureihe
    28676.3h 3.03% Dokusoap
    27533.0h 2.91% Regionalmagazin
    24565.2h 2.59% Dokumentation
    23629.5h 2.50% *unknown*
    17470.0h 1.84% Zeichentrickserie
    17296.5h 1.83% Infomercial
    16944.2h 1.79% Animationsserie
    14111.3h 1.49% Comedyserie
    13371.6h 1.41% Magazin
    13337.7h 1.41% Morgenmagazin
    12834.2h 1.36% Religionsmagazin
    12549.4h 1.33% Talkshow
    9378.6h  0.99% E-Sport
    8918.6h  0.94% Sitcom
    8613.3h  0.91% Programmende
    8481.6h  0.90% Wetterbericht
    8238.7h  0.87% Komödie
    8184.7h  0.86% Quiz
    7931.2h  0.84% Börsenmagazin
    7132.0h  0.75% Politikmagazin
    7040.6h  0.74% Realityshow
    7033.1h  0.74% Wissensmagazin
    6584.1h  0.70% Wirtschaftsmagazin
    6398.1h  0.68% Telenovela
    6168.9h  0.65% Dramaserie
