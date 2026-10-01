"""Genera el blog de itacacrecimiento.com (blog/ y un subdirectorio por artículo).

Para añadir un artículo: añade un dict a POSTS con su fecha y vuelve a ejecutar
    python3 gen_blog.py <raíz del repositorio>
Los artículos se ordenan por fecha, del más reciente al más antiguo.
"""
import json, os, sys

ROOT = sys.argv[1]
SITE = "https://itacacrecimiento.com"
AUTOR = "Javier Beltrán"
MESES = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto",
         "septiembre", "octubre", "noviembre", "diciembre"]

def fecha_larga(iso):
    y, m, d = iso.split("-")
    return f"{int(d)} de {MESES[int(m) - 1]} de {y}"

NOTA_ICO = '<p class="note">Datos de ICO Crecimiento según la información pública del ICO a septiembre de 2026. Comprueba siempre las condiciones vigentes en <a href="https://www.ico.es" rel="noopener">www.ico.es</a>.</p>'

POSTS = []

# ------------------------------------------------------------------ 1
POSTS.append(dict(
slug="ico-crecimiento-o-prestamo-bancario",
fecha="2026-09-30",
titulo="ICO Crecimiento o préstamo bancario: cuál le conviene a tu pyme",
seo="ICO Crecimiento o préstamo bancario: diferencias y cuál conviene",
desc="Comparamos ICO Crecimiento con un préstamo o una póliza del banco: quién decide, plazos, carencia y en qué casos conviene cada uno.",
resumen="""<p>ICO Crecimiento y el préstamo bancario no compiten: se complementan.</p>
<ul>
  <li><strong>ICO Crecimiento</strong> conviene cuando necesitas plazo largo (hasta 5 años para circulante y 10 para inversión), carencia, o cuando tu banco no ve bien la operación, por ejemplo porque la inversión es en intangibles.</li>
  <li><strong>El banco</strong> conviene para importes pequeños, empresas de menos de 4 años o bienes que sirven de garantía, como un vehículo en leasing.</li>
</ul>""",
cuerpo=NOTA_ICO + """
<h2>Las diferencias principales</h2>
<div class="table-wrap">
<table>
  <thead><tr><th></th><th>ICO Crecimiento</th><th>Préstamo o póliza del banco</th></tr></thead>
  <tbody>
    <tr><td>Quién decide</td><td>El ICO</td><td>El banco</td></tr>
    <tr><td>Dónde se pide</td><td>ICO Online</td><td>En la oficina o la banca online</td></tr>
    <tr><td>Importe mínimo</td><td>50.000 €</td><td>Sin mínimo general</td></tr>
    <tr><td>Plazo circulante</td><td>Hasta 5 años, con 1 de carencia</td><td>Pólizas que se suelen renovar cada año</td></tr>
    <tr><td>Plazo inversión</td><td>Hasta 10 años, con 2 de carencia</td><td>Según el banco y la garantía</td></tr>
    <tr><td>Tipo de interés</td><td>Euríbor + 0,75 % a 1,75 %</td><td>Según el banco y el cliente</td></tr>
    <tr><td>Requisitos</td><td>4 años de antigüedad y cuentas auditadas o aval público</td><td>Los que fije el banco</td></tr>
  </tbody>
</table>
</div>

<h2>Cuándo conviene ICO Crecimiento</h2>
<ul>
  <li><strong>Necesitas plazo largo.</strong> Para circulante, 5 años con uno de carencia es mucho más de lo que suele dar una póliza de crédito.</li>
  <li><strong>Inviertes en intangibles.</strong> Software, desarrollo, marca o digitalización: el banco no tiene nada que tomar como garantía y suele ponerlo difícil. ICO Crecimiento está pensado justamente para eso.</li>
  <li><strong>Tu banco ya tiene mucho riesgo contigo.</strong> Si tu endeudamiento es alto pero sostenible, el ICO puede financiar lo que el banco ya no quiere asumir.</li>
  <li><strong>Quieres dejar libres tus líneas bancarias</strong> para el día a día, los avales o los imprevistos.</li>
</ul>

<h2>Cuándo conviene el banco</h2>
<ul>
  <li>Necesitas <strong>menos de 50.000 €</strong>, el mínimo de ICO Crecimiento.</li>
  <li>Tu empresa tiene <strong>menos de 4 años</strong>.</li>
  <li>Financias un bien que sirve de garantía, como un <strong>vehículo o una máquina en leasing</strong>, donde el banco o la financiera del fabricante ofrecen buenas condiciones.</li>
  <li>Necesitas el dinero <strong>en muy pocos días</strong> y ya tienes una línea aprobada con tu banco.</li>
</ul>

<h2>Lo más habitual: combinar los dos</h2>
<p>Muchas pymes usan ICO Crecimiento para la financiación a largo plazo (el circulante estructural o un proyecto de inversión) y mantienen con el banco las pólizas y el leasing del día a día. Así reparten el riesgo entre dos financiadores y no dependen de uno solo.</p>
""",
faqs=[
("¿Es mejor ICO Crecimiento que un préstamo del banco?", "Depende de la operación. ICO Crecimiento ofrece plazos largos y carencia y no depende del banco, pero exige un mínimo de 50.000 €, 4 años de antigüedad y cuentas auditadas o un aval público. Para importes pequeños o empresas jóvenes suele encajar mejor el banco."),
("¿Puedo tener a la vez ICO Crecimiento y préstamos con el banco?", "Sí. Es lo más habitual: ICO Crecimiento para la financiación a largo plazo y el banco para las pólizas y el leasing del día a día."),
],
))

