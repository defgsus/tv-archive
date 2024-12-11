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

**109** channels, **1,178,849.9** hours playtime between **2023-01-17** and **2024-12-12**


### playtime per genre (top 30)

    77093.6h 6.54% Nachrichten
    53638.8h 4.55% Verkaufsshow
    49185.8h 4.17% Krimiserie
    43498.2h 3.69% Werbesendung
    36714.6h 3.11% Dokureihe
    34945.4h 2.96% Dokusoap
    34523.8h 2.93% Regionalmagazin
    31075.7h 2.64% Dokumentation
    27813.5h 2.36% *unknown*
    22098.0h 1.87% Zeichentrickserie
    21817.3h 1.85% Infomercial
    21078.0h 1.79% Animationsserie
    16762.0h 1.42% Comedyserie
    16529.2h 1.40% Morgenmagazin
    15636.4h 1.33% Talkshow
    15599.1h 1.32% Religionsmagazin
    14572.0h 1.24% Magazin
    11652.5h 0.99% E-Sport
    11358.1h 0.96% Sitcom
    10658.4h 0.90% Wetterbericht
    10438.7h 0.89% Quiz
    10399.5h 0.88% Programmende
    10384.2h 0.88% Komödie
    9094.2h  0.77% Realityshow
    9002.0h  0.76% Politikmagazin
    8833.7h  0.75% Wissensmagazin
    8670.6h  0.74% Börsenmagazin
    7878.5h  0.67% Wirtschaftsmagazin
    7824.1h  0.66% Telenovela
    7810.8h  0.66% Dramaserie
