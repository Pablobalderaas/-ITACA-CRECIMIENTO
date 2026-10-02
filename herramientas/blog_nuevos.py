"""Artículos del blog añadidos en octubre de 2026. Se cargan desde gen_blog.py."""

NOTA_DCG = '<p class="note">Basado en el Documento de Condiciones Generales (DCG) de la línea ICO Crecimiento. Las condiciones pueden cambiar y, en caso de duda, prevalece el texto oficial: compruébalo siempre en <a href="https://www.ico.es" rel="noopener">www.ico.es</a>.</p>'

NUEVOS = []

# ------------------------------------------------------------------ coste
NUEVOS.append(dict(
slug="cuanto-cuesta-ico-crecimiento",
fecha="2026-10-02",
titulo="Cuánto cuesta un préstamo ICO Crecimiento: tipo, comisiones y un ejemplo completo",
seo="Cuánto cuesta ICO Crecimiento: tipo de interés, comisiones y ejemplo",
desc="Todo lo que se paga en un préstamo ICO Crecimiento: Euríbor más margen, comisión de apertura, cancelación anticipada, el efecto del aval y un ejemplo de 400.000 € a 10 años.",
resumen="""<p>El coste de ICO Crecimiento tiene pocas piezas y todas están en el reglamento de la línea:</p>
<ul>
  <li><strong>Tipo de interés:</strong> Euríbor a 12 meses (mínimo 0 %) + 1,75 %, que baja al 1,25 % o al 0,75 % con aval. Se revisa cada año.</li>
  <li><strong>Comisión de apertura:</strong> 0,5 %, descontada del primer desembolso.</li>
  <li><strong>Cancelación anticipada:</strong> 0,5 % de lo que se devuelva antes de tiempo.</li>
  <li><strong>Sin comisión</strong> por la parte que no se llegue a disponer.</li>
  <li>Posible <strong>recargo de sostenibilidad</strong> del 0,25 % anual si no se cumple el Plan de Remediación.</li>
</ul>""",
cuerpo=NOTA_DCG + """
<h2>El tipo de interés</h2>
<p>El préstamo es a tipo variable: <strong>Euríbor a un año más un margen</strong>. Si el Euríbor fuese negativo, se toma como 0 %. El tipo se revisa una vez al año y se mantiene durante los 12 meses siguientes. El margen depende de la garantía:</p>
<div class="table-wrap">
<table>
  <thead><tr><th>Garantía</th><th>Margen</th></tr></thead>
  <tbody>
    <tr><td>Sin aval, o aval de menos del 50 %</td><td>1,75 %</td></tr>
    <tr><td>Aval del Estado o de una entidad financiera solvente entre el 50 % y el 70 %</td><td>1,25 %</td></tr>
    <tr><td>Aval del Estado o de una entidad financiera solvente entre el 70 % y el 90 %</td><td>0,75 %</td></tr>
    <tr><td>Aval del 100 % de una SGR</td><td>Según el convenio entre el ICO y esa SGR</td></tr>
  </tbody>
</table>
</div>
<p>Cuando hay aval, a ese margen hay que sumar lo que cobra el avalista. En el caso de una SGR, sus comisiones y la aportación a su capital se pueden incluir en la propia financiación.</p>

<h2>Cómo se devuelve</h2>
<p>Los intereses se pagan <strong>cada mes</strong>, el día 15. Durante la carencia solo se pagan intereses. Después, el capital se devuelve, como regla general, en <strong>cuotas mensuales de capital constantes</strong>: cada mes se amortiza lo mismo y los intereses se calculan sobre lo que queda pendiente, así que la cuota total va bajando con el tiempo.</p>

<h2>Ejemplo: 400.000 € de inversión a 10 años</h2>
<p>Una empresa financia una inversión con 400.000 € a 10 años, con 2 de carencia y sin aval. Para el ejemplo suponemos un Euríbor constante del 2 %, es decir, un tipo del 3,75 %. En la realidad el Euríbor cambiará cada año.</p>
<dl class="data-list">
  <div><dt>Comisión de apertura</dt><dd>2.000 € (0,5 %), que se descuentan del primer desembolso</dd></div>
  <div><dt>Años 1 y 2 (carencia)</dt><dd>Solo intereses: 1.250 € al mes</dd></div>
  <div><dt>Años 3 a 10</dt><dd>4.167 € de capital al mes más intereses: la primera cuota ronda los 5.417 € y la última, unos 4.180 €</dd></div>
  <div><dt>Intereses totales</dt><dd>Unos 90.600 €</dd></div>
  <div><dt>Coste financiero total</dt><dd>Unos 92.600 € (intereses + apertura)</dd></div>
</dl>

<h3>El mismo préstamo con aval del 80 %</h3>
<p>Con un aval público o de una entidad financiera solvente que cubra el 80 %, el margen bajaría al 0,75 % y el tipo quedaría en el 2,75 %. Los intereses totales bajarían a unos 66.500 €: unos 24.000 € menos, a los que habría que restar lo que cueste el aval. Por eso conviene comparar las dos opciones con números antes de presentar la solicitud.</p>

<h2>Otros costes posibles</h2>
<ul>
  <li><strong>Cancelación anticipada:</strong> 0,5 % de lo que se devuelva antes de tiempo. Si el préstamo vence anticipadamente por un incumplimiento, la comisión es del 1 % del capital pendiente.</li>
  <li><strong>Intereses de demora:</strong> el tipo ordinario más un 6 % sobre las cuotas que no se paguen a tiempo.</li>
  <li><strong>Recargo de sostenibilidad:</strong> si la empresa saca menos de 2 puntos en el cuestionario ASG y no acredita mejoras en 24 meses, 0,25 % anual sobre el importe firmado. En este ejemplo, 1.000 € al año. Lo explicamos en la guía del <a href="../../guias/cuestionario-sostenibilidad-ico-crecimiento/">cuestionario de sostenibilidad</a>.</li>
  <li><strong>Notaría:</strong> el contrato se firma en documento público.</li>
</ul>

<h2>Lo que no cuesta</h2>
<ul>
  <li>No hay comisión por la parte del préstamo que no se llegue a disponer.</li>
  <li>No hay que contratar seguros, tarjetas ni otros productos vinculados.</li>
  <li>Los gastos de consultoría para preparar la solicitud se pueden financiar dentro del propio préstamo.</li>
</ul>
""",
faqs=[
("¿Qué tipo de interés tiene ICO Crecimiento?", "Euríbor a 12 meses, con un mínimo del 0 %, más un margen del 1,75 %. El margen baja al 1,25 % o al 0,75 % si la operación lleva un aval que cubra entre el 50 % y el 70 % o entre el 70 % y el 90 %. El tipo se revisa cada año."),
("¿Qué comisiones tiene ICO Crecimiento?", "Una comisión de apertura del 0,5 %, que se descuenta del primer desembolso, y una comisión del 0,5 % sobre lo que se cancele anticipadamente. No hay comisión por la parte que no se disponga."),
("¿La cuota de ICO Crecimiento es fija?", "No. Pasada la carencia, el capital se devuelve en cuotas mensuales constantes y los intereses se calculan sobre lo pendiente, así que la cuota total baja con el tiempo. Además, el tipo se revisa cada año con el Euríbor."),
],
))

