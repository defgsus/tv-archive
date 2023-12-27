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

**97** channels, **618,825.8** hours playtime between **2023-01-17** and **2023-12-28**


### playtime per genre (top 30)

    40495.0h 6.54% Nachrichten
    29666.8h 4.79% Verkaufsshow
    24839.0h 4.01% Krimiserie
    21026.2h 3.40% Werbesendung
    20095.3h 3.25% Dokureihe
    18494.4h 2.99% Dokusoap
    17834.9h 2.88% Regionalmagazin
    15982.4h 2.58% Dokumentation
    15250.6h 2.46% *unknown*
    11407.0h 1.84% Zeichentrickserie
    11239.4h 1.82% Infomercial
    10896.5h 1.76% Animationsserie
    9426.0h  1.52% Comedyserie
    8772.4h  1.42% Morgenmagazin
    8384.6h  1.35% Religionsmagazin
    8226.5h  1.33% Talkshow
    8053.9h  1.30% Magazin
    6081.8h  0.98% E-Sport
    6075.7h  0.98% Programmende
    6011.3h  0.97% Sitcom
    5649.4h  0.91% Wetterbericht
    5557.4h  0.90% Börsenmagazin
    5091.5h  0.82% Quiz
    5089.6h  0.82% Komödie
    4688.4h  0.76% Wissensmagazin
    4586.2h  0.74% Wirtschaftsmagazin
    4470.4h  0.72% Realityshow
    4460.6h  0.72% Musikmagazin
    4458.2h  0.72% Telenovela
    4380.3h  0.71% Politikmagazin
