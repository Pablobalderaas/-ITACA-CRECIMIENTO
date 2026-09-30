"""Genera la sección de guías de itacacrecimiento.com (guias/ y un subdirectorio por guía)."""
import json, os, sys, html, re

ROOT = sys.argv[1]
SITE = "https://itacacrecimiento.com"
FECHA_ISO = "2026-09-30"
FECHA = "30 de septiembre de 2026"
AUTOR = "Javier Beltrán"

GUIAS = []  # (slug, titulo, titulo_seo, descripcion, resumen_lista, cuerpo_html, faqs)

# ---------------------------------------------------------------- guía 1
GUIAS.append(dict(
slug="como-solicitar-un-prestamo-ico",
titulo="Cómo solicitar un préstamo ICO paso a paso",
seo="Cómo solicitar un préstamo ICO paso a paso (guía 2026)",
desc="Guía para autónomos y pymes: qué es un préstamo ICO, dónde se pide, qué pasos seguir y los errores que retrasan la solicitud.",
resumen="""<p>Un préstamo ICO se solicita de dos formas, según la línea:</p>
<ul>
  <li><strong>En tu banco</strong>, si es una línea de mediación (por ejemplo, ICO Empresas y Emprendedores). El banco estudia la operación y decide.</li>
  <li><strong>Directamente al ICO</strong>, en la plataforma ICO Online, si es la línea ICO Crecimiento.</li>
</ul>
<p>Los pasos son: definir qué necesitas financiar, elegir la línea, comprobar los requisitos, preparar la documentación, presentar la solicitud y responder a las preguntas del analista hasta la firma.</p>""",
cuerpo="""
<h2>Qué es un préstamo ICO</h2>
<p>El Instituto de Crédito Oficial (ICO) es el banco público de España, dependiente del Ministerio de Economía. Pone en marcha líneas de financiación para autónomos y empresas con condiciones pensadas para la inversión y la liquidez: plazos más largos, periodos de carencia y, en algunos casos, garantías públicas que facilitan que el préstamo se conceda.</p>
<p>Cuando alguien habla de «pedir un ICO» suele referirse a uno de estos préstamos. No es una subvención: es un préstamo que hay que devolver, aunque algunas líneas incluyen ayudas o bonificaciones.</p>

<h2>Las dos vías para solicitarlo</h2>
<h3>1. Líneas de mediación: a través de un banco</h3>
<p>Son la mayoría de las líneas ICO. El ICO pone los fondos y fija las condiciones generales, pero la solicitud se presenta en un banco o entidad adherida a la línea. Es el banco quien analiza el riesgo, decide si concede el préstamo y puede pedir garantías. Puedes acudir a tu banco habitual si está adherido, o a otro.</p>
<h3>2. Financiación directa: ICO Crecimiento</h3>
<p>En la línea ICO Crecimiento no hay banco de por medio. La empresa presenta la solicitud en la plataforma ICO Online, con certificado digital o Cl@ve, y es el propio ICO quien la estudia y concede el préstamo. Tienes todos los detalles en nuestra guía de <a href="../ico-crecimiento/">ICO Crecimiento</a>.</p>

<h2>Paso a paso</h2>
<ol class="pasos-guia">
  <li><strong>Define qué necesitas financiar.</strong> No es lo mismo comprar maquinaria que cubrir tensiones de tesorería. La finalidad (inversión o liquidez), el importe y el plazo determinan qué línea encaja.</li>
  <li><strong>Elige la línea ICO adecuada.</strong> Cada línea tiene sus beneficiarios, finalidades, importes y plazos. Revisa las líneas vigentes en ico.es o consúltalo con un asesor.</li>
  <li><strong>Comprueba los requisitos.</strong> Por ejemplo, estar al corriente con Hacienda y la Seguridad Social, la antigüedad de la empresa o, en algunas líneas, tener cuentas auditadas.</li>
  <li><strong>Prepara la documentación.</strong> Cuentas, impuestos, deudas, certificados y la información del proyecto. Tienes la lista completa en la guía de <a href="../documentacion-prestamo-ico/">documentación para un préstamo ICO</a>.</li>
  <li><strong>Redacta la memoria del proyecto.</strong> Explica qué vas a hacer con el dinero, por qué es viable y cómo vas a devolverlo. Algunas líneas exigen además una memoria técnica.</li>
  <li><strong>Presenta la solicitud.</strong> En tu banco (líneas de mediación) o en ICO Online (ICO Crecimiento). Puedes pedir oferta a varios bancos con el mismo expediente.</li>
  <li><strong>Responde a los requerimientos.</strong> El analista suele pedir aclaraciones o documentos adicionales. Cuanto más completo llegue el expediente, menos idas y vueltas.</li>
  <li><strong>Firma y justifica.</strong> Si se aprueba, se formaliza el préstamo. Algunas líneas piden después justificar el destino de los fondos.</li>
</ol>

<h2>Cuánto tarda</h2>
<p>Depende de la línea, de la entidad y, sobre todo, de lo completo que esté el expediente. Una solicitud con toda la documentación desde el principio evita requerimientos y reduce los plazos de análisis.</p>

<h2>Errores que retrasan o tumban la solicitud</h2>
<ul>
  <li>Pedir una línea que no encaja con la finalidad o con el tipo de empresa.</li>
  <li>Presentar certificados caducados o cifras que no cuadran entre impuestos y cuentas.</li>
  <li>No explicar bien el proyecto ni la capacidad de devolución.</li>
  <li>Solicitar un importe que no se corresponde con el tamaño y los resultados de la empresa.</li>
  <li>No tener en cuenta las deudas que ya tiene la empresa (lo que aparece en la CIRBE).</li>
</ul>
""",
faqs=[
("¿Puedo pedir un préstamo ICO siendo autónomo?", "Sí. Muchas líneas ICO, como la de Empresas y Emprendedores, incluyen a los autónomos. Otras, como ICO Crecimiento, están dirigidas a pymes con unos requisitos concretos de antigüedad y cuentas."),
("¿El ICO me da el dinero directamente?", "Solo en la línea ICO Crecimiento. En las líneas de mediación, que son la mayoría, el préstamo lo concede y lo firma un banco adherido con fondos y condiciones del ICO."),
("¿Quién decide si me conceden el préstamo ICO?", "En las líneas de mediación decide el banco, tras analizar el riesgo de la operación. En ICO Crecimiento decide el propio ICO."),
("¿Me pueden pedir garantías o avales?", "Sí. En las líneas de mediación el banco puede pedir las garantías que considere, salvo lo que establezca cada línea. En algunas líneas el ICO cubre parte del riesgo, lo que facilita la concesión."),
],
))

