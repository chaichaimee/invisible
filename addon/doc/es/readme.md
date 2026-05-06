<p align="center">
  <img src="https://www.nvaccess.org/wp-content/uploads/2015/10/NVDA_logo_standard_transparent.png" alt="NVDA Logo" width="220">
</p>

# Invisible

<p align="center"><i>Silencia el desorden. Da forma a la voz. Sé dueño de tu experiencia de navegación.</i></p>

<p align="center">
  <strong>Autor:</strong> Chai Chaimee<br>
  <strong>Repositorio:</strong> <a href="https://github.com/chaichaimee/invisible">github.com/chaichaimee/invisible</a>
</p>

---

## ¿Por qué conformarse con páginas web ruidosas?

Los sitios web modernos están llenos de repeticiones, etiquetas de patrocinio, avisos de cookies, contadores de comentarios, barras laterales y contenido de relleno generado automáticamente que los lectores de pantalla deben leer en voz alta, una y otra vez.

**Invisible** te devuelve el control.

Decide exactamente qué palabras, frases o patrones debe omitir NVDA por completo, o reemplázalos discretamente por algo más corto, limpio o por el silencio absoluto.

<br><br>

Esto no es solo filtrar. Esto es **curaduría de audio personal** para la web.

## Potente pero elegantemente simple

*   Oculta texto por completo: NVDA actúa como si nunca hubiera existido
*   Reemplaza etiquetas molestas por marcadores cortos (“Patrocinado · Anuncio” → “omitir”)
*   Aplica reglas a una página, a todo un dominio o a patrones de URL complejos (regex)
*   Soporte completo de expresiones regulares para una precisión quirúrgica
*   Efecto instantáneo: no es necesario recargar la página
*   Interfaz sensible al contexto: el gesto de doble toque abre “Añadir sitio” con la URL actual ya rellenada
*   Soporte para clic derecho + tecla Suprimir para una gestión rápida
*   Archivos .json portátiles por sitio: fáciles de respaldar o compartir

## Comienza en menos de 30 segundos

1.  Ve a cualquier página donde NVDA lea algo que quieras silenciar o cambiar.

2.  Presiona **NVDA + Mayús + W**<br><br>
    → Un toque → abre la ventana principal de gestión<br>
    → Doble toque (rápido) → abre el diálogo “Añadir nuevo sitio” con la URL actual ya rellenada

3.  En el diálogo **Añadir sitio**:<br><br>
    • Mantén o edita el nombre a mostrar<br>
    • Elige el alcance:<br>
    &nbsp;&nbsp;– Solo una página<br>
    &nbsp;&nbsp;– Todo el sitio web (dominio)<br>
    &nbsp;&nbsp;– Expresión regular (coincidencia avanzada de URL)<br><br>
    Haz clic en **Guardar**

4.  Ahora estás dentro del gestor de reglas del sitio:<br><br>
    • Escribe el patrón que quieres marcar como objetivo<br>
    • Introduce el texto de reemplazo, o déjalo en blanco para un silencio total<br>
    • Marca “Usar como expresión regular” cuando sea necesario<br>
    • Haz clic en **Añadir** (o **Actualizar** al editar)<br><br>
    Los cambios se aplican al instante: vuelve a navegar y escucha.

<br>

Puedes volver en cualquier momento con **NVDA+Mayús+W** (un toque) para editar, añadir más reglas, eliminar entradas o cambiar entre sitios.

## Ejemplos reales que ahorran tiempo cada día

| Patrón Objetivo | Reemplazo | ¿Regex? | Lo que escuchas en su lugar |
| :--- | :--- | :--- | :--- |
| Anuncio | (en blanco) | No | — omitido por completo — |
| Patrocinado | omitir | No | “omitir” |
| · [0-9,]+ comentarios? | (en blanco) | Sí | — sin recuento de comentarios — |
| Última hora: | Noticias: | No | Más corto y limpio |
| ^Aviso de cookies.*aceptar | (en blanco) | Sí | Texto del banner silenciado |

## Consejos para usuarios avanzados

*   Clic derecho en cualquier sitio o entrada → menú contextual con Editar / Eliminar
*   Presiona la tecla **Suprimir** en el elemento seleccionado para una eliminación instantánea
*   Utiliza coincidencia literal de "el más largo primero" → evita problemas con palabras parciales
*   Importa reglas de otro archivo .json directamente a cualquier sitio
*   El modo Regex admite grupos de reemplazo, muy potente para contenido dinámico

<br><br>

## Apóyame

Si esta herramienta ha facilitado tu vida, considera impulsar la próxima actualización con una pequeña donación.

<br>

[<img src="https://img.shields.io/badge/Donate-Support%20Me-blue?style=for-the-badge&logo=stripe" alt="Support me">](https://buy.stripe.com/dRm9AU1xQ3Ds22N6VK1VK01)

<br>

Tu apoyo lo significa todo. Construyamos algo grandioso juntos.

<br>

<p align="center">© 2026 Chai Chaimee NVDA Add-on Lanzado bajo GNU</p>