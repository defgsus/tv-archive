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

**109** channels, **1,159,957.2** hours playtime between **2023-01-17** and **2024-11-30**


### playtime per genre (top 30)

    75748.1h 6.53% Nachrichten
    52949.8h 4.56% Verkaufsshow
    48414.6h 4.17% Krimiserie
    42726.2h 3.68% Werbesendung
    36159.4h 3.12% Dokureihe
    34517.3h 2.98% Dokusoap
    33966.4h 2.93% Regionalmagazin
    30500.6h 2.63% Dokumentation
    27329.7h 2.36% *unknown*
    21732.3h 1.87% Zeichentrickserie
    21429.3h 1.85% Infomercial
    20732.2h 1.79% Animationsserie
    16564.5h 1.43% Comedyserie
    16255.0h 1.40% Morgenmagazin
    15426.1h 1.33% Religionsmagazin
    15393.0h 1.33% Talkshow
    14438.7h 1.24% Magazin
    11462.7h 0.99% E-Sport
    11201.4h 0.97% Sitcom
    10479.0h 0.90% Wetterbericht
    10263.8h 0.88% Quiz
    10244.8h 0.88% Programmende
    10170.0h 0.88% Komödie
    8920.6h  0.77% Realityshow
    8826.3h  0.76% Politikmagazin
    8711.4h  0.75% Wissensmagazin
    8613.7h  0.74% Börsenmagazin
    7765.7h  0.67% Wirtschaftsmagazin
    7688.6h  0.66% Telenovela
    7666.6h  0.66% Dramaserie