# ---------------------------------------------------------------- guía 2
GUIAS.append(dict(
slug="documentacion-prestamo-ico",
titulo="Documentación para solicitar un préstamo ICO",
seo="Documentación para solicitar un préstamo ICO: lista completa",
desc="Lista de documentos que suelen pedir para un préstamo ICO a autónomos y sociedades: cuentas, impuestos, CIRBE, certificados y memoria del proyecto.",
resumen="""<p>Para un préstamo ICO suelen pedir cuatro bloques de documentos:</p>
<ul>
  <li><strong>Identificación:</strong> escrituras, CIF y poderes (sociedades) o DNI y alta de autónomo.</li>
  <li><strong>Información económica:</strong> cuentas anuales o IRPF, Impuesto sobre Sociedades, IVA y un balance del año en curso.</li>
  <li><strong>Deudas y obligaciones:</strong> relación de préstamos, informe CIRBE y certificados de estar al corriente con Hacienda y la Seguridad Social.</li>
  <li><strong>El proyecto:</strong> presupuestos o facturas proforma y una memoria que explique la inversión o la necesidad.</li>
</ul>""",
cuerpo="""
<p>Cada banco y cada línea pueden pedir documentos distintos, pero la base es casi siempre la misma. Esta es la lista que usamos para preparar un expediente completo.</p>

<h2>Lista de documentos</h2>
<div class="table-wrap">
<table>
  <thead><tr><th>Documento</th><th>Autónomo</th><th>Sociedad</th></tr></thead>
  <tbody>
    <tr><td>DNI del titular o de los administradores</td><td>Sí</td><td>Sí</td></tr>
    <tr><td>Alta en Hacienda (modelo 036 o 037) y en la Seguridad Social</td><td>Sí</td><td>—</td></tr>
    <tr><td>Escrituras de constitución, CIF y poderes del firmante</td><td>—</td><td>Sí</td></tr>
    <tr><td>Declaración de la renta (modelo 100) de los dos últimos años</td><td>Sí</td><td>—</td></tr>
    <tr><td>Pagos fraccionados del IRPF (modelos 130 o 131)</td><td>Sí</td><td>—</td></tr>
    <tr><td>Cuentas anuales depositadas en el Registro Mercantil (dos o tres últimos ejercicios)</td><td>—</td><td>Sí</td></tr>
    <tr><td>Impuesto sobre Sociedades (modelo 200)</td><td>—</td><td>Sí</td></tr>
    <tr><td>IVA: declaraciones trimestrales (modelo 303) y resumen anual (modelo 390)</td><td>Sí</td><td>Sí</td></tr>
    <tr><td>Balance y cuenta de resultados provisionales del año en curso</td><td>Recomendable</td><td>Sí</td></tr>
    <tr><td>Relación de deudas bancarias (pool bancario)</td><td>Sí</td><td>Sí</td></tr>
    <tr><td>Informe CIRBE del Banco de España</td><td>Sí</td><td>Sí</td></tr>
    <tr><td>Certificados de estar al corriente con Hacienda y la Seguridad Social</td><td>Sí</td><td>Sí</td></tr>
    <tr><td>Presupuestos o facturas proforma de la inversión</td><td>Sí</td><td>Sí</td></tr>
    <tr><td>Memoria del proyecto y previsiones</td><td>Sí</td><td>Sí</td></tr>
  </tbody>
</table>
</div>

<h2>Documentos que más problemas dan</h2>
<h3>El informe CIRBE</h3>
<p>La Central de Información de Riesgos del Banco de España (CIRBE) recoge los préstamos y avales que tienes con las entidades financieras. El banco lo consulta siempre. Puedes pedir tu propio informe gratis en la sede electrónica del Banco de España y revisar que coincide con tu relación de deudas antes de presentar la solicitud.</p>
<h3>Los certificados de estar al corriente</h3>
<p>Los certificados de Hacienda y de la Seguridad Social tienen una validez limitada. Pídelos cerca de la fecha de presentación para que no caduquen durante el análisis.</p>
<h3>La memoria del proyecto</h3>
<p>Es el documento que más pesa en la decisión y el que más se descuida. Debe explicar quién es la empresa, qué se va a financiar, cuánto cuesta, qué resultados se esperan y cómo se devolverá el préstamo. En las empresas de nueva creación, sin histórico contable, es todavía más importante.</p>

<h2>Documentación específica de algunas líneas</h2>
<ul>
  <li><strong>Líneas de inversión sostenible:</strong> suelen exigir una memoria técnica que justifique el impacto del proyecto, por ejemplo el ahorro energético.</li>
  <li><strong>ICO Crecimiento:</strong> la solicitud se presenta en ICO Online con certificado digital o Cl@ve, y se piden cuentas auditadas de los dos últimos ejercicios o un aval público. Más detalles en la guía de <a href="../ico-crecimiento/">ICO Crecimiento</a>.</li>
</ul>

<h2>Consejos para que el expediente pase a la primera</h2>
<ul>
  <li>Comprueba que las cifras cuadran entre impuestos, cuentas y balance provisional.</li>
  <li>Ordena los documentos y nómbralos con claridad: el analista lo agradece.</li>
  <li>Explica por adelantado cualquier dato llamativo, como un año de pérdidas o una deuda puntual.</li>
  <li>Prepara un único expediente que puedas presentar en varios bancos a la vez.</li>
</ul>
""",
faqs=[
("¿Qué documentos piden para un préstamo ICO?", "Normalmente: identificación de la empresa o del autónomo, cuentas anuales o declaración de la renta, Impuesto sobre Sociedades, IVA, balance del año en curso, relación de deudas, informe CIRBE, certificados de estar al corriente con Hacienda y la Seguridad Social, presupuestos de la inversión y una memoria del proyecto."),
("¿Qué es la CIRBE y cómo la consigo?", "Es el informe de la Central de Información de Riesgos del Banco de España, con los préstamos y avales que tienes con entidades financieras. Se puede pedir gratis en la sede electrónica del Banco de España."),
("¿Una empresa nueva puede pedir un préstamo ICO sin cuentas anuales?", "Algunas líneas lo permiten. En ese caso la memoria del proyecto y el plan de negocio, con previsiones realistas, sustituyen al histórico contable y pesan mucho más en la decisión."),
],
))

