# Metin2 Singleplayer - traduções da comunidade

[English](README.md) | [Polski](README_PL.md) | [Türkçe](README_TR.md) | [Deutsch](README_DE.md) | [Français](README_FR.md) | [Español](README_ES.md) | [Italiano](README_IT.md) | **Português** | [Română](README_RO.md) | [Magyar](README_HU.md) | [Nederlands](README_NL.md) | [Čeština](README_CS.md) | [Dansk](README_DA.md) | [Ελληνικά](README_EL.md) | [Русский](README_RU.md) | [العربية](README_AR.md) | [한국어](README_KO.md)

Este repositório contém os textos do **Metin2 Singleplayer** - o cliente do
jogo, os nomes dos itens e dos monstros, as mensagens do servidor, as missões,
o chat dos bots, o launcher do Windows e o painel web clássico - para que os jogadores possam traduzir
o jogo para a sua própria língua. Contém apenas traduções: nenhum código do
jogo.

Cada pull request é verificado automaticamente, e as traduções aceites entram
no jogo nas versões seguintes.

## O que está aqui

| pasta | conteúdo |
|---|---|
| `template/` | todos os textos do jogo, com a coluna `translation` vazia. O ponto de partida de uma nova língua. |
| `de/` `fr/` `pt/` `ro/` `tr/` | as línguas que o jogo já tem, com a tradução atual: corrige-a e completa o que falta (linhas com `status` `new`). |
| `hu/` `es/` `it/` `cs/` `nl/` `da/` `el/` `ru/` `ar/` `ko/` | línguas novas, totalmente traduzidas com ajuda de IA: falantes nativos, corrijam o que soar mal. |
| `en_US/` | inglês americano: o texto de origem em inglês (ortografia britânica) em ortografia dos EUA (color, armor, defense...). |
| `tools/validate.py` | a verificação pela qual passa cada pull request. |

O inglês é a fonte e o polaco aparece ao lado como referência; nenhum dos dois
tem pasta própria.

Cada pasta de língua tem os mesmos ficheiros CSV, divididos em partes para que
o GitHub os possa mostrar e editar (no máximo 700 linhas por ficheiro):

| ficheiros | conteúdo |
|---|---|
| `1_klient_NN.csv` | o cliente: janelas, botões, dicas, habilidades, regras |
| `2_przedmioty_potwory_NN.csv` | nomes dos itens e dos monstros, descrições dos itens |
| `3_gra_serwer_NN.csv` | as mensagens próprias do servidor (chat, linhas do sistema) |
| `4_questy_NN.csv` | os diálogos das missões |
| `5_boty_czat_NN.csv` | o chat dos bots, a conversa dos monstros, as frases do servidor |
| `6_launcher_NN.csv` | o launcher do Windows |
| `7_panel_NN.csv` | o painel web clássico (o painel de administração na porta 7788, no navegador) |

Cada ficheiro tem as colunas:

| coluna | |
|---|---|
| `id` | a chave da linha. **Nunca a alteres.** |
| `english` | o texto a traduzir. **Nunca o alteres.** |
| `polski` | o mesmo texto em polaco, como referência (pode estar vazio). |
| `translation` | **a tua tradução - a única coluna que editas.** Vazia = o jogo mostra o inglês. |
| `notes` | onde o texto aparece, o que tem de ser mantido, um limite de comprimento. |
| `status` | `new` (não traduzido), `done` (traduzido), `check` (igual ao inglês - verifica-o). Podes mudá-lo para `done`. |

## Como traduzir

### A. No navegador (pequenas alterações)

1. Abre o ficheiro, p. ex. [`pt/1_klient_01.csv`](pt/1_klient_01.csv). O
   GitHub mostra-o como uma tabela; usa a caixa de pesquisa por cima para
   encontrar uma linha.
2. Clica no lápis (**Edit this file**). Da primeira vez, o GitHub cria uma
   cópia (um fork) para ti.
3. Altera apenas a coluna `translation` das linhas que quiseres. Um texto com
   uma vírgula, aspas ou uma quebra de linha fica entre aspas duplas
   (`"assim, por exemplo"`); aspas dentro dele escrevem-se duas vezes (`""`).
4. Clica em **Commit changes...**, depois em **Propose changes** e depois em
   **Create pull request**. Diz numa frase o que traduziste.

### B. Numa folha de cálculo (muitas linhas)

1. Descarrega os ficheiros (abre um ficheiro, **Download raw file**; ou o
   botão verde **Code**, **Download ZIP**, para tudo).
2. Abre-os numa folha de cálculo:
   - **Google Sheets**: Ficheiro > Importar > Carregar. Funciona sem
     configurações.
   - **LibreOffice Calc**: abre o ficheiro; escolhe o conjunto de caracteres
     **UTF-8**, o separador **vírgula** e define as colunas como **Texto**.
   - **Excel**: não faças duplo clique no ficheiro (o Excel leria mal as
     letras). Usa Dados > De Texto/CSV, origem do ficheiro **65001: Unicode
     (UTF-8)**, delimitador **Vírgula**. Guarda como **CSV UTF-8 (delimitado
     por vírgulas)**.
3. Preenche a coluna `translation`. Não mudes o nome dos ficheiros, não
   acrescentes nem removas colunas e não alteres `id` nem `english`. Ordenar e
   filtrar não tem problema.
4. Guarda como CSV (UTF-8, separado por vírgulas) com o mesmo nome.
5. No GitHub abre a pasta da língua, **Add file > Upload files**, larga os
   teus ficheiros e depois **Propose changes** e **Create pull request**.

