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

**96** channels, **53,711.2** hours playtime between **2023-01-17** and **2023-02-15**


### playtime per genre (top 30)

    3743.8h 6.97% Nachrichten
    2778.1h 5.17% Verkaufsshow
    2276.2h 4.24% Krimiserie
    1857.1h 3.46% Dokusoap
    1808.8h 3.37% Werbesendung
    1606.3h 2.99% Dokureihe
    1506.0h 2.80% Regionalmagazin
    1364.7h 2.54% Dokumentation
    1353.0h 2.52% *unknown*
    1027.5h 1.91% Zeichentrickserie
    992.9h  1.85% Infomercial
    980.0h  1.82% Animationsserie
    894.0h  1.66% Comedyserie
    756.4h  1.41% Morgenmagazin
    707.7h  1.32% Talkshow
    700.9h  1.30% Religionsmagazin
    697.2h  1.30% Programmende
    601.1h  1.12% Magazin
    563.4h  1.05% E-Sport
    496.8h  0.92% Sitcom
    476.5h  0.89% Börsenmagazin
    466.9h  0.87% Wetterbericht
    446.4h  0.83% Wirtschaftsmagazin
    421.5h  0.78% Wissensmagazin
    413.7h  0.77% Quiz
    399.8h  0.74% Musikmagazin
    399.6h  0.74% Dramaserie
    384.1h  0.72% Telenovela
    378.6h  0.70% Gesundheitsmagazin
    349.0h  0.65% Gerichtsshow