# ------------------------------------------------------------------ 2
POSTS.append(dict(
slug="que-se-puede-financiar-con-ico-crecimiento",
fecha="2026-09-30",
titulo="Qué se puede financiar con ICO Crecimiento: ejemplos por tipo de gasto",
seo="Qué se puede financiar con ICO Crecimiento: ejemplos de gastos",
desc="Ejemplos concretos de lo que se puede financiar con ICO Crecimiento: circulante, maquinaria, vehículos, software, I+D, marca y más, con los porcentajes que cubre.",
resumen="""<p>ICO Crecimiento financia dos grandes tipos de necesidad:</p>
<ul>
  <li><strong>Circulante:</strong> el dinero para funcionar mientras cobras (proveedores, existencias, nóminas). Hasta el 100 % de la necesidad, a 5 años.</li>
  <li><strong>Inversión:</strong> activos materiales, inmateriales o financieros. Hasta el 80 % de la inversión, a 10 años.</li>
</ul>""",
cuerpo=NOTA_ICO + """
<h2>Circulante</h2>
<p>Es la necesidad de dinero que genera la propia actividad, sobre todo cuando pagas antes de cobrar. Ejemplos:</p>
<ul>
  <li>Pago a proveedores y compra de materia prima.</li>
  <li>Existencias: el stock que necesitas para vender.</li>
  <li>Nóminas y gastos corrientes mientras llegan los cobros.</li>
  <li>El desfase de tesorería al crecer: nuevos clientes que pagan a 60 o 90 días.</li>
</ul>
<p>Plazo de hasta 5 años con 1 de carencia, y hasta el 100 % de la necesidad. Lo explicamos a fondo en la guía de <a href="../../guias/ico-crecimiento-circulante/">ICO Crecimiento para circulante</a>.</p>

<h2>Inversión en activos materiales</h2>
<ul>
  <li>Maquinaria y equipos de producción.</li>
  <li>Vehículos y renovación de flota.</li>
  <li>Reforma o ampliación de naves, locales y oficinas.</li>
  <li>Instalaciones: cámaras de frío, placas solares, climatización.</li>
  <li>Equipos informáticos.</li>
</ul>

<h2>Inversión en activos inmateriales</h2>
<p>Es donde ICO Crecimiento marca más diferencia, porque el banco suele financiar mal lo que no se puede tocar:</p>
<ul>
  <li>Desarrollo de software y aplicaciones propias.</li>
  <li>Proyectos de I+D.</li>
  <li>Registro y desarrollo de marcas y patentes.</li>
  <li>Digitalización: comercio electrónico, programas de gestión, automatización.</li>
</ul>

<h2>Inversión en activos financieros</h2>
<p>La línea también contempla activos financieros. Si tu proyecto pasa por una operación de este tipo, conviene revisar con detalle cómo encaja en las condiciones vigentes antes de plantearla.</p>

<h2>Cuánto financia</h2>
<dl class="data-list">
  <div><dt>Circulante</dt><dd>Hasta el 100 % de la necesidad, a un plazo de hasta 5 años con 1 de carencia</dd></div>
  <div><dt>Inversión</dt><dd>Hasta el 80 % de la inversión, a un plazo de hasta 10 años con 2 de carencia. El 20 % restante lo aporta la empresa</dd></div>
  <div><dt>Mínimo</dt><dd>50.000 €, sin importe máximo fijado</dd></div>
</dl>

<h2>¿Y si mi necesidad es otra?</h2>
<p>Si lo que necesitas no aparece aquí, por ejemplo reorganizar deudas que ya tienes, confirma antes si encaja en las condiciones vigentes de la línea. En el diagnóstico inicial lo revisamos contigo.</p>
""",
faqs=[
("¿ICO Crecimiento financia software y digitalización?", "Sí. Financia activos inmateriales como el desarrollo de software, la I+D, las marcas o la digitalización, que son justamente lo que peor financia el banco."),
("¿ICO Crecimiento financia vehículos?", "Sí, los vehículos son activos materiales y pueden financiarse como inversión, hasta el 80 % y a un plazo de hasta 10 años."),
("¿Qué parte de la inversión cubre ICO Crecimiento?", "Hasta el 80 % en las operaciones de inversión y hasta el 100 % en las de circulante."),
],
))

