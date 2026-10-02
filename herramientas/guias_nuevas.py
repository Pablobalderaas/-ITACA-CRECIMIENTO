"""Guías añadidas en octubre de 2026: cuestionario ASG, ICO Crecimiento DANA,
circulante por sector y novedades. Se cargan desde gen_guias.py."""

NOTA_DCG = '<p class="note">Elaborado a partir del Documento de Condiciones Generales (DCG) de la línea ICO Crecimiento publicado por el ICO. Las condiciones pueden cambiar y, en caso de duda, prevalece el texto oficial: compruébalo siempre en <a href="https://www.ico.es" rel="noopener">www.ico.es</a> antes de solicitar.</p>'

NUEVAS = []

# ---------------------------------------------------------------- cuestionario ASG
NUEVAS.append(dict(
slug="cuestionario-sostenibilidad-ico-crecimiento",
titulo="El cuestionario de sostenibilidad (ASG) de ICO Crecimiento",
seo="Cuestionario de sostenibilidad ASG de ICO Crecimiento: puntuación y plan de remediación",
desc="Toda solicitud de ICO Crecimiento incluye un cuestionario de sostenibilidad que el ICO puntúa de 0 a 6. Qué evalúa, qué pasa si sacas menos de 2 puntos y cuánto puede costar.",
resumen="""<p>Toda solicitud de ICO Crecimiento lleva un <strong>cuestionario de sostenibilidad</strong> sobre aspectos ambientales, sociales y de gobierno de la empresa (ASG).</p>
<ul>
  <li>El ICO lo puntúa de <strong>0 a 6 puntos</strong> con un sistema interno y lo tiene en cuenta al analizar la operación.</li>
  <li>Si la empresa saca <strong>menos de 2 puntos</strong>, el contrato incluye un <strong>Plan de Remediación</strong> con mejoras concretas.</li>
  <li>Hay <strong>24 meses</strong> desde la firma para acreditar esas mejoras.</li>
  <li>Si no se acreditan, se aplica una comisión adicional del <strong>0,25 % anual sobre el importe firmado</strong> durante el resto del préstamo.</li>
</ul>""",
cuerpo=NOTA_DCG + """

<h2>Qué es y dónde aparece</h2>
<p>La memoria técnica que acompaña a la solicitud de ICO Crecimiento tiene un apartado de <strong>información de sostenibilidad</strong>: una serie de preguntas sobre cómo trabaja la empresa en tres dimensiones, la ambiental, la social y la de gobierno corporativo (lo que se conoce como criterios ASG o, en inglés, ESG).</p>
<p>Con esas respuestas, el ICO aplica un sistema interno de puntuación (<em>scoring</em>) que da un resultado de 0 a 6 puntos. La evaluación de sostenibilidad forma parte de los aspectos que el ICO analiza antes de aprobar la financiación, junto con la solvencia, la viabilidad del proyecto y el resto de requisitos.</p>

<h2>Qué pasa según la puntuación</h2>
<div class="table-wrap">
<table>
  <thead><tr><th>Puntuación</th><th>Consecuencia</th></tr></thead>
  <tbody>
    <tr><td>2 puntos o más</td><td>Ninguna obligación adicional por este motivo</td></tr>
    <tr><td>Menos de 2 puntos</td><td>El ICO fija un Plan de Remediación, que se incorpora al contrato de préstamo</td></tr>
    <tr><td>Menos de 2 puntos y, a los 24 meses, mejoras acreditadas</td><td>Sin penalización</td></tr>
    <tr><td>Menos de 2 puntos y, a los 24 meses, sin mejoras acreditadas</td><td>Comisión adicional de 25 puntos básicos (0,25 %) anual sobre el nominal firmado, cobrada mes a mes</td></tr>
  </tbody>
</table>
</div>
<p>El Plan de Remediación señala los aspectos concretos en los que la empresa podría mejorar en una o varias de las tres dimensiones. Pasados los 24 meses, el ICO hace una revisión de seguimiento con la documentación que haya enviado la empresa.</p>

<h2>Cuánto puede costar no cumplirlo</h2>
<p>La comisión se calcula sobre el <strong>importe firmado</strong>, no sobre lo que quede pendiente, y se aplica desde el mes siguiente a la comunicación del resultado del seguimiento. Por ejemplo, en un préstamo de 500.000 € serían unos 1.250 € al año. En un préstamo de inversión a 10 años, eso puede sumar bastante.</p>
<p>Además, el seguimiento del préstamo incluye comprobar los avances en sostenibilidad: no es un trámite que se responda y se olvide.</p>

<h2>Qué tipo de aspectos se valoran</h2>
<p>Las preguntas concretas las fija el ICO en el formulario de la solicitud. A modo orientativo, estos son los temas que suelen entrar en cada dimensión en este tipo de evaluaciones:</p>
<h3>Ambiental</h3>
<ul>
  <li>Control y reducción del consumo de energía y agua.</li>
  <li>Uso de energías renovables, por ejemplo placas solares de autoconsumo.</li>
  <li>Gestión de residuos y reciclaje.</li>
  <li>Certificaciones ambientales, como la ISO 14001, o el cálculo de la huella de carbono.</li>
</ul>
<h3>Social</h3>
<ul>
  <li>Prevención de riesgos laborales y salud de la plantilla.</li>
  <li>Estabilidad del empleo y formación del equipo.</li>
  <li>Igualdad y conciliación. El plan de igualdad es obligatorio para las empresas de 50 o más trabajadores.</li>
  <li>Relación con el entorno y la comunidad local.</li>
</ul>
<h3>Gobierno corporativo</h3>
<ul>
  <li>Código ético o de conducta.</li>
  <li>Canal de denuncias. Es obligatorio para las empresas de 50 o más trabajadores desde la Ley 2/2023.</li>
  <li>Cumplimiento normativo y protección de datos.</li>
  <li>Criterios para elegir y evaluar a los proveedores.</li>
</ul>

<h2>El error más habitual: no tenerlo por escrito</h2>
<p>Muchas pymes hacen bastantes de estas cosas, pero no las tienen documentadas: miden el consumo eléctrico pero no lo registran, forman a su equipo pero no tienen un plan, o eligen a los proveedores con criterio pero sin una política escrita. En un cuestionario que luego se puede comprobar, lo que no se puede acreditar es difícil de defender.</p>
<p>Por eso conviene revisar la situación de la empresa <strong>antes</strong> de presentar la solicitud. A veces, poner por escrito lo que ya se hace basta para cambiar la puntuación. Y si hay que hacer mejoras, es mejor saberlo con tiempo.</p>

<h2>Responde con exactitud</h2>
<p>La solicitud incluye una declaración responsable de que todos los datos son ciertos, y el ICO puede comprobarlos. Inflar las respuestas no compensa: la puntuación queda vinculada al contrato y se revisa durante el seguimiento del préstamo.</p>
""",
faqs=[
("¿Qué es el cuestionario de sostenibilidad de ICO Crecimiento?", "Es un apartado de la memoria técnica de la solicitud con preguntas sobre los aspectos ambientales, sociales y de gobierno de la empresa (ASG). El ICO lo puntúa de 0 a 6 con un sistema interno."),
("¿Qué pasa si saco menos de 2 puntos en sostenibilidad?", "El contrato de préstamo incluirá un Plan de Remediación con mejoras concretas. La empresa tiene 24 meses desde la firma para acreditarlas. Si no lo hace, se aplica una comisión adicional del 0,25 % anual sobre el importe firmado."),
("¿El cuestionario ASG puede hacer que me denieguen el préstamo?", "La evaluación de sostenibilidad forma parte del análisis del ICO, pero una puntuación baja no supone por sí sola la denegación: el DCG prevé para ese caso un Plan de Remediación incorporado al contrato."),
("¿Cuánto cuesta la penalización por sostenibilidad?", "25 puntos básicos (0,25 %) anuales sobre el nominal firmado, cobrados mes a mes desde el mes siguiente a la comunicación del resultado del seguimiento. En un préstamo de 500.000 € son unos 1.250 € al año."),
],
))