# ---------------------------------------------------------------- guía 3
GUIAS.append(dict(
slug="ico-crecimiento",
titulo="ICO Crecimiento: qué es, requisitos y cómo solicitarlo",
seo="ICO Crecimiento 2026: requisitos, condiciones y cómo solicitarlo",
desc="ICO Crecimiento es el préstamo directo del ICO para pymes, sin banco: desde 50.000 €, para circulante (hasta 5 años) o inversión (hasta 10 años). Requisitos y cómo se solicita.",
resumen="""<p><strong>ICO Crecimiento</strong> es la línea de financiación directa del ICO: la pyme la solicita en la plataforma ICO Online y es el propio ICO quien analiza y presta, sin banco intermediario.</p>
<ul>
  <li>Préstamos <strong>desde 50.000 €</strong>, sin importe máximo fijado.</li>
  <li>Para <strong>circulante</strong>: hasta 5 años con 1 de carencia y hasta el 100 % de la necesidad.</li>
  <li>Para <strong>inversión</strong>: hasta 10 años con 2 de carencia y hasta el 80 % de la inversión.</li>
  <li>Tipo: <strong>Euríbor más un diferencial</strong> de entre 0,75 % y 1,75 %, según el riesgo.</li>
  <li>Para pymes con <strong>al menos 4 años</strong> y cuentas auditadas de los dos últimos ejercicios o un aval público.</li>
  <li>Solicitudes <strong>hasta el 31 de diciembre de 2027</strong> o hasta que se agoten los fondos.</li>
</ul>""",
cuerpo="""
<p class="note">Datos según la información pública del ICO a septiembre de 2026. Las condiciones pueden cambiar: comprueba siempre las vigentes en <a href="https://www.ico.es" rel="noopener">www.ico.es</a> antes de solicitar.</p>

<h2>Qué es ICO Crecimiento</h2>
<p>Es la primera línea de financiación directa y 100 % digital del Instituto de Crédito Oficial. A diferencia de las líneas de mediación, donde el préstamo lo concede un banco, en ICO Crecimiento la empresa presenta la solicitud directamente al ICO, que la estudia, la aprueba y firma el préstamo. Cuenta con una dotación inicial de 1.000 millones de euros.</p>

<h2>A quién va dirigida</h2>
<p>A pymes con potencial de crecimiento y generación de empleo que tienen más difícil conseguir financiación bancaria por su perfil. En particular:</p>
<ul>
  <li>Empresas innovadoras.</li>
  <li>Empresas con mucha inversión en intangibles: software, I+D, marcas o digitalización.</li>
  <li>Empresas con un endeudamiento elevado pero sostenible.</li>
</ul>

<h2>Condiciones principales</h2>
<dl class="data-list">
  <div><dt>Importe</dt><dd>Desde 50.000 €, sin importe máximo fijado</dd></div>
  <div><dt>Plazo circulante</dt><dd>Hasta 5 años, con hasta 1 año de carencia. Financia hasta el 100 % de la necesidad. Más detalles en la guía de <a href="../ico-crecimiento-circulante/">ICO Crecimiento para circulante</a></dd></div>
  <div><dt>Plazo inversión</dt><dd>Hasta 10 años, con hasta 2 años de carencia de principal. Financia hasta el 80 % de la inversión</dd></div>
  <div><dt>Tipo de interés</dt><dd>Euríbor más un diferencial de entre 0,75 % y 1,75 %, según el riesgo de la operación</dd></div>
  <div><dt>Comisión de apertura</dt><dd>0,5 % del importe concedido</dd></div>
  <div><dt>Finalidad</dt><dd>Activos fijos materiales, inmateriales o financieros, y necesidades de circulante</dd></div>
  <div><dt>Solicitud</dt><dd>En la plataforma ICO Online, con certificado digital o Cl@ve</dd></div>
  <div><dt>Plazo de solicitud</dt><dd>Hasta el 31 de diciembre de 2027 o hasta agotar los fondos</dd></div>
</dl>

<h2>Requisitos</h2>
<ul>
  <li>Ser pyme con domicilio social, establecimiento o sucursal de actividad en España.</li>
  <li>Tener al menos 4 años de antigüedad.</li>
  <li>Tener auditadas las cuentas anuales de los dos últimos ejercicios o contar con un aval público, por ejemplo de una sociedad de garantía recíproca (SGR). Lo explicamos en la guía del <a href="../aval-sgr/">aval de SGR</a>.</li>
  <li>Presentar un proyecto de crecimiento viable.</li>
</ul>

<h2>Cómo se solicita</h2>
<ol class="pasos-guia">
  <li>Comprueba que la empresa cumple los requisitos, sobre todo la antigüedad y las cuentas auditadas o el aval.</li>
  <li>Prepara la documentación económica y el plan del proyecto: qué se financia, cuánto cuesta y cómo se devolverá.</li>
  <li>Accede a ICO Online con el certificado digital de la empresa o Cl@ve y rellena la solicitud.</li>
  <li>Responde a las peticiones de información del ICO durante el análisis.</li>
  <li>Si se aprueba, firma el préstamo también de forma digital.</li>
</ol>
<p>Al no haber un banco que acompañe el proceso, la solicitud tiene que estar completa y bien argumentada desde el principio. Ahí es donde más ayuda preparar el expediente con un especialista.</p>

<h2>ICO Crecimiento frente a las líneas de mediación</h2>
<div class="table-wrap">
<table>
  <thead><tr><th></th><th>ICO Crecimiento</th><th>Líneas de mediación</th></tr></thead>
  <tbody>
    <tr><td>Dónde se pide</td><td>ICO Online</td><td>En un banco adherido</td></tr>
    <tr><td>Quién decide</td><td>El ICO</td><td>El banco</td></tr>
    <tr><td>Quién firma el préstamo</td><td>El ICO</td><td>El banco</td></tr>
    <tr><td>Para quién</td><td>Pymes con al menos 4 años y cuentas auditadas o aval público</td><td>Autónomos y empresas, según cada línea</td></tr>
  </tbody>
</table>
</div>

<h2>ICO Crecimiento Exportadores</h2>
<p>Existe una línea relacionada, ICO Crecimiento Exportadores, dirigida a pymes exportadoras afectadas por el entorno arancelario. Combina préstamos a largo plazo con ayudas, como bonificaciones del tipo de interés y un tramo no reembolsable. Si tu empresa exporta, conviene estudiar cuál de las dos encaja mejor.</p>
""",
faqs=[
("¿Qué es ICO Crecimiento?", "Es la línea de financiación directa del ICO para pymes: la solicitud se presenta en la plataforma ICO Online y es el propio ICO quien analiza y concede el préstamo, sin banco intermediario."),
("¿Cuáles son los requisitos de ICO Crecimiento?", "Ser una pyme con actividad en España, tener al menos 4 años de antigüedad y contar con las cuentas de los dos últimos ejercicios auditadas o con un aval público, además de un proyecto de crecimiento viable."),
("¿Cuánto se puede pedir con ICO Crecimiento?", "Desde 50.000 €, sin un importe máximo fijado. Para circulante, hasta el 100 % de la necesidad a un plazo de hasta 5 años con 1 de carencia; para inversión, hasta el 80 % a un plazo de hasta 10 años con 2 de carencia."),
("¿Hasta cuándo se puede solicitar ICO Crecimiento?", "Hasta el 31 de diciembre de 2027 o hasta que se agoten los fondos disponibles."),
],
))