# ------------------------------------------------------------------ 3
POSTS.append(dict(
slug="ico-crecimiento-empresas-de-transporte",
fecha="2026-09-30",
titulo="ICO Crecimiento para empresas de transporte: circulante y renovación de flota",
seo="ICO Crecimiento para empresas de transporte y logística",
desc="Cómo pueden usar ICO Crecimiento las empresas de transporte: financiar el gasoil y las nóminas mientras cobran, renovar la flota o invertir en naves y digitalización.",
resumen="""<p>Las empresas de transporte son de las que más pueden aprovechar ICO Crecimiento:</p>
<ul>
  <li><strong>Circulante:</strong> pagan gasoil, peajes y nóminas al momento y cobran a 60 o 90 días. ICO Crecimiento financia ese desfase a 5 años con 1 de carencia.</li>
  <li><strong>Inversión:</strong> renovación de flota, vehículos de bajas emisiones, naves, cámaras de frío o digitalización, a 10 años con 2 de carencia.</li>
  <li>Encaja sobre todo en empresas con flota mediana o grande, al menos 4 años de actividad y cuentas auditadas o aval de SGR.</li>
</ul>""",
cuerpo=NOTA_ICO + """
<h2>El problema de siempre: pagar antes de cobrar</h2>
<p>En transporte, la mayoría de gastos se pagan al contado: gasoil, peajes, nóminas de los conductores, mantenimiento y seguros. En cambio, los cargadores suelen pagar a 60 o 90 días, y a veces más. Cuanto más crece la empresa, más dinero tiene que adelantar.</p>
<p>Normalmente ese hueco se cubre con pólizas de crédito o descuento de facturas que el banco renueva cada año. ICO Crecimiento permite financiarlo a <strong>5 años con 1 de carencia</strong> y hasta el <strong>100 % de la necesidad</strong>, sin depender del banco.</p>

<h2>Inversiones que encajan</h2>
<ul>
  <li><strong>Renovación de flota</strong> y vehículos de bajas emisiones (eléctricos, gas), cada vez más necesarios por las zonas de bajas emisiones de las ciudades.</li>
  <li><strong>Naves y plataformas logísticas</strong>, almacenes y cámaras de frío.</li>
  <li><strong>Digitalización:</strong> programas de gestión de transporte, localización de flota, planificación de rutas.</li>
  <li><strong>Talleres propios</strong> y equipamiento de mantenimiento.</li>
</ul>
<p>Para inversión, el plazo llega a <strong>10 años con 2 de carencia</strong> y se financia hasta el <strong>80 %</strong>. Si solo vas a comprar camiones, compara también con el leasing o la financiación del fabricante: a veces es más sencillo. ICO Crecimiento destaca cuando el proyecto es más amplio o cuando el banco no quiere asumir más riesgo.</p>

<h2>Qué empresas de transporte encajan</h2>
<ul>
  <li>Sociedades con al menos 4 años de actividad.</li>
  <li>Con cuentas auditadas de los dos últimos ejercicios o, si no, con el aval de una <a href="../../guias/aval-sgr/">sociedad de garantía recíproca (SGR)</a>.</li>
  <li>Con una necesidad de al menos 50.000 €.</li>
  <li>En la práctica, flotas medianas y grandes: son las que más circulante mueven y las que suelen tener tamaño para estar auditadas.</li>
</ul>

<h2>Cómo reforzar la solicitud</h2>
<ol class="pasos-guia">
  <li><strong>Periodo medio de cobro:</strong> cuántos días tardan de media tus clientes en pagar, con datos de los últimos meses.</li>
  <li><strong>Gastos al contado:</strong> gasoil, peajes y nóminas por mes, para mostrar cuánto adelantas.</li>
  <li><strong>Contratos con cargadores</strong> o clientes recurrentes que justifiquen el crecimiento.</li>
  <li><strong>Plan de tesorería</strong> a 12 o 24 meses que muestre cómo se devuelve el préstamo.</li>
</ol>
""",
faqs=[
("¿Una empresa de transporte puede pedir ICO Crecimiento?", "Sí, si es una pyme con al menos 4 años de actividad y cuentas auditadas de los dos últimos ejercicios o un aval público, y necesita al menos 50.000 €."),
("¿Se puede financiar el gasoil y las nóminas con ICO Crecimiento?", "Sí, como circulante: ICO Crecimiento financia el desfase entre pagar y cobrar a un plazo de hasta 5 años con 1 de carencia."),
("¿Conviene ICO Crecimiento para comprar camiones?", "Puede convenir, sobre todo si forma parte de un proyecto más amplio o si el banco no quiere asumir más riesgo. Para una compra aislada, compáralo con el leasing o la financiación del fabricante."),
],
))

