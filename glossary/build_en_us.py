# Builds en_US/ from template/: the English source in US spelling (python3 glossary/build_en_us.py).
import csv,glob,io,os,sys
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import uk2us
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
tot=chg=0
for f in sorted(glob.glob('template/*.csv')):
    raw=open(f,encoding='utf-8',newline='').read()
    rows=list(csv.reader(io.StringIO(raw,newline='')))
    nl='\r\n' if raw.split('\n',1)[0].endswith('\r') else '\n'
    out=[rows[0]]
    for r in rows[1:]:
        r=list(r)
        if len(r)==6 and r[1].strip():
            t=uk2us.convert(r[1]); r[3]=t; r[5]='done'; tot+=1; chg+= t!=r[1]
        out.append(r)
    buf=io.StringIO(); csv.writer(buf,lineterminator=nl).writerows(out)
    open(os.path.join('en_US',os.path.basename(f)),'w',encoding='utf-8',newline='').write(buf.getvalue())
print('rows',tot,'changed',chg)