GUIAS.append(dict(
slug="aval-sgr",
titulo="Aval de SGR: qué es y cómo te ayuda a pedir ICO Crecimiento",
seo="Aval de SGR para ICO Crecimiento: qué es, cómo se pide y cuánto cuesta",
desc="Si tu pyme no tiene las cuentas auditadas, un aval de una sociedad de garantía recíproca (SGR) puede abrirte la puerta a ICO Crecimiento. Qué es, cómo se pide y qué cuesta.",
resumen="""<p>Una <strong>sociedad de garantía recíproca (SGR)</strong> es una entidad financiera que avala a pymes y autónomos para que consigan financiación en mejores condiciones.</p>
<ul>
  <li>En <strong>ICO Crecimiento</strong>, la línea pide cuentas auditadas de los dos últimos ejercicios <strong>o un aval público</strong>. El aval de una SGR es la vía habitual para las pymes que no auditan sus cuentas.</li>
  <li>Para obtenerlo, la empresa presenta una solicitud a la SGR de su comunidad autónoma, que estudia la operación y, si la aprueba, emite el aval.</li>
  <li>La empresa se hace <strong>socia de la SGR</strong>: compra unas participaciones que se le devuelven al terminar la relación, y paga comisiones por el estudio y por el aval.</li>
</ul>""",
cuerpo="""
<p class="note">La forma concreta de combinar el aval de una SGR con ICO Crecimiento puede variar según la SGR y las condiciones vigentes de la línea. Confírmalo con la SGR de tu comunidad y en <a href="https://www.ico.es" rel="noopener">www.ico.es</a> antes de empezar.</p>

<h2>Qué es una SGR</h2>
<p>Las sociedades de garantía recíproca son entidades financieras reguladas por la Ley 1/1994 y supervisadas por el Banco de España. Su función es avalar a pymes y autónomos ante bancos, administraciones y otros organismos, para que consigan financiación que por sí solos tendrían más difícil, o que la consigan con mejores plazos y condiciones.</p>
<p>Son entidades de carácter mutualista: las empresas avaladas se convierten en socias de la SGR. En su capital participan también administraciones públicas, cámaras de comercio y otras entidades. Además, el Estado respalda parte del riesgo que asumen a través de la Compañía Española de Reafianzamiento (CERSA).</p>
<p>La mayoría tienen ámbito autonómico. Hay una SGR en casi todas las comunidades: en Andalucía, por ejemplo, opera Garántia SGR. Puedes consultar la lista completa en la web de la Confederación Española de Sociedades de Garantía (SGR-CESGAR).</p>

<h2>Por qué importa para ICO Crecimiento</h2>
<p>Entre los requisitos de ICO Crecimiento está tener auditadas las cuentas anuales de los dos últimos ejercicios. Muchas pymes no están obligadas a auditarse y no lo hacen. Para ellas, la alternativa que prevé la línea es contar con un aval público, y el aval de una SGR es la forma más habitual de conseguirlo. Varias SGR ya ofrecen productos específicos para acompañar solicitudes de ICO Crecimiento.</p>
<p>Además de cumplir el requisito, el aval refuerza la solicitud: una entidad especializada ha estudiado el proyecto y responde de una parte del riesgo.</p>

<h2>Cómo se consigue el aval, paso a paso</h2>
<ol class="pasos-guia">
  <li><strong>Localiza la SGR de tu comunidad autónoma</strong> y consulta si tiene un producto para ICO Crecimiento.</li>
  <li><strong>Presenta la solicitud</strong> con la documentación de la empresa y del proyecto. Es muy parecida a la que pide el ICO: cuentas, impuestos, deudas y un plan que explique la inversión.</li>
  <li><strong>La SGR estudia la operación.</strong> Analiza la solvencia de la empresa y la viabilidad del proyecto, y puede pedir aclaraciones o garantías adicionales, por ejemplo de los socios.</li>
  <li><strong>Aprobación.</strong> Si la operación sale adelante, la SGR comunica el importe avalado y las condiciones.</li>
  <li><strong>Te haces socio partícipe</strong> suscribiendo las participaciones sociales que te indiquen.</li>
  <li><strong>Emisión del aval</strong> y presentación de la solicitud de ICO Crecimiento en ICO Online con ese aval.</li>
</ol>

<h2>Cuánto cuesta</h2>
<p>El aval de una SGR tiene tres costes principales. Cada SGR publica sus tarifas, así que pide siempre una propuesta por escrito antes de decidir.</p>
<dl class="data-list">
  <div><dt>Participaciones sociales</dt><dd>Un porcentaje del importe avalado que la empresa aporta para hacerse socia. No es un gasto: se devuelve cuando se cancela el aval y la empresa deja de ser socia.</dd></div>
  <div><dt>Comisión de estudio</dt><dd>Se paga una vez, al estudiar o formalizar la operación.</dd></div>
  <div><dt>Comisión de aval</dt><dd>Un porcentaje anual sobre el importe avalado pendiente, mientras dure el aval.</dd></div>
</dl>
<p>Para comparar, suma estos costes al tipo de interés del préstamo y calcula el coste total de la financiación a lo largo de todo el plazo.</p>

<h2>Ventajas e inconvenientes</h2>
<h3>Ventajas</h3>
<ul>
  <li>Permite cumplir el requisito de ICO Crecimiento sin cuentas auditadas.</li>
  <li>Reduce las garantías personales que la empresa tendría que aportar.</li>
  <li>El análisis de la SGR ayuda a detectar puntos débiles del proyecto antes de presentarlo.</li>
</ul>
<h3>Inconvenientes</h3>
<ul>
  <li>Añade un coste: comisiones y la aportación a las participaciones mientras dure el aval.</li>
  <li>Añade un paso más y alarga el calendario: primero hay que obtener el aval y después solicitar el préstamo.</li>
  <li>La SGR puede pedir contragarantías, por ejemplo avales personales de los socios.</li>
</ul>

<h2>¿Aval de SGR o auditar las cuentas?</h2>
<p>Depende de cada empresa. Encargar ahora la auditoría de dos ejercicios puede no ser posible o salir más caro, y no siempre llega a tiempo. El aval de SGR suele ser más rápido de conseguir, pero tiene un coste anual mientras dure el préstamo. En el diagnóstico inicial comparamos las dos opciones con tus cifras.</p>
""",
faqs=[
("¿Qué es una SGR?", "Una sociedad de garantía recíproca es una entidad financiera, supervisada por el Banco de España, que avala a pymes y autónomos para que consigan financiación. Las empresas avaladas se convierten en socias de la SGR."),
("¿Puedo pedir ICO Crecimiento sin cuentas auditadas?", "Sí, si cuentas con un aval público. La vía habitual es el aval de una sociedad de garantía recíproca (SGR), que sustituye al requisito de tener auditadas las cuentas de los dos últimos ejercicios."),
("¿Cuánto cuesta el aval de una SGR?", "Tiene una comisión de estudio, una comisión anual sobre el importe avalado y la aportación a participaciones sociales, que se devuelve al terminar el aval. Cada SGR publica sus tarifas."),
("¿Qué SGR me corresponde?", "Normalmente la de la comunidad autónoma donde tiene su domicilio o su actividad la empresa. En Andalucía, por ejemplo, opera Garántia SGR. La lista completa está en la web de SGR-CESGAR."),
],
))

