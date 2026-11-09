# -*- coding: utf-8 -*-
"""British -> American spelling for the game texts (whole words, case kept)."""
import re
W = {}
def add(uk, us):
    W[uk] = us
# -our -> -or (with derivatives)
for s in ['colour','armour','honour','favour','flavour','rumour','behaviour','neighbour','harbour','labour',
          'valour','vigour','rigour','odour','humour','splendour','saviour','endeavour','parlour','clamour',
          'ardour','fervour','candour','tumour','vapour','savour','arbour','rancour','demeanour','succour']:
    base = s[:-2] + 'r'   # colour -> color
    for suf in ['', 's', 'ed', 'ing', 'ful', 'less', 'able', 'ably', 'ite', 'ites', 'er', 'ers', 'ful', 'fully', 'ous', 'ation', 'y', 'ers']:
        add(s + suf, base + suf)
add('honourable', 'honorable'); add('favourable', 'favorable'); add('favourably', 'favorably')
add('armoury', 'armory'); add('armouries', 'armories'); add('savoury', 'savory'); add('flavoured', 'flavored')
add('neighbourhood', 'neighborhood'); add('neighbourhoods', 'neighborhoods'); add('behavioural', 'behavioral')
add('humourous', 'humorous'); add('glamourous', 'glamorous'); add('vigourous', 'vigorous')
# -re -> -er
for s in ['centre','theatre','metre','litre','fibre','sabre','sombre','spectre','calibre','lustre','meagre','sceptre','mitre','kilometre','centimetre','millimetre']:
    us = s[:-2] + 'er'
    for suf, usuf in [('', ''), ('s', 's'), ('d', 'ed')]:
        add(s + suf, us + usuf)
add('centring', 'centering')
# -ise -> -ize
for st in ['real','recogn','organ','apolog','special','summar','memor','priorit','util','optim','custom','final','minim',
           'maxim','material','mobil','critic','emphas','sympath','visual','synchron','character','categor','legal',
           'civil','normal','stabil','energ','personal','author','standard','initial','crystall','terror','harmon',
           'immobil','revital','scrutin','neutral','fertil','central','capital','popular','modern','familiar','jeopard',
           'agon','antagon','baptis','colon','econom','equal','evangel','fantas','galvan','global','hospital','hypnot',
           'ideal','immortal','industrial','item','legitim','liberal','magnet','marginal','mechan','memorial','mesmer',
           'moral','nationa','natural','oxid','patron','penal','pulver','radical','random','rational','reorgan','revolution',
           'satir','scandal','sensit','serial','social','spiritual','steril','stigmat','subsid','symbol','tantal','theor',
           'tranquil','trivial','tyrann','unrecogn','vandal','vapor','victim','vocal','westernis','sanit','monopol','demoral',
           'person','desensit','human','vital','energ','fossil','canon','mobil','immun','summon_never']:
    if st == 'summon_never': continue
    for suf, usuf in [('ise','ize'),('ised','ized'),('ises','izes'),('ising','izing'),('isation','ization'),('isations','izations'),('iser','izer'),('isers','izers'),('isable','izable')]:
        add(st + suf, st + usuf)