# ---------------------------------------------------------------- DANA
NUEVAS.append(dict(
slug="ico-crecimiento-dana",
titulo="ICO Crecimiento DANA: financiación para empresas afectadas por la DANA",
seo="ICO Crecimiento DANA: aval del 80 %, requisitos y condiciones",
desc="ICO Crecimiento DANA es la modalidad de ICO Crecimiento para empresas de los municipios afectados por la DANA de 2024: aval público gratuito del 80 %, sin comisiones y con posibilidad de intereses subvencionados.",
resumen="""<p><strong>ICO Crecimiento DANA</strong> es una modalidad de ICO Crecimiento para empresas afectadas por la DANA de octubre y noviembre de 2024. Incorpora directamente un <strong>aval público</strong> del programa de avales del Real Decreto-ley 6/2024.</p>
<ul>
  <li>Aval del Estado del <strong>80 % del principal</strong>, <strong>sin coste</strong> para la empresa.</li>
  <li><strong>Sin comisión de apertura ni de cancelación.</strong></li>
  <li>Hasta <strong>5 años</strong> para circulante y hasta <strong>7 años</strong> para renovación de activos e inversiones (hasta 10 en el sector agrícola).</li>
  <li><strong>12 meses de carencia</strong>, ampliables hasta 12 más si el proyecto lo requiere.</li>
  <li>Hasta <strong>12,5 millones de euros</strong> por empresa.</li>
  <li>Un tramo con <strong>intereses subvencionados</strong> (coste del 0 %) para préstamos de circulante de pymes, según disponibilidad presupuestaria.</li>
</ul>""",
cuerpo=NOTA_DCG + """

<h2>Qué es ICO Crecimiento DANA</h2>
<p>La DANA que empezó el 27 de octubre de 2024 provocó graves inundaciones en la Comunitat Valenciana y, en menor medida, en Castilla-La Mancha, Andalucía, Illes Balears, Cataluña y Aragón. Para ayudar a las empresas afectadas, el Real Decreto-ley 6/2024, de 5 de noviembre, creó una línea de avales públicos gestionada por el ICO, con varias modalidades.</p>
<p>La tercera, de <strong>recuperación de la capacidad productiva de las empresas</strong>, se aplica directamente a ICO Crecimiento. Para facilitar el acceso, el ICO ha creado dentro de esta línea una marca específica, ICO Crecimiento DANA, que lleva ya incorporado ese aval público como garantía.</p>

<h2>Qué se puede financiar</h2>
<ul>
  <li><strong>Renovación de activos dañados</strong> por la DANA.</li>
  <li><strong>Otras inversiones</strong> que permitan ampliar, mejorar o diversificar el establecimiento afectado o su proceso de producción.</li>
  <li><strong>Circulante</strong> para cubrir el ciclo de explotación.</li>
  <li><strong>Reposición de medios de transporte</strong> de la actividad que resultaran dañados en alguno de los municipios afectados.</li>
</ul>
<p>Los activos financiados deben quedar vinculados, durante toda la vida del préstamo, a un establecimiento de la empresa situado en uno de los municipios del anexo del Real Decreto-ley 6/2024.</p>
<p><strong>No se admiten</strong> novaciones, renovaciones ni ampliaciones de préstamos que ya existan, ni préstamos nuevos para amortizar anticipadamente otras deudas.</p>

<h2>Quién puede pedirlo</h2>
<ul>
  <li>Empresas con centro de trabajo, domicilio social o establecimiento en alguno de los municipios del anexo del Real Decreto-ley 6/2024 que puedan estimar un perjuicio patrimonial causado por la DANA.</li>
  <li>Empresas cuyos medios de transporte resultaran dañados mientras trabajaban en alguna de esas localidades, aunque no tengan allí su domicilio ni un establecimiento.</li>
</ul>
<p>Además, hay que tener actividad productiva a 29 de octubre de 2024, no tener ningún aval gestionado por el ICO por cuenta del Estado que se haya ejecutado por impago, y no figurar como moroso en la CIRBE en la fecha de firma.</p>
<p>Al tratarse de una modalidad de ICO Crecimiento, siguen aplicándose los requisitos generales de la línea: sociedad pyme, antigüedad, resultados, rating y el resto. Los repasamos en la guía de <a href="../ico-crecimiento/">ICO Crecimiento</a>.</p>

<h2>Condiciones</h2>
<dl class="data-list">
  <div><dt>Aval</dt><dd>Aval público del 80 % del principal. Solo cubre el capital, no los intereses ni las comisiones</dd></div>
  <div><dt>Coste del aval</dt><dd>Ninguno: los avales de este programa no se cobran</dd></div>
  <div><dt>Importe máximo</dt><dd>Depende de la finalidad, el plazo y el régimen de ayudas aplicable, con un tope de 12,5 millones de euros por empresa</dd></div>
  <div><dt>Plazo</dt><dd>Hasta 5 años para circulante y hasta 7 años para renovación de activos e inversiones. En el sector agrícola, las inversiones pueden llegar a 10 años</dd></div>
  <div><dt>Carencia</dt><dd>12 meses de carencia de principal, ampliables hasta 12 meses más si el proyecto de inversión lo requiere, sin alargar el vencimiento</dd></div>
  <div><dt>Comisiones</dt><dd>Sin comisión de apertura ni de cancelación</dd></div>
</dl>

<h2>El tramo con intereses subvencionados</h2>
<p>El Consejo de Ministros de 3 de diciembre de 2024 aprobó un tramo específico del programa de avales en el que el Estado subvenciona la totalidad de los intereses, de modo que la empresa paga un <strong>0 %</strong>. Sus condiciones principales son:</p>
<ul>
  <li>Hasta 240 millones de euros en avales, equivalentes a 300 millones en préstamos.</li>
  <li>Solo para <strong>pymes</strong> que no pertenezcan a los sectores agrícola, ganadero o de pesca y acuicultura.</li>
  <li>Solo para préstamos de <strong>circulante</strong>, a tipo fijo y con amortización de cuota constante (sistema francés).</li>
  <li>El tipo de interés antes de la subvención no puede superar el 5 % nominal anual. Si lo supera, la operación no entra en este tramo, aunque puede ir a otros tramos del programa.</li>
  <li>Depende de que quede <strong>presupuesto</strong> disponible.</li>
</ul>
<p>La subvención queda condicionada a cumplir los requisitos del tramo, las normas de ayudas de Estado y el contrato. Si se incumplen, hay que devolverla.</p>

<h2>Documentación adicional</h2>
<p>Además de la documentación general de ICO Crecimiento, hay que aportar:</p>
<ol class="pasos-guia">
  <li>Una <strong>declaración responsable</strong> de que se cumplen las condiciones de esta modalidad, según el modelo del ICO.</li>
  <li>La <strong>acreditación del domicilio o del establecimiento</strong> en un municipio afectado: cuentas anuales, domicilio fiscal en la Agencia Tributaria, centro de trabajo dado de alta en la Seguridad Social u otro medio válido.</li>
  <li>Si se trata de vehículos dañados, el <strong>certificado del Consorcio de Compensación de Seguros</strong> que reconoce el daño.</li>
</ol>

<h2>¿Sigue disponible?</h2>
<p>La modalidad figura en el DCG vigente de ICO Crecimiento, pero el tramo con intereses subvencionados depende del presupuesto que quede. Antes de preparar la solicitud, conviene confirmar con el ICO que sigue habiendo fondos. En el estudio gratuito lo comprobamos por ti.</p>
""",
faqs=[
("¿Qué es ICO Crecimiento DANA?", "Es una modalidad de la línea ICO Crecimiento para empresas afectadas por la DANA de 2024, que incorpora directamente un aval público gratuito del 80 % del principal, sin comisión de apertura ni de cancelación."),
("¿Quién puede pedir ICO Crecimiento DANA?", "Empresas con domicilio, centro de trabajo o establecimiento en alguno de los municipios del anexo del Real Decreto-ley 6/2024 que hayan sufrido un perjuicio patrimonial por la DANA, y empresas cuyos vehículos resultaran dañados trabajando en esas localidades. Además tienen que cumplir los requisitos generales de ICO Crecimiento."),
("¿Qué plazo tiene ICO Crecimiento DANA?", "Hasta 5 años para circulante y hasta 7 años para renovación de activos e inversiones, o hasta 10 en el sector agrícola. Incluye 12 meses de carencia, ampliables hasta 12 más si el proyecto lo requiere."),
("¿ICO Crecimiento DANA tiene intereses gratis?", "Existe un tramo con intereses subvencionados en su totalidad, de modo que la empresa paga un 0 %. Es solo para préstamos de circulante de pymes no agrícolas, ganaderas ni pesqueras, con un tipo previo no superior al 5 %, y depende de la disponibilidad presupuestaria."),
("¿Se puede usar ICO Crecimiento DANA para refinanciar deudas?", "No. Esta modalidad no admite novaciones, renovaciones ni ampliaciones de préstamos existentes, ni préstamos nuevos destinados a amortizar anticipadamente otras deudas."),
],
))