# ------------------------------------------------------------------ 4
POSTS.append(dict(
slug="errores-al-solicitar-ico-crecimiento",
fecha="2026-09-30",
titulo="7 errores al solicitar ICO Crecimiento y cómo evitarlos",
seo="7 errores al solicitar ICO Crecimiento (y cómo evitarlos)",
desc="Los errores más frecuentes al pedir ICO Crecimiento: requisitos sin comprobar, certificado digital, importes desproporcionados, cifras que no cuadran y más.",
resumen="""<p>La mayoría de solicitudes de ICO Crecimiento que se retrasan o no salen adelante fallan por lo mismo:</p>
<ol>
  <li>No comprobar antes los requisitos.</li>
  <li>Dejar el certificado digital para el final.</li>
  <li>Pedir un importe desproporcionado.</li>
  <li>No distinguir entre circulante e inversión.</li>
  <li>Presentar cifras que no cuadran.</li>
  <li>Olvidar deudas que aparecen en la CIRBE.</li>
  <li>Esperar al final del plazo.</li>
</ol>""",
cuerpo=NOTA_ICO + """
<h2>1. No comprobar antes los requisitos</h2>
<p>ICO Crecimiento pide al menos 4 años de antigüedad y cuentas auditadas de los dos últimos ejercicios o un aval público. Muchas empresas descubren a mitad del proceso que no auditan sus cuentas. Compruébalo antes de empezar y, si hace falta, estudia el <a href="../../guias/aval-sgr/">aval de una SGR</a>.</p>

<h2>2. Dejar el certificado digital para el final</h2>
<p>La solicitud se presenta en ICO Online con el certificado digital de la empresa o Cl@ve. Obtener el certificado de representante de la empresa lleva unos días y exige acreditar el cargo. Tramítalo al principio.</p>

<h2>3. Pedir un importe desproporcionado</h2>
<p>El importe tiene que corresponderse con el tamaño de la empresa, sus resultados y su capacidad de devolución. Pedir de más no aumenta lo que te conceden: aumenta las dudas del analista.</p>

<h2>4. No distinguir entre circulante e inversión</h2>
<p>Tienen condiciones distintas: el circulante, hasta 5 años y el 100 % de la necesidad; la inversión, hasta 10 años y el 80 %. Si tu necesidad mezcla las dos, plantéalo así desde el principio y justifica cada parte por separado.</p>

<h2>5. Presentar cifras que no cuadran</h2>
<p>Las previsiones tienen que ser coherentes con las cuentas anuales, el Impuesto sobre Sociedades y el IVA. Una diferencia sin explicar entre documentos es de lo primero que se detecta.</p>

<h2>6. Olvidar deudas que aparecen en la CIRBE</h2>
<p>El informe de la Central de Información de Riesgos del Banco de España muestra todos tus préstamos y avales. Pide tu informe antes de solicitar y asegúrate de que tu relación de deudas coincide con él.</p>

<h2>7. Esperar al final del plazo</h2>
<p>Las solicitudes se admiten hasta el 31 de diciembre de 2027 o hasta que se agoten los fondos. Con fondos limitados, esperar al último momento es arriesgarse a llegar tarde.</p>

<h2>Cómo evitarlos</h2>
<p>La lista de documentos está en la guía de <a href="../../guias/documentacion-prestamo-ico/">documentación para un préstamo ICO</a>, y las condiciones completas en la guía de <a href="../../guias/ico-crecimiento/">ICO Crecimiento</a>. Si prefieres no arriesgarte, en Ítaca Crecimiento revisamos tu caso y preparamos la solicitud completa.</p>
""",
faqs=[
("¿Por qué se rechaza una solicitud de ICO Crecimiento?", "Los motivos habituales son no cumplir los requisitos de antigüedad o de cuentas auditadas, pedir un importe desproporcionado, presentar cifras que no cuadran entre documentos o no demostrar la capacidad de devolución."),
("¿Qué necesito para presentar la solicitud en ICO Online?", "El certificado digital de representante de la empresa o Cl@ve, además de la documentación económica y el plan del proyecto."),
],
))

