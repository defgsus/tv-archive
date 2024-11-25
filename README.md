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

**109** channels, **1,154,844.9** hours playtime between **2023-01-17** and **2024-11-26**


### playtime per genre (top 30)

    75347.3h 6.52% Nachrichten
    52746.4h 4.57% Verkaufsshow
    48165.4h 4.17% Krimiserie
    42525.0h 3.68% Werbesendung
    36024.8h 3.12% Dokureihe
    34382.2h 2.98% Dokusoap
    33793.2h 2.93% Regionalmagazin
    30366.2h 2.63% Dokumentation
    27242.3h 2.36% *unknown*
    21630.7h 1.87% Zeichentrickserie
    21327.2h 1.85% Infomercial
    20636.5h 1.79% Animationsserie
    16507.5h 1.43% Comedyserie
    16154.3h 1.40% Morgenmagazin
    15384.2h 1.33% Religionsmagazin
    15308.1h 1.33% Talkshow
    14400.4h 1.25% Magazin
    11413.2h 0.99% E-Sport
    11153.3h 0.97% Sitcom
    10431.4h 0.90% Wetterbericht
    10209.5h 0.88% Quiz
    10204.6h 0.88% Programmende
    10130.0h 0.88% Komödie
    8859.1h  0.77% Realityshow
    8770.3h  0.76% Politikmagazin
    8679.7h  0.75% Wissensmagazin
    8587.4h  0.74% Börsenmagazin
    7723.8h  0.67% Wirtschaftsmagazin
    7631.7h  0.66% Telenovela
    7604.5h  0.66% Dramaserie