# ---------------------------------------------------------------- sectores
SECTOR_INTRO = '<p class="note">Esta página aplica las condiciones generales de <a href="../ico-crecimiento-circulante/">ICO Crecimiento para circulante</a> a un sector concreto. Los ejemplos son orientativos. Las condiciones vigentes son las que publica el ICO en <a href="https://www.ico.es" rel="noopener">www.ico.es</a>.</p>'

NUEVAS.append(dict(
grupo="sector",
slug="circulante-empresas-agroalimentarias",
corto="Agroalimentarias",
titulo="ICO Crecimiento para empresas agroalimentarias: financiar la campaña",
seo="ICO Crecimiento para empresas agroalimentarias: circulante para la campaña",
desc="Cómo usar ICO Crecimiento en una empresa agroalimentaria: financiar la campaña, el stock y los cobros a clientes a 5 años con 1 de carencia, sin pasar por el banco.",
resumen="""<p>En el sector agroalimentario el dinero sale de golpe, en la campaña, y vuelve poco a poco, a medida que se vende. <strong>ICO Crecimiento para circulante</strong> permite financiar ese desfase:</p>
<ul>
  <li>Hasta <strong>5 años</strong> con <strong>1 de carencia</strong> y hasta el <strong>100 %</strong> de la necesidad, desde 50.000 €.</li>
  <li>Sirve para pagar la materia prima de la campaña, mantener el stock y financiar a los clientes.</li>
  <li>Se puede combinar con un préstamo de <strong>inversión</strong>: cámaras frigoríficas, líneas de envasado o placas solares.</li>
  <li>Exige ser una <strong>sociedad mercantil</strong> pyme con al menos 4 años. Las cooperativas y SAT deben revisar si encajan.</li>
</ul>""",
cuerpo=SECTOR_INTRO + """

<h2>El problema: la campaña se paga antes de venderse</h2>
<p>Una almazara, una central hortofrutícola, una bodega o una industria cárnica comparten el mismo patrón: la materia prima llega en pocas semanas y hay que pagarla al productor, pero la venta del producto se reparte a lo largo de muchos meses. A eso se suman los clientes, sobre todo la gran distribución y los compradores extranjeros, que pagan a 60 o 90 días.</p>
<p>El resultado es una necesidad de circulante muy alta en unos meses concretos del año, que el banco suele cubrir con pólizas de un año y que hay que renegociar en cada campaña.</p>

<h2>Cómo encaja ICO Crecimiento</h2>
<ul>
  <li><strong>Plazo largo para una necesidad recurrente:</strong> hasta 5 años, en lugar de renovar la póliza cada campaña.</li>
  <li><strong>Un año de carencia:</strong> durante el primer año solo se pagan intereses, lo que da margen para cerrar la campaña y cobrar.</li>
  <li><strong>Hasta el 100 %</strong> de la necesidad de circulante justificada.</li>
  <li><strong>Las líneas del banco quedan libres</strong> para los picos de cada temporada.</li>
</ul>
<p>Un detalle práctico: el préstamo de circulante se desembolsa <strong>de una sola vez</strong>, en los 15 días siguientes a la firma. Por eso conviene calcular bien el calendario y presentar la solicitud con antelación a la campaña.</p>

<h2>Ejemplo orientativo</h2>
<p>Una almazara compra aceituna por valor de 900.000 € entre noviembre y enero y vende el aceite a lo largo del año, con clientes que pagan a 60 días. En el peor momento, tiene inmovilizados unos 600.000 € entre existencias y facturas pendientes de cobro. Con ICO Crecimiento podría financiar una parte estable de esa necesidad a 5 años y dejar la póliza del banco solo para los picos de la campaña.</p>

<h2>Inversión y circulante a la vez</h2>
<p>Muchas empresas del sector combinan las dos finalidades en la misma solicitud: por ejemplo, una nueva cámara frigorífica o una línea de envasado (inversión, hasta 10 años y hasta el 80 %) y el circulante que esa mayor capacidad necesita (hasta 5 años y hasta el 100 %). También se financian instalaciones de renovables para autoconsumo y la apertura de nuevos mercados de exportación.</p>

<h2>Lo que conviene revisar antes</h2>
<ul>
  <li><strong>La forma jurídica.</strong> La línea exige una sociedad mercantil. Si la empresa es una cooperativa o una SAT, hay que revisar si encaja antes de preparar nada.</li>
  <li><strong>La actividad.</strong> No es lo mismo transformar y comercializar que la producción agrícola primaria: el régimen de ayudas de <em>minimis</em> que se aplica, y su límite, pueden ser distintos. Hay que declarar las ayudas recibidas en los tres últimos años.</li>
  <li><strong>La estacionalidad en las cuentas.</strong> Un balance cerrado en plena campaña puede dar una imagen distinta a uno cerrado tras la venta. Conviene explicarlo en la solicitud.</li>
  <li><strong>Los resultados.</strong> Un mal año por sequía o heladas puede dejar pérdidas. La línea no admite pérdidas en los dos últimos ejercicios ni patrimonio neto negativo.</li>
</ul>
<p>Si la empresa está en un municipio afectado por la DANA de 2024, revisa también la modalidad <a href="../ico-crecimiento-dana/">ICO Crecimiento DANA</a>, que permite hasta 10 años en inversiones agrícolas.</p>
""",
faqs=[
("¿Puede una empresa agroalimentaria pedir ICO Crecimiento para la campaña?", "Sí, si es una sociedad mercantil pyme con al menos 4 años y cumple los requisitos. El circulante de la campaña se puede financiar hasta 5 años, con 1 de carencia y hasta el 100 % de la necesidad justificada."),
("¿Una cooperativa agraria puede pedir ICO Crecimiento?", "La línea está dirigida a sociedades mercantiles, así que una cooperativa o una SAT debe revisar si encaja antes de preparar la solicitud. Lo comprobamos en el estudio gratuito."),
("¿Se pueden financiar cámaras frigoríficas o placas solares?", "Sí, como inversión: hasta el 80 % y hasta 10 años con 2 de carencia. Se pueden combinar con circulante en la misma solicitud."),
],
))

