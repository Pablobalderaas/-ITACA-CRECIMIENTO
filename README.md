# Ítaca Crecimiento

Web de Ítaca Crecimiento, consultoría especializada en ICO Crecimiento, el préstamo directo del ICO para pymes. Es una página única y estática, hecha a partir del handoff de diseño `design_handoff_itaca_web`.

## Estructura

- `index.html`: la página completa, con el HTML, el CSS y el JS incluidos.
- `guias/`: sección de guías (una carpeta por guía). Se genera con un script a partir de una plantilla común; usa `assets/legal.css` y `assets/guias.css`.
- `assets/og-image.jpg`: imagen de 1200×630 que se muestra al compartir la web en WhatsApp o redes.
- `llms.txt`: resumen de la web para asistentes de IA (ChatGPT, Perplexity, Gemini…).
- `aviso-legal.html`, `privacidad.html` y `cookies.html`: las páginas legales, que usan los estilos de `assets/legal.css`.
- `assets/velero.avif`: la foto del hero.
- `assets/logo/`: los logos oficiales (horizontal, horizontal-azul, monocromo, símbolo, vertical e icono). El icono se usa también como favicon.

## Ver en local

```bash
python3 -m http.server 8000
# abre http://localhost:8000
```

## Formulario de contacto

El formulario envía las consultas a Formspree (`https://formspree.io/f/myezlpqe`, en el atributo `data-endpoint` del `<form id="contact-form">`), que las reenvía a `general@itacacrecimiento.com`. El campo del correo se llama `email` para que, al pulsar Responder, la respuesta vaya a quien escribió. Si se deja `data-endpoint` vacío, al enviar se abre el programa de correo del visitante con la consulta ya redactada.

## Pendiente de confirmar

- El plazo de respuesta de 48 horas laborables.
- Las condiciones de ICO Crecimiento (portada, guía y `llms.txt`): comprobarlas en ico.es y actualizarlas si cambian.
- Si se añade analítica u otras cookies no técnicas, actualiza `cookies.html` y pon un banner de consentimiento.

## Google Search Console

- `robots.txt` permite rastrear toda la web e indica dónde está el sitemap.
- `sitemap.xml` lista la página principal y las guías. Las páginas legales no se incluyen porque llevan `noindex`.
- La portada y las guías llevan datos estructurados (schema.org): empresa, preguntas frecuentes, artículos y migas de pan.
- `index.html` declara `https://itacacrecimiento.com/` como dirección canónica.

Al añadir páginas nuevas, inclúyelas en `sitemap.xml` y actualiza su `lastmod`.

## Publicar en GitHub Pages

1. Si el repositorio es privado, GitHub Pages solo funciona con un plan de pago (GitHub Pro o superior). Con el plan gratuito, haz el repositorio público en Settings → General → Danger Zone → Change visibility.
2. En Settings → Pages, elige Source: **Deploy from a branch**, la rama con la web y la carpeta **/ (root)**, y pulsa Save.
3. En uno o dos minutos la web estará en `https://<usuario>.github.io/<repositorio>/`.

El archivo `.nojekyll` hace que GitHub sirva los archivos tal cual, sin procesarlos con Jekyll.

### Dominio propio: itacacrecimiento.com

El archivo `CNAME` indica a GitHub Pages que la web se sirve en `itacacrecimiento.com`. En el panel DNS del proveedor del dominio hay que crear estos registros:

| Tipo | Nombre | Valor |
|---|---|---|
| A | @ | 185.199.108.153 |
| A | @ | 185.199.109.153 |
| A | @ | 185.199.110.153 |
| A | @ | 185.199.111.153 |
| AAAA | @ | 2606:50c0:8000::153 |
| AAAA | @ | 2606:50c0:8001::153 |
| AAAA | @ | 2606:50c0:8002::153 |
| AAAA | @ | 2606:50c0:8003::153 |
| CNAME | www | pablobalderaas.github.io |

- Borra cualquier otro registro A, AAAA o CNAME que ya exista para `@` o `www` (por ejemplo, la página de aparcamiento del proveedor).
- **No toques los registros MX ni TXT del correo**, o dejará de funcionar `general@itacacrecimiento.com`.
- Cuando los DNS se hayan propagado (de minutos a 24 horas), marca **Enforce HTTPS** en Settings → Pages.
- Recomendado: verifica el dominio en la configuración de tu cuenta de GitHub (Settings → Pages → Add a domain) para que nadie más pueda usarlo en GitHub Pages.