# ------------------------------------------------------------------ plantilla
LOGO = '''<svg class="logo" viewBox="0 0 560 160" aria-hidden="true">
        <g transform="translate(24 38) scale(1.3)">
          <path d="M30 4 L30 46 L6 46 Q14 22 30 4 Z" fill="#F3EEE4"/>
          <path d="M35 13 L35 46 L57 46 Q52 26 35 13 Z" fill="#D9774C"/>
          <path d="M4 54 Q18 48 32 54 T60 54" fill="none" stroke="#F3EEE4" stroke-width="3" stroke-linecap="round"/>
        </g>
        <text class="name" x="122" y="98" fill="#F3EEE4">Ítaca</text>
        <text class="tag" x="124" y="124" fill="#F3EEE4">CRECIMIENTO</text>
      </svg>'''

POSTS.sort(key=lambda p: p["fecha"], reverse=True)
ORG = {"@type": "ProfessionalService", "@id": f"{SITE}/#empresa", "name": "Ítaca Crecimiento", "url": f"{SITE}/"}
PERSON = {"@type": "Person", "name": AUTOR, "worksFor": {"@id": f"{SITE}/#empresa"}}

def page(depth, url, title, desc, current, body, jsonld, og_type="article"):
    up = "../" * depth
    CUR = ' aria-current="page"'
    nav = "".join(f'<a href="{up}blog/{p["slug"]}/"{CUR if current == p["slug"] else ""}>{p["titulo"]}</a>' for p in POSTS)
    ld = "\n".join(f'<script type="application/ld+json">\n{json.dumps(j, ensure_ascii=False, indent=2)}\n</script>' for j in jsonld)
    return f'''<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="Ítaca Crecimiento">
<meta property="og:locale" content="es_ES">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/assets/og-image.jpg">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/favicon.ico" sizes="48x48">
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<link rel="icon" type="image/png" sizes="96x96" href="/favicon-96x96.png">
<link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<meta name="theme-color" content="#0E2A47">
<link rel="stylesheet" href="{up}assets/fonts/fonts.css">
<link rel="stylesheet" href="{up}assets/legal.css">
<link rel="stylesheet" href="{up}assets/guias.css">
{ld}
</head>
<body>

<header class="legal-header" data-autohide="sticky">
  <div class="inner">
    <a href="{up}" aria-label="Ítaca Crecimiento, volver al inicio">
      {LOGO}
    </a>
    <a class="back" href="{up}#contacto">Solicitar ICO Crecimiento →</a>
  </div>
</header>

<main class="legal">
  <aside class="legal-side">
    <p class="eyebrow">Blog</p>
    <nav class="legal-nav" aria-label="Artículos del blog"><a href="{up}blog/"{CUR if current == "hub" else ""}>Todos los artículos</a>{nav}<a href="{up}guias/">Guías sobre ICO Crecimiento →</a></nav>
  </aside>
  <article class="legal-body">
{body}
  </article>
</main>

<footer class="legal-footer">
  <div class="inner">
    <span>© 2026 Ítaca Crecimiento · Consultoría independiente. No somos una entidad financiera ni formamos parte del ICO.</span>
    <nav aria-label="Legal"><a href="{up}">Inicio</a><a href="{up}guias/">Guías</a><a href="{up}aviso-legal.html">Aviso legal</a><a href="{up}privacidad.html">Privacidad</a><a href="{up}cookies.html">Cookies</a></nav>
  </div>
</footer>

<script src="{up}assets/nav.js" defer></script>
</body>
</html>
'''