GUIAS.append(dict(
slug="ico-crecimiento-circulante",
titulo="ICO Crecimiento para circulante: cómo financiar el día a día de tu empresa",
seo="ICO Crecimiento para circulante y liquidez: condiciones y cómo pedirlo",
desc="ICO Crecimiento también financia circulante: hasta 5 años con 1 de carencia y hasta el 100 % de la necesidad, directamente con el ICO y sin banco. Condiciones, ejemplo y cómo justificarlo.",
resumen="""<p>ICO Crecimiento no es solo para inversiones: también financia el <strong>circulante</strong>, es decir, el dinero que la empresa necesita para funcionar mientras cobra.</p>
<ul>
  <li>Plazo de <strong>hasta 5 años con hasta 1 año de carencia</strong>.</li>
  <li>Financia <strong>hasta el 100 %</strong> de la necesidad de circulante.</li>
  <li>Desde <strong>50.000 €</strong>, a tipo Euríbor más un diferencial de entre 0,75 % y 1,75 %, con una comisión de apertura del 0,5 %.</li>
  <li>Se pide <strong>directamente al ICO</strong> en ICO Online, sin banco, con los mismos requisitos: al menos 4 años de antigüedad y cuentas auditadas o un aval público.</li>
</ul>""",
cuerpo="""
<p class="note">Datos según la información pública del ICO a septiembre de 2026. Comprueba siempre las condiciones vigentes en <a href="https://www.ico.es" rel="noopener">www.ico.es</a> antes de solicitar.</p>

<h2>Qué es el circulante</h2>
<p>El circulante es el dinero que una empresa necesita para su actividad diaria: pagar a proveedores, comprar existencias, pagar nóminas y suministros. El problema aparece cuando hay que pagar antes de cobrar.</p>
<p>Un ejemplo típico es una empresa de transporte: paga el gasoil, los peajes y las nóminas cada mes, pero cobra a sus clientes a 60 o 90 días. Cuanto más crece, más dinero tiene que adelantar. Por eso muchas empresas que venden bien se quedan sin liquidez.</p>

<h2>Condiciones de ICO Crecimiento para circulante</h2>
<div class="table-wrap">
<table>
  <thead><tr><th></th><th>Circulante</th><th>Inversión</th></tr></thead>
  <tbody>
    <tr><td>Plazo</td><td>Hasta 5 años</td><td>Hasta 10 años</td></tr>
    <tr><td>Carencia</td><td>Hasta 1 año</td><td>Hasta 2 años</td></tr>
    <tr><td>Parte financiada</td><td>Hasta el 100 % de la necesidad</td><td>Hasta el 80 % de la inversión</td></tr>
    <tr><td>Importe mínimo</td><td>50.000 €</td><td>50.000 €</td></tr>
    <tr><td>Tipo de interés</td><td>Euríbor + 0,75 % a 1,75 %</td><td>Euríbor + 0,75 % a 1,75 %</td></tr>
    <tr><td>Comisión de apertura</td><td>0,5 %</td><td>0,5 %</td></tr>
  </tbody>
</table>
</div>
<p>Una misma empresa puede combinar las dos finalidades si tiene a la vez un proyecto de inversión y una necesidad de circulante.</p>

<h2>Frente a una póliza de crédito del banco</h2>
<p>La forma habitual de financiar el circulante es una póliza de crédito o una línea de descuento, que el banco renueva cada año. ICO Crecimiento no las sustituye, pero tiene ventajas claras como complemento:</p>
<ul>
  <li><strong>Plazo mucho más largo:</strong> hasta 5 años, frente a pólizas que suelen renovarse cada año y que el banco puede reducir.</li>
  <li><strong>Un año de carencia:</strong> el primer año solo se pagan intereses, justo cuando más aprieta la tesorería.</li>
  <li><strong>No depende de tu banco:</strong> las líneas bancarias quedan libres para el día a día.</li>
</ul>

<h2>Ejemplo orientativo</h2>
<p>Una empresa de transporte necesita 200.000 € para cubrir el desfase entre pagos y cobros. Pide ICO Crecimiento para circulante a 5 años con 1 de carencia. Suponiendo un tipo total del 3,5 % (el real depende del Euríbor y del riesgo de la operación):</p>
<dl class="data-list">
  <div><dt>Comisión de apertura</dt><dd>1.000 € (0,5 %), una sola vez</dd></div>
  <div><dt>Primer año (carencia)</dt><dd>Solo intereses: unos 583 € al mes</dd></div>
  <div><dt>Años 2 a 5</dt><dd>Cuota de unos 4.471 € al mes, capital más intereses</dd></div>
  <div><dt>Intereses totales</dt><dd>Unos 21.600 € en los 5 años</dd></div>
</dl>
<p>Es un cálculo simplificado para hacerse una idea. En el diagnóstico hacemos el cálculo con las cifras reales de tu empresa.</p>

<h2>Sectores donde más se usa</h2>
<ul>
  <li><strong>Transporte y logística:</strong> gasoil, peajes y nóminas al contado; cobro a 60 o 90 días.</li>
  <li><strong>Empresas que trabajan para la Administración:</strong> los pagos públicos a veces llegan tarde.</li>
  <li><strong>Agroalimentarias y exportadoras:</strong> adelantan la campaña y cobran después.</li>
  <li><strong>Distribución y mayoristas:</strong> mucho dinero inmovilizado en almacén y en facturas pendientes de cobro.</li>
  <li><strong>Construcción e instaladoras:</strong> certifican la obra y cobran meses después.</li>
  <li><strong>Empresas en fuerte crecimiento:</strong> cuanto más venden, más circulante necesitan.</li>
</ul>

<h2>Cómo justificar la necesidad de circulante</h2>
<p>El ICO tiene que entender por qué la empresa necesita ese dinero y cómo lo va a devolver. Una solicitud sólida incluye:</p>
<ol class="pasos-guia">
  <li><strong>El ciclo de la empresa:</strong> cuántos días tarda en cobrar a sus clientes y en pagar a sus proveedores, y cuánto stock necesita.</li>
  <li><strong>Un plan de tesorería</strong> de 12 a 24 meses, con cobros y pagos mes a mes.</li>
  <li><strong>La relación con el crecimiento:</strong> nuevos clientes, contratos o mercados que explican por qué aumenta la necesidad de circulante.</li>
  <li><strong>La capacidad de devolución:</strong> cómo los resultados de la empresa permiten pagar las cuotas a partir del segundo año.</li>
</ol>

<h2>Errores que conviene evitar</h2>
<ul>
  <li>Pedir circulante para tapar pérdidas continuadas: el ICO busca empresas viables con un proyecto de crecimiento.</li>
  <li>Pedir un importe que no se corresponde con el tamaño de la empresa ni con su ciclo de cobros y pagos.</li>
  <li>Presentar un plan de tesorería que no cuadra con las cuentas y los impuestos.</li>
</ul>

<h2>Requisitos</h2>
<p>Son los mismos que para inversión: pyme con actividad en España, al menos 4 años de antigüedad y cuentas auditadas de los dos últimos ejercicios o un aval público. Si tus cuentas no están auditadas, lee la guía del <a href="../aval-sgr/">aval de SGR</a>. Tienes todas las condiciones en la guía de <a href="../ico-crecimiento/">ICO Crecimiento</a>.</p>
""",
faqs=[
("¿ICO Crecimiento financia circulante?", "Sí. Además de inversiones, financia necesidades de circulante, con un plazo de hasta 5 años, hasta 1 año de carencia y hasta el 100 % de la necesidad."),
("¿Qué plazo tiene ICO Crecimiento para circulante?", "Hasta 5 años, con hasta 1 año de carencia en el que solo se pagan intereses. Para inversión el plazo llega a 10 años con hasta 2 de carencia."),
("¿Cuánto circulante puedo pedir con ICO Crecimiento?", "Desde 50.000 € y hasta el 100 % de la necesidad de circulante que la empresa pueda justificar con su ciclo de cobros y pagos y su plan de tesorería."),
("¿Sustituye a la póliza de crédito del banco?", "No necesariamente. Es un complemento: aporta financiación a más largo plazo y deja libres las líneas del banco para el día a día."),
],
))

