# TACA Crecimiento

Web de presentación del servicio de preparación y elaboración de expedientes para solicitar financiación de las Líneas ICO.

## Estructura

- `index.html`: página única (HTML + CSS incrustado, sin dependencias de compilación).

## Ver en local

Abre `index.html` en el navegador, o sirve la carpeta:

```bash
python3 -m http.server 8000
```

## Pendiente de personalizar

- Correo y teléfono de contacto (sección `#contacto`; ahora son de ejemplo).
- Datos fiscales del autónomo (nombre y NIF) en el pie, si quieres mostrarlos.
- Aviso legal, política de privacidad y cookies antes de publicar.

## Publicar

Al ser un sitio estático puede publicarse gratis en GitHub Pages (Settings → Pages → rama `main`, carpeta raíz), Netlify o Cloudflare Pages.
