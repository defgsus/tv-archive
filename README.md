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

**109** channels, **1,199,629.1** hours playtime between **2023-01-17** and **2024-12-26**


### playtime per genre (top 30)

    78443.8h 6.54% Nachrichten
    54457.8h 4.54% Verkaufsshow
    49896.7h 4.16% Krimiserie
    44358.1h 3.70% Werbesendung
    37310.4h 3.11% Dokureihe
    35359.6h 2.95% Dokusoap
    35048.7h 2.92% Regionalmagazin
    31809.3h 2.65% Dokumentation
    28402.1h 2.37% *unknown*
    22504.7h 1.88% Zeichentrickserie
    22207.9h 1.85% Infomercial
    21428.2h 1.79% Animationsserie
    16954.7h 1.41% Comedyserie
    16777.8h 1.40% Morgenmagazin
    15884.8h 1.32% Talkshow
    15778.5h 1.32% Religionsmagazin
    14729.1h 1.23% Magazin
    11863.1h 0.99% E-Sport
    11512.5h 0.96% Sitcom
    10853.8h 0.90% Wetterbericht
    10819.9h 0.90% Komödie
    10606.0h 0.88% Quiz
    10555.7h 0.88% Programmende
    9260.2h  0.77% Realityshow
    9156.5h  0.76% Politikmagazin
    8955.0h  0.75% Wissensmagazin
    8721.7h  0.73% Börsenmagazin
    7982.7h  0.67% Wirtschaftsmagazin
    7960.0h  0.66% Arztserie
    7949.5h  0.66% Dramaserie