ORDEN = ["ico-crecimiento", "ico-crecimiento-circulante", "aval-sgr", "documentacion-prestamo-ico", "como-solicitar-un-prestamo-ico"]
GUIAS.sort(key=lambda g: ORDEN.index(g["slug"]))

# ---------------------------------------------------------------- plantilla
LOGO = '''<svg class="logo" viewBox="0 0 560 160" aria-hidden="true">
        <g transform="translate(24 38) scale(1.3)">
          <path d="M30 4 L30 46 L6 46 Q14 22 30 4 Z" fill="#F3EEE4"/>
          <path d="M35 13 L35 46 L57 46 Q52 26 35 13 Z" fill="#D9774C"/>
          <path d="M4 54 Q18 48 32 54 T60 54" fill="none" stroke="#F3EEE4" stroke-width="3" stroke-linecap="round"/>
        </g>
        <text class="name" x="122" y="98" fill="#F3EEE4">Ítaca</text>
        <text class="tag" x="124" y="124" fill="#F3EEE4">CRECIMIENTO</text>
      </svg>'''

def strip(s):
    return html.unescape(re.sub(r"<[^>]+>", "", s))

def page(depth, url, title, desc, side_current, body, jsonld):
    up = "../" * depth
    CUR = ' aria-current="page"'
    nav = "".join(
        f'<a href="{up}guias/{g["slug"]}/"{CUR if side_current == g["slug"] else ""}>{g["titulo"]}</a>'
        for g in GUIAS
    )
    hub_cur = ' aria-current="page"' if side_current == "hub" else ""
    ld = "\n".join(
        f'<script type="application/ld+json">\n{json.dumps(j, ensure_ascii=False, indent=2)}\n</script>' for j in jsonld
    )
    return f'''<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="article">
<meta property="og:site_name" content="Ítaca Crecimiento">
<meta property="og:locale" content="es_ES">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/assets/og-image.jpg">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" type="image/svg+xml" href="{up}assets/logo/itaca-icono.svg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@600&family=Manrope:wght@500&family=Schibsted+Grotesk:wght@400;500;600&display=swap">
<link rel="stylesheet" href="{up}assets/legal.css">
<link rel="stylesheet" href="{up}assets/guias.css">
{ld}
</head>
<body>

<header class="legal-header">
  <div class="inner">
    <a href="{up}" aria-label="Ítaca Crecimiento, volver al inicio">
      {LOGO}
    </a>
    <a class="back" href="{up}#contacto">Solicitar ICO Crecimiento →</a>
  </div>
</header>

<main class="legal">
  <aside class="legal-side">
    <p class="eyebrow">Guías ICO</p>
    <nav class="legal-nav" aria-label="Guías"><a href="{up}guias/"{hub_cur}>Todas las guías</a>{nav}<a href="{up}blog/">Blog →</a></nav>
  </aside>
  <article class="legal-body">
{body}
  </article>
</main>

<footer class="legal-footer">
  <div class="inner">
    <span>© 2026 Ítaca Crecimiento · Consultoría independiente. No somos una entidad financiera ni formamos parte del ICO.</span>
    <nav aria-label="Legal"><a href="{up}">Inicio</a><a href="{up}blog/">Blog</a><a href="{up}aviso-legal.html">Aviso legal</a><a href="{up}privacidad.html">Privacidad</a><a href="{up}cookies.html">Cookies</a></nav>
  </div>
</footer>

</body>
</html>
'''

