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

**97** channels, **634,763.7** hours playtime between **2023-01-17** and **2024-01-06**


### playtime per genre (top 30)

    41443.2h 6.53% Nachrichten
    30365.5h 4.78% Verkaufsshow
    25419.8h 4.00% Krimiserie
    21569.1h 3.40% Werbesendung
    20609.4h 3.25% Dokureihe
    18968.5h 2.99% Dokusoap
    18241.9h 2.87% Regionalmagazin
    16492.6h 2.60% Dokumentation
    15760.6h 2.48% *unknown*
    11709.0h 1.84% Zeichentrickserie
    11508.9h 1.81% Infomercial
    11158.1h 1.76% Animationsserie
    9645.6h  1.52% Comedyserie
    8991.5h  1.42% Morgenmagazin
    8585.7h  1.35% Religionsmagazin
    8371.9h  1.32% Talkshow
    8314.1h  1.31% Magazin
    6253.6h  0.99% E-Sport
    6199.6h  0.98% Programmende
    6162.1h  0.97% Sitcom
    5778.8h  0.91% Wetterbericht
    5677.8h  0.89% Börsenmagazin
    5382.2h  0.85% Komödie
    5221.5h  0.82% Quiz
    4774.8h  0.75% Wissensmagazin
    4671.8h  0.74% Wirtschaftsmagazin
    4610.3h  0.73% Realityshow
    4552.5h  0.72% Musikmagazin
    4529.2h  0.71% Telenovela
    4466.5h  0.70% Politikmagazin
