# Assets — imágenes que faltan

Subí estos dos archivos a esta carpeta `assets/`:

## 1. `hermes-cyberpunk.jpg` (hero portrait)
- La imagen del Hermes cyberpunk con el caduceo de neón.
- Recomendado: **vertical, ~800x1067 px (relación 3:4)**, JPG calidad 80–85.
- Se muestra en el hero, tanto en mobile como en desktop.

## 2. `hermes-og.jpg` (preview para WhatsApp/Twitter/etc.)
- **Obligatorio para que WhatsApp muestre la previsualización al compartir el link.**
- Tamaño: **1200 x 630 px** (landscape, relación ~1.91:1), JPG calidad 80.
- Pesar **menos de 300 KB** idealmente. WhatsApp ignora imágenes muy pesadas.
- Idea: el mismo personaje del hero pero recortado/centrado en formato horizontal,
  con el título "Hermes Agent" superpuesto.

## Verificar previsualización en WhatsApp
1. Subí los archivos y publicá los cambios.
2. Abrí https://developers.facebook.com/tools/debug/ y pegá la URL del sitio.
3. Tocá "Scrape Again" para forzar el refresco del cache de OG.
4. WhatsApp comparte el cache con Facebook, así que la previsualización debería verse.

Si tu dominio no es `https://fedesapuppo.github.io/hermes-landing/`, actualizá las
etiquetas `og:url` y `og:image` en `index.html` para que apunten al dominio correcto.