ORG = {"@type": "ProfessionalService", "@id": f"{SITE}/#empresa", "name": "Ítaca Crecimiento", "url": f"{SITE}/"}
PERSON = {"@type": "Person", "name": AUTOR, "worksFor": {"@id": f"{SITE}/#empresa"}}

CTA = '''
    <aside class="cta">
      <h2>¿Quieres solicitar ICO Crecimiento?</h2>
      <p>Comprobamos si tu empresa cumple los requisitos de ICO Crecimiento, preparamos el expediente completo y te acompañamos en la solicitud en ICO Online hasta la firma.</p>
      <a class="btn" href="{up}#contacto">Comprobar si mi empresa puede pedirlo</a>
    </aside>'''

for g in GUIAS:
    url = f"{SITE}/guias/{g['slug']}/"
    faq_html = "".join(f"\n    <h3>{q}</h3>\n    <p>{a}</p>" for q, a in g["faqs"])
    body = f'''    <p class="breadcrumb"><a href="../../">Inicio</a><span aria-hidden="true">/</span><a href="../">Guías</a><span aria-hidden="true">/</span>{g["titulo"]}</p>
    <h1>{g["titulo"]}</h1>
    <p class="byline">Por <strong>{AUTOR}</strong>, Ítaca Crecimiento · Actualizado el <time datetime="{FECHA_ISO}">{FECHA}</time></p>
    <div class="resumen">
      <p class="eyebrow">En resumen</p>
      {g["resumen"]}
    </div>
{g["cuerpo"]}
    <h2>Preguntas frecuentes</h2>
    <div class="faq-guia">{faq_html}
    </div>
{CTA.format(up="../../")}'''
    jsonld = [
        {"@context": "https://schema.org", "@type": "Article", "headline": g["titulo"], "description": g["desc"],
         "datePublished": FECHA_ISO, "dateModified": FECHA_ISO, "inLanguage": "es-ES",
         "author": PERSON, "publisher": ORG, "mainEntityOfPage": url, "image": f"{SITE}/assets/og-image.jpg"},
        {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in g["faqs"]]},
        {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Inicio", "item": f"{SITE}/"},
            {"@type": "ListItem", "position": 2, "name": "Guías", "item": f"{SITE}/guias/"},
            {"@type": "ListItem", "position": 3, "name": g["titulo"], "item": url}]},
    ]
    os.makedirs(f"{ROOT}/guias/{g['slug']}", exist_ok=True)
    with open(f"{ROOT}/guias/{g['slug']}/index.html", "w") as fh:
        fh.write(page(2, url, f"{g['seo']} | Ítaca Crecimiento", g["desc"], g["slug"], body, jsonld))

