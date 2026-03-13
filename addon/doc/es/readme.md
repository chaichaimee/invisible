<div align="center">
  <img src="https://www.nvaccess.org/wp-content/uploads/2015/10/NVDA_logo_standard_transparent.png" alt="NVDA Logo" width="220">
</div>

# Invisible

*Silencia el ruido. Moldea la voz. Domina tu experiencia de navegación.*

**Autor:** Chai Chaimee  
**Repositorio:** [github.com/chaichaimee/invisible](https://github.com/chaichaimee/invisible)

---

## ¿Por qué conformarse con páginas web ruidosas?

Los sitios web modernos están llenos de repeticiones, etiquetas de patrocinio, avisos de cookies, conteos de comentarios, barras laterales y contenido generado automáticamente que los lectores de pantalla deben leer en voz alta — una y otra vez.

**Invisible** te devuelve el control.

Decide exactamente qué palabras, frases o patrones debe omitir NVDA por completo — o reemplazar silenciosamente por algo más corto, limpio o completamente silencioso.

Esto no es solo filtrado. Esto es **curaduría de audio personal** para la web.

## Potente pero elegantemente simple

- Ocultar texto por completo — NVDA actúa como si nunca hubiera existido
- Reemplazar etiquetas molestas con marcadores cortos (“Sponsored · Advertisement” → “skip”)
- Aplicar reglas a una sola página, un dominio completo o patrones URL complejos (regex)
- Soporte completo para expresiones regulares con precisión quirúrgica
- Efecto instantáneo — sin necesidad de recargar la página
- Interfaz sensible al contexto: doble pulsación abre “Añadir sitio” con la URL actual ya rellenada
- Soporte para clic derecho + tecla Supr para gestión rápida
- Archivos .json portátiles por sitio — fáciles de respaldar o compartir

## Comienza en menos de 30 segundos

1. Ve a cualquier página donde NVDA lea algo que quieras silenciar o cambiar.

2. Pulsa **NVDA + Shift + W**  
   - Pulsación simple → abre la ventana principal de gestión  
   - Doble pulsación (rápida) → abre el diálogo “Añadir nuevo sitio” con la URL actual ya insertada

3. En el diálogo **Añadir sitio**:  
   - Mantén o edita el nombre visible  
   - Elige el alcance:  
     - Solo página actual  
     - Toda la web (dominio)  
     - Expresión regular (coincidencia avanzada de URL)  
   - Pulsa **Guardar**

4. Ahora estás en el gestor de reglas del sitio:  
   - Escribe el patrón que deseas afectar  
   - Ingresa texto de reemplazo — o déjalo en blanco para silencio total  
   - Marca “Usar como expresión regular” si es necesario  
   - Pulsa **Añadir** (o **Actualizar** al editar)  
   Los cambios se aplican al instante — regresa a navegar y escuchar.

Puedes volver en cualquier momento con **NVDA+Shift+W** (pulsación simple) para editar, añadir más reglas, eliminar entradas o cambiar entre sitios.

## Ejemplos reales que ahorran tiempo todos los días

| Patrón objetivo             | Reemplazo     | ¿Regex? | Lo que escuchas en su lugar    |
|-----------------------------|---------------|---------|--------------------------------|
| Advertisement               | (en blanco)   | No      | — completamente omitido —      |
| Sponsored                   | skip          | No      | “skip”                         |
| · [0-9,]+ comments?         | (en blanco)   | Sí      | — sin conteos de comentarios — |
| Breaking News:              | News:         | No      | Más corto y limpio             |
| ^Cookie notice.*accept      | (en blanco)   | Sí      | Texto del banner silenciado    |

## Consejos pro para usuarios avanzados

- Clic derecho en cualquier sitio o entrada → menú contextual con Editar / Eliminar
- Pulsa la tecla **Supr** sobre el elemento seleccionado para eliminación instantánea
- Usa coincidencia literal de mayor longitud primero → evita problemas con palabras parciales
- Importa reglas desde otro archivo .json directamente a cualquier sitio
- El modo regex soporta grupos de reemplazo — muy potente para contenido dinámico

## Apoya el proyecto

Si Invisible ha mejorado tu experiencia de navegación diaria, considera apoyar su desarrollo continuo.

[**Donar vía GitHub Sponsors**](https://github.com/chaichaimee)

---

© 2026 Chai Chaimee · Invisible NVDA Add-on · Publicado bajo GNU GPL v2+