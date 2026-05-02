# Contrato de Prestación de Servicios — Hermes Agent

## 1. Partes

- **Prestador:** Federico Sapuppo, con domicilio en la Alta Gracia, Provincia de Córdoba, República Argentina.
- **Cliente:** ______________________________, con domicilio en ______________________________.

## 2. Descripción del servicio

El Prestador provee al Cliente una instancia gestionada del software open-source *hermes-agent*, desplegada en la plataforma Fly.io. El servicio incluye:

- Una aplicación dedicada en Fly.io con volumen de almacenamiento aislado (single-tenant, sin estado compartido con otros clientes).
- Un bot de Telegram configurado para el Cliente: texto, memos de voz, reportes programados.
- Conectores opcionales según el plan contratado: Gmail / Google Calendar, Outlook / Microsoft 365, búsqueda web, síntesis de voz, generación de imágenes.
- Memoria entre sesiones (el agente aprende las preferencias del Cliente con el tiempo).
- Un prompt de sistema (`SOUL.md`) personalizado al nombre, tono, zona horaria y caso de uso del Cliente.

## 3. Precio

### 3.1 Cargo de instalación (único)

Según la cotización aceptada por el Cliente antes del inicio del servicio. El cargo cubre: provisión de la app en Fly.io, configuración del bot de Telegram, claves de API, personalización del prompt de sistema, y garantía de 30 días (corrección sin cargo de cualquier defecto en lo configurado por el Prestador).

### 3.2 Suscripción mensual

| Plan | Precio (USD/mes) | Incluye |
| --- | --- | --- |
| Base | 50 | Hosting en Fly.io, monitoreo de infraestructura, USD 10 de uso de LLM, Telegram, búsqueda web (tier gratuito), memoria entre sesiones, síntesis de voz Edge TTS, chequeo semanal de salud, 30 min/mes de soporte |
| Pro | 90 | Todo lo del plan Base + conector de email activo, USD 25 de uso de LLM incluido, síntesis de voz ElevenLabs hasta 1 hora/mes, 1 hora/mes de soporte |

### 3.3 Uso incluido y facturación de excedentes

El uso de LLM (OpenRouter) incluido en cada plan se detalla en la tabla anterior. El consumo que exceda el monto incluido se factura al cierre del mes con un recargo de 1.5x sobre el costo real (el recargo cubre la administración y monitoreo de facturación). Otros excedentes (minutos de TTS, plan pago de búsqueda web, tiempo de soporte adicional) se facturan según la tarifa vigente comunicada al Cliente.

## 4. Titularidad de cuentas

- **Cuentas del Prestador:** Fly.io, OpenRouter, Firecrawl, Honcho, Groq, Hugging Face. El Prestador es titular y responsable de estas cuentas. Los costos se trasladan al Cliente a través de la suscripción mensual.
- **Cuentas del Cliente:** Gmail / Google Workspace, Microsoft 365, Telegram (usuario). Los tokens OAuth residen en el volumen dedicado del Cliente; el Prestador no accede a las contraseñas del Cliente.

## 5. Nivel de servicio (SLA)

El Prestador ofrece un servicio de **mejor esfuerzo**. No se garantiza una disponibilidad del 99.9% ni se ofrecen créditos por tiempo de inactividad. El Prestador realizará chequeos semanales de salud y atenderá incidentes reportados dentro del horario de soporte acordado.

## 6. Datos y privacidad

- **Aislamiento:** Cada cliente opera en una aplicación y volumen dedicados en Fly.io. No existe estado compartido entre clientes.
- **Propiedad de datos:** El Cliente es dueño de todos los datos generados en su instancia (sesiones, memorias, configuraciones).
- **Baja del servicio:** Al finalizar el contrato, el Prestador exportará un backup comprimido (`tar.gz`) de los datos del Cliente y lo entregará por medio seguro. Luego, la aplicación y el volumen serán destruidos.

## 7. Limitaciones y exclusiones

El servicio **no incluye**:

- Cuentas multiusuario en una misma instancia. Cada usuario requiere su propio despliegue.
- Cumplimiento de HIPAA, SOC2, PCI u otras certificaciones de seguridad.
- Llamadas telefónicas o agentes de voz en tiempo real.
- Selección de modelo de IA por solicitud individual. El Cliente recibe un modelo por defecto configurable.
- Garantías de residencia de datos más allá de la región de Fly.io elegida en la instalación.
- Migración de datos en formatos distintos al backup `tar.gz` estándar.
- Ingesta de datos regulados (CRM, ERP, datos médicos o financieros sensibles).

## 8. Limitación de responsabilidad

- El Prestador **no es responsable** por el contenido generado por el modelo de lenguaje (LLM). Las respuestas del agente son generadas por modelos de terceros y pueden contener errores.
- El Prestador **no es responsable** por interrupciones causadas por caídas de servicios de terceros (OpenRouter, Fly.io, Groq, Firecrawl, proveedores de email del Cliente).
- El Prestador **no es responsable** por la deprecación o cambio de comportamiento de modelos de IA por parte de sus proveedores.
- La responsabilidad total del Prestador bajo este contrato se limita al monto total pagado por el Cliente en los últimos 3 meses de servicio.

## 9. Plazo y cancelación

- El servicio se contrata **mes a mes** después del pago del cargo de instalación y el primer mes.
- Cualquiera de las partes puede cancelar con **30 días de aviso** por escrito (email es suficiente).
- Al cancelar, se aplica el procedimiento de baja descrito en la sección 6.

## 10. Ley aplicable y jurisdicción

Este contrato se rige por las leyes de la **República Argentina**. Cualquier controversia será sometida a los tribunales ordinarios de la Ciudad de Córdoba.

---

**Prestador:**

Firma: ______________________________

Nombre: Federico Sapuppo

Fecha: ______________________________

**Cliente:**

Firma: ______________________________

Nombre: ______________________________

Fecha: ______________________________