# hub
items = "".join(
    f'\n      <li><h2><a href="{g["slug"]}/">{g["titulo"]}</a></h2><p>{g["desc"]}</p></li>' for g in GUIAS)
hub_body = f'''    <p class="breadcrumb"><a href="../">Inicio</a><span aria-hidden="true">/</span>Guías</p>
    <h1>Guías sobre ICO Crecimiento y préstamos ICO</h1>
    <p class="lead">Explicaciones claras sobre ICO Crecimiento, el préstamo directo del ICO para pymes, y sobre cómo se piden los préstamos ICO: requisitos, documentación y pasos. Escritas por {AUTOR}, de Ítaca Crecimiento.</p>
    <ul class="guia-list">{items}
    </ul>
{CTA.format(up="../")}'''
hub_url = f"{SITE}/guias/"
hub_ld = [{"@context": "https://schema.org", "@type": "CollectionPage", "name": "Guías sobre ICO Crecimiento y préstamos ICO",
           "url": hub_url, "inLanguage": "es-ES", "publisher": ORG,
           "hasPart": [{"@type": "Article", "headline": g["titulo"], "url": f"{SITE}/guias/{g['slug']}/"} for g in GUIAS]}]
with open(f"{ROOT}/guias/index.html", "w") as fh:
    fh.write(page(1, hub_url, "Guías sobre ICO Crecimiento y préstamos ICO | Ítaca Crecimiento",
                  "Guías prácticas sobre ICO Crecimiento, el préstamo directo del ICO para pymes: requisitos, documentación y cómo solicitarlo en ICO Online.",
                  "hub", hub_body, hub_ld))

print("\n".join(f"guias/{g['slug']}/" for g in GUIAS))
