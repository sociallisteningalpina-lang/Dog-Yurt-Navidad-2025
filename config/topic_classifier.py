#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Clasificador de Temas para Comentarios de Campañas
Personalizable por campaña/producto
"""
import re
from typing import Callable

def create_topic_classifier() -> Callable[[str], str]:
    """
    Retorna una función de clasificación personalizada para la campaña
    Dog Yurt Navidad 2025 (Alta toxicidad / Enfoque en Influencer).
    """
    
    def classify_topic(comment: str) -> str:
        # Normalización básica
        comment_lower = str(comment).lower()
        
        # ---------------------------------------------------------
        # NIVEL 1: ALTA PRIORIDAD (Detectar Toxicidad y Odio)
        # ---------------------------------------------------------
        
        # CATEGORÍA 1: Discurso de Odio / Homofobia / Insultos de Género
        # (Lamentablemente, este es el grueso de tu muestra actual)
        if re.search(
            r'maric[ao]|gay|rosc[oó]n|plumero|nena|niña|locota|'
            r'amanerado|rosqueto|pendejo|bobo|cloncito|'
            r'cag[aá]|mierda|verga|culo|asterisco|zoof[ií]lico|degenerado|'
            r'gonorrea|hp|hijueputa|maricon',
            comment_lower
        ):
            return 'Toxicidad y Ataques Personales'

        # CATEGORÍA 2: Crítica al Estilo del Influencer / Presentador
        # (Sin ser necesariamente insultos soeces, pero crítica a la forma de hablar/actuar)
        if re.search(
            r'hablad[oi]|tono|voz|actuaci[oó]n|personaje|juanda|copia|'
            r'cringe|fastidio|mamera|cansoneria|bobo|'
            r'rolos?|bogotan|payaso|madur[oa]|que le pasa',
            comment_lower
        ):
            return 'Crítica al Influencer/Estilo'

        # ---------------------------------------------------------
        # NIVEL 2: REACCIONES A LA MARCA Y TEMÁTICA
        # ---------------------------------------------------------

        # CATEGORÍA 3: Sentimiento Negativo hacia la Marca (Boicot/Rechazo)
        if re.search(
            r'alpina|cliente fiel|no (te )?voy a comprar|te cagaste|'
            r'que asco|comercial|propaganda|adi[oó]s|bye|'
            r'presupuesto|marketing|publicidad',
            comment_lower
        ):
            return 'Rechazo a la Campaña'

        # CATEGORÍA 4: Tema Religioso 
        if re.search(
            r'biblia|dios|jes[uú]s|cristo|satan[aá]s|demonio|'
            r'paganas?|idolatr[ií]a|iglesia|santo|esp[ií]ritu|'
            r'navidad.*existe|nacimiento',
            comment_lower
        ):
            return 'Discusión Religiosa'

        # ---------------------------------------------------------
        # NIVEL 3: INTERÉS GENUINO (Lo que realmente vende)
        # ---------------------------------------------------------

        # CATEGORÍA 5: Interés de Compra / Preguntas / Producto
        if re.search(
            r'd[oó]nde.*venden|precio|regalo|participar|'
            r'perros?|chuchos?|mascotas?|yurt|'
            r'sirve para|gripe|pulmones|' # Específico del comentario sobre Ajonjo
            r'quiero|comprar',
            comment_lower
        ):
            return 'Interés en Producto/Mascotas'

        # CATEGORÍA 6: Sentimiento Positivo / Apoyo
        if re.search(
            r'lindo|bellezas?|gusta|amo|excelente|'
            r'disfr[uú]ta|buen inicio|❤️|😍|🥰|'
            r'buena energ[ií]a',
            comment_lower
        ):
            return 'Sentimiento Positivo'

        # ---------------------------------------------------------
        # NIVEL 4: RUIDO
        # ---------------------------------------------------------
        
        # CATEGORÍA 7: Ruido / Spam / Cortos
        if len(comment_lower.split()) < 2:
            return 'Ruido / Cortos'
        
        return 'Otros / Sin Clasificar'
    
    return classify_topic

# ============================================================================
# METADATA DE LA CAMPAÑA (OPCIONAL)
# ============================================================================

CAMPAIGN_METADATA = {
    'campaign_name': 'Alpina - Kéfir',
    'product': 'Kéfir Alpina',
    'categories': [
        'Preguntas sobre el Producto',
        'Comparación con Kéfir Casero/Artesanal',
        'Ingredientes y Salud',
        'Competencia y Disponibilidad',
        'Opinión General del Producto',
        'Fuera de Tema / No Relevante',
        'Otros'
    ],
    'version': '1.0',
    'last_updated': '2025-11-20'
}


def get_campaign_metadata() -> dict:
    """Retorna metadata de la campaña"""
    return CAMPAIGN_METADATA.copy()