# ------------------------------------------------------------------ minimis
NUEVOS.append(dict(
slug="ayudas-de-minimis-ico-crecimiento",
fecha="2026-10-02",
titulo="Ayudas de minimis e ICO Crecimiento: por qué te preguntan por tus subvenciones",
seo="Ayudas de minimis en ICO Crecimiento: qué son, límites y declaración",
desc="Al pedir ICO Crecimiento hay que declarar las ayudas públicas recibidas. Qué son las ayudas de minimis, el límite de 300.000 € en tres años y cómo afecta a tu préstamo.",
resumen="""<p>Aunque ICO Crecimiento es un préstamo, el ICO calcula la <strong>ayuda pública implícita</strong> que contiene: el ahorro frente a un préstamo a precio de mercado.</p>
<ul>
  <li>Esa ayuda se encuadra en el régimen de <strong>minimis</strong> o, en inversión, en el régimen europeo de ayudas a pymes.</li>
  <li>El límite general de <em>minimis</em> es de <strong>300.000 € por empresa en tres años</strong> (50.000 € en agricultura y 30.000 € en pesca).</li>
  <li>Por eso hay que declarar todas las ayudas de <em>minimis</em> recibidas, también las del grupo.</li>
</ul>""",
cuerpo=NOTA_DCG + """
<h2>¿Por qué un préstamo lleva una «ayuda»?</h2>
<p>El ICO es una entidad pública. Cuando presta a un tipo inferior al que se considera de mercado según la normativa europea, la diferencia cuenta como ayuda de Estado, aunque sea pequeña. El ICO la calcula comparando el tipo aprobado con un tipo de referencia fijado por la Comisión Europea según la solvencia de la empresa y las garantías, y la refleja en el contrato.</p>
<p>En muchas operaciones esa ayuda es pequeña o nula, pero hay que comprobar que cabe dentro de los límites europeos.</p>

<h2>Qué régimen se aplica</h2>
<div class="table-wrap">
<table>
  <thead><tr><th>Finalidad del préstamo</th><th>Régimen de ayudas</th></tr></thead>
  <tbody>
    <tr><td>Circulante</td><td>Solo <em>minimis</em> (Reglamento UE 2023/2831)</td></tr>
    <tr><td>Compra de participaciones</td><td>Solo <em>minimis</em></td></tr>
    <tr><td>Inversión</td><td>Régimen de ayudas a pymes del Reglamento UE 651/2014 o <em>minimis</em></td></tr>
  </tbody>
</table>
</div>
<p>En inversión, el régimen de ayudas a pymes permite una ayuda de hasta el 20 % de los costes en las pequeñas empresas y hasta el 10 % en las medianas. Para ese régimen se firma además una declaración específica.</p>

<h2>Los límites de minimis</h2>
<ul>
  <li><strong>300.000 €</strong> por empresa en cualquier periodo de tres años, con carácter general.</li>
  <li><strong>50.000 €</strong> para las empresas del sector agrícola.</li>
  <li><strong>30.000 €</strong> para el sector de la pesca y la acuicultura.</li>
</ul>
<p>Son importes de ayuda, no de préstamo: lo que cuenta es la ayuda implícita calculada, no el nominal. El límite se aplica a la «única empresa», es decir, sumando las empresas del mismo grupo. En fusiones y adquisiciones se suman las ayudas previas de las empresas que se unen.</p>

<h2>Qué hay que declarar</h2>
<p>La solicitud incluye una declaración de ayudas de <em>minimis</em> en la que hay que indicar las recibidas en los tres años anteriores, por la empresa y por su grupo: organismo, fecha, importe y si fue préstamo, subvención o garantía. Muchas pymes han recibido ayudas de <em>minimis</em> sin saberlo: por ejemplo, el Kit Digital se concedió en este régimen, como muchas subvenciones autonómicas y locales.</p>
<p>La empresa también se compromete a no superar el límite en los tres años siguientes, sumando la ayuda del préstamo del ICO.</p>

<h2>Qué puede pasar si te acercas al límite</h2>
<ul>
  <li>El importe o el plazo del préstamo pueden quedar limitados para no superar el tope de ayuda.</li>
  <li>La empresa puede pedir al ICO un tipo de interés más alto, precisamente para reducir la ayuda implícita y no agotar el margen de <em>minimis</em> que necesite para otras subvenciones.</li>
  <li>Un préstamo puede dividirse en tramos acogidos a regímenes distintos.</li>
</ul>

<h2>Recomendación práctica</h2>
<p>Antes de solicitar, haz una lista de todas las ayudas públicas de los últimos tres años, de la empresa y del grupo, con sus resoluciones. Si piensas pedir otras subvenciones próximamente, tenlo en cuenta: lo que consuma ICO Crecimiento del límite de <em>minimis</em> no estará disponible para ellas.</p>
""",
faqs=[
("¿ICO Crecimiento es una ayuda de minimis?", "El préstamo puede incluir una ayuda implícita: el ahorro frente a un préstamo a precio de mercado. En circulante y compra de participaciones se encuadra en el régimen de minimis; en inversión, en el régimen de ayudas a pymes del Reglamento 651/2014 o en minimis."),
("¿Cuál es el límite de las ayudas de minimis?", "Con carácter general, 300.000 € por empresa (sumando su grupo) en cualquier periodo de tres años. Para el sector agrícola el límite es de 50.000 € y para la pesca y la acuicultura, de 30.000 €."),
("¿El Kit Digital cuenta como ayuda de minimis?", "Sí, el Kit Digital se concedió en régimen de minimis, así que hay que incluirlo en la declaración si se recibió en los tres años anteriores."),
],
))