Não precisas de traduzir tudo de uma vez - envia o que tiveres.

## Regras

1. **Apenas a coluna `translation`.** `id` e `english` ficam como estão; a
   verificação recusa um ficheiro em que tenham sido alterados.
2. **Mantém cada variável e cada código exatamente como no inglês, na mesma
   ordem** - é o jogo que os preenche:
   - variáveis printf: `%s` `%d` `%u` `%ld` `%.1f` `%5d` ... e `%%` (um sinal de percentagem);
   - marcadores: `{0}` `{#0}` `{name}` `{skrot}` ...;
   - `[ENTER]` é uma quebra de linha numa janela de missão; `[WAIT]`,
     `[DELAY value;5]`, `[COLOR r;1|g;0|b;0]` são os seus comandos;
   - cores `|cffff0000` ... `|r`, ligações `|H` ... `|h`, `|E` ... `|e`.

   Podes movê-los dentro da frase conforme a tua língua precisar, mas as
   variáveis do tipo `%` têm de ficar na mesma ordem. Um texto entre
   parênteses retos como `[Guild]` ou `[PT]` é texto normal: traduz-o.
3. **Letras.** O jogo desenha cada língua numa página de código do Windows,
   por isso só as suas letras podem ser mostradas - nada de emoji, nem
   símbolos como `→` ou `✓`:

   | página de código | línguas | letras |
   |---|---|---|
   | 1250 | pl, cs, sk, hu, ro, hr, sl, sr (latino), bs, sq | ą ć ę ł ń ó ś ź ż, á č ď é ě í ň ř š ť ú ů ý ž, ő ű, ă â î ş ţ |
   | 1251 | ru, uk, bg, be, mk, sr (cirílico) | а б в г д ... я, є і ї ґ, ў, ђ ј љ њ ћ џ |
   | 1252 | de, fr, es, it, pt, nl, da, sv, no, fi, ca, id ... | à á â ã ä å æ ç è é ê ë ì í î ï ñ ò ó ô õ ö ø ù ú û ü ß œ |
   | 1253 | el | α β γ δ ... ω, ά έ ή ί ό ύ ώ |
   | 1254 | tr, az | ç ğ ı İ ö ş ü, â î û |
   | 1257 | lt, lv, et | ā č ē ģ ī ķ ļ ņ š ū ž, ą ę ė į ų |

   Romeno: a página de código só tem **ş ţ com cedilha**, não ș ț com
   vírgula. O launcher (`6_launcher_*`) é um programa do Windows à parte e
   aceita qualquer letra. O painel web (`7_panel_*`), uma página no navegador,
   também: ambos são **UTF-8**, qualquer letra de qualquer língua.
4. **O chat dos bots** (linhas cujas notas dizem "ASCII letters only"): os
   bots escrevem como jogadores, com letras simples a-z sem acentos.
5. **Comprimento.** Onde as notas dizem "max N characters", o jogo não tem
   espaço para mais.
6. **Quebras de linha** só onde o inglês as tem ou as notas dizem "new lines
   allowed".
7. **O painel web** (`7_panel_*`): os seus textos vão para uma página web, por
   isso mantém as tags HTML do inglês exatamente como estão (`<b>`, `</b>`,
   `<a href="...">`, `<br>` e os marcadores do tipo `<number>` entre ângulos) e
   não acrescentes nenhum `<`, `>` ou `javascript:` teu. As suas variáveis são
   `%s`, `%d`, `%(name)s` e `{name}`; um `%(name)s` com nome pode mudar de
   lugar. Um `%` seguido de espaço (`25% a character`) é um sinal de
   percentagem. Uma língua com pelo menos um texto do painel traduzido aparece
   na escolha de língua do painel; o que não está traduzido aparece em inglês.

## Uma nova língua

1. Copia toda a pasta `template/` para uma pasta com o código ISO 639-1 de
   duas letras da tua língua (`hu`, `es`, `cs`, `pl`... - vê
   [a lista](https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes)).
   Podes fazê-lo numa folha de cálculo: descarrega `template/`, traduz e
   carrega os ficheiros na nova pasta (**Add file > Upload files**, escreve
   `xx/` antes do nome para criar a pasta).
2. Traduz e abre um pull request.

Uma nova língua precisa de algum trabalho no jogo antes de os jogadores a
poderem escolher (as línguas fora da página de código 1250 precisam também de
um novo cliente), por isso pode chegar algumas versões depois da primeira
tradução.

## A verificação

Cada pull request executa `tools/validate.py` (GitHub Actions). Assinala, na
linha onde o encontrou:

- um `id` que não está em `template/`, ou que aparece duas vezes;
- uma coluna `english` alterada;
- variáveis, marcadores, etiquetas ou códigos de cor diferentes dos do inglês;
- na folha do painel web, outras tags HTML que as do inglês, ou um `<`, `>`
  ou `javascript:` próprio;
- uma letra fora da página de código da língua, uma tabulação, um carácter de
  controlo, uma quebra de linha onde não é permitida, um texto demasiado
  longo.

Só são avaliadas as linhas que o teu pull request alterou; os problemas que já
estavam nos ficheiros são contados, não te são atribuídos. Para a executares
tu mesmo (Python 3, nada a instalar): `python tools/validate.py pt`.

## Licença

Ao abrires um pull request, aceitas que a tua tradução seja usada no Metin2
Singleplayer e partilhada nas mesmas condições que o projeto:
[CC BY-NC-ND 4.0](LICENSE). Os colaboradores são creditados no projeto. O
Metin2 e os seus textos originais pertencem à Ymir Interactive e à Webzen.