NUEVAS.append(dict(
grupo="sector",
slug="circulante-distribucion-mayoristas",
corto="Distribución y mayoristas",
titulo="ICO Crecimiento para distribuidores y mayoristas",
seo="ICO Crecimiento para distribución y mayoristas: financiar stock y clientes",
desc="Para un distribuidor, crecer exige más stock y más crédito a clientes. Cómo financiarlo con ICO Crecimiento a 5 años, con 1 de carencia y hasta el 100 % de la necesidad.",
resumen="""<p>En la distribución, el circulante crece con las ventas: más clientes significan más stock en almacén y más facturas pendientes de cobro. <strong>ICO Crecimiento para circulante</strong> financia ese crecimiento:</p>
<ul>
  <li>Hasta <strong>5 años</strong> con <strong>1 de carencia</strong> y hasta el <strong>100 %</strong> de la necesidad, desde 50.000 €.</li>
  <li>Sirve para existencias, financiación a clientes y para <strong>cancelar deuda a corto plazo</strong> con proveedores o bancos.</li>
  <li>Se pide directamente al ICO y no consume las líneas del banco.</li>
</ul>""",
cuerpo=SECTOR_INTRO + """

<h2>Por qué un distribuidor que vende más necesita más dinero</h2>
<p>Un mayorista compra, almacena y vende con márgenes ajustados. Entre que paga al proveedor y cobra al cliente pasan semanas o meses, y ese dinero lo adelanta la empresa. Cuando entra un cliente grande o una nueva referencia, la necesidad de circulante sube de golpe, mucho antes de que lleguen los beneficios.</p>

<h2>Ejemplo orientativo</h2>
<p>Un distribuidor factura 6 millones de euros al año y compra mercancía por 4,8 millones. Cobra a sus clientes a 60 días, mantiene 45 días de stock y paga a sus proveedores a 30 días:</p>
<dl class="data-list">
  <div><dt>Clientes</dt><dd>60 días de ventas: unos 986.000 €</dd></div>
  <div><dt>Existencias</dt><dd>45 días de compras: unos 592.000 €</dd></div>
  <div><dt>Proveedores</dt><dd>30 días de compras: unos 395.000 € que financia el proveedor</dd></div>
  <div><dt>Necesidad de circulante</dt><dd>Unos 1,18 millones de euros</dd></div>
</dl>
<p>Si las ventas crecen un 20 %, esa necesidad sube en unos 235.000 €. Esa es exactamente la cifra que hay que justificar ante el ICO, y que puede financiarse a 5 años en lugar de tensionar la póliza.</p>

<h2>Usos habituales en distribución</h2>
<ul>
  <li><strong>Ampliar stock</strong> para dar servicio a nuevos clientes o referencias.</li>
  <li><strong>Financiar a clientes</strong> que exigen plazos de pago más largos.</li>
  <li><strong>Aprovechar descuentos por pronto pago</strong> o compras por volumen a los proveedores.</li>
  <li><strong>Cancelar deuda a corto plazo</strong> y pasarla a un plazo más largo y ordenado.</li>
  <li>Junto con un préstamo de <strong>inversión</strong>: una nave o la ampliación del almacén, estanterías, carretillas o un software de gestión de almacén.</li>
</ul>

<h2>Lo que conviene revisar antes</h2>
<ul>
  <li><strong>Los vehículos.</strong> ICO Crecimiento no financia los vehículos de transporte de mercancías por carretera. Si la flota de reparto es una parte importante del proyecto, hay que revisarlo con cuidado.</li>
  <li><strong>El margen.</strong> Con márgenes bajos, el ICO mirará con atención la capacidad de devolución: hay que demostrar que el crecimiento genera caja suficiente para pagar las cuotas a partir del segundo año.</li>
  <li><strong>La concentración de clientes.</strong> Si uno o dos clientes suponen buena parte de las ventas, conviene explicarlo y mostrar su solvencia.</li>
  <li><strong>La coherencia de las cifras.</strong> Los días de cobro, pago y stock que se declaren tienen que cuadrar con el balance y la cuenta de resultados.</li>
</ul>
""",
faqs=[
("¿ICO Crecimiento financia stock y existencias?", "Sí. La inversión en existencias es una de las necesidades de circulante que financia la línea, hasta 5 años, con 1 de carencia y hasta el 100 % de la necesidad justificada."),
("¿Puedo cancelar la póliza del banco con ICO Crecimiento?", "La línea permite destinar el circulante a cancelar deuda a corto plazo, tanto comercial como financiera. Conviene estudiar si interesa cancelarla o mantenerla para los picos."),
("¿ICO Crecimiento financia furgonetas o camiones de reparto?", "Los vehículos de transporte de mercancías por carretera están excluidos. Otros vehículos industriales de la actividad sí pueden financiarse como inversión, así que hay que revisarlo caso por caso."),
],
))