# ------------------------------------------------------------------ deuda corto plazo
NUEVOS.append(dict(
slug="cancelar-deuda-corto-plazo-ico-crecimiento",
fecha="2026-10-02",
titulo="Cancelar deuda a corto plazo con ICO Crecimiento: cuándo tiene sentido",
seo="Cancelar deuda a corto plazo con ICO Crecimiento: cuándo conviene",
desc="ICO Crecimiento permite destinar el circulante a cancelar deuda a corto plazo con proveedores o bancos. Cuándo tiene sentido, cuándo no y qué hay que tener en cuenta.",
resumen="""<p>Entre las finalidades de circulante de ICO Crecimiento está la <strong>cancelación de deuda a corto plazo</strong>, tanto comercial (proveedores) como financiera (bancos).</p>
<ul>
  <li>Permite pasar deuda que vence en meses a un préstamo de <strong>hasta 5 años con 1 de carencia</strong>.</li>
  <li>Tiene sentido en empresas <strong>rentables</strong> cuyo crecimiento se ha financiado con deuda demasiado corta.</li>
  <li>No sirve para empresas con pérdidas, morosidad en la CIRBE o deudas con Hacienda o la Seguridad Social: no cumplen los requisitos.</li>
</ul>""",
cuerpo=NOTA_DCG + """
<h2>El problema: crecer con deuda a corto</h2>
<p>Es muy habitual: una pyme crece, necesita más circulante y lo va cubriendo con lo que tiene a mano, como pólizas de crédito, descuento comercial, confirming o pagar más tarde a los proveedores. Todo es deuda que vence en meses. La empresa es rentable, pero vive pendiente de las renovaciones y cualquier recorte de una línea bancaria la pone en apuros.</p>

<h2>Qué permite ICO Crecimiento</h2>
<p>El reglamento de la línea incluye dentro del circulante la <strong>cancelación de deuda a corto plazo de naturaleza comercial y financiera</strong>. Es decir, se puede pedir un préstamo de ICO Crecimiento para pagar esas deudas y devolverlo:</p>
<ul>
  <li>en <strong>hasta 5 años</strong>,</li>
  <li>con <strong>hasta 1 año de carencia</strong>, en el que solo se pagan intereses,</li>
  <li>desde 50.000 € y hasta el 100 % de la necesidad justificada.</li>
</ul>

<h2>Ejemplo orientativo</h2>
<p>Una empresa factura 3 millones de euros, gana dinero y tiene 350.000 € dispuestos en pólizas y descuento que renueva cada año. Si pasa 250.000 € de esa deuda a ICO Crecimiento a 5 años con 1 de carencia, durante el primer año solo paga intereses y después devuelve unos 5.200 € de capital al mes, más los intereses. Las pólizas vuelven a quedar libres para los picos de tesorería.</p>

<h2>Cuándo tiene sentido</h2>
<ul>
  <li>La empresa es <strong>rentable</strong> y su problema es de plazos, no de resultados.</li>
  <li>La deuda a corto viene de <strong>financiar el crecimiento</strong>: más clientes, más stock, nuevos contratos.</li>
  <li>Los bancos han empezado a <strong>reducir o endurecer</strong> las líneas de corto plazo.</li>
  <li>Se quiere <strong>ordenar la deuda</strong> en un calendario de pagos previsible.</li>
</ul>

<h2>Cuándo no funciona</h2>
<ul>
  <li>Si la empresa ha tenido <strong>pérdidas en los dos últimos ejercicios</strong> o tiene patrimonio neto negativo: no cumple los requisitos.</li>
  <li>Si figura como <strong>morosa en la CIRBE</strong>, al pedirlo o al firmarlo.</li>
  <li>Si no está <strong>al corriente con Hacienda o la Seguridad Social</strong>: es un requisito previo, no algo que se pueda arreglar con el préstamo.</li>
  <li>Si la deuda corta tapa <strong>pérdidas recurrentes</strong>: el ICO analiza la capacidad de devolución y lo detectará.</li>
</ul>

<h2>Lo que conviene preparar</h2>
<ul>
  <li>El detalle de la deuda a corto plazo: con quién, cuánto, vencimientos y coste.</li>
  <li>Una explicación de por qué se generó esa deuda y cómo mejora la situación al alargar el plazo.</li>
  <li>Una previsión de tesorería que muestre que las cuotas son asumibles a partir del segundo año.</li>
</ul>
<p>Después habrá que justificar ante el ICO el destino de los fondos con los documentos correspondientes.</p>
<p>Ojo: la modalidad <a href="../../guias/ico-crecimiento-dana/">ICO Crecimiento DANA</a> sí excluye expresamente las refinanciaciones. Este artículo se refiere a la línea general.</p>
""",
faqs=[
("¿Se puede refinanciar deuda con ICO Crecimiento?", "La línea general permite destinar el circulante a cancelar deuda a corto plazo, tanto comercial como financiera, con un préstamo de hasta 5 años y 1 de carencia. La modalidad DANA, en cambio, excluye las refinanciaciones."),
("¿Puedo pagar deudas con Hacienda con ICO Crecimiento?", "No es el caso de uso: estar al corriente con Hacienda y la Seguridad Social es un requisito para solicitar el préstamo, no algo que se pueda resolver con él."),
("¿Conviene cancelar la póliza de crédito con ICO Crecimiento?", "Puede convenir pasar a largo plazo la parte estable de la deuda a corto y dejar la póliza libre para los picos de tesorería. Depende de cada empresa y conviene estudiarlo con números."),
],
))

