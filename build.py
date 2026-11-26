FONTS="https://fonts.googleapis.com/css2?family=Aref+Ruqaa:wght@400;700&family=Amiri:wght@400;700&family=Cormorant+Garamond:wght@500;600;700&family=Source+Sans+3:wght@400;600&display=swap"
WA="https://wa.me/201117008483?text="
L={"ar":dict(dir="rtl",p="",f="index.html",o="en/index.html",ol="EN",oh="en",title="المركز القانوني العالمي | المستشار محمد عبد الجواد عبد المحسن",
 desc="المركز القانوني العالمي: المستشار محمد عبد الجواد عبد المحسن، المحامي بالنقض والإدارية العليا ومشاركوه.",
 brand="المركز القانوني العالمي",nav=("عن المركز","مجالات الممارسة","تواصل"),
 hero='<img src="assets/name.jpg" alt="المستشار محمد عبد الجواد عبد المحسن – المحامي بالنقض والإدارية العليا" width="928" height="450"><div class="dv"></div><h1>المركز القانوني العالمي</h1><p>المستشار محمد عبد الجواد عبد المحسن ومشاركوه، محامون بالنقض والإدارية العليا ومجلس الدولة.</p>',
 cta="تواصل عبر واتساب",msg="السلام عليكم، أود الاستفسار.",about="عن المركز",
 name="المستشار محمد عبد الجواد عبد المحسن",role="المحامي بالنقض والإدارية العليا ومشاركوه",team="السادة المستشارون",
 ppl=[("وليد رمضان الزيادي","المحامي بالنقض والإدارية العليا والدستورية العليا"),("صلاح عبد الله البهلول","المحامي بالنقض والإدارية العليا والدستورية العليا"),("هيثم رشدي","المحامي بالاستئناف العالي ومجلس الدولة"),("عصام عبد اللطيف","المحامي بالاستئناف العالي ومجلس الدولة")],
 areasT="مجالات الممارسة",areas=["القضايا المدنية والتجارية","مجلس الدولة والقضاء الإداري","الأحوال الشخصية والأسرة","العقارات والإيجارات","تأسيس الشركات","صياغة ومراجعة العقود","الاستشارات القانونية"],
 ct="تواصل معنا",ctp="للاستفسار الأولي تواصل معنا عبر واتساب.",
 foot="© 2026 المركز القانوني العالمي. المحتوى للتعريف العام ولا يُعد استشارة قانونية. لا ترسل مستندات أو وقائع سرية عبر واتساب."),
"en":dict(dir="ltr",p="../",f="en/index.html",o="../index.html",ol="عربي",oh="ar",title="Global Legal Center | Counselor Mohammed Abd-El-Gawad Abd-El-Mohsen",
 desc="Global Legal Center: Counselor Mohammed Abd-El-Gawad Abd-El-Mohsen, Lawyer before the Court of Cassation and the Supreme Administrative Court, and Partners.",
 brand="Global Legal Center",nav=("About","Practice areas","Contact"),
 hero='<h1>Global Legal Center</h1><div class="dv"></div><p style="font-family:var(--hd);font-size:30px;color:var(--navy);margin-bottom:6px">Counselor Mohammed Abd-El-Gawad Abd-El-Mohsen</p><p>Lawyer before the Court of Cassation and the Supreme Administrative Court, and Partners.</p>',
 cta="Contact us on WhatsApp",msg="Hello, I would like to inquire.",about="About the firm",
 name="Counselor Mohammed Abd-El-Gawad Abd-El-Mohsen",role="Lawyer before the Court of Cassation and the Supreme Administrative Court, and Partners",team="Our counselors",
 ppl=[("Waleed Ramadan El-Zayadi","Attorney before the Court of Cassation, the Supreme Administrative Court and the Supreme Constitutional Court"),("Salah Abdallah El-Bahlool","Attorney before the Court of Cassation, the Supreme Administrative Court and the Supreme Constitutional Court"),("Haitham Rushdy","Attorney before the Court of Appeal and the Council of State"),("Essam Abd-El-Latif","Attorney before the Court of Appeal and the Council of State")],
 areasT="Practice areas",areas=["Civil and commercial law","Council of State and administrative justice","Personal status and family law","Real estate and rent disputes","Company formation","Contract drafting and review","Legal consultations"],
 ct="Contact",ctp="For an initial inquiry, message us on WhatsApp.",
 foot="© 2026 Global Legal Center. Content is for general information and is not legal advice. Do not send confidential documents or facts over WhatsApp.")}
from urllib.parse import quote
for k,t in L.items():
    p=t["p"];nv=t["nav"]
    ppl="".join(f'<div class="card"><h3>{a}</h3><p>{b}</p></div>' for a,b in t["ppl"])
    ar="".join(f"<li>{a}</li>" for a in t["areas"])
    h=f'''<!doctype html><html lang="{k}" dir="{t["dir"]}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{t["title"]}</title><meta name="description" content="{t["desc"]}"><link rel="canonical" href="https://faresalqalm-tech.github.io/Global-Legal-Center/{t["f"].replace("index.html","")}">
<link rel="alternate" hreflang="ar" href="https://faresalqalm-tech.github.io/Global-Legal-Center/"><link rel="alternate" hreflang="en" href="https://faresalqalm-tech.github.io/Global-Legal-Center/en/"><link rel="alternate" hreflang="x-default" href="https://faresalqalm-tech.github.io/Global-Legal-Center/">
<meta property="og:title" content="{t["title"]}"><meta property="og:description" content="{t["desc"]}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="{FONTS}" rel="stylesheet"><link rel="stylesheet" href="{p}style.css"></head><body>
<header><div class="w bar"><a class="brand" href="#top"><img src="{p}assets/logo.jpg" alt="" width="48" height="48"><span class="bn">{t["brand"]}</span></a>
<nav><a class="l" href="#about">{nv[0]}</a><a class="l" href="#areas">{nv[1]}</a><a class="l" href="#contact">{nv[2]}</a><a class="lg" href="{t["o"]}" hreflang="{t["oh"]}" lang="{t["oh"]}">{t["ol"]}</a></nav></div></header>
<main id="top"><div class="hero"><div class="w">{t["hero"].replace('src="assets','src="'+p+'assets')}<p><a class="btn" href="{WA}{quote(t["msg"])}">{t["cta"]}</a></p></div></div>
<section class="wh" id="about"><div class="w"><div class="pf"><img src="{p}assets/counselor.jpg" alt="{t["name"]}" width="320" height="320"><div><h2 style="margin-bottom:4px">{t["name"]}</h2><p>{t["role"]}</p></div></div>
<h2>{t["team"]}</h2><div class="grid">{ppl}</div></div></section>
<section id="areas"><div class="w"><h2>{t["areasT"]}</h2><ul class="al">{ar}</ul></div></section>
<section class="ct" id="contact"><div class="w"><h2>{t["ct"]}</h2><p>{t["ctp"]}</p><a class="btn" href="{WA}{quote(t["msg"])}">{t["cta"]}</a></div></section></main>
<footer><div class="w">{t["foot"]}</div></footer></body></html>'''
    open(t["f"],"w",encoding="utf-8").write(h)