NUEVAS.append(dict(
grupo="sector",
slug="circulante-construccion-instaladoras",
corto="Construcción e instaladoras",
titulo="ICO Crecimiento para constructoras e instaladoras",
seo="ICO Crecimiento para construcción e instaladoras: financiar obra y certificaciones",
desc="Constructoras e instaladoras adelantan materiales y mano de obra y cobran meses después. Cómo financiarlo con ICO Crecimiento a 5 años con 1 de carencia.",
resumen="""<p>En la construcción y las instalaciones se trabaja primero y se cobra después: materiales, subcontratas y nóminas se pagan antes de certificar y cobrar la obra. <strong>ICO Crecimiento para circulante</strong> financia ese desfase:</p>
<ul>
  <li>Hasta <strong>5 años</strong> con <strong>1 de carencia</strong> y hasta el <strong>100 %</strong> de la necesidad, desde 50.000 €.</li>
  <li>Útil para acopio de materiales, retenciones de garantía y cobros lentos, también de la Administración.</li>
  <li>Se puede combinar con <strong>inversión</strong> en maquinaria, herramientas o una nave.</li>
</ul>""",
cuerpo=SECTOR_INTRO + """

<h2>Dónde se queda atrapado el dinero</h2>
<ul>
  <li><strong>Entre la ejecución y la certificación:</strong> la obra avanza durante el mes y se certifica al final.</li>
  <li><strong>Entre la certificación y el cobro:</strong> el cliente o la Administración paga semanas o meses después.</li>
  <li><strong>Las retenciones de garantía:</strong> una parte de cada certificación, a menudo el 5 %, no se cobra hasta el final del periodo de garantía.</li>
  <li><strong>El acopio de materiales:</strong> cuadros eléctricos, paneles solares, equipos de climatización o tubería que hay que comprar antes de empezar.</li>
</ul>
<p>Cuantas más obras simultáneas tiene la empresa, más dinero adelanta. Por eso las constructoras e instaladoras que crecen suelen ir justas de tesorería aunque tengan cartera.</p>

<h2>Ejemplo orientativo</h2>
<p>Una instaladora de climatización y fotovoltaica firma contratos por 1,5 millones de euros para el próximo año. Tiene que comprar equipos por adelantado y cobra a 60 días de cada certificación, con un 5 % retenido hasta la recepción. Para atender esa cartera, necesita unos 300.000 € más de circulante. Con ICO Crecimiento podría financiarlo a 5 años con el primer año solo de intereses, que es justo cuando se ejecutan las obras.</p>

<h2>Cómo encaja ICO Crecimiento</h2>
<ul>
  <li><strong>Plazo largo:</strong> hasta 5 años frente a las pólizas y el descuento de certificaciones a un año.</li>
  <li><strong>Carencia de un año</strong> mientras se ejecuta y cobra la cartera contratada.</li>
  <li><strong>Inversión en la misma solicitud:</strong> maquinaria, herramientas, equipos de medición, una nave o software de gestión de obra, hasta el 80 % y hasta 10 años.</li>
</ul>
<p>Hay que tener en cuenta que ICO Crecimiento es un préstamo: no sustituye a los avales técnicos que piden las licitaciones o los contratos de obra.</p>

<h2>Lo que conviene revisar antes</h2>
<ul>
  <li><strong>La cartera contratada.</strong> Los contratos firmados y las certificaciones pendientes son la mejor justificación de la necesidad de circulante.</li>
  <li><strong>Los resultados.</strong> Una obra con pérdidas puede afectar a todo el ejercicio. La línea no admite pérdidas en los dos últimos ejercicios ni patrimonio neto negativo.</li>
  <li><strong>La CIRBE y las deudas.</strong> Hay que estar al corriente con Hacienda, la Seguridad Social y los bancos, tanto al pedirlo como al firmarlo.</li>
  <li><strong>El riesgo de los clientes.</strong> Trabajar con clientes solventes o con la Administración reduce el riesgo que ve el ICO.</li>
</ul>
""",
faqs=[
("¿Puede una constructora pedir ICO Crecimiento?", "Sí, si es una sociedad mercantil pyme con al menos 4 años, sin pérdidas en los dos últimos ejercicios ni patrimonio neto negativo, y cumple el resto de requisitos. Puede financiar circulante y también inversión."),
("¿ICO Crecimiento sirve como aval para licitaciones?", "No. ICO Crecimiento es un préstamo, no un aval técnico. Puede financiar el circulante que necesitan las obras, pero no sustituye a los avales que piden las licitaciones o los contratos."),
("¿Se puede financiar el acopio de materiales?", "Sí. La compra de materiales y existencias forma parte del circulante que financia la línea, hasta 5 años, con 1 de carencia y hasta el 100 % de la necesidad justificada."),
],
))