# ------------------------------------------------------------------ relevo generacional
NUEVOS.append(dict(
slug="relevo-generacional-ico-crecimiento",
fecha="2026-10-02",
titulo="Relevo generacional en la empresa familiar: cómo puede ayudar ICO Crecimiento",
seo="Relevo generacional en la empresa familiar con ICO Crecimiento",
desc="ICO Crecimiento puede financiar la compra de participaciones o de acciones propias para facilitar el relevo generacional en la empresa familiar. Qué permite y qué hay que estudiar.",
resumen="""<p>Las empresas familiares que afrontan un <strong>relevo generacional</strong> son uno de los públicos a los que se dirige expresamente ICO Crecimiento. La línea permite financiar:</p>
<ul>
  <li>La <strong>compra de participaciones empresariales</strong> para facilitar el relevo de los socios mayoritarios.</li>
  <li>La <strong>adquisición de acciones o participaciones propias</strong> por la empresa familiar, hasta el límite de la Ley de Sociedades de Capital.</li>
  <li>Inversiones y gastos que acompañan al relevo, como la <strong>formación</strong> del equipo o los sistemas de gestión.</li>
</ul>""",
cuerpo=NOTA_DCG + """
<h2>El problema del relevo</h2>
<p>Cuando el fundador se retira, a menudo no todos los herederos quieren seguir en la empresa, o hay socios que quieren salir. Alguien tiene que comprar esas participaciones, y ni la siguiente generación ni la empresa suelen tener la liquidez necesaria. Los bancos, además, son prudentes con este tipo de operaciones porque no financian un activo productivo.</p>

<h2>Qué permite ICO Crecimiento</h2>
<p>El reglamento de la línea incluye dos finalidades pensadas para este caso:</p>
<ol class="pasos-guia">
  <li><strong>Adquisición de participaciones empresariales</strong> para facilitar el relevo generacional de los accionistas mayoritarios de la empresa familiar.</li>
  <li><strong>Adquisición de acciones propias</strong> por parte de la empresa familiar, hasta el límite que permite la Ley de Sociedades de Capital, con el mismo objetivo.</li>
</ol>
<p>Hay que tener en cuenta que el prestatario es siempre una <strong>sociedad mercantil</strong> que cumple los requisitos de la línea, no una persona física. Por eso la forma de la operación (quién compra, a quién y cómo se estructura) hay que diseñarla con cuidado, junto con el asesor legal y fiscal de la familia.</p>

<h2>Condiciones a tener en cuenta</h2>
<ul>
  <li>La compra de participaciones se financia como máximo al <strong>80 %</strong>.</li>
  <li>La ayuda implícita del préstamo en estas operaciones se encuadra solo en el régimen de <em>minimis</em>. Lo explicamos en el artículo sobre <a href="../ayudas-de-minimis-ico-crecimiento/">ayudas de minimis</a>.</li>
  <li>La compra se justifica con una nota simple actualizada del Registro Mercantil o un certificado de la sociedad que confirme la transmisión.</li>
  <li>Se aplican todos los requisitos generales: pyme con al menos 4 años, cuentas auditadas o aval, sin pérdidas en los dos últimos ejercicios, sin morosidad y al corriente de pagos. Si la empresa forma parte de un grupo, los requisitos deben cumplirse también a nivel de grupo.</li>
</ul>

<h2>Más allá de la compra</h2>
<p>Un relevo no es solo un cambio de propiedad. ICO Crecimiento también financia gastos que ayudan a que salga bien:</p>
<ul>
  <li><strong>Formación</strong> del equipo y de la nueva dirección.</li>
  <li><strong>Sistemas de gestión e informes</strong> que profesionalizan la empresa.</li>
  <li><strong>Inversiones</strong> que la nueva generación quiere acometer: digitalización, maquinaria o nuevos mercados.</li>
  <li>El <strong>circulante</strong> necesario para mantener la actividad durante la transición.</li>
</ul>

<h2>Por dónde empezar</h2>
<p>Antes de preparar la solicitud conviene tener claro el acuerdo entre la familia: quién se queda, quién sale, a qué valor y con qué calendario. Con eso definido, se puede estudiar si la operación encaja en ICO Crecimiento y cómo combinarla con otras fuentes de financiación.</p>
""",
faqs=[
("¿ICO Crecimiento financia la compra de participaciones?", "Sí, para fines concretos: facilitar el relevo generacional de los accionistas mayoritarios de la empresa familiar, ampliar la capacidad productiva, mejorar el acceso a la financiación o asegurar el suministro de insumos clave. Se financia hasta el 80 %."),
("¿Puede la empresa familiar comprar sus propias participaciones con ICO Crecimiento?", "Sí. La línea permite financiar la adquisición de acciones propias por la empresa familiar, hasta el límite de la Ley de Sociedades de Capital, para facilitar el relevo generacional de los socios mayoritarios."),
("¿Puede un heredero pedir ICO Crecimiento a título personal?", "No. El beneficiario tiene que ser una sociedad mercantil pyme que cumpla los requisitos de la línea. La estructura de la operación conviene diseñarla con el asesor legal y fiscal."),
],
))

