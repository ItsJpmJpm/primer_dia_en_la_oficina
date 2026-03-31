# 📊 Dashboard de Análisis Militar

Una página web interactiva para explorar datos históricos de batallas militares.

## 🚀 Características

- **Dashboard Principal**: Estadísticas generales y visualizaciones en tiempo real
- **Gráficos Interactivos**: 
  - Batallas por guerra (gráfico de barras)
  - Distribución por ubicación (gráfico circular)
- **Tablas Dinámicas**:
  - Búsqueda y filtrado en todas las tablas
  - Paginación automática
  - Ordenamiento por columnas
- **Múltiples Vistas**:
  - **Dashboard**: Resumen y estadísticas
  - **Batallas**: Registro completo de batallas
  - **Beligerantes**: Fuerzas y actores participantes
  - **Comandantes**: Militares destacados
  - **Resumen**: Información sobre los datos cargados

## 📁 Archivos de Datos

El dashboard carga y analiza estos archivos CSV:

- `battles.csv` - 🗡️ Registro de batallas históricas
- `belligerents.csv` - 👥 Beligerantes y fuerzas militares
- `commanders.csv` - 👑 Comandantes militares
- `active_periods.csv` - ⏰ Períodos activos
- `battle_actors.csv` - 🎭 Actores participantes
- `battle_durations.csv` - ⏱️ Duración de batallas
- `battle_dyads.csv` - 🤝 Pares de beligerantes
- `terrain.csv` - 🗺️ Información de terreno
- `weather.csv` - 🌤️ Condiciones climáticas
- `front_widths.csv` - 📏 Ancho de frentes

## 🎯 Cómo Usar

### Opción 1: Usando el Archivo Batch

```batch
iniciar_dashboard.bat
```

Esto abrirá el dashboard en http://localhost:8000

### Opción 2: Línea de Comando Manual

```bash
python -m http.server 8000 --directory .
```

Luego abre tu navegador en: http://localhost:8000/dashboard.html

### Opción 3: Abrir Directamente

Simplemente abre `dashboard.html` en tu navegador web moderno (Chrome, Firefox, Edge, Safari).

## 📊 Visualizaciones

### Dashboard Principal
- Tarjetas de estadísticas con números clave
- Gráfico de barras: Top 10 guerras por número de batallas
- Gráfico circular: Top 10 ubicaciones de batallas

### Tablas Interactivas
- Búsqueda en tiempo real
- Filtrado de datos
- Paginación
- Sorting por cualquier columna
- Exportación de datos (con extensiones adicionales)

## 🔍 Funcionalidades de Búsqueda

En cada pestaña puedes:
1. **Escribir en el campo de búsqueda** para filtrar datos
2. **Hacer clic en "Buscar"** para aplicar el filtro
3. **Hacer clic en "Limpiar"** para restaurar todos los datos
4. **Ordenar por columnas** haciendo clic en los encabezados

## 🌐 Navegadores Compatibles

- ✅ Google Chrome (recomendado)
- ✅ Mozilla Firefox
- ✅ Microsoft Edge
- ✅ Safari
- ✅ Opera

## ⚙️ Requisitos

- Python 3.6+ (para servir los archivos)
- Navegador web moderno
- Los archivos CSV deben estar en la carpeta `archive/`

## 💡 Consejos

- Para mejor experiencia, usa un navegador moderno
- Los datos se cargan desde archivos locales, por lo que funciona sin conexión
- Las tablas pueden mostrar hasta 500 registros inicialmente
- Usa la búsqueda para encontrar batallas, comandantes o beligerantes específicos

## 📝 Notas

- Los gráficos se actualizan automáticamente al cambiar de pestaña
- Las tablas soportan búsqueda multicolumna
- Los datos se cargan en paralelo para mejor rendimiento

## 🎨 Personalización

Para cambiar los colores o estilos, edita el archivo `dashboard.html`:
- Colores principales: `#667eea` y `#764ba2`
- Cambia los estilos CSS en la sección `<style>`

---

**Creado con ❤️ para análisis de datos históricos militares**