NUEVAS.append(dict(
grupo="sector",
slug="circulante-empresas-industriales",
corto="Industria",
titulo="ICO Crecimiento para empresas industriales",
seo="ICO Crecimiento para la industria: financiar producción, maquinaria y circulante",
desc="Una empresa industrial inmoviliza dinero en materia prima, producción en curso y producto terminado. Cómo financiar circulante e inversión con ICO Crecimiento, directamente con el ICO.",
resumen="""<p>En la industria el ciclo es largo: se compra materia prima, se fabrica, se almacena el producto terminado y se cobra al cliente. <strong>ICO Crecimiento</strong> permite financiar ese ciclo y, a la vez, la inversión productiva:</p>
<ul>
  <li><strong>Circulante:</strong> hasta 5 años con 1 de carencia y hasta el 100 % de la necesidad.</li>
  <li><strong>Inversión:</strong> maquinaria, naves, instalaciones, renovables o software, hasta 10 años con 2 de carencia y hasta el 80 %.</li>
  <li>Se pueden financiar inversiones hechas o iniciadas en los <strong>12 meses anteriores</strong> a la solicitud.</li>
</ul>""",
cuerpo=SECTOR_INTRO + """

<h2>Un ciclo largo que consume caja</h2>
<p>Una empresa industrial adelanta dinero en tres fases: la materia prima que compra, la producción en curso y el producto terminado que espera a ser vendido. Después, el cliente paga a 60 o 90 días. Cuanto más largo es el proceso, más circulante necesita. Y cuando entra un pedido grande, hay que comprar y producir mucho antes de cobrar.</p>

<h2>Ejemplo orientativo</h2>
<p>Un fabricante de componentes metálicos gana un contrato anual con un cliente nuevo por 800.000 €. Para servirlo tiene que comprar acero con 90 días de antelación, aumentar la producción y mantener un stock de seguridad. Calcula que necesita 250.000 € más de circulante y, además, una máquina de corte láser de 300.000 €.</p>
<p>Con ICO Crecimiento podría pedir las dos cosas en la misma solicitud: la máquina como inversión (hasta el 80 %, a 10 años con 2 de carencia) y el circulante del contrato (hasta el 100 %, a 5 años con 1 de carencia).</p>

<h2>Qué puede financiar una industria</h2>
<ul>
  <li><strong>Circulante:</strong> materia prima, existencias, financiación a clientes, personal y cancelación de deuda a corto plazo.</li>
  <li><strong>Maquinaria, utillaje e instalaciones</strong> productivas.</li>
  <li><strong>Naves y terrenos</strong> industriales.</li>
  <li><strong>Renovables</strong> para autoconsumo o venta a red.</li>
  <li><strong>Intangibles:</strong> I+D, patentes, software industrial, digitalización y formación del equipo.</li>
  <li>Inversiones realizadas o iniciadas en los <strong>12 meses anteriores</strong> a la solicitud.</li>
</ul>

<h2>Por qué ICO Crecimiento encaja bien en la industria</h2>
<ul>
  <li><strong>Carencia en inversión:</strong> hasta 2 años sin amortizar capital mientras la nueva maquinaria empieza a producir.</li>
  <li><strong>Intangibles incluidos:</strong> el software, la digitalización o la I+D, que a muchos bancos les cuesta financiar, entran en la línea.</li>
  <li><strong>Sin vinculación bancaria:</strong> no hay que contratar productos ni concentrar riesgo con un solo banco.</li>
</ul>

<h2>Lo que conviene revisar antes</h2>
<ul>
  <li><strong>Las ayudas ya recibidas.</strong> Si la empresa ha recibido subvenciones o préstamos públicos para el mismo proyecto, hay que declararlos para respetar los límites de acumulación.</li>
  <li><strong>Los presupuestos de la inversión.</strong> Hacen falta presupuestos o facturas de cada elemento, y después hay que justificar los pagos.</li>
  <li><strong>El calendario.</strong> En inversión, los desembolsos pueden hacerse por partes, pero deben completarse antes de que termine la carencia.</li>
  <li><strong>Las licencias.</strong> Las inversiones que requieran licencia o autorización deben contar con ella.</li>
</ul>
""",
faqs=[
("¿Puede una empresa industrial pedir circulante e inversión a la vez con ICO Crecimiento?", "Sí. La misma solicitud puede incluir una inversión, por ejemplo maquinaria, a hasta 10 años con 2 de carencia y hasta el 80 %, y circulante a hasta 5 años con 1 de carencia y hasta el 100 % de la necesidad."),
("¿ICO Crecimiento financia maquinaria ya comprada?", "Puede financiar inversiones realizadas o iniciadas en los 12 meses anteriores a la solicitud, siempre que se justifiquen con sus facturas."),
("¿Se puede financiar una instalación de placas solares en la fábrica?", "Sí. Las instalaciones de energías renovables para autoconsumo o venta a red están entre las inversiones financiables."),
],
))

