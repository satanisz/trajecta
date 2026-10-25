# Laboratorium i plan eksperymentów

## Działający punkt odniesienia

Uruchom z katalogu głównego, używając Pythona 3.10 lub nowszego:

```powershell
python -m unittest discover -s tests -v
python -m experiments.synthetic_ctmc --seed 42
```

Nie są wymagane biblioteki zewnętrzne. Eksperyment generuje 2000 trajektorii treningowych i 500 testowych, każdą z horyzontem 5 jednostek czasu. Niezależne strumienie RNG mają ziarna `seed` i `seed+1`; stany początkowe przechodzą cyklicznie przez trzy stany. Generator prawdziwy:

```text
[-1.0,  0.8,  0.2]
[ 0.3, -0.8,  0.5]
[ 0.4,  0.1, -0.5]
```

Estymator korzysta wyłącznie z trajektorii treningowych. Ocenę log-wiarygodności wykonuje na osobnym zbiorze, a rozkład końcowy porównuje dla startu w stanie 0. Wynik trafia do ignorowanego `outputs/synthetic_ctmc.json`. Parametry `--train-size`, `--test-size`, `--seed` i `--output` pozwalają zmienić konfigurację.

Przebieg kontrolny z 2026-10-25 (Python 3.14.4, seed 42):

| Metryka | Wynik |
| --- | ---: |
| MAE sześciu intensywności poza przekątną | 0.009867 |
| NLL / trajektorię testową — prawdziwy generator | 6.711172 |
| NLL / trajektorię testową — dopasowany MLE | 6.709500 |
| NLL / trajektorię testową — intensywność 1 na każdej krawędzi | 10.000000 |
| L1 między rozkładami końcowymi | 0.021864 |
| Błąd sumy prawdopodobieństw dopasowanego modelu | 2.29e-14 |
| Raportowana granica obcięcia szeregu (maksimum obu propagacji) | 3.26e-13 |

MLE może w pojedynczej skończonej próbce testowej uzyskać nieco niższą NLL niż generator prawdziwy. Ten wynik nie dowodzi przewagi nad modelem generującym dane. Jest kontrolą poprawności prostego przykładu, a nie wynikiem benchmarku.

Dziesięć testów obejmuje rozwiązanie analityczne dla dwóch stanów, stany absorbujące, masę szeregu z resztą, końcowy czas bez skoku, nieobserwowane wiersze, niemożliwe skoki, błędne dane, zgodność symulacji z Master Equation, odzyskanie intensywności i kolejność okresów. Progi testów Monte Carlo dotyczą ustalonych przykładów; nie są kryteriami akceptacji foundation modelu.

## Proponowane etapy

Poniższe zadania nie są jeszcze zaimplementowane.

| Etap | Pytanie | Dane i porównania | Warunek przejścia |
| --- | --- | --- | --- |
| 1. Wiele grafów syntetycznych | Czy poprawność utrzymuje się przy innej topologii i skali czasu? | Łańcuchy, cykle, rozgałęzienia, absorpcja; MLE, stałe intensywności, generator prawdziwy | Zgodność numeryczna oraz raport błędów po topologii, rozmiarze i ekspozycji |
| 2. Uczona głowica Q | Czy współdzielenie parametrów pomaga przy małej liczbie trajektorii? | Znane stany; model bez enkodera, prosty enkoder cech, bogatsza historia | Lepsza NLL poza próbą przy zgodnych ograniczeniach Q; ablacją oddzielony wpływ historii |
| 3. Nowe grafy i słowniki | Czy model przenosi się na nieznane systemy? | Rozłączne systemy, permutacje ID, inna liczba stanów; MiNT jako inspiracja protokołu | Wyniki bez wspólnych encji i bez przecieku; krzywe jakości względem ilości adaptacji |
| 4. Częściowa obserwacja | Czy można odzyskać dynamikę z braków i szumu? | Kontrolowane próbkowanie i emisje; jawny model obserwacji | Kalibracja niepewności i diagnoza nieidentyfikowalnych przypadków |
| 5. TTA / period folding | Czy atrybucja ścieżek zachowuje wynik i kontroluje resztę? | Małe grafy z niezależnym rozwiązaniem, cykle i zmiany okresów | Zgodność sumy wkładów i reszty, jawny koszt obliczeń |
| 6. Jedna domena rzeczywista | Czy semantyka CTMC odpowiada obserwowanym zdarzeniom? | Najpierw jeden log procesowy; osobno adapter gospodarczy | Porównanie z prostymi modelami domenowymi i ocena błędów danych |

## Protokół porównywania

1. Dziel dane po systemach/grafach oraz czasie. Historie jednego obiektu nie mogą przeciekać między zbiorami przez współdzielone okna. Dla handlu używaj daty udostępnienia danych (`available_at`), nie tylko okresu, którego dane dotyczą.
2. Zamroź konfiguracje i zbiory przed testem; dostrajaj na walidacji. Raportuj co najmniej pięć ziaren wraz ze średnią, rozrzutem i przedziałami niepewności. Jednostką resamplingu powinien być niezależny system lub trajektoria, zależnie od eksperymentu.
3. Zawsze porównuj z modelem stałym, MLE dla znanych stanów oraz wariantem bez historii. Dla nowcastingu dodaj sezonowy naiwny model i prosty model regresyjny. Koszt uczenia, pamięć i czas inferencji są częścią porównania.
4. Raportuj NLL, MAE intensywności tam, gdzie znane jest Q, błąd rozkładu końcowego, kalibrację, masę i granicę obcięcia. W nowcastingu dodaj metryki wolumenów we właściwych jednostkach; nie porównuj ich bezpośrednio z błędem prawdopodobieństwa.
5. Sprawdź ablacją tokenizację, historię, cechy grafu, priory, maskę przejść oraz podział intensywność/wybór celu. Nie nazywaj generalizacją wyników na tym samym grafie przy nowym seedzie.

Przed deklaracją nowości trzeba porównać konkretny algorytm z metodami z bibliografii. Obecne repozytorium przygotowuje warunki takiego badania.
