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

**109** channels, **1,168,411.0** hours playtime between **2023-01-17** and **2024-12-05**


### playtime per genre (top 30)

    76349.3h 6.53% Nachrichten
    53213.2h 4.55% Verkaufsshow
    48747.0h 4.17% Krimiserie
    43076.9h 3.69% Werbesendung
    36407.5h 3.12% Dokureihe
    34714.6h 2.97% Dokusoap
    34214.5h 2.93% Regionalmagazin
    30758.7h 2.63% Dokumentation
    27526.8h 2.36% *unknown*
    21896.4h 1.87% Zeichentrickserie
    21605.8h 1.85% Infomercial
    20889.4h 1.79% Animationsserie
    16654.2h 1.43% Comedyserie
    16375.9h 1.40% Morgenmagazin
    15505.5h 1.33% Religionsmagazin
    15501.3h 1.33% Talkshow
    14500.0h 1.24% Magazin
    11540.9h 0.99% E-Sport
    11271.2h 0.96% Sitcom
    10558.3h 0.90% Wetterbericht
    10335.8h 0.88% Quiz
    10314.8h 0.88% Programmende
    10260.8h 0.88% Komödie
    8998.6h  0.77% Realityshow
    8907.1h  0.76% Politikmagazin
    8770.4h  0.75% Wissensmagazin
    8638.5h  0.74% Börsenmagazin
    7814.1h  0.67% Wirtschaftsmagazin
    7746.9h  0.66% Telenovela
    7728.7h  0.66% Dramaserie
