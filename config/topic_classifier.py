#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Clasificador de Temas para Comentarios de Campañas
Personalizable por campaña/producto
"""

import re
from typing import Callable

def create_topic_classifier() -> Callable[[str], str]:
    
    def classify_topic(comment: str) -> str:
        # Normalización: minúsculas y quitar espacios extra
        comment_lower = str(comment).lower().strip()
        

        # ---------------------------------------------------------
        # NIVEL 1: ALTA PRIORIDAD (Toxicidad y Odio)
        # ---------------------------------------------------------
        
        # CATEGORÍA 1: Discurso de Odio / Homofobia / Insultos Graves
        # Se añaden: zoofílico, asterisco, gonorrea, hijueputa, perra, etc.
        if re.search(
            r'maric[oa]n?|gay|rosc[oó]n|plumero|locot[aa]|'
            r'rosqueto|pendejo|zoof[ií]lico|degenerado|asterisco|'
            r'hijueputa|hp|gonorrea|perra|mierda|verga|culo|'
            r'nena|marica|maricon', 
            comment_lower
        ):
            return 'Toxicidad y Ataques Personales'

        # CATEGORÍA 2: Crítica al Estilo / Influencer / Xenofobia Regional
        # Se añaden: "sal" (por bajito de sal), "rolo", "juanda" (comparación), "habladito"
        if re.search(
            r'hablad[oi]|tono|voz|rolo|bogotan|tu y te|'
            r'amanerado|nena|plumero|fingido|'
            r'copi[oó]n|juanda|val[ea] verga|'
            r'sal|simpl[oó]n|bajo de sal|'
            r'cringe|fastidio|mamera|cansoneria|bobo|'
            r'payaso|madur[oa]|que le pasa',
            comment_lower
        ):
            return 'Crítica al Influencer/Estilo'

        # ---------------------------------------------------------
        # NIVEL 2: REACCIONES A LA MARCA Y CAMPAÑA
        # ---------------------------------------------------------

        # CATEGORÍA 3: Rechazo Directo a la Marca (Boicot)
        # Se añaden: "alpina", "cliente", "cagaste", "no compro"
        if re.search(
            r'alpina|cliente|no (te )?vuelvo a comprar|te cagaste|'
            r'asco|comercial|propaganda|rid[ií]cul[oa]|'
            r'presupuesto|marketing|publicidad|asco de comercial',
            comment_lower
        ):
            return 'Rechazo a la Campaña/Marca'

        # CATEGORÍA 4: Discusión Religiosa / Navidad
        if re.search(
            r'biblia|dios|jes[uú]s|cristo|satan[aá]s|demonio|'
            r'paganas?|idolatr[ií]a|iglesia|santo|esp[ií]ritu|'
            r'navidad|nacimiento|am[eé]n',
            comment_lower
        ):
            return 'Discusión Religiosa'

        # ---------------------------------------------------------
        # NIVEL 3: INTERÉS Y POSITIVISMO
        # ---------------------------------------------------------

        # CATEGORÍA 5: Interés en Producto / Mascotas
        # Se añaden: "perro", "chucho", "yurt", "donde venden"
        if re.search(
            r'd[oó]nde.*venden|precio|regalo|donde lo|'
            r'perros?|chuchos?|mascotas?|yurt|'
            r'ajonjo|sirve para|gripe|pulmones|'
            r'quiero|comprar|venden',
            comment_lower
        ):
            return 'Interés en Producto/Mascotas'

        # CATEGORÍA 6: Sentimiento Positivo / Apoyo
        if re.search(
            r'lindo|bellezas?|gusta|amo|excelente|me encanta|'
            r'disfr[uú]ta|buen inicio|❤️|😍|🥰|🙏|'
            r'que pases bien|bonito',
            comment_lower
        ):
            return 'Sentimiento Positivo'

        # ---------------------------------------------------------
        # NIVEL 4: RUIDO Y OTROS
        # ---------------------------------------------------------
        
        # CATEGORÍA 7: Ruido / Cortos (Menos de 3 caracteres o palabras sueltas sin contexto)
        if len(comment_lower.split()) < 2 or len(comment_lower) < 3:
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