CTA = '''
    <aside class="cta">
      <h2>¿Quieres solicitar ICO Crecimiento?</h2>
      <p>Empezamos con un <strong>estudio gratuito y sin compromiso</strong>: si la operación es viable y cuánto conviene pedir. Si decides seguir, preparamos el expediente completo y te acompañamos en ICO Online hasta la firma.</p>
      <a class="btn" href="{up}test-ico-crecimiento/">Haz el test de requisitos (1 minuto)</a>
      <p style="font-size:14px">O <a href="{up}#contacto" style="color:var(--cream);text-decoration:underline">escríbenos directamente</a>.</p>
    </aside>'''

GUIAS_CLAVE = [("ico-crecimiento", "ICO Crecimiento: qué es, requisitos y cómo solicitarlo"),
               ("ico-crecimiento-circulante", "ICO Crecimiento para circulante")]

def relacionados(slug):
    otros = [x for x in POSTS if x["slug"] != slug][:2]
    li = "".join(f'\n      <li><a href="../{x["slug"]}/">{x["titulo"]}</a></li>' for x in otros)
    li += "".join(f'\n      <li><a href="../../guias/{s_}/">{t}</a></li>' for s_, t in GUIAS_CLAVE)
    return f'''
    <nav class="relacionados" aria-label="Sigue leyendo">
      <p class="eyebrow">Sigue leyendo</p>
      <ul>{li}
      </ul>
    </nav>'''

