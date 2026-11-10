# Metin2 Singleplayer - traducciones de la comunidad

[English](README.md) | [Polski](README_PL.md) | [Türkçe](README_TR.md) | [Deutsch](README_DE.md) | [Français](README_FR.md) | **Español** | [Italiano](README_IT.md) | [Português](README_PT.md) | [Română](README_RO.md) | [Magyar](README_HU.md) | [Nederlands](README_NL.md) | [Čeština](README_CS.md) | [Dansk](README_DA.md) | [Ελληνικά](README_EL.md) | [Русский](README_RU.md) | [العربية](README_AR.md) | [한국어](README_KO.md)

Este repositorio contiene los textos de **Metin2 Singleplayer** - el cliente
del juego, los nombres de objetos y monstruos, los mensajes del servidor, las
misiones, el chat de los bots, el lanzador de Windows y el panel web clásico - para que los
jugadores puedan traducir el juego a su propio idioma. Solo contiene
traducciones: nada de código del juego.

Cada pull request se comprueba automáticamente, y las traducciones aceptadas
entran en el juego en las versiones siguientes.

## Qué hay aquí

| carpeta | contenido |
|---|---|
| `template/` | todos los textos del juego, con la columna `translation` vacía. El punto de partida de un idioma nuevo. |
| `de/` `fr/` `pt/` `ro/` `tr/` | los idiomas que el juego ya tiene, con su traducción actual: corrígela y completa lo que falte (filas con `status` `new`). |
| `hu/` `es/` `it/` `cs/` `nl/` `da/` `el/` `ru/` `ar/` `ko/` | idiomas nuevos, traducidos por completo con ayuda de IA: hablantes nativos, corregid lo que suene mal. |
| `en_US/` | inglés estadounidense: el texto fuente en inglés (ortografía británica) con ortografía de EE. UU. (color, armor, defense...). |
| `tools/validate.py` | la comprobación por la que pasa cada pull request. |

El inglés es el original y el polaco se muestra al lado como referencia;
ninguno de los dos tiene carpeta propia.

Cada carpeta de idioma tiene los mismos archivos CSV, divididos en partes para
que GitHub pueda mostrarlos y editarlos (como máximo 700 filas por archivo):

| archivos | contenido |
|---|---|
| `1_klient_NN.csv` | el cliente: ventanas, botones, descripciones emergentes, habilidades, reglas |
| `2_przedmioty_potwory_NN.csv` | nombres de objetos y monstruos, descripciones de objetos |
| `3_gra_serwer_NN.csv` | los mensajes propios del servidor (chat, líneas del sistema) |
| `4_questy_NN.csv` | los diálogos de las misiones |
| `5_boty_czat_NN.csv` | el chat de los bots, la charla de los monstruos, las frases del servidor |
| `6_launcher_NN.csv` | el lanzador de Windows |
| `7_panel_NN.csv` | el panel web clásico (el panel de administración en el puerto 7788, en el navegador) |

Cada archivo tiene las columnas:

| columna | |
|---|---|
| `id` | la clave de la fila. **No la cambies nunca.** |
| `english` | el texto que hay que traducir. **No lo cambies nunca.** |
| `polski` | el mismo texto en polaco, como referencia (puede estar vacío). |
| `translation` | **tu traducción - la única columna que editas.** Vacía = el juego muestra el inglés. |
| `notes` | dónde se ve el texto, qué hay que conservar, un límite de longitud. |
| `status` | `new` (sin traducir), `done` (traducido), `check` (igual que el inglés - revísalo). Puedes ponerlo en `done`. |

## Cómo traducir

### A. En el navegador (cambios pequeños)

1. Abre el archivo, p. ej. [`es/1_klient_01.csv`](es/1_klient_01.csv).
   GitHub lo muestra como una tabla; usa el cuadro de búsqueda de arriba para
   encontrar una fila.
2. Haz clic en el lápiz (**Edit this file**). La primera vez, GitHub crea una
   copia (un fork) para ti.
3. Cambia solo la columna `translation` de las filas que quieras. Un texto con
   una coma, unas comillas o un salto de línea va entre comillas dobles
   (`"así, por ejemplo"`); unas comillas dentro se escriben dos veces (`""`).
4. Haz clic en **Commit changes...**, luego en **Propose changes** y luego en
   **Create pull request**. Di en una frase qué has traducido.

### B. En una hoja de cálculo (muchas filas)

1. Descarga los archivos (abre un archivo, **Download raw file**; o el botón
   verde **Code**, **Download ZIP**, para todo).
2. Ábrelos en una hoja de cálculo:
   - **Google Sheets**: Archivo > Importar > Subir. Funciona sin ajustes.
   - **LibreOffice Calc**: abre el archivo; elige el juego de caracteres
     **UTF-8**, el separador **coma** y pon las columnas como **Texto**.
   - **Excel**: no hagas doble clic en el archivo (Excel leería mal las
     letras). Usa Datos > Desde el texto/CSV, origen del archivo **65001:
     Unicode (UTF-8)**, delimitador **Coma**. Guarda como **CSV UTF-8
     (delimitado por comas)**.
3. Rellena la columna `translation`. No cambies el nombre de los archivos, no
   añadas ni quites columnas y no cambies `id` ni `english`. Ordenar y
   filtrar no es problema.
4. Guarda como CSV (UTF-8, separado por comas) con el mismo nombre.
5. En GitHub abre la carpeta del idioma, **Add file > Upload files**, suelta
   tus archivos y luego **Propose changes** y **Create pull request**.

No hace falta traducirlo todo de una vez - envía lo que tengas.

