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

**97** channels, **622,428.2** hours playtime between **2023-01-17** and **2023-12-30**


### playtime per genre (top 30)

    40710.7h 6.54% Nachrichten
    29840.2h 4.79% Verkaufsshow
    24960.1h 4.01% Krimiserie
    21143.2h 3.40% Werbesendung
    20268.4h 3.26% Dokureihe
    18566.5h 2.98% Dokusoap
    17939.9h 2.88% Regionalmagazin
    16086.4h 2.58% Dokumentation
    15372.6h 2.47% *unknown*
    11466.0h 1.84% Zeichentrickserie
    11303.7h 1.82% Infomercial
    10964.8h 1.76% Animationsserie
    9475.2h  1.52% Comedyserie
    8841.7h  1.42% Morgenmagazin
    8428.9h  1.35% Religionsmagazin
    8257.9h  1.33% Talkshow
    8112.7h  1.30% Magazin
    6114.9h  0.98% E-Sport
    6101.3h  0.98% Programmende
    6040.6h  0.97% Sitcom
    5681.4h  0.91% Wetterbericht
    5586.6h  0.90% Börsenmagazin
    5164.4h  0.83% Komödie
    5113.6h  0.82% Quiz
    4710.3h  0.76% Wissensmagazin
    4606.6h  0.74% Wirtschaftsmagazin
    4495.6h  0.72% Realityshow
    4478.9h  0.72% Musikmagazin
    4476.2h  0.72% Telenovela
    4399.7h  0.71% Politikmagazin
