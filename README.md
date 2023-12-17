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

**97** channels, **600,955.8** hours playtime between **2023-01-17** and **2023-12-18**


### playtime per genre (top 30)

    39432.1h 6.56% Nachrichten
    28845.2h 4.80% Verkaufsshow
    24273.4h 4.04% Krimiserie
    20432.8h 3.40% Werbesendung
    19528.2h 3.25% Dokureihe
    18038.5h 3.00% Dokusoap
    17368.6h 2.89% Regionalmagazin
    15412.4h 2.56% Dokumentation
    14721.8h 2.45% *unknown*
    11104.6h 1.85% Zeichentrickserie
    10950.9h 1.82% Infomercial
    10652.2h 1.77% Animationsserie
    9210.1h  1.53% Comedyserie
    8552.4h  1.42% Morgenmagazin
    8151.4h  1.36% Religionsmagazin
    8058.0h  1.34% Talkshow
    7755.3h  1.29% Magazin
    5935.2h  0.99% Programmende
    5914.8h  0.98% E-Sport
    5815.8h  0.97% Sitcom
    5495.3h  0.91% Wetterbericht
    5425.4h  0.90% Börsenmagazin
    4974.0h  0.83% Quiz
    4714.2h  0.78% Komödie
    4586.7h  0.76% Wissensmagazin
    4480.9h  0.75% Wirtschaftsmagazin
    4352.2h  0.72% Telenovela
    4350.1h  0.72% Musikmagazin
    4336.8h  0.72% Realityshow
    4259.2h  0.71% Politikmagazin