add('westernise','westernize')
for uk, us in [('analyse','analyze'),('analysed','analyzed'),('analyses_v','x'),('analysing','analyzing'),('paralyse','paralyze'),
               ('paralysed','paralyzed'),('paralyses','paralyzes'),('paralysing','paralyzing'),('catalyse','catalyze'),
               ('defence','defense'),('defences','defenses'),('offence','offense'),('offences','offenses'),('pretence','pretense'),
               ('licence','license'),('licences','licenses'),
               ('travelled','traveled'),('travelling','traveling'),('traveller','traveler'),('travellers','travelers'),
               ('cancelled','canceled'),('cancelling','canceling'),('levelled','leveled'),('levelling','leveling'),
               ('labelled','labeled'),('labelling','labeling'),('fuelled','fueled'),('fuelling','fueling'),
               ('modelled','modeled'),('modelling','modeling'),('signalled','signaled'),('signalling','signaling'),
               ('marvellous','marvelous'),('marvelled','marveled'),('jewellery','jewelry'),('jeweller','jeweler'),('jewellers','jewelers'),
               ('fulfil','fulfill'),('fulfils','fulfills'),('fulfilment','fulfillment'),('enrol','enroll'),('enrols','enrolls'),('enrolment','enrollment'),
               ('skilful','skillful'),('skilfully','skillfully'),('wilful','willful'),('instalment','installment'),('instalments','installments'),
               ('quarrelled','quarreled'),('quarrelling','quarreling'),('duelled','dueled'),('duelling','dueling'),('dueller','dueler'),
               ('totalled','totaled'),('rivalled','rivaled'),('channelled','channeled'),('tunnelled','tunneled'),('shovelled','shoveled'),
               ('counsellor','counselor'),('counsellors','counselors'),('worshipped','worshiped'),('worshipping','worshiping'),('worshipper','worshiper'),('worshippers','worshipers'),
               ('grey','gray'),('greyish','grayish'),('greys','grays'),('mould','mold'),('mouldy','moldy'),('moulds','molds'),('plough','plow'),('ploughs','plows'),
               ('programme','program'),('programmes','programs'),('catalogue','catalog'),('catalogues','catalogs'),
               ('manoeuvre','maneuver'),('manoeuvres','maneuvers'),('ageing','aging'),('judgement','judgment'),('judgements','judgments'),
               ('acknowledgement','acknowledgment'),('sceptical','skeptical'),('sceptic','skeptic'),('aeroplane','airplane'),
               ('practise','practice'),('practised','practiced'),('practising','practicing'),('draught','draft'),('draughts','drafts'),
               ('cheque','check'),('cheques','checks'),('pyjamas','pajamas'),('whilst','while'),('mum','mom'),('mummy_never','x'),
               ('moustache','mustache'),('storey','story'),('storeys','stories'),('tyre','tire'),('tyres','tires'),
               ('kerb','curb'),('aluminium','aluminum'),('sulphur','sulfur'),('enquiry','inquiry'),('enquiries','inquiries'),('enquire','inquire'),
               ('oesophagus','esophagus'),('foetus','fetus'),('haemorrhage','hemorrhage'),('anaemia','anemia'),('anaesthetic','anesthetic'),
               ('encyclopaedia','encyclopedia'),('mediaeval','medieval'),('archaeologist_keep','x'),('dialled','dialed'),
               ('gaol','jail'),('gaoler','jailer'),('learnt','learned'),('spelt_never','x'),('artefact','artifact'),('artefacts','artifacts'),
               ('vice-like','vise-like'),('connexion','connection'),('waggon','wagon'),('waggons','wagons'),('speciality','specialty'),('specialities','specialties'),
               ('omelette','omelet'),('doughnut_keep','x'),('cosy','cozy'),('chilli','chili'),('woollen','woolen'),('distil','distill'),('instil','instill'),
               ('appal','appall'),('appals','appalls'),('fiord','fjord'),('carcase','carcass'),('veranda_keep','x')]:
    if us != 'x':
        add(uk, us)
W.pop('analyses_v', None)
# never touch these (they are also American, or differ in meaning)
for keep in ['your','four','hour','pour','tour','flour','sour','contour','devour','glamour','troubadour','amour',
             'advise','surprise','rise','exercise','promise','wise','compromise','enterprise','revise','supervise','televise',
             'devise','disguise','despise','expertise','merchandise','franchise','comprise','otherwise','raise','praise',
             'noise','poise','cruise','chastise','improvise','premise','arise','incise','excise','precise','concise','paradise']:
    W.pop(keep, None)

WORD = re.compile(r"[A-Za-z]+(?:-like)?")
# parts that are code, not prose: HTML tags, {placeholders}, %(name)s, |H...|h link data, [TAGS]
PROTECT = re.compile(r"<[^>]*>|\{[^}]*\}|%\([A-Za-z_]\w*\)[a-z]|\|H.*?\|h|\[[^\]]*\]|https?://\S+")

def conv_word(w, hits):
    low = w.lower()
    us = W.get(low)
    if us is None:
        return w
    if w.isupper() and len(w) > 1:
        r = us.upper()
    elif w[0].isupper():
        r = us[0].upper() + us[1:]
    else:
        r = us
    hits[low] = hits.get(low, 0) + 1
    return r

def convert(text, hits=None):
    if hits is None:
        hits = {}
    out, pos = [], 0
    for m in PROTECT.finditer(text):
        out.append(WORD.sub(lambda x: conv_word(x.group(0), hits), text[pos:m.start()]))
        out.append(m.group(0))
        pos = m.end()
    out.append(WORD.sub(lambda x: conv_word(x.group(0), hits), text[pos:]))
    return ''.join(out)
for uk, us in [('disorganised','disorganized'),('unauthorised','unauthorized'),('multicoloured','multicolored'),
               ('colourfully','colorfully')]:
    W[uk] = us
for uk, us in [('football','soccer'),('footballs','soccer balls'),('footballer','soccer player'),('footballers','soccer players')]:
    W[uk] = us
