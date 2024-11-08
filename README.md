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

**109** channels, **1,128,689.1** hours playtime between **2023-01-17** and **2024-11-09**


### playtime per genre (top 30)

    73539.4h 6.52% Nachrichten
    51784.2h 4.59% Verkaufsshow
    46991.1h 4.16% Krimiserie
    41443.3h 3.67% Werbesendung
    35262.4h 3.12% Dokureihe
    33722.1h 2.99% Dokusoap
    33028.0h 2.93% Regionalmagazin
    29628.1h 2.63% Dokumentation
    26751.7h 2.37% *unknown*
    21103.2h 1.87% Zeichentrickserie
    20788.9h 1.84% Infomercial
    20181.0h 1.79% Animationsserie
    16222.0h 1.44% Comedyserie
    15801.0h 1.40% Morgenmagazin
    15116.8h 1.34% Religionsmagazin
    14944.1h 1.32% Talkshow
    14186.8h 1.26% Magazin
    11135.8h 0.99% E-Sport
    10906.1h 0.97% Sitcom
    10207.6h 0.90% Wetterbericht
    9994.9h  0.89% Programmende
    9941.5h  0.88% Quiz
    9920.7h  0.88% Komödie
    8619.5h  0.76% Realityshow
    8550.1h  0.76% Politikmagazin
    8512.9h  0.75% Börsenmagazin
    8474.3h  0.75% Wissensmagazin
    7578.2h  0.67% Wirtschaftsmagazin
    7461.8h  0.66% Telenovela
    7388.7h  0.65% Dramaserie
