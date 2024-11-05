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

**109** channels, **1,125,089.5** hours playtime between **2023-01-17** and **2024-11-06**


### playtime per genre (top 30)

    73289.6h 6.51% Nachrichten
    51635.8h 4.59% Verkaufsshow
    46805.4h 4.16% Krimiserie
    41296.1h 3.67% Werbesendung
    35162.2h 3.13% Dokureihe
    33620.8h 2.99% Dokusoap
    32890.1h 2.92% Regionalmagazin
    29550.5h 2.63% Dokumentation
    26657.7h 2.37% *unknown*
    21036.0h 1.87% Zeichentrickserie
    20717.4h 1.84% Infomercial
    20117.7h 1.79% Animationsserie
    16177.8h 1.44% Comedyserie
    15744.9h 1.40% Morgenmagazin
    15088.8h 1.34% Religionsmagazin
    14885.3h 1.32% Talkshow
    14163.7h 1.26% Magazin
    11110.1h 0.99% E-Sport
    10859.8h 0.97% Sitcom
    10177.1h 0.90% Wetterbericht
    9968.5h  0.89% Programmende
    9903.1h  0.88% Komödie
    9893.7h  0.88% Quiz
    8585.5h  0.76% Realityshow
    8512.1h  0.76% Politikmagazin
    8497.7h  0.76% Börsenmagazin
    8449.0h  0.75% Wissensmagazin
    7550.6h  0.67% Wirtschaftsmagazin
    7423.4h  0.66% Telenovela
    7351.4h  0.65% Dramaserie
