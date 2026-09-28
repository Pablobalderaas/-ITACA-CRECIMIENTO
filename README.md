# Ítaca Crecimiento

Web de Ítaca Crecimiento, consultoría de financiación ICO. Es una página única y estática, hecha a partir del handoff de diseño `design_handoff_itaca_web`.

## Estructura

- `index.html`: la página completa, con el HTML, el CSS y el JS incluidos.
- `aviso-legal.html`, `privacidad.html` y `cookies.html`: las páginas legales, que usan los estilos de `assets/legal.css`.
- `assets/velero.avif`: la foto del hero.
- `assets/logo/`: los logos oficiales (horizontal, horizontal-azul, monocromo, símbolo, vertical e icono). El icono se usa también como favicon.

## Ver en local

```bash
python3 -m http.server 8000
# abre http://localhost:8000
```

## Formulario de contacto

En `index.html`, el `<form id="contact-form">` tiene un atributo `data-endpoint`:

- **Vacío (así está ahora):** al enviar se abre el programa de correo del visitante con la consulta ya redactada para `general@itacacrecimiento.com`.
- **Con una URL** (por ejemplo, de Formspree o Getform): la consulta se envía por POST y se muestra el mensaje «Gracias.».

## Pendiente de confirmar

- El plazo de respuesta de 48 horas laborables.
- Los textos de las líneas ICO y de las preguntas frecuentes.
- Los datos del titular en las páginas legales: nombre y apellidos, NIF, domicilio y la localidad para la jurisdicción. Están marcados en naranja como `[...]` (clase `pendiente`).
- Si se añade analítica u otras cookies no técnicas, actualiza `cookies.html` y pon un banner de consentimiento.

## Publicar

Es un sitio estático, así que puedes publicarlo en GitHub Pages (Settings → Pages), Netlify o Cloudflare Pages.