for p in POSTS:
    url = f"{SITE}/blog/{p['slug']}/"
    faq_html = "".join(f"\n    <h3>{q}</h3>\n    <p>{a}</p>" for q, a in p["faqs"])
    body = f'''    <p class="breadcrumb"><a href="../../">Inicio</a><span aria-hidden="true">/</span><a href="../">Blog</a><span aria-hidden="true">/</span>{p["titulo"]}</p>
    <h1>{p["titulo"]}</h1>
    <p class="byline">Por <strong>{AUTOR}</strong>, Ítaca Crecimiento · <time datetime="{p["fecha"]}">{fecha_larga(p["fecha"])}</time></p>
    <div class="resumen">
      <p class="eyebrow">En resumen</p>
      {p["resumen"]}
    </div>
{p["cuerpo"]}
    <h2>Preguntas frecuentes</h2>
    <div class="faq-guia">{faq_html}
    </div>
{relacionados(p["slug"])}
{CTA.format(up="../../")}'''
    jsonld = [
        {"@context": "https://schema.org", "@type": "BlogPosting", "headline": p["titulo"], "description": p["desc"],
         "datePublished": p["fecha"], "dateModified": p["fecha"], "inLanguage": "es-ES",
         "author": PERSON, "publisher": ORG, "mainEntityOfPage": url, "image": f"{SITE}/assets/og-image.jpg"},
        {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in p["faqs"]]},
        {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Inicio", "item": f"{SITE}/"},
            {"@type": "ListItem", "position": 2, "name": "Blog", "item": f"{SITE}/blog/"},
            {"@type": "ListItem", "position": 3, "name": p["titulo"], "item": url}]},
    ]
    os.makedirs(f"{ROOT}/blog/{p['slug']}", exist_ok=True)
    with open(f"{ROOT}/blog/{p['slug']}/index.html", "w") as fh:
        fh.write(page(2, url, f"{p['seo']} | Ítaca Crecimiento", p["desc"], p["slug"], body, jsonld))

items = "".join(
    f'\n      <li><p class="byline" style="margin:0 0 6px"><time datetime="{p["fecha"]}">{fecha_larga(p["fecha"])}</time></p><h2><a href="{p["slug"]}/">{p["titulo"]}</a></h2><p>{p["desc"]}</p></li>'
    for p in POSTS)
hub_body = f'''    <p class="breadcrumb"><a href="../">Inicio</a><span aria-hidden="true">/</span>Blog</p>
    <h1>Blog de ICO Crecimiento</h1>
    <p class="lead">Artículos prácticos sobre ICO Crecimiento y la financiación de pymes: casos por sector, comparativas y consejos para preparar una buena solicitud. Por {AUTOR}, de Ítaca Crecimiento.</p>
    <ul class="guia-list">{items}
    </ul>
{CTA.format(up="../")}'''
hub_url = f"{SITE}/blog/"
hub_ld = [{"@context": "https://schema.org", "@type": "Blog", "name": "Blog de ICO Crecimiento · Ítaca Crecimiento",
           "url": hub_url, "inLanguage": "es-ES", "publisher": ORG,
           "blogPost": [{"@type": "BlogPosting", "headline": p["titulo"], "url": f"{SITE}/blog/{p['slug']}/", "datePublished": p["fecha"]} for p in POSTS]}]
with open(f"{ROOT}/blog/index.html", "w") as fh:
    fh.write(page(1, hub_url, "Blog de ICO Crecimiento | Ítaca Crecimiento",
                  "Artículos prácticos sobre ICO Crecimiento y financiación de pymes: casos por sector, comparativas y consejos para preparar la solicitud.",
                  "hub", hub_body, hub_ld, og_type="website"))

print("\n".join(f"blog/{p['slug']}/" for p in POSTS))
