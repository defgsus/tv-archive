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

**97** channels, **629,458.3** hours playtime between **2023-01-17** and **2024-01-03**


### playtime per genre (top 30)

    41067.7h 6.52% Nachrichten
    30107.0h 4.78% Verkaufsshow
    25163.2h 4.00% Krimiserie
    21385.8h 3.40% Werbesendung
    20451.5h 3.25% Dokureihe
    18831.5h 2.99% Dokusoap
    18069.3h 2.87% Regionalmagazin
    16358.9h 2.60% Dokumentation
    15615.5h 2.48% *unknown*
    11604.6h 1.84% Zeichentrickserie
    11409.9h 1.81% Infomercial
    11072.5h 1.76% Animationsserie
    9563.9h  1.52% Comedyserie
    8889.7h  1.41% Morgenmagazin
    8525.4h  1.35% Religionsmagazin
    8318.7h  1.32% Talkshow
    8238.6h  1.31% Magazin
    6191.9h  0.98% E-Sport
    6156.9h  0.98% Programmende
    6112.8h  0.97% Sitcom
    5732.6h  0.91% Wetterbericht
    5626.4h  0.89% Börsenmagazin
    5338.1h  0.85% Komödie
    5149.2h  0.82% Quiz
    4740.0h  0.75% Wissensmagazin
    4632.0h  0.74% Wirtschaftsmagazin
    4570.1h  0.73% Realityshow
    4529.6h  0.72% Musikmagazin
    4487.3h  0.71% Telenovela
    4429.7h  0.70% Politikmagazin
