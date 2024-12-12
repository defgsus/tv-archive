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

**109** channels, **1,180,567.9** hours playtime between **2023-01-17** and **2024-12-13**


### playtime per genre (top 30)

    77229.3h 6.54% Nachrichten
    53700.8h 4.55% Verkaufsshow
    49274.5h 4.17% Krimiserie
    43567.6h 3.69% Werbesendung
    36762.9h 3.11% Dokureihe
    34993.6h 2.96% Dokusoap
    34578.2h 2.93% Regionalmagazin
    31125.8h 2.64% Dokumentation
    27843.1h 2.36% *unknown*
    22129.5h 1.87% Zeichentrickserie
    21854.7h 1.85% Infomercial
    21109.8h 1.79% Animationsserie
    16777.6h 1.42% Comedyserie
    16563.1h 1.40% Morgenmagazin
    15660.8h 1.33% Talkshow
    15608.5h 1.32% Religionsmagazin
    14580.9h 1.24% Magazin
    11673.5h 0.99% E-Sport
    11369.6h 0.96% Sitcom
    10675.9h 0.90% Wetterbericht
    10463.5h 0.89% Quiz
    10413.2h 0.88% Programmende
    10392.1h 0.88% Komödie
    9115.6h  0.77% Realityshow
    9019.9h  0.76% Politikmagazin
    8847.3h  0.75% Wissensmagazin
    8679.4h  0.74% Börsenmagazin
    7894.7h  0.67% Wirtschaftsmagazin
    7842.6h  0.66% Telenovela
    7839.3h  0.66% Dramaserie
