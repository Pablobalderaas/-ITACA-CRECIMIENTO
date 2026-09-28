# Ítaca Crecimiento

Web de Ítaca Crecimiento, consultoría de financiación ICO. Es una página única y estática, hecha a partir del handoff de diseño `design_handoff_itaca_web`.

## Estructura

- `index.html`: la página completa, con el HTML, el CSS y el JS incluidos.
- `assets/velero.avif`: la foto del hero.
- `assets/logo/`: los logos oficiales (horizontal, horizontal-azul, monocromo, símbolo, vertical e icono). El icono se usa también como favicon.

## Ver en local

```bash
python3 -m http.server 8000
# abre http://localhost:8000
```

## Formulario de contacto

En `index.html`, el `<form id="contact-form">` tiene un atributo `data-endpoint`:

- **Vacío (así está ahora):** al enviar se abre el programa de correo del visitante con la consulta ya redactada para `hola@itacacrecimiento.es`.
- **Con una URL** (por ejemplo, de Formspree o Getform): la consulta se envía por POST y se muestra el mensaje «Gracias.».

## Pendiente de confirmar

- El correo y el teléfono reales. Ahora son de ejemplo: `hola@itacacrecimiento.es` y `+34 900 000 000`.
- El plazo de respuesta de 48 horas laborables.
- Los textos de las líneas ICO y de las preguntas frecuentes.
- Las páginas legales: aviso legal, privacidad y cookies. Los enlaces del pie apuntan a `#`.

## Publicar

Es un sitio estático, así que puedes publicarlo en GitHub Pages (Settings → Pages), Netlify o Cloudflare Pages.
