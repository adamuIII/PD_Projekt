# PD_Projekt
Aplikacja desktopowa do zarządzania sklepem z grami komputerowymi

# **Wymagania funkcjonalne:**
-Rejestracja użytkowników i logowanie do aplikacji.  
-Dodawanie, przeglądanie, edycja i usuwanie gier w sklepie.  
-Przeglądanie listy gier oraz sortowanie po kategoriach, cenach i ocenach.  
-Dodawanie gier do koszyka i składanie zamówień.  
-Przeglądanie historii zamówień i statusu zamówienia.  
-Możliwość dodawania recenzji i oceny dla gier.  
-Wyszukiwanie gier po nazwie lub opisie.  
# **Wymagania niefunkcjonalne:**
-Aplikacja powinna być dostępna na systemach operacyjnych Windows, Linux i macOS.  
-Aplikacja powinna działać w przeglądarkach internetowych Google Chrome, Mozilla Firefox, Microsoft Edge i Safari.  
-Interfejs graficzny powinien być intuicyjny i responsywny.  
-Wszystkie zapytania HTTP powinny być obsługiwane przez odpowiednie klasy programu i korzystać z biblioteki do obsługi formatu JSON.  
-Aplikacja powinna być zabezpieczona przed popularnymi atakami, takimi jak SQL Injection, Cross-Site Scripting (XSS) i podobnymi.  
-Wszystkie operacje związane z użytkownikami będą przeprowadzane przy użyciu mechanizmów autoryzacji i uwierzytelnienia z wykorzystaniem F2A oparty na algorytmie TOTP, a dane będą przechowywane w bezpieczny sposób.  
-Kod aplikacji powinien być pokryty testami jednostkowymi na poziomie minimum 75%.  
-Kod aplikacji musi być poddany analizie statycznej przy użyciu oprogramowania SonarQube lub innego narzędzia, w celu zapewnienia jakości, czytelności i zgodności z najlepszymi praktykami programistycznymi.  
-Aplikacja powinna obsługiwać duże ilości użytkowników i działać stabilnie nawet przy dużym obciążeniu.  
-Dokumentacja techniczna i użytkownika powinna być dostępna i łatwo zrozumiała.  

# Obsługa projektu

- Po pobraniu projektu, należy zainstalować wszystkie wymagane biblioteki za pomocą pip install -r requirements.txt
- Następnie, w głównym folderze z projektem należy wykonać komendę python manage.py makemigrations, następnie python manage.py migrate
- Projekt powinien być gotowy do uruchomienia. Do uruchomienia należy wykorzystać komendę python manage.py runserver, strona www dostępna będzie pod adresem 127.0.0.1:8000

Panel administratora dostępny jest pod linkiem /admin, dostępny jedynie z maszyny lokalnej. 

# Dokumentacja API

Po uruchomieniu projektu API dostepne jest pod adresem 127.0.0.1:8000/api

Z API można korzystać przy użyciu Postmana, lub przy użyciu wbudowanego narzędzia w Django REST Framework (wystarczy wbić link do APi w przeglądarke)

UWAGA przy korzystaniu z API przy użyciu Postmana, nie można korzystać z autentykacji przez logowanie - trzeba wygenerować token JWT
Generowanie tokenu przebiega w następujący sposób:
1. Należy wejść pod adres 127.0.0.1:8000/api/token/
2. Należy podać dane do logowania w okienku pod body request
3. Wygenerowana zostanie para kluczy, w postmanie należy podawać klucz ACCESS (trzeba go podać w zakładce authorization > bearer token) UWAGA KOD WAŻNY TYLKO 5 MINUT

Dostępne API dla niezalogowanego:
- GET /api/games/
- GET /api/developers/
- GET /api/categories/

API dostępne po zalogowaniu / posiadaniu klucza JWT:
- POST /api/admin/developers #do dodania developera
- POST /api/admin/categories #do dodania kategorii

- GET/PUT/DELETE /api/admin/developers/<ID_DEWELOPERA> #do otrzymania informacji o danym deweloperze, modyfikacji lub usunięca (MA WPŁYW NA BAZĘ TAK)
- GET/PUT/DELETE /api/admin/categories/<ID_KATEGORII> #do otrzymania informacji o danej kategorii, modyfikacji lub usunięca (MA WPŁYW NA BAZĘ TAK)

API związane z kluczami JWT:
- POST api/token/ JAKO PAYLOAD DANE DO LOGOWANIA
- POST api/token/refresh JAKO PAYLOAD TOKEN REFRESH DLA WASZEGO TOKENU
- POST api/token/verify JAKO PAYLOAD WASZ TOKEN ACCESS, SŁUŻY DO SPRAWDZANIA TOKENU

# Aby uruchomić LiveTesty Selenium w Chrome należy:
dodać w sytemowych PATH ścieżke do chromedriver.exe - można to zrobić za pomocą CMD: setx PATH "%PATH%;waszaSciezkaDoPlikuExe"
np. setx PATH "%PATH%;C:\Users\Kowalski\Desktop\PD_Projekt\chromedriver.exe"
a następnie za pomocą komendy w terminalu: "python manage.py test" - rozpoczyna się proces testowania (Należy mieć odpalony projekt przed wystartowaniem testów)