# ------------------------------------------------------------------ después de la aprobación
NUEVOS.append(dict(
slug="despues-de-la-aprobacion-ico-crecimiento",
fecha="2026-10-02",
titulo="Me han aprobado ICO Crecimiento: firma, desembolso y justificación",
seo="ICO Crecimiento aprobado: firma ante notario, desembolso y justificación",
desc="Qué pasa después de que el ICO apruebe tu préstamo: plazo para firmar, cuándo llega el dinero, cómo se justifica el gasto y qué obligaciones tienes durante el préstamo.",
resumen="""<p>La aprobación no es el final. Después vienen estos pasos:</p>
<ol>
  <li><strong>Aceptar</strong> las condiciones de la resolución de concesión.</li>
  <li><strong>Firmar</strong> el contrato en documento público en un máximo de 3 meses (prorrogables otros 3).</li>
  <li><strong>Recibir el dinero:</strong> el circulante, de una vez en 15 días; la inversión, en una o varias entregas antes de que acabe la carencia.</li>
  <li><strong>Justificar</strong> el destino de los fondos con facturas en ICO Online.</li>
  <li><strong>Conservar</strong> la documentación durante 10 años desde el vencimiento.</li>
</ol>""",
cuerpo=NOTA_DCG + """
<h2>1. La resolución de concesión</h2>
<p>El Comité de Operaciones del ICO aprueba la operación con una resolución que fija exactamente las condiciones: importe, plazo, carencia, tipo y garantías. La empresa tiene que <strong>aceptarlas expresamente</strong> y, a partir de ahí, ya no se pueden cambiar en la firma, salvo en los casos previstos en el reglamento.</p>

<h2>2. La firma del contrato</h2>
<p>El contrato de préstamo se formaliza en <strong>documento público</strong>, ante notario. La resolución indica el plazo máximo para firmarlo, que no puede superar <strong>3 meses</strong>, con una única prórroga de otros 3 si se justifica. En la fecha de firma, la empresa no puede figurar como morosa en la CIRBE.</p>
<p>Si la operación lleva aval de una SGR u otras garantías, tienen que estar listas para la firma.</p>

<h2>3. El desembolso</h2>
<dl class="data-list">
  <div><dt>Circulante</dt><dd>De una sola vez, en un máximo de 15 días naturales desde la firma</dd></div>
  <div><dt>Inversión</dt><dd>En una o varias entregas, siempre antes de que termine la carencia</dd></div>
  <div><dt>Comisión de apertura</dt><dd>El 0,5 % se descuenta del primer desembolso</dd></div>
  <div><dt>Lo no dispuesto</dt><dd>Si no se dispone todo en plazo, el préstamo queda en lo dispuesto, sin comisión por el resto</dd></div>
</dl>

<h2>4. La justificación</h2>
<p>La empresa tiene que justificar en qué ha gastado el dinero. Se hace en la aplicación de <strong>ICO Online</strong>, subiendo copia de las facturas, que deben cumplir el reglamento de facturación, y certificando con firma electrónica que son copia fiel de los originales. En la compra de participaciones se justifica con una nota simple del Registro Mercantil o un certificado de la sociedad, y en la compra de inmuebles hace falta un certificado de tasación.</p>
<p>No justificar, o justificar de forma insuficiente, puede provocar el <strong>vencimiento anticipado</strong> del préstamo o que no se hagan los desembolsos pendientes. Conviene tener las facturas y los justificantes de pago ordenados desde el principio.</p>

<h2>5. Durante la vida del préstamo</h2>
<ul>
  <li><strong>Pagos mensuales:</strong> intereses el día 15 de cada mes y, pasada la carencia, el capital en cuotas constantes.</li>
  <li><strong>Revisión del tipo</strong> una vez al año, con aviso previo.</li>
  <li><strong>Controles:</strong> el ICO, la Intervención General del Estado y el Tribunal de Cuentas pueden pedir información y visitar las instalaciones.</li>
  <li><strong>Plan de Remediación</strong>, si la puntuación de sostenibilidad fue inferior a 2: hay 24 meses para acreditar mejoras.</li>
  <li><strong>Desarrollar el proyecto</strong> según el plan presentado y comunicar cualquier cambio relevante.</li>
  <li><strong>Conservar los documentos</strong> justificativos durante 10 años desde el vencimiento del préstamo.</li>
</ul>

<h2>¿Se pueden cambiar las condiciones después?</h2>
<p>En algunos casos, sí: cambios de titularidad, fusiones o escisiones (si el nuevo titular cumple los requisitos), una ampliación del plazo por circunstancias imprevisibles o una ampliación del plazo de disposición. Nunca se puede aumentar el importe aprobado, y la mala situación económica de la empresa no justifica por sí sola alargar el plazo.</p>
<p>También se puede cancelar el préstamo antes de tiempo, total o parcialmente, con una comisión del 0,5 % sobre lo devuelto.</p>

<h2>Causas de vencimiento anticipado</h2>
<ul>
  <li>Dejar de pagar seis liquidaciones consecutivas.</li>
  <li>Haber obtenido el préstamo falseando u ocultando condiciones.</li>
  <li>No cumplir el objetivo o el proyecto financiado.</li>
  <li>No justificar, o justificar de forma insuficiente, el destino de los fondos.</li>
  <li>Obstaculizar los controles.</li>
</ul>
""",
faqs=[
("¿Cuánto tiempo hay para firmar ICO Crecimiento tras la aprobación?", "El plazo lo fija la resolución de concesión y no puede superar 3 meses, con una única prórroga de otros 3 meses si se justifica. El contrato se firma en documento público."),
("¿Cuándo se recibe el dinero de ICO Crecimiento?", "En circulante, de una sola vez en un máximo de 15 días naturales desde la firma. En inversión, en una o varias entregas antes de que termine el periodo de carencia."),
("¿Cómo se justifica el préstamo de ICO Crecimiento?", "Subiendo a ICO Online copia de las facturas del gasto, certificadas con firma electrónica. La compra de participaciones se justifica con nota simple o certificado de la sociedad. La documentación se conserva 10 años desde el vencimiento."),
],
))