# ---------------------------------------------------------------- novedades
NUEVAS.append(dict(
slug="novedades-ico-crecimiento",
titulo="Novedades de ICO Crecimiento",
seo="Novedades de ICO Crecimiento 2026: últimos cambios de la línea",
desc="Los cambios y noticias de la línea ICO Crecimiento ordenados por fecha: lanzamiento, ICO Crecimiento Exportadores, modalidad DANA, cuestionario de sostenibilidad y estado actual de la línea.",
resumen="""<p>Recogemos aquí, por fecha, los cambios relevantes de la línea ICO Crecimiento. A <strong>2 de octubre de 2026</strong>:</p>
<ul>
  <li>La línea sigue <strong>abierta</strong> hasta el 31 de diciembre de 2027 o hasta agotar el presupuesto.</li>
  <li>Las solicitudes se atienden <strong>por orden de presentación</strong>.</li>
  <li>El DCG vigente incluye la <strong>modalidad DANA</strong> y la <strong>evaluación de sostenibilidad</strong> con Plan de Remediación.</li>
</ul>""",
cuerpo="""
<p class="note">Página actualizada periódicamente por Ítaca Crecimiento. Las fuentes son el Documento de Condiciones Generales de la línea y las comunicaciones públicas del ICO y del Gobierno. Comprueba siempre la información vigente en <a href="https://www.ico.es" rel="noopener">www.ico.es</a>.</p>

<h2>Octubre de 2026: situación de la línea</h2>
<p>ICO Crecimiento sigue admitiendo solicitudes. El plazo termina el <strong>31 de diciembre de 2027</strong>, salvo que antes se agote el presupuesto. Si eso ocurre, el ICO publicará en su web la fecha de cierre. Como las solicitudes se atienden por orden de presentación, no conviene esperar al final.</p>
<p>Hemos revisado todas nuestras guías con el DCG vigente. Algunos puntos que a menudo pasan desapercibidos:</p>
<ul>
  <li>El tipo de interés se <strong>revisa cada año</strong> con el Euríbor a un año, y los intereses se pagan mensualmente.</li>
  <li>El capital se devuelve, como regla general, en <strong>cuotas mensuales de capital constantes</strong>, así que la cuota total baja con el tiempo.</li>
  <li>Los requerimientos de documentación del ICO se contestan en <strong>5 días hábiles</strong>. Si no se atienden, o si la notificación electrónica no se abre en ese plazo, la solicitud se da por desistida.</li>
  <li>El ICO exige una calificación crediticia mínima equivalente a <strong>B</strong> en su análisis interno.</li>
  <li>Una solicitud inadmitida o desestimada se puede <strong>volver a presentar</strong> una vez corregidos los defectos.</li>
</ul>

<h2>Evaluación de sostenibilidad y Plan de Remediación</h2>
<p>El DCG vigente incorpora la evaluación de sostenibilidad: el ICO puntúa de 0 a 6 las respuestas del cuestionario ASG de la memoria técnica. Por debajo de 2 puntos se exige un Plan de Remediación con 24 meses para acreditar mejoras; si no se acreditan, se aplica una comisión adicional del 0,25 % anual sobre el importe firmado. Lo explicamos en la guía del <a href="../cuestionario-sostenibilidad-ico-crecimiento/">cuestionario de sostenibilidad</a>.</p>

<h2>Modalidad ICO Crecimiento DANA</h2>
<p>El DCG vigente incluye la marca ICO Crecimiento DANA, para empresas de los municipios afectados por la DANA de 2024. Incorpora el aval público gratuito del 80 % del Real Decreto-ley 6/2024, sin comisiones de apertura ni de cancelación, y un tramo con intereses subvencionados para el circulante de pymes, según disponibilidad presupuestaria. Lo explicamos en la guía de <a href="../ico-crecimiento-dana/">ICO Crecimiento DANA</a>.</p>

<h2>9 de febrero de 2026: ICO Crecimiento Exportadores</h2>
<p>El Gobierno activó la línea <strong>ICO Crecimiento Exportadores</strong>, con 750 millones de euros, para pymes afectadas por los cambios en el entorno arancelario mundial: exportadoras, importadoras y proveedoras de empresas expuestas. Incluye un componente de ayuda de 181 millones de euros de fondos europeos Next Generation, en forma de tramo no reembolsable y bonificación del tipo de interés. El plazo de solicitud anunciado llegaba hasta el 1 de julio de 2026, así que, si te interesa, confirma en el ICO si sigue abierta.</p>

<h2>5 de septiembre de 2025: lanzamiento de ICO Crecimiento</h2>
<p>El Gobierno y el ICO presentaron ICO Crecimiento, la primera línea de <strong>financiación directa y 100 % digital</strong> del ICO para pymes, sin banco intermediario, con una dotación inicial de <strong>1.000 millones de euros</strong>. Las solicitudes se presentan en la plataforma ICO Online desde el día siguiente a la publicación del DCG en la web del ICO.</p>
<p>Desde el principio, la línea se dirigió a sociedades pyme con al menos 4 años de antigüedad y cuentas auditadas de los dos últimos ejercicios (o un aval que las sustituya), con préstamos desde 50.000 € para inversión (hasta 10 años) y circulante (hasta 5 años).</p>
""",
faqs=[
("¿Sigue abierta la línea ICO Crecimiento?", "Sí. A 2 de octubre de 2026 sigue admitiendo solicitudes, con plazo hasta el 31 de diciembre de 2027 o hasta que se agote el presupuesto. Las solicitudes se atienden por orden de presentación."),
("¿Cuándo se lanzó ICO Crecimiento?", "Se presentó el 5 de septiembre de 2025, con una dotación inicial de 1.000 millones de euros, como la primera línea de financiación directa y 100 % digital del ICO para pymes."),
("¿Qué es ICO Crecimiento Exportadores?", "Una línea relacionada, activada el 9 de febrero de 2026 con 750 millones de euros, para pymes afectadas por el entorno arancelario. Incluye un tramo no reembolsable y bonificación del tipo de interés con fondos Next Generation."),
],
))
