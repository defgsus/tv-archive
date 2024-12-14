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

**109** channels, **1,182,349.0** hours playtime between **2023-01-17** and **2024-12-15**


### playtime per genre (top 30)

    77318.9h 6.54% Nachrichten
    53792.4h 4.55% Verkaufsshow
    49320.6h 4.17% Krimiserie
    43633.1h 3.69% Werbesendung
    36810.4h 3.11% Dokureihe
    35013.6h 2.96% Dokusoap
    34608.4h 2.93% Regionalmagazin
    31204.9h 2.64% Dokumentation
    27911.3h 2.36% *unknown*
    22167.9h 1.87% Zeichentrickserie
    21889.5h 1.85% Infomercial
    21145.3h 1.79% Animationsserie
    16792.1h 1.42% Comedyserie
    16571.1h 1.40% Morgenmagazin
    15692.8h 1.33% Talkshow
    15627.9h 1.32% Religionsmagazin
    14595.0h 1.23% Magazin
    11694.5h 0.99% E-Sport
    11389.6h 0.96% Sitcom
    10690.7h 0.90% Wetterbericht
    10466.3h 0.89% Quiz
    10427.1h 0.88% Komödie
    10426.8h 0.88% Programmende
    9117.7h  0.77% Realityshow
    9014.4h  0.76% Politikmagazin
    8851.8h  0.75% Wissensmagazin
    8679.7h  0.73% Börsenmagazin
    7895.3h  0.67% Wirtschaftsmagazin
    7843.2h  0.66% Telenovela
    7834.9h  0.66% Dramaserie