# ------------------------------------------------------------------ filtros de solvencia
NUEVOS.append(dict(
slug="por-que-deniegan-ico-crecimiento",
fecha="2026-10-02",
titulo="Por qué el ICO deniega ICO Crecimiento: los filtros de solvencia",
seo="Por qué deniegan ICO Crecimiento: rating, pérdidas, CIRBE y otros filtros",
desc="Rating mínimo B, pérdidas, patrimonio neto, CIRBE, empresa en crisis y pérdida esperada: los filtros que aplica el ICO antes de aprobar ICO Crecimiento y cómo comprobarlos antes.",
resumen="""<p>Antes de valorar el proyecto, el ICO comprueba unos filtros que, si fallan, descartan la solicitud:</p>
<ul>
  <li>Calificación crediticia mínima <strong>B</strong> (B- o inferior queda descartada).</li>
  <li><strong>Sin pérdidas</strong> en los dos últimos ejercicios cerrados y <strong>sin patrimonio neto negativo</strong>.</li>
  <li><strong>Sin morosidad en la CIRBE</strong>, al solicitar y al firmar.</li>
  <li>No ser <strong>empresa en crisis</strong>.</li>
  <li>Una <strong>pérdida esperada</strong> de la operación no superior al 1 %.</li>
</ul>""",
cuerpo=NOTA_DCG + """
<h2>Los filtros, uno a uno</h2>

<h3>1. Calificación crediticia mínima: B</h3>
<p>El ICO calcula un rating de la empresa con su sistema interno, en la escala de Standard &amp; Poor's. El mínimo es <strong>B</strong>: las solicitudes con B- o inferior se descartan. Si la empresa pertenece a un grupo, se calcula el rating de la empresa y el del grupo, y cuenta el peor de los dos.</p>

<h3>2. Pérdidas y patrimonio neto</h3>
<p>No se admiten empresas con <strong>pérdidas en los dos últimos ejercicios cerrados</strong> ni con <strong>patrimonio neto negativo</strong> en el último. Un solo año en pérdidas no descarta por sí solo, pero pesa en el rating y conviene explicarlo bien.</p>

<h3>3. CIRBE sin morosidad</h3>
<p>La empresa no puede figurar como morosa en la Central de Información de Riesgos del Banco de España ni el día de la solicitud ni el de la firma. Un recibo devuelto o una cuota impagada que se haya olvidado puede bastar. Conviene pedir el informe CIRBE, que es gratuito, antes de presentar nada.</p>

<h3>4. Empresa en crisis</h3>
<p>Al cierre del último ejercicio, la empresa no puede estar «en crisis» según la normativa europea. En una sociedad limitada o anónima, eso ocurre, entre otros casos, cuando las pérdidas acumuladas se han comido más de la mitad del capital social suscrito, o cuando la empresa está en concurso o reúne las condiciones para estarlo.</p>

<h3>5. Pérdida esperada de la operación</h3>
<p>El ICO estima la pérdida esperada de cada operación, que combina la probabilidad de impago, la exposición y las garantías. Si supera el <strong>1 %</strong>, la operación no entra en la línea. Aquí las garantías importan: un aval puede reducir la pérdida esperada y hacer viable una operación que sin él no lo sería.</p>

<h3>6. Capacidad de devolución</h3>
<p>Con los estados financieros y las previsiones, el ICO analiza si la empresa puede pagar las cuotas. Puede pedir información adicional e incluso encargar un informe a un experto independiente.</p>

<h2>Otros motivos de exclusión</h2>
<ul>
  <li>No estar al corriente con Hacienda o la Seguridad Social, o tener pendiente el reintegro de alguna subvención.</li>
  <li>Estar en concurso de acreedores o inhabilitada.</li>
  <li>Pertenecer a un sector excluido: juego, armamento letal, medios de comunicación, intermediación financiera (salvo fintech e insurtech), actividades religiosas o políticas, entre otros.</li>
  <li>No ser pyme si se cuenta el grupo, o estar participada en un 25 % o más por organismos públicos.</li>
  <li>No cumplir los requisitos a nivel de grupo, cuando la empresa pertenece a uno.</li>
</ul>

<h2>¿Y si me lo deniegan?</h2>
<p>Contra la inadmisión o la desestimación <strong>no cabe recurso</strong> administrativo. Pero la empresa puede presentar una nueva solicitud, para otro proyecto o para el mismo una vez corregidos los defectos. Eso sí, la nueva solicitud entra al final de la cola, que se atiende por orden de llegada. Por eso es tan importante revisar estos filtros antes de la primera presentación.</p>
<p>Puedes hacer una primera comprobación con nuestro <a href="../../test-ico-crecimiento/">test de requisitos</a>. En el estudio gratuito revisamos con tus cifras los puntos que el test no puede medir, como el rating o la pérdida esperada.</p>
""",
faqs=[
("¿Qué rating mínimo exige ICO Crecimiento?", "Una calificación de B en la escala de Standard & Poor's, según el análisis interno del ICO. Las solicitudes con B- o inferior se descartan. Si la empresa pertenece a un grupo, cuenta la peor calificación entre la empresa y el grupo."),
("¿Puedo pedir ICO Crecimiento con un año en pérdidas?", "Un solo ejercicio con pérdidas no descarta automáticamente, porque el filtro es tener pérdidas en los dos últimos ejercicios cerrados. Pero afecta al rating y conviene explicarlo bien en la solicitud."),
("¿Se puede recurrir si el ICO deniega ICO Crecimiento?", "No cabe recurso administrativo, pero se puede presentar una nueva solicitud una vez corregidos los defectos. Entra de nuevo por orden de llegada."),
],
))
