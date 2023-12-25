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

**97** channels, **615,296.8** hours playtime between **2023-01-17** and **2023-12-26**


### playtime per genre (top 30)

    40304.0h 6.55% Nachrichten
    29503.1h 4.79% Verkaufsshow
    24747.3h 4.02% Krimiserie
    20917.9h 3.40% Werbesendung
    19970.7h 3.25% Dokureihe
    18418.2h 2.99% Dokusoap
    17761.5h 2.89% Regionalmagazin
    15831.8h 2.57% Dokumentation
    15150.3h 2.46% *unknown*
    11350.9h 1.84% Zeichentrickserie
    11182.1h 1.82% Infomercial
    10847.6h 1.76% Animationsserie
    9395.6h  1.53% Comedyserie
    8738.0h  1.42% Morgenmagazin
    8343.7h  1.36% Religionsmagazin
    8201.5h  1.33% Talkshow
    8007.7h  1.30% Magazin
    6062.1h  0.99% E-Sport
    6045.8h  0.98% Programmende
    5961.5h  0.97% Sitcom
    5618.6h  0.91% Wetterbericht
    5532.8h  0.90% Börsenmagazin
    5063.2h  0.82% Quiz
    4993.0h  0.81% Komödie
    4667.2h  0.76% Wissensmagazin
    4568.5h  0.74% Wirtschaftsmagazin
    4450.3h  0.72% Telenovela
    4440.4h  0.72% Realityshow
    4434.2h  0.72% Musikmagazin
    4354.1h  0.71% Politikmagazin
