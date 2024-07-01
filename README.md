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

**109** channels, **928,884.1** hours playtime between **2023-01-17** and **2024-07-02**


### playtime per genre (top 30)

    60613.4h 6.53% Nachrichten
    43564.0h 4.69% Verkaufsshow
    37945.1h 4.09% Krimiserie
    32964.2h 3.55% Werbesendung
    29219.8h 3.15% Dokureihe
    28098.7h 3.02% Dokusoap
    26998.3h 2.91% Regionalmagazin
    24110.7h 2.60% Dokumentation
    23245.1h 2.50% *unknown*
    17111.8h 1.84% Zeichentrickserie
    16944.5h 1.82% Infomercial
    16598.2h 1.79% Animationsserie
    13865.4h 1.49% Comedyserie
    13271.7h 1.43% Magazin
    13076.1h 1.41% Morgenmagazin
    12589.3h 1.36% Religionsmagazin
    12333.0h 1.33% Talkshow
    9187.2h  0.99% E-Sport
    8711.5h  0.94% Sitcom
    8476.9h  0.91% Programmende
    8302.2h  0.89% Wetterbericht
    8069.4h  0.87% Komödie
    8029.9h  0.86% Quiz
    7869.4h  0.85% Börsenmagazin
    6990.9h  0.75% Politikmagazin
    6905.4h  0.74% Realityshow
    6898.7h  0.74% Wissensmagazin
    6485.9h  0.70% Wirtschaftsmagazin
    6344.1h  0.68% Telenovela
    6071.5h  0.65% Musikmagazin
