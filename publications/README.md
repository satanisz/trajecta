# Biblioteka publikacji

[Bibliografia z opisami](BIBLIOGRAPHY.md) obejmuje 49 odrębnych publikacji wskazanych w czacie **„Pragma i Master Equation”**. Przejrzano wszystkie siedem wymian rozmowy, nazwy prac i odnośniki; powtórzenia scalono. Firmy, projekty i serwisy danych są opisane oddzielnie w [mapie źródeł danych](../docs/data-sources.md). Pełna treść prywatnej rozmowy nie jest częścią repozytorium.

Stan na 2026-10-25: **39 PDF-ów, dwie książki w tekstowej postaci HTML i osiem braków pełnego tekstu**. Braki wraz z przyczynami są na początku bibliografii. Nie zastępujemy pełnych publikacji abstraktami, spisami treści ani stronami z CAPTCHA.

## Układ i odtwarzanie

`catalog.json` jest źródłem metadanych, krótkich opisów, adresów pobierania i datowanego stanu lokalnego. Podkatalogi `files/` odpowiadają czterem grupom:

- `markov-and-master-equation/` — procesy skokowe, Master Equation, trajektorie;
- `process-and-temporal-models/` — grafy czasowe i modele zdarzeń;
- `economics-and-applications/` — sieci produkcyjne, handel i szoki;
- `books/` — książki, w tym dwie wersje HTML w osobnych katalogach.

Z katalogu głównego repozytorium:

```powershell
python scripts/download_publications.py --list
python scripts/download_publications.py
python scripts/download_web_books.py
```

Wybrany materiał można pobrać przez `--id neural-mjp`. Niektóre serwery nie współpracowały z klientem `urllib`; na tym komputerze pomógł systemowy `curl`:

```powershell
python scripts/download_publications.py --id imf-space --system-client
```

Opcja wymaga `curl` w PATH. Weryfikacja TLS pozostaje włączona. Skrypt PDF sprawdza sygnaturę i znacznik końca dokumentu, pomija istniejące poprawne pliki i zapisuje wynik każdej próby w ignorowanym `local/download-report.json`. Kończy się kodem 0 również przy brakach dostępu: sprawdź statusy w raporcie. Książki HTML pobiera drugi skrypt; brak PDF dla tych dwóch pozycji jest oczekiwany.

Wersje HTML zawierają zapis tekstów, lokalny indeks i manifest adresów/hashów. Nie są kompletną kopią stron do pracy offline: style, ilustracje, interakcje i część odnośników mogą potrzebować sieci. Skrypt ponownie pobiera aktualne strony i nadpisuje lokalny zapis książek.

Po zmianie katalogu odtwórz opis:

```powershell
python scripts/render_bibliography.py
```

Pole `snapshot` dokumentuje konkretny audyt, a nie bieżący stan każdego klona. Ponowne pobranie może zwrócić inną rewizję. Do porównań służą zapisane SHA-256. Przy nowym audycie aktualizuj metadane, status, datę i hashe łącznie.

## Zakres weryfikacji

Wszystkie 39 pobranych PDF-ów odczytano parserem PDF; sprawdzono liczbę stron oraz tożsamość tekstu na stronach początkowych. Nie przeprowadzono recenzji metod, replikacji eksperymentów ani pełnego przeglądu systematycznego.

| Status metadanych | Znaczenie |
| --- | --- |
| `fulltext_title_verified` | PDF odczytany, tożsamość tytułu i rodzaj wersji sprawdzone |
| `metadata_verified` | Potwierdzono tożsamość bibliograficzną; brak pełnego tekstu lokalnie |
| `landing_page_verified` | Sprawdzono stronę publikacji/książki; szczegóły ograniczeń w uwagach |

W rozmowie wystąpiły rozbieżności, które zachowano jawnie:

- Etykieta „GFlowNets — Trajectory Balance” prowadziła do **Towards Understanding and Improving GFlowNet Training** (2023). Katalog zawiera zarówno rzeczywiście podlinkowaną pracę, jak i odrębne **Trajectory balance** (2022).
- Rekord TIDES potwierdzono na stronie projektu, lecz nie rozstrzygnięto rozbieżności między opisem ICML a warsztatem GFM przy ICML. PDF OpenReview był zablokowany.
- Odnośnik do Miller–Blair prowadził do spisu treści. Zastąpiono go rekordem całej książki, zachowując informację o braku pełnego tekstu.
- Kopie autorskie, preprinty, aktualizowana książka *What If* oraz artykuły „in press” są oznaczone przy odpowiednich pozycjach. Rok publikacji nie musi być datą pobranej rewizji.
- TTA w kontekście pracy Stanisza, Oettingena i Cetnara oznacza **Transmutation Trajectory Analysis**. Dołączony kod uniformizacji CTMC nie jest implementacją TTA.

## Git i prawa do materiałów

Całe `publications/files/`, z wyjątkiem pustych plików `.gitkeep`, jest ignorowane. Dodatkowo ignorowane są PDF/EPUB/MOBI w całym repozytorium oraz katalogi `local/`, `data/` i `outputs/`. Git przechowuje katalog, opisy i skrypty. Prawa i warunki użycia poszczególnych publikacji pozostają po stronie ich autorów i wydawców; dostęp publiczny nie oznacza dowolnego prawa do redystrybucji.