## Reglas

1. **Solo la columna `translation`.** `id` y `english` se quedan como están;
   la comprobación rechaza un archivo en el que se hayan cambiado.
2. **Conserva cada variable y cada código exactamente como en el inglés, en
   el mismo orden** - el juego los rellena:
   - variables printf: `%s` `%d` `%u` `%ld` `%.1f` `%5d` ... y `%%` (un signo de porcentaje);
   - marcadores: `{0}` `{#0}` `{name}` `{skrot}` ...;
   - `[ENTER]` es un salto de línea en una ventana de misión; `[WAIT]`,
     `[DELAY value;5]`, `[COLOR r;1|g;0|b;0]` son sus órdenes;
   - colores `|cffff0000` ... `|r`, enlaces `|H` ... `|h`, `|E` ... `|e`.

   Puedes moverlos dentro de la frase según lo necesite tu idioma, pero las
   variables del tipo `%` deben mantener el mismo orden. Un texto entre
   corchetes como `[Guild]` o `[PT]` es texto normal: tradúcelo.
3. **Letras.** El juego dibuja cada idioma en una página de códigos de
   Windows, así que solo se pueden mostrar sus letras - nada de emoji ni de
   símbolos como `→` o `✓`:

   | página de códigos | idiomas | letras |
   |---|---|---|
   | 1250 | pl, cs, sk, hu, ro, hr, sl, sr (latino), bs, sq | ą ć ę ł ń ó ś ź ż, á č ď é ě í ň ř š ť ú ů ý ž, ő ű, ă â î ş ţ |
   | 1251 | ru, uk, bg, be, mk, sr (cirílico) | а б в г д ... я, є і ї ґ, ў, ђ ј љ њ ћ џ |
   | 1252 | de, fr, es, it, pt, nl, da, sv, no, fi, ca, id ... | à á â ã ä å æ ç è é ê ë ì í î ï ñ ò ó ô õ ö ø ù ú û ü ß œ |
   | 1253 | el | α β γ δ ... ω, ά έ ή ί ό ύ ώ |
   | 1254 | tr, az | ç ğ ı İ ö ş ü, â î û |
   | 1257 | lt, lv, et | ā č ē ģ ī ķ ļ ņ š ū ž, ą ę ė į ų |

   Rumano: la página de códigos solo tiene **ş ţ con cedilla**, no ș ț con
   coma. El lanzador (`6_launcher_*`) es un programa de Windows aparte y
   admite cualquier letra. También el panel web (`7_panel_*`), una página en el
   navegador: ambos son **UTF-8**, cualquier letra de cualquier idioma.
4. **El chat de los bots** (filas cuyas notas dicen "ASCII letters only"):
   los bots escriben como jugadores, con letras simples a-z sin acentos.
5. **Longitud.** Donde las notas dicen "max N characters", el juego no tiene
   sitio para más.
6. **Saltos de línea** solo donde los tiene el inglés o las notas dicen "new
   lines allowed".
7. **El panel web** (`7_panel_*`): sus textos van a una página web, así que
   conserva las etiquetas HTML del inglés exactamente como están (`<b>`, `</b>`,
   `<a href="...">`, `<br>` y los marcadores del tipo `<number>` entre ángulos)
   y no añadas ningún `<`, `>` ni `javascript:` propio. Sus variables son `%s`,
   `%d`, `%(name)s` y `{name}`; un `%(name)s` con nombre puede moverse. Un `%`
   seguido de un espacio (`25% a character`) es un signo de porcentaje. Un
   idioma con al menos un texto del panel traducido aparece en el selector de
   idioma del panel; lo que no está traducido se muestra en inglés.

## Un idioma nuevo

1. Copia toda la carpeta `template/` en una carpeta con el código ISO 639-1
   de dos letras de tu idioma (`hu`, `es`, `cs`, `pl`... - mira
   [la lista](https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes)).
   Puedes hacerlo en una hoja de cálculo: descarga `template/`, traduce y sube
   los archivos a la carpeta nueva (**Add file > Upload files**, escribe `xx/`
   delante del nombre para crear la carpeta).
2. Traduce y abre una pull request.

Un idioma nuevo necesita algo de trabajo en el juego antes de que los
jugadores puedan elegirlo (los idiomas fuera de la página de códigos 1250
necesitan además un cliente nuevo), así que puede llegar unas versiones
después de la primera traducción.

## La comprobación

Cada pull request ejecuta `tools/validate.py` (GitHub Actions). Señala, en la
fila donde lo encontró:

- un `id` que no está en `template/`, o que aparece dos veces;
- una columna `english` cambiada;
- variables, marcadores, etiquetas o códigos de color distintos de los del
  inglés;
- en la hoja del panel web, otras etiquetas HTML que las del inglés, o un
  `<`, `>` o `javascript:` propio;
- una letra fuera de la página de códigos del idioma, un tabulador, un
  carácter de control, un salto de línea donde no se permite, un texto
  demasiado largo.

Solo se juzgan las filas que ha cambiado tu pull request; los problemas que ya
estaban en los archivos se cuentan, pero no se te atribuyen. Para ejecutarla
tú mismo (Python 3, nada que instalar): `python tools/validate.py es`.

## Licencia

Al abrir una pull request aceptas que tu traducción se use en Metin2
Singleplayer y se comparta en las mismas condiciones que el proyecto:
[CC BY-NC-ND 4.0](LICENSE). Los colaboradores aparecen en los créditos del
proyecto. Metin2 y sus textos originales pertenecen a Ymir Interactive y
Webzen.
